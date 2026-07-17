# github

[English](README.md)

面向托管在 GitHub 上的项目的 meta-skill：协作约定与模板、镜像本地检查的
CI 质量门、平台护栏（依赖自动化、代码所有权、保护规则、扫描）、社区健康
文件，以及规划与发布约定。每个 skill 都教 harness 构建 agent 从 GitHub
文档现场获取当前平台能力，而不是规定版本化的语法。在 `core` 之上按项目
安装，且仅当目标托管在 GitHub 上时安装——本 catalog 不属于默认安装。

这些 skill 是**一次性**的：harness 构建并验证完成后，`core` 的移除
skill 会将它们一并删除。

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install github@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/github
npx skills add ryan-minato/meta-skills/skills/github --skill <skill-name>
```

## Skills

| Skill | 描述 |
|---|---|
| [meta-gh-collaboration](meta-gh-collaboration/) | commit 格式、分支与 pull request 流程、review 预期、issue 收件——写出 `.github/` 模板并把商定的约定沉淀进 AGENTS.md |
| [meta-gh-cicd](meta-gh-cicd/) | 通过镜像项目本地检查来把关 pull request 的 GitHub Actions workflow，workflow 语法与能力一律现场获取 |
| [meta-gh-guardrails](meta-gh-guardrails/) | Dependabot、CODEOWNERS、rulesets 与分支保护、secret 与 code scanning——逐项核实仓库的可见性与套餐实际提供的功能 |
| [meta-gh-community-files](meta-gh-community-files/) | 项目真正需要的社区健康文件——CONTRIBUTING、SECURITY、SUPPORT、CODE_OF_CONDUCT、GOVERNANCE、FUNDING、LICENSE——每个都放在平台可识别的位置并有真实负责人 |
| [meta-gh-planning-release](meta-gh-planning-release/) | 按团队规模设定的 label 分类法、milestone 与 Projects 用法，以及版本方案、changelog 政策和发布流程 |
