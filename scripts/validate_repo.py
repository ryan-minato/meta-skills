#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
"""Repository validator: catalogs, docs, translations, and the marker contract.

Covers what belongs to the repository as a whole; a single skill's structure
and SKILL.md content are check_skill.py's job. Check IDs (each has a
self-test fixture proving it fires):

    B1-B3  catalog scaffolds and inventory listings
    C1-C3  repository docs: translation pairs, root docs and their links,
           knowledge reachability
    D1-D3  marker-contract integrity
    E1-E3  published docs pages: frontmatter schema, link containment,
           directory hygiene

The self-test runs first on every invocation because the published catalogs
may be empty: with zero subjects several checks pass vacuously and could
rot unnoticed. `--self-test` runs the fixtures alone; `--no-self-test`
skips them.

MARKER below is one of the aligned copies of the marker literal; the
sync-contract skill owns the alignment procedure when the marker changes.

Exit codes: 0 clean, 1 repository issue, 2 broken validator (self-test failed).
"""

from __future__ import annotations

import argparse
import copy
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import yaml

MARKER = "Disposable meta-skill (delete after the harness is built):"
NEAR_MISS = "Disposable meta-skill ("
FENCE_TAG = "text meta-skill-marker"
TEMPLATE_PATH = ".agents/skills/meta-skill-authoring/assets/skill-template.md"
KNOWLEDGE_DIR = ".agents/knowledge"
DOCS_DIR = "docs"
SITE_DIR = "_site"
ROOT_DOCS = ("AGENTS.md", "ARCHITECTURE.md", "README.md", "README.zh.md")
CATALOG_FILES = ("CONTEXT.md", "README.md", "README.zh.md")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
CATALOG_ENTRY_RE = re.compile(r"^- `([a-z0-9][a-z0-9-]*)`", re.MULTILINE)
KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# `pages` would collide with the llms.txt lead section heading.
RESERVED_TAGS = frozenset({"pages"})


@dataclass
class Issue:
    check: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"[{self.check}] {self.path}: {self.message}"


def read_frontmatter(path: Path) -> tuple[dict | None, str | None]:
    """Parse the YAML frontmatter block; return (mapping, error)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "no YAML frontmatter block at the top of the file"
    end = text.find("\n---", 4)
    if end == -1:
        return None, "frontmatter block is never closed with `---`"
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        return None, f"frontmatter is not valid YAML ({exc})"
    if not isinstance(data, dict):
        return None, "frontmatter is not a YAML mapping"
    return data, None


def markdown_links(text: str) -> list[str]:
    """Local link targets, ignoring code fences, inline code, URLs, anchors."""
    targets: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_RE.finditer(re.sub(r"`[^`]*`", "", line)):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if target:
                targets.append(target)
    return targets


def tagged_fences(text: str) -> list[str]:
    """Bodies of every ```text meta-skill-marker fence in the text."""
    bodies: list[str] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("```") and stripped[3:].strip() == FENCE_TAG:
            body: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            bodies.append("\n".join(body).strip())
        i += 1
    return bodies


def markdown_files(root: Path) -> list[Path]:
    # _site/ is the generated docs site (never committed); scanning build
    # output would double-fire C1/D1 on copies of the sources.
    return [
        p
        for p in root.rglob("*.md")
        if ".git" not in p.parts and SITE_DIR not in p.parts
    ]


def listed_catalogs(doc_name: str, text: str) -> set[str]:
    """Catalog names the doc lists in its canonical form.

    A prose mention must not count (it would let the inventory rot while the
    check stays green), so ARCHITECTURE.md counts only backtick list entries
    in its ## Catalogs section, and the READMEs count only links into
    skills/<name>/.
    """
    if doc_name == "ARCHITECTURE.md":
        section = re.search(
            r"^## Catalogs$(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL
        )
        return set(CATALOG_ENTRY_RE.findall(section.group(1))) if section else set()
    names: set[str] = set()
    for target in markdown_links(text):
        if not target.startswith("skills/"):
            continue
        name = target.removeprefix("skills/").rstrip("/")
        if name and "/" not in name:
            names.add(name)
    return names


