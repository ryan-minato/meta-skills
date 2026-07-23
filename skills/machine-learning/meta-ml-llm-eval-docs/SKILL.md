---
name: meta-ml-llm-eval-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps an
  LLM-evaluation project to authoritative documentation entry points —
  benchmark and evaluation harnesses (lm-evaluation-harness, HELM,
  OpenCompass, VLMEvalKit, Ragas, DeepEval, Promptfoo, Inspect AI,
  EvalPlus) and LLM observability platforms (Arize Phoenix, Langfuse).
  Use when a harness build must record where the docs live for a project
  that benchmarks, evaluates, or traces LLMs and generative models. Not
  for choosing between tools or recommending one, and not for building
  LLM applications or training models.
---

# LLM Evaluation Documentation Map

This skill produces the documentation entry points a harness build
records for a project that evaluates LLMs or generative models:
benchmarks, RAG and app-level evals, and trace-based observability. It
expects a harness build in progress and access to the target's
dependency manifests. Per-tool content is one line plus a URL — install
commands and API details are always fetched from the recorded entry
point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the evaluation stack: dependency manifests and imports
   (`lm_eval`, `opencompass`, `ragas`, `deepeval`, `inspect_ai`,
   `phoenix`, `langfuse`), promptfoo configs, benchmark task lists, and
   eval datasets or result files in the repository.
2. Read [llm-evaluation.md](references/llm-evaluation.md) when the
   target runs benchmarks or scores model, RAG, or agent quality.
3. Read [observability.md](references/observability.md) when the target
   traces LLM calls in development or production.
4. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
5. Record each detected tool the tables cover — name, one-line role,
   documentation entry point, and its llms.txt when present — wherever
   the harness keeps conventions.

Done when: every evaluation harness and observability platform the
target actually uses has a recorded, live documentation entry point, and
nothing recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: harness selection is the user's
  decision.
- Hugging Face Evaluate/LightEval and LangSmith belong to their
  ecosystems' own documentation maps — do not duplicate their entries
  from here.
- The same tool may appear in another domain skill's tables; record it
  once per harness, not once per skill.
- Tools this skill does not list are out of scope — leave finding their
  docs to the agent; it is not this skill's job.
