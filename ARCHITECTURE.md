# Architecture

## Repository layout

The following tree is the complete repository contract. Paths marked
`future` are created only when the first distributable public skill requires
them; this bootstrap intentionally has no empty catalog or marketplace.

```text
.
├── .agents/
│   ├── knowledge/
│   │   ├── meta-skill-lifecycle.md
│   │   ├── product-specification.md
│   │   ├── references.md
│   │   └── skill-quality.md
│   ├── skills/
│   │   ├── issue-workflow/
│   │   │   └── SKILL.md
│   │   ├── knowledge-sync/
│   │   │   └── SKILL.md
│   │   └── skill-authoring/
│   │       └── SKILL.md
│   └── mcp-servers.json
├── .claude/
│   └── skills -> ../.agents/skills
├── .codex/
│   └── config.toml
├── .devcontainer/
│   └── devcontainer.json
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       ├── quality.yml
│       └── secrets.yml
├── .vscode/
│   └── mcp.json
├── scripts/
│   ├── check_commit_safety.py
│   ├── check_links.py
│   ├── check_skill.py
│   ├── gen_marketplace.py
│   ├── render_mcp_configs.py
│   ├── validate_commit_message.py
│   └── validate_skills.py
├── tests/
│   ├── fixtures/
│   └── test_*.py
├── skills/                         # future: public catalogs only
│   └── <catalog>/
│       ├── README.md                # catalog purpose and skill inventory
│       ├── README.zh.md             # content-equivalent Chinese guide
│       ├── CONTEXT.md               # catalog-scoped rules and source index
│       └── <skill-name>/
│           ├── SKILL.md
│           ├── references/          # optional, conditionally loaded
│           └── scripts/             # optional, non-interactive helpers
├── .claude-plugin/                  # future: only for non-empty catalogs
│   └── marketplace.json
├── .editorconfig
├── .gitleaks.toml
├── .gitmessage
├── .mcp.json
├── .pre-commit-config.yaml
├── AGENTS.md
├── ARCHITECTURE.md
├── CLAUDE.md
├── LICENSE
├── README.md
├── README.zh.md
└── justfile
```

`<catalog>` is a capability boundary, not a generic folder. Each catalog has
the same mandatory scaffold: English and Chinese catalog guides plus one
`CONTEXT.md`; skills are its direct child directories. A skill root contains
only its `SKILL.md` and any genuinely needed optional `references/` or
`scripts/` folders. It never contains a separate README.

`CONTEXT.md` is not an installation guide. It is the progressively loaded
source for rules, boundaries, vocabulary, shared tool conventions, and
authoritative reference URLs that apply to every skill in that one catalog.
Put cross-catalog or repository-wide material in `.agents/knowledge/` instead.

## Harness file responsibilities

This table assigns one durable responsibility to every harness artifact. When
the responsibility changes, update this table and the corresponding discovery
pointer in `AGENTS.md` in the same change.

