#!/usr/bin/env python3
"""Check manual-verdict input validation and independence from AI assessments.

Usage: python3 work/scripts/test_manual_decisions.py
"""
import csv
import json
from pathlib import Path
import tempfile
import unittest

from manual_decisions import load_screening, read_decisions


class ManualDecisionsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.path = self.work / 'manual_decisions.csv'

    def write(self, rows):
        with self.path.open('w', newline='') as handle:
            writer = csv.writer(handle)
            writer.writerow(['openalex_id', 'decision', 'title'])
            writer.writerows(rows)

    def test_verdict_changes_preserve_ai_and_source(self):
        original = {'records': [{'openalex_id': 'W1', 'ai_decision': 'include',
                                 'stage': 'title_abstract', 'reason': 'AI rationale'}]}
        source = self.work / 'screening.json'
        source.write_text(json.dumps(original))
        before = source.read_bytes()
        for verdict in ['exclude', 'include', 'not_screened', 'uncertain']:
            self.write([['W1', verdict, 'A title, with commas']])
            result = load_screening(self.work)['records'][0]
            self.assertEqual(result, {**original['records'][0], 'human_decision': verdict})
            self.assertEqual(source.read_bytes(), before)

    def test_invalid_verdict(self):
        self.write([['W1', 'included', 'Paper']])
        with self.assertRaisesRegex(ValueError, 'invalid decision'):
            read_decisions(self.path, {'W1'})

    def test_duplicate_id(self):
        self.write([['W1', 'include', 'Paper'], ['W1', 'exclude', 'Paper']])
        with self.assertRaisesRegex(ValueError, 'duplicate candidate'):
            read_decisions(self.path, {'W1'})

    def test_missing_or_unknown_id(self):
        self.write([['W2', 'include', 'Paper']])
        with self.assertRaisesRegex(ValueError, 'candidate IDs differ'):
            read_decisions(self.path, {'W1'})

    def test_malformed_csv(self):
        self.path.write_text('openalex_id,decision,title\nW1,include,Unquoted, comma\n')
        with self.assertRaisesRegex(ValueError, 'expected three CSV fields'):
            read_decisions(self.path, {'W1'})


if __name__ == '__main__':
    unittest.main()
