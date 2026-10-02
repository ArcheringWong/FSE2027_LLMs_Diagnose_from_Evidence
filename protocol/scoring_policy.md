# Confirmatory Scoring Policy

## Hierarchy

1. Headline: localization-stratum mean incident-level SER.
2. Key secondary: localization accuracy gap.
3. Secondary component: fault SER and fault accuracy gap.
4. Secondary semantic: blinded Judge outcomes.
5. Descriptive only: Full capability floor, citation shifts, confidence deltas, raw/normalized changes, service-equivalent and hierarchy-partial sensitivity scores.

## Root correctness

Primary is Policy A: exact canonical entity at the RCA100 gold-declared type. A cross-level operation/deployment/pod mapped to the gold service is not primary-correct. Policy B service-equivalent and Policy C hierarchy-aware partial are sensitivity analyses only.

## Fault correctness

Primary deterministic score accepts the canonical label or a synonym already present in frozen RCA100 taxonomy. Strict-label-only is sensitivity. Semantic mechanism correctness is a separate Judge outcome.

## Accuracy gap and Full

`AccuracyGap_im = Correct_Placebo_im - Correct_KO_im`; incident estimate averages available complete model triplets. Full defines capability and flip reference. Full-incorrect incidents stay in SER, flip, and citation analyses but cannot contribute a correct-to-incorrect transition.

## Citation and confidence

Report valid-ID Jaccard plus added/removed IDs and evidence-role counts. Report `confidence_KO - confidence_Full` and `confidence_Placebo - confidence_Full`. Neither is primary; confidence is not calibrated probability.
