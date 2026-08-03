---
title: HPC, MPI & Cluster Scheduling
description: MPI stacks, cluster schedulers, scientific workflow managers, and GPU/multi-node collective communication.
tags: [hpc, scientific-computing, distributed, gpu]
---

# HPC, MPI & Cluster Scheduling

Fetch when the target passes messages between processes, submits cluster jobs, runs scientific workflows, or communicates across GPUs or nodes. Each entry is one line and a documentation entry point; schedulers and MPI usually come from the cluster — fetch build, module, and topology details from the entry point, never from memory. No entry is a recommendation.

Dask and Ray are recorded on the [distributed-compute page](distributed-compute.md), Flyte on the [pipelines-and-mlops page](pipelines-and-mlops.md), and the parallel-I/O stack (HDF5 and friends) on the [dataframes-and-storage page](dataframes-and-storage.md). Framework-level distributed training (PyTorch Distributed, TensorFlow Distributed, JAX multi-host, DeepSpeed, Megatron-LM, NeMo) is covered on the [training-and-finetuning](training-and-finetuning.md) and [deep-learning-frameworks](deep-learning-frameworks.md) pages.

## MPI, Workflow Managers & Cluster Schedulers

| Tool | One line | Docs |
|---|---|---|
| MPI Forum | the MPI standard itself | <https://www.mpi-forum.org/> |
| Open MPI | widely deployed open MPI implementation | <https://docs.open-mpi.org/> — llms.txt: <https://docs.open-mpi.org/llms.txt> |
| MPICH | the reference MPI implementation | <https://www.mpich.org/> |
| mpi4py | MPI bindings for Python | <https://mpi4py.readthedocs.io/> |
| MPI.jl | MPI bindings for Julia | <https://juliaparallel.org/MPI.jl/> |
| OpenMP | shared-memory parallelism directives | <https://www.openmp.org/> |
| Dask-Jobqueue | Dask clusters on Slurm/PBS/LSF | <https://jobqueue.dask.org/> |
| Distributed.jl | Julia's built-in distributed computing | <https://docs.julialang.org/> |
| Dagger.jl | task-graph parallelism for Julia | <https://juliaparallel.org/Dagger.jl/> |
| Parsl | parallel workflows from Python apps | <https://parsl.readthedocs.io/> |
| Snakemake | reproducible workflow rules | <https://snakemake.readthedocs.io/> |
| Nextflow | dataflow pipelines for scientific computing | <https://docs.seqera.io/nextflow> — llms.txt: <https://docs.seqera.io/llms.txt> |
| Slurm | the dominant HPC scheduler | <https://slurm.schedmd.com/> |
| OpenPBS | open PBS scheduler | <https://openpbs.org/> |
| IBM Spectrum LSF | IBM's cluster scheduler (commercial) | <https://www.ibm.com/docs/en/spectrum-lsf> |
| HTCondor | high-throughput computing scheduler | <https://htcondor.readthedocs.io/> |
| Kubernetes | container orchestration under many clusters | <https://kubernetes.io/docs/> |

## GPU & Multi-Node Communication

| Tool | One line | Docs |
|---|---|---|
| NVIDIA NCCL | GPU collective communication | <https://docs.nvidia.com/deeplearning/nccl/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| AMD RCCL | ROCm collective communication | <https://rocm.docs.amd.com/projects/rccl/> |
| Intel oneCCL | oneAPI collective communication | <https://oneapi-src.github.io/oneCCL/> |
| Gloo | CPU collective library behind PyTorch | <https://github.com/pytorch/gloo> |
| UCX | unified communication framework (RDMA, shared memory) | <https://openucx.org/> |
| NVSHMEM | GPU-initiated partitioned global memory | <https://docs.nvidia.com/nvshmem/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| libfabric | the OpenFabrics interface layer | <https://ofiwg.github.io/libfabric/> |

## Gotchas

- MPI implementation and scheduler selection is usually the cluster's, not the project's — record what the site runs.
- Cluster-provided modules (MPI, HDF5) often differ from pip-installed builds — record both the entry point and the site's module convention when one exists.
