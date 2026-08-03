# data-science

[中文](README.zh.md)

Meta-skills for data-analysis and scientific-computing target projects:
opinionated project scaffolds that declare their defaults explicitly.
Documentation entry points for these domains live in the published docs
index, consumed on demand by `core`'s docs-map skill. Install on top of
`core`, per project, and only when the target analyzes data, runs data
pipelines, or does numerical and scientific computing — this catalog is not
part of the default install.

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
| [meta-ds-project](meta-ds-project/) | Opinionated reproducible Python data-science project scaffold with immutable source data, storage branches, observable workflows, and an agent knowledge base |
