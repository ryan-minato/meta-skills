---
name: meta-gl-community-files
description: >-
  Disposable meta-skill (delete after the harness is built): decides
  which community health files a GitLab-hosted project actually needs —
  CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT, GOVERNANCE, LICENSE —
  and writes each chosen file with a real owner behind it, verifying live
  which of these files the platform actually surfaces in its UI and
  linking the rest from the README. Use when a harness build on a GitLab
  project (gitlab.com or self-managed) must prepare what an outside
  contributor, reporter, or user will see. Not for the internal
  conventions these files summarize — commit format, MR flow, and
  protections are separate concerns of the harness.
---

# GitLab Community Health Files

This skill produces the outward-facing document set of the target
project: only the files its real audience needs, each with a named
owner, none with placeholders — and each either surfaced by the
platform or deliberately linked from the README, because GitLab
surfaces fewer of these files than other forges. It expects a
repository whose origin remote is a GitLab instance and a user who can
say who answers for security reports, conduct enforcement, and
contributions.

## Workflow

1. Assess the audience with the user: public or private, accepting
   outside contributions or not, and which community files already
   exist.
2. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.gitlab.com, or when any recorded URL
   no longer resolves. Verify through the llms.txt index which files
   the platform actually links in the project UI (license, contribution
   guide, changelog detection) — do not assume parity with other
   forges.
3. Decide with the user which files this project needs, and name a real
   owner for each: a security contact who reads the inbox, a
   code-of-conduct enforcer. A file nobody owns is not created. A file
   the platform does not surface is still worth having only when humans
   are pointed at it — link it from the README in the same change.
4. CONTRIBUTING: copy [contributing.md](assets/contributing.md) to
   `CONTRIBUTING.md` and rework every line against the conventions the
   project's AGENTS.md and task runner already record — it documents
   commands that exist, never aspirations.
5. SECURITY and SUPPORT: copy [security.md](assets/security.md) and
   [support.md](assets/support.md) likewise — SECURITY names a reporting
   channel a real person monitors and, where this instance and tier offer
   private vulnerability reporting (verify live), prefers it so reports
   never start in a public issue, with confidential issues the common
   fallback; SUPPORT lists only channels somebody actually answers. A code
   of conduct is adopted, never drafted: fetch the current text of an
   established
   covenant (<https://www.contributor-covenant.org/> is the common one)
   and fill in the enforcement contact.
6. Read [licensing.md](references/licensing.md) when the repository has
   no LICENSE and will be public.
7. Copy
   [agents-md-community-files.md](assets/agents-md-community-files.md)
   into the target's AGENTS.md and rework it: which community files
   exist, who owns each, and the standing rule that CONTRIBUTING is
   updated in the same change that alters the commands it documents.
   This deposit is what future agents keep after this skill is deleted.

Done when: every community file the project needs exists with a named
owner and no placeholder, each is either platform-surfaced (verified
live) or linked from the README — and no file was created for an
audience the project does not have.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- Do not assume another forge's community-file mechanics: verify per
  file whether GitLab surfaces it at all, on this instance's version.
- Never draft a code of conduct or a license text from scratch — adopt
  canonical texts, fetched live.
- An unmonitored security contact is worse than none: it promises a
  response nobody will send.
