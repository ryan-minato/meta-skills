# data-science

[English](README.md)

面向数据分析与科学计算目标项目的 meta-skill：既包括按项目领域拆分的权威
文档入口，也包括明确声明其默认值的、带观点的项目脚手架。agent 只加载目标
所需的领域或构建器。在 `core` 之上按项目安装，仅当目标做数据分析、运行
数据流水线或进行数值与科学计算时使用——本 catalog 不属于默认安装。

这些技能是**一次性的**：harness 建成并验证后，`core` 的移除技能会把
它们与其余 meta-skill 一并删除。

```bash
claude plugin marketplace add ryan-minato/meta-skills   # 每台机器一次
claude plugin install data-science@meta-skills --scope project
# 或使用 skills CLI（catalog 路径即发现范围）：
npx skills add ryan-minato/meta-skills/skills/data-science
npx skills add ryan-minato/meta-skills/skills/data-science --skill <skill-name>
```

## Skills

| Skill | 描述 |
|---|---|
| [meta-ds-analysis-docs](meta-ds-analysis-docs/) | 数值与统计、dataframe 与 SQL、存储格式、多维数据、图分析、可视化、数据质量与 notebook 的文档入口 |
| [meta-ds-scale-docs](meta-ds-scale-docs/) | NVIDIA RAPIDS GPU 数据科学、Dask 家族与集群分析引擎（Spark、Flink、Trino、Sedona）的文档入口 |
| [meta-ds-pipelines-docs](meta-ds-pipelines-docs/) | 工作流编排与分析工程（Airflow、dbt、Dagster、Prefect）的文档入口 |
| [meta-ds-geospatial-docs](meta-ds-geospatial-docs/) | 地理空间矢量与栅格栈及空间引擎的文档入口 |
| [meta-ds-numerics-docs](meta-ds-numerics-docs/) | 科学计算平台、数学内核与稀疏求解器、编译器/GPU 工具链与自动微分的文档入口 |
| [meta-ds-simulation-docs](meta-ds-simulation-docs/) | 数值优化与求解器、微分方程、PDE/FEM 框架与科学可视化的文档入口 |
| [meta-ds-hpc-docs](meta-ds-hpc-docs/) | MPI/工作流管理器/调度器、GPU 与多机通信、科学数据与并行 I/O 的文档入口 |
| [meta-ds-project](meta-ds-project/) | 带观点的可复现 Python 数据科学项目脚手架，包含不可变源数据、存储分支、可观测工作流与 agent 知识库 |
