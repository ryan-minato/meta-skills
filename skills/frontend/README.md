# frontend

[中文](README.zh.md)

Meta-skills for projects with a user-facing visual surface: design
description and visual language. Install on top of `core`, per project, and
only when the target actually has a frontend — this catalog is not part of
the default install.

These skills are **disposable**: once the harness is built and verified,
the `core` removal skill deletes them together with the rest.

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install frontend@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/frontend
npx skills add ryan-minato/meta-skills/skills/frontend --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-design-md](meta-design-md/) | Authors or edits DESIGN.md per the public visual-design description format, with an OKLCH calculator for conversion, gamut checks, and WCAG contrast |
