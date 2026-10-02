# Final Semantic Results Report

# 1. Human Audit Integrity

- sample N = 63
- complete = 63
- invalid labels = 0
- Judge leakage during human review = 0
- labels frozen before Judge comparison = YES

# 2. Judge–Human Agreement

- fault_semantic_correct raw agreement = 0.873016 (55/63)
- unsupported_claim raw agreement = 0.650794 (41/63)
- causal_explanation_quality linear weighted kappa = 0.140501; 95% bootstrap CI = [0.058998, 0.232714]
- causal exact agreement = 0.158730; within-one agreement = 0.777778
- evidence_grounding linear weighted kappa = 0.385965; 95% bootstrap CI = [0.191917, 0.560530]
- grounding exact agreement = 0.619048; within-one agreement = 0.984127
- operational weighting = linear
- bootstrap = 10000 paired audit-row resamples, seed 20270828, percentile 95% CI; undefined replicates excluded and counted
- adjudication performed = NO

# 3. Full 420 Semantic Outcomes

| Condition | Fault semantic yes rate | Causal quality mean | Grounding mean | Unsupported-claim yes rate |
|---|---:|---:|---:|---:|
| FULL | 0.092857 | 2.314286 | 2.242857 | 0.157143 |
| KO | 0.000000 | 1.550000 | 1.542857 | 0.621429 |
| PLACEBO | 0.171429 | 2.321429 | 2.285714 | 0.157143 |

# 4. By Model

Qwen and DeepSeek descriptive semantic outcomes are reported separately, overall and by condition, in `semantic_model_summary.csv`. No model-difference significance test was performed.

# 5. By Component

ROOT_LOCALIZATION and FAULT_IDENTIFICATION descriptive semantic outcomes are reported separately, overall and by condition, in `semantic_component_summary.csv`.

# 6. Paired Semantic Contrasts

The frozen statistical plan did not pre-register inferential tests for Judge semantic outcomes. `semantic_paired_contrasts.csv` therefore reports only incident-level paired descriptive differences for KO − FULL, PLACEBO − FULL, and PLACEBO − KO, with descriptive incident-bootstrap CIs and no p-values.

# 7. Relationship to Deterministic Results

- deterministic primary unchanged = YES
- semantic Judge role = secondary only
- deterministic taxonomy accuracy is not semantic mechanism correctness
- semantic results do not replace, correct, or validate deterministic scores

# 8. Integrity

- Judge outputs modified = 0
- Human labels modified after comparison = 0
- Judge labels overwritten by human = 0
- API calls = 0
- network calls = 0
