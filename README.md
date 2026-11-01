# CSLR review search and screening

**[Open the project report →](html-report/index.html)**

The report presents exact saved retrieval filters, M1–M3, and all 33 active candidates. AI screening decisions are proposals. Each AI verdict links to a concise paper report, with detailed evidence in linked JSON.

Active runs and query IDs are selected in `work/analysis_config.json`. The 1 November 2026 revision retains q11–q13, q21–q23 and s1; it removes empty s2, redundant q1r/q2r, and the DOI-only Ibrahim candidate whose OpenAlex date is before 2020. Original runs remain immutable; the removed assessment, date-conflict evidence and previous configuration are preserved in `work/archive/2026-11-01-selection-revision.json`. The query configuration files describe the historical executions; rebuilding applies the active selection without rerunning searches.

Rebuild and verify offline with Python 3.10 or newer (standard library):

```sh
python3 work/scripts/report.py
python3 work/scripts/verify.py
python3 work/scripts/test_screening_report.py
python3 work/scripts/test_manual_decisions.py
```

`work/screening.json` is the source of AI proposals and assessment histories; `work/manual_decisions.csv` stores current manual verdicts. Report generation combines them in the HTML, data snapshot and screening CSV. Paper descriptions, verdict explanations, and evidence files under `html-report/support/` are generated from those records. Each Markdown report contains only a short description and verdict explanation, capped at 150 words including the heading. Source URLs, passages, locators, access limitations, and assessment provenance remain in structured data.

## Recording a manual screening decision

1. Open [work/manual_decisions.csv](work/manual_decisions.csv) and find the paper by title or OpenAlex ID.
2. Change only its `decision` value to `include` or `exclude`. Use `uncertain` for an unresolved decision, or `not_screened` to reset it. For example, this line marks the paper as included:

   ```csv
   W4408859567,include,Deep Learning Approaches for Continuous Sign Language Recognition: A Comprehensive Review
   ```

3. Regenerate the report:

   ```sh
   python3 work/scripts/report.py
   ```

Refresh `html-report/index.html` to see the updated **Manual screening decision**. This CSV is the source of manual verdicts; leave IDs, titles and existing CSV quotes unchanged. AI decisions remain separate. Regeneration updates the report date automatically when this file changes, so no other file needs editing. To check the result, run `python3 work/scripts/verify.py`.

Saved raw search runs are immutable. Screening uses saved abstracts and available full texts; targeted source acquisition adds no discovery candidates. New source responses and retrieval metadata are archived under `work/sources/`. Optional PDF extraction uses `pypdf` in the project virtual environment:

```sh
.venv/bin/python work/scripts/fetch_sources.py --input work/assessment_batches/batch0-sources.json --source-id SOURCE_ID
```

Use a selected source ID to avoid retrying unrelated failed requests. Update `work/analysis_config.json` with the report generation time for a new reporting edition; generation itself is deterministic and offline.

For a manually downloaded PDF, archive the original bytes, page-labelled text and provenance before screening:

```sh
.venv/bin/python work/scripts/import_local_pdf.py "manually_downloaded_papers/slr a deep survey.pdf" --source-id manual-W3046952127 --openalex-id W3046952127 --doi 10.1016/j.eswa.2020.113794
```

This import requires `pypdf` and refuses to overwrite existing source archives. Once imported, reuse the saved files. A user-supplied PDF does not count as a manual screening decision.

Serve the report locally by opening the HTML file, or package it with nginx:

```sh
docker build -t cslr-report html-report
docker run --rm -p 8080:80 cslr-report
```

The Docker image includes all generated paper reports and evidence JSON. Markdown reports are served as readable plain text.
