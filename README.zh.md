# meta-skills

[English](README.md)

一次性的 meta-skill，帮助 agent 在你的项目中搭建持久的 **harness**，随后主动
退场。

harness 指一切对 agent 可见、并帮助 agent 达成你预期的东西：agent 运行所处的
环境、对其产出的约束、可调用的工具，以及可获取的知识。搭建一个好的 harness 本身
就是一门技艺，而这些技能承载的正是这门技艺。它们是普通技能库的反面：生来就是为了
删除自己。

## 工作方式

1. **安装** —— 把 `core` 目录装进项目的技能目录（例如 `./.agents/skills/`），
   随后优先按目录安装符合技术栈的主题技能；同时仍支持单技能安装。
2. **提出需求** —— 把项目的需求与规范交给 agent，请它搭建 harness。
3. **搭建** —— agent 调用这些 meta-skill，它们承载着最佳实践。
4. **移除** —— harness 建成并验证后，agent 依据标记找到所有 meta-skill 并全部
   删除。它们的使命已经完成，每个留下的技能都会在之后的每个会话中消耗上下文。

移除操作在设计上必须经过确认：先前"搭建 harness"的请求绝不被视为删除任何东西的
授权。

## meta-skill 如何自我标识

每个发布技能的 description 都以标记开头：

```text meta-skill-marker
Disposable meta-skill (delete after the harness is built):
```

agent 正是靠这个标记重新找到这些技能并删除它们。识别依据是 **description 而非
名称**，因为安装器会为避免冲突而重命名技能——`meta-` 名称前缀只用于在文件树中
归组。

## 目录

| 目录 | 内容 | 安装范围 |
|---|---|---|
| [core](skills/core/) | 必装集合：足以让任何项目从没有 harness 到拥有可用的 harness，包括实时发现目录/技能与集中安装指引 | 按项目安装，在搭建 harness 之前 |
| [frontend](skills/frontend/) | 面向具有用户可见前端的项目的设计描述与视觉语言 | 按项目安装，在 `core` 之上，仅当目标有视觉界面时 |
| [python](skills/python/) | 面向 Python 项目的可信默认值与文档 URL：docstring 与注释约定、测试设置、工具链选择 | 按项目安装，在 `core` 之上，仅当目标是 Python 项目时 |
| [machine-learning](skills/machine-learning/) | 面向 ML 项目的文档入口，每个领域一个技能（框架、训练、推理、视觉、音频……）——只提供信息——另有项目脚手架（快速实验、可维护训练）与 GPU 镜像发现技能，各自声明其观点默认值 | 按项目安装，在 `core` 之上，仅当目标训练、微调、部署或构建于 ML 模型之上时 |
| [data-science](skills/data-science/) | 面向数据分析与科学计算领域的文档入口——只提供信息——另有明确声明其默认值的带观点项目脚手架 | 按项目安装，在 `core` 之上，仅当目标做数据分析或科学计算时 |
| [github](skills/github/) | 面向托管在 GitHub 上的项目的平台侧约定，每个关注点一个技能：协作流程与模板、镜像本地检查的 CI 质量门、护栏（Dependabot、CODEOWNERS、rulesets、扫描）、社区健康文件、规划与发布——平台能力一律从 GitHub 文档现场获取 | 按项目安装，在 `core` 之上，仅当目标托管在 GitHub 上时 |
| [gitlab](skills/gitlab/) | 面向托管在 GitLab 上的项目的平台侧约定，镜像 `github` catalog 的五个关注点（协作、CI、护栏、社区文件、规划与发布），并尊重实例的版本与 tier——平台能力一律从 GitLab 文档现场获取 | 按项目安装，在 `core` 之上，仅当目标托管在 GitLab（gitlab.com 或自管实例）上时 |

按目录安装只是推荐方式，并非技能存在性的保证：只有 `core` 可以假设已安装。每个技能
都会显式列出所有非 core 依赖，并引导 agent 使用 `meta-skill-discovery` 查询当前
清单与安装方法。

## 安装

使用 `meta-skill-discovery` 实时筛选目录和技能、选择单个技能，并了解项目级或全局
scope。下列命令展示推荐的项目级目录安装方式。

作为 Claude Code 插件安装——每个目录（catalog）就是本仓库市场中的一个插件：

```bash
claude plugin marketplace add ryan-minato/meta-skills
claude plugin install core@meta-skills --scope project
claude plugin install frontend@meta-skills --scope project   # 仅当项目有视觉界面
claude plugin install python@meta-skills --scope project     # 仅当是 Python 项目
claude plugin install machine-learning@meta-skills --scope project  # 仅当是 ML 项目
claude plugin install data-science@meta-skills --scope project      # 仅当是数据/科学计算项目
claude plugin install github@meta-skills --scope project            # 仅当托管在 GitHub 上
claude plugin install gitlab@meta-skills --scope project            # 仅当托管在 GitLab 上
```

以插件方式安装的技能用 `claude plugin uninstall` 移除，而不是由移除技能删除
文件。

或使用 skills CLI——指向 catalog 路径，发现范围即精确限定在该 catalog：

```bash
npx skills add ryan-minato/meta-skills/skills/core
npx skills add ryan-minato/meta-skills/skills/frontend      # 仅当项目有视觉界面
npx skills add ryan-minato/meta-skills/skills/python        # 仅当是 Python 项目
npx skills add ryan-minato/meta-skills/skills/machine-learning  # 仅当是 ML 项目
npx skills add ryan-minato/meta-skills/skills/data-science  # 仅当是数据/科学计算项目
npx skills add ryan-minato/meta-skills/skills/github        # 仅当托管在 GitHub 上
npx skills add ryan-minato/meta-skills/skills/gitlab        # 仅当托管在 GitLab 上
npx skills add ryan-minato/meta-skills/skills               # 全部已发布技能
```

也可以把技能目录（`skills/<catalog>/<skill>/`）直接复制进项目的技能目录。项目级
scope 是默认值与推荐方式：这些技能只为单个项目的一次任务搭建脚手架。明确需要时也
支持全局安装，但一次性技能会因此进入所有项目，完成后必须在对应的全局 scope 清理。

## 相关项目

姊妹库 [ryan-minato/skills](https://github.com/ryan-minato/skills) 提供
**持久的**技能，其中包括常驻安装的通用设计辅助 `meta-harness`。本仓库提供的则是
一次性的、按项目使用的搭建者。两者可以配合使用。

## 参与贡献

从 [AGENTS.md](AGENTS.md) 开始，然后阅读 [ARCHITECTURE.md](ARCHITECTURE.md)。
克隆后运行一次 `just setup`，提交更改前运行 `just check`。

## 许可证

[Apache-2.0](LICENSE)
