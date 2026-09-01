"""Regression tests for SukkaW watermark filtering and validation."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from generate_rules import apply_project_guardrails
from rule_validator import validate_rule_file


MARKERS = (
    "DOMAIN,7h15_ru1353t_1s_m4d3_by_5ukk4w.skk.moe",
    "DOMAIN,7h15.ru1353t.1s.m4d3.by.5ukk4w.skk.moe",
)


class SukkaWWatermarkTests(unittest.TestCase):
    def test_generator_removes_separator_variants(self):
        rules = ["DOMAIN,example.com", *MARKERS]
        self.assertEqual(
            apply_project_guardrails("AI.list", rules),
            ["DOMAIN,example.com"],
        )

    def test_validator_rejects_separator_variants(self):
        for marker in MARKERS:
            with self.subTest(marker=marker):
                errors = validate_rule_file([marker], "AI.list")
                self.assertTrue(any("SukkaW marker leaked" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
