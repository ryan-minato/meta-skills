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

# Validate structure and the marker contract only (fast iteration).
# The validator self-tests on every run; --self-test runs fixtures alone.
validate:
    @uv run --quiet scripts/validate_repo.py

# Format and autofix the validator script.
fmt:
    ruff format scripts/
    ruff check --fix scripts/
