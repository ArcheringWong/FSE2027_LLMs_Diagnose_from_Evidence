# Confirmatory Statistical Plan

## Population and units

The pre-model clean pool contains 84 incidents: 59 `LOCALIZATION_DEMANDING` and 25 `SAME_SERVICE_FAULT`. Future exclusion is allowed only for pre-frozen intervention-feasibility failures, before subject-model execution and without model outputs. Incident is the independent unit; subject models are repeated measurements within incident.

## Primary estimand

For incident `i`, model `m`, `K_im = I(CanonicalKO != CanonicalFull)`, `P_im = I(CanonicalPlacebo != CanonicalFull)`, and `SER_im = K_im - P_im`. Let `SER_i` be the mean over complete model triplets and estimate `mean_i(SER_i)` in the 59-case localization stratum.

## Primary inference

- Direction: one-sided, `H0: mean SER <= 0`, `H1: mean SER > 0`.
- Primary test: paired incident-level sign-randomization/permutation test with 100,000 Monte Carlo sign flips, seed `20270827`; the observed statistic is mean incident-level SER. Use `(extreme+1)/(B+1)`.
- CI: always report a two-sided 95% percentile bootstrap CI using 10,000 incident-cluster resamples with replacement, seed `20270828`; all model/condition observations for an incident travel together.
- Alpha: 0.05. Report effect estimate, CI, p-value, eligible N, analyzed N, and attrition.

## Secondary family

Exactly three secondary tests are: fault-stratum SER, localization accuracy gap, and fault accuracy gap. Report two-sided paired incident permutation p-values and 95% incident-cluster bootstrap CIs; apply Holm correction across these three. Pooled 84-case and model-specific estimates are descriptive/exploratory and do not create confirmatory p-value claims.

## Missingness and reporting

Apply `missing_data_policy.md`. Report Full/KO/Placebo flip rates, correctness, SER, accuracy gap, valid citation shifts, and confidence deltas with denominators. Full-incorrect cases are retained. No metric, direction, resampling unit, family, seed, or exclusion criterion may change after viewing confirmatory output.
