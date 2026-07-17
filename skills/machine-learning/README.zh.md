# machine-learning

[English](README.md)

面向机器学习目标项目的 meta-skill：按项目领域拆分，为 ML 项目正在使用或
可能需要的框架、库与工具提供权威文档入口，并附带未收录工具的发现流程。
每个技能只覆盖一个领域，agent 只加载目标所属领域的技能。这些技能只提供
信息，绝不做推荐。在 `core` 之上按项目安装，仅当目标训练、微调、部署或
构建于机器学习模型之上时使用——本 catalog 不属于默认安装。

这些技能是**一次性的**：harness 建成并验证后，`core` 的移除技能会把它们
与其余 meta-skill 一并删除。

```bash
claude plugin marketplace add ryan-minato/meta-skills   # 每台机器一次
claude plugin install machine-learning@meta-skills --scope project
# 或使用 skills CLI（catalog 路径即发现范围）：
npx skills add ryan-minato/meta-skills/skills/machine-learning
npx skills add ryan-minato/meta-skills/skills/machine-learning --skill <skill-name>
```

## Skills

| Skill | 描述 |
|---|---|
| [meta-ml-frameworks-docs](meta-ml-frameworks-docs/) | 通用深度学习与张量框架（PyTorch、TensorFlow、Keras、JAX、MLX、PaddlePaddle、tinygrad）及 GPU 内核与编译算子库的文档入口 |
| [meta-ml-training-docs](meta-ml-training-docs/) | 分布式训练栈（DeepSpeed、Megatron、Lightning、NeMo、Colossal-AI、TorchTitan）与微调框架（torchtune、LLaMA-Factory、Axolotl、Unsloth、OpenRLHF）的文档入口 |
| [meta-ml-huggingface-docs](meta-ml-huggingface-docs/) | Hugging Face 生态的文档入口：模型与数据库、训练与优化、Hub 侧服务与应用 |
| [meta-ml-ray-docs](meta-ml-ray-docs/) | Ray 各库（Core、Data、Train、Tune、Serve、Serve LLM、RLlib）与 KubeRay/Anyscale 集群层的文档入口 |
| [meta-ml-inference-docs](meta-ml-inference-docs/) | LLM 推理引擎、量化压缩、模型编译与跨平台运行时、模型服务平台的文档入口 |
| [meta-ml-mlops-docs](meta-ml-mlops-docs/) | 实验跟踪与版本管理（MLflow、W&B、DVC）及 ML 流水线与监控（Kubeflow、Flyte、ZenML、Evidently、Prometheus/Grafana）的文档入口 |
| [meta-ml-llm-apps-docs](meta-ml-llm-apps-docs/) | RAG 与 Agent 框架、LLM 网关与护栏、从本地 ANN 库到向量数据库的向量检索的文档入口 |
| [meta-ml-llm-eval-docs](meta-ml-llm-eval-docs/) | LLM 基准与评测框架及 LLM 可观测平台的文档入口 |
| [meta-ml-vision-docs](meta-ml-vision-docs/) | 基础视觉库、检测/分割/跟踪、OCR 与文档智能、3D 视觉与神经渲染的文档入口 |
