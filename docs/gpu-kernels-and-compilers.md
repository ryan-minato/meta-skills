---
title: GPU Kernels, Compilers & Autodiff
description: JIT compilers, GPU kernel languages and toolchains, kernel-level libraries, and automatic differentiation of programs.
tags: [scientific-computing, machine-learning, gpu, numerics]
---

# GPU Kernels, Compilers & Autodiff

Fetch when the target JIT-compiles numerical code, targets GPUs directly, ships custom GPU kernels or compiled extensions, or differentiates programs. Each entry is one line and a documentation entry point; fetch toolchain, build-flag, and install details from the entry point, never from memory. No entry is a recommendation.

NumPy lives on the [numerical-computing page](numerical-computing.md); JAX on the [deep-learning-frameworks page](deep-learning-frameworks.md); Diffrax and torchdiffeq on the [optimization-and-simulation page](optimization-and-simulation.md); OpenMP on the [hpc-and-scheduling page](hpc-and-scheduling.md); bitsandbytes on the [huggingface page](huggingface.md).

## Compilers & GPU Toolchains

| Tool | One line | Docs |
|---|---|---|
| LLVM / MLIR | the compiler infrastructure and its multi-level IR for domain compilers | <https://llvm.org/docs/> — MLIR: <https://mlir.llvm.org/> |
| Triton | Python-embedded GPU kernel language and compiler | <https://triton-lang.org/> |
| CUDA | NVIDIA's GPU computing toolkit — cuBLAS, cuSOLVER, cuSPARSE, cuFFT under the CUDA docs | <https://docs.nvidia.com/cuda/> — llms.txt: <https://docs.nvidia.com/cuda/llms.txt> |
| ROCm | AMD's GPU computing platform (HIP) — rocBLAS, rocSOLVER, rocSPARSE, rocFFT under the ROCm docs | <https://rocm.docs.amd.com/> |
| SYCL | Khronos' C++ heterogeneous-compute standard | <https://www.khronos.org/sycl/> |
| Kokkos | performance-portable C++ parallelism | <https://kokkos.org/> |
| Numba | JIT compiler for numerical Python and CUDA kernels | <https://numba.readthedocs.io/> |
| Cython | C-compiled Python extensions | <https://cython.readthedocs.io/> |
| CUDA.jl | NVIDIA GPUs from Julia | <https://cuda.juliagpu.org/> |
| AMDGPU.jl | AMD GPUs from Julia | <https://amdgpu.juliagpu.org/> |
| KernelAbstractions.jl | vendor-portable Julia GPU kernels | <https://juliagpu.github.io/KernelAbstractions.jl/> |

## Kernel Libraries & Compiled Ops

| Tool | One line | Docs |
|---|---|---|
| CuPy | NumPy/SciPy-compatible arrays on CUDA and ROCm | <https://docs.cupy.dev/> |
| einops | readable tensor rearrangement across frameworks | <https://einops.rocks/> |
| FlashAttention | fused exact-attention CUDA kernels | <https://github.com/Dao-AILab/flash-attention> |
| xFormers | composable transformer building blocks and memory-efficient attention | <https://facebookresearch.github.io/xformers/> |
| NVIDIA Transformer Engine | FP8/FP4 transformer kernels for NVIDIA GPUs | <https://docs.nvidia.com/deeplearning/transformer-engine/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| Liger Kernel | Triton kernels for LLM training efficiency | <https://github.com/linkedin/Liger-Kernel> |

## Automatic Differentiation

| Tool | One line | Docs |
|---|---|---|
| Enzyme | LLVM-level automatic differentiation | <https://enzyme.mit.edu/> |
| ForwardDiff.jl | forward-mode AD for Julia | <https://juliadiff.org/ForwardDiff.jl/> |
| Zygote.jl | reverse-mode AD for Julia | <https://fluxml.ai/Zygote.jl/> |
| SciMLSensitivity.jl | sensitivities of differential-equation solves | <https://docs.sciml.ai/SciMLSensitivity/> |

## Gotchas

- Two different Tritons exist — this page's Triton is the GPU kernel language and compiler; the NVIDIA Triton Inference Server is a different tool, recorded on the [inference-and-serving page](inference-and-serving.md).
- A repository README is a legitimate entry point for projects without a docs site — record the repository root, not a guessed docs domain.
