"""Regression checks for packaging boundaries and malformed project fixtures."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate import RUNTIME, read_version, validate
from package import build

class ProjectToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "professor-humanizer"
        for name in (*RUNTIME, "tests/cases.json", "examples/showcases.json"):
            dest = self.root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, dest)

    def test_missing_runtime_reference_blocks_release(self):
        (self.root / "references/rules.md").unlink()
        self.assertTrue(validate(self.root))
        with self.assertRaises(ValueError):
            build(self.root)

    def test_missing_document_link_blocks_release(self):
        with (self.root / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write("\n[missing](references/absent.md)\n")
        self.assertTrue(any("Broken/escaping" in item for item in validate(self.root)))

    def test_duplicate_pattern_id_detected(self):
        with (self.root / "references/patterns.md").open("a", encoding="utf-8") as file:
            file.write("\n## P01 — Duplicate\n")
        self.assertTrue(any("IDs" in item for item in validate(self.root)))

    def test_escaping_local_link_detected(self):
        (self.root.parent / "outside.md").write_text("private", encoding="utf-8")
        with (self.root / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write("\n[outside](../outside.md)\n")
        self.assertTrue(any("escaping" in item for item in validate(self.root)))

    def test_unknown_case_rule_detected(self):
        path = self.root / "tests/cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        cases[0]["rules"].append("P99")
        path.write_text(json.dumps(cases), encoding="utf-8")
        self.assertTrue(any("Unknown rule" in item for item in validate(self.root)))

    def test_release_excludes_untracked_and_private_files(self):
        (self.root / ".env").write_text("PRIVATE=example", encoding="utf-8")
        (self.root / "unrelated.txt").write_text("do not ship", encoding="utf-8")
        archive, checksum = build(self.root)
        with ZipFile(archive) as bundle:
            names = set(bundle.namelist())
            self.assertEqual(names, {"professor-humanizer/" + p for p in RUNTIME})
            self.assertTrue(all(".." not in Path(n).parts for n in names))
        self.assertEqual(checksum.read_text().split()[0],
                         hashlib.sha256(archive.read_bytes()).hexdigest())

    def test_archive_reproducible(self):
        archive, _ = build(self.root)
        first = archive.read_bytes()
        archive, _ = build(self.root)
        self.assertEqual(first, archive.read_bytes())

    def test_extracted_package_self_contained(self):
        archive, _ = build(self.root)
        extracted = self.root.parent / "extracted"
        with ZipFile(archive) as bundle:
            bundle.extractall(extracted)
        self.assertEqual(validate(extracted / "professor-humanizer"), [])

    def test_version_controls_archive_name(self):
        path = self.root / "SKILL.md"
        current_version = read_version(self.root)
        text = path.read_text(encoding="utf-8").replace(f'version: "{current_version}"', 'version: "9.8.7"')
        path.write_text(text, encoding="utf-8")
        archive, _ = build(self.root)
        self.assertEqual(archive.name, "professor-humanizer-v9.8.7.zip")

    def test_invalid_version_blocks_archive(self):
        path = self.root / "SKILL.md"
        current_version = read_version(self.root)
        path.write_text(path.read_text(encoding="utf-8").replace(f'version: "{current_version}"', 'version: "../bad"'), encoding="utf-8")
        with self.assertRaises(ValueError):
            build(self.root)

if __name__ == "__main__":
    unittest.main()
