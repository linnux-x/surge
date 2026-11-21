"""Regression tests for routing-order fallback consistency."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "test_routing_order.py"


def load_routing_module():
    spec = importlib.util.spec_from_file_location("routing_order", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FallbackOrderTests(unittest.TestCase):
    def test_fallback_order_matches_public_config(self):
        module = load_routing_module()
        parsed = module.load_routing_order()
        self.assertEqual(module.FALLBACK_ORDER, parsed)

    def test_parser_excludes_rule_options_from_policy(self):
        module = load_routing_module()
        parsed = module.load_routing_order()
        self.assertEqual(("AdBlock.list", "REJECT"), parsed[0])  # pre-matching is an option, not a policy
        self.assertEqual(("WeChat.list", "WeChat"), parsed[1])
        self.assertEqual(("Speedtest_China.list", "DIRECT"), parsed[2])
        self.assertEqual(("Apple_AI.list", "Apple_AI"), parsed[4])
        self.assertEqual(("AppleMedia.list", "GlobalMedia"), parsed[5])
        self.assertEqual(("Claude.list", "Claude"), parsed[10])
        self.assertEqual(("AI.list", "AI"), parsed[11])

    def test_apple_rules_do_not_route_by_unscoped_request_metadata(self):
        module = load_routing_module()
        for name in ("Apple.list", "AppleMedia.list"):
            with self.subTest(ruleset=name):
                rules = module.load_ruleset(module.RULE_DIR / name)
                broad_rules = sorted(rule for rule in rules if rule.startswith((
                    "domain-keyword,", "user-agent,", "process-name,",
                )))
                self.assertEqual(broad_rules, [])

        global_media = module.load_ruleset(module.RULE_DIR / "GlobalMedia.list")
        broad_apple_tv_rules = {"user-agent,appletv*", "user-agent,com.apple.tv*", "process-name,tv"}
        self.assertEqual(broad_apple_tv_rules & global_media, set())

    def test_ai_keeps_claude_standalone_compatibility_without_the_gemini_redirect(self):
        module = load_routing_module()
        ai_rules = module.load_ruleset(module.RULE_DIR / "AI.list")
        for hostname in ("probe.livepreview.claude.app", "claude.site", "claude.new", "claude.dev"):
            with self.subTest(hostname=hostname):
                self.assertTrue(module.match_domain(hostname, ai_rules))
        self.assertFalse(any(rule.startswith("url-regex,") and "continue=" in rule
                             for rule in ai_rules))


if __name__ == "__main__":
    unittest.main()
