---
name: meta-ml-training-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  model-training project to authoritative documentation entry points —
  distributed-training stacks (DeepSpeed, Megatron, PyTorch Lightning,
  NeMo, Colossal-AI, TorchTitan) and finetuning frameworks (torchtune,
  LLaMA-Factory, Axolotl, Unsloth, OpenRLHF) — plus a discovery
  procedure for tools not listed. Use when a harness build must record
  where the docs live for a project that trains or finetunes models,
  especially across multiple devices or nodes. Not for choosing
  between tools or recommending one, and not for base frameworks, the
  Hugging Face or Ray ecosystems, or inference stacks.
---

# Training & Finetuning Documentation Map

This skill produces the documentation entry points a harness build
records for a project that trains or finetunes models. It expects a
harness build in progress and access to the target's dependency manifests
and training configs. Per-tool content is one line plus a URL — install
commands and config syntax are always fetched from the recorded entry
point, never recalled from memory — and nothing here is a recommendation:
when the target lacks a tool for a need, record the option list with URLs
and leave the choice to the user.

## Workflow

1. Detect the training stack: dependency manifests, imports
   (`deepspeed`, `lightning`, `megatron`), launcher configs
   (`deepspeed_config.json`, `accelerate`/`torchrun` invocations in
   scripts or CI), and finetuning configs (Axolotl/LLaMA-Factory YAML,
   torchtune recipes).
2. Read [distributed-training.md](references/distributed-training.md)
   when the project trains across multiple GPUs or nodes, or depends on a
   distributed-training framework.
3. Read [finetuning.md](references/finetuning.md) when the project
   finetunes or post-trains existing models with a dedicated framework.
4. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
5. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
6. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every training and finetuning framework the target actually
uses has a recorded, live documentation entry point, and nothing recorded
ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: a project picking a training
  stack gets the option list and the user's decision, not a default.
- Hugging Face Accelerate/PEFT/TRL and Ray Train belong to their
  ecosystems' own documentation maps — do not duplicate their entries
  from here.
- The same tool may appear in another domain skill's tables; record it
  once per harness, not once per skill.
