---
name: meta-python-pypi-lookup
description: >-
  Disposable meta-skill (delete after the harness is built): locates the
  authoritative documentation entry point for a Python package from durable
  identifiers — the PyPI/conda metadata and the maintaining organization —
  preferring an agent-oriented Markdown or llms.txt rendition over HTML. Use
  when a harness build needs a package's docs and has no recorded URL for
  it, or when a recorded doc URL no longer resolves. Not for choosing or
  ranking tools, and not for re-documenting packages whose docs are already
  recorded.
---

# PyPI Package Documentation Discovery

This skill produces a single authoritative documentation entry point for a
Python package the harness must document but has no URL for — resolved from
durable identifiers rather than a memorized or guessed URL. It expects a
harness build in progress and records where the docs live, never the docs
themselves.

## Workflow

1. **Start from the package index, not a web search.** For a Python package,
   fetch `https://pypi.org/pypi/<package>/json` and read
   `info.project_urls` — the `Documentation`, `Homepage`, and
   `Repository`/`Source` keys — falling back to `info.home_page`. For conda
   packages, the feedstock at
   `https://github.com/conda-forge/<package>-feedstock` records the same
   links. For non-Python tools, start from the project's official
   organization on its code host.
2. **Rank the candidates**: a dedicated documentation site first, the
   project homepage second, the repository last — but a repository README is
   a legitimate entry point when it is all the project publishes; record the
   repository root rather than guessing a docs domain.
3. **Canonicalize.** Fetch the candidate and follow redirects; record the
   final URL. A redirect to a different host usually means the docs moved —
   the destination is the entry point, unless it embeds a version segment,
   in which case keep the stable alias that redirected.
4. **Prefer an agent-oriented rendition.** Before reading any HTML: many
   docs sites serve a page's Markdown source at the same path with `.md`
   appended — fetch that instead of parsing HTML. At the docs root (and the
   site root when the docs live under a path) probe `llms.txt`: a compact
   plain-text index of the site — fetch it to locate the right page. Only if
   neither exists, fall back to `llms-full.txt`: a single file concatenating
   *all* of the site's text, often enormous. Never read `llms-full.txt` end
   to end — fetch it and search it programmatically (grep for the tool or
   topic) to jump to the relevant section.
5. **Verify ownership.** The entry point must belong to the project or its
   maintaining organization — cross-check against the package metadata or
   the repository's website field. Mirrors, tutorials, and third-party
   rehosts are never recorded as the entry point.
6. **Record only the entry point.** Versioned paths, deep links, and
   individual API pages go stale; the entry point plus a fetch at use time
   does not. Record its `llms.txt` too when the site publishes one.

Done when: the package has one recorded documentation entry point that
resolves live, belongs to the project or its maintaining organization, and
is the stablest form available — its `.md` or `llms.txt` when the site
offers one.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- A repository README is a legitimate entry point for a project that
  publishes nothing else — record the repository root, not a guessed docs
  domain.
- `llms-full.txt` is a search target, not a document to read: loading it
  whole wastes the very context this discovery exists to save. Prefer a
  page's `.md` source, then `llms.txt`, and reach for `llms-full.txt` only
  when both are absent — then grep it, never read it through.
- Mirrors, rehosts, and tutorials rank above nothing: if only a third-party
  page exists, record the repository root and note the gap rather than
  passing off a rehost as the authoritative entry point.
