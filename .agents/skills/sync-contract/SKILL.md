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
contract. The other two copies exist because the rule must be visible without
loading a pointer, and enforceable without reading prose.

## Dependent Artifacts

| Artifact | Carries |
|---|---|
| `.agents/knowledge/meta-skill-contract.md` | the literal plus full rationale — **source of truth** |
| `AGENTS.md`, Core Conventions | the literal, one line, always loaded |
| `scripts/check_skill.py`, `MARKER` | the literal as an enforced constant |
| `skills/<catalog>/CONTEXT.md` | the authoring form authors copy from |

## Workflow

1. Change the contract file first; it is the source of truth.
2. Propagate the literal to the `AGENTS.md` Core Conventions line and the `MARKER`
   constant in `scripts/check_skill.py`. All three must agree byte for byte.
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
- Copy the literal from the fenced block, never from rendered documentation.
  Rendered text introduces U+00A0 and smart quotes, which are invisible on screen
  and fatal to a byte-exact match.
- The three copies are deliberate duplication, not an accident to be refactored
  away. Pointer-loaded content only loads when its condition fires, so the
  always-loaded copy in `AGENTS.md` stays.