def check_catalogs(root: Path) -> list[Issue]:
    """B1-B3: catalog scaffolds and inventory listings."""
    issues: list[Issue] = []
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return issues
    listings = {
        name: (root / name).read_text(encoding="utf-8")
        if (root / name).is_file()
        else ""
        for name in ("ARCHITECTURE.md", "README.md", "README.zh.md")
    }
    for catalog in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        rel = str(catalog.relative_to(root))
        missing = [f for f in CATALOG_FILES if not (catalog / f).is_file()]
        if missing:
            issues.append(
                Issue(
                    "B1",
                    rel,
                    f"catalog is missing {', '.join(missing)}. Every catalog "
                    "carries author context and a bilingual README pair so it "
                    "is usable and documented. Create the missing file(s); "
                    "the sync-catalog skill owns the procedure.",
                )
            )
        for child in sorted(catalog.iterdir()):
            if child.name in CATALOG_FILES:
                continue
            if not child.is_dir() or not (child / "SKILL.md").is_file():
                issues.append(
                    Issue(
                        "B2",
                        str(child.relative_to(root)),
                        "unexpected catalog entry. A catalog holds only "
                        "CONTEXT.md, the README pair, and skill directories "
                        "containing SKILL.md — installers copy whole skill "
                        "directories, and anything else confuses them. Move "
                        "or remove it.",
                    )
                )
        for doc, text in listings.items():
            if catalog.name not in listed_catalogs(doc, text):
                form = (
                    f"a ``- `{catalog.name}` …`` entry in the ## Catalogs section"
                    if doc == "ARCHITECTURE.md"
                    else f"a `skills/{catalog.name}/` link in the catalog table"
                )
                issues.append(
                    Issue(
                        "B3",
                        rel,
                        f"catalog `{catalog.name}` is not listed in {doc}; "
                        f"expected {form} — a prose mention does not count. "
                        "The architecture catalog list and the README tables "
                        "must cover every catalog or it is undiscoverable. "
                        "Run the sync-catalog skill.",
                    )
                )
    return issues


def check_repo_docs(root: Path) -> list[Issue]:
    """C1-C3: translation pairs, doc links, knowledge reachability."""
    issues: list[Issue] = []
    for md in markdown_files(root):
        parts = md.relative_to(root).parts
        if parts[0] == "skills" and len(parts) > 3:
            continue  # inside a skill directory; check_skill.py owns those
        if md.name == "README.md" and not (md.parent / "README.zh.md").is_file():
            issues.append(
                Issue(
                    "C1",
                    str(md.relative_to(root)),
                    "has no README.zh.md sibling. Every README ships in "
                    "English and Chinese, English authoritative. Run the "
                    "sync-translation skill.",
                )
            )
        if md.name == "README.zh.md" and not (md.parent / "README.md").is_file():
            issues.append(
                Issue(
                    "C1",
                    str(md.relative_to(root)),
                    "has no README.md sibling. English is the authoritative "
                    "language; a Chinese-only README has no source of truth. "
                    "Write the English README first.",
                )
            )
    doc_paths = [root / name for name in ROOT_DOCS]
    knowledge = root / KNOWLEDGE_DIR
    if knowledge.is_dir():
        doc_paths.extend(sorted(knowledge.glob("*.md")))
    for doc in doc_paths:
        if not doc.is_file():
            issues.append(
                Issue(
                    "C2",
                    str(doc.relative_to(root)),
                    "required root document is missing. Agents enter the "
                    "repository through these files; a missing one strands "
                    "them before any other check can help. Restore it.",
                )
            )
            continue
        for target in markdown_links(doc.read_text(encoding="utf-8")):
            if not (doc.parent / target).exists():
                issues.append(
                    Issue(
                        "C2",
                        str(doc.relative_to(root)),
                        f"link `{target}` does not resolve. Broken links "
                        "strand agents mid-procedure. Fix the path or remove "
                        "the link.",
                    )
                )
    agents_md = root / "AGENTS.md"
    if knowledge.is_dir():
        agents_text = (
            agents_md.read_text(encoding="utf-8") if agents_md.is_file() else ""
        )
        linked = {(root / target).resolve() for target in markdown_links(agents_text)}
        for kfile in sorted(knowledge.glob("*.md")):
            if kfile.resolve() not in linked:
                issues.append(
                    Issue(
                        "C3",
                        str(kfile.relative_to(root)),
                        "is not linked from AGENTS.md. Knowledge files have "
                        "no self-announcement; without a when-to-read link "
                        "the file is invisible to agents — a bare prose "
                        "mention does not count. Link it from the AGENTS.md "
                        "when-to-read table.",
                    )
                )
    return issues


