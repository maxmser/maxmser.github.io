// Service worker: answers clicks from a local copy of the site, so a page
// appears without waiting for the server. See DECISIONS.md, "Vorladen von Seiten".
// This file is a Hugo template; the page list and the version are filled in at build time.
//
// Freshness:
// - VERSION changes with every build. The browser checks sw.js on every page load,
//   bypassing the HTTP cache, installs the new version and deletes the old copy.
// - Stale-while-revalidate: a page comes from the copy at once, and the server is
//   asked in the background whether it changed, for the next visit.
// - Both go to the server, not to the browser's HTTP cache (GitHub Pages allows
//   10 minutes there), so a new version is never filled with old pages.
// - The fonts are not checked on every page: they only change with a deploy.
// Kill switch, if this ever goes wrong: replace this file with one that deletes all
// caches and calls self.registration.unregister(), then deploy.
//
// Pages exist twice (see baseof.html): index.html carries the font inline for a
// first visit, lean.html links the font file. This worker stores the lean
// rendering under the normal address, so every later visit gets the small page
// and the font from the local copy.
{{- $pages := slice }}
{{- range site.Pages }}
  {{- $lean := .OutputFormats.Get "lean" }}
  {{- if $lean }}{{ $pages = $pages | append .RelPermalink $lean.RelPermalink }}{{ end }}
{{- end }}
{{- $assets := slice ("fonts/geist/Geist.woff2" | relURL) ("fonts/crimson/CrimsonPro.woff2" | relURL) }}

const VERSION = {{ now.UnixMilli | string }};
const CACHE = "site-" + VERSION;
// Page address and the address of its lean rendering, as a flat list of pairs.
const PAIRS = {{ $pages | jsonify | safeJS }};
const PAGES = new Map();
for (let i = 0; i < PAIRS.length; i += 2) {
  PAGES.set(new URL(PAIRS[i], location.href).href, new URL(PAIRS[i + 1], location.href).href);
}
// Files that only change with a deploy, and a deploy brings a new VERSION anyway.
const ASSETS = {{ $assets | jsonify | safeJS }}.map((url) => new URL(url, location.href).href);

// Keeps only plain, complete, same-origin answers. Safari refuses redirected
// responses for navigations, so those are never stored.
const store = (cache, key, response) => {
  if (response.ok && response.type === "basic" && !response.redirected) {
    return cache.put(key, response);
  }
};

// Fetches a file from the server, not from the browser's HTTP cache, and stores it under key.
const refresh = (cache, key, url) =>
  fetch(url, { cache: "no-cache" }).then((response) => store(cache, key, response));

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => Promise.all([
        ...[...PAGES].map(([page, lean]) =>
          fetch(lean, { cache: "reload" }).then((response) => {
            if (!response.ok) throw new Error("precache failed: " + lean);
            return store(cache, page, response);
          })),
        ...ASSETS.map((url) =>
          fetch(url, { cache: "reload" }).then((response) => {
            if (!response.ok) throw new Error("precache failed: " + url);
            return store(cache, url, response);
          })),
      ]))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((key) => key !== CACHE).map((key) => caches.delete(key))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET" || new URL(request.url).origin !== location.origin) return;

  // One copy per address: the key is the address without query string.
  const url = new URL(request.url);
  url.search = "";
  const key = url.href;
  const lean = PAGES.get(key);

  event.respondWith(caches.open(CACHE).then(async (cache) => {
    const cached = await cache.match(key, { ignoreVary: true });
    if (cached) {
      // Assets are only replaced with a new VERSION. Everything else is checked
      // in the background with a cheap conditional request, for the next visit.
      if (!ASSETS.includes(key)) {
        event.waitUntil(refresh(cache, key, lean || key).catch(() => {}));
      }
      return cached;
    }
    const response = await fetch(request);
    // For a page, store the lean rendering instead of the one with the inline font.
    event.waitUntil(Promise.resolve(lean ? refresh(cache, key, lean) : store(cache, key, response.clone())).catch(() => {}));
    return response;
  }));
});
