# machine-learning — Catalog Context

Read this before authoring or reviewing anything in
`skills/machine-learning/`. Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `machine-learning`. Neither this
file nor the catalog READMEs ship to targets — installers copy skill
directories only.

## Goal

`machine-learning` holds scaffolding and discovery skills for ML target
projects: they build an ML project's harness or enumerate live external
inventories, and may carry opinionated defaults — each one declares that
in its own description. Documentation entry points for ML domains live
in the published `docs/` index, consumed on demand by `core`'s docs-map
skill — no skill here restates them. Every skill installs per project,
on top of `core`, and only when the target trains, finetunes, serves, or
builds on machine-learning models — it is not part of the default
install.

## Constraints On What May Enter

- **ML-only usefulness.** A skill belongs here only if it is useless to a
  project that does no machine learning. Anything useful regardless of
  stack belongs in `core`; general data analysis and scientific computing
  belong in `data-science`.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Scaffolding declares itself.** A skill that carries opinionated
  defaults — a project scaffold or a recommendation skill — says so in
  its own description. Its defaults apply only where the user expressed
  no preference and the target shows no working convention, and it never
  migrates a working setup unbidden.
- **One situation per skill.** A skill's boundary is one project
  situation (a quick experiment and a long-lived training codebase are
  two skills). Finer splits live behind per-reference load conditions; a
  skill that mixes unrelated situations gets split, not grown.
- **Doc-root fidelity.** When a skill's references cite URLs, only stable
  entry points: a docs root, an org root, or a repository root. Volatile
  facts (versions, install commands, API pages, deep links) always defer
  to a fetch from the entry point. A dead or moved URL is a bug, fixed in
  the same change that finds it.
- **No documentation maps.** Tool-to-docs tables belong in the published
  `docs/` pages, not in a skill; a skill's references cite only the URLs
  its own procedure needs.
- **Reuse is declared, never assumed.** Building on another skill goes
  through the repository dependency contract; catalog co-membership
  never implies installation.

## Authoring

Start from the authoring skill's template
(`.agents/skills/meta-skill-authoring/assets/skill-template.md`), which
ships with the marker pre-filled. The marker's exact bytes and YAML form
are defined in the contract; copy them from there, never from rendered
documentation. Skills take the unsuffixed `meta-ml-<name>`; the
`meta-ml-<domain>-docs` pattern is retired — its content moved to the
published `docs/` pages.

## References

- llms.txt specification (agent-preferred plain-text doc indexes) —
  <https://llmstxt.org/>
- Agent Skills specification — reachable through the `agentskills` MCP
  server.
