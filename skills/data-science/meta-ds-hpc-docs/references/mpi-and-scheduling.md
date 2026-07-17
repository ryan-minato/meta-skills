# MPI, Workflow Managers & Cluster Schedulers

Read when the target passes messages, submits cluster jobs, or runs
scientific workflows. One line and an entry point per tool; schedulers
and MPI usually come from the cluster — fetch build and module details
from the entry point. No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| MPI Forum | the MPI standard itself | <https://www.mpi-forum.org/> |
| Open MPI | widely deployed open MPI implementation | <https://docs.open-mpi.org/> — llms.txt: <https://docs.open-mpi.org/llms.txt> |
| MPICH | the reference MPI implementation | <https://www.mpich.org/> |
| mpi4py | MPI bindings for Python | <https://mpi4py.readthedocs.io/> |
| MPI.jl | MPI bindings for Julia | <https://juliaparallel.org/MPI.jl/> |
| OpenMP | shared-memory parallelism directives | <https://www.openmp.org/> |
| Dask | parallel Python with cluster deployment | <https://docs.dask.org/> — llms.txt: <https://docs.dask.org/llms.txt> |
| Dask-Jobqueue | Dask clusters on Slurm/PBS/LSF | <https://jobqueue.dask.org/> |
| Ray | Python-native distributed compute | <https://docs.ray.io/> — llms.txt: <https://docs.ray.io/llms.txt> |
| Distributed.jl | Julia's built-in distributed computing | <https://docs.julialang.org/> |
| Dagger.jl | task-graph parallelism for Julia | <https://juliaparallel.org/Dagger.jl/> |
| Parsl | parallel workflows from Python apps | <https://parsl.readthedocs.io/> |
| Snakemake | reproducible workflow rules | <https://snakemake.readthedocs.io/> |
| Nextflow | dataflow pipelines for scientific computing | <https://docs.seqera.io/nextflow> — llms.txt: <https://docs.seqera.io/llms.txt> |
| Flyte | typed, versioned workflows on Kubernetes | <https://docs.flyte.org/> — llms.txt: <https://www.union.ai/llms.txt> |
| Slurm | the dominant HPC scheduler | <https://slurm.schedmd.com/> |
| OpenPBS | open PBS scheduler | <https://openpbs.org/> |
| IBM Spectrum LSF | IBM's cluster scheduler (commercial) | <https://www.ibm.com/docs/en/spectrum-lsf> |
| HTCondor | high-throughput computing scheduler | <https://htcondor.readthedocs.io/> |
| Kubernetes | container orchestration under many clusters | <https://kubernetes.io/docs/> |
