# data-science

[中文](README.zh.md)

Meta-skills for data-analysis and scientific-computing target projects:
authoritative documentation entry points, split by project domain, for
the libraries, engines, and tools such a project uses or is likely to
need — plus the discovery procedure for anything not listed. Each skill
covers one domain, so an agent loads only the domains the target
belongs to. These skills inform; they never recommend. Install on top
of `core`, per project, and only when the target analyzes data, runs
data pipelines, or does numerical and scientific computing — this
catalog is not part of the default install.

These skills are **disposable**: once the harness is built and verified,
the `core` removal skill deletes them together with the rest.

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install data-science@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/data-science
npx skills add ryan-minato/meta-skills/skills/data-science --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-ds-analysis-docs](meta-ds-analysis-docs/) | Documentation entry points for numerics and statistics, dataframes and SQL, storage formats, multidimensional data, graph analysis, visualization, data quality, and notebooks |
