---
name: sync-catalog
description: >
  Realigns the catalog inventory across the architecture document, catalog
  scaffolds, and both catalog README tables. Use when a catalog or a published
  skill is added, renamed, or removed under skills/, or when `just validate-repo`
  reports a catalog mismatch. Not for editing a skill's own content.
---

# Catalog Sync

## Source Of Truth

The directories under `skills/` are the truth. Every other artifact describes
them and must be corrected to match — never the reverse.

## Dependent Artifacts

- The `## Catalogs` list in `ARCHITECTURE.md`
- Each catalog's `CONTEXT.md`, `README.md`, and `README.zh.md`
- The skill tables inside both catalog READMEs

## Workflow

1. List the directories under `skills/` and the catalogs named in the
   `## Catalogs` list in `ARCHITECTURE.md`.
2. Reconcile the two. A new catalog is added to the list with a one-line purpose;
   a removed one is deleted from it.
3. Ensure every catalog has `CONTEXT.md`, `README.md`, and `README.zh.md`. A new
   catalog needs all three: `CONTEXT.md` states the catalog's goal, its
   constraints on what may enter, and its catalog-scoped reference URLs.
4. Update the skill table in the catalog's `README.md`, then mirror the change
   into `README.zh.md`. A catalog with no skills yet keeps a `_(none yet)_` row
   rather than an empty table.
5. Run `just validate-repo` and `just check-skills`.

## Gotchas

- The `## Catalogs` list also defines the legal commit scopes. Adding a catalog
  silently adds a commit scope; removing one invalidates any scope still in use.
- Catalog depth is exactly two (`skills/<catalog>/<skill>/`). Installation
  flattens it to `<root>/<skill>/`, and the target-side disposal procedure can
  only assume that shape. Never nest a catalog inside a catalog.
- The README skill table is written by a maintainer, not copied from the
  frontmatter description. It says what the skill is for, without the marker.
