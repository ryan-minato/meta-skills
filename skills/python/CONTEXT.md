# python — Catalog Context

Read this before authoring or reviewing anything in `skills/python/`.
Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `python`. Neither this file nor
the catalog READMEs ship to targets — installers copy skill directories
only.

## Goal

`python` holds information skills for Python target projects: trusted
defaults and authoritative doc URLs the harness-building agent consults
on demand when deciding documentation conventions, testing setup, and
toolchain. It installs per project, on top of `core`, and only when the
target is (predominantly) Python — it is not part of the default install.
These skills answer "which tool, which style, which default"; the
harness-build procedure itself belongs to `core` and is never restated
here.

## Constraints On What May Enter

- **Python-only usefulness.** A skill belongs here only if it is useless
  to a non-Python project. Anything useful regardless of stack belongs in
  `core`; anything tied to a different stack belongs in its own topic
  catalog.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Defaults are defaults, not dogma.** Every default a skill records
  applies only when the user expressed no preference and the target shows
  no existing convention. No skill here may instruct migration away from
  a working existing choice; migration happens only when the user asks.
- **Upstream-URL fidelity.** Per-tool content is minimal — one line of
  positioning, an install pointer, and the authoritative doc URL. Volatile
  facts (versions, install commands, config syntax, plugin inventories)
  always defer to the URL with an instruction to fetch current details.
  A dead or moved URL is a bug, fixed in the same change that finds it.
- **Information, not procedure.** No step-by-step harness manual. Skills
  here produce recorded decisions; where those decisions get registered
  is `core`'s territory and is referenced only as "wherever the harness
  keeps conventions".

## Authoring

Start from the authoring skill's template
(`.agents/skills/meta-skill-authoring/assets/skill-template.md`), which
ships with the marker pre-filled. The marker's exact bytes and YAML form are
defined in the contract; copy them from there, never from rendered
documentation.

## References

- Astral docs hub (several category defaults live there) —
  <https://docs.astral.sh/>
- Agent Skills specification — reachable through the `agentskills` MCP
  server.
