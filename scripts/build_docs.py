#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
"""Docs site generator: copies docs/*.md, writes llms.txt, index.html, .nojekyll.

Generation only — schema and link validation is validate_repo.py's E1-E3
job, which pre-commit and the pages workflow run first. Output is generated
in CI and never committed; local builds target _site/, which is gitignored
and excluded from the repository validator's markdown scan.

llms.txt lists every page (link and description) under `## Pages`, then one
section per tag listing the pages that carry it. Pages sort by filename,
tags alphabetically.

The frontmatter parser is deliberately duplicated from validate_repo.py:
the scripts are self-contained single files by design.

Exit codes: 0 built, 1 unreadable page (fix via `just validate-repo`).
"""

from __future__ import annotations

import argparse
import html
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

DEFAULT_BASE_URL = "https://ryan-minato.github.io/meta-skills"
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"


@dataclass
class Page:
    name: str  # filename, e.g. "geospatial.md"
    title: str
    description: str
    tags: list[str]


def read_page(path: Path) -> Page:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or (end := text.find("\n---", 4)) == -1:
        raise ValueError(f"{path.name}: no frontmatter block")
    data = yaml.safe_load(text[4:end])
    if not isinstance(data, dict):
        raise ValueError(f"{path.name}: frontmatter is not a mapping")
    return Page(
        name=path.name,
        title=str(data.get("title", "")).strip(),
        description=str(data.get("description", "")).strip(),
        tags=[str(t) for t in data.get("tags") or []],
    )


def render_llms_txt(pages: list[Page], base_url: str) -> str:
    lines = [
        "# meta-skills docs",
        "",
        "> Agent-facing tool-documentation pages, served as raw markdown. Every page",
        "> carries YAML frontmatter with title, description, and tags.",
        "",
        "## Pages",
        "",
    ]
    for page in pages:
        lines.append(f"- [{page.title}]({base_url}/{page.name}): {page.description}")
    for tag in sorted({tag for page in pages for tag in page.tags}):
        lines += ["", f"## {tag}", ""]
        for page in pages:
            if tag in page.tags:
                lines.append(f"- [{page.title}]({base_url}/{page.name})")
    return "\n".join(lines) + "\n"


def render_index_html(pages: list[Page], base_url: str) -> str:
    items = "\n".join(
        f'      <li><a href="{p.name}">{html.escape(p.title)}</a>'
        f" — {html.escape(p.description)}</li>"
        for p in pages
    )
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>meta-skills docs</title>
  </head>
  <body>
    <h1>meta-skills docs</h1>
    <p>
      Agent-facing documentation pages, served as raw markdown. Start at
      <a href="llms.txt">llms.txt</a>; source lives at
      <a href="https://github.com/ryan-minato/meta-skills">ryan-minato/meta-skills</a>.
    </p>
    <ul>
{items}
    </ul>
  </body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path, help="output directory")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    args = parser.parse_args()
    base_url = args.base_url.rstrip("/")

    sources = sorted(DOCS_DIR.glob("*.md")) if DOCS_DIR.is_dir() else []
    try:
        pages = [read_page(path) for path in sources]
    except ValueError as exc:
        print(f"build_docs: {exc} — run `just validate-repo` for the full report")
        return 1

    out: Path = args.out
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for path in sources:
        shutil.copyfile(path, out / path.name)
    (out / "llms.txt").write_text(render_llms_txt(pages, base_url), encoding="utf-8")
    (out / "index.html").write_text(
        render_index_html(pages, base_url), encoding="utf-8"
    )
    (out / ".nojekyll").write_text("", encoding="utf-8")
    print(f"build_docs: {len(pages)} page(s) -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
