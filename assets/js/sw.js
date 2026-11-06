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
// Kill switch, if this ever goes wrong: replace this file with one that deletes all
// caches and calls self.registration.unregister(), then deploy.
{{- $pages := slice }}
{{- range site.Pages }}{{ $pages = $pages | append .RelPermalink }}{{ end }}
{{- $assets := slice ("fonts/inter/InterVariable.woff2" | relURL) }}

const VERSION = {{ now.UnixMilli | string }};
const CACHE = "site-" + VERSION;
// Pages are fetched from the server. The font may come from the HTTP cache:
// it was usually just downloaded for the first page, and it practically never changes.
const PAGES = {{ $pages | uniq | jsonify | safeJS }};
const ASSETS = {{ $assets | jsonify | safeJS }};

// Keeps only plain, complete, same-origin answers. Safari refuses redirected
// responses for navigations, so those are never stored.
const store = (cache, key, response) => {
  if (response.ok && response.type === "basic" && !response.redirected) {
    return cache.put(key, response);
  }
};

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => cache.addAll([
        ...PAGES.map((url) => new Request(url, { cache: "reload" })),
        ...ASSETS,
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

  // One copy per page: the key is the address without query string.
  const url = new URL(request.url);
  url.search = "";
  const key = url.href;

  event.respondWith(caches.open(CACHE).then(async (cache) => {
    const cached = await cache.match(key, { ignoreVary: true });
    if (cached) {
      // "no-cache": ask the server (a cheap conditional request), not the HTTP cache.
      event.waitUntil(
        fetch(key, { cache: "no-cache" })
          .then((response) => store(cache, key, response))
          .catch(() => {})
      );
      return cached;
    }
    const response = await fetch(request);
    event.waitUntil(Promise.resolve(store(cache, key, response.clone())));
    return response;
  }));
});
