# Data dictionary

## `data/final_confirmatory_cohort.csv`

One row per RCA100 task considered for the final cohort. The 70 rows have
`final_confirmatory_eligible=true`. `study_stratum` is either
`LOCALIZATION_DEMANDING` or `SAME_SERVICE_FAULT`.

## `data/final_model_facing_panels.jsonl`

One row per incident and condition (70 × 3 = 210 rows).

- `task_id`: stable benchmark task identifier.
- `study_stratum`: analysis stratum.
- `condition`: `FULL`, `KO`, or `PLACEBO`.
- `alert`: model-visible title, entity, and time window.
- `evidence_cards`: ordered model-visible cards. Each card records its
  condition-stable `evidence_id`, modality, entity, entity type, time, and
  rendered observation.

The file does not contain gold labels or hidden evidence-role annotations.

## `data/subject_outputs.jsonl`

One row per incident, condition, and subject model (420 rows). Important fields:

- `subject_model`, `condition`, `task_id`, and `study_stratum`: observation key.
- `raw_content`: exact model-returned textual content.
- `parsed_json`: parsed five-field prediction.
- `parse_status`, `observation_status`, `technical_status`: execution validity.
- `evidence_panel_hash`, `prompt_hash`: linkage/integrity hashes.

Network request IDs, provider-account metadata, timestamps, token billing, and
raw request/response paths were removed because they do not support a paper
claim and are unnecessary for peer review.

## Deterministic results

- `deterministic_observation_scores.csv`: one row per subject observation,
  including canonical identities and correctness under the frozen policies.
- `model_incident_triplets.csv`: one Full/KO/Placebo triplet per incident and
  subject model; 140 rows. This is the most useful file for transition checks.
- `incident_level_scores.csv`: 70 incident-level rows after averaging the two
  repeated subject-model measurements. This is the inferential input.
- `primary_results.json` and `secondary_results.json`: frozen estimates,
  resampling results, and Holm adjustment.
- `sensitivity_results.csv`: Policy B service-equivalent and Policy C
  hierarchy-aware localization scores plus strict fault-label sensitivity.

`K_i` is the incident-level Targeted-KO canonical flip rate, `P_i` is the
incident-level Placebo canonical flip rate, and `SER_i = K_i - P_i`.
`AccuracyGap_i = CorrectPlacebo_i - CorrectKO_i`.

## Semantic results

- `semantic_observation_results.csv`: 420 parsed Judge label sets.
- `semantic_*_summary.csv`: condition, model, component, and paired summaries.
- `judge_human_audit_labels.csv`: 63 anonymous Judge--human label pairs.
- `judge_human_agreement_summary.csv`: categorical raw agreement and ordinal
  linearly weighted kappa estimates.

Semantic outcomes are secondary and never overwrite deterministic entity or
taxonomy correctness.

## Post-hoc results

- `transition_decomposition_by_observation.csv` and its summaries decompose
  Full-to-KO and Full-to-Placebo correctness transitions.
- `root_visibility_by_incident.csv` records the mechanical visibility audit for
  the 57 localization KO panels.

These analyses are descriptive and introduce no additional hypothesis test.

