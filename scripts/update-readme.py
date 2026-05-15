from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
TOPICS_START = "<!-- AUTO:TOPICS:START -->"
TOPICS_END = "<!-- AUTO:TOPICS:END -->"
COUNT_START = "<!-- AUTO:COUNT:START -->"
COUNT_END = "<!-- AUTO:COUNT:END -->"


def is_topic_folder(path: Path) -> bool:
    return path.is_dir() and path.name not in {".git", ".github", "scripts"}


def note_count(folder: Path) -> int:
    return sum(
        1
        for item in folder.glob("*.md")
        if item.name.lower() != "readme.md" and item.name != "TIL_TEMPLATE.md"
    )


def build_topics_block() -> str:
    folders = sorted([item for item in ROOT.iterdir() if is_topic_folder(item)], key=lambda item: item.name.lower())
    lines = [TOPICS_START]
    for folder in folders:
        count = note_count(folder)
        lines.append(f"* [{folder.name}](./{folder.name.replace(' ', '%20')}) - {count} notes")
    lines.append(TOPICS_END)
    return "\n".join(lines)


def replace_block(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start_index = text.index(start_marker)
    end_index = text.index(end_marker) + len(end_marker)
    return text[:start_index] + replacement + text[end_index:]


def build_readme() -> str:
    content = README_PATH.read_text(encoding="utf-8")
    total_notes = sum(
        1
        for path in ROOT.rglob("*.md")
        if path.name.lower() != "readme.md" and path.name != "TIL_TEMPLATE.md" and ".git" not in path.parts and ".github" not in path.parts and "scripts" not in path.parts
    )
    count_block = f"{COUNT_START}\n![TILs](https://img.shields.io/badge/TILs-{total_notes}-blue?style=for-the-badge)\n{COUNT_END}"
    content = replace_block(content, COUNT_START, COUNT_END, count_block)
    content = replace_block(content, TOPICS_START, TOPICS_END, build_topics_block())
    return content


def main() -> int:
    parser = argparse.ArgumentParser(description="Update the root README from the topic folder structure.")
    parser.add_argument("--check", action="store_true", help="Exit non-zero if README.md is out of date.")
    args = parser.parse_args()

    updated = build_readme()
    current = README_PATH.read_text(encoding="utf-8")

    if args.check:
        return 0 if current == updated else 1

    if current != updated:
        README_PATH.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())