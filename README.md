# meta-skills

[中文](README.zh.md)

Disposable meta-skills that help an agent build a durable **harness** in
your project — and then get out of the way.

A harness is everything agent-visible that helps agents meet your
expectations: the environment they run in, the constraints on what they
produce, the tools they can call, and the knowledge they can reach. Building
a good one is a skill in itself; that is what these skills carry. They are
the inverse of a normal skill library: they are designed to delete
themselves.

## How It Works

1. **Install** the `core` catalog into your project's skill directory (for
   example `./.agents/skills/`), then preferably install the topic catalogs
   that fit your stack. Single-skill installs remain supported.
2. **Ask** — hand your project's requirements and conventions to an agent
   and ask it to build a harness.
3. **Build** — the agent invokes the meta-skills, which encode the
   practices.
4. **Remove** — once the harness is built and verified, the agent finds
   every meta-skill by its marker and deletes them all. They have done their
   job, and every skill left installed costs context in every future
   session.

Removal is confirmation-gated by design: an earlier request to build a
harness is never treated as consent to delete anything.

## How A Meta-Skill Identifies Itself

Every published skill's description begins with the marker:

```text meta-skill-marker
Disposable meta-skill (delete after the harness is built):
```

The marker is how an agent finds these skills again in order to remove
them. Identification is by **description, not by name**, because installers
rename skills to avoid collisions — the `meta-` name prefix only groups
them in the file tree.

## Catalogs

| Catalog | Contents | Install scope |
|---|---|---|
| [core](skills/core/) | The required set: enough to take any project from no harness to a working one, including live catalog/skill discovery and centralized installation guidance | Per project, before a harness build |
| [frontend](skills/frontend/) | Design description and visual language for projects with a user-facing frontend | Per project, on top of `core`, only when the target has a visual surface |
| [python](skills/python/) | Trusted defaults and doc URLs for Python projects: docstring and comment conventions, testing setup, toolchain choices, and locating a package's documentation | Per project, on top of `core`, only when the target is a Python project |
| [machine-learning](skills/machine-learning/) | Project scaffolds (quick experiment, maintainable training) and GPU-image discovery for ML projects, each declaring its opinionated defaults; documentation entry points live in the published docs index | Per project, on top of `core`, only when the target trains, finetunes, serves, or builds on ML models |
| [data-science](skills/data-science/) | Opinionated project scaffolds for data-analysis and scientific-computing targets that declare their defaults; documentation entry points live in the published docs index | Per project, on top of `core`, only when the target analyzes data or does scientific computing |
| [github](skills/github/) | Platform-side conventions for GitHub-hosted projects, one skill per concern: collaboration flow and templates, CI gates that mirror local checks, guardrails (Dependabot, CODEOWNERS, rulesets, scanning), community health files, planning and releases — platform capabilities always fetched live from the GitHub docs | Per project, on top of `core`, only when the target is hosted on GitHub |
| [gitlab](skills/gitlab/) | Platform-side conventions for GitLab-hosted projects, mirroring the `github` catalog's five concerns (collaboration, CI, guardrails, community files, planning and releases) while respecting the instance's version and tier — platform capabilities always fetched live from the GitLab docs | Per project, on top of `core`, only when the target is hosted on GitLab (gitlab.com or self-managed) |

Catalog installation is the recommendation, not an availability guarantee:
only `core` may be assumed present. A skill names every non-core dependency
explicitly and directs the agent to `meta-skill-discovery` for the current
inventory and installation guidance.

## Installation

Use `meta-skill-discovery` for live catalog and skill filtering, single-skill
selection, and project or global scope guidance. The commands below show the
recommended project-scoped catalog installs.

As Claude Code plugins — each catalog is one plugin in this repository's
marketplace:

```bash
claude plugin marketplace add ryan-minato/meta-skills
claude plugin install core@meta-skills --scope project
claude plugin install frontend@meta-skills --scope project   # only with a visual surface
claude plugin install python@meta-skills --scope project     # only for Python projects
claude plugin install machine-learning@meta-skills --scope project  # only for ML projects
claude plugin install data-science@meta-skills --scope project      # only for data/scientific projects
claude plugin install github@meta-skills --scope project            # only for GitHub-hosted projects
claude plugin install gitlab@meta-skills --scope project            # only for GitLab-hosted projects
```

Plugin-managed installs are removed with `claude plugin uninstall`, not by
the disposal skill's file deletion.

Or with the skills CLI — point it at a catalog path, which scopes
discovery to exactly that catalog:

```bash
npx skills add ryan-minato/meta-skills/skills/core
npx skills add ryan-minato/meta-skills/skills/frontend      # only with a visual surface
npx skills add ryan-minato/meta-skills/skills/python        # only for Python projects
npx skills add ryan-minato/meta-skills/skills/machine-learning  # only for ML projects
npx skills add ryan-minato/meta-skills/skills/data-science  # only for data/scientific projects
npx skills add ryan-minato/meta-skills/skills/github        # only for GitHub-hosted projects
npx skills add ryan-minato/meta-skills/skills/gitlab        # only for GitLab-hosted projects
npx skills add ryan-minato/meta-skills/skills               # every published skill
```

Or copy skill directories (`skills/<catalog>/<skill>/`) straight into your
project's skill directory. Project scope is the default and recommendation:
these skills scaffold one job in one project. Global installation is supported
when deliberately requested, but it exposes the disposable skills to every
project and requires matching global cleanup afterward.

## Related

The sibling library [ryan-minato/skills](https://github.com/ryan-minato/skills)
ships **durable** skills, including `meta-harness`, a general design aid
that stays installed. This repository ships the disposable, per-project
builders. Both are useful together.

## Contributing

Start at [AGENTS.md](AGENTS.md), then [ARCHITECTURE.md](ARCHITECTURE.md).
Run `just setup` once, and `just check` before proposing changes.

## License

[Apache-2.0](LICENSE)
