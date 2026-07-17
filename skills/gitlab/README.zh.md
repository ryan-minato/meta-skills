# gitlab

[English](README.md)

面向托管在 GitLab（gitlab.com 或自管实例）上的项目的 meta-skill：协作
约定与模板、镜像本地检查的 CI 质量门、平台护栏（保护规则、审批、代码
所有权、扫描、更新自动化）、社区文件，以及规划与发布约定。每个 skill
都教 harness 构建 agent 从 GitLab 文档现场获取当前平台能力——尊重实例
的版本与 tier——而不是规定版本化的语法。在 `core` 之上按项目安装，且
仅当目标托管在 GitLab 上时安装——本 catalog 不属于默认安装。

这些 skill 是**一次性**的：harness 构建并验证完成后，`core` 的移除
skill 会将它们一并删除。

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install gitlab@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/gitlab
npx skills add ryan-minato/meta-skills/skills/gitlab --skill <skill-name>
```

## Skills

| Skill | 描述 |
|---|---|
| [meta-gl-collaboration](meta-gl-collaboration/) | commit 格式、分支与 merge request 流程、review 预期、issue 收件——写出 `.gitlab/` 描述模板并把商定的约定沉淀进 AGENTS.md |
| [meta-gl-cicd](meta-gl-cicd/) | 通过镜像项目本地检查来把关 merge request 的 `.gitlab-ci.yml` 流水线，关键字与 runner 能力一律现场获取 |
| [meta-gl-guardrails](meta-gl-guardrails/) | 受保护分支与 tag、审批规则、CODEOWNERS、平台的依赖与 secret 扫描、第三方更新自动化——逐项核实实例 tier 的实际提供 |
| [meta-gl-community-files](meta-gl-community-files/) | 项目真正需要的社区健康文件——CONTRIBUTING、SECURITY、SUPPORT、CODE_OF_CONDUCT、GOVERNANCE、LICENSE——每个都有真实负责人，并核对 GitLab 实际呈现哪些 |
| [meta-gl-planning-release](meta-gl-planning-release/) | 按团队规模与 tier 设定的 label 分类法、milestone、看板与 epic 用法，以及版本方案、changelog 政策和发布流程 |
