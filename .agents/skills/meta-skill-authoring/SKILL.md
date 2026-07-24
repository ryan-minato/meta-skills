---
name: meta-skill-authoring
description: >-
  Authors and reviews published meta-skills under skills/. Use when creating,
  editing, or reviewing a skill in any catalog, or when a published skill
  fails validation on marker, naming, structure, or portability. Not for this
  repository's own durable skills.
metadata:
  internal: true
---

# Meta-Skill Authoring

## Before Writing

1. Read [meta-skill-contract.md](../../knowledge/meta-skill-contract.md) —
   the audience model, the marker, and the destination test.
2. Read the target catalog's `CONTEXT.md`.
3. For Agent Skills spec questions (frontmatter fields, limits), ask the
   `agentskills` MCP server rather than answering from memory.

## Workflow

1. Copy [assets/skill-template.md](assets/skill-template.md) to
   `skills/<catalog>/<name>/SKILL.md`. The template ships with the marker
   pre-filled — edit only the text after it.
2. Frontmatter checklist:
   - `name` equals the directory name: lowercase kebab-case, at most 64
     chars, `meta-` prefix.
   - `description` keeps the marker first, then what the skill does, "Use
     when …", and optionally "Not for …". At most 1024 chars — every char
     loads into every target session, so keep the trigger tight.
   - When the skill has non-core dependencies, set the string metadata key
     `meta-skills.dependencies` to their space-separated
     `catalog/meta-skill` identifiers. Omit core dependencies and omit the
     key when none remain.
3. Body rules — write for the target-project agent:
   - Assume the target project's conventions; never mention this
     repository's files, commands, or workflow.
   - Keep every relative link inside the skill directory. Push long material
     into `references/` behind a precise load condition. Put copyable
     material in `assets/` as the raw file the target copies — bare code
     with its real extension, or the raw document — never an `.md` wrapper
     around a fenced block, and never carrying copy instructions or
     adaptation notes; that how-to belongs in SKILL.md or `references/`.
   - Assume `core` is installed, and no other skill. Catalog installation is
     recommended but never proves a sibling is present. Put every non-core
     dependency — including a same-catalog dependency — in both metadata and
     a `## Meta-skill Dependencies` section. Name its purpose and direct the
     agent to `core/meta-skill-discovery` for live lookup and installation
     guidance; never duplicate installation commands.
   - Dependencies may name only published skills in this repository. Do not
     hide a dependency in ordinary prose or depend on an external skill.
   - Any template the skill copies into the target's harness must NOT carry
     the marker — it has to survive the cleanup (the destination test).
4. Run `just check-skill skills/<catalog>/<name>` and fix what it names —
   errors are contract violations, warnings are advice worth taking. Run
   `just check` before committing.

## Gotchas

- Keep the marker on one physical line of the description; conformance is
  tested on the YAML-resolved value.
- READMEs never go inside a skill directory — catalog READMEs document the
  skill instead.
- Never set `metadata.internal` on a published skill: skill installers
  honor it by hiding the skill from installs (check M6 blocks it).
- Keep dependency metadata and the body section identical; check M7 validates
  the repository targets, portable fallback, and centralized install path.
- Renaming a skill means renaming the directory and the `name` field
  together, then running the sync-catalog skill for the README tables.
