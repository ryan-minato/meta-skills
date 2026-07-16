# core

[English](README.md)

必装集合。在请求 agent 为目标项目搭建 harness 之前，先安装全部 `core` 技能，
随后按项目需要追加主题目录。

这些技能是**一次性的**：harness 搭建完成并通过验证后，由其中自带的移除技能将
它们全部删除。

```bash
npx skills add ryan-minato/meta-skills --skill <skill-name>
```

## 技能列表

| 技能 | 说明 |
|---|---|
| [meta-harness-plan](meta-harness-plan/) | 在相互独立的决策轴上规划、审计或改进项目的 agent harness；产出经用户批准、供其余搭建技能遵循的计划 |
| [meta-agents-md](meta-agents-md/) | 创建或改进 AGENTS.md 入口与框架指针文件，把过长的架构材料卸载到章节定位指针之后 |
| [meta-knowledge-base](meta-knowledge-base/) | 搭建 agent 知识库：唯一一致的结构、按类型的文档骨架，并以技能或入口形态沉淀 authoring 规则 |
| [meta-project-skill](meta-project-skill/) | 用按情形分类的骨架创建或翻修耐久项目技能，并为后来的 agent 沉淀本项目的技能设计规则 |
