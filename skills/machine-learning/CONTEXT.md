# machine-learning — Catalog Context

Read this before authoring or reviewing anything in
`skills/machine-learning/`. Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `machine-learning`. Neither this
file nor the catalog READMEs ship to targets — installers copy skill
directories only.

## Goal

`machine-learning` holds information skills for ML target projects:
authoritative documentation entry points for the frameworks, libraries,
and tools an ML project uses or is likely to need, plus the discovery
procedure for anything not listed. A harness-building agent detects which
domains the target belongs to (from manifests, imports, and configs),
loads only the matching skills, and records where the docs live. It
installs per project, on top of `core`, and only when the target trains,
finetunes, serves, or builds on machine-learning models — it is not part
of the default install. Recommendations and guidance are future, separate
skills in this catalog; the skills here only inform.

## Constraints On What May Enter

- **ML-only usefulness.** A skill belongs here only if it is useless to a
  project that does no machine learning. Anything useful regardless of
  stack belongs in `core`; general data analysis and scientific computing
  belong in `data-science`.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Information, not recommendation.** Unlike `python`, which records
  trusted defaults, no skill in this catalog may record a default, a
  ranking, or a "prefer X". Skills report what exists and where its docs
  live; every choice between tools stays with the user. A future
  recommendation skill that breaks this rule must say so in its own
  description, not hide inside a docs skill.
- **One domain per skill.** A skill's boundary is a project domain with a
  detectable trigger (dependencies, imports, config files), so an agent
  loads exactly the domains the target belongs to. Finer splits live
  behind per-reference load conditions; a skill that mixes unrelated
  domains gets split, not grown.
- **Doc-root fidelity.** Only stable entry points: a docs root, an org
  root, or a repository root. Volatile facts (versions, install commands,
  API pages, deep links) always defer to a fetch from the entry point. A
  dead or moved URL is a bug, fixed in the same change that finds it.
- **Registry completeness.** Every URL any reference cites appears in
  this file's Upstream Registry, in the section mirroring its reference
  table. A URL in a skill but not the registry is a bug.
- **Sibling-catalog overlap is intentional.** Tools shared with
  `data-science` (NumPy, scikit-learn, statsmodels, Dask, Faiss, …) are
  recorded independently in both catalogs, because skills are
  self-contained and never reference the sibling catalog.

## Authoring

Start from the authoring skill's template
(`.agents/skills/meta-skill-authoring/assets/skill-template.md`), which
ships with the marker pre-filled. The marker's exact bytes and YAML form
are defined in the contract; copy them from there, never from rendered
documentation. Skill names use the `meta-ml-<domain>-docs` pattern — the
`-docs` suffix reserves the domain name for future scaffolding or
recommendation skills. Every skill carries `references/doc-discovery.md`,
byte-identical across the catalog (and across `data-science`); the
canonical copy is
`skills/machine-learning/meta-ml-frameworks-docs/references/doc-discovery.md`,
and any change to it is copied to every sibling in the same change
(`sha256sum` across the copies is the review check).

## References

- llms.txt specification (agent-preferred plain-text doc indexes) —
  <https://llmstxt.org/>
- PyPI JSON API (package metadata → project homepage and doc URLs) —
  <https://docs.pypi.org/api/json/>
- Agent Skills specification — reachable through the `agentskills` MCP
  server.

## Upstream Registry

