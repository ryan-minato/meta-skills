---
name: meta-ds-numerics-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  numerical-computing project to authoritative documentation entry
  points — scientific platforms (SciPy, SymPy, Julia SciML, MATLAB,
  Wolfram), math kernels and sparse solvers (BLAS/LAPACK, FFTW, CUDA and
  ROCm math libraries, PETSc, Trilinos), and compilers and automatic
  differentiation (LLVM/MLIR, Numba, JAX, Kokkos, Enzyme, Julia AD). Use
  when a harness build must record where the docs live for a project
  doing numerical, symbolic, or GPU-accelerated computation. Not for
  choosing between tools or recommending one, and not for dataframe
  analysis, simulation frameworks, or cluster scheduling.
---

# Numerical Computing Documentation Map

This skill produces the documentation entry points a harness build
records for a numerical- or symbolic-computing project. It expects a
harness build in progress and access to the target's dependency
manifests and build files. Per-tool content is one line plus a URL —
install commands and build flags are always fetched from the recorded
entry point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the numerics stack: dependency manifests and imports
   (`scipy`, `sympy`, `numba`, `cython`, `jax`), Julia `Project.toml`,
   MATLAB/Wolfram sources, C/C++ build files linking BLAS/LAPACK/FFTW,
   and CUDA/ROCm toolchains in build or CI configs.
2. Read [platforms.md](references/platforms.md) when the target builds
   on a scientific-computing platform or language ecosystem.
3. Read
   [numerics-and-math-kernels.md](references/numerics-and-math-kernels.md)
   when the target links math kernels, sparse solvers, or C/C++
   numerical libraries.
4. Read
   [compilers-and-autodiff.md](references/compilers-and-autodiff.md)
   when the target JIT-compiles numerical code, targets GPUs directly,
   or differentiates programs.
5. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
6. Record each detected tool the tables cover — name, one-line role,
   documentation entry point, and its llms.txt when present — wherever
   the harness keeps conventions.

Done when: every numerical library, kernel, and compiler the target
actually uses has a recorded, live documentation entry point, and
nothing recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: platform and kernel selection is
  the user's decision.
- Several vendor doc portals (Intel, MathWorks) block automated fetches
  — a 403 from a script does not mean the entry point is dead; verify
  in a browser context before replacing it.
- The same tool may appear in another domain skill's tables (NumPy,
  Numba, PETSc); record it once per harness, not once per skill.
- Tools this skill does not list are out of scope — leave finding their
  docs to the agent; it is not this skill's job.
