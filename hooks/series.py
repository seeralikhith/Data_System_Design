"""Publishes the handbook as a series, one part at a time.

series.yml lists the parts in reading order. This MkDocs hook:

- builds the site navigation from that list, one section per part, with the
  chapters of each part in file-name order;
- leaves unreleased parts and their diagrams out of the build, so unpublished
  chapters never reach the site or its search index;
- replaces the <!-- series --> marker on the home page with a card for every
  part, showing whether it is out yet.

Set PREVIEW_ALL=1 to build every part, released or not. Pages from parts that
are not released yet then carry a "Preview" note.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

import yaml
from mkdocs.exceptions import PluginError

SERIES_FILE = Path(__file__).resolve().parent.parent / "series.yml"
MARKER = "<!-- series -->"
REQUIRED_KEYS = ("title", "folder", "version", "summary", "released")
CHAPTER_FILE = re.compile(r"^(\d{2})-.+\.md$")
DIAGRAM_FILE = re.compile(r"^assets/diagrams/(\d{2})-\d+-(?:light|dark)\.svg$")

_parts: list[dict] = []


def _preview_all() -> bool:
    return os.environ.get("PREVIEW_ALL", "").strip().lower() in {"1", "true", "yes"}


def _is_built(part: dict) -> bool:
    return part["released"] or _preview_all()


def _load_parts(docs_dir: Path) -> list[dict]:
    data = yaml.safe_load(SERIES_FILE.read_text(encoding="utf-8")) or {}
    parts = data.get("parts") or []
    if not parts:
        raise PluginError("series.yml lists no parts")

    for part in parts:
        missing = [key for key in REQUIRED_KEYS if key not in part]
        if missing:
            raise PluginError(f"series.yml: {part.get('title', part)} is missing {', '.join(missing)}")
        if not isinstance(part["released"], bool):
            raise PluginError(f"series.yml: 'released' for {part['title']} must be true or false")

        folder = docs_dir / part["folder"]
        names = sorted(path.name for path in folder.glob("*.md"))
        numbers = [CHAPTER_FILE.match(name) for name in names]
        if not names or not all(numbers):
            raise PluginError(
                f"docs/{part['folder']} needs chapter files named like 01-title.md, found: {names or 'none'}"
            )
        part["chapters"] = [f"{part['folder']}/{name}" for name in names]
        part["numbers"] = [int(match.group(1)) for match in numbers]
    return parts


def on_config(config):
    global _parts
    _parts = _load_parts(Path(config["docs_dir"]))

    nav: list = [{"Home": "index.md"}]
    for part in _parts:
        if _is_built(part):
            nav.append({part["title"]: part["chapters"]})
    config["nav"] = nav
    return config


def on_files(files, config):
    hidden = [part for part in _parts if not _is_built(part)]
    hidden_folders = {part["folder"] for part in hidden}
    hidden_numbers = {number for part in hidden for number in part["numbers"]}

    for file in list(files):
        uri = file.src_uri
        diagram = DIAGRAM_FILE.match(uri)
        if uri.split("/", 1)[0] in hidden_folders or (diagram and int(diagram.group(1)) in hidden_numbers):
            files.remove(file)
    return files


def _chapter_range(part: dict) -> str:
    first, last = min(part["numbers"]), max(part["numbers"])
    return f"Chapter {first}" if first == last else f"Chapters {first} to {last}"


def _series_cards() -> str:
    cards = []
    for part in _parts:
        if part["released"]:
            status = f"[Start reading]({part['chapters'][0]})"
        elif _preview_all():
            status = f"Preview, not released yet. [Start reading]({part['chapters'][0]})"
        else:
            status = f"*Coming soon in release {part['version']}*"
        cards.append(
            "\n".join(
                [
                    f"-   **{part['title']}**",
                    "",
                    "    ---",
                    "",
                    f"    {_chapter_range(part)}. {part['summary']}",
                    "",
                    f"    {status}",
                ]
            )
        )
    return '<div class="grid cards" markdown>\n\n' + "\n\n".join(cards) + "\n\n</div>"


def on_page_markdown(markdown, page, config, files):
    uri = page.file.src_uri

    if uri == "index.md" and MARKER in markdown:
        return markdown.replace(MARKER, _series_cards())

    for part in _parts:
        if not part["released"] and uri.startswith(part["folder"] + "/"):
            title, _, body = markdown.partition("\n")
            note = (
                '!!! warning "Preview"\n'
                f"    This part is not released yet. It is planned for release {part['version']}."
            )
            return f"{title}\n\n{note}\n{body}"
    return markdown
