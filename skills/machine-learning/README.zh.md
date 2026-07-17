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
