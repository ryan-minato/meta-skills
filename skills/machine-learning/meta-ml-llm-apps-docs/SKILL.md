---
name: meta-ml-llm-apps-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps an
  LLM-application project to authoritative documentation entry points —
  RAG and agent frameworks (LangChain, LlamaIndex, Haystack, DSPy,
  AutoGen, CrewAI, PydanticAI), LLM gateways and guardrails (LiteLLM,
  Instructor, Guardrails, MCP), and vector search from local ANN
  libraries to vector databases (Faiss, Milvus, Qdrant, pgvector). Use
  when a harness build must record where the docs live for a project
  that builds applications on LLM APIs or local models. Not for choosing
  between tools or recommending one, and not for model training,
  inference engines, or LLM evaluation harnesses.
---

# LLM Application Documentation Map

This skill produces the documentation entry points a harness build
records for a project that builds on LLMs: retrieval-augmented
generation, agents, structured output, and the vector search beneath
them. It expects a harness build in progress and access to the target's
dependency manifests. Per-tool content is one line plus a URL — install
commands and API details are always fetched from the recorded entry
point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the application stack: dependency manifests and imports
   (`langchain`, `llama_index`, `haystack`, `dspy`, `autogen`,
   `crewai`, `pydantic_ai`, `litellm`, `mcp`), LLM API clients and keys
   in env files, and vector-store dependencies or services in compose
   files.
2. Read [rag-and-agents.md](references/rag-and-agents.md) when the
   target orchestrates LLM calls: RAG pipelines, agents, structured
   output, gateways, or guardrails.
3. Read [vector-search.md](references/vector-search.md) when the target
   embeds and retrieves: local ANN indexes or vector databases.
4. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
5. Record each detected tool the tables cover — name, one-line role,
   documentation entry point, and its llms.txt when present — wherever
   the harness keeps conventions.

Done when: every LLM-application framework and vector-search component
the target actually uses has a recorded, live documentation entry point,
and nothing recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: framework and vector-store
  selection is the user's decision.
- LLM-app docs sites publish llms.txt unusually often — probing is
  especially worth it in this domain.
- The same tool may appear in another domain skill's tables (Faiss also
  serves recommender retrieval); record it once per harness, not once
  per skill.
- Tools this skill does not list are out of scope — leave finding their
  docs to the agent; it is not this skill's job.
