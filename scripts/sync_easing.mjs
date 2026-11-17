// sync_easing.mjs - keeps the easing code inlined in the example pages identical to easing.mjs.
//   node scripts/sync_easing.mjs          rewrite the block between the markers in every example page
//   node scripts/sync_easing.mjs --check  exit 1 if any page's block differs from the module (used by selftest.py)
// A page marks its copy with   // <easing-inline>   and   // </easing-inline>   on lines of their own.
// The copy is the module text with the word "export" removed, so every name is the module's own name.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const examples = path.join(here, '..', 'examples');
const source = fs.readFileSync(path.join(here, 'easing.mjs'), 'utf8')
  .replace(/\r\n/g, '\n')
  .replace(/^export /gm, '')
  .trimEnd();
const OPEN = '// <easing-inline>';
const CLOSE = '// </easing-inline>';
const block = `${OPEN} (generated from scripts/easing.mjs by scripts/sync_easing.mjs: do not edit by hand)\n${source}\n${CLOSE}`;
const re = new RegExp(`${OPEN.replace(/[/<>]/g, '\\$&')}[\\s\\S]*?${CLOSE.replace(/[/<>]/g, '\\$&')}`);

const pages = [];
(function walk(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p); else if (e.name.endsWith('.html')) pages.push(p);
  }
})(examples);

const check = process.argv.includes('--check');
let bad = 0, used = 0;
for (const p of pages) {
  const text = fs.readFileSync(p, 'utf8');
  const nl = text.includes('\r\n') ? '\r\n' : '\n';
  const norm = text.replace(/\r\n/g, '\n');
  if (!re.test(norm)) continue;
  used++;
  const next = norm.replace(re, () => block);
  if (next !== norm) {
    if (check) { console.error('DRIFT: ' + path.relative(examples, p)); bad++; }
    else fs.writeFileSync(p, nl === '\r\n' ? next.replace(/\n/g, '\r\n') : next);
  }
}
if (used === 0) { console.error('no example page carries the markers'); process.exit(1); }
if (check && bad) process.exit(1);
console.log(check ? `easing copy in ${used} page(s) matches easing.mjs` : `synced ${used} page(s)`);