def check_contract(root: Path) -> list[Issue]:
    """D1-D3: marker-contract integrity."""
    issues: list[Issue] = []
    for md in markdown_files(root):
        for body in tagged_fences(md.read_text(encoding="utf-8")):
            if body != MARKER:
                issues.append(
                    Issue(
                        "D1",
                        str(md.relative_to(root)),
                        "marker fence does not match the MARKER constant in "
                        "the repository validator. All tagged copies must "
                        "agree byte for byte, or validation and disposal "
                        "disagree about what the marker is. Run the "
                        f"sync-contract skill. Expected exactly: `{MARKER}`",
                    )
                )
    for md in markdown_files(root):
        for lineno, line in enumerate(
            md.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if NEAR_MISS in line and MARKER not in line:
                issues.append(
                    Issue(
                        "D1",
                        f"{md.relative_to(root)}:{lineno}",
                        "near-miss marker: the line starts the marker but "
                        "does not contain it exactly. A drifted copy teaches "
                        "authors wrong bytes, and skills copied from it "
                        "survive cleanup. Run the sync-contract skill. "
                        f"Expected the line to contain: `{MARKER}`",
                    )
                )
    for skill_md in root.rglob("SKILL.md"):
        rel_parts = skill_md.relative_to(root).parts
        if ".git" in rel_parts or rel_parts[0] == "skills":
            continue
        data, _ = read_frontmatter(skill_md)
        description = data.get("description") if data else None
        if isinstance(description, str) and MARKER in description:
            issues.append(
                Issue(
                    "D2",
                    str(skill_md.relative_to(root)),
                    "carries the marker but lives outside skills/. The "
                    "marker means 'disposable in a target project'; on this "
                    "repository's own skills it would invite deletion of the "
                    "harness. Remove the marker from this description.",
                )
            )
    template = root / TEMPLATE_PATH
    if not template.is_file():
        issues.append(
            Issue(
                "D3",
                TEMPLATE_PATH,
                "the authoring template is missing. Every published skill "
                "starts as a copy of it; without the template authors "
                "improvise and the marker contract drifts. Restore it (the "
                "meta-skill-authoring skill owns the template).",
            )
        )
    else:
        data, _ = read_frontmatter(template)
        description = data.get("description") if data else None
        if not isinstance(description, str) or not description.startswith(MARKER):
            issues.append(
                Issue(
                    "D3",
                    TEMPLATE_PATH,
                    "the authoring template's description does not start "
                    "with the marker. Skills copied from it would ship "
                    "unmarked and survive cleanup in target projects. "
                    "Restore the marker in the template frontmatter.",
                )
            )
    return issues


def check_docs_pages(root: Path) -> list[Issue]:
    """E1-E3: published docs pages — frontmatter, links, directory hygiene."""
    issues: list[Issue] = []
    docs_dir = root / DOCS_DIR
    if not docs_dir.is_dir():
        return issues
    titles: dict[str, str] = {}
    for entry in sorted(docs_dir.iterdir()):
        rel = str(entry.relative_to(root))
        if entry.is_dir():
            issues.append(
                Issue(
                    "E3",
                    rel,
                    "docs/ holds a flat set of published pages; a "
                    "subdirectory would change the public URL surface and "
                    "the site builder does not descend into it. Move its "
                    "contents up into docs/ or out of it.",
                )
            )
            continue
        if entry.suffix != ".md" or not KEBAB_RE.match(entry.stem):
            issues.append(
                Issue(
                    "E3",
                    rel,
                    "docs/ pages are published verbatim and the filename is "
                    "the public URL slug, so only kebab-case `.md` files "
                    "belong here — READMEs and other repository files do "
                    "not (a README would also demand a Chinese mirror the "
                    "published site never serves). Rename or move it.",
                )
            )
            continue
        data, error = read_frontmatter(entry)
        if error:
            issues.append(
                Issue(
                    "E1",
                    rel,
                    f"{error}. The llms.txt index is generated from each "
                    "page's title, description, and tags; a page without "
                    "them is invisible to fetching agents. Add the "
                    "frontmatter block.",
                )
            )
            continue
        for field in ("title", "description"):
            value = data.get(field)
            if not isinstance(value, str) or not value.strip():
                issues.append(
                    Issue(
                        "E1",
                        rel,
                        f"frontmatter `{field}` must be a nonempty string. "
                        "The llms.txt index lists every page by title and "
                        "description; an empty one publishes a blank entry "
                        "agents cannot select on. Fill it in.",
                    )
                )
        title = data.get("title")
        if isinstance(title, str) and title.strip():
            if title in titles:
                issues.append(
                    Issue(
                        "E3",
                        rel,
                        f"duplicate page title `{title}` (also used by "
                        f"{titles[title]}). llms.txt links pages by title; "
                        "two identical titles are indistinguishable to a "
                        "selecting agent. Retitle one of them.",
                    )
                )
            else:
                titles[title] = rel
        tags = data.get("tags")
        if (
            not isinstance(tags, list)
            or not tags
            or not all(isinstance(t, str) for t in tags)
        ):
            issues.append(
                Issue(
                    "E1",
                    rel,
                    "frontmatter `tags` must be a nonempty list of strings. "
                    "Tags drive the llms.txt tag sections agents use to "
                    "select pages; an untagged page appears in no section. "
                    "Add tags (the docs contract lists the vocabulary).",
                )
            )
        else:
            for tag in tags:
                if not KEBAB_RE.match(tag):
                    issues.append(
                        Issue(
                            "E1",
                            rel,
                            f"tag `{tag}` is not kebab-case. Tags become "
                            "llms.txt section headings and must be stable "
                            "machine-matchable slugs. Rename it (lowercase, "
                            "digits, single hyphens).",
                        )
                    )
                elif tag in RESERVED_TAGS:
                    issues.append(
                        Issue(
                            "E1",
                            rel,
                            f"tag `{tag}` is reserved: it collides with the "
                            "llms.txt lead section heading, making the tag "
                            "section ambiguous. Pick another tag.",
                        )
                    )
            if len(set(tags)) != len(tags):
                issues.append(
                    Issue(
                        "E1",
                        rel,
                        "frontmatter `tags` contains duplicates, which "
                        "would list the page twice in one llms.txt section. "
                        "Deduplicate the list.",
                    )
                )
        for target in markdown_links(entry.read_text(encoding="utf-8")):
            resolved = (entry.parent / target).resolve()
            if not (entry.parent / target).exists():
                issues.append(
                    Issue(
                        "E2",
                        rel,
                        f"link `{target}` does not resolve. Only docs/ is "
                        "published, so every local link must point at a "
                        "sibling page; a broken one 404s for every fetching "
                        "agent. Fix the path or remove the link.",
                    )
                )
            elif not resolved.is_relative_to(docs_dir.resolve()):
                issues.append(
                    Issue(
                        "E2",
                        rel,
                        f"link `{target}` escapes docs/. The published site "
                        "serves docs/ alone, so this link 404s on the site "
                        "even though it resolves in the repository. Inline "
                        "the content or link a sibling page instead.",
                    )
                )
    return issues


def run_checks(root: Path) -> list[Issue]:
    return (
        check_catalogs(root)
        + check_repo_docs(root)
        + check_contract(root)
        + check_docs_pages(root)
    )


# --- self-test ---------------------------------------------------------------

VALID_SKILL = f"""---
name: meta-good
description: >-
  {MARKER} Scaffolds an example. Use when testing.
---

# Meta Good

A valid body with a [local link](references/notes.md).
"""

# Mirrors the canonical listing forms B3 and C3 accept; the stray prose
# mentions of `core` prove the valid fixture passes through those forms,
# not through loose matching.
BASE_FIXTURE: dict[str, str] = {
    "AGENTS.md": (
        "# Agents\n\nRead [guide.md](.agents/knowledge/guide.md) "
        "and [ARCHITECTURE.md](ARCHITECTURE.md).\n"
    ),
    "ARCHITECTURE.md": (
        "# Architecture\n\n## Catalogs\n\n- `core` — the required set.\n\n"
        "## Conventions\n\nCommit scopes come from the list above: "
        "`feat(core): …`.\n"
    ),
    "README.md": (
        "# Repo\n\n| Catalog | Why |\n|---|---|\n"
        "| [core](skills/core/) | the core of every build |\n\n"
        f"```{FENCE_TAG}\n{MARKER}\n```\n"
    ),
    "README.zh.md": (
        "# 仓库\n\n| 目录 | 用途 |\n|---|---|\n"
        "| [core](skills/core/) | 每次构建的核心 |\n\n"
        f"```{FENCE_TAG}\n{MARKER}\n```\n"
    ),
    ".agents/knowledge/guide.md": "# Guide\n",
    "skills/core/CONTEXT.md": "# core\n",
    "skills/core/README.md": "# core\n",
    "skills/core/README.zh.md": "# core\n",
    "skills/core/meta-good/SKILL.md": VALID_SKILL,
    "skills/core/meta-good/references/notes.md": "notes\n",
    "docs/example-tooling.md": (
        "---\ntitle: Example Tooling\n"
        "description: Example tools and where their docs live.\n"
        "tags: [data-science, tooling]\n---\n\n# Example Tooling\n\n"
        "Related pages: [Other Page](other-page.md).\n\n"
        "| Tool | One line | Docs |\n|---|---|---|\n"
        "| Example | an example tool | <https://example.org/docs/> |\n"
    ),
    "docs/other-page.md": (
        "---\ntitle: Other Page\ndescription: A second valid page.\n"
        "tags: [machine-learning]\n---\n\n# Other Page\n\nBody.\n"
    ),
    TEMPLATE_PATH: (
        f'---\nname: meta-template\ndescription: "{MARKER} X. Use when Y."\n---\n\nBody.\n'
    ),
}


def _with(edits: dict[str, str | None]) -> dict[str, str]:
    """BASE_FIXTURE with files replaced, or removed when the value is None."""
    fixture = copy.deepcopy(BASE_FIXTURE)
    for path, content in edits.items():
        if content is None:
            fixture.pop(path, None)
        else:
            fixture[path] = content
    return fixture


# (check id, expected issue path, fixture). Pinning the path keeps a
# fixture from passing by firing its check on an unrelated subject; paths
# match exactly or up to a `:` suffix (D1 near-miss carries a line number).
SELF_TEST_CASES: list[tuple[str, str, dict[str, str]]] = [
    ("B1", "skills/core", _with({"skills/core/CONTEXT.md": None})),
    ("B2", "skills/core/stray.md", _with({"skills/core/stray.md": "stray\n"})),
    # Prose and the commit-scope example still say `core`; only the
    # canonical listing is gone. Bare-substring B3 missed exactly this.
    (
        "B3",
        "skills/core",
        _with(
            {
                "ARCHITECTURE.md": (
                    "# Architecture\n\n## Catalogs\n\n(none listed yet)\n\n"
                    "## Conventions\n\nProse still mentions core and "
                    "`feat(core): …` anyway.\n"
                )
            }
        ),
    ),
    (
        "B3",
        "skills/core",
        _with(
            {
                "README.md": (
                    "# Repo\n\nThe core catalog is described in prose only.\n\n"
                    f"```{FENCE_TAG}\n{MARKER}\n```\n"
                )
            }
        ),
    ),
    ("C1", "skills/core/README.md", _with({"skills/core/README.zh.md": None})),
    (
        "C2",
        "AGENTS.md",
        _with(
            {
                "AGENTS.md": (
                    "# Agents\n\nRead [guide.md](.agents/knowledge/guide.md) "
                    "and [missing.md](missing.md).\n"
                )
            }
        ),
    ),
    ("C2", "AGENTS.md", _with({"AGENTS.md": None})),
    (
        "C3",
        ".agents/knowledge/unlisted.md",
        _with({".agents/knowledge/unlisted.md": "# Unlisted\n"}),
    ),
    # `contract.md` is a substring of the linked `meta-skill-contract.md`;
    # that must not satisfy C3.
    (
        "C3",
        ".agents/knowledge/contract.md",
        _with(
            {
                ".agents/knowledge/contract.md": "# Addendum\n",
                ".agents/knowledge/meta-skill-contract.md": "# Contract\n",
                "AGENTS.md": (
                    "# Agents\n\nRead [guide.md](.agents/knowledge/guide.md), "
                    "[the contract](.agents/knowledge/meta-skill-contract.md) "
                    "and [ARCHITECTURE.md](ARCHITECTURE.md). The contract.md "
                    "addendum matters too.\n"
                ),
            }
        ),
    ),
    (
        "D1",
        "README.md",
        _with(
            {
                "README.md": (
                    f"# Repo\n\n| Catalog | Why |\n|---|---|\n"
                    "| [core](skills/core/) | the core of every build |\n\n"
                    f"```{FENCE_TAG}\nWrong marker\n```\n"
                )
            }
        ),
    ),
    (
        "D1",
        "ARCHITECTURE.md",
        _with(
            {
                "ARCHITECTURE.md": (
                    "# Architecture\n\n## Catalogs\n\n- `core` — the required "
                    "set.\n\nDisposable meta-skill (delete after harness "
                    "setup): drifted.\n"
                )
            }
        ),
    ),
    (
        "D2",
        ".agents/skills/helper/SKILL.md",
        _with(
            {
                ".agents/skills/helper/SKILL.md": (
                    f'---\nname: helper\ndescription: "{MARKER} Oops."\n---\n\nBody.\n'
                )
            }
        ),
    ),
    (
        "D2",
        ".agents/skills/helper/SKILL.md",
        _with(
            {
                ".agents/skills/helper/SKILL.md": (
                    f'---\nname: helper\ndescription: "Helps. {MARKER} Oops."\n---\n\nBody.\n'
                )
            }
        ),
    ),
    (
        "D3",
        TEMPLATE_PATH,
        _with(
            {
                TEMPLATE_PATH: (
                    "---\nname: meta-template\ndescription: No marker.\n---\n\nBody.\n"
                )
            }
        ),
    ),
    ("D3", TEMPLATE_PATH, _with({TEMPLATE_PATH: None})),
    (
        "E1",
        "docs/other-page.md",
        _with(
            {
                "docs/other-page.md": (
                    "---\ntitle: Other Page\ntags: [machine-learning]\n---\n\nBody.\n"
                )
            }
        ),
    ),
    (
        "E1",
        "docs/other-page.md",
        _with(
            {
                "docs/other-page.md": (
                    "---\ntitle: Other Page\ndescription: A page.\n"
                    'tags: ["Data Science"]\n---\n\nBody.\n'
                )
            }
        ),
    ),
    (
        "E1",
        "docs/other-page.md",
        _with(
            {
                "docs/other-page.md": (
                    "---\ntitle: Other Page\ndescription: A page.\n"
                    "tags: [pages]\n---\n\nBody.\n"
                )
            }
        ),
    ),
    (
        "E2",
        "docs/other-page.md",
        _with(
            {
                "docs/other-page.md": (
                    "---\ntitle: Other Page\ndescription: A page.\n"
                    "tags: [machine-learning]\n---\n\n"
                    "A [broken link](missing-page.md).\n"
                )
            }
        ),
    ),
    # The target resolves inside the repository but outside docs/ — on the
    # published site, which serves docs/ alone, it would 404.
    (
        "E2",
        "docs/other-page.md",
        _with(
            {
                "docs/other-page.md": (
                    "---\ntitle: Other Page\ndescription: A page.\n"
                    "tags: [machine-learning]\n---\n\n"
                    "An [escaping link](../AGENTS.md).\n"
                )
            }
        ),
    ),
    ("E3", "docs/README.md", _with({"docs/README.md": "# Docs\n"})),
    ("E3", "docs/nested", _with({"docs/nested/page.md": "nested\n"})),
    (
        "E3",
        "docs/other-page.md",
        _with(
            {
                "docs/other-page.md": (
                    "---\ntitle: Example Tooling\ndescription: A page.\n"
                    "tags: [machine-learning]\n---\n\nBody.\n"
                )
            }
        ),
    ),
]


def materialize(fixture: dict[str, str], root: Path) -> None:
    for rel, content in fixture.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def run_self_test(verbose: bool) -> bool:
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        valid_root = Path(tmp) / "valid"
        materialize(BASE_FIXTURE, valid_root)
        unexpected = run_checks(valid_root)
        if unexpected:
            ok = False
            print("self-test: the fully valid fixture raised issues:")
            for issue in unexpected:
                print(f"  {issue}")
        for index, (check_id, expected_path, fixture) in enumerate(SELF_TEST_CASES):
            case_root = Path(tmp) / f"case{index}"
            materialize(fixture, case_root)
            fired = {(issue.check, issue.path) for issue in run_checks(case_root)}
            hit = any(
                check == check_id
                and (path == expected_path or path.startswith(expected_path + ":"))
                for check, path in fired
            )
            if not hit:
                ok = False
                print(
                    f"self-test: fixture {index} for {check_id} at "
                    f"{expected_path} did not trip it "
                    f"(fired: {sorted(fired) or 'none'})"
                )
            elif verbose:
                print(f"self-test: {check_id} fires on {expected_path}")
    if ok and verbose:
        print(
            f"self-test: all {len(SELF_TEST_CASES)} negative fixtures fire; "
            "the valid fixture passes"
        )
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test", action="store_true", help="run only the fixture self-test"
    )
    parser.add_argument(
        "--no-self-test", action="store_true", help="skip the fixture self-test"
    )
    args = parser.parse_args()

    if not args.no_self_test:
        if not run_self_test(verbose=args.self_test):
            print(
                "validate_repo: self-test FAILED — a check is broken; fix the "
                "validator before trusting any green run"
            )
            return 2
        if args.self_test:
            return 0

    root = Path(__file__).resolve().parent.parent
    issues = run_checks(root)
    for issue in issues:
        print(issue)
    if issues:
        print(f"validate_repo: {len(issues)} issue(s)")
        return 1
    print("validate_repo: OK (self-test passed, repository clean)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
