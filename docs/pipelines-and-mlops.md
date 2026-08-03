---
title: Pipelines, Orchestration & MLOps
description: Workflow orchestrators, analytics engineering, experiment tracking and versioning, and ML/production monitoring.
tags: [data-engineering, machine-learning, mlops]
---

# Pipelines, Orchestration & MLOps

Fetch when the target orchestrates data or ML workflows, logs runs, metrics, artifacts, or model versions, or monitors models and data in production. Each entry is one line and a documentation entry point; Kubeflow, Prometheus, and Grafana deploy as services — fetch install commands, deployment, and config details from the entry point, never from memory. No entry is a recommendation.

## Orchestration & Analytics Engineering

| Tool | One line | Docs |
|---|---|---|
| Apache Airflow | DAG-based workflow orchestration | <https://airflow.apache.org/docs/> |
| dbt | SQL transformation pipelines in the warehouse | <https://docs.getdbt.com/> — llms.txt: <https://docs.getdbt.com/llms.txt> |
| Dagster | asset-oriented data and ML orchestration | <https://docs.dagster.io/> — llms.txt: <https://docs.dagster.io/llms.txt> |
| Prefect | Pythonic workflow orchestration | <https://docs.prefect.io/> — llms.txt: <https://docs.prefect.io/llms.txt> |
| Flyte | typed, versioned workflows on Kubernetes | <https://docs.flyte.org/> — llms.txt: <https://www.union.ai/llms.txt> |
| Kubeflow | ML toolkit and pipelines on Kubernetes | <https://www.kubeflow.org/docs/> |
| Metaflow | workflow framework from prototype to production | <https://docs.metaflow.org/> |
| ZenML | portable ML pipelines over pluggable stacks | <https://docs.zenml.io/> — llms.txt: <https://docs.zenml.io/llms.txt> |

## Experiment Tracking & Versioning

| Tool | One line | Docs |
|---|---|---|
| MLflow | experiment tracking, model registry, and deployment glue | <https://mlflow.org/docs/> |
| Weights & Biases | hosted experiment tracking and collaboration | <https://docs.wandb.ai/> — llms.txt: <https://docs.wandb.ai/llms.txt> |
| TensorBoard | training-metric visualization | <https://www.tensorflow.org/tensorboard> |
| ClearML | experiment tracking, orchestration, and data management | <https://clear.ml/docs/> — llms.txt: <https://clear.ml/llms.txt> |
| Neptune | experiment tracker for large-scale training | <https://docs.neptune.ai/> |
| Comet | experiment tracking and model production monitoring | <https://www.comet.com/docs/> — llms.txt: <https://www.comet.com/docs/opik/llms.txt> |
| DVC | git-coupled data and model versioning | <https://doc.dvc.org/> |

## Monitoring & Observability

| Tool | One line | Docs |
|---|---|---|
| Evidently | ML and data quality monitoring and reports | <https://docs.evidentlyai.com/> — llms.txt: <https://docs.evidentlyai.com/llms.txt> |
| Prometheus | metrics collection and alerting | <https://prometheus.io/docs/> |
| Grafana | dashboards over metrics and logs | <https://grafana.com/docs/> — llms.txt: <https://grafana.com/llms.txt> |
| OpenTelemetry | vendor-neutral traces, metrics, and logs | <https://opentelemetry.io/docs/> — llms.txt: <https://opentelemetry.io/llms.txt> |

## Gotchas

- The same orchestrators (Airflow, Prefect, Dagster) serve both data engineering and ML platforms — a harness records each entry point once, whichever side uses it.
