# core — Catalog Context

Read this before authoring or reviewing anything in `skills/core/`.
Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `core`. Neither this file nor the
catalog READMEs ship to targets — installers copy skill directories only.

## Goal

`core` is the required set. A user installs `core` before asking an agent to
build a target project's harness, then adds topic catalogs as the project
needs them. Together, `core` must be enough to take any project from no
harness to a working one — including live discovery of this repository's
skills and the skill that removes all the meta-skills afterwards.

## Constraints On What May Enter

- **Disposable only.** A skill belongs here only if it is one-time
  scaffolding a target project discards after harness setup. A durable,
  general design aid belongs in the sibling repository
  `ryan-minato/skills`; the marker is the admission test — if a skill should
  not carry it, it does not belong in this repository.
- **Stack-agnostic.** `core` installs for every harness build, so a skill
  here must be useful regardless of the target's language, framework, or
  platform. Stack-specific help belongs in a topic catalog.
- **Tightly scoped descriptions.** Every `core` skill loads into every
  target session at once; a description that triggers on unrelated work
  pollutes all of them simultaneously.
- **Cheap to carry.** Keep `SKILL.md` bodies short; push long material into
  `references/` behind precise load conditions.
- **Core-only assumption.** No relative link may escape the skill root.
  Published skills may assume core is installed, but a catalog install never
  proves a non-core sibling is present; the repository dependency contract
  governs every non-core dependency.
- **Assets carry no marker.** A template a skill copies into the target's
  harness must survive the cleanup; apply the contract's destination test to
  every file, not just `SKILL.md`.
- **Assets are raw resources.** An `assets/` file is exactly the file the
  target copies — bare code with its real extension, or the raw document —
  never an `.md` wrapper around a fenced block, and never carrying copy or
  adaptation prose. That how-to lives in `SKILL.md` or `references/`.

## Authoring

Start from the authoring skill's template
(`.agents/skills/meta-skill-authoring/assets/skill-template.md`), which
ships with the marker pre-filled. The marker's exact bytes and YAML form are
defined in the contract; copy them from there, never from rendered
documentation — rendering introduces invisible characters that break a
byte-exact match.

## References

- Agent Skills specification — reachable through the `agentskills` MCP
  server.
- Sibling repository, the durable side of the product boundary —
  <https://github.com/ryan-minato/skills>
