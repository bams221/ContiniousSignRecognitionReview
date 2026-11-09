You are a senior computer vision researcher specializing in **Continuous Sign Language Recognition (CSLR)** and evidence-based literature analysis.

Analyze the attached PDF and extract information for two comparison tables:

1. **Survey characteristics** — scope, focus, methodology, and literature coverage.
2. **CSLR thematic coverage** — which topics the survey addresses and how substantively it analyzes them.

The purpose is to compare existing surveys consistently and identify defensible gaps for a future CSLR review.

## Source and evidence rules

- Use **only the attached PDF**, including its tables, figures, appendices, and supplementary material if included in the file. Do not browse or use outside knowledge to fill missing information.
- Examine the entire paper before assigning final coverage scores.
- Distinguish the survey’s own analysis from claims about individual studies it cites.
- Support every substantive extracted value and positive coverage score with a precise location and a short explanation.
- Use **1-based PDF page numbers**, where the first page of the file is page 1. Cite locations as `[PDF p. 8, §4.2, Table 3]`. Include section, table, or figure identifiers only when present.
- If printed page numbers differ from PDF page numbers, explain the difference once.
- Never invent page numbers, quotations, counts, model names, datasets, or findings.
- Use `Not reported` when information is absent, `Unclear` when evidence is ambiguous, and `Not assessable` when the relevant content cannot be inspected.
- Report extraction or readability limitations. Do not assign an absence score when incomplete access prevents verification.
- Write in English, preserving original technical names and acronyms.

## Step 1 — Establish the paper’s type and scope

Identify the title, authors, year, and publication venue when available.

Determine whether it is:

- a survey/review;
- an original research paper;
- a mixed review and experimental study.

Determine whether CSLR is a primary topic, a substantive secondary topic, mentioned only, or absent.

**Task boundaries matter:**

- Isolated sign recognition is not CSLR.
- Sign language translation (SLT) is not CSLR.
- Sign generation/production is not CSLR.
- Broad discussion of sign language recognition must not automatically be attributed to CSLR.

If the paper is not a survey, state this clearly. Still fill both tables where possible, but do not treat evaluation of the paper’s own model as comparative survey coverage.

## Step 2 — Fill Table 1: Survey characteristics

Use the following fields:

| Field                               | What to extract                                                                                                                                                                                            |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Paper ID, title, and link           | Use an author–year identifier; reproduce a DOI or URL only if it appears in the PDF.                                                                                                                       |
| Authors                             | Authors as stated in the paper.                                                                                                                                                                            |
| Publication year and venue          | Distinguish publication year from online-first dates when relevant; flag ambiguity.                                                                                                                        |
| Literature coverage period          | Years covered and search cutoff date, if reported. Do not infer these from the oldest and newest references.                                                                                               |
| Tasks and CSLR relevance            | Tasks addressed and whether CSLR is primary, substantive secondary, mentioned only, or absent.                                                                                                             |
| Main emphasis                       | One sentence describing what receives the most analytical attention.                                                                                                                                       |
| Number of included primary studies  | Report the explicit count and its scope: entire review or CSLR subset. Do not substitute bibliography length. If counting a clearly enumerated set yourself, label it as your count and explain the basis. |
| Number of previous surveys compared | Record separately from primary studies. State whether explicitly reported or counted from a specific comparison table.                                                                                     |
| Sign languages                      | Languages covered, distinguishing those relevant to CSLR when possible.                                                                                                                                    |
| Input data and modalities           | RGB, depth, skeleton/keypoints, optical flow, sensor inputs, and multimodal combinations.                                                                                                                  |
| Claimed contribution                | Summarize how the authors position the review relative to earlier surveys. Label this as an author claim, not an independently verified novelty finding.                                                   |

## Step 3 — Fill Table 2: CSLR thematic coverage

Use these fixed categories so that results remain comparable across papers:

