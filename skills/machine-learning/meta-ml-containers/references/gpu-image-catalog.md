# GPU Image Families: Characteristics and Fit

Read when shortlisting which image family to enumerate. Characteristics are
stable; sizes, tag names, and version support are volatile — enumerate live
with the bundled scripts and confirm details from each entry point.

| Image family | Characteristics | Fits when | Entry |
|---|---|---|---|
| `nvcr.io/nvidia/pytorch` (NGC, monthly `yy.mm-py3` tags) | PyTorch preinstalled on NVIDIA's tuned stack: CUDA, cuDNN, NCCL, Transformer Engine, and performance libraries, validated together; large images | Multi-GPU training on NVIDIA servers where out-of-the-box tuned NCCL/CUDA matters more than image size | <https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch> |
| Other NGC framework images (JAX, TensorFlow, NeMo, Triton, RAPIDS, …) | Same tuned-stack model per framework or product | The project's framework or serving stack has a dedicated NGC image | <https://catalog.ngc.nvidia.com/> |
| `pytorch/pytorch` (Docker Hub, `-runtime` / `-devel` variants) | The PyTorch project's own slim images; `runtime` runs models, `devel` adds the CUDA toolchain for compiling extensions | Running or quick-starting on a single GPU (`runtime`), or building CUDA extensions such as flash-attention (`devel`) | <https://hub.docker.com/r/pytorch/pytorch> |
| `nvidia/cuda` (`base` / `runtime` / `devel` variants) + Python and torch installed by the project's own dependency manager | Only the CUDA layer comes from the image; every Python package comes from the project's lockfile | Reproducibility-first projects that already pin torch through uv or another lockfile and want the container to match it exactly | <https://hub.docker.com/r/nvidia/cuda> |
| `rocm/pytorch` | PyTorch on the ROCm stack | AMD GPUs | <https://hub.docker.com/r/rocm/pytorch> |
| `tensorflow/tensorflow` (`-gpu` variants) | The TensorFlow project's own images | TensorFlow projects | <https://hub.docker.com/r/tensorflow/tensorflow> |

Cross-cutting facts:

- **Preinstalled torch vs the project's lockfile is an either/or.** An image
  that ships its own framework build conflicts with a lockfile that pins the
  same framework: either the image's build is authoritative (the lockfile
  stops listing it — record that rule in the project's agent entrypoint) or
  the project installs everything from its lockfile onto a bare
  `nvidia/cuda` base.
- **NGC tag ↔ CUDA/driver compatibility** is published only in NVIDIA's
  framework-containers documentation (support matrix):
  <https://docs.nvidia.com/deeplearning/frameworks/>. The tag name alone
  does not state the minimum driver.
- **ROCm** version and device support live in the ROCm documentation root:
  <https://rocm.docs.amd.com/>.
