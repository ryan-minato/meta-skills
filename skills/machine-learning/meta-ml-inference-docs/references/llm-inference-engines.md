# LLM Inference Engines & Local Runtimes

Read when the target runs LLMs locally or serves them at scale. One line
and an entry point per tool; fetch install commands and server flags
from the entry point. Most engines here install from PyPI; Ollama and
llama.cpp ship binaries — see their docs. No entry is a recommendation.

## Engines

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
