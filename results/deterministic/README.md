# 1. Cohort

- final incidents = 70
- localization = 57
- fault = 13
- models = 2
- complete triplets = 140

# 2. Primary result

## Localization

- mean incident-level SER = 0.710526
- 95% CI = [0.596491, 0.815789]
- one-sided permutation p = 0.000010
- K rate = 0.798246
- Placebo flip rate = 0.087719
- primary hypothesis result = SUPPORTED

# 3. Localization accuracy

- Full accuracy = 0.596491
- KO accuracy = 0.017544
- Placebo accuracy = 0.614035
- AccuracyGap = 0.596491
- 95% CI = [0.482456, 0.710526]
- raw p = 0.000010
- adjusted p = 0.000030

# 4. Fault component

- Fault SER = 0.153846
- Fault AccuracyGap = 0.000000
- Full deterministic accuracy = 0.000000
- KO deterministic accuracy = 0.000000
- Placebo deterministic accuracy = 0.000000

Fault deterministic scoring accepts only the frozen canonical taxonomy label or pre-frozen deterministic synonyms. Low deterministic accuracy does not authorize taxonomy changes.

# 5. By model

## Qwen

- localization K rate = 0.877193
- localization P rate = 0.035088
- localization mean SER = 0.842105
- Full / KO / Placebo accuracy = 0.684211 / 0.035088 / 0.684211
- AccuracyGap = 0.649123

## DeepSeek

- localization K rate = 0.719298
- localization P rate = 0.140351
- localization mean SER = 0.578947
- Full / KO / Placebo accuracy = 0.508772 / 0.000000 / 0.543860
- AccuracyGap = 0.543860

# 6. Descriptive

- observations with invalid evidence IDs = 0
- total invalid evidence IDs = 0
- raw prediction changes across KO/Placebo comparisons = 125
- canonical primary flips = 121
- granularity-only changes = 0
- evidence role analysis = ROLE_METADATA_NOT_AVAILABLE

- KO vs Full: mean valid-ID Jaccard = 0.420095; mean confidence delta = -0.013929; median confidence delta = 0.000000
- PLACEBO vs Full: mean valid-ID Jaccard = 0.869420; mean confidence delta = -0.001143; median confidence delta = 0.000000

Confidence values are descriptive model reports, not calibrated probabilities.

# 7. Sensitivity

- POLICY_B_SERVICE_EQUIVALENT: Full=0.605263, KO=0.017544, Placebo=0.640351, gap=0.622807
- POLICY_C_HIERARCHY_AWARE_PARTIAL: Full=0.692982, KO=0.017544, Placebo=0.719298, gap=0.701754
- FAULT_STRICT_LABEL_ONLY: Full=0.000000, KO=0.000000, Placebo=0.000000, gap=0.000000

# 8. Integrity

- post-freeze aliases added = 0
- post-freeze synonyms added = 0
- cases removed based on result = 0
- model/Judge calls in this stage = 0
- network calls = 0

Inference used the incident as the independent unit. The primary test was one-sided; the three frozen secondary tests were two-sided and Holm-adjusted.
