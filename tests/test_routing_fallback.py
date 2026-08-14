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
        self.assertEqual(("WeChat.list", "WeChat"), parsed[0])
        self.assertEqual(("Apple_AI.list", "Apple_AI"), parsed[2])


if __name__ == "__main__":
    unittest.main()
