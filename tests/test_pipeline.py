"""The runner fixes step order, success criteria and the read-only receipt check."""
import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import pipeline


def completed(code=0, stdout=''):
    return subprocess.CompletedProcess([], code, stdout, '')


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)
        (self.root / 'Rule' / '.sources').mkdir(parents=True)
        (self.root / 'scripts').mkdir()
        (self.root / 'Rule' / 'AI.list').write_text('DOMAIN,a.example\n')
        self.paths = patch.multiple(
            pipeline, ROOT=self.root, RULE_DIR=self.root / 'Rule',
            STATE=self.root / 'scripts' / 'source_state.json',
            NEXT_STATE=self.root / 'scripts' / 'source_state.next.json',
            RECEIPTS=(self.root / 'scripts' / 'generation_receipt.json',
                      self.root / 'scripts' / 'generation_receipt.md'))
        self.paths.start()

    def tearDown(self):
        self.paths.stop()
        self.dir.cleanup()

    def summary(self, argv, run):
        out = io.StringIO()
        with patch.object(pipeline, 'run', side_effect=run), redirect_stdout(out):
            code = pipeline.main(argv)
        return code, json.loads(out.getvalue().splitlines()[-1])

    def test_build_runs_derived_steps_in_order_only_after_a_change(self):
        calls = []

        def run(args, capture=False):
            calls.append(args[0] if args[0] != 'scripts/manifest.py' else ' '.join(args))
            if args[0] == 'scripts/generate_rules.py':
                (self.root / 'Rule' / 'AI.list').write_text('DOMAIN,b.example\n')
            return completed()
        code, summary = self.summary(['build', '--rulesets', 'AI.list'], run)
        self.assertEqual(code, 0)
        self.assertEqual(calls, ['scripts/generate_rules.py', 'scripts/manifest.py',
                                 'scripts/manifest.py --diff', 'scripts/generate_receipt.py'])
        self.assertEqual(summary['changed_files'], ['Rule/AI.list'])

    def test_unchanged_build_leaves_derived_artifacts_alone(self):
        calls = []
        code, summary = self.summary(['build', '--rulesets', 'AI.list'],
                                     lambda args, capture=False: calls.append(args[0]) or completed())
        self.assertEqual((code, summary['status'], calls), (0, 'unchanged', ['scripts/generate_rules.py']))

    def test_generation_failure_stops_before_derived_steps(self):
        calls = []
        code, summary = self.summary(['build', '--rulesets', 'AI.list'],
                                     lambda args, capture=False: calls.append(args[0]) or completed(1))
        self.assertEqual((code, summary['status'], calls), (1, 'failed', ['scripts/generate_rules.py']))

    def test_upstream_gate(self):
        def probe(summary, code=0):
            return lambda args, capture=False: completed(code, 'log\n' + json.dumps(summary))
        ok = {'status': 'changed', 'unavailable_sources': 0, 'unknown_timestamp_sources': 1, 'rulesets': ['AI.list']}
        self.assertEqual(self.summary(['upstream'], probe(ok))[0], 0)
        self.assertEqual(self.summary(['upstream', '--require-known-timestamps'], probe(ok))[0], 1)
        self.assertEqual(self.summary(['upstream'], probe({**ok, 'unavailable_sources': 1}, 1))[0], 1)
        self.assertEqual(self.summary(['upstream'], probe({**ok, 'rulesets': ['Missing.list']}))[0], 1)
        calls = []

        def unchanged(args, capture=False):
            calls.append(args[0])
            return completed(0, json.dumps({**ok, 'status': 'unchanged', 'rulesets': []}))
        code, summary = self.summary(['build', '--from-upstream'], unchanged)
        self.assertEqual((code, summary['status'], calls), (0, 'unchanged', ['scripts/check_upstream_updates.py']))

    def test_receipt_check_is_read_only(self):
        receipt = self.root / 'scripts' / 'generation_receipt.json'
        receipt.write_text('{"committed": true}\n')

        def regenerate(content):
            def run(args, capture=False):
                receipt.write_text(content)
                return completed()
            return run
        with patch.object(pipeline, 'run', side_effect=regenerate('{"committed": true}\n')):
            self.assertTrue(pipeline.receipt_is_current())
        with patch.object(pipeline, 'run', side_effect=regenerate('{"stale": true}\n')):
            self.assertFalse(pipeline.receipt_is_current())
        self.assertEqual(receipt.read_text(), '{"committed": true}\n')

    def test_verify_matches_ci_scope_and_reports_failures(self):
        names = [name for name, _ in pipeline.verify_checks(ci=True, online=False)]
        self.assertEqual(names, ['repository invariants', 'generation receipt', 'unit tests',
                                 'routing order', 'whitespace'])
        self.assertIn('online audit', [name for name, _ in pipeline.verify_checks(ci=False, online=True)])

        def run(args, capture=False):
            return completed(1 if args[0] == 'scripts/test_routing_order.py' else 0)
        with patch.object(pipeline, 'receipt_is_current', return_value=True), \
                patch.object(pipeline, 'git', return_value=completed()):
            code, summary = self.summary(['verify', '--ci'], run)
        self.assertEqual((code, summary['failed']), (1, ['routing order']))

    def test_promote_state(self):
        self.assertEqual(self.summary(['promote-state'], None)[1]['promoted'], False)
        pipeline.NEXT_STATE.write_text('{"https://example.test": {}}\n')
        self.assertTrue(self.summary(['promote-state'], None)[1]['promoted'])
        self.assertFalse(pipeline.NEXT_STATE.exists())
        self.assertEqual(json.loads(pipeline.STATE.read_text()), {'https://example.test': {}})
        pipeline.NEXT_STATE.write_text('{broken')
        self.assertEqual(self.summary(['promote-state'], None)[0], 1)
        self.assertTrue(pipeline.NEXT_STATE.exists())


if __name__ == '__main__':
    unittest.main()
