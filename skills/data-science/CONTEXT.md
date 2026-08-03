# data-science — Catalog Context

Read this before authoring or reviewing anything in
`skills/data-science/`. Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `data-science`. Neither this
file nor the catalog READMEs ship to targets — installers copy skill
directories only.

## Goal

`data-science` holds project skills for data-analysis and
scientific-computing targets: opinionated scaffolds that build a
data-science repository's harness and declare their defaults in their
descriptions. Documentation entry points for these domains live in the
published `docs/` index, consumed on demand by `core`'s docs-map skill —
no skill here restates them. The catalog installs per project, on top of
`core`, and only when the target analyzes data, runs data pipelines, or
does numerical and scientific computing — it is not part of the default
install.

## Constraints On What May Enter

- **DS-only usefulness.** A skill belongs here only if it is useless to
  a project that does no data analysis or scientific computing.
  Anything useful regardless of stack belongs in `core`; model training
  and ML-specific tooling belong in `machine-learning`.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Scaffolding declares itself.** An opinionated scaffold or
  recommendation skill may choose defaults only when its description
  says so and its body preserves existing working choices.
- **One situation per skill.** A skill's boundary is one project
  situation with a detectable trigger. Finer splits live behind
  per-reference load conditions; a skill that mixes unrelated
  situations gets split, not grown.
- **Doc-root fidelity.** When a skill's references cite URLs, only
  stable entry points: a docs root, an org root, or a repository root.
  Volatile facts (versions, install commands, API pages, deep links)
  always defer to a fetch from the entry point. A dead or moved URL is
  a bug, fixed in the same change that finds it.
- **No documentation maps.** Tool-to-docs tables belong in the
  published `docs/` pages, not in a skill; a skill's references cite
  only the URLs its own procedure needs.
- **Reuse is declared, never assumed.** Building on another skill goes
  through the repository dependency contract; catalog co-membership
  never implies installation.

## Authoring

Start from the authoring skill's template
(`.agents/skills/meta-skill-authoring/assets/skill-template.md`), which
ships with the marker pre-filled. The marker's exact bytes and YAML form
are defined in the contract; copy them from there, never from rendered
documentation. Project builders use the `meta-ds-<domain>-project`
pattern; the `meta-ds-<domain>-docs` pattern is retired — its content
moved to the published `docs/` pages.

## References

- llms.txt specification (agent-preferred plain-text doc indexes) —
  <https://llmstxt.org/>
- Agent Skills specification — reachable through the `agentskills` MCP
  server.
