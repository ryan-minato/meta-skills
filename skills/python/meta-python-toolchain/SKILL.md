---
name: meta-python-toolchain
description: >-
  Disposable meta-skill (delete after the harness is built): supplies
  trusted defaults and authoritative doc URLs for a Python project's
  toolchain — uv for dependencies, Ruff for linting and formatting, ty
  for type checking, a justfile for tasks, pre-commit for git hooks, and
  Zensical for documentation — with the established alternatives for each
  category. Use when a harness build must choose or record Python tooling
  and the user has not specified it. Not for migrating a project off
  tools it already uses, and not for non-Python projects.
---

# Python Toolchain Defaults

This skill produces the tool choices and doc URLs a harness build records
for a Python target project, one decision per category: dependencies,
linting, formatting, type checking, task running, git hooks, and
documentation. Per-tool content is deliberately one line plus a URL — fetch
current install commands and configuration from each tool's own docs, never
from memory — and every default yields to an existing working choice.

## Workflow

1. Inventory what exists: `[tool.*]` tables in `pyproject.toml`, lockfiles
   (`uv.lock`, `poetry.lock`, `pdm.lock`, `requirements*.txt`),
   `.pre-commit-config.yaml`, a `justfile` / `Makefile` / `noxfile.py` /
   `tox.ini`, `mkdocs.yml` or `docs/conf.py`, and CI workflows. Every
   existing tool wins its category — record it with its doc URL; migration
   happens only when the user asks for it.
2. Decide dependency management — default **uv**. Read
   [dependency-managers.md](references/dependency-managers.md) when
   choosing the manager, and note the target's shape first: a one-off
   script, a pinned-requirements workflow, and a full pyproject-managed
   project each get a different working mode.
3. Decide code quality tools — defaults **Ruff** for linting, **Ruff's
   formatter** for formatting, **ty** for type checking. Read
   [quality-tools.md](references/quality-tools.md) when choosing, when the
   user names an alternative, or when maturity requirements rule out a
   young tool.
4. Decide how checks and dev tasks are invoked — defaults **just** for the
   task runner and **pre-commit** for git hooks. Read
   [task-runners-and-hooks.md](references/task-runners-and-hooks.md) when
   deciding how contributors and agents run the project's checks and
   whether hooks enforce them.
5. Decide documentation tooling only when the project will publish
   generated docs — "no doc generator" is a valid recorded decision. When
   it will, read [doc-generators.md](references/doc-generators.md);
   default **Zensical**.
6. For every chosen tool, fetch the current install command and minimal
   configuration from its doc URL — when the docs site publishes an
   `llms.txt` plain-text index, fetch that first to locate the right
   page — then record the tool, its one-line role, the command that runs
   it, and the URL wherever the harness keeps conventions.

Done when: every category — dependencies, lint, format, types, tasks,
hooks, docs — has either a recorded choice with its doc URL or an explicit
not-needed, and the command to run each chosen tool is written into the
harness.

## Gotchas

- Defaults are for absent preference, never migration orders: a working
  Poetry, Black, or mypy setup stays, and gets recorded as-is.
- ty and Zensical are young projects — confirm current maturity from their
  docs before recording them, and offer the established fallback (mypy or
  Pyright; Material for MkDocs) when the user needs stability.
- Ruff's formatter is Black-compatible but not Black-identical — never run
  both on the same tree.
- Ruff ships import-sorting rules; adding a separate isort next to it
  creates two fighting sorters.
- pre-commit pins its own tool versions in its config, independent of the
  project's dependencies — record the rule that the two stay aligned, or
  hooks and local runs will disagree.
- Targets in the conda ecosystem (compiled scientific dependencies) may
  need micromamba regardless of the uv default.
