---
title: Hugging Face Ecosystem
description: Everything documented under the Hugging Face docs root plus HF-owned products — model, data, training, optimization, serving, and app libraries.
tags: [machine-learning, training, inference, llm]
---

# Hugging Face Ecosystem

Fetch when the target depends on any Hugging Face library, loads models or datasets from the Hub, or trains, serves, or demos models with Hub-side tooling. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Core Model, Data & File Libraries

| Tool | One line | Docs |
|---|---|---|
| Transformers | text, vision, speech, and multimodal models under one API | <https://huggingface.co/docs/transformers> — llms.txt: <https://huggingface.co/docs/transformers/llms.txt> |
| Diffusers | diffusion models for image, video, and audio generation | <https://huggingface.co/docs/diffusers> — llms.txt: <https://huggingface.co/docs/diffusers/llms.txt> |
| Sentence Transformers | embeddings, semantic retrieval, and rerankers | <https://sbert.net/> |
| timm | vision models, pretrained weights, and training components | <https://huggingface.co/docs/timm> — llms.txt: <https://huggingface.co/docs/timm/llms.txt> |
| Transformers.js | model inference in the browser and Node.js | <https://huggingface.co/docs/transformers.js> — llms.txt: <https://huggingface.co/docs/transformers.js/llms.txt> |
| Datasets | data loading, streaming, processing, and sharing | <https://huggingface.co/docs/datasets> — llms.txt: <https://huggingface.co/docs/datasets/llms.txt> |
| Tokenizers | high-performance tokenizers backed by Rust | <https://github.com/huggingface/tokenizers> |
| Safetensors | safe, fast model-weight serialization | <https://huggingface.co/docs/safetensors> — llms.txt: <https://huggingface.co/docs/safetensors/llms.txt> |
| huggingface_hub | the Hub's Python client | <https://huggingface.co/docs/huggingface_hub> — llms.txt: <https://huggingface.co/docs/huggingface_hub/llms.txt> |
| Hub (incl. Xet storage) | model, dataset, and Space hosting and its storage backend | <https://huggingface.co/docs/hub> — llms.txt: <https://huggingface.co/docs/hub/llms.txt> |

## Training, Evaluation & Optimization

| Tool | One line | Docs |
|---|---|---|
| Accelerate | device placement and multi-GPU/multi-node launch for PyTorch loops | <https://huggingface.co/docs/accelerate> — llms.txt: <https://huggingface.co/docs/accelerate/llms.txt> |
| PEFT | parameter-efficient finetuning (LoRA, AdaLoRA, IA³, prompt tuning) | <https://huggingface.co/docs/peft> — llms.txt: <https://huggingface.co/docs/peft/llms.txt> |
| TRL | LLM post-training: SFT, DPO, GRPO, KTO, reward models | <https://huggingface.co/docs/trl> — llms.txt: <https://huggingface.co/docs/trl/llms.txt> |
| AutoTrain | low-code training and finetuning | <https://huggingface.co/docs/autotrain> — llms.txt: <https://huggingface.co/docs/autotrain/llms.txt> |
| bitsandbytes | 8-bit/4-bit quantized optimizers and matmul | <https://huggingface.co/docs/bitsandbytes> — llms.txt: <https://huggingface.co/docs/bitsandbytes/llms.txt> |
| Kernels | optimized compute kernels loaded from the Hub | <https://huggingface.co/docs/kernels> — llms.txt: <https://huggingface.co/docs/kernels/llms.txt> |
| Optimum | ONNX Runtime, OpenVINO, quantization, and hardware-accelerated export | <https://huggingface.co/docs/optimum> — llms.txt: <https://huggingface.co/docs/optimum/llms.txt> |
| Evaluate | shared evaluation metrics | <https://huggingface.co/docs/evaluate> |
| LightEval | LLM evaluation harness across backends | <https://huggingface.co/docs/lighteval> — llms.txt: <https://huggingface.co/docs/lighteval/llms.txt> |

## Serving, Apps & Data Production

| Tool | One line | Docs |
|---|---|---|
| Text Generation Inference | LLM serving engine behind an HTTP API | <https://huggingface.co/docs/text-generation-inference> — llms.txt: <https://huggingface.co/docs/text-generation-inference/llms.txt> |
| Text Embeddings Inference | embedding and reranker serving | <https://huggingface.co/docs/text-embeddings-inference> — llms.txt: <https://huggingface.co/docs/text-embeddings-inference/llms.txt> |
| Inference Providers | one API over hosted and third-party inference | <https://huggingface.co/docs/inference-providers> — llms.txt: <https://huggingface.co/docs/inference-providers/llms.txt> |
| Inference Endpoints | dedicated managed inference deployments | <https://huggingface.co/docs/inference-endpoints> — llms.txt: <https://huggingface.co/docs/inference-endpoints/llms.txt> |
| Spaces | hosted model demos and apps | <https://huggingface.co/docs/hub/spaces> — llms.txt: <https://huggingface.co/docs/hub/llms.txt> |
| Gradio | interactive ML web UIs in Python | <https://gradio.app/docs> — llms.txt: <https://gradio.app/llms.txt> |
| smolagents | code agents, tool-calling agents, and MCP | <https://huggingface.co/docs/smolagents> — llms.txt: <https://huggingface.co/docs/smolagents/llms.txt> |
| LeRobot | robotics datasets, policy training, and hardware interfaces | <https://huggingface.co/docs/lerobot> — llms.txt: <https://huggingface.co/docs/lerobot/llms.txt> |
| Argilla | data labeling, feedback collection, and curation | <https://docs.argilla.io/> |
| Distilabel | synthetic, preference, and distillation data generation | <https://distilabel.argilla.io/> |
| Trackio | lightweight experiment tracking | <https://huggingface.co/docs/trackio> — llms.txt: <https://huggingface.co/docs/trackio/llms.txt> |
| Leaderboards | building and reading evaluation leaderboards on the Hub | <https://huggingface.co/docs/leaderboards> — llms.txt: <https://huggingface.co/docs/leaderboards/llms.txt> |

## Gotchas

- Most of the ecosystem's docs live under one root (`https://huggingface.co/docs`) — record the per-library entry point (`huggingface.co/docs/<library>`), not just the shared root, so links go straight to the right library.
- llms.txt files are likewise per-library (`huggingface.co/docs/<library>/llms.txt`), not one index for the whole docs root.
