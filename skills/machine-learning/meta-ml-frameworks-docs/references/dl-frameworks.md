# General DL & Tensor Frameworks

Read when the target depends on a deep-learning or tensor framework, or
needs one and the user must pick. One line and an entry point per
framework; fetch install commands and API details from the entry point,
never from memory. No entry is a recommendation.

## Frameworks

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

Framework choice is the user's: when the target has none, record the
options relevant to its constraints (hardware, deployment, ecosystem)
with these URLs and ask.
