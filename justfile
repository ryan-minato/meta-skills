# Command surface. Check logic lives once, in .pre-commit-config.yaml;
# recipes here only wrap it. When a recipe changes, update the Validation
# section in AGENTS.md and the Quality Gates table in ARCHITECTURE.md.

_default:
    @just --list

# Install git hooks and the commit template. Run once after cloning.
setup:
    pre-commit install
    git config commit.template .gitmessage
    @echo "Setup complete. Run 'just check' before proposing changes."

# Run every gate: hygiene, lint, secrets, and the repository validator.
check:
    pre-commit run --all-files

# Validate repository structure: catalogs, docs, translations, contract.
# Both validators self-test on every run; --self-test runs fixtures alone.
validate-repo:
    @uv run --quiet scripts/validate_repo.py

# Check one or more skills: file structure, SKILL.md content, and links.
check-skill +PATHS:
    @uv run --quiet scripts/check_skill.py {{ PATHS }}

# Check every published and internal skill.
check-skills:
    @uv run --quiet scripts/check_skill.py --all

# Everything structural (fast iteration; `just check` runs the full registry).
validate: validate-repo check-skills

# Build the docs site + llms.txt into _site/ (gitignored; CI deploys it).
docs-build:
    @uv run --quiet scripts/build_docs.py --out _site

# Format and autofix the validator scripts.
fmt:
    ruff format scripts/
    ruff check --fix scripts/
