# github — Catalog Context

Read this before authoring or reviewing anything in `skills/github/`.
Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `github`. Neither this file nor
the catalog READMEs ship to targets — installers copy skill directories
only.

## Goal

`github` holds procedure skills for projects hosted on GitHub
(github.com or GitHub Enterprise Server). Each skill establishes one
platform-side concern of the target's harness — collaboration
conventions, CI gates, platform guardrails, community files, planning
and releases — by fetching current platform capabilities live, agreeing
conventions with the user, writing the target's own files (`.github/`
configuration, community documents), and depositing the decisions into
the target's AGENTS.md. It installs per project, on top of `core`, and
only when the target's origin remote is GitHub (visible in
`git remote -v`) — it is not part of the default install. The sibling
`gitlab` catalog mirrors this one for GitLab-hosted targets.

## Constraints On What May Enter

- **GitHub-only usefulness.** A skill belongs here only if it is useless
  to a project not hosted on GitHub. Anything useful regardless of host
  belongs in `core`; anything GitLab-shaped belongs in `gitlab`.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Teach discovery, never prescribe syntax.** No skill records platform
  syntax (workflow YAML, issue-form schema, the Dependabot schema,
  CODEOWNERS grammar), pinned tool or action versions, or feature
  availability in prose. Details are always fetched live through the
  shared `docs-navigation.md` procedure; skeleton assets sketch shape
  only, and the SKILL.md that copies one says so — the asset itself stays
  a bare resource. A hard-coded action version or schema fragment
  presented as authoritative is a bug.
- **Doc-root fidelity.** Recorded entry points are the docs root and the
  `/en/<product>` roots; deep guide pages are navigation results, never
  records. A dead or moved URL is a bug, fixed in the same change that
  finds it.
- **Existing conventions win.** Every default applies only when the user
  expressed no preference and the target shows no working convention. No
  skill migrates a working setup unbidden.
- **Concern boundaries.** Flow conventions and templates belong to
  `meta-gh-collaboration`; workflows that gate merges to `meta-gh-cicd`;
  platform-enforced settings, scanning, Dependabot, and CODEOWNERS to
  `meta-gh-guardrails`; outward-facing documents to
  `meta-gh-community-files`; labels, milestones, versioning, changelogs,
  and releases (including workflows that cut releases) to
  `meta-gh-planning-release`. A skill that grows across a boundary is
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
documentation. Skill names take `meta-gh-<concern>`. Every skill carries
`references/docs-navigation.md`, byte-identical across the catalog; the
canonical copy is
`skills/github/meta-gh-collaboration/references/docs-navigation.md`,
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
same change. GitHub Docs particulars, verified on the same date: the
agent index <https://docs.github.com/llms.txt> is a shallow curated
landing page (not a sitemap — absence there proves nothing), there is no
`llms-full.txt`, and every docs page also serves its Markdown source
when `.md` is appended to the page URL. Re-verify those properties when
refreshing this table.

Sections mirror the catalog's skills, in order; each skill's rows land
in the same change that adds the skill.

### Shared (docs-navigation.md, all skills)

| Source | Docs |
|---|---|
| GitHub Docs | <https://docs.github.com/> — llms.txt: <https://docs.github.com/llms.txt> |

### meta-gh-collaboration

| Source | Docs |
|---|---|
| GitHub Docs: pull requests | <https://docs.github.com/en/pull-requests> |
| GitHub Docs: communities (templates) | <https://docs.github.com/en/communities> |
| Conventional Commits | <https://www.conventionalcommits.org/> |

### meta-gh-cicd

| Source | Docs |
|---|---|
| GitHub Docs: actions | <https://docs.github.com/en/actions> |

### meta-gh-guardrails

| Source | Docs |
|---|---|
| GitHub Docs: code security | <https://docs.github.com/en/code-security> |
| GitHub Docs: repositories | <https://docs.github.com/en/repositories> |
| GitHub CLI manual | <https://cli.github.com/manual/> |

### meta-gh-community-files

| Source | Docs |
|---|---|
| GitHub Docs: communities | <https://docs.github.com/en/communities> |
| GitHub Docs: organizations | <https://docs.github.com/en/organizations> |
| Contributor Covenant | <https://www.contributor-covenant.org/> |
| Choose a License | <https://choosealicense.com/> |

### meta-gh-planning-release

| Source | Docs |
|---|---|
| GitHub Docs: issues (planning) | <https://docs.github.com/en/issues> |
| GitHub Docs: repositories (releases) | <https://docs.github.com/en/repositories> |
| GitHub Docs: actions (release automation) | <https://docs.github.com/en/actions> |
| SemVer | <https://semver.org/> |
| CalVer | <https://calver.org/> |
| Keep a Changelog | <https://keepachangelog.com/> |
| release-please | <https://github.com/googleapis/release-please> |
| semantic-release | <https://semantic-release.gitbook.io/> |
