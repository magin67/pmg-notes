import assert from "node:assert/strict";
import { once } from "node:events";
import { spawn } from "node:child_process";
import { readFileSync } from "node:fs";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { fromHtml } from "hast-util-from-html";

const server = spawn(process.execPath, ["assistant/server.mjs"], {
  env: { ...process.env, PMG_HOST: "127.0.0.1", PMG_PORT: "0" },
  stdio: ["ignore", "pipe", "inherit"],
});
const client = new Client({ name: "pmg-check", version: "0.1.0" });
try {
  const endpoint = await Promise.race([
    once(server.stdout, "data").then(([line]) => String(line).match(/http:\/\/\S+/)[0]),
    once(server, "exit").then(([code]) => { throw new Error(`Server exited: ${code}`); }),
  ]);
  await client.connect(new StreamableHTTPClientTransport(new URL(endpoint)));
  assert.deepEqual((await client.listTools()).tools.map((tool) => tool.name).sort(), ["fetch", "search"]);
  for (const [query, lang, anchor] of [
    ["Оператор метрического распределения", "ru", "оператор-метрического-распределения"],
    ["The metric distribution operator", "en", "the-metric-distribution-operator"],
  ]) {
    const search = await client.callTool({ name: "search", arguments: { query } });
    const hit = search.structuredContent.results.find(({ id }) => id.startsWith(lang + "/") && id.endsWith("#" + anchor));
    assert.ok(hit, query);
    const read = await client.callTool({ name: "fetch", arguments: { id: hit.id } });
    const section = read.structuredContent;
    assert.equal(section.url, hit.url);
    const source = readFileSync(`pmg-library/${section.metadata.source}`, "utf8").replaceAll("\r\n", "\n");
    assert.ok(source.includes(section.text), "fetch preserves the original Markdown");
    assert.match(section.text, /\$\$\n[\s\S]+?\n\$\$/);
    assert.match(section.text, /D_\{?L/);
    const slug = hit.id.split("#")[0];
    const html = fromHtml(readFileSync(`public/${slug}.html`, "utf8"));
    const hasAnchor = (node) => node.properties?.id === anchor || node.children?.some(hasAnchor);
    assert.ok(hasAnchor(html), hit.url);
    console.log(hit.url);
  }
  const searchFormula = async (query) =>
    (await client.callTool({ name: "search", arguments: { query } })).structuredContent.results;
  const formulas = await searchFormula("D_L");
  assert.ok(formulas.length);
  assert.deepEqual(await searchFormula("D_{L}"), formulas);
  assert.deepEqual(await searchFormula("qzxpmgunknownqzx"), []);
  assert.equal((await client.callTool({ name: "fetch", arguments: { id: "missing" } })).isError, true);
} finally {
  try { await client.close(); } finally { server.kill(); }
}