| Path | Responsibility |
| --- | --- |
| `AGENTS.md` | Sole agent discovery root: task routing, operating constraints, commands, and human boundaries. |
| `CLAUDE.md` | Minimal Claude Code pointer to `AGENTS.md`; it must not duplicate rules. |
| `ARCHITECTURE.md` | This repository's layout, ownership, adapter, catalog, quality, and synchronization contracts. |
| `README.md` / `README.zh.md` | Public, content-equivalent project introduction, lifecycle, profile, and development guidance. |
| `.agents/knowledge/product-specification.md` | Product scope, profiles, catalog contract, lifecycle, and non-goals; not a visual-design standard. |
| `.agents/knowledge/skill-quality.md` | Skill authoring shape, progressive disclosure, scripts, and behavioral-test standards. |
| `.agents/knowledge/meta-skill-lifecycle.md` | Required dual marker and future confirmation-gated removal protocol. |
| `.agents/knowledge/references.md` | Conditional index of authoritative external documentation. |
| `.agents/skills/issue-workflow/SKILL.md` | Linear issue, branch, commit, push, and draft-PR delivery procedure. |
| `.agents/skills/skill-authoring/SKILL.md` | Internal procedure for writing and validating internal or public skills. |
| `.agents/skills/knowledge-sync/SKILL.md` | Post-merge one-way knowledge synchronization from Git to Linear Documents. |
| `.agents/mcp-servers.json` | Credential-free source declaration for all supported MCP servers. |
| `.mcp.json` | Generated Claude MCP adapter. |
| `.codex/config.toml` | Generated Codex MCP adapter. |
| `.vscode/mcp.json` | Generated VS Code MCP adapter. |
| `.claude/skills` | Relative symlink exposing `.agents/skills/` to Claude Code. |
| `.devcontainer/devcontainer.json` | Trusted, reproducible development environment and idempotent setup entrypoint. |
| `.editorconfig` | Cross-editor whitespace, encoding, newline, and indentation baseline. |
| `.gitignore` | Generated/local artifacts that must not enter version control. |
| `.gitmessage` | Scoped Conventional Commit message template. |
| `.gitleaks.toml` / `.secrets.baseline` | Secret and non-anonymous-email scan policy and accepted baseline. |
| `.pre-commit-config.yaml` | Local formatting, secret, repository-contract, and commit-message gates. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Required PR handoff structure and verification checklist. |
| `.github/workflows/quality.yml` | CI execution of the full repository quality gate. |
| `.github/workflows/secrets.yml` | CI scan of repository history for secrets. |
| `justfile` | Canonical public command surface for setup, validation, tests, lint, and safety. |
| `scripts/check_skill.py` | Focused public/internal skill frontmatter and marker validator. |
| `scripts/validate_skills.py` | Repository-wide skill placement, symlink, README, and lifecycle validator. |
| `scripts/render_mcp_configs.py` | Deterministic MCP adapter renderer and drift checker. |
| `scripts/gen_marketplace.py` | Future marketplace generator/checker; succeeds without public catalogs. |
| `scripts/check_links.py` | Local Markdown-link validator. |
| `scripts/validate_commit_message.py` | Mandatory scoped Conventional Commit validator. |
| `scripts/check_commit_safety.py` | Staged-diff secret/PII and committer-identity gate. |
| `tests/fixtures/` | Deliberately valid and invalid repository-contract examples. |
| `tests/test_*.py` | Stdlib regression tests for validators and deterministic generators. |

## Catalog and skill directory contract

The following roles apply to every future catalog; no part of this scaffold is
created until that catalog has its first public skill.

| Path | Required? | Responsibility |
| --- | --- | --- |
| `skills/<catalog>/` | Yes | Capability boundary and distribution unit. A catalog owns only related public skills and their shared context. |
| `skills/<catalog>/README.md` | Yes | English catalog overview, intended users, boundaries, and current skill inventory. |
| `skills/<catalog>/README.zh.md` | Yes | Content-equivalent Chinese translation of the catalog README. |
| `skills/<catalog>/CONTEXT.md` | Yes | Progressively loaded catalog-only rules, vocabulary, boundary decisions, shared tool conventions, and authoritative source URLs. It is not copied into individual skills. |
| `skills/<catalog>/<skill-name>/` | Yes | One self-contained, distributable public meta-skill. Its name matches frontmatter and its purpose belongs to the catalog. |
| `skills/<catalog>/<skill-name>/SKILL.md` | Yes | The installed skill: Agent Skills frontmatter, trigger description, exact dual META-SKILL markers, workflow, safety constraints, and outcome. |
| `skills/<catalog>/<skill-name>/references/` | Only when needed | Conditionally loaded deep documentation that the skill explicitly links to; never an unreferenced document dump. |
| `skills/<catalog>/<skill-name>/scripts/` | Only when needed | Small non-interactive helpers invoked by the skill; each provides `--help`, validates input, and avoids credentials. |
| `.agents/skills/<skill-name>` | Yes for every public skill | Relative symlink to the public skill for this repository's dogfooding; it is not a second copy. |
| `.claude-plugin/marketplace.json` | Only for non-empty catalogs | Generated distribution metadata. It enumerates the real public skill paths and never includes internal workflows. |

