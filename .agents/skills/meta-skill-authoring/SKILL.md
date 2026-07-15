---
name: meta-skill-authoring
description: >-
  Authors and reviews published meta-skills under skills/. Use when creating,
  editing, or reviewing a skill in any catalog, or when a published skill
  fails validation on marker, naming, structure, or portability. Not for this
  repository's own durable skills.
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
3. Body rules — write for the target-project agent:
   - Assume the target project's conventions; never mention this
     repository's files, commands, or workflow.
   - Keep every relative link inside the skill directory. Push long material
     into `references/` behind a precise load condition; put copyable
     skeletons in `assets/`.
   - Never assume another meta-skill is installed. To build on one, instruct
     the user to install it.
   - Any template the skill copies into the target's harness must NOT carry
     the marker — it has to survive the cleanup (the destination test).
4. Run `just validate` and fix what it names; run `just check` before
   committing.

## Gotchas

- Keep the marker on one physical line of the description; conformance is
  tested on the YAML-resolved value.
- READMEs never go inside a skill directory — catalog READMEs document the
  skill instead.
- Renaming a skill means renaming the directory and the `name` field
  together, then running the sync-catalog skill for the README tables.
