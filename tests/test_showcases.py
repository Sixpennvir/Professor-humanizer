"""Fault-injection tests for examples; these do not judge the writing."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from showcases import START, END, check, load_examples, render_readme, write

class ShowcaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "examples").mkdir()
        (self.root / "references").mkdir()
        shutil.copyfile(ROOT / "examples/showcases.json", self.root / "examples/showcases.json")
        self.readme = self.root / "README.md"
        self.readme.write_text("# Keep this title\n\n" + START + "\n" + END + "\n\nKeep this footer.\n", encoding="utf-8")
        write(self.root)

    def change(self, mutate):
        path = self.root / "examples/showcases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        mutate(cases)
        path.write_text(json.dumps(cases, ensure_ascii=False), encoding="utf-8")

    def test_numeric_change_detected(self):
        self.change(lambda cases: cases[1].update(after=cases[1]["after"].replace("18", "19")))
        self.assertTrue(check(self.root))

    def test_exact_quotation_change_detected(self):
        self.change(lambda cases: cases[0].update(after=cases[0]["after"].replace("remember the room exactly", "recall the room exactly")))
        self.assertTrue(any("anchor" in error for error in check(self.root)))

    def test_added_quantity_detected_even_without_explicit_anchor(self):
        self.change(lambda cases: cases[-1].update(after=cases[-1]["after"] + " Bring 2 copies."))
        self.assertTrue(any("Numeric" in error for error in check(self.root)))

    def test_readme_drift_detected(self):
        self.readme.write_text(self.readme.read_text(encoding="utf-8").replace("The narrator qualifies", "The author qualifies"), encoding="utf-8")
        self.assertTrue(any("README" in error for error in check(self.root)))

    def test_gallery_drift_detected(self):
        gallery = self.root / "references/examples.md"
        gallery.write_text(gallery.read_text(encoding="utf-8") + "\nUntracked edit.\n", encoding="utf-8")
        self.assertTrue(any("gallery" in error for error in check(self.root)))

    def test_render_preserves_surrounding_readme(self):
        text = self.readme.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Keep this title\n\n"))
        self.assertTrue(text.endswith("\n\nKeep this footer.\n"))
        self.assertEqual(check(self.root), [])

    def test_duplicate_markers_rejected(self):
        self.readme.write_text(self.readme.read_text(encoding="utf-8") + START, encoding="utf-8")
        self.assertTrue(any("marker" in error for error in check(self.root)))

    def test_numeric_only_guard_does_not_claim_semantic_validation(self):
        # All literal anchors survive even though the interpretation changes.
        self.change(lambda cases: cases[0].update(after=cases[0]["after"].replace(
            "leaves the memory's accuracy unresolved", "establishes the memory's accuracy"
        )))
        changed = load_examples(self.root)[0]["after"]
        self.assertIn("establishes the memory's accuracy", changed)
        write(self.root)
        self.assertEqual(check(self.root), [])
        # This passing structural check must still fail human semantic review.

    def test_generation_repeatable(self):
        before = self.readme.read_bytes()
        write(self.root)
        self.assertEqual(self.readme.read_bytes(), before)

if __name__ == "__main__":
    unittest.main()