Catalog context is loaded before authoring or changing a skill in that
catalog. A skill may add task-specific references below its own directory, but
it must not duplicate or contradict its catalog's `CONTEXT.md`. Repository-wide
rules remain in `.agents/knowledge/`; durable target-project output must never
inherit META-SKILL markers.

## Layers and ownership

The repository is a full L2 harness: a reproducible environment, explicit
targets, discoverable knowledge, strong quality gates, and a Linear/GitHub
delivery workflow. `AGENTS.md` is the sole discovery root; all other documents
are reached from it.

| Layer | Location | Authority |
| --- | --- | --- |
| Agent entrypoint | `AGENTS.md`, `CLAUDE.md` | Git |
| Product and structure | `.agents/knowledge/product-specification.md`, this file | Git |
| Knowledge | `.agents/knowledge/` | Git default branch |
| Internal workflows | `.agents/skills/` | Git |
| MCP declaration | `.agents/mcp-servers.json` | Git |
| Client adapters | `.mcp.json`, `.codex/config.toml`, `.vscode/mcp.json` | Generated from declaration |
| Quality | `scripts/`, `tests/`, hooks, CI | Git |
| Delivery tracking | Linear project and issues | Linear |

## Skills

Internal workflows live as real directories in `.agents/skills/` and declare
`metadata.internal: "true"`. `.claude/skills` is a relative symlink to that
directory so clients discover one shared implementation.

Future public skills live in `skills/<catalog>/<skill>/` and are exposed for
dogfooding through relative symlinks in `.agents/skills/`. They must be
self-contained, use relative links, pass the Agent Skills contract, and carry
the two META-SKILL lifecycle markers. On the first skill in a catalog, add the
catalog's `README.md`, `README.zh.md`, `CONTEXT.md`, and marketplace entry. No
empty public catalog, `skills/` directory, or marketplace exists before then.

## Catalog registry

There are no public catalogs in this bootstrap. When a catalog is first added,
list it here using `- \`name\` — purpose` and keep that list synchronized with
the actual `skills/` directories. The expected initial capability boundaries
are:

- `core` — required, profile-orchestrating meta-skills.
- platform or workflow topics such as `github`, `gitlab`, `linear`,
  `devcontainer`, and `ci-cd`.
- language or framework topics when a reusable target-specific contract is
  justified.

Adding a catalog requires its complete scaffold from the tree above, an entry
in this registry, public-skill symlinks for dogfooding, and a marketplace entry
only after the catalog contains a real skill. `CONTEXT.md` must state the
catalog's scope, boundaries with neighboring catalogs, shared conventions, and
the authoritative URLs that its skills may rely on. `scripts/validate_skills.py`
and `scripts/gen_marketplace.py` enforce the resulting distribution contracts.

## MCP adapters

`.agents/mcp-servers.json` contains endpoints and auth modes but no credentials.
`scripts/render_mcp_configs.py` deterministically produces:

- Claude: root `.mcp.json` with `mcpServers`.
- Codex: `.codex/config.toml` with `[mcp_servers.<name>]` tables.
- VS Code: `.vscode/mcp.json` with `servers`.

GitHub uses `GH_TOKEN` for Claude/Codex. VS Code intentionally relies on its
OAuth connection. Linear and Agent Skills use their supported remote flows.
Always run `just sync-mcp --check` after adapter changes.

## Validation and safety

The public command surface is the `justfile`. Stdlib-first Python scripts
validate skill shape and markers, generated MCP drift, marketplace conditions,
local Markdown links, scoped commit messages, and staged safety. Pre-commit and
commit-msg hooks run the same contracts locally; GitHub Actions reruns `just
check` and scans history. Secret and PII checks permit GitHub noreply and
`example.*` placeholders but reject likely credentials and personal email.

## Knowledge synchronization

Git's origin default branch is authoritative. `knowledge-sync` fetches it,
compares only merged `.agents/knowledge/` content, and creates or updates
equivalent Linear Documents. It never edits local knowledge from Linear and
never deletes unowned remote documents. Synchronization is post-merge only.
