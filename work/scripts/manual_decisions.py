"""Load human verdicts from the dedicated CSV without changing AI assessments.

Usage: imported by report.py, html_report.py and verify.py during offline builds.
Edit only the decision column in work/manual_decisions.csv, then run report.py.
"""
import csv
import json

VERDICTS = {'include', 'exclude', 'uncertain', 'not_screened'}


def read_decisions(path, candidate_ids):
    decisions = {}
    with path.open(newline='', encoding='utf-8-sig') as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ['openalex_id', 'decision', 'title']:
            raise ValueError(f'{path}: expected header openalex_id,decision,title')
        for line, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f'{path}:{line}: expected three CSV fields; quote titles containing commas')
            wid, verdict = row['openalex_id'].strip(), row['decision'].strip()
            if wid in decisions:
                raise ValueError(f'{path}:{line}: duplicate candidate {wid}')
            if verdict not in VERDICTS:
                raise ValueError(f'{path}:{line}: invalid decision {verdict!r}; use {", ".join(sorted(VERDICTS))}')
            decisions[wid] = verdict
    missing = set(candidate_ids) - decisions.keys()
    extra = decisions.keys() - set(candidate_ids)
    if missing or extra:
        raise ValueError(f'{path}: candidate IDs differ; missing={sorted(missing)}, unknown={sorted(extra)}')
    return decisions


def load_screening(work):
    screening = json.loads((work / 'screening.json').read_text())
    records = screening['records']
    decisions = read_decisions(work / 'manual_decisions.csv', {r['openalex_id'] for r in records})
    for record in records:
        record['human_decision'] = decisions[record['openalex_id']]
    return screening
