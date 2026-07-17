# machine-learning

[中文](README.zh.md)

Meta-skills for machine-learning target projects: authoritative
documentation entry points, split by project domain, for the frameworks,
libraries, and tools an ML project uses or is likely to need — plus the
discovery procedure for anything not listed. Each skill covers one
domain, so an agent loads only the domains the target belongs to. These
skills inform; they never recommend. Install on top of `core`, per
project, and only when the target trains, finetunes, serves, or builds on
ML models — this catalog is not part of the default install.

These skills are **disposable**: once the harness is built and verified,
the `core` removal skill deletes them together with the rest.

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install machine-learning@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/machine-learning
npx skills add ryan-minato/meta-skills/skills/machine-learning --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| none yet | |
