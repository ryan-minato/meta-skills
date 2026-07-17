# Compilers, GPU Toolchains & Automatic Differentiation

Read when the target JIT-compiles numerical code, targets GPUs
directly, or differentiates programs. One line and an entry point per
tool; fetch toolchain and install details from the entry point. No
entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| LLVM | the compiler infrastructure | <https://llvm.org/docs/> |
| MLIR | multi-level IR for domain compilers | <https://mlir.llvm.org/> |
| JAX | composable transforms and XLA compilation | <https://docs.jax.dev/> |
| Triton | Python-embedded GPU kernel language | <https://triton-lang.org/> |
| CUDA | NVIDIA's GPU computing toolkit | <https://docs.nvidia.com/cuda/> — llms.txt: <https://docs.nvidia.com/cuda/llms.txt> |
| ROCm | AMD's GPU computing platform (HIP) | <https://rocm.docs.amd.com/> |
| SYCL | Khronos' C++ heterogeneous-compute standard | <https://www.khronos.org/sycl/> |
| Kokkos | performance-portable C++ parallelism | <https://kokkos.org/> |
| OpenMP | shared-memory parallelism directives | <https://www.openmp.org/> |
| CUDA.jl | NVIDIA GPUs from Julia | <https://cuda.juliagpu.org/> |
| AMDGPU.jl | AMD GPUs from Julia | <https://amdgpu.juliagpu.org/> |
| KernelAbstractions.jl | vendor-portable Julia GPU kernels | <https://juliagpu.github.io/KernelAbstractions.jl/> |
| CasADi | symbolic framework for optimization with AD | <https://web.casadi.org/> |
| Enzyme | LLVM-level automatic differentiation | <https://enzyme.mit.edu/> |
| ForwardDiff.jl | forward-mode AD for Julia | <https://juliadiff.org/ForwardDiff.jl/> |
| Zygote.jl | reverse-mode AD for Julia | <https://fluxml.ai/Zygote.jl/> |
| SciMLSensitivity.jl | sensitivities of differential-equation solves | <https://docs.sciml.ai/SciMLSensitivity/> |
| Diffrax | differentiable ODE/SDE solvers in JAX | <https://docs.kidger.site/diffrax/> |
| torchdiffeq | differentiable ODE solvers for PyTorch | <https://github.com/rtqichen/torchdiffeq> |
