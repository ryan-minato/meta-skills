# github

[中文](README.zh.md)

Meta-skills for projects hosted on GitHub: collaboration conventions and
templates, CI quality gates that mirror local checks, platform guardrails
(dependency automation, code ownership, protections, scanning), community
health files, and planning and release conventions. Every skill teaches
the harness-building agent to fetch current platform capabilities live
from the GitHub docs instead of prescribing versioned syntax. Install on
top of `core`, per project, and only when the target is hosted on GitHub
— this catalog is not part of the default install.

These skills are **disposable**: once the harness is built and verified,
the `core` removal skill deletes them together with the rest.

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install github@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/github
npx skills add ryan-minato/meta-skills/skills/github --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-gh-collaboration](meta-gh-collaboration/) | Commit format, branch and pull request flow, review expectations, and issue intake — writes the `.github/` templates and deposits the agreed conventions into AGENTS.md |
| [meta-gh-cicd](meta-gh-cicd/) | GitHub Actions workflows that gate pull requests by mirroring the project's local checks, with workflow syntax and capabilities always fetched live |
| [meta-gh-guardrails](meta-gh-guardrails/) | Dependabot, CODEOWNERS, rulesets and branch protection, and secret and code scanning — verified against what the repository's visibility and plan actually offer |
| [meta-gh-community-files](meta-gh-community-files/) | The community health files a project actually needs — CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT, GOVERNANCE, FUNDING, LICENSE — each in a platform-recognized location with a real owner |
| [meta-gh-planning-release](meta-gh-planning-release/) | A label taxonomy, milestone and Projects usage sized to the team, then versioning, changelog policy, and the release procedure |
