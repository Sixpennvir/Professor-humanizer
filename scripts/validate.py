"""Validate repository structure and reference integrity; never grade prose."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = (
    "SKILL.md", "LICENSE", "agents/openai.yaml",
    "references/rules.md", "references/patterns.md",
    "references/course-profile.md", "references/examples.md",
    "references/evidence.md", "references/traceability.md",
)

def validate(root=ROOT):
    root = Path(root).resolve()
    errors = []
    for name in RUNTIME:
        path = root / name
        if not path.is_file():
            errors.append(f"Missing runtime file: {name}")
        elif path.is_symlink() or not path.resolve().is_relative_to(root):
            errors.append(f"Unsafe runtime path: {name}")
    if errors:
        return errors
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        errors.append("Missing YAML frontmatter")
    else:
        parts = skill.split("---", 2)
        if len(parts) != 3:
            errors.append("Unclosed YAML frontmatter")
        else:
            meta = parts[1]
            if not re.search(r"(?m)^name: better-ai-writer$", meta):
                errors.append("Wrong skill name")
            desc = re.search(r"(?m)^description: (.+)$", meta)
            if not desc or not 1 <= len(desc[1]) <= 1024:
                errors.append("Description must contain 1–1024 characters")
            if not re.search(r'(?m)^  version: "0\.1\.0"$', meta):
                errors.append("Version does not match package version")
    if len(skill.splitlines()) > 500:
        errors.append("Entrypoint exceeds 500 lines")
    ui = (root / "agents/openai.yaml").read_text(encoding="utf-8")
    short = re.search(r'short_description: "([^"]+)"', ui)
    if not short or not 25 <= len(short[1]) <= 64:
        errors.append("UI description length outside 25–64 characters")
    if "$better-ai-writer" not in ui:
        errors.append("UI prompt lacks skill invocation")
    for filename, prefix, count in [
        ("rules.md", "R", 16), ("patterns.md", "P", 22),
        ("course-profile.md", "C", 14),
    ]:
        source = (root / "references" / filename).read_text(encoding="utf-8")
        ids = re.findall(r"(?m)^## (" + prefix + r"\d{2}) — ", source)
        expected = [f"{prefix}{n:02}" for n in range(1, count + 1)]
        if ids != expected:
            errors.append(f"Missing, duplicate, or unordered IDs: {filename}")
    for path in root.rglob("*.md"):
        if any(part in {".git", "dist", "__pycache__", ".venv"} for part in path.relative_to(root).parts):
            continue
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            dest = (path.parent / target).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f"Broken/escaping local link: {path.relative_to(root)} -> {target}")
    case_path = root / "tests/cases.json"
    if case_path.exists():
        try:
            cases = json.loads(case_path.read_text(encoding="utf-8"))
            seen = set()
            for case in cases:
                if case["id"] in seen:
                    errors.append(f"Duplicate case: {case['id']}")
                seen.add(case["id"])
                for key in ("input", "expect", "rules"):
                    if not case.get(key):
                        errors.append(f"Missing {key}: {case['id']}")
                for rule in case["rules"]:
                    match = re.fullmatch(r"([RPC])(\d{2})", rule)
                    limits = {"R": 16, "P": 22, "C": 14}
                    if not match or not 1 <= int(match[2]) <= limits[match[1]]:
                        errors.append(f"Unknown rule {rule}: {case['id']}")
        except (ValueError, TypeError, KeyError) as exc:
            errors.append(f"Invalid cases: {exc}")
    return errors

if __name__ == "__main__":
    issues = validate()
    for issue in issues:
        print("ERROR:", issue)
    if issues:
        sys.exit(1)
    print("Structural validation passed. Prose behavior requires separate evaluation.")
