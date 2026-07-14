# Meta Skills

[![Quality](https://github.com/ryan-minato/meta-skills/actions/workflows/quality.yml/badge.svg)](https://github.com/ryan-minato/meta-skills/actions/workflows/quality.yml)
[![Secret history scan](https://github.com/ryan-minato/meta-skills/actions/workflows/secrets.yml/badge.svg)](https://github.com/ryan-minato/meta-skills/actions/workflows/secrets.yml)

> Disposable meta-skills that generate durable, project-specific agent harnesses.

[中文](README.zh.md) · [Design](DESIGN.md) · [Architecture](ARCHITECTURE.md) · [Agent guide](AGENTS.md)

Meta Skills will help an agent turn a selected set of one-time scaffolding
skills into a maintainable harness: clear agent entrypoints, project knowledge,
design and architecture contracts, workflow skills, MCP adapters, CI, Git hooks,
and repository conventions.

## Lifecycle

```text
Install core + selected topics → choose a profile → generate and verify harness
                                                      ↓
                                  explicitly confirm removal of meta-skills
```

The removal step is intentional: a meta-skill is scaffolding, while the harness
it creates is meant to remain with the target project.

## Profiles

| Profile | What it creates |
| --- | --- |
| `minimal` | Entrypoint, goal, map, core constraints, commands, and maintenance rules. |
| `standard` | Minimal plus applicable design/architecture docs, reproducible environment, checks, CI, and safety. Default. |
| `full` | Standard plus knowledge, workflow skills, MCP, hooks, complete CI/PII, and stronger maintenance. |

All profiles are supervised L2 harnesses. They do not introduce unattended or
self-modifying L3/L4 behavior.

## Catalogs

Future public skills will use `skills/<catalog>/<skill>/`. `core` will be
installed as a complete set; users will then select only relevant topic catalogs
such as GitHub, GitLab, Linear, devcontainer, CI/CD, or language/framework
support. A catalog is created only with its first real skill.

**There are currently no public skills to install.** This repository first
builds the quality, lifecycle, and delivery harness that future skills require.

## META-SKILL safety

Every future distributable scaffolding skill will carry two matching markers:
one at the start of its frontmatter description and one as the first body line.
Validators reject partial markers and reject those markers in durable or
internal skills. The future cleanup tool will show a dry-run list and require an
explicit confirmation before removing only verified, non-symlinked meta-skills.

## Develop this repository

```sh
just setup
just check
```

Read [AGENTS.md](AGENTS.md) first. The current repository uses the `full`
profile and is managed in Linear as **Meta Skills**. Git's default branch is the
knowledge authority; Linear mirrors merged knowledge only.
