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
| [meta-harness-sync](meta-harness-sync/) | 安装双向的保鲜机制——一事一机制，技能或入口两种形态——外加定期熵回收与折中模式的任务后提议规则 |
| [meta-disposal](meta-disposal/) | 按 description 标记移除全部已安装的 meta-skill：先 dry-run 列表，经新鲜明确的确认后删除，自身最后删 |
