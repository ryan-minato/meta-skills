---
name: meta-ds-simulation-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  simulation or mathematical-optimization project to authoritative
  documentation entry points — optimization and solvers (CVXPY, Pyomo,
  JuMP, Ipopt, OR-Tools, Gurobi), differential equations (SUNDIALS,
  DifferentialEquations.jl, Diffrax), PDE and FEM frameworks (FEniCSx,
  Firedrake, deal.II, MFEM, OpenFOAM, Gmsh), and scientific
  visualization (VTK, PyVista, ParaView, Makie). Use when a harness
  build must record where the docs live for a project that solves
  optimization problems, integrates differential equations, or runs
  PDE/FEM simulations. Not for choosing between tools or recommending
  one, and not for base numerics, HPC scheduling, or physics-informed
  ML.
---

# Simulation & Optimization Documentation Map

This skill produces the documentation entry points a harness build
records for a simulation or optimization project. It expects a harness
build in progress and access to the target's dependency manifests and
build files. Per-tool content is one line plus a URL — install commands
and solver licensing are always fetched from the recorded entry point,
never recalled from memory — and nothing here is a recommendation: when
the target lacks a tool for a need, record the option list with URLs
and leave the choice to the user.

## Workflow

1. Detect the simulation stack: dependency manifests and imports
   (`cvxpy`, `pyomo`, `casadi`, `diffrax`), Julia `Project.toml`
   (JuMP, DifferentialEquations), solver binaries and licenses (Ipopt,
   Gurobi, CPLEX), mesh and case files (Gmsh `.geo`, OpenFOAM cases,
   FEniCS scripts), and visualization pipelines (VTK/ParaView).
2. Read
   [optimization-and-solvers.md](references/optimization-and-solvers.md)
   when the target formulates optimization or mathematical programs.
3. Read
   [differential-equations.md](references/differential-equations.md)
   when the target integrates ODEs/DAEs or models dynamical systems.
4. Read [pde-and-fem.md](references/pde-and-fem.md) when the target
   solves PDEs, meshes geometry, or runs multiphysics simulations.
5. Read
   [scientific-visualization.md](references/scientific-visualization.md)
   when the target renders meshes, volumes, or large scientific data.
6. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
7. Record each detected tool the tables cover — name, one-line role,
   documentation entry point, and its llms.txt when present — wherever
   the harness keeps conventions.

Done when: every optimization, differential-equation, PDE, and
visualization tool the target actually uses has a recorded, live
documentation entry point, and nothing recorded ranks or recommends
between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: solver and framework selection
  is the user's decision.
- Commercial solvers (Gurobi, CPLEX) need licenses — record the entry
  point and leave procurement to the user.
- The underlying sparse solvers (PETSc, Trilinos, MUMPS) belong to the
  numerics stack — record them once per harness, not once per skill.
- Tools this skill does not list are out of scope — leave finding their
  docs to the agent; it is not this skill's job.
