---
title: Optimization, Differential Equations & FEM
description: Mathematical-programming solvers, ODE/DAE integrators, and PDE/FEM/multiphysics frameworks.
tags: [scientific-computing, simulation, numerics]
---

# Optimization, Differential Equations & FEM

Fetch when the target formulates optimization or mathematical programs, integrates ODEs/DAEs or models dynamical systems, or solves PDEs, meshes geometry, or runs multiphysics simulations. Each entry is one line and a documentation entry point; many of these install from source, containers, or system packages — fetch install, build, and licensing details from the entry point, never from memory. No entry is a recommendation.

SciPy is not listed here — its `scipy.optimize` and `scipy.integrate` modules document under the SciPy entry point on the [numerical-computing page](numerical-computing.md). The sparse solvers underneath the FEM stacks (PETSc, Trilinos, hypre, SLEPc, MUMPS, SuperLU_DIST) are also recorded there. The scientific-visualization tools (VTK, PyVista, ParaView, Makie) live on the [visualization-and-apps page](visualization-and-apps.md).

## Optimization & Mathematical Programming

| Tool | One line | Docs |
|---|---|---|
| NLopt | nonlinear optimization across languages | <https://nlopt.readthedocs.io/> |
| Ipopt | interior-point nonlinear programming | <https://coin-or.github.io/Ipopt/> |
| Ceres Solver | nonlinear least squares at scale | <http://ceres-solver.org/> |
| Optimization.jl | SciML's unified optimization interface | <https://docs.sciml.ai/Optimization/> |
| CVXPY | convex optimization modeling in Python | <https://www.cvxpy.org/> |
| Pyomo | algebraic modeling for mathematical programs | <https://pyomo.readthedocs.io/> |
| JuMP.jl | algebraic modeling in Julia | <https://jump.dev/> |
| CasADi | symbolic optimization with automatic differentiation | <https://web.casadi.org/> |
| Google OR-Tools | routing, scheduling, and CP-SAT | <https://developers.google.com/optimization> |
| HiGHS | open LP/MIP/QP solver | <https://highs.dev/> |
| OSQP | operator-splitting QP solver | <https://osqp.org/> |
| SCS | conic solver for large problems | <https://www.cvxgrp.org/scs/> |
| Gurobi | commercial MIP/LP solver | <https://docs.gurobi.com/> |
| CPLEX | IBM's commercial optimization suite | <https://www.ibm.com/docs/en/icos> |

## Differential Equations & Dynamical Systems

| Tool | One line | Docs |
|---|---|---|
| SUNDIALS | CVODE, ARKODE, IDA, and KINSOL solver suite | <https://sundials.readthedocs.io/> |
| DifferentialEquations.jl | Julia's differential-equation suite | <https://docs.sciml.ai/DiffEqDocs/> |
| Diffrax | differentiable ODE/SDE solvers in JAX | <https://docs.kidger.site/diffrax/> |
| torchdiffeq | differentiable ODE solvers for PyTorch | <https://github.com/rtqichen/torchdiffeq> |
| ModelingToolkit.jl | symbolic-numeric system modeling | <https://docs.sciml.ai/ModelingToolkit/> |
| OpenModelica | open Modelica environment for system modeling | <https://openmodelica.org/> |
| Simulink | MathWorks' block-diagram simulation (commercial) | <https://www.mathworks.com/help/simulink/> |

## PDE, FEM & Multiphysics

| Tool | One line | Docs |
|---|---|---|
| FEniCSx | automated FEM from variational forms | <https://docs.fenicsproject.org/> |
| Firedrake | automated finite elements with code generation | <https://www.firedrakeproject.org/> |
| deal.II | C++ finite-element library | <https://dealii.org/> |
| MFEM | scalable C++ FEM with GPU support | <https://mfem.org/> |
| MOOSE Framework | multiphysics FEM platform | <https://mooseframework.inl.gov/> |
| OpenFOAM | finite-volume CFD toolbox | <https://www.openfoam.com/> |
| FreeFEM | high-level PDE language | <https://freefem.org/> |
| Gmsh | mesh generation with CAD kernel | <https://gmsh.info/> |
| meshio | mesh format conversion | <https://github.com/nschloe/meshio> |
| CGAL | computational-geometry algorithms in C++ | <https://www.cgal.org/> |
| Open CASCADE | the open CAD kernel | <https://dev.opencascade.org/> |

## Gotchas

- Commercial solvers (Gurobi, CPLEX) need licenses — record the entry point and leave procurement to the user.
