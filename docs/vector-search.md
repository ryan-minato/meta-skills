---
title: Vector Search & Databases
description: Local ANN index libraries, vector databases, and search engines for embedding retrieval.
tags: [machine-learning, llm, data-engineering, recsys]
---

# Vector Search & Databases

Fetch when the target embeds and retrieves: local ANN indexes or vector databases. Each entry is one line and a documentation entry point; fetch install and deployment details from the entry point, never from memory. No entry is a recommendation.

## Local ANN libraries

| Tool | One line | Docs |
|---|---|---|
| Faiss | similarity search over dense vectors, CPU and GPU | <https://github.com/facebookresearch/faiss> |
| ScaNN | Google's high-recall ANN search | <https://github.com/google-research/google-research/tree/master/scann> |
| HNSWlib | header-only HNSW index | <https://github.com/nmslib/hnswlib> |
| Annoy | static mmap-friendly ANN trees | <https://github.com/spotify/annoy> |
| USearch | compact single-file vector index | <https://github.com/unum-cloud/usearch> |

## Vector databases & search engines

| Tool | One line | Docs |
|---|---|---|
| Milvus | distributed vector database | <https://milvus.io/docs> — llms.txt: <https://milvus.io/llms.txt> |
| Qdrant | vector database with filtering and hybrid search | <https://qdrant.tech/documentation/> — llms.txt: <https://qdrant.tech/llms.txt> |
| Weaviate | vector database with modular vectorizers | <https://docs.weaviate.io/> — llms.txt: <https://weaviate.io/llms.txt> |
| Chroma | developer-first embedding database | <https://docs.trychroma.com/> — llms.txt: <https://docs.trychroma.com/llms.txt> |
| LanceDB | embedded vector database on the Lance format | <https://docs.lancedb.com/> — llms.txt: <https://docs.lancedb.com/llms.txt> |
| pgvector | vector similarity inside PostgreSQL | <https://github.com/pgvector/pgvector> |
| Vespa | search and ranking engine with vector support | <https://docs.vespa.ai/> — llms.txt: <https://docs.vespa.ai/llms.txt> |
| Elasticsearch | full-text search with dense-vector retrieval | <https://www.elastic.co/docs> — llms.txt: <https://www.elastic.co/docs/llms.txt> |
| OpenSearch | open-source search with k-NN plugin | <https://docs.opensearch.org/> |
| Redis | in-memory store with vector search | <https://redis.io/docs/> — llms.txt: <https://redis.io/llms.txt> |
| Pinecone | managed vector database | <https://docs.pinecone.io/> — llms.txt: <https://docs.pinecone.io/llms.txt> |

## Gotchas

- The databases deploy as services (containers or managed) while the ANN libraries install as packages — fetch deployment details from the entry point before assuming a pip install suffices.
- Faiss and ScaNN also serve recommender retrieval; the [recsys](recsys.md) page points here rather than duplicating their rows.
