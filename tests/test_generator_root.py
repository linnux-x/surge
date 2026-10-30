import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_rules.py"


class GeneratorRootTests(unittest.TestCase):
    def test_paths_are_anchored_to_repository(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        try:
            import generate_rules
        finally:
            sys.path.pop(0)
        self.assertEqual(generate_rules.RULE_DIR, ROOT / "Rule")
        self.assertEqual(generate_rules.MANUAL_DIR, ROOT / "Rule" / "Manual")

    def test_foreign_cwd_does_not_create_rule_tree(self):
        with tempfile.TemporaryDirectory() as cwd:
            env = {**os.environ, "CHANGED_RULESETS": "[]", "GITHUB_EVENT_NAME": ""}
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPT)], cwd=cwd, env=env,
                capture_output=True, text=True, timeout=60,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(os.listdir(cwd), [])

    def test_clash_check_is_cwd_independent(self):
        clash = ROOT / "scripts" / "generate_clash_rules.py"
        with tempfile.TemporaryDirectory() as cwd:
            result = subprocess.run(
                [sys.executable, "-B", str(clash), "--check", "--validate"],
                cwd=cwd, capture_output=True, text=True, timeout=120,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(os.listdir(cwd), [])


if __name__ == "__main__":
    unittest.main()
