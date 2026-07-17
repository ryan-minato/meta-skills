# Containerized Environments

Read when the user asks for a containerized dev environment or for
training to run on a server or in a container. Never scaffold either
unprompted.

## Is a container needed at all?

When `uv sync` works directly on the target machine, skip containers.
Legitimate reasons to add one: the server's environment is not yours to
control, CUDA/driver versions drift between machines, the team needs
identical dev environments, or the deployment platform demands an image.
The dev container and the training image are two independent decisions —
take either without the other.

## Base image

| Image | Positioning | Entry |
|---|---|---|
| `nvidia/cuda` (`base`/`runtime`/`devel` variants) + Python and packages from this project's `uv.lock` — the default here | Only the CUDA layer comes from the image; the environment equals the committed lockfile, which is this scaffold's whole reproducibility story | <https://hub.docker.com/r/nvidia/cuda> |
| `nvcr.io/nvidia/pytorch` (NGC) | NVIDIA's tuned full stack (CUDA, cuDNN, NCCL) with torch preinstalled; large | <https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch> |
| `pytorch/pytorch` (`-runtime`/`-devel`) | The PyTorch project's slim images, torch preinstalled | <https://hub.docker.com/r/pytorch/pytorch> |
| `rocm/pytorch` | AMD GPUs | <https://hub.docker.com/r/rocm/pytorch> |

Preinstalled-torch images conflict with the lockfile: either the image's
torch is authoritative (drop torch from `pyproject.toml` and record that
rule in AGENTS.md) or — the default — build on `nvidia/cuda` and
`uv sync --frozen` the whole environment. Tags are always enumerated live
from the registry, never assumed.

## GPU access

- Host prerequisite for NVIDIA: the NVIDIA Container Toolkit —
  <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/>.
  AMD needs the kernel driver plus device nodes only.
- `docker run`: `--gpus all` (or `--gpus 'device=N'` to expose a subset);
  ROCm passes devices through with `--device /dev/kfd --device /dev/dri`.
- Compose: a device reservation under the service
  (`deploy.resources.reservations.devices` with `driver: nvidia` and
  `capabilities: [gpu]`); current syntax from the Compose docs,
  <https://docs.docker.com/compose/>.
- Dev container: declare `"hostRequirements": {"gpu": "optional"}` and
  nothing else — implementations inject `--gpus all` when a GPU runtime
  is present and skip it otherwise, so one config serves GPU and
  CPU-only machines. Two known limits (spec: <https://containers.dev/>):
  detection keys on the *runtime*, so a machine with the NVIDIA runtime
  but no GPU can fail to start; and compose-based dev containers ignore
  the field. In both cases fall back to explicit
  `"runArgs": ["--gpus", "all"]`, accepting the config then only works
  on GPU machines.
- DataLoader workers exhaust Docker's default shared memory: raise it
  (`--shm-size`, compose `shm_size`, or `ipc: host`) in any training
  container.

## Volumes and data

Mount `data/`, `outputs/`, and the Hugging Face cache directory as
volumes. Images contain the environment only — never data, checkpoints,
or credentials. Record the container-path ↔ config-path mapping in
AGENTS.md.

## Assets

- Dev environment → copy the `assets/devcontainer.md` skeleton.
- Training image and runner → copy the `assets/docker-training.md`
  skeleton.
