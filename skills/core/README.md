# core

[中文](README.zh.md)

The required set. Install every `core` skill into a target project before
asking an agent to build its harness, then add topic catalogs as the project
needs them.

These skills are **disposable**: once the harness is built and verified,
their own removal skill deletes them all.

```bash
npx skills add ryan-minato/meta-skills --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-harness-plan](meta-harness-plan/) | Plans, audits, or improves the project's agent harness on independent decision axes; produces the user-approved plan the other builders follow |
