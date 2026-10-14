"""Render authored examples and check inspectable anchors, not prose quality."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- showcase:start -->"
END = "<!-- showcase:end -->"

def load_examples(root=ROOT):
    cases = json.loads((Path(root) / "examples/showcases.json").read_text(encoding="utf-8"))
    if not isinstance(cases, list) or not cases:
        raise ValueError("Showcases must be a nonempty list")
    seen = set()
    for case in cases:
        for field in ("id", "title", "task", "provenance", "before", "after"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                raise ValueError(f"Missing showcase field: {field}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case["id"]) or case["id"] in seen:
            raise ValueError(f"Invalid or duplicate showcase id: {case['id']}")
        seen.add(case["id"])
        for field in ("protected", "checks", "changes", "rules"):
            values = case.get(field)
            if not isinstance(values, list) or not values or not all(
                isinstance(value, str) and value.strip() for value in values
            ):
                raise ValueError(f"Invalid showcase {field}: {case['id']}")
        for anchor in case["protected"]:
            before_count = case["before"].count(anchor)
            if not before_count or case["after"].count(anchor) != before_count:
                raise ValueError(f"Protected anchor changed: {case['id']}: {anchor}")
        # This fixture rule protects literal quantities. It does not evaluate claims.
        numbers = lambda text: Counter(re.findall(r"(?<!\w)\d+(?:\.\d+)?(?!\w)", text))
        if numbers(case["before"]) != numbers(case["after"]):
            raise ValueError(f"Numeric anchors changed: {case['id']}")
    if cases[0]["id"] != "close-reading":
        raise ValueError("The homepage showcase must be close-reading")
    return cases

def quote(text):
    return "\n".join("> " + line if line else ">" for line in text.splitlines())

def featured(case):
    return (
        "**Before**\n\n" + quote(case["before"]) +
        "\n\n**After**\n\n" + quote(case["after"]) +
        "\n\n**What changed:** " + " ".join(case["changes"]) + "\n"
    )

def render_gallery(cases):
    output = [
        "# Worked revisions",
        "These original teaching examples expose their complete inputs. Each revision uses only the draft's factual content. The notes define the task and provenance; they add no hidden evidence.",
        "They are authored demonstrations, not independent model outputs or user-study results. Protected anchors receive mechanical checks. The editorial checks below require judgment.",
        "## Browse the examples",
        "\n".join(f"- [{c['title']}](#{c['id']})" for c in cases),
    ]
    for case in cases:
        output.extend([
            f'<a id="{case["id"]}"></a>\n\n## {case["title"]}',
            "**Task:** " + case["task"],
            "**Provenance:** " + case["provenance"],
            featured(case).rstrip(),
            "**Preservation review:**\n\n" + "\n".join("- " + item for item in case["checks"]),
            "**Rules:** " + ", ".join(case["rules"]) + ".",
        ])
    return "\n\n".join(output) + "\n"

def render_readme(current, case):
    if current.count(START) != 1 or current.count(END) != 1:
        raise ValueError("README needs exactly one showcase marker pair")
    left, rest = current.split(START)
    _, right = rest.split(END)
    return left + START + "\n" + featured(case) + END + right

def check(root=ROOT):
    root = Path(root)
    path = root / "examples/showcases.json"
    if not path.exists():
        return ["Missing showcase source"] if (root / "tests/cases.json").exists() else []
    try:
        cases = load_examples(root)
        errors = []
        gallery = root / "references/examples.md"
        if gallery.read_text(encoding="utf-8") != render_gallery(cases):
            errors.append("Showcase gallery drift: run python scripts/showcases.py --write")
        readme = root / "README.md"
        if readme.exists():
            current = readme.read_text(encoding="utf-8")
            if current != render_readme(current, cases[0]):
                errors.append("README showcase drift: run python scripts/showcases.py --write")
        return errors
    except (ValueError, KeyError, TypeError, OSError) as exc:
        return [str(exc)]

def write(root=ROOT):
    root = Path(root)
    cases = load_examples(root)
    readme = root / "README.md"
    revised = render_readme(readme.read_text(encoding="utf-8"), cases[0])
    (root / "references/examples.md").write_text(render_gallery(cases), encoding="utf-8", newline="\n")
    readme.write_text(revised, encoding="utf-8", newline="\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the gallery and README example")
    args = parser.parse_args()
    if args.write:
        write()
    errors = check()
    if errors:
        raise SystemExit("\n".join(errors))
    print("Showcase anchors and generated documents match. Semantic review remains required.")
