---
name: sync-contract
description: >
  Realigns the meta-skill marker contract across the knowledge base, the agent
  entrypoint, and the validator constant. Use when the marker string, its YAML
  form, or the rules for who must carry it change. Not for routine skill
  authoring, which only reads the contract.
---

# Contract Sync

## Source Of Truth

`.agents/knowledge/meta-skill-contract.md` is the source of truth for the marker
contract. The other copies exist because the rule must be visible without
loading a pointer, and enforceable without reading prose.

## Dependent Artifacts

**This table is the inventory.** Nothing else states how many copies there are.
A count written in prose drifts the moment a copy is added — which is exactly
how `validate_repo.py` stayed unlisted while three separate sentences insisted
there were three copies.

| Artifact | Carries | Byte-exact |
|---|---|---|
| `.agents/knowledge/meta-skill-contract.md` | the literal plus full rationale — **source of truth** | display form, uses a visible placeholder for the trailing space |
| `AGENTS.md`, Core Conventions | the literal, one line, always loaded | yes |
| `scripts/check_skill.py`, `MARKER` | the enforced constant | yes |
| `scripts/validate_repo.py`, `MARKER` | the enforced constant, for misplaced-marker detection | yes |
| `skills/<catalog>/CONTEXT.md` | the authoring form authors copy from, one per catalog | yes, as a folded scalar |
| `skills/core/meta-disposal/scripts/find_meta_skills.py`, `MARKER` | the matching constant that **ships to target projects** | yes |
| `README.md` and its `README.zh.md` mirror | the literal, quoted in the public explanation | states the same literal |

Every published skill's `description` also carries the literal, but those are
step 6's business rather than rows here — there is one per skill and the list
would go stale on its own.

## Workflow

1. Change the contract file first; it is the source of truth.
2. Propagate the literal to every artifact in the table above. The ones marked
   byte-exact must agree byte for byte; the rest must state the same literal.
3. Update the fenced authoring form in every catalog's `CONTEXT.md`.
4. Update `check_skill.py --selftest` cases so they still assert the new literal,
   including the near-miss case.
5. Run `just selftest`, then `just check`.
6. If the literal itself changed, every already-published skill is now unmarked.
   Re-mark them in the same change, or the next cleanup pass will not find them.

## Gotchas

- Changing the marker is a **breaking change to already-installed skills**. A
  meta-skill sitting in someone's project keeps the old literal, and a new
  disposal skill will not find it. Prefer never changing it; if you must, say so
  in the release notes.
- That break runs both ways, because `meta-disposal` ships its own `MARKER`
  constant. An installation is self-consistent — old skills and the old disposal
  tool that came with them agree — but a project that installs a *newly* marked
  skill beside an *older* disposal skill has a tool looking for the wrong
  literal, in a copy this repository cannot reach to update.
- Copy the literal from the fenced block, never from rendered documentation.
  Rendered text introduces U+00A0 and smart quotes, which are invisible on screen
  and fatal to a byte-exact match.
- The copies are deliberate duplication, not an accident to be refactored away.
  Pointer-loaded content only loads when its condition fires, so the
  always-loaded copy in `AGENTS.md` stays.
- Nothing enforces this inventory. `just check` passes with a copy missing from
  the table, because a validator cannot know a literal it never learned about.
  Adding a new copy of the marker means adding a row here in the same change.
