# Quantization & Compression

Read when the target quantizes, prunes, or otherwise compresses models.
One line and an entry point per tool; fetch supported schemes and API
details from the entry point. No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| PyTorch torchao | PyTorch-native quantization and sparsity | <https://github.com/pytorch/ao> |
| TensorFlow Model Optimization | quantization and pruning for TensorFlow | <https://www.tensorflow.org/model_optimization> |
| NVIDIA Model Optimizer | quantization, distillation, and pruning for NVIDIA deployment | <https://nvidia.github.io/Model-Optimizer/> |
| Intel Neural Compressor | quantization across Intel hardware | <https://intel.github.io/neural-compressor/> |
| OpenVINO NNCF | compression for OpenVINO deployment | <https://github.com/openvinotoolkit/nncf> |
| bitsandbytes | 8-bit/4-bit quantized inference and optimizers | <https://huggingface.co/docs/bitsandbytes> |
| GPTQModel | GPTQ post-training quantization for LLMs | <https://github.com/ModelCloud/GPTQModel> |
| AutoAWQ | AWQ activation-aware quantization for LLMs | <https://github.com/casper-hansen/AutoAWQ> |
| SparseML | sparsification recipes for inference speedup | <https://github.com/neuralmagic/sparseml> |

GGUF quantization lives in llama.cpp's docs, recorded from
[llm-inference-engines.md](llm-inference-engines.md).
