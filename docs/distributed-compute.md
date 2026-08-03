---
title: Distributed & GPU Data Compute
description: Dask, cluster analytics engines (Spark, Flink, Trino), the Ray ecosystem, and RAPIDS GPU data science.
tags: [data-science, data-engineering, distributed, gpu]
---

# Distributed & GPU Data Compute

Fetch when the target parallelizes Python with Dask or Ray, runs SQL or dataflow jobs on a cluster engine, or runs data science on NVIDIA GPUs. Each entry is one line and a documentation entry point; engines and clusters deploy as services — fetch install commands, cluster setup, and deployment details from the entry point, never from memory. No entry is a recommendation.

The RAPIDS component libraries are recorded on their domain pages: cuDF on [dataframes-and-storage](dataframes-and-storage.md), cuML on [tabular-and-automl](tabular-and-automl.md), cuGraph on [graphs-and-networks](graphs-and-networks.md), cuSpatial on [geospatial](geospatial.md), and CuPy on [gpu-kernels-and-compilers](gpu-kernels-and-compilers.md). Apache Sedona lives on the geospatial page and GraphFrames on the graphs-and-networks page.

## Dask

| Tool | One line | Docs |
|---|---|---|
| Dask | parallel arrays, dataframes, bags, delayed, and futures | <https://docs.dask.org/> — llms.txt: <https://docs.dask.org/llms.txt> |
| Dask Distributed | the scheduler and workers behind Dask clusters | <https://distributed.dask.org/> |
| Dask-ML | scalable ML utilities on Dask | <https://ml.dask.org/> |

## Cluster Analytics Engines

| Tool | One line | Docs |
|---|---|---|
| Apache Spark | the batch and streaming cluster-compute engine | <https://spark.apache.org/docs/latest/> — llms.txt: <https://spark.apache.org/docs/llms.txt> |
| PySpark | Spark's Python API | <https://spark.apache.org/docs/latest/api/python/> — llms.txt: <https://spark.apache.org/docs/llms.txt> |
| Apache Flink | stateful stream processing | <https://nightlies.apache.org/flink/flink-docs-stable/> |
| Trino | distributed SQL over federated sources | <https://trino.io/docs/current/> |

## Ray

| Tool | One line | Docs |
|---|---|---|
| Ray | Python-native distributed compute: Core (tasks, actors, object store), Data (distributed ETL and batch inference), Train (multi-node training), Tune (hyperparameter search), Serve (model serving), Serve LLM (OpenAI-compatible LLM serving), RLlib (reinforcement learning) | <https://docs.ray.io/> — llms.txt: <https://docs.ray.io/llms.txt> |
| KubeRay | Kubernetes operator with RayCluster, RayJob, and RayService CRDs | <https://github.com/ray-project/kuberay> |
| Anyscale | managed Ray platform | <https://docs.anyscale.com/> — llms.txt: <https://docs.anyscale.com/llms.txt> |

## RAPIDS GPU Data Science

| Tool | One line | Docs |
|---|---|---|
| RAPIDS | the GPU data-science suite's documentation hub | <https://docs.rapids.ai/> |
| Dask-CUDA | multi-GPU Dask clusters | <https://docs.rapids.ai/api/dask-cuda/stable/> |
| RMM | GPU memory management | <https://docs.rapids.ai/api/rmm/stable/> |

## Gotchas

- Every Ray library documents under the one docs root — record the root once and name the components the target actually uses (for example "Ray Data + Ray Train") next to it, so a later agent lands on the right section. Ray's docs root also carries the Kubernetes deployment and cluster-launcher guides.
- "Ray AIR" is a retired umbrella name for the libraries, not a separate component — record the individual libraries the target uses.
- RAPIDS installs come from conda/pip channels that must match the CUDA version — fetch install channels from the entry point.
