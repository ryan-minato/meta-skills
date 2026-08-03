# core

[English](README.md)

必装集合。在请求 agent 为目标项目搭建 harness 之前，先安装 `core`，随后优先按项目
需要追加主题目录。只有 core 可以假设已存在；按目录安装并不能证明某个非 core 同目录
技能可用。

这些技能是**一次性的**：harness 搭建完成并通过验证后，由其中自带的移除技能将
它们全部删除。

```bash
claude plugin marketplace add ryan-minato/meta-skills   # 每台机器一次
claude plugin install core@meta-skills --scope project
# 或通过 skills CLI（catalog 路径即发现范围）：
npx skills add ryan-minato/meta-skills/skills/core
npx skills add ryan-minato/meta-skills/skills/core --skill <skill-name>
```

## 技能列表

| 技能 | 说明 |
|---|---|
| [meta-skill-discovery](meta-skill-discovery/) | 实时发现本仓库的目录与技能，按目录过滤，并集中提供项目级/全局安装指引 |
| [meta-harness-plan](meta-harness-plan/) | 在相互独立的决策轴上规划、审计或改进项目的 agent harness；产出经用户批准、供其余搭建技能遵循的计划 |
| [meta-agents-md](meta-agents-md/) | 创建或改进 AGENTS.md 入口与框架指针文件，把过长的架构材料卸载到章节定位指针之后 |
| [meta-knowledge-base](meta-knowledge-base/) | 搭建 agent 知识库：唯一一致的结构、按类型的文档骨架，并以技能或入口形态沉淀 authoring 规则 |
| [meta-project-skill](meta-project-skill/) | 用按情形分类的骨架创建或翻修耐久项目技能，并为后来的 agent 沉淀本项目的技能设计规则 |
| [meta-harness-sync](meta-harness-sync/) | 安装双向的保鲜机制——一事一机制，技能或入口两种形态——外加定期熵回收与折中模式的任务后提议规则 |
| [meta-docs-map](meta-docs-map/) | 从已发布的文档索引为目标技术栈记录文档入口：检测技术栈、抓取 llms.txt、按 tag 选页、记录文档所在 |
| [meta-disposal](meta-disposal/) | 按 description 标记移除全部已安装的 meta-skill：先 dry-run 列表，经新鲜明确的确认后删除，自身最后删 |
