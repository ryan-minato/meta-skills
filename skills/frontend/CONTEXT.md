# frontend — Catalog Context

Read this before authoring or reviewing anything in `skills/frontend/`.
Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `frontend`. Neither this file nor
the catalog READMEs ship to targets — installers copy skill directories
only.

## Goal

`frontend` holds the meta-skills that only matter to projects with a
user-facing visual surface: design description, visual language, UI
conventions. It installs per project, on top of `core`, and only when the
target actually has a frontend — it is not part of the default install.

## Constraints On What May Enter

- **Frontend-only usefulness.** A skill belongs here only if it is useless
  to a backend-only project. Anything useful regardless of the target's
  surface belongs in `core`; anything tied to a specific stack belongs in a
  narrower topic catalog.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Framework-neutral.** No React, Vue, or build-tool assumptions; name
  categories, never products. Frontend-ness is about the target having a
  visual surface, not about its stack.
- **Public-spec fidelity.** A skill that encodes a public specification
  must match the published spec, cite the upstream URL in a reference, and
  never fork or extend the format's normative rules. Bundled tooling may
  only be a compatible enhancement, clearly labeled optional. When the
  upstream spec changes, the skill's reference is updated in the same
  change — spec drift is a bug.
- **Reserved names.** A conventional file name that a public spec claims
  (`DESIGN.md`) is never repurposed by any skill in this catalog.

## Authoring

Start from the authoring skill's template
(`.agents/skills/meta-skill-authoring/assets/skill-template.md`), which
ships with the marker pre-filled. The marker's exact bytes and YAML form are
defined in the contract; copy them from there, never from rendered
documentation.

## References

- DESIGN.md specification — <https://github.com/google-labs-code/design.md>
- Agent Skills specification — reachable through the `agentskills` MCP
  server.
