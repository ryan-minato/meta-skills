---
name: sync-contract
description: >-
  Propagates a change to the meta-skill marker or its rules across every
  aligned copy. Use when the marker string, its YAML form, or the
  who-carries-it rules change, or when the validator reports D1-D3 issues.
  Not for routine skill authoring, which only reads the contract.
metadata:
  internal: true
---

# Sync: Marker Contract

[meta-skill-contract.md](../../knowledge/meta-skill-contract.md) is the
source of truth. Changing the marker is a **breaking change** for
already-installed copies — get explicit user sign-off before starting.

## Workflow

1. Update the marker fence and the YAML authoring form in the contract
   file.
2. Update the `MARKER` constants in **both** validators —
   `scripts/validate_repo.py` (plus the `NEAR_MISS` prefix beside it) and
   `scripts/check_skill.py` — and both scripts' self-test fixtures.
3. Update every fence tagged `text meta-skill-marker` (search for the tag
   across the repository — the root README pair carries copies).
4. Update the authoring template's description
   (`.agents/skills/meta-skill-authoring/assets/skill-template.md`) and
   every published skill's description.
5. Run `just check`. Checks D1, D3, and M3 name every copy still out of
   line; iterate until green — the validators, not a remembered list, are
   the inventory.
6. Record the change as breaking in the PR body: already-installed copies
   still carry the old marker, so their removal procedure no longer matches
   them.

## Gotchas

- Never restate the copy inventory as a count in any document; counts drift
  the moment a copy is added.
- The marker fence bodies carry no trailing whitespace by design; do not
  "fix" them by adding any.
