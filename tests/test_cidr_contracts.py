"""CIDR contracts captured before the refactor, plus an independent oracle."""
import contextlib
import io
import ipaddress
import json
from pathlib import Path
import random
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from cidr_rules import prune_cidr_lines, redundant_cidr_indices
import generate_rules as generator
from rule_validator import validate_rule_file

FIXTURE = json.loads((Path(__file__).parent / 'fixtures/cidr-baseline.json').read_text())


class CIDRContractTests(unittest.TestCase):
    def test_file_bytes_and_logs_match_pre_refactor(self):
        for case in FIXTURE['cases']:
            with self.subTest(case=case['name']), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / 'Test.list'
                path.write_text(case['input'])
                with contextlib.redirect_stdout(io.StringIO()) as log:
                    self.assertIsNone(generator.prune_redundant_cidr(path))
                self.assertEqual(path.read_bytes(), case['output'].encode())
                self.assertEqual(log.getvalue(), case['stdout'])

    def test_validation_errors_and_line_numbers_match_pre_refactor(self):
        for case in FIXTURE['cases']:
            # The empty fixture was validated as an empty list, not a blank line.
            lines = [] if case['name'] == 'empty' else case['input'].splitlines()
            with self.subTest(case=case['name']):
                self.assertEqual(validate_rule_file(lines, 'Test.list'), case['errors'])

    def test_pruning_preserves_input_and_unmodified_line_text(self):
        for case in FIXTURE['cases']:
            lines = case['input'].splitlines()
            original = lines[:]
            result, before, after = prune_cidr_lines(lines)
            self.assertEqual(lines, original)
            self.assertEqual(result, case['output'].splitlines())
            self.assertEqual(before - after, len(lines) - len(result))

    def test_no_file_rewrite_when_no_pruning_needed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'Test.list'
            path.write_bytes(b'DOMAIN,example.test')
            with patch.object(Path, 'write_text', side_effect=AssertionError('unexpected write')):
                generator.prune_redundant_cidr(path)

    def test_randomized_coverage_matches_pairwise_subnet_oracle(self):
        rng = random.Random(20260927)
        for version, bits in ((4, 32), (6, 128)):
            network_class = ipaddress.IPv4Network if version == 4 else ipaddress.IPv6Network
            entries = []
            for _ in range(150):
                parent = network_class((rng.getrandbits(bits), rng.randrange(bits)), strict=False)
                child = network_class((int(parent.network_address), rng.randint(parent.prefixlen, bits)))
                for network in (parent, child):
                    options = rng.choice([(), ('no-resolve',), ('extended-matching', 'no-resolve')])
                    entries.append((len(entries), network, options))
            expected = {index for index, network, options in entries if any(
                options == parent_options and network != parent and network.subnet_of(parent)
                for _, parent, parent_options in entries
            )}
            with self.subTest(version=version):
                self.assertEqual(redundant_cidr_indices(entries), expected)

    def test_generation_preserves_mode_and_cleans_failed_stage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / 'Test.list'
            target.write_bytes(b'previous\n')
            target.chmod(0o640)
            with patch.object(generator, 'RULE_DIR', root), patch.object(generator, 'MANUAL_DIR', root / 'Manual'), patch.object(generator, 'fetch_source', return_value=['DOMAIN,example.test']):
                generator.process_rule('Test.list', 'Test', [('Fixture', 'https://example.test', None)])
                self.assertEqual(target.stat().st_mode & 0o777, 0o640)
                previous = target.read_bytes()
                with patch.object(Path, 'replace', side_effect=OSError('injected replace failure')):
                    with self.assertRaises(OSError):
                        generator.process_rule('Test.list', 'Test', [('Fixture', 'https://example.test', None)])
            self.assertEqual(target.read_bytes(), previous)
            self.assertEqual(list(root.glob('.rules-*.tmp')), [])
