# Analysis: Reviewing 25 years of continuous sign language recognition research: Advances, challenges, and prospects

**Authors:** Sarah Alyami, Hamzah Luqman, Mohammad Hammoudeh.  
**Year:** 2024.  
**Paper type and CSLR relevance:** Survey/review; CSLR is the primary topic.  
**Citation convention:** References use 1-based PDF page numbers, which match the printed page numbers where shown.  
**Access or extraction limitations:** All 32 pages were accessible, including references, tables, and figures. No appended supplementary material was found. Several internal inconsistencies affect dates, dataset statistics, and performance values; these are flagged below.

## 1. Survey characteristics

### Paper ID, title, and link

**Value:** Alyami et al. (2024). *Reviewing 25 years of continuous sign language recognition research: Advances, challenges, and prospects*. [DOI: 10.1016/j.ipm.2024.103774](https://doi.org/10.1016/j.ipm.2024.103774).

**Explanation:** The title and DOI appear on the first page.

**Evidence:** [PDF p. 1]

### Authors

**Value:** Sarah Alyami; Hamzah Luqman; Mohammad Hammoudeh.

**Explanation:** Names follow the paper’s author list.

**Evidence:** [PDF p. 1]

### Publication year and venue

**Value:** 2024; *Information Processing and Management*, volume 61, article 103774. Available online 24 May 2024.

**Explanation:** The publication year and online availability date are explicitly stated; acceptance was 8 May 2024.

**Evidence:** [PDF p. 1]

### Paper type

**Value:** Survey/review with taxonomy, literature synthesis, and comparisons of published results.

**Explanation:** The paper reviews 126 studies and classifies existing approaches. Its performance tables summarize cited studies rather than experiments on a newly proposed model.

**Evidence:** [PDF p. 1, Abstract]; [PDF pp. 20–21, Table 8]; [PDF p. 26, §7]

### Literature coverage period

**Value:** **1997–2023 according to Table 1; reported search cutoff: March 2024. Exact period is internally inconsistent.**

**Explanation:** The authors describe approximately 25 years of research, but Table 8 includes studies dated 2024. Preserve the stated period and cutoff separately rather than silently resolving the discrepancy.

**Evidence:** [PDF p. 3, §2, Table 1]; [PDF pp. 20–21, Table 8]

### Tasks and CSLR relevance

**Value:** **CSLR primary**; isolated SLR, fingerspelling, and SLT provide context, pretraining resources, or related multitask settings.

**Explanation:** CSLR is formulated as video-to-gloss-sequence prediction. SLT is distinguished from recognition, although joint CSLR–SLT systems are included; the stated screening exclusions cover isolated SLR, translation-focused studies, and sign spotting.

**Evidence:** [PDF p. 3, §§2–3]; [PDF p. 4, §3]; [PDF p. 18, §4.2.7]

### Main emphasis

**Value:** Classification and comparison of CSLR methods, especially deep-learning spatial, temporal, and alignment components, alongside datasets, acquisition methods, modalities, and sign cues.

**Explanation:** The architecture review and comparative tables receive substantial attention, followed by synthesis of performance and practical limitations.

**Evidence:** [PDF pp. 14–19, §4]; [PDF pp. 20–24, Tables 8–9, §5]

### Review methodology

**Value:** Author-described comprehensive review; database search with a brief exclusion procedure, but incomplete reproducibility reporting.

**Explanation:** Sources are Google Scholar, ProQuest, Scopus, and “IEEE Explore,” as written. The authors report reducing 306 papers to 126 by excluding isolated SLR, studies outside recognition such as translation and spotting, and non-English publications; exact queries, deduplication, screening stages/reviewers, quality appraisal, and PRISMA usage are **Not reported**.

**Evidence:** [PDF p. 3, §2]; [PDF p. 26, §7]

### Number of included primary studies

**Value:** **126 studies**, explicitly reported for the CSLR review.

**Explanation:** This is the authors’ included-study count, not the bibliography length. It should be recorded as a reported count rather than an independently verified set of 126 uniquely eligible primary studies.

**Evidence:** [PDF p. 1, Abstract]; [PDF p. 3, §2]; [PDF p. 26, §7]

### Number of previous surveys compared

**Value:** **7 previous surveys** — extraction count from Table 1, excluding “Our survey.”

**Explanation:** Table 1 compares seven earlier reviews across seven coverage features. This count is separate from the 126 reviewed studies.

**Evidence:** [PDF p. 3, Table 1]

### Sign languages

**Value:** **16 sign languages reported across reviewed CSLR studies**, with German, Chinese, and American Sign Language receiving the most attention.

**Explanation:** Additional examples include Arabic, Indian, Greek, Taiwanese, Spanish, Italian, Irish, Persian, Turkish, French, Dutch, and Japanese sign languages. Dataset coverage also includes Russian and a “Kazakh-Russian” label; these resource labels should not be conflated with the authors’ study-level count.

**Evidence:** [PDF p. 19, §5]; [PDF p. 22, Fig. 9]; [PDF p. 16, Table 7]; [PDF p. 7, Table 2]

### Datasets/corpora

**Value:** Principal comparison resources: **PHOENIX2014, PHOENIX2014T, SIGNUM, CSL, CSL-Daily, and continuous GrSL**.

**Explanation:** This is a selective list of repeatedly analyzed CSLR benchmarks; Table 2 additionally includes RWTH-BOSTON-104, TheRuSLan, ArabSign, FluentSigners-50, ASL-Homework, Scene-PHOENIX, and others. How2Sign is discussed as an SLT resource, while Kinetics-400, Sports1M, and UCF101 appear as action-recognition pretraining sources rather than CSLR benchmarks.

**Evidence:** [PDF pp. 6–7, §3.2, Table 2]; [PDF pp. 20–21, Table 8]; [PDF p. 19, §5]; [PDF pp. 22–23, §5]

### Claimed contribution

**Value:** **Author claim:** a comprehensive CSLR-focused historical review, seven-dimensional taxonomy, detailed deep-learning classification, and identification of research gaps.

**Explanation:** The authors position the review against earlier surveys that they describe as narrower in task coverage, acquisition methods, historical coverage, or treatment of deep learning. This is their novelty claim, not an independently verified finding.

**Evidence:** [PDF p. 2, §1]; [PDF p. 3, §2, Table 1]; [PDF p. 26, §7]

## 2. CSLR thematic coverage

Scores describe the depth of this survey’s CSLR coverage, not the reliability of every underlying claim.

### Corpora and sign languages

**Value:** **2 — Substantively analyzed**

**Explanation:** Table 2 compares language, vocabulary, sentences, signers, samples, modalities, and domains. The prose examines recording conditions, signer diversity, restricted vocabularies, public availability, and differences between evaluation splits.

**Evidence:** [PDF pp. 5–7, §3.2, Table 2]; [PDF p. 19, §5]; [PDF p. 25, §6.1]

### Annotation and task formulation

**Value:** **2 — Substantively analyzed**

**Explanation:** The paper defines order-preserving video-to-gloss recognition, distinguishes it from translation, and connects missing temporal boundaries to alignment-based training. It discusses gloss annotations and optional sentence translations, although annotation procedures and quality control receive little attention.

**Evidence:** [PDF pp. 3–4, §3]; [PDF p. 6, §3.2]; [PDF pp. 12–13, §3.6]

### Input data and modalities

**Value:** **2 — Substantively analyzed**

**Explanation:** The survey compares vision and sensor acquisition, RGB, depth, skeleton representations, optical flow, and multimodal combinations. It discusses tradeoffs involving practicality, noise, visual detail, robustness, and computational cost.

**Evidence:** [PDF pp. 8–11, §§3.3–3.4, Tables 3–5]; [PDF pp. 21–22, §5]

### Manual and non-manual cues

**Value:** **2 — Substantively analyzed**

**Explanation:** Hands, face, mouth, head motion, body pose, and gaze are classified and connected to recognition roles. The survey synthesizes full-frame versus localized-cue approaches and identifies difficulties in capturing subtle cues and combining them.

**Evidence:** [PDF pp. 10–13, §3.5, Table 6]; [PDF p. 22, §5]; [PDF p. 26, §6.2]

### Visual feature models

**Value:** **2 — Substantively analyzed**

**Explanation:** Coverage includes handcrafted representations, CNNs, 3D CNNs, GCNs, ViTs, and hybrid architectures. The survey classifies spatial backbones and discusses feature detail, modality representation, memory requirements, and reported recognition performance.

**Evidence:** [PDF pp. 14–19, §§4.1–4.2]; [PDF p. 22, §5]; [PDF p. 24, Table 9]

### Temporal modeling

**Value:** **2 — Substantively analyzed**

**Explanation:** RNN/LSTM/BLSTM, temporal convolutions, fully convolutional networks, and Transformers are compared in terms of contextual modeling and sequence processing. The synthesis addresses receptive-field limitations, variable sign lengths, and constraints on online recognition.

**Evidence:** [PDF pp. 15–18, §§4.2.2–4.2.7]; [PDF pp. 22–23, §5]; [PDF p. 24, Table 9]

### Alignment and decoding

**Value:** **2 — Substantively analyzed**

**Explanation:** HMM, CTC, DTW, reinforcement learning, and transducer approaches are discussed. The survey explains alignment without explicit boundaries, illustrates CTC decoding, and compares strategies addressing independence assumptions, overfitting, and alignment quality.

**Evidence:** [PDF pp. 12–14, §3.6, Fig. 7]; [PDF pp. 14–15, §4.1]; [PDF p. 19, §4.2.9]; [PDF pp. 23–24, §5, Table 9]

### Learning strategies and knowledge transfer

**Value:** **2 — Substantively analyzed**

**Explanation:** The review examines iterative pseudo-label training, isolated-sign and action-recognition pretraining, self-mutual knowledge distillation, multilingual training, and cross-lingual transfer, including limitations. These support the score; self-supervised learning does not receive a comparable dedicated synthesis.

**Evidence:** [PDF pp. 15–17, §§4.2.2–4.2.4]; [PDF p. 22, §5]; [PDF pp. 25–26, §6.2]

### Data augmentation

**Value:** **2 — Substantively analyzed**

**Explanation:** The survey explains paired video–text edits in Cross Modal Augmentation and the language-model-assisted extension PA-CMA, discussing their purpose and limitations. Background augmentation and augmentation for signer variability are also addressed, although there is no comprehensive taxonomy of spatial and temporal transformations.

**Evidence:** [PDF p. 6, §3.2]; [PDF p. 16, §4.2.2]; [PDF p. 23, §5]; [PDF p. 25, §6.2]

### Language models and LLMs

**Value:** **2 — Substantively analyzed, principally for conventional and BERT-based language modeling**

**Explanation:** **Conventional LM status:** n-gram and RNN models have concrete recognition/training roles; BERT-based gloss modeling is also discussed, including contextual learning, augmentation, and reported gains. **LLM status:** an explicit discussion of large language models as a distinct category was not found after full-text inspection; BERT coverage should be recorded explicitly rather than automatically treated as broad LLM coverage.

**Evidence:** [PDF pp. 16–17, §§4.2.2–4.2.4]; [PDF pp. 18–19, §§4.2.7–4.2.8]; [PDF p. 26, §6.2]

### Generative models

**Value:** **1 — Mentioned/described**

**Explanation:** SLRGAN is described as generating glosses in a recognition–translation pipeline, and DBN is identified as a generative model used for WiFi feature extraction; GAN approaches also appear in the performance table. These are scattered descriptions rather than a substantive generative-model synthesis; **diffusion models: Not found after full-text inspection**.

**Evidence:** [PDF p. 18, §4.2.7]; [PDF p. 19, §4.2.9]; [PDF pp. 20–21, Table 8]

### Evaluation and comparability

**Value:** **2 — Substantively analyzed**

**Explanation:** The paper explains WER, distinguishes it from accuracy and translation-oriented BLEU, separates several benchmark splits, and compares published results. It discusses private-dataset comparability and additional training data, but provides neither a unified experimental reevaluation nor a systematic audit of all protocol differences.

**Evidence:** [PDF pp. 3–4, §3]; [PDF p. 6, §3.2]; [PDF pp. 20–21, Table 8]; [PDF pp. 23–24, §5]

### Generalization and practical limitations

**Value:** **2 — Substantively analyzed**

**Explanation:** Coverage includes signer variation, unseen sentences, coarticulation, movement epenthesis, limited data and domains, background variation, computational demands, and online recognition. Data-centric and model-centric gaps organize these limitations into a broader synthesis.

**Evidence:** [PDF pp. 4–5, §3.1]; [PDF pp. 23–24, §5]; [PDF pp. 25–26, §§6.1–6.2]

## 3. Brief synthesis

- **Main emphasis:** A broad CSLR taxonomy with substantial coverage of architectures, alignment, acquisition, modalities, sign cues, and benchmark results. Learning strategies and language modeling are already meaningfully covered, so they should not be coded as absent.

- **Coverage limitations:** Generative models receive only scattered descriptions, and diffusion models and an explicit LLM-focused synthesis were not found. Search reproducibility, annotation quality assurance, and systematic evaluation-protocol auditing are limited.

- **Verification needed:** Preserve several unresolved inconsistencies:
  - **Coverage dates:** 1997–2023 in Table 1 versus a March 2024 cutoff and 2024 studies. [PDF p. 3, §2, Table 1]; [PDF pp. 20–21, Table 8]
  - **Dataset statistics:** PHOENIX2014 vocabulary is given as 2,048 in Table 2 but 1,389 in §6.1. [PDF p. 7, Table 2]; [PDF p. 25, §6.1]
  - **Performance values:** Cross-Ling’s PHOENIX2014 WER is 16.7 in Table 8 but 16.8 in §5; PHOENIX2014T is 18.5 in the table but 18.6 in the prose. [PDF pp. 20–21, Table 8]; [PDF p. 23, §5]
  - **Task eligibility:** Despite excluding translation-focused studies, Table 8 includes “Pose-SLT,” whose reference is titled *Neural sign language translation based on human keypoint estimation*. Its eligibility as CSLR evidence remains **Unclear** from this survey alone. [PDF p. 3, §2]; [PDF p. 21, Table 8]; [PDF p. 29, References]
