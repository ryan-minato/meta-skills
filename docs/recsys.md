---
title: Recommender Systems
description: Ranking, retrieval, and CTR frameworks for recommendation and candidate-generation systems.
tags: [machine-learning, recsys, tabular]
---

# Recommender Systems

Fetch when the target builds recommendation, ranking, or candidate retrieval. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| TorchRec | PyTorch's sharded embeddings and recsys primitives | <https://meta-pytorch.org/torchrec/> |
| TensorFlow Recommenders | retrieval and ranking on Keras | <https://www.tensorflow.org/recommenders> |
| NVIDIA Merlin | GPU-accelerated end-to-end recsys stack | <https://github.com/NVIDIA-Merlin/Merlin> |
| RecBole | unified benchmark of classic and neural recommenders | <https://recbole.io/> |
| DeepCTR | CTR model zoo on TensorFlow | <https://deepctr-doc.readthedocs.io/> |
| DeepCTR-Torch | CTR model zoo on PyTorch | <https://deepctr-torch.readthedocs.io/> |
| Microsoft Recommenders | best-practice recsys examples and utilities | <https://github.com/recommenders-team/recommenders> |
| implicit | fast implicit-feedback collaborative filtering | <https://benfred.github.io/implicit/> |
| LightFM | hybrid matrix factorization | <https://github.com/lyst/lightfm> |

## Gotchas

- ANN retrieval libraries for candidate generation (Faiss, ScaNN) are recorded with vector search — see the [vector-search](vector-search.md) page.
