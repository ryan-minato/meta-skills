# meta-skills

[English](README.md)

一次性的 meta-skill，帮助 agent 在你的项目中搭建持久的 **harness**，随后主动退场。

harness 指一切对 agent 可见、并帮助 agent 达成你预期的东西：agent 运行所处的环境、
对其产出的约束、可调用的工具，以及可获取的知识。搭建一个好的 harness 本身就是一门
技艺，而这些技能承载的正是这门技艺。

它们与常规技能库相反：它们被设计为会删除自己。

## 工作方式

1. **安装** —— 将 `core` 分类安装到项目中，并按技术栈追加相关主题分类。
2. **提出需求** —— 把项目的需求与规范交给 agent，请它搭建 harness。
3. **搭建** —— agent 调用这些 meta-skill，其中沉淀了相应的最佳实践。
4. **移除** —— harness 搭建完成并经你验证后，请 agent 移除这些 meta-skill。它们已
   完成使命；任何留下的技能都会在此后每一次会话中持续消耗上下文。

移除环节刻意需要确认：先前"搭建 harness"的请求，永远不等同于同意删除任何内容。

## 分类

| 分类 | 内容 | 安装范围 |
|---|---|---|
| [core](skills/core/) | 必需集合：足以让任意项目从没有 harness 到拥有可用的 harness | 按项目安装，在搭建 harness 前 |

## 安装

```bash
npx skills add ryan-minato/meta-skills                      # 交互式
npx skills add ryan-minato/meta-skills --skill <skill-name>
```

请**按项目**安装，而非全局安装。它们是为某个项目的某项工作准备的脚手架；全局安装会
让它们跟进那些已经拥有 harness 的项目。

## meta-skill 如何标识自身

每个已发布技能的 description 都以标记开头：

```text
[META-SKILL: remove after harness setup]
```

该标记是 agent 再次找到这些技能并将其移除的依据。标识依据是 **description，而非名称**
—— 因为安装器会为避免冲突而重命名技能；`meta-` 名称前缀仅用于在文件树中将它们归拢。

## 相关项目

姊妹库 [ryan-minato/skills](https://github.com/ryan-minato/skills) 提供**持久**技能，
其中包括 `meta-harness`：一个常驻安装的通用设计辅助。本仓库提供的则是一次性的、按
项目使用的搭建者。两者可以配合使用。

## 参与贡献

请从 [AGENTS.md](AGENTS.md) 开始，然后阅读 [ARCHITECTURE.md](ARCHITECTURE.md)。执行
一次 `just setup`，并在提交前运行 `just check`。

## 许可证

[Apache-2.0](LICENSE)
