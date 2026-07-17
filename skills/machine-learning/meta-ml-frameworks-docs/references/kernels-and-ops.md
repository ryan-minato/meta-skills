# GPU Kernels & Compiled Ops

Read when the target ships custom GPU kernels or compiled extensions, or
depends on kernel-level libraries. One line and an entry point per tool;
fetch build flags and API details from the entry point. Triton here is
the GPU programming language — the NVIDIA inference server of the same
name is a different tool documented with the serving stack.

## Libraries

| Tool | One line | Docs |
|---|---|---|
| NumPy | the array API most kernel libraries interoperate with | <https://numpy.org/doc/> |
| CuPy | NumPy/SciPy-compatible arrays on CUDA and ROCm | <https://docs.cupy.dev/> |
| Triton | Python-embedded GPU kernel language and compiler | <https://triton-lang.org/> |
| einops | readable tensor rearrangement across frameworks | <https://einops.rocks/> |
| FlashAttention | fused exact-attention CUDA kernels | <https://github.com/Dao-AILab/flash-attention> |
| xFormers | composable transformer building blocks and memory-efficient attention | <https://facebookresearch.github.io/xformers/> |
| bitsandbytes | 8-bit/4-bit quantized optimizers and matmul | <https://huggingface.co/docs/bitsandbytes> — llms.txt: <https://huggingface.co/docs/bitsandbytes/llms.txt> |
| NVIDIA Transformer Engine | FP8/FP4 transformer kernels for NVIDIA GPUs | <https://docs.nvidia.com/deeplearning/transformer-engine/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| Liger Kernel | Triton kernels for LLM training efficiency | <https://github.com/linkedin/Liger-Kernel> |
| Numba | JIT compiler for numerical Python and CUDA kernels | <https://numba.readthedocs.io/> |
| Cython | C-compiled Python extensions | <https://cython.readthedocs.io/> |
