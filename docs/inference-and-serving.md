---
title: Inference Engines & Model Serving
description: LLM inference engines, local runtimes, and model-serving platforms for running models locally or behind an API.
tags: [machine-learning, inference, llm]
---

# Inference Engines & Model Serving

Fetch when the target runs LLMs locally, serves them at scale, or serves models behind an API or on Kubernetes. Each entry is one line and a documentation entry point; fetch install commands, server flags, and deployment manifests from the entry point, never from memory. No entry is a recommendation.

## LLM inference engines & local runtimes

Most engines here install from PyPI; Ollama and llama.cpp ship binaries — see their docs.

| Tool | One line | Docs |
|---|---|---|
| vLLM | high-throughput LLM serving with PagedAttention | <https://docs.vllm.ai/> |
| SGLang | fast LLM serving with RadixAttention and structured output | <https://docs.sglang.io/> — llms.txt: <https://docs.sglang.io/llms.txt> |
| NVIDIA TensorRT-LLM | TensorRT-compiled LLM inference on NVIDIA GPUs | <https://nvidia.github.io/TensorRT-LLM/> |
| llama.cpp | CPU/GPU LLM inference in C/C++ with GGUF models | <https://github.com/ggml-org/llama.cpp> |
| Ollama | packaged local LLM runtime with a simple API (binary install) | <https://docs.ollama.com/> — llms.txt: <https://docs.ollama.com/llms.txt> |
| MLX-LM | LLM inference and finetuning on Apple silicon | <https://github.com/ml-explore/mlx-lm> |
| ONNX Runtime GenAI | generative-AI loop on ONNX Runtime | <https://onnxruntime.ai/docs/genai/> |
| OpenVINO GenAI | generative-AI pipelines on OpenVINO | <https://docs.openvino.ai/> |
| MLC LLM | ML-compiled LLM deployment across platforms | <https://llm.mlc.ai/docs/> |

## Serving platforms

Triton Inference Server, KServe, and Seldon deploy as containers/operators — see their docs.

| Tool | One line | Docs |
|---|---|---|
| NVIDIA Triton Inference Server | multi-framework, multi-model GPU serving | <https://docs.nvidia.com/deeplearning/triton-inference-server/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| KServe | Kubernetes-native model inference CRDs | <https://kserve.github.io/website/> |
| BentoML | package and serve models as APIs | <https://docs.bentoml.com/> |
| Seldon Core | Kubernetes model deployment and inference graphs | <https://docs.seldon.ai/> — llms.txt: <https://docs.seldon.ai/home/llms.txt> |
| TensorFlow Serving | production serving for TensorFlow models | <https://github.com/tensorflow/serving> |
| TorchServe | model serving for PyTorch | <https://docs.pytorch.org/serve/> |
| MLServer | multi-framework inference server behind Seldon and KServe | <https://docs.seldon.ai/mlserver> — llms.txt: <https://docs.seldon.ai/mlserver/llms.txt> |
| FastAPI | general Python API framework often wrapping model inference | <https://fastapi.tiangolo.com/> |

## Gotchas

- Two Tritons exist: the NVIDIA Triton Inference Server lives on this page; the Triton GPU kernel language is on the [gpu-kernels-and-compilers](gpu-kernels-and-compilers.md) page — name which one the harness records.
- Hugging Face Text Generation Inference (TGI) and Text Embeddings Inference (TEI) document under the Hugging Face docs root — see the [huggingface](huggingface.md) page. Gradio is also recorded there.
- Streamlit app serving is recorded on the [visualization-and-apps](visualization-and-apps.md) page; Ray Serve is recorded with the Ray stack on the distributed-compute page.
