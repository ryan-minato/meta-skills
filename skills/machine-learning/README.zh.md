# machine-learning

[English](README.md)

面向机器学习目标项目的 meta-skill：harness 脚手架与线上注册表发现，
各自在自己的 description 中声明其观点默认值。ML 各领域的文档入口位于
已发布的 docs 索引中，由 `core` 的 docs-map 技能按需消费。在 `core`
之上按项目安装，仅当目标训练、微调、部署或构建于机器学习模型之上时
使用——本 catalog 不属于默认安装。

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
| [meta-ml-containers](meta-ml-containers/) | 用脚本列出并过滤 NVIDIA NGC 与 Docker Hub 当前可用的 GPU 镜像及 tag，并附各镜像族特点与适用情境指南 |
| [meta-ml-experiment](meta-ml-experiment/) | 搭建快速 ML 实验仓库（带观点默认值）：uv 编译的锁定依赖、根目录入口脚本、Pydantic Settings 配置、justfile、Ruff/pytest/Gitleaks、Accelerate 训练循环模板与单页 AGENTS.md |
| [meta-ml-training-project](meta-ml-training-project/) | 搭建可维护的训练/评估项目（带观点默认值）：uv + pyproject 与硬件匹配的 torch 索引、Hydra 配置、raw/interim/processed 数据分层、Accelerate 训练循环模板与目录地图式 AGENTS.md 加知识库 |
