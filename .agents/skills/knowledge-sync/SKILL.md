---
name: knowledge-sync
description: Mirrors merged repository knowledge to Linear Documents without reversing the Git source of truth.
metadata:
  internal: "true"
---

# Knowledge Sync Workflow

Use this workflow only after knowledge changes have merged to the origin default
branch and Linear connectivity is available.

1. Fetch `origin`, resolve its default branch, and read `.agents/knowledge/`
   from that remote ref. Never use unmerged local files as the source.
2. Resolve the Meta Skills project dynamically in Linear. For each owned
   knowledge document, compare semantic content after removing the title line.
   Create or update a Linear Document only when merged Git content differs.
3. Preserve document ownership metadata so future runs update only documents
   managed by this workflow. Report unowned remote documents; never delete them.
4. Do not edit local files from Linear, import Linear-only knowledge into Git,
   or run before merge. Report skipped or unavailable synchronization honestly.

The direction is one-way: origin default branch to Linear Documents.
