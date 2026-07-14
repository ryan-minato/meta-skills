default:
    @just --list

setup:
    pre-commit install --hook-type pre-commit
    pre-commit install --hook-type commit-msg
    git config commit.template .gitmessage

validate:
    python3 scripts/validate_skills.py
    python3 scripts/render_mcp_configs.py --check
    python3 scripts/check_links.py

lint:
    ruff check scripts
    ruff format --check scripts

check-skill +paths:
    python3 scripts/check_skill.py {{paths}}

sync-mcp mode="--write":
    python3 scripts/render_mcp_configs.py {{mode}}

gen-marketplace mode="--write":
    python3 scripts/gen_marketplace.py {{mode}}

commit-gate:
    python3 scripts/check_commit_safety.py

check: validate lint
    pre-commit run --all-files
