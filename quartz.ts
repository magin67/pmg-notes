import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import * as ExternalPlugin from "./.quartz/plugins"
import { PMGContentIndex } from "./pmg-content-index"

type ExplorerNode = {
  displayName?: string
  isFolder: boolean
  data: Record<string, unknown> | null
}

type SortablePage = {
  slug?: string
  frontmatter?: {
    order?: unknown
    title?: unknown
  }
}

ExternalPlugin.Explorer({
  sortFn: (a: ExplorerNode, b: ExplorerNode) => {
    if (a.isFolder !== b.isFolder) {
      return a.isFolder ? -1 : 1
    }

    const getOrder = (node: ExplorerNode) => {
      const raw = node.data?.order
      if (typeof raw === "number" && Number.isFinite(raw)) return raw
      if (typeof raw === "string" && raw.trim() !== "") {
        const value = Number(raw)
        if (Number.isFinite(value)) return value
      }
      return Number.POSITIVE_INFINITY
    }

    const orderA = getOrder(a)
    const orderB = getOrder(b)
    if (orderA !== orderB) return orderA - orderB

    return (a.displayName ?? "").localeCompare(b.displayName ?? "", undefined, {
      numeric: true,
      sensitivity: "base",
    })
  },
})

ExternalPlugin.FolderPage({
  sort: (a: SortablePage, b: SortablePage) => {
    const folderA = String(a.slug ?? "").endsWith("/index")
    const folderB = String(b.slug ?? "").endsWith("/index")
    if (folderA !== folderB) return folderA ? -1 : 1

    const rawA = a.frontmatter?.order
    const rawB = b.frontmatter?.order
    const toOrder = (raw: unknown) => {
      if (typeof raw === "number" && Number.isFinite(raw)) return raw
      if (typeof raw === "string" && raw.trim() !== "") {
        const value = Number(raw)
        if (Number.isFinite(value)) return value
      }
      return Number.POSITIVE_INFINITY
    }

    const orderA = toOrder(rawA)
    const orderB = toOrder(rawB)
    if (orderA !== orderB) return orderA - orderB

    const titleA = a.frontmatter?.title ?? a.slug ?? ""
    const titleB = b.frontmatter?.title ?? b.slug ?? ""
    return String(titleA).localeCompare(String(titleB), undefined, {
      numeric: true,
      sensitivity: "base",
    })
  },
})

const config = await loadQuartzConfig()
config.plugins.emitters = config.plugins.emitters.map((emitter) =>
  emitter.name === "ContentIndex" ? PMGContentIndex({ enableSiteMap: true, enableRSS: true }) : emitter,
)

export default config
export const layout = await loadQuartzLayout()
