# Meta Skills

[![质量检查](https://github.com/ryan-minato/meta-skills/actions/workflows/quality.yml/badge.svg)](https://github.com/ryan-minato/meta-skills/actions/workflows/quality.yml)
[![历史密钥扫描](https://github.com/ryan-minato/meta-skills/actions/workflows/secrets.yml/badge.svg)](https://github.com/ryan-minato/meta-skills/actions/workflows/secrets.yml)

> 用于生成持久化、项目专属 agent harness 的一次性 meta-skill。

[English](README.md) · [设计](DESIGN.md) · [架构](ARCHITECTURE.md) · [Agent 指南](AGENTS.md)

Meta Skills 将帮助 agent 把一组一次性脚手架 skill 转化为可维护的 harness：清晰的 agent 入口、项目知识库、设计和架构契约、工作流 skill、MCP 适配器、CI、Git hook 与仓库规范。

## 生命周期

```text
安装 core 与选定主题 → 选择 profile → 生成并验证 harness
                                      ↓
                         明确确认后移除 meta-skill
```

移除步骤是有意设计：meta-skill 是脚手架，而它创建的 harness 应长期保留在目标项目中。

## Profile

| Profile | 创建内容 |
| --- | --- |
| `minimal` | 入口、目标、仓库地图、核心约束、命令与维护规则。 |
| `standard` | 在 minimal 基础上增加适用的设计/架构文档、可复现环境、检查、CI 与安全机制；这是默认值。 |
| `full` | 在 standard 基础上增加知识库、工作流 skill、MCP、hook、完整 CI/PII 与更强的维护机制。 |

所有 profile 都是受人工监督的 L2 harness，不引入无人值守或自修改的 L3/L4 行为。

## Catalog

未来公开 skill 将使用 `skills/<catalog>/<skill>/`。`core` 会作为完整集合安装；之后用户只选择相关的主题 catalog，例如 GitHub、GitLab、Linear、devcontainer、CI/CD 或语言/框架支持。catalog 只会在其中出现第一个真实 skill 时创建。

**当前尚无可安装的公开 skill。** 本仓库优先建设未来 skill 所需的质量、生命周期和交付 harness。

## META-SKILL 安全

每个未来可分发的脚手架 skill 都会携带两个匹配标记：一个在 frontmatter 的 description 开头，另一个是正文的第一行。验证器会拒绝不完整标记，也会拒绝 durable 或内部 skill 继承这些标记。未来的清理工具会显示 dry-run 清单，并在明确确认后，只移除已验证且不是 symlink 的 meta-skill。

## 开发本仓库

```sh
just setup
just check
```

请先阅读 [AGENTS.md](AGENTS.md)。当前仓库采用 `full` profile，并在 Linear 中由 **Meta Skills** 项目管理。Git 默认分支是知识权威源；Linear 只镜像已合并知识。
