#!/usr/bin/env node
// Checks the vertical rhythm of the site in a real browser (headless Chrome).
// See DECISIONS.md, "Grundlinienraster".
//
// For every page reachable from the home page and every width in WIDTHS:
// 1. Baselines: every element with its own text has its first baseline at the same
//    height in the grid of half lines (0.5rlh). The reference is the first paragraph
//    of running text. Fails if any baseline is off by more than the tolerance:
//    0.25 px at the normal text size. With the text size at 200 % the tolerance is
//    1 px: browsers round font metrics to whole pixels, and Inter 18 px and
//    Crimson Pro 21 px differ by 0.6 px before rounding (1.2 px at double size).
//    At normal size both round to the same pixel.
//    Text in code blocks gets 2 px: it is set in the system's monospace font
//    (SF Mono, Consolas, ...), whose metrics differ by operating system.
// 2. Heights: every block with its own text whose line height is on the grid is a
//    whole number of half lines tall, so nothing below it leaves the grid (an inline
//    element in another font or a superscript can stretch a line). Elements with a
//    smaller line height on purpose (the numbers in project lists) are skipped.
// 3. Blocks in running text (figures, lists, quotations, code) are a whole number of
//    half lines tall, so an image cannot push the text below it off the grid.
// 4. No horizontal scrolling.
//
// Usage: node tools/raster-check.mjs [base URL] [extra paths...]
//   Default base URL http://localhost:1313 (hugo server). Pages not linked from the
//   site, such as /projects/layout-test/, can be added as extra paths.
// Needs Node 22 or newer and Google Chrome; set CHROME to its path if it is not in the
// default macOS location. Exit code 0 when everything sits, 1 otherwise.
import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const BASE = (process.argv[2] || 'http://localhost:1313').replace(/\/$/, '');
const EXTRA = process.argv.slice(3);
// Widths, plus the widest one with the browser's text size at 200 % (default font 32 px).
const VIEWS = [{ width: 320 }, { width: 375 }, { width: 768 }, { width: 1440 }, { width: 1440, font: 32, tolerance: 1 }];
const MAX_PAGES = 40;
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = 9400 + Math.floor(Math.random() * 400);

const profile = mkdtempSync(join(tmpdir(), 'raster-check-'));
const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
  '--no-first-run', '--no-default-browser-check', '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const quit = (code) => { chrome.kill(); try { rmSync(profile, { recursive: true, force: true }); } catch {} process.exit(code); };

let target;
for (let i = 0; i < 50 && !target; i++) {
  await sleep(200);
  try { target = (await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json()).find((t) => t.type === 'page'); } catch {}
}
if (!target) { console.error('Chrome did not start (set CHROME to its path)'); quit(1); }
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener('open', r));
let id = 0; const pending = new Map(); const waiters = [];
ws.addEventListener('message', (e) => {
  const m = JSON.parse(e.data);
  if (m.id && pending.has(m.id)) { const p = pending.get(m.id); pending.delete(m.id); m.error ? p.rej(new Error(JSON.stringify(m.error))) : p.res(m.result); }
  if (m.method) waiters.filter((w) => w.method === m.method).forEach((w) => { waiters.splice(waiters.indexOf(w), 1); w.res(m.params); });
});
const send = (method, params = {}) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); });
const once = (method) => new Promise((res) => waiters.push({ method, res }));
const evaluate = async (expr) => (await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true })).result.value;
await send('Page.enable');
await send('Runtime.enable');

async function open(url, width, font = 16) {
  await send('Page.setFontSizes', { fontSizes: { standard: font, fixed: Math.round(font * 13 / 16) } });
  await send('Emulation.setDeviceMetricsOverride', { width, height: 900, deviceScaleFactor: 1, mobile: width < 600 });
  const loaded = once('Page.loadEventFired');
  await send('Page.navigate', { url });
  await loaded;
  await evaluate('document.fonts.ready.then(() => true)');
}

