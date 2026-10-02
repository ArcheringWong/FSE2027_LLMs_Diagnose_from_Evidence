# Prediction-change Definitions

For each incident `i`, model `m`, and non-Full condition `c`:

1. `raw_prediction_change`: raw primary-field string under `c` is not byte-equal to Full. Auxiliary only.
2. `normalized_string_change`: strings differ after the frozen format normalizer. Auxiliary only.
3. `canonical_primary_flip`: frozen canonical primary identity under `c` differs from Full. Formal flip metric.
4. `correctness_change`: deterministic primary correctness under `c` differs from Full.
5. `granularity_only_change`: normalized strings and resolved entity levels differ, but unique topology-derived canonical primary identity is equal. Then canonical flip is false.

Fault canonical identity is the deterministic frozen taxonomy label. Root canonical flip identity is `service:<id>` when service projection is unique, otherwise the exact typed entity identity; unresolved text uses a normalized unresolved sentinel. Correctness continues to use strict gold-declared entity level, so canonical flip and correctness are intentionally different constructs.
