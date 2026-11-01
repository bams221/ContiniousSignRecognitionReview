#!/usr/bin/env python3
"""Archive a user-supplied PDF with page-labelled text and source provenance.

Usage: .venv/bin/python work/scripts/import_local_pdf.py \
  "manually_downloaded_papers/slr a deep survey.pdf" \
  --source-id manual-W3046952127 --openalex-id W3046952127 \
  --doi 10.1016/j.eswa.2020.113794
Requires pypdf. No network; existing source archives cannot be overwritten.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

import pypdf

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    parser.add_argument('--source-id', required=True)
    parser.add_argument('--openalex-id', required=True)
    parser.add_argument('--doi', required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]+', args.source_id):
        parser.error('source-id must contain only letters, digits, underscores or hyphens')
    source = args.path.resolve()
    relative = str(source.relative_to(ROOT))
    data = source.read_bytes()
    if not data.startswith(b'%PDF'):
        parser.error('Input is not a PDF')
    folder = ROOT / 'work/sources'
    folder.mkdir(exist_ok=True)
    outputs = {ext: folder / (args.source_id + ext) for ext in ('.pdf', '.txt', '.json')}
    if any(p.exists() for p in outputs.values()):
        parser.error('Source already exists; use its saved files or a new source-id')
    reader = pypdf.PdfReader(source)
    text = '\n'.join(f'\n--- PDF page {i+1} ---\n' + (page.extract_text() or '')
                     for i, page in enumerate(reader.pages))
    entry = {
        'source_id': args.source_id, 'openalex_id': args.openalex_id,
        'doi': args.doi, 'url': 'https://doi.org/' + args.doi,
        'url_role': 'Publication identifier; original download URL was not supplied',
        'acquisition': 'User-supplied local PDF', 'original_path': relative,
        'downloaded_utc': None, 'imported_utc': datetime.now(timezone.utc).isoformat(),
        'body': outputs['.pdf'].name, 'sha256': hashlib.sha256(data).hexdigest(),
        'text': outputs['.txt'].name, 'text_sha256': hashlib.sha256(text.encode()).hexdigest(),
        'pages': len(reader.pages), 'extractor': 'pypdf ' + pypdf.__version__,
    }
    outputs['.pdf'].write_bytes(data)
    outputs['.txt'].write_text(text)
    outputs['.json'].write_text(json.dumps(entry, indent=2, ensure_ascii=False) + '\n')
    print(f'Archived {args.source_id}: {len(reader.pages)} pages; no network requests.')


if __name__ == '__main__':
    main()
