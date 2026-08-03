---
title: Quantization, Model Compilers & Edge Runtimes
description: Quantization and compression toolkits plus model compilers and cross-platform runtimes for compiled, mobile, and edge deployment.
tags: [machine-learning, inference, gpu]
---

# Quantization, Model Compilers & Edge Runtimes

Fetch when the target quantizes, prunes, or otherwise compresses models, or exports them to a compiled or cross-platform runtime, including mobile and edge. Each entry is one line and a documentation entry point; fetch supported schemes, export flows, and runtime APIs from the entry point, never from memory. No entry is a recommendation.

## Quantization & compression

| Tool | One line | Docs |
|---|---|---|
| PyTorch torchao | PyTorch-native quantization and sparsity | <https://github.com/pytorch/ao> |
| TensorFlow Model Optimization | quantization and pruning for TensorFlow | <https://www.tensorflow.org/model_optimization> |
| NVIDIA Model Optimizer | quantization, distillation, and pruning for NVIDIA deployment | <https://nvidia.github.io/Model-Optimizer/> |
| Intel Neural Compressor | quantization across Intel hardware | <https://intel.github.io/neural-compressor/> |
| OpenVINO NNCF | compression for OpenVINO deployment | <https://github.com/openvinotoolkit/nncf> |
| GPTQModel | GPTQ post-training quantization for LLMs | <https://github.com/ModelCloud/GPTQModel> |
| AutoAWQ | AWQ activation-aware quantization for LLMs | <https://github.com/casper-hansen/AutoAWQ> |
| SparseML | sparsification recipes for inference speedup | <https://github.com/neuralmagic/sparseml> |

## Compilers & cross-platform runtimes

| Tool | One line | Docs |
|---|---|---|
| ONNX | the open model-exchange format | <https://onnx.ai/> |
| ONNX Runtime | cross-platform accelerated ONNX inference | <https://onnxruntime.ai/> |
| NVIDIA TensorRT | optimizing compiler and runtime for NVIDIA GPUs | <https://docs.nvidia.com/deeplearning/tensorrt/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| OpenVINO | optimized inference across Intel hardware | <https://docs.openvino.ai/> |
| Apache TVM | ML compiler stack for many backends | <https://tvm.apache.org/> |
| OpenXLA / XLA | compiler powering JAX and TensorFlow | <https://openxla.org/> |
| IREE | MLIR-based compiler and minimal runtime | <https://iree.dev/> |
| LiteRT | on-device runtime (formerly TensorFlow Lite) | <https://developers.google.com/edge/litert> |
| ExecuTorch | PyTorch on-device inference | <https://docs.pytorch.org/executorch/> |
| Core ML Tools | model conversion for Apple's Core ML | <https://apple.github.io/coremltools/> |
| NCNN | mobile-first inference framework | <https://github.com/Tencent/ncnn> |
| MNN | lightweight inference engine | <https://github.com/alibaba/MNN> |
| Paddle Lite | PaddlePaddle's edge runtime | <https://github.com/PaddlePaddle/Paddle-Lite> |
| DirectML | hardware-accelerated ML on DirectX 12 | <https://github.com/microsoft/DirectML> |

## Gotchas

- GGUF quantization lives in llama.cpp's docs — llama.cpp is recorded on the [inference-and-serving](inference-and-serving.md) page.
- bitsandbytes documents under the Hugging Face docs root — see the [huggingface](huggingface.md) page.
- MLIR itself is recorded with the compiler infrastructure on the [gpu-kernels-and-compilers](gpu-kernels-and-compilers.md) page.
