---
title: LLM Evaluation & Observability
description: Benchmark harnesses for scoring model, RAG, and agent quality, plus tracing platforms for LLM calls in development and production.
tags: [machine-learning, llm, evaluation, mlops]
---

# LLM Evaluation & Observability

Fetch when the target runs benchmarks, scores model, RAG, or agent quality, or traces LLM calls in development or production. Each entry is one line and a documentation entry point; fetch task lists, runner details, and instrumentation guidance from the entry point, never from memory. No entry is a recommendation.

## Evaluation harnesses

| Tool | One line | Docs |
|---|---|---|
| lm-evaluation-harness | the widely used few-shot benchmark runner | <https://github.com/EleutherAI/lm-evaluation-harness> |
| HELM | Stanford's holistic evaluation framework | <https://crfm-helm.readthedocs.io/> |
| OpenCompass | large-scale LLM benchmark platform | <https://opencompass.readthedocs.io/> |
| VLMEvalKit | vision-language model evaluation | <https://github.com/open-compass/VLMEvalKit> |
| Ragas | RAG pipeline evaluation metrics | <https://docs.ragas.io/> — llms.txt: <https://docs.ragas.io/llms.txt> |
| DeepEval | unit-test-style LLM evaluation | <https://deepeval.com/docs/getting-started> — llms.txt: <https://deepeval.com/llms.txt> |
| Promptfoo | prompt and model comparison with red-teaming | <https://www.promptfoo.dev/docs/> — llms.txt: <https://www.promptfoo.dev/llms.txt> |
| Inspect AI | UK AISI's evaluation framework | <https://inspect.aisi.org.uk/> — llms.txt: <https://inspect.aisi.org.uk/llms.txt> |
| EvalPlus | rigorous code-generation benchmarks | <https://github.com/evalplus/evalplus> |

## Observability platforms

Both deploy as services or managed platforms — see their docs.

| Tool | One line | Docs |
|---|---|---|
| Arize Phoenix | open-source LLM tracing and evaluation | <https://arize.com/docs/phoenix> — llms.txt: <https://arize.com/docs/phoenix/llms.txt> |
| Langfuse | open-source LLM engineering platform: traces, evals, prompts | <https://langfuse.com/docs> — llms.txt: <https://langfuse.com/llms.txt> |

## Gotchas

- Hugging Face Evaluate and LightEval document under the Hugging Face docs root — see the [huggingface](huggingface.md) page rather than duplicating them here.
- LangSmith is recorded with the LLM-application stack — see the [llm-applications](llm-applications.md) page.
