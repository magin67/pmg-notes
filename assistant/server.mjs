import { createServer } from "node:http";
import { readFileSync } from "node:fs";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { z } from "zod";

const index = JSON.parse(readFileSync(process.argv[2] ?? "assistant/pmg-index.json", "utf8"));
const sections = new Map(index.sections.map((section) => [section.id, section]));
if (!sections.size || sections.size !== index.sections.length) throw new Error("Invalid PMG index");

function normalize(text) {
  return text.normalize("NFKC").toLowerCase().replaceAll("ё", "е")
    .replace(/([_^])\s*\{\s*([\p{L}\p{N}]+)\s*\}/gu, "$1$2")
    .replace(/\s+/g, " ").trim();
}

function tokens(text) {
  return text.match(/[\p{L}\p{N}]+(?:[_^][\p{L}\p{N}]+)*/gu) ?? [];
}

const documents = [...sections.values()].map((section) => ({
  section,
  title: normalize(section.title),
  titleWords: new Set(tokens(normalize(section.title))),
  words: new Set(tokens(normalize(section.text))),
  symbols: new Set(section.formulas.flatMap((formula) => tokens(normalize(formula)))),
}));

function search(query) {
  const phrase = normalize(query);
  const terms = [...new Set(tokens(phrase))];
  if (!terms.length) return { results: [] };
  const language = /\p{Script=Cyrillic}/u.test(query) ? "ru" : /[a-z]{3}/i.test(query) ? "en" : null;
  const results = documents.map(({ section, title, titleWords, words, symbols }) => {
    let score = terms.reduce((sum, term) => sum + (titleWords.has(term) ? 5 : 0) +
      (symbols.has(term) ? 4 : 0) + (words.has(term) ? 1 : 0), 0);
    if (score && title.includes(phrase)) score += 10;
    if (score && section.metadata.lang === language) score *= 1.25;
    return { section, score };
  }).filter(({ score }) => score > 0).sort((a, b) => b.score - a.score).slice(0, 8)
    .map(({ section: { id, title, url } }) => ({ id, title, url }));
  return { results };
}

function result(structuredContent) {
  return { structuredContent, content: [{ type: "text", text: JSON.stringify(structuredContent) }] };
}

function createMcpServer() {
  const server = new McpServer({ name: "pmg-assistant", version: "0.1.0" }, {
    instructions: "Search published PMG notes in Russian and English. Fetch sections before citing them. " +
      "Check assumptions and distinguish published proofs, examples, computational checks, " +
      "your own derivations and conjectures. Say when the available sources do not establish an answer.",
  });
  const readOnly = { readOnlyHint: true, openWorldHint: false };
  server.registerTool("search", {
    title: "Search PMG",
    description: "Find published PMG sections by Russian or English terms, headings and LaTeX notation.",
    inputSchema: { query: z.string().max(1000) },
    annotations: readOnly,
  }, ({ query }) => result(search(query)));
  server.registerTool("fetch", {
    title: "Read PMG section",
    description: "Read a section returned by search, with source Markdown, LaTeX and a citation URL.",
    inputSchema: { id: z.string().min(1).max(2000) },
    annotations: readOnly,
  }, ({ id }) => {
    const section = sections.get(id);
    if (!section) return { isError: true, content: [{ type: "text", text: "PMG section not found." }] };
    const { title, url, text, metadata } = section;
    return result({ id, title, url, text, metadata: { ...metadata, commit: index.revision } });
  });
  return server;
}

const host = process.env.PMG_HOST ?? "127.0.0.1";
const port = Number(process.env.PMG_PORT ?? 3000);
const http = createServer(async (request, response) => {
  if (request.url !== "/mcp") return response.writeHead(404).end();
  if (request.headers.origin) return response.writeHead(403).end();
  if (request.method !== "POST") return response.writeHead(405, { Allow: "POST" }).end();
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: undefined,
    enableJsonResponse: true,
  });
  const server = createMcpServer();
  response.once("close", () => void server.close());
  try {
    await server.connect(transport);
    await transport.handleRequest(request, response);
  } catch (error) {
    console.error(error);
    if (!response.headersSent) response.writeHead(500);
    response.end();
  }
});
http.listen(port, host, () => console.log(`PMG MCP listening on http://${host}:${http.address().port}/mcp`));
