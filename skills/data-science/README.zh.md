# data-science

[English](README.md)

面向数据分析与科学计算目标项目的 meta-skill：明确声明其默认值的、带观点
的项目脚手架。这些领域的文档入口位于已发布的 docs 索引中，由 `core` 的
docs-map 技能按需消费。在 `core` 之上按项目安装，仅当目标做数据分析、运行
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
| [meta-ds-project](meta-ds-project/) | 带观点的可复现 Python 数据科学项目脚手架，包含不可变源数据、存储分支、可观测工作流与 agent 知识库 |
