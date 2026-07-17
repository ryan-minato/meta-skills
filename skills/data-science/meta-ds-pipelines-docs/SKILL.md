---
name: meta-ds-pipelines-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  data-pipeline project to authoritative documentation entry points —
  workflow orchestration and analytics engineering (Apache Airflow,
  dbt, Dagster, Prefect) — plus a discovery procedure for tools not
  listed. Use when a harness build must record where the docs live for
  a project that schedules data workflows or builds dbt-style
  transformation pipelines. Not for choosing between tools or
  recommending one, and not for compute engines, ML pipelines, or
  scientific workflow managers.
---

# Data Pipeline Documentation Map

This skill produces the documentation entry points a harness build
records for a project that orchestrates data workflows. It expects a
harness build in progress and access to the target's dependency
manifests and pipeline definitions. Per-tool content is one line plus a
URL — install commands and deployment details are always fetched from
the recorded entry point, never recalled from memory — and nothing here
is a recommendation: when the target lacks a tool for a need, record
the option list with URLs and leave the choice to the user.

## Workflow

1. Detect the pipeline stack: dependency manifests and imports
   (`airflow`, `dbt`, `dagster`, `prefect`), pipeline layouts (`dags/`,
   `dbt_project.yml`, Dagster definitions, Prefect deployments), and
   scheduler deployment configs.
2. Read [orchestration.md](references/orchestration.md) for the
   orchestrators and transformation frameworks in play.
3. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
4. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
5. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every orchestrator and transformation framework the target
actually uses has a recorded, live documentation entry point, and
nothing recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: orchestrator selection is the
  user's decision.
- The same orchestrators also run ML pipelines — a project using them
  for model workflows is an ML-operations concern; record the entry
  point once either way.
