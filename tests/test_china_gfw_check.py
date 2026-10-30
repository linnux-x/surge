import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import audit_rules  # noqa: E402


class ChinaGfwCheckTests(unittest.TestCase):
    def test_parse_domain_set_strips_suffix_marker_and_comments(self):
        parsed = audit_rules.parse_domain_set("# c\n.example.com\nhost.test\n\n")
        self.assertEqual(parsed, {"example.com", "host.test"})

    def test_reports_only_entries_that_still_reach_china(self):
        blocked = {"blocked.com"}
        rules = [
            "DOMAIN-SUFFIX,blocked.com",       # falls through to China → leak
            "DOMAIN,cdn.blocked.com",          # caught earlier by Global → fine
            "DOMAIN-SUFFIX,baidu.com",         # not blocked → fine
            "DOMAIN-KEYWORD,blocked",          # not a domain entry → ignored
        ]
        routes = {"blocked.com": "China.list→DIRECT", "cdn.blocked.com": "Global.list→Global",
                  "baidu.com": "China.list→DIRECT"}
        leaks = audit_rules.china_direct_blocked_entries(blocked, rules, routes.__getitem__)
        self.assertEqual(leaks, [("DOMAIN-SUFFIX,blocked.com", "blocked.com")])

    def test_subdomain_of_blocked_parent_is_reported(self):
        leaks = audit_rules.china_direct_blocked_entries(
            {"blocked.com"}, ["DOMAIN,a.b.blocked.com"], lambda _d: "China.list→DIRECT")
        self.assertEqual(leaks, [("DOMAIN,a.b.blocked.com", "blocked.com")])

    def test_check_wires_into_main(self):
        source = (ROOT / "scripts" / "audit_rules.py").read_text(encoding="utf-8")
        self.assertIn("check_china_direct_vs_gfw()", source.split("def main", 1)[1])


if __name__ == "__main__":
    unittest.main()
