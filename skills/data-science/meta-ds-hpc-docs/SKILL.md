---
name: meta-ds-hpc-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps an HPC
  or multi-node computing project to authoritative documentation entry
  points — MPI, workflow managers, and cluster schedulers (Open MPI,
  mpi4py, Slurm, HTCondor, Snakemake, Nextflow), GPU and multi-node
  communication (NCCL, RCCL, UCX, PyTorch/JAX distributed), and
  scientific data and parallel I/O (HDF5, NetCDF, Zarr, ADIOS2, Arrow).
  Use when a harness build must record where the docs live for a project
  that runs on clusters, communicates across nodes or GPUs, or does
  parallel I/O. Not for choosing between tools or recommending one, and
  not for single-machine numerics, cluster analytics engines, or
  data-pipeline orchestrators.
---

# HPC & Parallel Computing Documentation Map

This skill produces the documentation entry points a harness build
records for an HPC project: message passing, scheduling, scientific
workflows, GPU communication, and parallel I/O. It expects a harness
build in progress and access to the target's dependency manifests, job
scripts, and cluster configs. Per-tool content is one line plus a URL —
build flags and module details are always fetched from the recorded
entry point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the HPC stack: dependency manifests and imports (`mpi4py`,
   `dask`, `parsl`, `snakemake`), job scripts (`sbatch`/`#SBATCH`, PBS,
   LSF, HTCondor submit files), workflow definitions (Snakefile,
   Nextflow pipelines), communication libraries in build configs (MPI,
   NCCL, UCX), and parallel data formats (HDF5, NetCDF, Zarr, ADIOS2).
2. Read [mpi-and-scheduling.md](references/mpi-and-scheduling.md) when
   the target passes messages, submits cluster jobs, or runs scientific
   workflows.
3. Read [gpu-communication.md](references/gpu-communication.md) when
   the target communicates across GPUs or nodes, including framework
   distributed backends.
4. Read [parallel-io.md](references/parallel-io.md) when the target
   reads or writes scientific data in parallel or from object storage.
5. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
6. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every MPI, scheduler, communication, and parallel-I/O tool
the target actually uses has a recorded, live documentation entry
point, and nothing recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: MPI implementation and
  scheduler selection is usually the cluster's, not the project's —
  record what the site runs.
- Cluster-provided modules (MPI, HDF5) often differ from pip-installed
  builds — record both the entry point and the site's module convention
  when one exists.
- The same tool may appear in another domain skill's tables (Dask, Ray,
  xarray, Arrow, fsspec); record it once per harness, not once per
  skill.
- Tools this skill does not list are out of scope: record only what its
  tables cover, and leave finding docs for anything else to the agent —
  it is not this skill's job.
