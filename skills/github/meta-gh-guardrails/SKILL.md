---
name: meta-gh-guardrails
description: >-
  Disposable meta-skill (delete after the harness is built): sets up a
  GitHub repository's platform-enforced guardrails — automated dependency
  updates via Dependabot, review routing via CODEOWNERS, branch and tag
  protection via rulesets, and the platform's secret and code scanning —
  verifying live which features the repository's visibility and plan
  actually offer. Use when a harness build on a GitHub repository must
  decide who may change what, how merges are protected, or how dependency
  and security alerts are automated. Not for the CI checks the
  protections require or the collaboration flow they enforce — those are
  separate concerns of the harness.
---

# GitHub Platform Guardrails

This skill produces the target repository's platform-enforced layer:
committed guardrail files (`.github/dependabot.yml`, `CODEOWNERS`),
applied or precisely recorded protection settings, and an AGENTS.md
section stating who owns what and what the platform will refuse. It
expects a repository whose origin remote is GitHub and a user who can
say who is responsible for which part of the code.

## Workflow

1. Assess the current state: repository visibility and plan, existing
   `.github/dependabot.yml`, `CODEOWNERS`, active rulesets or branch
   protection, and enabled security features — via `gh` when
   authenticated, otherwise by asking the user. Also collect the check
   names produced by workflows under `.github/workflows/`; protections
   key on them.
2. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.github.com, or when any recorded URL
   no longer resolves. The governing entry points are
   <https://docs.github.com/en/code-security> and
   <https://docs.github.com/en/repositories>.
3. Agree with the user which guardrails this project warrants: a solo
   private repository rarely needs approval counts; a public library
   needs update automation and scanning first.
4. Read [dependency-automation.md](references/dependency-automation.md)
   when the project has dependency manifests the user wants kept current
   automatically. It guides copying [dependabot.yml](assets/dependabot.yml)
   to `.github/dependabot.yml` and agreeing how update PRs get handled.
5. When review routing is wanted, copy
   [the CODEOWNERS skeleton](assets/CODEOWNERS) to `CODEOWNERS` and rework it:
   every line names a real path and a real owner, against syntax fetched
   this session.
6. Read [rulesets.md](references/rulesets.md) when the user wants merges
   or tags enforced by the platform rather than by convention. Apply via
   `gh` when authenticated; otherwise record the exact settings in the
   AGENTS.md deposit as manual steps.
7. Enable secret scanning and code scanning per live-verified
   availability — or record them as manual steps — then copy
   [agents-md-guardrails.md](assets/agents-md-guardrails.md) into the
   target's AGENTS.md and rework it: the protection map, the ownership
   map, and the standing rule for handling update PRs. This deposit is
   what future agents keep after this skill is deleted.

Done when: every chosen guardrail is either a committed file or an
applied (or precisely recorded) platform setting, required status checks
name checks that actually exist in this repository, and AGENTS.md states
who owns what and what the platform will refuse.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- Feature availability differs by visibility and plan — verify live
  before promising secret scanning or required reviewers.
- CODEOWNERS errors are skipped silently, line by line — a typo protects
  nothing and reports nothing.
- A required status check whose name matches no real check blocks every
  merge forever; one whose name drifts after a CI rename protects
  nothing. Record the name coupling in AGENTS.md.
