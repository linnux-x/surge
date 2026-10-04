"""Probe fallback contract and response lifetime, without network access."""
import io
from pathlib import Path
import sys
import unittest
import urllib.error
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import check_upstream_updates as checker


class Response(io.BytesIO):
    def __init__(self, body=b'payload'):
        super().__init__(body)
        self.headers = {'ETag': 'version', 'Last-Modified': 'date', 'Content-Length': '1'}
        self.reads = 0

    def read(self, *args):
        self.reads += 1
        return super().read(*args)


class UpstreamProbeTests(unittest.TestCase):
    def test_fallback_order_headers_body_and_closure(self):
        for failures in range(3):
            with self.subTest(failures=failures):
                response = Response()
                errors = [urllib.error.URLError('unavailable') for _ in range(failures)]
                with patch.object(checker.urllib.request, 'urlopen', side_effect=errors + [response]) as fetch:
                    result = checker.fetch_upstream_info('https://example.test/rules')
                self.assertEqual(result, {'etag': 'version', 'last_modified': 'date', 'content_length': '7' if failures == 2 else '1', 'source_available': True})
                self.assertEqual([c.args[0].method for c in fetch.call_args_list], ['HEAD', 'GET', 'GET'][:failures+1])
                for index, call in enumerate(fetch.call_args_list):
                    self.assertEqual(call.args[0].get_header('Range'), 'bytes=0-0' if index == 1 else None)
                    self.assertEqual(call.kwargs['timeout'], checker.REQUEST_TIMEOUT)
                    self.assertEqual(call.args[0].get_header('User-agent'), checker.REQUEST_HEADERS['User-Agent'])
                self.assertEqual(response.reads, int(failures == 2))
                self.assertTrue(response.closed)

    def test_http_errors_are_closed_and_outage_result_preserved(self):
        bodies = [Response() for _ in range(3)]
        errors = [urllib.error.HTTPError('https://example.test', 403, 'blocked', {}, body) for body in bodies]
        with patch.object(checker.urllib.request, 'urlopen', side_effect=errors):
            result = checker.fetch_upstream_info('https://example.test/rules')
        self.assertEqual(result, {'etag': None, 'last_modified': None, 'content_length': None, 'source_available': False})
        self.assertTrue(all(body.closed for body in bodies))

    def test_full_read_failure_closes_response(self):
        response = Response()
        with patch.object(response, 'read', side_effect=OSError('read failed')), patch.object(checker.urllib.request, 'urlopen', side_effect=[OSError(), OSError(), response]):
            self.assertFalse(checker.fetch_upstream_info('https://example.test/rules')['source_available'])
        self.assertTrue(response.closed)

    def test_unavailable_fails_without_promoting_any_state(self):
        import argparse, contextlib, json
        url = 'https://example.test/rules'
        for option in ('write', 'candidate'):
            with self.subTest(option=option):
                output = io.StringIO()
                args = argparse.Namespace(write_state=option == 'write', state_out=Path('candidate.json') if option == 'candidate' else None, github_output=None)
                with patch.object(checker, 'parse_args', return_value=args), patch.object(checker, 'SOURCE_URL_MAP', {url: ['AI.list']}), patch.object(checker, 'load_state', return_value={url: {'source_available': True, 'etag': 'old'}}), patch.object(checker, 'fetch_upstream_info', return_value={'source_available': False}), patch.object(checker, 'save_state') as save, contextlib.redirect_stdout(output), contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as exc: checker.main()
                self.assertEqual(exc.exception.code, 1)
                save.assert_not_called()
                summary = json.loads(output.getvalue())
                self.assertEqual(summary['status'], 'failed')
                self.assertEqual(summary['unavailable_sources'], 1)
                self.assertEqual(summary['unknown_timestamp_sources'], 0)

    def test_available_without_version_is_changed_not_unavailable(self):
        import contextlib
        url = 'https://example.test/rules'
        with patch.object(checker, 'SOURCE_URL_MAP', {url: ['AI.list']}), patch.object(checker, 'fetch_upstream_info', return_value={'source_available': True}), contextlib.redirect_stderr(io.StringIO()):
            changed, state, count, unknown = checker.check_all_sources_parallel([url], {})
        self.assertEqual((count, unknown), (1, 1))
        self.assertIn('AI.list', changed)
        self.assertTrue(state[url]['source_available'])
