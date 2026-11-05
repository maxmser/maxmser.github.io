# maxmser.github.io

Personal project site of Max Moser. It shows selected projects: the problem, the decisions, the outcome and what I learned. There is no blog.

Built with [Hugo](https://gohugo.io/) (extended, version pinned in `.github/workflows/hugo.yaml`) and custom minimal layouts. No JavaScript, no external requests, no cookies, no analytics.

## Build locally

Requirements: Hugo extended in the version pinned in the workflow (`brew install hugo`).

```sh
hugo server          # preview at http://localhost:1313/
hugo build --gc --minify   # writes the site to ./public
```

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
- `assets/css/main.css`: the only stylesheet
- `i18n/`: interface strings, prepared for a later German version
- `DECISIONS.md`: decisions and open points (in German)