| Category                                   | What qualifies as relevant content                                                                                                      |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Data acquisition methods                   | Discussed data acquisition methods                                                                                                      |
| CSLR challenges                            | Identified current CSLR challenges                                                                                                      |
| Manual and non-manual cues                 | Discussed hands, body, face, mouth, and their contributions to recognition.                                                             |
| Visual feature models                      | Spatial/visual feature extraction, including CNNs, 3D CNNs, vision Transformers, and related families.                                  |
| Temporal modeling                          | Modeling sequences and motion using RNNs/LSTMs, temporal convolutions, Transformers, or other approaches.                               |
| Alignment and decoding                     | Frame-to-gloss alignment, CTC, HMMs, segmentation, decoding, and related sequence recognition approaches.                               |
| Learning strategies and knowledge transfer | Explored pretraining, self-supervision, weak supervision, distillation, and cross-language or cross-domain transfer.                    |
| Data augmentation                          | Spatial/temporal transformations, synthetic training data, and analysis of their benefits or limitations.                               |
| Language models                            | Discussed a concrete role of LLM's in recognition, decoding, correction, or training.                                                   |
| Generative models                          | Their role in CSLR or its training pipeline. Explicitly identify whether diffusion models are analyzed, merely mentioned, or not found. |

Categories may overlap when justified.

### Coverage scoring

Assign scores **specifically for CSLR-related survey coverage**:

- **0 — Not found:** No relevant CSLR discussion found after inspection of the full paper.
- **1 — Mentioned/described:** Brief mention, examples, or a descriptive list, without substantive synthesis or comparison.
- **2 — Substantively analyzed:** Meaningful classification, comparison, synthesis, or discussion of strengths, limitations, or implications.
- **? — Uncertain/not assessable:** Ambiguous task attribution, inaccessible content, or insufficient evidence.

Apply the following constraints:

- A dedicated heading does not automatically justify `2`.
- A substantive comparison table can justify `2`, even if accompanying prose is brief.
- A bibliography entry alone does not justify `1`.
- Coverage limited to isolated SLR, SLT, or sign production does not count as CSLR coverage. Record that other-task coverage explicitly in the explanation.
- If a general SLR discussion cannot reliably be attributed to CSLR, use `?` and explain.
- For the combined language-model category, state **conventional LM status and LLM status separately** in the explanation.
- For generative models, state **diffusion-model status separately**. General generative-model coverage does not imply diffusion-model coverage.
- For `0`, write “Not found after full-text inspection.” Cite the closest relevant sections inspected where useful, but do not pretend that a single page proves absence.

# Analysis: [Paper title]

**Authors:** [...]
**Year:** [...]
**Paper type and CSLR relevance:** [...]
**Citation convention:** Page references use 1-based PDF page numbers.

## 1. Survey characteristics

### Paper ID, title, and link

**Value:** [Concise value ready to enter into the comparison table.]
**Explanation:** [One or two sentences explaining the value.]
**Evidence:** [PDF p. X, §Y, Table Z]

### Authors

**Value:** [...]
**Explanation:** [...]
**Evidence:** [...]

[Continue with every field specified for Table 1, in the original order.]

## 2. CSLR thematic coverage

### Corpora and sign languages

**Value:** [0 / 1 / 2 / ?] — [Not found / Mentioned or described / Substantively analyzed / Uncertain or not assessable]
**Explanation:** [One or two sentences describing what is covered, its task scope, and why this score applies.]
**Evidence:** [PDF p. X, §Y, Table Z]

[Continue with all categories specified for Table 2, in the original order.]

## 3. Brief synthesis

- **Main emphasis:** [...]
- **Coverage limitations:** [...]
- **Verification needed:** [...]

Do not claim that a new review is necessary, or that no existing survey covers a topic, based on this paper alone. Describe only what this paper supports.

Before responding, verify that every requested row is present, counts are correctly scoped, positive scores have evidence, and coverage of neighboring tasks has not been mistaken for CSLR coverage.
