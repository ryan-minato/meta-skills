---
title: Numerical Computing & Statistics
description: Scientific-computing platforms, array and statistics libraries, and the math kernels and sparse solvers C/C++/Julia numerics link against.
tags: [scientific-computing, data-science, numerics]
---

# Numerical Computing & Statistics

Fetch when the target computes on arrays or runs statistical models, builds on a scientific-computing platform or language ecosystem, or links math kernels, sparse solvers, or C/C++ numerical libraries. Each entry is one line and a documentation entry point; fetch install commands and build flags from the entry point, never from memory. No entry is a recommendation.

## Platforms

MATLAB and Wolfram are commercial platforms; fetch licensing details from the entry point.

| Tool | One line | Docs |
|---|---|---|
| SciPy | linear algebra, optimization, statistics, and signal processing | <https://docs.scipy.org/doc/scipy/> |
| SymPy | symbolic mathematics in Python | <https://docs.sympy.org/> |
| Julia | the Julia language and standard library | <https://docs.julialang.org/> |
| Julia SciML | the SciML ecosystem's documentation hub | <https://docs.sciml.ai/> |
| MATLAB | MathWorks' numerical platform (commercial) | <https://www.mathworks.com/help/matlab/> |
| Wolfram Language | Mathematica's language reference (commercial) | <https://reference.wolfram.com/language/> — llms.txt: <https://reference.wolfram.com/llms.txt> |

## Arrays & Statistics

| Tool | One line | Docs |
|---|---|---|
| NumPy | the standard array library | <https://numpy.org/doc/> |
| statsmodels | statistical modeling and econometrics | <https://www.statsmodels.org/> |
| lifelines | survival analysis | <https://lifelines.readthedocs.io/> |

## Math Kernels & Sparse Solvers

Most install from system packages or source — fetch build details from the entry point.

| Tool | One line | Docs |
|---|---|---|
| Eigen | C++ template linear algebra | <https://libeigen.gitlab.io/> |
| Armadillo | C++ linear algebra with MATLAB-like syntax | <https://arma.sourceforge.net/> |
| Boost.Math | C++ special functions and statistics | <https://www.boost.org/doc/libs/release/libs/math/> |
| GNU Scientific Library | C routines across numerical analysis | <https://www.gnu.org/software/gsl/> |
| OpenBLAS | optimized open-source BLAS | <https://www.openblas.net/> |
| LAPACK | the dense linear-algebra reference | <https://www.netlib.org/lapack/> |
| ScaLAPACK | distributed-memory LAPACK | <https://www.netlib.org/scalapack/> |
| Intel oneMKL | Intel's math kernel library | <https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html> |
| FFTW | the fastest FFT in the West | <https://www.fftw.org/> |
| SuiteSparse | sparse-matrix factorization suite | <https://github.com/DrTimothyAldenDavis/SuiteSparse> |
| PETSc | scalable PDE and solver toolkit (with petsc4py) | <https://petsc.org/> |
| Trilinos | large-scale solver and discretization stack | <https://trilinos.github.io/> |
| hypre | parallel multigrid preconditioners | <https://hypre.readthedocs.io/> |
| SLEPc | large-scale eigenvalue solvers on PETSc | <https://slepc.upv.es/> |
| MUMPS | parallel sparse direct solver | <https://mumps-solver.org/> |
| SuperLU | sparse direct solvers (incl. SuperLU_DIST) | <https://github.com/xiaoyeli/superlu> |
| ARPACK-NG | large-scale eigenvalue problems | <https://github.com/opencollab/arpack-ng> |
| StaticArrays.jl | stack-allocated arrays for Julia | <https://juliaarrays.github.io/StaticArrays.jl/> |
| SpecialFunctions.jl | special functions for Julia | <https://specialfunctions.juliamath.org/> |

## Gotchas

- Several vendor doc portals (Intel, MathWorks) block automated fetches — a 403 from a script does not mean the entry point is dead; verify in a browser context before replacing it.
- JIT compilation, GPU arrays, and vendor GPU math libraries (Numba, Cython, CuPy, the CUDA/ROCm math libraries) live on the [gpu-kernels-and-compilers](gpu-kernels-and-compilers.md) page.
- Bayesian modeling (PyMC, ArviZ) lives on the probabilistic-and-causal page; classic ML for analysis (scikit-learn) lives on the tabular-and-automl page.