// Runs in the page. Returns the measurements.
const MEASURE = `(() => {
  const L = parseFloat(getComputedStyle(document.documentElement).lineHeight);
  const G = L / 2;
  const top0 = document.documentElement.getBoundingClientRect().top;
  const name = (el) => el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\\s+/).join('.') : '');
  const items = [];
  for (const el of document.body.querySelectorAll('*')) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || el.closest('.skip-link')) continue;
    if (/flex|grid/.test(cs.display)) continue; // text directly in a grid or flex box is an anonymous item
    const text = [...el.childNodes].find((n) => n.nodeType === 3 && n.textContent.trim());
    if (!text) continue;
    const marker = document.createElement('span');
    marker.style.cssText = 'display:inline-block;width:0;height:0;vertical-align:baseline';
    el.insertBefore(marker, text);
    const baseline = marker.getBoundingClientRect().top - top0;
    marker.remove();
    const r = el.getBoundingClientRect();
    const lh = parseFloat(cs.lineHeight);
    const onGrid = Math.abs(lh / G - Math.round(lh / G)) < 0.001 && lh >= G;
    const block = /^(block|list-item)$/.test(cs.display) && onGrid;
    items.push({ el: name(el), font: cs.fontFamily.split(',')[0].replace(/"/g, ''), size: parseFloat(cs.fontSize),
      phase: ((baseline % G) + G) % G, mono: !!el.closest('pre'), height: block ? r.height : null, prose: !!el.closest('.prose') && el.tagName === 'P' });
  }
  const blocks = [...document.querySelectorAll('.prose > *')].map((el) => ({ el: name(el), height: el.getBoundingClientRect().height }));
  return { L, G, items, blocks, overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth };
})()`;

// Collect pages: everything on the same site linked from the home page and from those pages.
const pages = ['/', ...EXTRA];
for (let i = 0; i < pages.length && pages.length < MAX_PAGES; i++) {
  await open(BASE + pages[i], 1440);
  const links = await evaluate(`[...document.querySelectorAll('a[href]')].map((a) => new URL(a.href, location.href)).filter((u) => u.origin === location.origin && !u.hash && !/\\.(html|xml|txt|woff2)$/.test(u.pathname)).map((u) => u.pathname)`);
  for (const l of links) if (!pages.includes(l)) pages.push(l);
}

let failures = 0;
const fail = (msg) => { failures++; console.log('  FAIL ' + msg); };
for (const view of VIEWS) {
  for (const page of pages) {
    await open(BASE + page, view.width, view.font);
    const m = await evaluate(MEASURE);
    const ref = (m.items.find((i) => i.prose) || m.items[0]);
    const where = `${page} @${view.width}px${view.font ? ', text ' + view.font / 16 * 100 + ' %' : ''}`;
    const before = failures;
    if (!ref) { fail(`${where}: no text found`); continue; }
    for (const i of m.items) {
      let d = Math.abs(i.phase - ref.phase); d = Math.min(d, m.G - d);
      if (d > Math.max(view.tolerance || 0.25, i.mono ? 2 : 0) + 1e-6) fail(`${where}: baseline of ${i.el} (${i.font} ${i.size}px) is ${(i.phase - ref.phase).toFixed(2)}px off the grid`);
      if (i.height !== null) {
        const rest = i.height % m.G;
        if (Math.min(rest, m.G - rest) > 0.01) fail(`${where}: ${i.el} is ${i.height.toFixed(2)}px tall, not a multiple of ${m.G}px`);
      }
    }
    for (const b of m.blocks) {
      const rest = b.height % m.G;
      if (Math.min(rest, m.G - rest) > 0.01) fail(`${where}: block ${b.el} is ${b.height.toFixed(2)}px tall, not a multiple of ${m.G}px`);
    }
    if (m.overflow > 0) fail(`${where}: scrolls sideways by ${m.overflow}px`);
    console.log(`${failures === before ? 'ok  ' : 'FAIL'} ${where}: ${m.items.length} texts`);
  }
}
console.log(failures ? `\n${failures} problem(s) found.` : `\nAll baselines on the grid: ${pages.length} pages, ${VIEWS.length} views.`);
ws.close();
quit(failures ? 1 : 0);