Every doc URL the catalog's skills cite — a maintainer snapshot, last
verified live 2026-07-17. The URL is authoritative: when this table and
a tool's docs disagree, the docs win and this file updates in the same
change. Sites that publish an
`llms.txt` plain-text index (agent-preferred; probe `<docs-root>/llms.txt`,
then `llms-full.txt`) are marked; re-probe the others when refreshing
this table. PyPI packages install with `pip install <package>` (or the
project's own manager); non-PyPI tools carry an install pointer in their
skill's reference table, with details always fetched from the doc URL.

Sections mirror the catalog's skills and their reference tables, in
order; each skill's rows land in the same change that adds the skill.

### meta-ml-frameworks-docs

#### dl-frameworks.md

| Tool | Docs |
|---|---|
| PyTorch | <https://docs.pytorch.org/> |
| TensorFlow | <https://www.tensorflow.org/> |
| Keras | <https://keras.io/> |
| KerasHub | <https://keras.io/keras_hub/> |
| KerasCV | <https://keras.io/keras_cv/> |
| KerasTuner | <https://keras.io/keras_tuner/> |
| JAX | <https://docs.jax.dev/> |
| Flax | <https://flax.readthedocs.io/> |
| Optax | <https://optax.readthedocs.io/> |
| Orbax | <https://orbax.readthedocs.io/> |
| Equinox | <https://docs.kidger.site/equinox/> |
| MLX | <https://ml-explore.github.io/mlx/> |
| PaddlePaddle | <https://www.paddlepaddle.org.cn/en> |
| tinygrad | <https://docs.tinygrad.org/> |

#### kernels-and-ops.md

| Tool | Docs |
|---|---|
| NumPy | <https://numpy.org/doc/> |
| CuPy | <https://docs.cupy.dev/> |
| Triton | <https://triton-lang.org/> |
| einops | <https://einops.rocks/> |
| FlashAttention | <https://github.com/Dao-AILab/flash-attention> |
| xFormers | <https://facebookresearch.github.io/xformers/> |
| bitsandbytes | <https://huggingface.co/docs/bitsandbytes> |
| NVIDIA Transformer Engine | <https://docs.nvidia.com/deeplearning/transformer-engine/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| Liger Kernel | <https://github.com/linkedin/Liger-Kernel> |
| Numba | <https://numba.readthedocs.io/> |
| Cython | <https://cython.readthedocs.io/> |

### meta-ml-training-docs

#### distributed-training.md

| Tool | Docs |
|---|---|
| PyTorch Distributed | <https://docs.pytorch.org/> |
| TorchTitan | <https://github.com/pytorch/torchtitan> |
| DeepSpeed | <https://www.deepspeed.ai/> |
| Megatron-LM | <https://github.com/NVIDIA/Megatron-LM> |
| Megatron-Core | <https://docs.nvidia.com/megatron-core/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| PyTorch Lightning | <https://lightning.ai/docs/pytorch/> — llms.txt: <https://lightning.ai/llms.txt> |
| NVIDIA NeMo Framework | <https://docs.nvidia.com/nemo-framework/> — llms.txt: <https://docs.nvidia.com/nemo-framework/llms.txt> |
| Colossal-AI | <https://colossalai.org/> |

#### finetuning.md

| Tool | Docs |
|---|---|
| torchtune | <https://meta-pytorch.org/torchtune/> |
| LLaMA-Factory | <https://llamafactory.readthedocs.io/> |
| Axolotl | <https://docs.axolotl.ai/> |
| Unsloth | <https://unsloth.ai/docs> — llms.txt: <https://unsloth.ai/docs/llms.txt> |
| OpenRLHF | <https://github.com/OpenRLHF/OpenRLHF> |

### meta-ml-huggingface-docs

#### core-libraries.md

| Tool | Docs |
|---|---|
| Transformers | <https://huggingface.co/docs/transformers> |
| Diffusers | <https://huggingface.co/docs/diffusers> |
| Sentence Transformers | <https://sbert.net/> |
| timm | <https://huggingface.co/docs/timm> |
| Transformers.js | <https://huggingface.co/docs/transformers.js> |
| Datasets | <https://huggingface.co/docs/datasets> |
| Tokenizers | <https://huggingface.co/docs/tokenizers> |
| Safetensors | <https://huggingface.co/docs/safetensors> |
| huggingface_hub | <https://huggingface.co/docs/huggingface_hub> |
| Hugging Face Hub (Xet storage) | <https://huggingface.co/docs/hub> |

#### training-and-optimization.md

| Tool | Docs |
|---|---|
| Accelerate | <https://huggingface.co/docs/accelerate> |
| PEFT | <https://huggingface.co/docs/peft> |
| TRL | <https://huggingface.co/docs/trl> |
| AutoTrain | <https://huggingface.co/docs/autotrain> |
| Kernels | <https://huggingface.co/docs/kernels> |
| Optimum | <https://huggingface.co/docs/optimum> |
| Evaluate | <https://huggingface.co/docs/evaluate> |
| LightEval | <https://huggingface.co/docs/lighteval> |

#### serving-and-apps.md

| Tool | Docs |
|---|---|
| Text Generation Inference | <https://huggingface.co/docs/text-generation-inference> |
| Text Embeddings Inference | <https://huggingface.co/docs/text-embeddings-inference> |
| Inference Providers | <https://huggingface.co/docs/inference-providers> |
| Inference Endpoints | <https://huggingface.co/docs/inference-endpoints> |
| Spaces | <https://huggingface.co/docs/hub/spaces> |
| Gradio | <https://gradio.app/docs> — llms.txt: <https://gradio.app/llms.txt> |
| smolagents | <https://huggingface.co/docs/smolagents> |
| LeRobot | <https://huggingface.co/docs/lerobot> |
| Argilla | <https://docs.argilla.io/> |
| Distilabel | <https://distilabel.argilla.io/> |
| Trackio | <https://huggingface.co/docs/trackio> |
| Leaderboards | <https://huggingface.co/docs/leaderboards> |

### meta-ml-ray-docs

#### ray-libraries.md

| Tool | Docs |
|---|---|
| Ray | <https://docs.ray.io/> — llms.txt: <https://docs.ray.io/llms.txt> |

#### kuberay-and-clusters.md

| Tool | Docs |
|---|---|
| KubeRay | <https://github.com/ray-project/kuberay> |
| Anyscale | <https://docs.anyscale.com/> — llms.txt: <https://docs.anyscale.com/llms.txt> |

### meta-ml-inference-docs

#### llm-inference-engines.md

| Tool | Docs |
|---|---|
| vLLM | <https://docs.vllm.ai/> |
| SGLang | <https://docs.sglang.io/> — llms.txt: <https://docs.sglang.io/llms.txt> |
| NVIDIA TensorRT-LLM | <https://nvidia.github.io/TensorRT-LLM/> |
| llama.cpp | <https://github.com/ggml-org/llama.cpp> |
| Ollama | <https://docs.ollama.com/> — llms.txt: <https://docs.ollama.com/llms.txt> |
| MLX-LM | <https://github.com/ml-explore/mlx-lm> |
| ONNX Runtime GenAI | <https://onnxruntime.ai/docs/genai/> |
| OpenVINO GenAI | <https://docs.openvino.ai/> |
| MLC LLM | <https://llm.mlc.ai/docs/> |

#### quantization-compression.md

| Tool | Docs |
|---|---|
| PyTorch torchao | <https://github.com/pytorch/ao> |
| TensorFlow Model Optimization | <https://www.tensorflow.org/model_optimization> |
| NVIDIA Model Optimizer | <https://nvidia.github.io/Model-Optimizer/> |
| Intel Neural Compressor | <https://intel.github.io/neural-compressor/> |
| OpenVINO NNCF | <https://github.com/openvinotoolkit/nncf> |
| bitsandbytes | <https://huggingface.co/docs/bitsandbytes> |
| GPTQModel | <https://github.com/ModelCloud/GPTQModel> |
| AutoAWQ | <https://github.com/casper-hansen/AutoAWQ> |
| SparseML | <https://github.com/neuralmagic/sparseml> |

#### compilers-and-runtimes.md

| Tool | Docs |
|---|---|
| ONNX | <https://onnx.ai/> |
| ONNX Runtime | <https://onnxruntime.ai/> |
| NVIDIA TensorRT | <https://docs.nvidia.com/deeplearning/tensorrt/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| OpenVINO | <https://docs.openvino.ai/> |
| Apache TVM | <https://tvm.apache.org/> |
| OpenXLA | <https://openxla.org/> |
| IREE | <https://iree.dev/> |
| MLIR | <https://mlir.llvm.org/> |
| LiteRT | <https://developers.google.com/edge/litert> |
| ExecuTorch | <https://docs.pytorch.org/executorch/> |
| Core ML Tools | <https://apple.github.io/coremltools/> |
| NCNN | <https://github.com/Tencent/ncnn> |
| MNN | <https://github.com/alibaba/MNN> |
| Paddle Lite | <https://github.com/PaddlePaddle/Paddle-Lite> |
| DirectML | <https://github.com/microsoft/DirectML> |

#### model-serving.md

| Tool | Docs |
|---|---|
| NVIDIA Triton Inference Server | <https://docs.nvidia.com/deeplearning/triton-inference-server/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| KServe | <https://kserve.github.io/website/> |
| BentoML | <https://docs.bentoml.com/> |
| Seldon Core | <https://docs.seldon.ai/> — llms.txt: <https://docs.seldon.ai/home/llms.txt> |
| TensorFlow Serving | <https://github.com/tensorflow/serving> |
| TorchServe | <https://docs.pytorch.org/serve/> |
| MLServer | <https://docs.seldon.ai/mlserver> — llms.txt: <https://docs.seldon.ai/mlserver/llms.txt> |
| FastAPI | <https://fastapi.tiangolo.com/> |
| Gradio | <https://gradio.app/docs> — llms.txt: <https://gradio.app/llms.txt> |
| Streamlit | <https://docs.streamlit.io/> — llms.txt: <https://docs.streamlit.io/llms.txt> |

### meta-ml-mlops-docs

#### experiment-tracking.md

| Tool | Docs |
|---|---|
| MLflow | <https://mlflow.org/docs/> |
| Weights & Biases | <https://docs.wandb.ai/> — llms.txt: <https://docs.wandb.ai/llms.txt> |
| TensorBoard | <https://www.tensorflow.org/tensorboard> |
| ClearML | <https://clear.ml/docs/> — llms.txt: <https://clear.ml/llms.txt> |
| Neptune | <https://docs.neptune.ai/> |
| Comet | <https://www.comet.com/docs/> — llms.txt: <https://www.comet.com/docs/opik/llms.txt> |
| DVC | <https://doc.dvc.org/> |

#### pipelines-and-monitoring.md

| Tool | Docs |
|---|---|
| Kubeflow | <https://www.kubeflow.org/docs/> |
| Apache Airflow | <https://airflow.apache.org/docs/> |
| Prefect | <https://docs.prefect.io/> — llms.txt: <https://docs.prefect.io/llms.txt> |
| Dagster | <https://docs.dagster.io/> — llms.txt: <https://docs.dagster.io/llms.txt> |
| Flyte | <https://docs.flyte.org/> — llms.txt: <https://www.union.ai/llms.txt> |
| Metaflow | <https://docs.metaflow.org/> |
| ZenML | <https://docs.zenml.io/> — llms.txt: <https://docs.zenml.io/llms.txt> |
| Evidently | <https://docs.evidentlyai.com/> — llms.txt: <https://docs.evidentlyai.com/llms.txt> |
| Prometheus | <https://prometheus.io/docs/> |
| Grafana | <https://grafana.com/docs/> — llms.txt: <https://grafana.com/llms.txt> |
| OpenTelemetry | <https://opentelemetry.io/docs/> — llms.txt: <https://opentelemetry.io/llms.txt> |
