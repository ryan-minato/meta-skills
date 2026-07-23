---
name: meta-ml-huggingface-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  Hugging Face-based project to authoritative documentation entry points
  across the ecosystem — model and data libraries (Transformers,
  Diffusers, Datasets, Tokenizers), training and optimization
  (Accelerate, PEFT, TRL, Optimum), and Hub serving and apps (TGI, TEI,
  Inference Endpoints, Spaces, Gradio, smolagents). Use when a harness
  build must record where the docs live for a project that depends on
  any Hugging Face library or loads models from the Hub. Not for
  choosing between tools or recommending one, and not for
  non-Hugging-Face training or inference stacks.
---

# Hugging Face Ecosystem Documentation Map

This skill produces the documentation entry points a harness build
records for a project built on the Hugging Face ecosystem. It expects a
harness build in progress and access to the target's dependency
manifests. Per-library content is one line plus a URL — install commands
and API details are always fetched from the recorded entry point, never
recalled from memory — and nothing here is a recommendation: when the
target lacks a library for a need, record the option list with URLs and
leave the choice to the user.

## Workflow

1. Detect the ecosystem footprint: dependency manifests and imports
   (`transformers`, `datasets`, `diffusers`, `peft`, `trl`,
   `accelerate`, `huggingface_hub`, `gradio`), Hub model or dataset IDs
   in code and configs, and a populated `~/.cache/huggingface/`.
2. Read [core-libraries.md](references/core-libraries.md) when any
   model, data, or file-format library is in play — the default entry
   for every Hugging Face project.
3. Read
   [training-and-optimization.md](references/training-and-optimization.md)
   when the project trains, finetunes, evaluates, or exports models with
   Hugging Face tooling.
4. Read [serving-and-apps.md](references/serving-and-apps.md) when the
   project serves models, hosts demos, builds agents, or produces
   datasets with Hub-side tooling.
5. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
6. Record each detected library — name, one-line role, documentation
   entry point, and its llms.txt when present — wherever the harness
   keeps conventions.

Done when: every Hugging Face library the target actually uses has a
recorded, live documentation entry point, and nothing recorded ranks or
recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: a project picking between
  ecosystem libraries gets the option list and the user's decision.
- Most of the ecosystem's docs live under one root
  (`https://huggingface.co/docs`) — record the per-library entry point,
  not just the shared root, so the harness links straight to the right
  library.
- The same tool may appear in another domain skill's tables (timm,
  Gradio, bitsandbytes); record it once per harness, not once per skill.
- Tools this skill does not list are out of scope: record only what its
  tables cover, and leave finding docs for anything else to the agent —
  it is not this skill's job.
