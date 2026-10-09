import fs from "node:fs/promises"
import path from "node:path"
import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { componentRegistry } from "./quartz/components/registry"
import type { QuartzEmitterPluginInstance } from "./quartz/plugins/types"
import type { ProcessedContent, QuartzPluginData } from "./quartz/plugins/vfile"
import type { FilePath } from "./quartz/util/path"

// Accept both YAML numbers (order: 3) and numeric strings (order: "3").
function readingOrder(value: unknown): number | undefined {
  if (typeof value !== "number" && typeof value !== "string") return undefined
  if (typeof value === "string" && value.trim() === "") return undefined
  const number = Number(value)
  return Number.isFinite(number) ? number : undefined
}

// Folder pages: folders first, then order ascending, then title.
function sortPages(a: QuartzPluginData, b: QuartzPluginData): number {
  const aFolder = a.slug === "index" || (a.slug ?? "").endsWith("/index")
  const bFolder = b.slug === "index" || (b.slug ?? "").endsWith("/index")
  if (aFolder !== bFolder) return aFolder ? -1 : 1

  const aOrder = readingOrder(a.frontmatter?.order) ?? Infinity
  const bOrder = readingOrder(b.frontmatter?.order) ?? Infinity
  if (aOrder !== bOrder) return aOrder < bOrder ? -1 : 1

  return (a.frontmatter?.title ?? "").localeCompare(b.frontmatter?.title ?? "", undefined, {
    numeric: true,
    sensitivity: "base",
  })
}

interface ExplorerNode {
  isFolder: boolean
  displayName?: string
  data: { order?: number } | null
}

// Quartz serializes this function for the browser. Keep it self-contained:
// no references to readingOrder or other variables outside the function.
function sortExplorer(a: ExplorerNode, b: ExplorerNode): number {
  if (a.isFolder !== b.isFolder) return a.isFolder ? -1 : 1

  const aOrder = a.data?.order ?? Infinity
  const bOrder = b.data?.order ?? Infinity
  if (aOrder !== bOrder) return aOrder < bOrder ? -1 : 1

  return (a.displayName ?? "").localeCompare(b.displayName ?? "", undefined, {
    numeric: true,
    sensitivity: "base",
  })
}

// Register overrides before the YAML loader instantiates plugins and layouts.
componentRegistry.setOptionOverrides("@quartz-community/folder-page", { sort: sortPages })
componentRegistry.setOptionOverrides("@quartz-community/explorer", { sortFn: sortExplorer })

const config = await loadQuartzConfig()

// Explorer reads static/contentIndex.json, which normally omits custom YAML
// properties. Extend the existing index with just the numeric order field.
// Retain the standard index, RSS, sitemap, and publication filters.
async function addReadingOrder(
  files: FilePath[],
  content: ProcessedContent[],
): Promise<FilePath[]> {
  const indexPath = files.find(
    (file) =>
      path.basename(file) === "contentIndex.json" && path.basename(path.dirname(file)) === "static",
  )
  if (!indexPath) throw new Error("PMG sorting: ContentIndex did not emit static/contentIndex.json")

  const index = JSON.parse(await fs.readFile(indexPath, "utf8")) as Record<
    string,
    Record<string, unknown>
  >
  for (const [, file] of content) {
    const slug = file.data.slug
    if (!slug || !Object.hasOwn(index, slug)) continue
    const order = readingOrder(file.data.frontmatter?.order)
    if (order === undefined) delete index[slug].order
    else index[slug].order = order
  }
  await fs.writeFile(indexPath, JSON.stringify(index), "utf8")
  return files
}

async function collectFiles(
  result: ReturnType<QuartzEmitterPluginInstance["emit"]>,
): Promise<FilePath[]> {
  const files: FilePath[] = []
  for await (const file of await result) files.push(file)
  return files
}

const contentIndex = config.plugins.emitters.find((plugin) => plugin.name === "ContentIndex")
if (!contentIndex) throw new Error("PMG sorting requires the ContentIndex plugin")

const originalEmit = contentIndex.emit.bind(contentIndex)
contentIndex.emit = async (ctx, content, resources) =>
  addReadingOrder(await collectFiles(originalEmit(ctx, content, resources)), content)

// Also update order when Quartz rebuilds incrementally with --serve.
if (contentIndex.partialEmit) {
  const originalPartialEmit = contentIndex.partialEmit.bind(contentIndex)
  contentIndex.partialEmit = (ctx, content, resources, changes) => {
    const result = originalPartialEmit(ctx, content, resources, changes)
    if (result === null) return null
    return collectFiles(result).then((files) => addReadingOrder(files, content))
  }
}

export default config
export const layout = await loadQuartzLayout()
