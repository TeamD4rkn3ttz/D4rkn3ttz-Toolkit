#!/usr/bin/env python3
"""Validate this repository's bilingual Codex skill packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "en": ROOT / "skills/threat-intelligence-report/en",
    "ko": ROOT / "skills/threat-intelligence-report/ko",
}
REQUIRED_REFERENCES = {"examples.md", "output-formats.md", "verification.md"}
REQUIRED_ROOT_FILES = {
    "README.md",
    "LICENSE",
    "NOTICE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CITATION.cff",
}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, [f"{path.relative_to(ROOT)}: missing opening YAML delimiter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, [f"{path.relative_to(ROOT)}: missing closing YAML delimiter"]

    metadata: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.startswith((" ", "\t")) or ":" not in line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: "
                "frontmatter must use one-line key/value entries"
            )
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip().strip("\"'")
        if key in metadata:
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: duplicate key {key}")
        metadata[key] = value
    return metadata, errors


def validate_skill(language: str, directory: Path) -> list[str]:
    errors: list[str] = []
    skill_file = directory / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_file.relative_to(ROOT)}: required file is missing"]

    metadata, frontmatter_errors = parse_frontmatter(skill_file)
    errors.extend(frontmatter_errors)
    if set(metadata) != {"name", "description"}:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: frontmatter keys must be exactly "
            "'name' and 'description'"
        )
    expected_name = f"threat-intelligence-report-{language}"
    if metadata.get("name") != expected_name:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: name must be {expected_name!r}"
        )
    if not NAME_PATTERN.fullmatch(metadata.get("name", "")):
        errors.append(f"{skill_file.relative_to(ROOT)}: invalid skill name")
    if len(metadata.get("description", "")) < 80:
        errors.append(f"{skill_file.relative_to(ROOT)}: description is too short")

    reference_dir = directory / "references"
    found = {path.name for path in reference_dir.glob("*.md")}
    missing = REQUIRED_REFERENCES - found
    if missing:
        errors.append(
            f"{reference_dir.relative_to(ROOT)}: missing {', '.join(sorted(missing))}"
        )
    return errors


def validate_relative_links() -> list[str]:
    errors: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in MARKDOWN_LINK.finditer(line):
                target = match.group(1)
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith(("#", "mailto:")):
                    continue
                relative_path = unquote(parsed.path)
                if not relative_path:
                    continue
                destination = (markdown.parent / relative_path).resolve()
                try:
                    destination.relative_to(ROOT)
                except ValueError:
                    errors.append(
                        f"{markdown.relative_to(ROOT)}:{line_number}: "
                        f"link escapes repository: {target}"
                    )
                    continue
                if not destination.exists():
                    errors.append(
                        f"{markdown.relative_to(ROOT)}:{line_number}: "
                        f"missing link target: {target}"
                    )
    return errors


def main() -> int:
    errors: list[str] = []
    for filename in sorted(REQUIRED_ROOT_FILES):
        if not (ROOT / filename).is_file():
            errors.append(f"{filename}: required repository file is missing")
    for language, directory in SKILLS.items():
        errors.extend(validate_skill(language, directory))
    if SKILLS["en"].resolve() == SKILLS["ko"].resolve():
        errors.append("English and Korean skills must be separate packages")
    errors.extend(validate_relative_links())

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validated 2 independent skill packages and all relative Markdown links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
