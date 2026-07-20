---
name: meta-gh-community-files
description: >-
  Disposable meta-skill (delete after the harness is built): decides
  which community health files a GitHub-hosted project actually needs —
  CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT, GOVERNANCE, FUNDING,
  LICENSE — and writes each chosen file in a platform-recognized location
  with a real owner behind it, verifying the currently recognized
  filenames and locations live from the docs. Use when a harness build on
  a GitHub repository must prepare what an outside contributor, reporter,
  or user will see. Not for the internal conventions these files
  summarize — commit format, PR flow, and protections are separate
  concerns of the harness.
---

# GitHub Community Health Files

This skill produces the outward-facing document set of the target
repository: only the files its real audience needs, each in a location
GitHub surfaces, each with a named owner, none with placeholders. It
expects a repository whose origin remote is GitHub and a user who can
say who answers for security reports, conduct enforcement, and
contributions.

## Workflow

1. Assess the audience with the user: public or private, accepting
   outside contributions or not, and which community files already
   exist. Read [org-defaults.md](references/org-defaults.md) when the
   repository belongs to an organization — an org-level defaults
   repository may already provide files this one should inherit rather
   than duplicate.
2. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.github.com, or when any recorded URL
   no longer resolves. Fetch the currently recognized file set and
   locations from <https://docs.github.com/en/communities>.
3. Decide with the user which files this project needs, and name a real
   owner for each: a security contact who reads the inbox, a
   code-of-conduct enforcer, real funding handles. A file nobody owns is
   not created.
4. CONTRIBUTING: copy [contributing.md](assets/contributing.md) to
   `CONTRIBUTING.md` and rework every line against the conventions the
   project's AGENTS.md and task runner already record — it documents
   commands that exist, never aspirations.
5. SECURITY and SUPPORT: copy [security.md](assets/security.md) and
   [support.md](assets/support.md) likewise. A code of conduct is
   adopted, never drafted: fetch the current text of an established
   covenant (<https://www.contributor-covenant.org/> is the common one)
   and fill in the enforcement contact. A funding file is written
   directly against the schema fetched this session.
6. Read [licensing.md](references/licensing.md) when the repository has
   no LICENSE and will be public.
7. Copy
   [agents-md-community-files.md](assets/agents-md-community-files.md)
   into the target's AGENTS.md and rework it: which community files
   exist, who owns each, and the standing rule that CONTRIBUTING is
   updated in the same change that alters the commands it documents.
   This deposit is what future agents keep after this skill is deleted.

Done when: every community file the project needs exists in a
platform-recognized location with a named owner and no placeholder — and
no file was created for an audience the project does not have.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- The platform surfaces only specific filenames in specific locations —
  verify the currently recognized set live; a misplaced file silently
  never appears in the UI.
- Never draft a code of conduct or a license text from scratch — adopt
  canonical texts, fetched live.
- An unmonitored security contact is worse than none: it promises a
  response nobody will send.
