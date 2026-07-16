---
name: sync-catalog
description: >-
  Realigns the catalog inventory across the architecture document, catalog
  scaffolds, and the README tables. Use when a catalog or a published skill
  is added, renamed, or removed under skills/, or when the validator reports
  B1-B3 issues. Not for editing a skill's own content.
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
4. Mirror every README change into its `README.zh.md`; the sync-translation
   skill owns that procedure.
5. Run `just validate`; checks B1–B3 and C1 confirm the alignment.

## Gotchas

- The catalog list defines the legal commit scopes; adding a catalog adds a
  scope.
- Catalog depth is exactly two — never nest catalogs. The target-side
  disposal procedure assumes `<skill-root>/<name>/SKILL.md`.
