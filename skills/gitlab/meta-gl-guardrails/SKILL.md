---
name: meta-gl-guardrails
description: >-
  Disposable meta-skill (delete after the harness is built): sets up a
  GitLab project's platform-enforced guardrails — protected branches and
  tags, merge request approval rules, review routing via CODEOWNERS, the
  platform's dependency and secret scanning, and third-party
  dependency-update automation (GitLab ships no first-party update bot;
  Renovate is the established option) — verifying live which features the
  instance's tier actually offers. Use when a harness build on a GitLab
  project (gitlab.com or self-managed) must decide who may change what,
  how merges are protected, or how dependency and security alerts are
  handled. Not for the CI jobs the protections require or the
  collaboration flow they enforce — those are separate concerns of the
  harness.
---

# GitLab Platform Guardrails

This skill produces the target project's platform-enforced layer:
committed guardrail files (`CODEOWNERS`, an update-bot config when
wanted), applied or precisely recorded protection and approval settings,
and an AGENTS.md section stating who owns what and what the platform
will refuse. It expects a repository whose origin remote is a GitLab
instance and a user who can say who is responsible for which part of the
code.

## Workflow

1. Assess the current state: the instance (gitlab.com or self-managed,
   and its tier), existing protected branches and tags, approval rules,
   `CODEOWNERS`, and enabled security scanners — via `glab` or the API
   when authenticated (the CLI lives at
   <https://gitlab.com/gitlab-org/cli>), otherwise by asking the user.
   Also collect the job names from `.gitlab-ci.yml`; merge gates key on
   them.
2. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.gitlab.com, or when any recorded URL
   no longer resolves. Tier badges matter on every page this skill
   touches: several approval and ownership features are Premium — read
   the badge, and design the free-tier fallback first.
3. Agree with the user which guardrails this project warrants: a solo
   private project rarely needs approval rules; a public library needs
   update automation and scanning first.
4. Read [dependency-automation.md](references/dependency-automation.md)
   when the project has dependency manifests the user wants kept current
   automatically — detection (the platform's dependency scanning) and
   updating (a third-party bot) are separate decisions there.
5. When review routing is wanted, copy
   [the CODEOWNERS skeleton](assets/CODEOWNERS) to `CODEOWNERS` and rework it:
   every line names a real path and a real owner, against syntax located
   live through the llms.txt index. Whether CODEOWNERS can *require*
   approvals is tier-gated — verify before promising it.
6. Read
   [approvals-protections.md](references/approvals-protections.md) when
   the user wants merges or tags enforced by the platform — protected
   branches, approval rules, or merge-gate settings. Apply via `glab`
   or the API when authenticated; otherwise record the exact settings in
   the AGENTS.md deposit as manual steps.
7. Enable the scanning the tier offers (secret detection, dependency and
   static scanning) per live-verified availability — most wire into the
   pipeline as documented includes or components; agree with the user
   before touching `.gitlab-ci.yml`. Then copy
   [agents-md-guardrails.md](assets/agents-md-guardrails.md) into the
   target's AGENTS.md and rework it. This deposit is what future agents
   keep after this skill is deleted.

Done when: every chosen guardrail is either a committed file or an
applied (or precisely recorded) platform setting, merge gates reference
jobs that actually exist in this project's pipeline, and AGENTS.md
states who owns what and what the platform will refuse.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- Approval rules and CODEOWNERS-required approvals are tier-gated —
  verify on this instance before recording them as guarantees, and say
  in AGENTS.md which guardrails are convention-only on the current tier.
- CODEOWNERS errors are skipped silently, line by line — a typo protects
  nothing and reports nothing.
- A merge gate keyed to a renamed or deleted CI job blocks every merge
  forever, or protects nothing. Record the name coupling in AGENTS.md.
