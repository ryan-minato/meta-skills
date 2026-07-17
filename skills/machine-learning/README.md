# machine-learning

[中文](README.zh.md)

Meta-skills for machine-learning target projects, in two kinds. The
`-docs` skills map a project to authoritative documentation entry points,
split by project domain, for the frameworks, libraries, and tools an ML
project uses or is likely to need — plus the discovery procedure for
anything not listed; they inform and never recommend. The unsuffixed
skills scaffold ML project harnesses and enumerate live registries; they
carry opinionated defaults, each declared in its own description. An
agent loads only the skills matching the target. Install on top of
`core`, per project, and only when the target trains, finetunes, serves,
or builds on ML models — this catalog is not part of the default
install.

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
| [meta-ml-llm-eval-docs](meta-ml-llm-eval-docs/) | Documentation entry points for LLM benchmark and evaluation harnesses and LLM observability platforms |
| [meta-ml-vision-docs](meta-ml-vision-docs/) | Documentation entry points for core vision libraries, detection/segmentation/tracking, OCR and document AI, and 3D vision and neural rendering |
| [meta-ml-image-gen-docs](meta-ml-image-gen-docs/) | Documentation entry points for image/video generation UIs, LoRA trainers, conditioning adapters, and open video-generation projects |
| [meta-ml-audio-docs](meta-ml-audio-docs/) | Documentation entry points for speech recognition and speakers, speech synthesis and voice cloning, voice conversion and separation, and music and generative audio |
| [meta-ml-rl-docs](meta-ml-rl-docs/) | Documentation entry points for RL algorithm frameworks and for environments and simulators |
| [meta-ml-recsys-docs](meta-ml-recsys-docs/) | Documentation entry points for recommendation, ranking, and candidate-retrieval frameworks |
| [meta-ml-tabular-docs](meta-ml-tabular-docs/) | Documentation entry points for traditional ML and gradient boosting, interpretability, and AutoML and hyperparameter optimization |
| [meta-ml-timeseries-docs](meta-ml-timeseries-docs/) | Documentation entry points for time-series forecasting, feature extraction, and change-point and anomaly detection |
| [meta-ml-graph-docs](meta-ml-graph-docs/) | Documentation entry points for graph neural networks and for graph analysis and knowledge graphs |
| [meta-ml-probabilistic-docs](meta-ml-probabilistic-docs/) | Documentation entry points for probabilistic programming and Bayesian inference and for causal inference |
| [meta-ml-trustworthy-docs](meta-ml-trustworthy-docs/) | Documentation entry points for privacy, adversarial robustness, fairness, and interpretability, and for federated learning |
| [meta-ml-science-docs](meta-ml-science-docs/) | Documentation entry points for ML in medicine, biology, chemistry, molecular simulation, and physics-informed modeling |
| [meta-ml-containers](meta-ml-containers/) | Scripts that list and filter the currently available NVIDIA NGC and Docker Hub GPU images and tags, plus a guide to each image family's characteristics and fit |
| [meta-ml-experiment](meta-ml-experiment/) | Scaffolds a quick ML experiment repository (opinionated defaults): uv-compiled pinned requirements, root-level entry scripts, Pydantic Settings config, justfile, Ruff/pytest/Gitleaks, an Accelerate training-loop template, and a concise AGENTS.md |
| [meta-ml-training-project](meta-ml-training-project/) | Scaffolds a maintainable train/eval project (opinionated defaults): uv + pyproject with hardware-matched torch indexes, Hydra configs, raw/interim/processed data split, an Accelerate training-loop template, and a directory-map AGENTS.md with a knowledge base |
