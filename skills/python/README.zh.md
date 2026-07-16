# python

[English](README.md)

面向 Python 目标项目的 meta-skill：为文档约定、测试设置与工具链选择提供可信的默认值和权威文档
URL。按项目安装在 `core` 之上，且仅当目标是 Python 项目时安装——本目录不属于默认安装的一部分。

这些 skill 是**一次性的**：harness 构建并验证完成后，`core` 的移除 skill
会把它们与其余 meta-skill 一并删除。

```bash
claude plugin marketplace add ryan-minato/meta-skills   # 每台机器一次
claude plugin install python@meta-skills --scope project
# 或通过 skills CLI（目录路径限定发现范围）：
npx skills add ryan-minato/meta-skills/skills/python
npx skills add ryan-minato/meta-skills/skills/python --skill <skill-name>
```

## Skills

| Skill | 描述 |
|---|---|
| [meta-python-docstyle](meta-python-docstyle/) | docstring 风格（默认 Google；覆盖 NumPy 与 reST）、按对象类型的 docstring 完整度、自文档化代码的注释哲学、标注注释策略的默认值，附上游文档 URL |
| [meta-python-testing](meta-python-testing/) | 测试框架（pytest）、按明确需要选择插件、测试风格信条的默认值：Arrange-Act-Assert、经典派、真实对象优先于 mock、状态验证、错误路径必测 |
| [meta-python-toolchain](meta-python-toolchain/) | 依赖管理（uv）、lint 与格式化（Ruff）、类型检查（ty）、任务运行（just）、git 钩子（pre-commit）、文档生成（Zensical）的默认值与文档 URL，附成熟替代选项 |
