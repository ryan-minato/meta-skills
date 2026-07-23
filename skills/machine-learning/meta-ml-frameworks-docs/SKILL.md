---
name: meta-ml-frameworks-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  deep-learning project to authoritative documentation entry points —
  general DL and tensor frameworks (PyTorch, TensorFlow, Keras, JAX,
  MLX, PaddlePaddle, tinygrad) and the GPU-kernel and compiled-ops
  libraries beside them. Use when a harness build must record where the
  docs live for a project that depends on a DL or tensor framework or
  ships custom kernels. Not for choosing between frameworks or
  recommending one, and not for distributed-training, inference, or
  data-analysis stacks.
---

# DL Framework & Kernel Documentation Map

This skill produces the documentation entry points a harness build
records for a project built on a deep-learning or tensor framework. It
expects a harness build in progress and access to the target's dependency
manifests. Per-tool content is one line plus a URL — install commands and
API details are always fetched from the recorded entry point, never
recalled from memory — and nothing here is a recommendation: when the
target lacks a tool for a need, record the option list with URLs and
leave the choice to the user.

## Workflow

1. Detect the frameworks in play: dependency manifests (`pyproject.toml`,
   `requirements*.txt`, `environment.yml`, lockfiles), imports (`torch`,
   `tensorflow`, `keras`, `jax`, `mlx`, `paddle`, `tinygrad`), and
   CUDA/ROCm markers in Dockerfiles or CI.
2. Read [dl-frameworks.md](references/dl-frameworks.md) when any general
   DL or tensor framework is detected, or when the project clearly needs
   one and the user must pick from the options.
3. Read [kernels-and-ops.md](references/kernels-and-ops.md) when the
   project ships custom GPU kernels or compiled extensions, or depends on
   kernel-level libraries (`triton`, `flash-attn`, `xformers`,
   `bitsandbytes`, `einops`, `cupy`, `numba`, `cython`).
4. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
5. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every framework and kernel library the target actually uses
has a recorded, live documentation entry point, and nothing recorded
ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: a project with no framework gets
  the option list and the user's decision, not a default.
- A repository README is a legitimate entry point for projects without a
  docs site — record the repository root, not a guessed docs domain.
- The same tool may appear in another domain skill's tables; record it
  once per harness, not once per skill.
- Tools this skill does not list are out of scope: record only what its
  tables cover, and leave finding docs for anything else to the agent —
  it is not this skill's job.
