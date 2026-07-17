# gitlab

[中文](README.zh.md)

Meta-skills for projects hosted on GitLab (gitlab.com or self-managed):
collaboration conventions and templates, CI quality gates that mirror
local checks, platform guardrails (protections, approvals, code
ownership, scanning, update automation), community files, and planning
and release conventions. Every skill teaches the harness-building agent
to fetch current platform capabilities live from the GitLab docs —
respecting the instance's version and tier — instead of prescribing
versioned syntax. Install on top of `core`, per project, and only when
the target is hosted on GitLab — this catalog is not part of the
default install.

These skills are **disposable**: once the harness is built and verified,
the `core` removal skill deletes them together with the rest.

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install gitlab@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/gitlab
npx skills add ryan-minato/meta-skills/skills/gitlab --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-gl-collaboration](meta-gl-collaboration/) | Commit format, branch and merge request flow, review expectations, and issue intake — writes the `.gitlab/` description templates and deposits the agreed conventions into AGENTS.md |
| [meta-gl-cicd](meta-gl-cicd/) | A `.gitlab-ci.yml` pipeline that gates merge requests by mirroring the project's local checks, with keywords and runner capabilities always fetched live |
| [meta-gl-guardrails](meta-gl-guardrails/) | Protected branches and tags, approval rules, CODEOWNERS, the platform's dependency and secret scanning, and third-party update automation — verified against the instance's tier |
| [meta-gl-community-files](meta-gl-community-files/) | The community health files a project actually needs — CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT, GOVERNANCE, LICENSE — each with a real owner, checked against what GitLab actually surfaces |
| [meta-gl-planning-release](meta-gl-planning-release/) | A label taxonomy, milestone, board, and epic usage sized to the team and tier, then versioning, changelog policy, and the release procedure |
