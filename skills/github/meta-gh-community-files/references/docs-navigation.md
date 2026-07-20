# GitHub Docs Navigation

Read before the session's first fetch from docs.github.com, or when a
recorded URL no longer resolves. The procedure finds the current
authoritative page for any GitHub platform topic instead of recalling
syntax or feature availability from memory.

## Procedure

1. **The docs root is <https://docs.github.com/>.** An agent index lives
   at <https://docs.github.com/llms.txt>, but it is a shallow curated
   landing page, not a sitemap: use it to orient, and never conclude
   from a topic's absence there that the topic is undocumented.
2. **Fetch pages as Markdown.** Appending `.md` to any docs.github.com
   page URL returns the page's Markdown source — prefer it over parsing
   HTML. Index pages serve Markdown the same way, which turns them into
   plain link lists to walk.
3. **Navigate the path taxonomy.** Pages live at
   `/en/<product>/<category>/<subcategory>/<page>`. The products that
   cover harness work: `issues`, `pull-requests`, `actions`,
   `code-security`, `repositories`, `communities`, `organizations`.
   When the right page is unknown, fetch the product root as `.md` and
   follow its links downward.
4. **Keep the explicit `en` locale.** Translated trees lag; `en` is the
   authoritative one.
5. **GitHub Enterprise Server is documented per version.** When the
   target runs GHES, the same site serves matching docs under
   `enterprise-server@<version>` paths — the one legitimate versioned
   URL, matched to the instance's actual version at use time and never
   recorded in the harness.
6. **Record entry points only.** The docs root and the product roots are
   stable; deep guide pages move. Syntax, schemas, and feature
   availability are fetched at use time, never recalled from memory.
