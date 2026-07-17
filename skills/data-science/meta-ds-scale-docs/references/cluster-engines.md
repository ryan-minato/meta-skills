# Cluster Analytics Engines

Read when the target runs SQL or dataflow jobs on a cluster engine.
One line and an entry point per engine; engines deploy as services —
fetch deployment details from the entry point. No entry is a
recommendation.

## Engines

| Tool | One line | Docs |
|---|---|---|
| Apache Spark | the batch and streaming cluster-compute engine | <https://spark.apache.org/docs/latest/> — llms.txt: <https://spark.apache.org/docs/llms.txt> |
| PySpark | Spark's Python API | <https://spark.apache.org/docs/latest/api/python/> — llms.txt: <https://spark.apache.org/docs/llms.txt> |
| Apache Flink | stateful stream processing | <https://nightlies.apache.org/flink/flink-docs-stable/> |
| Trino | distributed SQL over federated sources | <https://trino.io/docs/current/> |
| Apache Sedona | spatial analytics on Spark and Flink | <https://sedona.apache.org/> |
| GraphFrames | dataframe-based graphs on Spark | <https://graphframes.io/> — llms.txt: <https://graphframes.io/llms.txt> |
| Ray | Python-native distributed compute (Data, Train, Serve under one root) | <https://docs.ray.io/> — llms.txt: <https://docs.ray.io/llms.txt> |
