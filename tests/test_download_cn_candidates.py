"""Tests for the review-only mainland-download candidate auditor."""

from __future__ import annotations

import csv
import importlib.util
import ipaddress
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "download_cn_candidates.py"


def load_module():
    spec = importlib.util.spec_from_file_location("download_cn_candidates", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class FakeRouting:
    @staticmethod
    def simulate_routing(host, _order, _rulesets):
        if host in {"cn-download.example", "blob.core.windows.net", "foreign-download.example"}:
            return "Download.list→Download"
        return "China.list→DIRECT"


class DownloadCandidateTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()
        self.networks = [ipaddress.ip_network("1.0.1.0/24")]

    def test_csv_rows_are_normalized_and_aggregated(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "traffic.csv"
            with source.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["Host", "RequestCount", "Upload", "Download"])
                writer.writerow(["CN-Download.Example.", "2", "10", "100"])
                writer.writerow(["cn-download.example", "3", "20", "200"])
                writer.writerow(["192.168.1.3", "9", "0", "0"])
            rows = self.module.parse_traffic_csv(source)

        self.assertEqual(rows, [self.module.TrafficRow("cn-download.example", 5, 30, 300)])

    def test_cn_ip_signal_stays_review_only(self):
        rows = [self.module.TrafficRow("cn-download.example", 2, 10, 100)]
        candidates = self.module.build_candidates(
            rows, FakeRouting, [], {}, self.networks, True,
            resolver=lambda _host: ["1.0.1.8"],
        )

        self.assertEqual(len(candidates), 1)
        candidate = candidates[0]
        self.assertEqual(candidate.cn_ip_signal, "ALL_CN_IP")
        self.assertEqual(candidate.disposition, "REVIEW_REQUIRED")
        self.assertEqual(candidate.proposed_rule, "DOMAIN,cn-download.example")
        self.assertIn("仍需官方", candidate.reason)

    def test_shared_cloud_host_is_never_a_direct_candidate(self):
        rows = [self.module.TrafficRow("blob.core.windows.net", 2, 10, 100)]
        candidate = self.module.build_candidates(
            rows, FakeRouting, [], {}, self.networks, True,
            resolver=lambda _host: ["1.0.1.8"],
        )[0]

        self.assertEqual(candidate.disposition, "REJECT_SHARED_INFRA")
        self.assertIsNone(candidate.proposed_rule)

    def test_non_cn_ip_is_rejected_and_non_download_is_ignored(self):
        rows = [
            self.module.TrafficRow("foreign-download.example", 1, 0, 50),
            self.module.TrafficRow("ordinary.example", 1, 0, 500),
        ]
        candidates = self.module.build_candidates(
            rows, FakeRouting, [], {}, self.networks, True,
            resolver=lambda _host: ["8.8.8.8"],
        )

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].host, "foreign-download.example")
        self.assertEqual(candidates[0].disposition, "REJECT_NON_CN_IP")
        self.assertIsNone(candidates[0].proposed_rule)

    def test_fake_ip_is_not_treated_as_non_cn_evidence(self):
        rows = [self.module.TrafficRow("cn-download.example", 1, 0, 50)]
        candidate = self.module.build_candidates(
            rows, FakeRouting, [], {}, self.networks, True,
            resolver=lambda _host: ["198.18.24.238", "192.168.1.1"],
        )[0]

        self.assertEqual(candidate.resolved_ips, [])
        self.assertEqual(candidate.cn_ip_signal, "UNRESOLVED")
        self.assertEqual(candidate.disposition, "REVIEW_REQUIRED")
        self.assertIn("DNS 无结果", candidate.reason)

    def test_rule_paths_and_list_outputs_are_refused(self):
        with self.assertRaises(ValueError):
            self.module.validate_output_path(ROOT / "Rule" / "Download_CN.list")
        with self.assertRaises(ValueError):
            self.module.validate_output_path(Path("/tmp/candidates.list"))


if __name__ == "__main__":
    unittest.main()
