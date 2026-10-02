# Anonymous Review Artifact

This package supports the paper's evidence-intervention study without exposing
author identities, API credentials, private annotation mappings, or internal
project history. It is intentionally compact: the package contains the frozen
model-visible inputs, subject outputs, analysis-ready scores, semantic labels,
and the code needed to recompute the paper's principal statistical results.

## What reviewers can verify

| Paper claim | Supporting files |
|---|---|
| 70 incidents, 57 localization and 13 fault-identification | `data/final_confirmatory_cohort.csv` |
| Full / Targeted-KO / Placebo inputs | `data/final_model_facing_panels.jsonl` |
| Exact prompts and structured output contract | `prompts/` |
| 420 complete subject-model observations | `data/subject_outputs.jsonl` |
| Canonical flips, correctness, SER, AccuracyGap, and sensitivity policies | `results/deterministic/` |
| Primary permutation test and bootstrap interval | `analysis/reproduce_results.py` |
| Secondary semantic Judge results and 15% human audit | `results/semantic/` |
| Full-correct transitions and root-visibility checks | `results/posthoc/` |
| Values used in paper tables and figures | `results/paper_values/` |

## Quick start

Python 3.10 or newer is recommended.

```text
python -m pip install -r requirements.txt
python analysis/verify_integrity.py
python analysis/reproduce_results.py
```

The reproduction script is offline. It makes no network, subject-model, or
Judge calls. On success it prints a JSON report and ends with
`REPRODUCTION_CHECKS_PASSED`.

## Package structure

```text
analysis/                 integrity and statistical reproduction scripts
data/                     frozen cohort, panels, and sanitized model outputs
licenses/                 code and RCA100 licensing information
prompts/                  exact subject prompts and output schema
protocol/                 frozen construct, scoring, inference, and audit rules
results/deterministic/    observation-, model-, and incident-level scores
results/semantic/         secondary Judge labels and anonymous human-audit labels
results/posthoc/          frozen transition and root-visibility analyses
results/paper_values/     direct table/figure value traces
SHA256SUMS                integrity ledger for every packaged file except itself
```

## Frozen design at a glance

- Incidents: 70 total; 57 root-localization and 13 same-service
  fault-identification.
- Conditions: Full, Targeted-KO, and matched neutral Placebo.
- Subject models: `qwen3.7-plus-2026-05-26` and `deepseek-v4-flash`.
- Subject observations: 70 incidents × 3 conditions × 2 models = 420.
- Subject decoding: temperature 0, top-p 1, thinking/tools/web disabled, one
  run per model-condition-incident, structured JSON output.
- Independent inferential unit: incident; the two subject models are repeated
  measurements within incident.
- Primary inference: 100,000 one-sided sign-randomization draws (seed
  20270827) and 10,000 incident-cluster bootstrap draws (seed 20270828).
- Semantic Judge: fixed `openai/gpt-4o-mini-2024-07-18`; secondary descriptive
  evaluation only.
- Human audit: one external annotator, 63 rows (15%), used only to estimate
  Judge--human agreement.

Full settings are recorded in `protocol/model_and_judge_settings.json`.

## Deliberate exclusions

The package does **not** contain:

- API keys, environment files, account/workspace identifiers, request IDs, or
  provider billing records;
- raw HTTP requests/responses, retry logs, or failed-attempt ledgers;
- author names, affiliations, local absolute paths, or revision history;
- private reviewer-to-task mappings or annotator contact information;
- RCA100 raw telemetry or the separately controlled RCA100 answer key;
- development-set outputs, superseded analyses, draft manuscripts, or internal
  engineering QA directories.

`data/subject_outputs.jsonl` is a field-minimized derivative of the frozen
execution ledger. It retains the model snapshot, condition, parsed prediction,
raw returned content, hashes, and technical status, while removing network and
billing metadata.

## Reproducibility boundary

The package reproduces the reported analyses from frozen model outputs. It does
not attempt to repeat paid API calls: hosted model behavior and provider
infrastructure may change even when a snapshot identifier is fixed. The
restricted RCA100 answer key is also not redistributed. Consequently, the
package exposes the already-frozen deterministic scoring records needed to
audit and recompute paper-level statistics, while documenting the scoring rules
used to create them.

See `CITATION_AND_LICENSE.md` for RCA100 attribution and redistribution terms.
See `DATA_DICTIONARY.md` for field-level guidance and
`protocol/intervention_summary.md` for a compact account of the three
conditions.

