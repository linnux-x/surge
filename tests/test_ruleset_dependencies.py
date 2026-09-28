"""Keep incremental rebuild triggers separate from Global pruning policy."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import check_upstream_updates as checker
import generate_rules as generator
from sources import (ALL_RULESETS, GLOBAL_OVERLAP_RULESETS, GLOBAL_REBUILD_ONLY_RULESETS,
                     OVERLAP_DEPENDENTS, SOURCE_URL_MAP, expand_ruleset_dependencies)

FIXTURE = json.loads((Path(__file__).parent / 'fixtures/cidr-baseline.json').read_text())
ROOT = Path(__file__).resolve().parents[1]


class DependencyTests(unittest.TestCase):
    def test_all_selections_match_pre_refactor_trigger_set(self):
        triggers = set(FIXTURE['overlap_dependents'])
        self.assertEqual(OVERLAP_DEPENDENTS, triggers)
        self.assertEqual(set(GLOBAL_OVERLAP_RULESETS), triggers - {'Apple_CN.list'})
        self.assertEqual(GLOBAL_REBUILD_ONLY_RULESETS, {'Apple_CN.list'})
        for name in ALL_RULESETS:
            selected = [name]
            expected = {name, 'Global.list'} if name in triggers else {name}
            with self.subTest(name=name):
                self.assertEqual(expand_ruleset_dependencies(selected), expected)
                self.assertEqual(selected, [name])
                self.assertEqual(expand_ruleset_dependencies(expected), expected)
        self.assertEqual(expand_ruleset_dependencies([]), set())

    def test_checker_and_generator_selection_agree_for_every_source(self):
        info = {'source_available': True, 'etag': 'new'}
        for url, targets in SOURCE_URL_MAP.items():
            with self.subTest(url=url), patch.object(checker, 'fetch_upstream_info', return_value=info), contextlib.redirect_stderr(io.StringIO()):
                changed, state, count, unknown = checker.check_all_sources_parallel([url], {})
                self.assertEqual(changed, expand_ruleset_dependencies(targets))
                self.assertEqual((state, count, unknown), ({url: info}, 1, 0))

    def test_pruning_sources_precede_global_in_public_config(self):
        text = (ROOT / 'Conf/Linnux.conf').read_text()
        lines = [line for line in text.splitlines() if line.startswith('RULE-SET,')]
        position = {}
        for index, line in enumerate(lines):
            position[line.split(',')[1].rsplit('/', 1)[-1]] = index
        for name in GLOBAL_OVERLAP_RULESETS:
            with self.subTest(name=name):
                self.assertLess(position[name], position['Global.list'])

    def test_apple_cn_still_triggers_rebuild_without_pruning_global(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'Apple_CN.list').write_text('DOMAIN,retained.example\n')
            (root / 'AI.list').write_text('DOMAIN,removed.example\n')
            path = root / 'Global.list'
            path.write_text('# TOTAL: 2\nDOMAIN,retained.example\nDOMAIN,removed.example\n')
            with patch.object(generator, 'RULE_DIR', root):
                generator.prune_global_first_match_overlaps()
            self.assertEqual(path.read_text(), '# TOTAL: 1\nDOMAIN,retained.example\n')
            self.assertEqual(expand_ruleset_dependencies(['Apple_CN.list']), {'Apple_CN.list', 'Global.list'})
