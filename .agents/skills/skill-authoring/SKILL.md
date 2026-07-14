---
name: skill-authoring
description: Authors and validates repository skills, including future public meta-skills and internal workflows.
metadata:
  internal: "true"
---

# Skill Authoring Workflow

Use this workflow before creating or revising a repository skill.

1. Read `.agents/knowledge/skill-quality.md`. Read
   `.agents/knowledge/meta-skill-lifecycle.md` when the skill is public and
   disposable.
2. Define the user trigger, desired outcome, safety boundaries, and behavioral
   acceptance set before editing: three triggering prompts, three near-misses,
   and two outcome cases. Use clean-context evaluation when available and report
   unavailable evaluation as a limitation.
3. Create one lowercase-kebab directory with one focused `SKILL.md`. Keep
   frontmatter valid, instructions English-first, and references local and
   conditional. Avoid empty support directories.
4. Public skills belong under `skills/<catalog>/<skill>/`, must have both
   META-SKILL markers, and require catalog docs/context/marketplace work when
   they are the first skill in a catalog. Expose public skills through a relative
   `.agents/skills/` symlink for dogfooding.
5. Internal workflow skills belong directly in `.agents/skills/`, set
   `metadata.internal: "true"`, and must never carry either META-SKILL marker.
6. Run `just check-skill <path>` and then `just check`. Commit the focused
   result using the skill name as scope for public work or an approved repository
   scope for harness work.
