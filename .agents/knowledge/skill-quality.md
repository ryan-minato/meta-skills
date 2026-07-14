# Skill Quality Standard

Load this document before creating or reviewing an Agent Skill.

## Required shape

- The directory name and frontmatter `name` are lowercase kebab-case and match.
- `SKILL.md` starts with YAML frontmatter and has a concrete third-person
  `description` that says what it does and when to invoke it.
- `metadata` values are strings. Internal project skills set
  `metadata.internal: "true"`.
- Keep the main file focused. Link to local references only when the workflow
  needs them, and make every link relative and self-contained.
- Use English for instructions, scripts, diagnostics, comments, and examples.

## Progressive disclosure

Put the trigger, outcome, constraints, and short workflow in `SKILL.md`. Put
deep reference material in a linked `references/` file only when it is read
conditionally. Do not create empty optional directories, redundant READMEs, or
large copied manuals.

## Scripts and verification

Prefer small non-interactive stdlib-first scripts. Each script provides `--help`,
validates arguments before work, returns 0 on success, 1 on validation failure,
and 2 on usage or configuration errors. Never print or persist credentials.

Before publishing a skill, define behavioral acceptance checks: at least three
trigger prompts, three near-misses, and two outcome cases. Use a clean-context
evaluation where available, target at least 90% success, and treat incorrect
external writes, reverse knowledge sync, missing commit scope, or deletion of a
durable skill as critical failures. These are delivery evaluations, not an
automated repository test layer. Record any unavailable clean-context evaluation as
an observability limitation rather than claiming it passed.

Run `just check-skill <path>` during authoring and `just check` before handoff.

## Public meta-skills

Future public scaffolding skills additionally follow
[the lifecycle protocol](meta-skill-lifecycle.md). Internal workflow skills and
durable target-harness files must not use META-SKILL markers.
