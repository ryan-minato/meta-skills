# gitlab — Catalog Context

Read this before authoring or reviewing anything in `skills/gitlab/`.
Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `gitlab`. Neither this file nor
the catalog READMEs ship to targets — installers copy skill directories
only.

## Goal

`gitlab` holds procedure skills for projects hosted on GitLab
(gitlab.com or a self-managed instance). Each skill establishes one
platform-side concern of the target's harness — collaboration
conventions, CI gates, platform guardrails, community files, planning
and releases — by fetching current platform capabilities live, agreeing
conventions with the user, writing the target's own files (`.gitlab/`
templates, `.gitlab-ci.yml`, community documents), and depositing the
decisions into the target's AGENTS.md. It installs per project, on top
of `core`, and only when the target's origin remote is a GitLab
instance (visible in `git remote -v`) — it is not part of the default
install. The sibling `github` catalog mirrors this one for GitHub-hosted
targets.

## Constraints On What May Enter

- **GitLab-only usefulness.** A skill belongs here only if it is useless
  to a project not hosted on GitLab. Anything useful regardless of host
  belongs in `core`; anything GitHub-shaped belongs in `github`.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Teach discovery, never prescribe syntax.** No skill records platform
  syntax (`.gitlab-ci.yml` keywords, template mechanics, CODEOWNERS
  grammar), pinned tool versions, or feature availability in prose.
  Details are always fetched live through the shared
  `docs-navigation.md` procedure; skeleton assets sketch shape only, and
  the SKILL.md that copies one says so — the asset itself stays a bare
  resource. A hard-coded CI keyword list or schema fragment presented as
  authoritative is a bug.
- **Doc-root fidelity.** The recorded entry points are the docs root and
  its llms.txt index; GitLab docs paths churn, so topic URLs live only
  in this registry — dated, and re-locatable through the llms.txt index
  when they die. A dead or moved URL is a bug, fixed in the same change
  that finds it.
- **Instance-version honesty.** docs.gitlab.com documents the latest
  GitLab. When the target is self-managed, feature claims are verified
  against what the instance actually runs — it serves its own matching
  docs at `<instance-url>/help`.
- **Tier honesty.** Features are gated by tier (Free, Premium,
  Ultimate). No skill records a paid-tier feature as a default; tier
  badges are read live, and the free-tier fallback is designed first.
- **Existing conventions win.** Every default applies only when the user
  expressed no preference and the target shows no working convention. No
  skill migrates a working setup unbidden.
- **Concern boundaries.** Flow conventions and templates belong to
  `meta-gl-collaboration`; the pipeline that gates merges to
  `meta-gl-cicd`; platform-enforced settings, scanning, and update
  automation to `meta-gl-guardrails`; outward-facing documents to
  `meta-gl-community-files`; labels, milestones, boards, versioning,
  changelogs, and releases (including pipeline jobs that cut releases)
  to `meta-gl-planning-release`. A skill that grows across a boundary is
  split, not grown.
- **Registry completeness.** Every URL any skill cites — in SKILL.md and
  references — appears in this file's Upstream Registry, in the section
  mirroring its skill. A URL in a skill but not the registry is a bug.
- **Sibling-catalog overlap is allowed.** Platform-neutral specs
  (Conventional Commits, SemVer, CalVer, Keep a Changelog, Contributor
  Covenant, Choose a License) may be recorded independently when that keeps a
  skill coherent. Reuse is also allowed through the repository dependency
  contract; catalog co-membership never implies installation.

## Authoring

Start from the authoring skill's template
(`.agents/skills/meta-skill-authoring/assets/skill-template.md`), which
ships with the marker pre-filled. The marker's exact bytes and YAML form
are defined in the contract; copy them from there, never from rendered
documentation. Skill names take `meta-gl-<concern>`. Every skill carries
`references/docs-navigation.md`, byte-identical across the catalog (a
different file from the `github` catalog's — the platforms' navigation
mechanics genuinely differ); the canonical copy is
`skills/gitlab/meta-gl-collaboration/references/docs-navigation.md`,
and any change to it is copied to every sibling in the same change
(`sha256sum` across the copies is the review check).

## References

- llms.txt specification (agent-preferred plain-text doc indexes) —
  <https://llmstxt.org/>
- Agent Skills specification — reachable through the `agentskills` MCP
  server.

## Upstream Registry

Every doc URL the catalog's skills cite — a maintainer snapshot, last
verified live 2026-07-17. The URL is authoritative: when this table and
the platform's docs disagree, the docs win and this file updates in the
same change. GitLab Docs particulars, verified on the same date: the
agent index <https://docs.gitlab.com/llms.txt> is a comprehensive
standard-format index (the primary navigation move is fetching it and
searching for the topic), there is no `llms-full.txt`, and pages serve
rendered HTML only — appending `.md` redirects to authentication.
Re-verify those properties when refreshing this table. Topic URLs below
are dated snapshots: when one dies, re-locate it through the llms.txt
index and update this row.

Sections mirror the catalog's skills, in order; each skill's rows land
in the same change that adds the skill.

### Shared (docs-navigation.md, all skills)

| Source | Docs |
|---|---|
| GitLab Docs | <https://docs.gitlab.com/> — llms.txt: <https://docs.gitlab.com/llms.txt> |

### meta-gl-collaboration

| Source | Docs |
|---|---|
| Merge requests (topic snapshot) | <https://docs.gitlab.com/user/project/merge_requests/> |
| Description templates (topic snapshot) | <https://docs.gitlab.com/user/project/description_templates/> |
| Conventional Commits | <https://www.conventionalcommits.org/> |

### meta-gl-cicd

| Source | Docs |
|---|---|
| GitLab CI/CD | <https://docs.gitlab.com/ci/> |
| CI/CD Catalog (components) | <https://gitlab.com/explore/catalog> |

### meta-gl-guardrails

| Source | Docs |
|---|---|
| Application security (topic snapshot) | <https://docs.gitlab.com/user/application_security/> |
| Protected branches (topic snapshot) | <https://docs.gitlab.com/user/project/repository/branches/protected/> |
| CODEOWNERS (topic snapshot) | <https://docs.gitlab.com/user/project/codeowners/> |
| Renovate | <https://docs.renovatebot.com/> |
| GitLab CLI (glab) | <https://gitlab.com/gitlab-org/cli> |

### meta-gl-community-files

| Source | Docs |
|---|---|
| Contributor Covenant | <https://www.contributor-covenant.org/> |
| Choose a License | <https://choosealicense.com/> |

### meta-gl-planning-release

| Source | Docs |
|---|---|
| Milestones (topic snapshot) | <https://docs.gitlab.com/user/project/milestones/> |
| Releases (topic snapshot) | <https://docs.gitlab.com/user/project/releases/> |
| SemVer | <https://semver.org/> |
| CalVer | <https://calver.org/> |
| Keep a Changelog | <https://keepachangelog.com/> |
