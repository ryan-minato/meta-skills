# Product Specification

## Goal

Meta Skills will distribute one-time meta-skills that help an agent build a
durable harness inside a target project. A user installs all `core` skills and
only the relevant topic skills into `.agents/skills/`, asks the agent to create
a harness, verifies the result, and explicitly confirms removal of the
disposable scaffolding skills.

This repository currently builds the development harness for that product. It
does not ship a public meta-skill, empty catalog, marketplace entry, or an
automatic cleanup program in this bootstrap.

## Profiles

The future core orchestrator asks for a profile before it changes a target
project. If the user does not answer, it chooses and records `standard`.

| Profile | Contract |
| --- | --- |
| `minimal` | Entrypoint, goal, repository map, core constraints, existing verification commands, and maintenance rules. |
| `standard` | `minimal` plus applicable design/architecture docs, reproducible environment, tests or lint, CI, and repository safety. This is the default. |
| `full` | `standard` plus a knowledge base, project workflow skills, MCP adapters, Git hooks, complete CI/PII checks, and thicker maintenance mechanisms. |

All profiles are human-supervised L2 harnesses. None may introduce autonomous
knowledge rewrites, unattended maintenance, or other L3/L4 behavior. This
repository uses the `full` profile.

## Catalog contract

Public skills will use capability-first paths:

`skills/<catalog>/<skill>/`

`core` will be the complete required set. Future optional catalogs may cover
GitHub, GitLab, Linear, devcontainers, CI/CD, languages, or frameworks. A
catalog is created only with its first real skill; that change also adds its
English and Chinese README, `CONTEXT.md`, and marketplace entry.

## Meta-skill lifecycle

Every future distributable public `SKILL.md` begins with YAML frontmatter. Its
`description` begins exactly with `[META-SKILL] `, and the first non-empty body
line after frontmatter is exactly:

> **META-SKILL** — One-time harness scaffolding; remove this skill after the target project's harness is verified.

Internal project workflow skills, durable generated harness files, and templates
must not carry either marker. The validator enforces both required markers and
the prohibition against inherited markers.

The later cleanup program is deliberately confirmation-gated: it operates only
inside the target `.agents/skills/`, requires both markers, rejects symlinks and
path escapes, checks remaining references, prints a dry-run list, obtains one
explicit confirmation, deletes only real marked directories, and verifies that
no markers remain. It is deferred to the core MVP.

## Safety and non-goals

Credentials are supplied only through local environment variables or OAuth and
are never committed. Git's default branch is the knowledge authority; Linear is
a delivery tracker and receives only post-merge knowledge mirrors. Humans select
profiles/topics, confirm cleanup, review pull requests, and merge them.
