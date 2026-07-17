# Documentation Discovery

Read when a tool is not listed in this skill's tables, or when a listed
URL no longer resolves. The procedure finds a tool's authoritative
documentation entry point from durable identifiers instead of memorized
or deep URLs.

## Procedure

1. **Start from the package index, not a web search.** For a Python
   package, fetch `https://pypi.org/pypi/<package>/json` and read
   `info.project_urls` — the `Documentation`, `Homepage`, and
   `Repository`/`Source` keys — falling back to `info.home_page`. For
   conda packages, the feedstock at
   `https://github.com/conda-forge/<package>-feedstock` records the same
   links. For non-Python tools, start from the project's official
   organization on its code host.
2. **Rank the candidates**: a dedicated documentation site first, the
   project homepage second, the repository last — but a repository README
   is a legitimate entry point when it is all the project publishes;
   record the repository root rather than guessing a docs domain.
3. **Canonicalize.** Fetch the candidate and follow redirects; record the
   final URL. A redirect to a different host usually means the docs moved
   — the destination is the entry point, unless it embeds a version
   segment, in which case keep the stable alias that redirected.
4. **Probe for agent-first indexes.** At the docs root — and at the site
   root when the docs live under a path — try `llms.txt`, then
   `llms-full.txt`. A hit is a plain-text index of the site; fetch it
   first to locate the right page. Many docs sites also serve a page as
   Markdown at the same path with an `.md` suffix appended; prefer that
   over parsing HTML.
5. **Verify ownership.** The entry point must belong to the project or
   its maintaining organization — cross-check against the package
   metadata or the repository's website field. Mirrors, tutorials, and
   third-party rehosts are never recorded as the entry point.
6. **Record only the entry point.** Versioned paths, deep links, and
   individual API pages go stale; the entry point plus a fetch at use
   time does not.
