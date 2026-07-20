# GitLab Docs Navigation

Read before the session's first fetch from docs.gitlab.com, or when a
recorded URL no longer resolves. The procedure finds the current
authoritative page for any GitLab platform topic instead of recalling
syntax, tier availability, or feature existence from memory.

## Procedure

1. **The docs root is <https://docs.gitlab.com/>.** The agent index at
   <https://docs.gitlab.com/llms.txt> is a comprehensive standard-format
   index of the whole site: the primary navigation move is to fetch it
   and search it for the topic. It also survives the path reshuffles
   GitLab docs periodically undergo — a dead topic URL is re-located
   there, never guessed at.
2. **Fetch pages as rendered HTML.** GitLab docs serve no Markdown
   renditions — appending `.md` to a page URL redirects to
   authentication. Fetch the page itself.
3. **Match the instance's version.** docs.gitlab.com documents the
   latest GitLab. A self-managed instance may run older: it serves docs
   matching exactly what it runs at `<instance-url>/help` — prefer those
   for feature availability, and ask the user for the instance URL and
   version early.
4. **Read the tier badge.** Docs pages mark features as Free, Premium,
   or Ultimate (and gitlab.com versus self-managed). Read the badge
   before proposing a feature; never assert tier availability from
   memory, and design the free-tier fallback first.
5. **Record entry points only.** The docs root and its llms.txt index
   are stable; topic pages move. Syntax, schemas, and feature
   availability are fetched at use time, never recalled from memory.
