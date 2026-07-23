---
name: meta-ml-inference-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  model-deployment project to authoritative documentation entry points —
  LLM inference engines (vLLM, SGLang, TensorRT-LLM, llama.cpp, Ollama),
  quantization and compression, model compilers and cross-platform
  runtimes (ONNX, TensorRT, OpenVINO, TVM, ExecuTorch), and serving
  platforms (Triton Inference Server, KServe, BentoML, TorchServe). Use
  when a harness build must record where the docs live for a project
  that serves, ships, quantizes, or compiles models. Not for choosing
  between tools or recommending one, and not for training stacks, LLM
  application frameworks, or experiment tracking.
---

# Inference & Deployment Documentation Map

This skill produces the documentation entry points a harness build
records for a project that serves or ships models. It expects a harness
build in progress and access to the target's dependency manifests,
Dockerfiles, and deployment configs. Per-tool content is one line plus a
URL — install commands and config syntax are always fetched from the
recorded entry point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the deployment stack: dependency manifests, inference-server
   images in Dockerfiles and compose files, exported model artifacts
   (`.onnx`, `.plan`/`.engine`, OpenVINO IR, `.gguf`, Core ML packages),
   quantization configs, and serving manifests (KServe/Seldon CRDs,
   BentoML `bentofile`).
2. Read
   [llm-inference-engines.md](references/llm-inference-engines.md) when
   the target runs LLMs locally or serves them at scale.
3. Read
   [quantization-compression.md](references/quantization-compression.md)
   when the target quantizes, prunes, or otherwise compresses models.
4. Read
   [compilers-and-runtimes.md](references/compilers-and-runtimes.md)
   when the target exports models to a compiled or cross-platform
   runtime, including mobile and edge.
5. Read [model-serving.md](references/model-serving.md) when the target
   serves models behind an API or on Kubernetes.
6. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
7. Record each detected tool the tables cover — name, one-line role,
   documentation entry point, and its llms.txt when present — wherever
   the harness keeps conventions.

Done when: every inference, quantization, compilation, and serving tool
the target actually uses has a recorded, live documentation entry point,
and nothing recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: engine and runtime selection is
  the user's decision.
- Two Tritons exist: the GPU kernel language documents with the
  framework stack; the NVIDIA Triton Inference Server lives here — name
  which one the harness records.
- Hugging Face TGI/TEI/Optimum and Ray Serve belong to their ecosystems'
  own documentation maps — do not duplicate their entries from here.
- The same tool may appear in another domain skill's tables; record it
  once per harness, not once per skill.
- Tools this skill does not list are out of scope — leave finding their
  docs to the agent; it is not this skill's job.
