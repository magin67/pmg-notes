import { execFileSync } from "node:child_process";
import { readFileSync, writeFileSync, renameSync } from "node:fs";
import { resolve, sep } from "node:path";
import { fromHtml } from "hast-util-from-html";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkMath from "remark-math";
import remarkGfm from "remark-gfm";
import { parse as parseYaml } from "yaml";

const parser = unified().use(remarkParse).use(remarkMath).use(remarkGfm);
const [siteDirectory = "public", output = "assistant/pmg-index.json", base =
  "https://magin67.github.io/pmg-notes/"] = process.argv.slice(2);
const library = resolve("pmg-library");
const revision = execFileSync("git", ["rev-parse", "HEAD"], { encoding: "utf8" }).trim();
const catalog = JSON.parse(readFileSync(resolve(siteDirectory, "static/contentIndex.json"), "utf8"));
const sections = [];
let notes = 0;

function* walk(node) {
  yield node;
  for (const child of node.children ?? []) yield* walk(child);
}

function text(node) {
  if (node.tagName === "a" && node.properties?.ariaHidden === "true") return "";
  return node.value ?? (node.children ?? []).map(text).join("");
}

for (const [slug, entry] of Object.entries(catalog)) {
  if (!entry.filePath?.endsWith(".md") || slug.startsWith("tags/")) continue;
  const relative = entry.filePath.replaceAll("\\", "/").replace(/^\.\//, "").replace(/^pmg-library\//, "");
  const source = resolve(library, relative);
  if (!source.startsWith(library + sep)) throw new Error(`Invalid source path: ${relative}`);
  let markdown;
  try {
    markdown = readFileSync(source, "utf8").replaceAll("\r\n", "\n");
  } catch (error) {
    if (error.code === "ENOENT" && slug.endsWith("/index") && relative === `${slug}.md`) continue;
    throw error;
  }
  const frontmatter = markdown.match(/^\uFEFF?---\n([\s\S]*?)\n---(?:\n|$)/);
  const meta = frontmatter ? parseYaml(frontmatter[1]) ?? {} : {};
  const body = markdown.slice(frontmatter?.[0].length ?? 0);
  const ast = parser.parse(body);
  const headings = ast.children.filter((node) => node.type === "heading");
  const html = fromHtml(readFileSync(resolve(siteDirectory, `${slug}.html`), "utf8"));
  const article = [...walk(html)].find((node) => node.tagName === "article");
  if (!article) throw new Error(`Missing article in ${slug}`);
  const anchors = [...walk(article)].filter((node) => /^h[1-6]$/.test(node.tagName) && node.properties.id);
  const comparable = (value) => value.normalize("NFKC").replace(/[^\p{L}\p{N}]+/gu, "").toLowerCase();
  let next = 0;
  const url = new URL(slug.split("/").map(encodeURIComponent).join("/").replace(/(^|\/)index$/, "$1"), base);
  const blocks = [{ offset: 0, title: entry.title, anchor: "" }];
  for (const heading of headings) {
    const headingText = text(heading);
    const expected = comparable(headingText);
    const match = anchors.findIndex((node, i) => i >= next &&
      node.tagName === `h${heading.depth}` &&
      [text(node), node.properties.id].some((value) => comparable(value) === expected));
    if (match < 0) throw new Error(`Unmatched heading in ${slug}: ${headingText}`);
    next = match + 1;
    blocks.push({ offset: heading.position.start.offset, title: headingText, anchor: anchors[match].properties.id });
  }
  const formulas = [...walk(ast)].filter((node) => node.type === "math" || node.type === "inlineMath");
  for (const [i, block] of blocks.entries()) {
    const end = blocks[i + 1]?.offset ?? body.length;
    const content = body.slice(block.offset, end).trim();
    if (!content) continue;
    url.hash = block.anchor;
    sections.push({
      id: `${slug}${block.anchor ? `#${block.anchor}` : ""}`,
      title: block.anchor ? `${entry.title} / ${block.title}` : entry.title,
      url: url.href,
      text: content,
      formulas: formulas.filter((node) => node.position.start.offset >= block.offset &&
        node.position.start.offset < end).map((node) => node.value),
      metadata: {
        source: relative, lang: meta.lang, translation_key: meta.translation_key, revision: meta.revision,
      },
    });
  }
  notes += 1;
}

if (!sections.length) throw new Error("No PMG sections found");
writeFileSync(`${output}.tmp`, JSON.stringify({ revision, sections }));
renameSync(`${output}.tmp`, output);
console.log(`Indexed ${sections.length} sections in ${notes} notes at ${revision}`);
