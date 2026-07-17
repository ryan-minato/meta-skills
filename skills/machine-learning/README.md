# machine-learning

[中文](README.zh.md)

Meta-skills for machine-learning target projects: authoritative
documentation entry points, split by project domain, for the frameworks,
libraries, and tools an ML project uses or is likely to need — plus the
discovery procedure for anything not listed. Each skill covers one
domain, so an agent loads only the domains the target belongs to. These
skills inform; they never recommend. Install on top of `core`, per
project, and only when the target trains, finetunes, serves, or builds on
ML models — this catalog is not part of the default install.

These skills are **disposable**: once the harness is built and verified,
the `core` removal skill deletes them together with the rest.

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install machine-learning@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/machine-learning
npx skills add ryan-minato/meta-skills/skills/machine-learning --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-ml-frameworks-docs](meta-ml-frameworks-docs/) | Documentation entry points for general DL and tensor frameworks (PyTorch, TensorFlow, Keras, JAX, MLX, PaddlePaddle, tinygrad) and GPU-kernel and compiled-ops libraries |
| [meta-ml-training-docs](meta-ml-training-docs/) | Documentation entry points for distributed-training stacks (DeepSpeed, Megatron, Lightning, NeMo, Colossal-AI, TorchTitan) and finetuning frameworks (torchtune, LLaMA-Factory, Axolotl, Unsloth, OpenRLHF) |
| [meta-ml-huggingface-docs](meta-ml-huggingface-docs/) | Documentation entry points across the Hugging Face ecosystem: model and data libraries, training and optimization, Hub serving and apps |
| [meta-ml-ray-docs](meta-ml-ray-docs/) | Documentation entry points for the Ray libraries (Core, Data, Train, Tune, Serve, Serve LLM, RLlib) and the KubeRay/Anyscale cluster layer |
| [meta-ml-inference-docs](meta-ml-inference-docs/) | Documentation entry points for LLM inference engines, quantization and compression, model compilers and cross-platform runtimes, and serving platforms |
| [meta-ml-mlops-docs](meta-ml-mlops-docs/) | Documentation entry points for experiment tracking and versioning (MLflow, W&B, DVC) and ML pipelines and monitoring (Kubeflow, Flyte, ZenML, Evidently, Prometheus/Grafana) |
| [meta-ml-llm-apps-docs](meta-ml-llm-apps-docs/) | Documentation entry points for RAG and agent frameworks, LLM gateways and guardrails, and vector search from local ANN libraries to vector databases |
