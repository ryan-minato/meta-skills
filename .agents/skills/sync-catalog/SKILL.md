---
name: sync-catalog
description: >-
  Realigns the catalog inventory across the architecture document, catalog
  scaffolds, the README tables, and the marketplace manifest. Use when a
  catalog or a published skill is added, renamed, or removed under skills/,
  or when the validator reports B1-B3 issues. Not for editing a skill's own
  content.
metadata:
  internal: true
---

# Sync: Catalog Inventory

The directories under `skills/` are the truth; every listing follows them.

## Workflow

1. Reconcile the `## Catalogs` list in
   [ARCHITECTURE.md](../../../ARCHITECTURE.md) with the directories under
   `skills/`, in both directions.
2. Ensure every catalog carries `CONTEXT.md`, `README.md`, and
   `README.zh.md`. A new catalog gets all three before its first skill.
3. Update the skill tables in the root README pair and in the affected
   catalog's README pair. Keep the "none yet" row while a catalog is empty.
   Table descriptions are maintainer prose — never paste the marker into
   them.
4. Reconcile `.claude-plugin/marketplace.json`: one plugin entry per
   catalog — `name` equal to the catalog directory, `source`
   `./skills/<catalog>`, `strict: false`, and `skills` listing **every
   skill directory explicitly** (`"./meta-…"`, one entry per skill).
   Adding, renaming, or removing a skill therefore edits the manifest in
   the same change. Then verify both consumers:
   `npx -y @anthropic-ai/claude-code@latest plugin validate .` (or
   `claude plugin validate .`), and
   `npx -y skills@latest add <repo-root-path> --list` — the listing must
   show one group header per catalog and exactly the published skills. This
   is the installer compatibility check. Then run the discovery script at
   `skills/core/meta-skill-discovery/scripts/discover.py` with
   `--repo-root <repo-root-path>`, and repeat with
   `--catalog <affected-catalog> --full`; these script results are the live
   discovery consumer. Verify every catalog name and description, the
   all-catalog result, and the affected filter.
5. Mirror every README change into its `README.zh.md`; the sync-translation
   skill owns that procedure.
6. Run `just validate`; checks B1–B3 and C1 confirm the alignment.

## Gotchas

- The catalog list defines the legal commit scopes; adding a catalog adds a
  scope.
- The explicit `skills` lists are load-bearing twice over: the plugin
  default scan only looks in `<source>/skills/`, which a catalog does not
  have (dropping the field loads zero skills), and the skills-CLI
  installer can only group the listing by catalog when each skill path is
  listed explicitly — a bare `["./"]` collapses it to an ungrouped flat
  list. The discovery script independently reads the same explicit paths
  from the manifest. A skill added or removed without its manifest edit
  silently disappears from (or lingers in) both consumers. Re-check after
  any manifest edit with `plugin details`, the `skills add … --list` run,
  and the discovery-script runs from step 4.
- Catalog depth is exactly two — never nest catalogs. The target-side
  disposal procedure assumes `<skill-root>/<name>/SKILL.md`.
