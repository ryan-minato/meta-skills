# Meta-skill Lifecycle Protocol

Load this document when adding, validating, or cleaning a distributable
scaffolding skill.

## Required dual marker

A future public `SKILL.md` keeps YAML frontmatter at byte zero and contains both:

1. A `description` beginning exactly with `[META-SKILL] `.
2. This first non-empty line after frontmatter:

   `> **META-SKILL** — One-time harness scaffolding; remove this skill after the target project's harness is verified.`

The dual marker makes intent machine-recognizable while preserving standard
Agent Skills frontmatter. Validators reject either missing half.

## Prohibited inheritance

Internal workflow skills, persistent project skills, generated durable harness
documents, templates, and marketplace metadata must carry neither marker. A
marker is a disposal contract, not a generic label.

## Future cleanup contract

Cleanup is not included in this bootstrap. Its future implementation must:

1. Limit discovery to the target `.agents/skills/` directory.
2. Require both markers for every candidate.
3. Reject symlinks and resolved paths outside the target directory.
4. Check surviving files for references and report conflicts.
5. Print a dry-run candidate list before mutation.
6. Obtain one explicit user confirmation.
7. Remove only confirmed real directories, then verify no marker remains.

No workflow may silently delete a skill or infer confirmation from an earlier
request to create a harness.
