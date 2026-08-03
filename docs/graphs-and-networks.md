---
title: Graphs & Graph Learning
description: Network analysis, graph neural networks, knowledge-graph embeddings, and probabilistic graphical models.
tags: [data-science, machine-learning, graphs]
---

# Graphs & Graph Learning

Fetch when the target analyzes networks or graph structure, trains graph neural networks or benchmarks on graph datasets, embeds knowledge graphs, or models probabilistic graphical structure. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Graph Analysis

| Tool | One line | Docs |
|---|---|---|
| NetworkX | graph creation and algorithms in pure Python | <https://networkx.org/> |
| igraph | fast graph analysis with Python bindings | <https://python.igraph.org/> |
| NVIDIA RAPIDS cuGraph | GPU graph algorithms and GNN acceleration | <https://docs.rapids.ai/api/cugraph/stable/> |
| GraphFrames | dataframe-based graphs on Spark | <https://graphframes.io/> — llms.txt: <https://graphframes.io/llms.txt> |

## Graph Learning

| Tool | One line | Docs |
|---|---|---|
| PyTorch Geometric | the main GNN library on PyTorch | <https://pytorch-geometric.readthedocs.io/> |
| DGL | graph learning across PyTorch and TensorFlow backends | <https://www.dgl.ai/> |
| TensorFlow GNN | GNNs on TensorFlow | <https://github.com/tensorflow/gnn> |
| Jraph | lightweight GNNs in JAX | <https://github.com/google-deepmind/jraph> |
| Open Graph Benchmark | standard graph-ML benchmark datasets | <https://ogb.stanford.edu/> |

## Knowledge Graphs & Graphical Models

| Tool | One line | Docs |
|---|---|---|
| PyKEEN | knowledge-graph embedding models | <https://pykeen.readthedocs.io/> |
| pgmpy | probabilistic graphical models and causal discovery | <https://pgmpy.org/> — llms.txt: <https://pgmpy.org/llms.txt> |

## Gotchas

- GraphFrames runs on Spark — the Spark engine itself lives on the distributed-compute page.
