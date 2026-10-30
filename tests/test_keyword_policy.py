import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import policy  # noqa: E402
import rule_validator  # noqa: E402
import validate_override_manifest  # noqa: E402


class KeywordPolicyTests(unittest.TestCase):
    def test_single_source_of_truth(self):
        self.assertIs(rule_validator.RISKY_DOMAIN_KEYWORDS, policy.RISKY_DOMAIN_KEYWORDS)
        self.assertFalse(hasattr(validate_override_manifest, "RISKY_DOMAIN_KEYWORDS"))

    def test_brand_generic_and_short_keywords_are_risky(self):
        for keyword in ("apple", "Google", "siri", "gmail", "1drv", "qiyi", "x"):
            self.assertTrue(policy.is_risky_domain_keyword(keyword), keyword)

    def test_reviewed_short_and_specific_keywords_pass(self):
        for keyword in ("porn", "avtb", "youtube", "telegram", "epicgames"):
            self.assertFalse(policy.is_risky_domain_keyword(keyword), keyword)

    def test_validator_warns_on_short_keyword(self):
        warnings = rule_validator.warn_rule_file(["DOMAIN-KEYWORD,siri"], "Apple_AI.list")
        self.assertEqual(len(warnings), 1)
        self.assertEqual(rule_validator.warn_rule_file(["DOMAIN-KEYWORD,youtube"], "YouTube.list"), [])


if __name__ == "__main__":
    unittest.main()
