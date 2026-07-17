---
name: meta-ds-scale-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  scaled data-processing project to authoritative documentation entry
  points — GPU data science (NVIDIA RAPIDS: cuDF, cuML, cuGraph,
  Dask-CUDA), the Dask distributed-computing family, and cluster
  analytics engines (Apache Spark, Flink, Trino, Sedona) — plus the
  discovery procedure (llms.txt probing, PyPI metadata, official org
  repos) for tools not listed. Use when a harness build must record
  where the docs live for a project that accelerates data processing on
  GPUs or scales it across a cluster. Not for choosing between tools or
  recommending one, and not for single-machine analysis, orchestration
  schedulers, or model training.
---

# Scaled Data Processing Documentation Map

This skill produces the documentation entry points a harness build
records for a project that processes data on GPUs or across clusters.
It expects a harness build in progress and access to the target's
dependency manifests and cluster configs. Per-tool content is one line
plus a URL — install commands and deployment details are always fetched
from the recorded entry point, never recalled from memory — and nothing
here is a recommendation: when the target lacks a tool for a need,
record the option list with URLs and leave the choice to the user.

## Workflow

1. Detect the scale stack: dependency manifests and imports (`cudf`,
   `cuml`, `dask`, `distributed`, `pyspark`, `sedona`), Spark configs
   (`spark-defaults.conf`, `SparkSession` builders), Flink jobs, Trino
   catalogs, and cluster deployment manifests.
2. Read [rapids.md](references/rapids.md) when the target runs data
   science on NVIDIA GPUs.
3. Read [dask.md](references/dask.md) when the target parallelizes
   Python with Dask.
4. Read [cluster-engines.md](references/cluster-engines.md) when the
   target runs SQL or dataflow jobs on a cluster engine.
5. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
6. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
7. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every GPU and cluster data-processing engine the target
actually uses has a recorded, live documentation entry point, and
nothing recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: engine selection is the user's
  decision.
- Ray's data and compute libraries document under Ray's own ecosystem —
  record its entry point once when the target uses Ray, not once per
  domain.
- The same tool may appear in another domain skill's tables (Dask also
  serves HPC scheduling); record it once per harness, not once per
  skill.
