"""Repository & Zero-Leak Privacy Shield validator for AGQuota-Swarm."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FORBIDDEN_PATTERNS = [
    (r"C:\\Users\\[A-Za-z0-9_.-]+", "Hardcoded Windows user path"),
    (r"D:\\AI-Tools", "Hardcoded local D:\\AI-Tools path"),
    (r"/Users/[A-Za-z0-9_.-]+", "Hardcoded macOS user path"),
    (r"/home/[A-Za-z0-9_.-]+", "Hardcoded Linux user path"),
    (r"\bvirtuoso\b", "Legacy personal brand reference"),
    (r"\bsk-[A-Za-z0-9]{20,}", "Potential OpenAI/Anthropic API key"),
    (r"\bAIza[0-9A-Za-z_-]{35}", "Potential Google API key"),
    (r"\bghp_[A-Za-z0-9]{36}", "Potential GitHub PAT"),
]


def validate_skill_frontmatter(skill_path: Path) -> list[str]:
    """Ensure SKILL.md has valid YAML frontmatter with name and description."""
    errors: list[str] = []
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return [f"{skill_path.name}: Missing YAML frontmatter block"]

    frontmatter = match.group(1)
    if not re.search(r"^name:\s*agquota-swarm\s*$", frontmatter, re.MULTILINE):
        errors.append(f"{skill_path.name}: Frontmatter missing 'name: agquota-swarm'")
    if not re.search(r"^description:\s*.+$", frontmatter, re.MULTILINE):
        errors.append(f"{skill_path.name}: Frontmatter missing 'description'")
    return errors


def scan_for_leaks(repo_root: Path) -> list[str]:
    """Scan all text files in the repository for personal paths or secret patterns."""
    errors: list[str] = []
    self_path = Path(__file__).resolve()

    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.resolve() == self_path:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        rel = path.relative_to(repo_root)
        for pattern, label in FORBIDDEN_PATTERNS:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                errors.append(f"{rel}: {label} matched '{m.group(0)}'")
    return errors


def main() -> int:
    errors: list[str] = []
    skill_path = REPO_ROOT / "SKILL.md"
    if not skill_path.exists():
        errors.append("Missing root SKILL.md")
    else:
        errors.extend(validate_skill_frontmatter(skill_path))

    errors.extend(scan_for_leaks(REPO_ROOT))

    if errors:
        print("VALIDATION FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("ALL CHECKS PASSED: SKILL.md manifest valid & zero privacy/secret leaks found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
