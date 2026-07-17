---
name: meta-ml-graph-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  graph machine-learning project to authoritative documentation entry
  points — graph neural networks (PyTorch Geometric, DGL, TensorFlow
  GNN, cuGraph) and graph analysis and knowledge graphs (NetworkX,
  igraph, PyKEEN, pgmpy) — plus the discovery procedure (llms.txt
  probing, PyPI metadata, official org repos) for tools not listed. Use
  when a harness build must record where the docs live for a project
  that learns on graphs or builds knowledge graphs. Not for choosing
  between tools or recommending one, and not for non-graph ML or general
  network analysis without ML.
---

# Graph ML & Knowledge Graph Documentation Map

This skill produces the documentation entry points a harness build
records for a graph-learning project. It expects a harness build in
progress and access to the target's dependency manifests. Per-tool
content is one line plus a URL — install commands and API details are
always fetched from the recorded entry point, never recalled from
memory — and nothing here is a recommendation: when the target lacks a
tool for a need, record the option list with URLs and leave the choice
to the user.

## Workflow

1. Detect the graph stack: dependency manifests and imports
   (`torch_geometric`, `dgl`, `tensorflow_gnn`, `networkx`, `igraph`,
   `pykeen`, `pgmpy`), graph dataset formats, and edge-list or triple
   data.
2. Read [graph-learning.md](references/graph-learning.md) when the
   target trains graph neural networks or benchmarks on graph datasets.
3. Read [graph-analysis-and-kg.md](references/graph-analysis-and-kg.md)
   when the target analyzes graph structure, embeds knowledge graphs,
   or models probabilistic graphical structure.
4. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
5. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
6. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every graph library the target actually uses has a recorded,
live documentation entry point, and nothing recorded ranks or recommends
between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: GNN-framework selection is the
  user's decision.
- The same tool may appear in another domain skill's tables (NetworkX,
  igraph, cuGraph also serve plain graph analytics); record it once per
  harness, not once per skill.
