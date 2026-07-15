# Command surface for this repository.
# When a recipe changes, update the Validation table in AGENTS.md and the
# Quality Gates table in ARCHITECTURE.md.

_default:
    @just --list

# Install git hooks and the commit template. Run once after cloning.
setup:
    pre-commit install
    git config commit.template .gitmessage
    @echo "Setup complete. Run 'just check' before committing."

# Validate the repository's file structure.
validate-repo:
    @uv run --quiet scripts/validate_repo.py

# Check one or more skills: file structure, SKILL.md, and links.
check-skill +PATHS:
    @uv run --quiet scripts/check_skill.py {{ PATHS }}

# Check every published skill.
check-skills:
    @uv run --quiet scripts/check_skill.py --all

# Prove the marker and link checks still fire. They have no real subject until
# the first skill lands, so without this a green run would prove nothing.
selftest:
    @uv run --quiet scripts/check_skill.py --selftest

# Everything structural.
validate: validate-repo check-skills

# Lint the validators.
lint:
    @ruff check scripts/
    @ruff format --check scripts/

# Run this before proposing changes.
check: selftest validate lint
    @pre-commit run --all-files
