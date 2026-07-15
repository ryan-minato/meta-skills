# core

[English](README.md)

必需的技能集合。在请求 agent 为目标项目搭建 harness 之前，先安装全部 `core`
技能，随后按项目需要追加主题分类。

这些技能是**一次性的**：harness 搭建完成并通过验证后，将它们移除。

```bash
npx skills add ryan-minato/meta-skills --skill <skill-name>
```

## 技能列表

按一次搭建中的使用顺序排列。

| 技能 | 说明 |
|---|---|
| `meta-harness-plan` | 在动手写任何文件之前，先弄清这个项目需要什么——以及不需要什么。读取仓库已经能自己展示的部分，就它无法展示的部分提问，并敲定要搭建的内容。 |
| `meta-agents-md` | 撰写入口文件：哪些内容留在常驻页面上，哪些移到指针之后，以及让其余内容可被发现的 when-to-read 表格。 |
| `meta-knowledge-file` | 创建入口文件所指向的那些文件——目标、计划、质量、工作流、参考资料——并判断每一种该是单个文件还是一个文件夹。 |
| `meta-framework-wiring` | 把 harness 接入团队实际使用的 agent。每个框架先读哪个文件、技能与 MCP 配置放在哪里、有哪些 hook。抓取厂商文档，而不是依赖既有笔记。 |
| `meta-project-skill` | 把值得沉淀的流程变成项目自己的耐久技能——同时避免它们继承那个会在清理时把它们删掉的 marker。 |
| `meta-harness-maintenance` | 搭建那些在无人盯守时维持 harness 正确性的机制：重新对齐散落在多个文件中的重复事实，并剪除已经过时的内容。 |
| `meta-disposal` | 在 harness 搭建完成并通过验证后移除这些 meta-skill。先试运行，删除前询问，并把自己留到最后。 |
