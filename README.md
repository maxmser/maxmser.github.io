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

Every page is built twice: `index.html` with the font inline for a first visit, and `lean.html` with the font as a file, which the service worker serves on later visits.

## Change the font

Edit `data/font.toml` (characters, features, weights), then run `python3 tools/build-fonts.py` (needs fontTools and brotli).

## Add a project

```sh
hugo new content projects/<slug>/index.md
```

The archetype in `archetypes/projects.md` creates the front matter and the four sections.

## Publish

Every push to `main` builds and deploys the site to GitHub Pages via GitHub Actions (`.github/workflows/hugo.yaml`). In the repository settings, the Pages source must be set to "GitHub Actions".

## Structure

- `hugo.toml`: site configuration
- `content/`: pages (home, projects, imprint)
- `layouts/`: templates (`baseof`, `home`, `list`, `single`, `text`, partials)
- `assets/css/main.css`: the only stylesheet, inlined into every page at build time
- `assets/js/sw.js`: the service worker (a Hugo template, published as `/sw.js`). Kill switch: see DECISIONS.md
- `data/font.toml`: characters and OpenType features of the web font. The build stops if a page uses a character outside this set
- `tools/build-fonts.py`: builds `static/fonts/inter/` from the full fonts in `tools/fonts-src/` with the settings in `data/font.toml`
- `static/fonts/inter/`: Inter Display, subset to English and German and weights 400 to 500, with its license
- `i18n/`: interface strings, prepared for a later German version
- `design/`: the static design draft of 2026-11-06 and the font specimen (`python3 design/schriftmuster/build.py`), not published
- `DECISIONS.md`: decisions and open points (in German)
