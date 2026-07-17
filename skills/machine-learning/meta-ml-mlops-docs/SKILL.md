---
name: meta-ml-mlops-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps an
  ML-operations project to authoritative documentation entry points —
  experiment tracking and model registries (MLflow, Weights & Biases,
  TensorBoard, DVC) and ML pipelines and monitoring (Kubeflow, Flyte,
  Metaflow, ZenML, Evidently, Prometheus/Grafana/OpenTelemetry) — plus
  a discovery procedure for tools not listed. Use when a harness build
  must record where the docs live for a project that tracks
  experiments, versions models and data, runs ML pipelines, or
  monitors models. Not for choosing between tools or recommending one,
  and not for training frameworks or model-serving platforms.
---

# MLOps Documentation Map

This skill produces the documentation entry points a harness build
records for a project that operates ML systems: experiment tracking,
model and data versioning, pipelines, and monitoring. It expects a
harness build in progress and access to the target's dependency
manifests and infrastructure configs. Per-tool content is one line plus
a URL — install commands and config syntax are always fetched from the
recorded entry point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the MLOps stack: dependency manifests, tracking-server URIs in
   code or env files (`MLFLOW_TRACKING_URI`, `WANDB_*`), `.dvc/`
   directories, pipeline definitions (Kubeflow manifests, Flyte or
   Metaflow decorators, ZenML configs), and monitoring configs
   (Prometheus scrape configs, Grafana dashboards).
2. Read [experiment-tracking.md](references/experiment-tracking.md)
   when the target logs runs, metrics, artifacts, or model versions.
3. Read
   [pipelines-and-monitoring.md](references/pipelines-and-monitoring.md)
   when the target orchestrates ML workflows or monitors models and
   data in production.
4. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
5. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
6. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every tracking, versioning, pipeline, and monitoring tool the
target actually uses has a recorded, live documentation entry point, and
nothing recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: tracker and orchestrator
  selection is the user's decision.
- General-purpose data orchestrators (Airflow, Prefect, Dagster) appear
  here because ML pipelines run on them — a project using them purely
  for data engineering is a data-stack concern, not an ML one.
- The same tool may appear in another domain skill's tables; record it
  once per harness, not once per skill.
