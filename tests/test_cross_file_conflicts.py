"""Regression checks for first-match parent/child rule conflicts."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cross_file_conflicts import collect_conflicts


class CrossFileConflictTests(unittest.TestCase):
    def test_parent_suffix_shadows_later_child_exact_and_suffix(self):
        order = {"AI.list": (0, "AI"), "China.list": (1, "DIRECT")}
        index = {
            "pool.ntp.org": [("AI.list", "DOMAIN-SUFFIX", "DOMAIN-SUFFIX,pool.ntp.org")],
            "cn.pool.ntp.org": [
                ("China.list", "DOMAIN", "DOMAIN,cn.pool.ntp.org"),
                ("China.list", "DOMAIN-SUFFIX", "DOMAIN-SUFFIX,cn.pool.ntp.org"),
            ],
        }
        conflicts = collect_conflicts(order, index)
        self.assertEqual(len(conflicts), 2)
        self.assertTrue(all(item[2][0] == "AI.list" for item in conflicts))

    def test_exact_parent_does_not_shadow_child_or_entire_suffix(self):
        order = {"Global.list": (0, "Global"), "China.list": (1, "DIRECT")}
        index = {
            "example.com": [
                ("Global.list", "DOMAIN", "DOMAIN,example.com"),
                ("China.list", "DOMAIN-SUFFIX", "DOMAIN-SUFFIX,example.com"),
            ],
            "cn.example.com": [("China.list", "DOMAIN", "DOMAIN,cn.example.com")],
        }
        self.assertEqual(collect_conflicts(order, index), [])

    def test_earliest_covering_policy_controls_conflict(self):
        order = {
            "First.list": (0, "DIRECT"),
            "Second.list": (1, "Global"),
            "China.list": (2, "DIRECT"),
        }
        index = {
            "example.com": [("First.list", "DOMAIN-SUFFIX", "DOMAIN-SUFFIX,example.com")],
            "cn.example.com": [
                ("Second.list", "DOMAIN-SUFFIX", "DOMAIN-SUFFIX,cn.example.com"),
                ("China.list", "DOMAIN", "DOMAIN,cn.example.com"),
            ],
        }
        conflicts = collect_conflicts(order, index)
        self.assertEqual(len(conflicts), 1)
        self.assertEqual(conflicts[0][3][0], "Second.list")
        self.assertEqual(conflicts[0][2][0], "First.list")


if __name__ == "__main__":
    unittest.main()
