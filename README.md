# Data Systems Design Handbook

HLD and LLD concepts for data engineering and analytics, in simple terms.

**Read it online:** https://seeralikhith.github.io/Data_System_Design/

The handbook explains how to design a data system, from the first questions to working pipelines. Each chapter gives the idea in one line, an everyday comparison, a diagram and one thing to remember. You need no system design experience, and basic SQL is enough.

## The series

The handbook is released in four parts. Watch this repository (Watch → Custom → Releases) to hear when the next part is out.

| Release | Part | Chapters | Status |
| --- | --- | --- | --- |
| v0.1.0 | Part 1: Foundations | 1 to 2 | Released |
| v0.2.0 | Part 2: High-level design (HLD) | 3 to 14 | Released |
| v0.3.0 | Part 3: Low-level design (LLD) | 15 to 27 | Released |
| v1.0.0 | Part 4: Putting it together | 28 to 30 | Released |

## How the project is laid out

```text
docs/                  The chapters, one Markdown file each, grouped by part
docs/assets/diagrams/  Rendered diagrams: a -light.svg and a -dark.svg for each
diagrams/src/          Diagram sources, one small React component per diagram
diagrams/render.mjs    Turns the sources into the SVG files
series.yml             The parts, in order, and which ones are released
hooks/series.py        Builds the navigation and leaves unreleased parts out
release-notes/         The text for each GitHub release
mkdocs.yml             Site settings (MkDocs with the Material theme)
```

## Work on it locally

You need Python 3.12 or later. Node.js 20 or later is only needed if you change a diagram.

Set up once:

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
```

On macOS or Linux, use `.venv/bin/python` instead of `.venv/Scripts/python`.

Preview the site as readers will see it, then open http://127.0.0.1:8000:

```bash
.venv/Scripts/python -m mkdocs serve
```

Preview every part, including unreleased ones (in PowerShell, run `$env:PREVIEW_ALL = "1"` first instead):

```bash
PREVIEW_ALL=1 .venv/Scripts/python -m mkdocs serve
```

Check the site builds with no broken links or missing images:

```bash
.venv/Scripts/python -m mkdocs build --strict
```

## Change a diagram

Diagrams are written as code so they stay sharp and match the light and dark themes. Edit the file in `diagrams/src/`, for example `diagrams/src/04-1.jsx`, then render it:

```bash
npm install
npm run diagrams
```

To render only some diagrams, pass the start of their names, for example `npm run diagrams -- 04-1`. Commit the source and the two SVG files together.

Colours are theme tokens such as `var(--cds-text-primary)`. `diagrams/render.mjs` lists the light and dark colour for each token.

## Publish

Every push to `main` rebuilds the site and publishes it to GitHub Pages, using `.github/workflows/deploy.yml`. Only the parts marked `released: true` in `series.yml` are published.

To release the next part, follow [RELEASING.md](RELEASING.md).
