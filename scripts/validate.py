"""Validate repository structure and reference integrity; never grade prose."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote
from showcases import check as check_showcases

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = (
    "SKILL.md", "LICENSE", "agents/openai.yaml",
    "references/rules.md", "references/patterns.md",
    "references/course-profile.md", "references/examples.md",
    "references/evidence.md", "references/traceability.md",
    "references/workflow.md", "references/long-form-example.md",
)

def read_version(root=ROOT):
    text = (Path(root) / "SKILL.md").read_text(encoding="utf-8")
    parts = text.split("---", 2)
    match = re.search(r'(?m)^  version: "(\d+\.\d+\.\d+)"$', parts[1]) if len(parts) == 3 else None
    if not match:
        raise ValueError("Missing or invalid skill version")
    return match[1]

def valid_rule(rule):
    if not isinstance(rule, str):
        return False
    match = re.fullmatch(r"([RPC])(\d{2})", rule)
    return bool(match and 1 <= int(match[2]) <= {"R": 16, "P": 22, "C": 14}[match[1]])

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
            try:
                read_version(root)
            except ValueError as exc:
                errors.append(str(exc))
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
        if prefix == "P":
            for section in re.split(r"(?m)^## P\d{2} — ", source)[1:]:
                if "**Worked draft:**" not in section or "**Preservation check:**" not in section:
                    errors.append("Pattern lacks a worked repair or preservation check")
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
                    if not valid_rule(rule):
                        errors.append(f"Unknown rule {rule}: {case['id']}")
        except (ValueError, TypeError, KeyError) as exc:
            errors.append(f"Invalid cases: {exc}")
    errors.extend(check_showcases(root))
    showcase_source = root / "examples/showcases.json"
    if showcase_source.exists():
        try:
            for case in json.loads(showcase_source.read_text(encoding="utf-8")):
                for rule in case.get("rules", []):
                    if not valid_rule(rule):
                        errors.append(f"Unknown showcase rule: {rule}")
        except (ValueError, TypeError, AttributeError):
            pass  # The showcase checker reports malformed input.
    return errors

if __name__ == "__main__":
    issues = validate()
    for issue in issues:
        print("ERROR:", issue)
    if issues:
        sys.exit(1)
    print("Structural validation passed. Prose behavior requires separate evaluation.")
