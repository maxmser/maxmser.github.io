# maxmser.github.io

Personal project site of Max Moser. It shows selected projects: the problem, the decisions, the outcome and what I learned. There is no blog.

Built with [Hugo](https://gohugo.io/) (extended, version pinned in `.github/workflows/hugo.yaml`) and custom minimal layouts. No framework: the only JavaScript is a small service worker that keeps a local copy of the pages, so clicks open without waiting for the server. No external requests, no cookies, no analytics.

## Build locally

Requirements: Hugo extended in the version pinned in the workflow (`brew install hugo`).

```sh
hugo server          # preview at http://localhost:1313/
hugo build --gc --minify   # writes the site to ./public
```

Under `hugo server` there is no service worker, so edits show up at once. The published build registers it.

Every page is built twice: `index.html` with the fonts inline for a first visit, and `lean.html` with the fonts as files, which the service worker serves on later visits.

## Check the vertical rhythm

Every baseline on every page sits on a grid of half lines (13.5 px). With `hugo server` running:

```sh
node tools/raster-check.mjs http://localhost:1313 /projects/layout-test/   # needs Node 22+ and Google Chrome; exit code 1 if anything is off the grid
```

Run it after any change to font sizes, line heights or fonts. If it fails, measure again and adjust `--snap-small` and `--snap-display` in `assets/css/main.css` (see DECISIONS.md, "Grundlinienraster").

## Change the fonts

Two fonts: Inter for titles, navigation and labels, Crimson Pro for introductions and running text. Edit `data/font.toml` (characters, features, weights; the table `[serif]` is Crimson Pro), then run `python3 tools/build-fonts.py` (needs fontTools and brotli). The same settings always give the same files.

## Add a project

```sh
hugo new content projects/<slug>/index.md
```

The archetype in `archetypes/projects.md` creates the front matter and the four sections. Images go into the project folder next to `index.md` and into the text as `![Alt text](file.jpg "Caption")`; Hugo makes WebP versions in several widths.

`/projects/layout-test/` is a test page with sample text and images that shows every element of running text. It is built but not listed anywhere.

## Publish

Every push to `main` builds and deploys the site to GitHub Pages via GitHub Actions (`.github/workflows/hugo.yaml`). In the repository settings, the Pages source must be set to "GitHub Actions".

## Structure

- `hugo.toml`: site configuration
- `content/`: pages (home, projects, imprint)
- `layouts/`: templates (`baseof`, `home`, `list`, `single`, `text`, partials)
- `assets/css/main.css`: the only stylesheet, inlined into every page at build time
- `assets/js/sw.js`: the service worker (a Hugo template, published as `/sw.js`). Kill switch: see DECISIONS.md
- `data/font.toml`: characters and OpenType features of the web fonts. The build stops if a page uses a character its font lacks
- `tools/build-fonts.py`: builds `static/fonts/` from the full fonts in `tools/fonts-src/` with the settings in `data/font.toml`
- `tools/raster-check.mjs`: checks in Chrome that every baseline sits on the grid
- `static/fonts/inter/`: Inter Display, subset to English and German and weights 400 to 500, with its license
- `static/fonts/crimson/`: Crimson Pro, subset the same way, with its license
- `i18n/`: interface strings, prepared for a later German version
- `design/`: the static design draft of 2026-11-06 and the font specimen (`python3 design/schriftmuster/build.py`), not published
- `DECISIONS.md`: decisions and open points (in German)
