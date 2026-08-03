---
name: meta-docs-map
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  project to authoritative documentation entry points from the published
  index at https://ryan-minato.github.io/meta-skills/ — detect the
  target's stack, fetch the index's llms.txt, select domain pages by
  tag, and record where the docs live. Use when a harness build must
  record documentation entry points for the tools a target project uses.
  Not for choosing between tools or recommending one, and not for tools
  no index page covers.
---

# Documentation Map

This skill produces the documentation entry points a harness build
records, drawn from a published index of domain pages rather than
memory. It expects a harness build in progress and access to the
target's dependency manifests. Per-tool content is one line plus a URL
fetched from the index at use time — and nothing recorded is a
recommendation: when the target lacks a tool for a need, the choice is
the user's.

## Workflow

1. Detect the stack: dependency manifests, imports, configuration
   files, data-file extensions, and Dockerfiles. Derive candidate
   domains from what is actually there (`geopandas` → geospatial,
   `torch` plus `transformers` → training and the Hugging Face
   ecosystem, GeoTIFFs → raster data).
2. Fetch `https://ryan-minato.github.io/meta-skills/llms.txt`. It lists
   every page with its description first, then one section per tag
   listing the pages that carry it.
3. Match the detected domains to tags and select pages from the tag
   sections, falling back to the descriptions in the full listing. If
   nothing matches the target's stack, record nothing and stop — this
   skill only covers what the index covers.
4. Fetch each selected page (plain markdown at the listed URL). Its
   intro states which targets it serves; its tables map tools to
   documentation entry points; its Gotchas carry domain-specific traps
   worth keeping.
5. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then the site's `llms.txt` (the
   index pages note one where it exists). Fall back to `llms-full.txt`
   only when neither exists, and never read it whole — search it
   programmatically.
6. Record each tool the target actually uses — name, one-line role,
   documentation entry point, and its llms.txt when present — wherever
   the harness keeps conventions, together with the applicable gotchas
   from the pages.

Done when: every tool the target actually uses that an index page
covers has a recorded, live documentation entry point, and nothing
recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: stack selection is the user's
  decision.
- Record once per harness: a tool detected through several domains
  still gets one entry.
- If the index site is unreachable, fetch the same content raw:
  `https://api.github.com/repos/ryan-minato/meta-skills/contents/docs`
  lists the pages, and each one serves at
  `https://raw.githubusercontent.com/ryan-minato/meta-skills/main/docs/<page>.md`.
  If that is unreachable too, record nothing and leave a dated TODO in
  the harness — never write documentation URLs from memory.
- A dead URL found while recording is a bug in the index: note it next
  to the recorded entry rather than silently substituting a guess.
- Tools no index page covers are out of scope — leave finding their
  docs to the agent at use time; for Python targets, a dedicated
  package-lookup meta-skill exists in the same library.
