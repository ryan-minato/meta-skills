---
name: meta-ml-image-gen-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps an
  image- or video-generation project to authoritative documentation
  entry points — generation UIs and pipelines (ComfyUI, SD WebUI Forge,
  InvokeAI), LoRA training (kohya_ss, LyCORIS), conditioning adapters
  (ControlNet, IP-Adapter), and open video generation (Open-Sora,
  LTX-Video). Use when a harness build must record where the docs live
  for a project that generates images or video with diffusion-model
  tooling. Not for choosing between tools or recommending one, and not
  for discriminative computer vision or the Diffusers library itself.
---

# Image & Video Generation Documentation Map

This skill produces the documentation entry points a harness build
records for a project that generates images or video. It expects a
harness build in progress and access to the target's dependency
manifests and tool checkouts. Per-tool content is one line plus a URL —
install steps and workflow details are always fetched from the recorded
entry point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the generation stack: tool checkouts and configs (ComfyUI
   workflows and `custom_nodes/`, WebUI extension folders, kohya
   configs), model files (checkpoints, LoRA/LyCORIS weights, ControlNet
   models), and generation dependencies in manifests.
2. Read [generation-tools.md](references/generation-tools.md) for the
   UIs, trainers, adapters, and video-generation projects in play.
3. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
4. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every generation tool the target actually uses has a
recorded, live documentation entry point, and nothing recorded ranks or
recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: UI and trainer selection is the
  user's decision.
- Most tools here are cloned applications, not pip packages — the
  repository root is the entry point and the install procedure lives in
  its README.
- The Diffusers library belongs to the Hugging Face ecosystem's own
  documentation map — do not duplicate its entry from here.
- Tools this skill does not list are out of scope: record only what its
  tables cover, and leave finding docs for anything else to the agent —
  it is not this skill's job.
