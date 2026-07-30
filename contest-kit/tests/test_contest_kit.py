from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ContestKitTests(unittest.TestCase):
    def test_phase_budget_is_exact(self) -> None:
        profile = json.loads((ROOT / "contest_profile.json").read_text(encoding="utf-8"))
        self.assertEqual(225, profile["duration_minutes"])
        self.assertEqual(225, sum(phase["minutes"] for phase in profile["phases"]))
        self.assertEqual(3, profile["post_submission_question_minutes"])
        self.assertFalse(profile["extension_assumed"])
        self.assertEqual(1, profile["max_active_heavy_workers"])
        self.assertLessEqual(
            profile["bundle_ready_minute"],
            profile["duration_minutes"] - 10,
        )

    def test_required_templates_exist(self) -> None:
        expected = {
            "problem.md",
            "data-audit.md",
            "experiment.md",
            "decision.md",
            "risk-register.md",
            "debate-card.md",
        }
        observed = {path.name for path in (ROOT / "templates").glob("*.md")}
        self.assertTrue(expected.issubset(observed))

    def test_work_initialization_is_idempotent_and_preserves_edits(self) -> None:
        initializer = load_script("init_work")
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "work"
            initializer.initialize(output)
            problem = output / "problem.md"
            problem.write_text("human decision\n", encoding="utf-8")
            initializer.initialize(output)
            self.assertEqual("human decision\n", problem.read_text(encoding="utf-8"))
            self.assertTrue((output / "data-audit.md").is_file())
            self.assertTrue((output / "run-receipt.json").is_file())
            self.assertTrue((output / "champion").is_dir())
            self.assertTrue((output / "experiments.jsonl").is_file())

    def test_deterministic_bundle(self) -> None:
        builder = load_script("build_bundle")
        with tempfile.TemporaryDirectory() as temp:
            first = Path(temp) / "first.zip"
            second = Path(temp) / "second.zip"
            old_argv = list(__import__("sys").argv)
            try:
                __import__("sys").argv = ["build_bundle.py", "--output", str(first)]
                self.assertEqual(0, builder.main())
                __import__("sys").argv = ["build_bundle.py", "--output", str(second)]
                self.assertEqual(0, builder.main())
            finally:
                __import__("sys").argv = old_argv
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as archive:
                names = archive.namelist()
            self.assertFalse(any(".env" in name or ".venv" in name for name in names))


if __name__ == "__main__":
    unittest.main()
