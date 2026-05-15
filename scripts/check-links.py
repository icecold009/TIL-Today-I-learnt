from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def is_external(link: str) -> bool:
    return link.startswith(("http://", "https://", "mailto:", "tel:"))


def resolve_link(source: Path, raw_link: str) -> Path | None:
    if is_external(raw_link):
        return None

    parsed = urlsplit(raw_link)
    target = unquote(parsed.path)
    if not target:
        return None

    candidate = (source.parent / target).resolve()
    return candidate


def check_markdown_file(path: Path) -> list[str]:
    problems: list[str] = []
    content = path.read_text(encoding="utf-8")
    for _, link in LINK_PATTERN.findall(content):
        if link.startswith("#") or link.startswith("./#"):
            continue
        resolved = resolve_link(path, link)
        if resolved is None:
            continue
        if resolved.exists():
            continue
        if resolved.suffix == "" and (resolved / "README.md").exists():
            continue
        problems.append(f"{path.relative_to(ROOT)} -> {link}")
    return problems


def main() -> int:
    problems: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or ".github" in path.parts or "scripts" in path.parts:
            continue
        problems.extend(check_markdown_file(path))

    if problems:
        print("Broken markdown links found:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("No broken markdown links found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())