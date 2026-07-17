---
name: meta-ml-recsys-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  recommender-system project to authoritative documentation entry
  points — ranking and retrieval frameworks (TorchRec, TensorFlow
  Recommenders, NVIDIA Merlin, RecBole, DeepCTR, implicit, LightFM)
  and the ANN retrieval beneath them (Faiss, ScaNN) — plus a discovery
  procedure for tools not listed. Use when a harness build must record
  where the docs live for a project that builds recommendation,
  ranking, or candidate retrieval. Not for choosing between tools or
  recommending one, and not for general vector databases or LLM
  retrieval stacks.
---

# Recommender Systems Documentation Map

This skill produces the documentation entry points a harness build
records for a recommender-system project. It expects a harness build in
progress and access to the target's dependency manifests. Per-tool
content is one line plus a URL — install commands and API details are
always fetched from the recorded entry point, never recalled from
memory — and nothing here is a recommendation: when the target lacks a
tool for a need, record the option list with URLs and leave the choice
to the user.

## Workflow

1. Detect the recsys stack: dependency manifests and imports
   (`torchrec`, `tensorflow_recommenders`, `merlin`, `recbole`,
   `deepctr`, `implicit`, `lightfm`, `faiss`), interaction-log schemas,
   and ranking-model configs.
2. Read [recsys.md](references/recsys.md) for the ranking, retrieval,
   and CTR frameworks in play.
3. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
4. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
5. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every recommender framework the target actually uses has a
recorded, live documentation entry point, and nothing recorded ranks or
recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: framework selection is the
  user's decision.
- Faiss and ScaNN also appear in LLM retrieval stacks — record them once
  per harness, not once per skill.
