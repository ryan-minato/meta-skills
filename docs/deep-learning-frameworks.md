---
title: Deep Learning Frameworks
description: General DL and tensor frameworks — PyTorch, TensorFlow, Keras, JAX and its ecosystem, MLX — and their documentation roots.
tags: [machine-learning, training]
---

# Deep Learning Frameworks

Fetch when the target depends on a deep-learning or tensor framework, or needs one and the user must pick from the options. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| PyTorch | dynamic-graph tensor framework; the largest model ecosystem | <https://docs.pytorch.org/> |
| TensorFlow | graph-compiled ML platform with production tooling | <https://www.tensorflow.org/> |
| Keras | high-level model API running on JAX, TensorFlow, or PyTorch | <https://keras.io/> |
| KerasHub | pretrained model library for Keras | <https://keras.io/keras_hub/> |
| KerasCV | Keras computer-vision components | <https://keras.io/keras_cv/> |
| KerasTuner | hyperparameter search for Keras models | <https://keras.io/keras_tuner/> |
| JAX | composable function transforms (grad, jit, vmap) on XLA | <https://docs.jax.dev/> |
| Flax | neural-network library for JAX | <https://flax.readthedocs.io/> |
| Optax | gradient-transformation and optimizer library for JAX | <https://optax.readthedocs.io/> |
| Orbax | checkpointing and persistence for JAX | <https://orbax.readthedocs.io/> |
| Equinox | JAX models as callable PyTrees | <https://docs.kidger.site/equinox/> |
| MLX | array framework for Apple silicon | <https://ml-explore.github.io/mlx/> |
| PaddlePaddle | Baidu's DL framework and toolchain | <https://www.paddlepaddle.org.cn/en> |
| tinygrad | minimal tensor framework targeting many accelerators | <https://docs.tinygrad.org/> |

## Gotchas

- A repository README is a legitimate entry point for frameworks without a docs site — record the repository root, not a guessed docs domain.
- PyTorch's distributed APIs (DDP, FSDP, collectives) document inside its root above; multi-node training stacks built on top live on the [training-and-finetuning](training-and-finetuning.md) page.
- GPU-kernel and compiled-ops libraries (Triton, flash-attn, xformers, and the like) live on the [gpu-kernels-and-compilers](gpu-kernels-and-compilers.md) page.
