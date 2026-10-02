# Human Judge Audit Plan

- Audit fraction: 15% of all valid Judge outputs, rounded up globally (`ceil(0.15*N)`). For the planned 84×2×3 = 504 outputs this is 76, subject to actual eligible/Judge count.
- Strata: component × subject-model slot × condition.
- Allocation: proportional largest-remainder allocation, minimum one per non-empty stratum when feasible; deterministic tie-break by stratum label.
- Within-stratum selection: ascending SHA-256 of `20270829|judge_unit_id`; fixed seed `20270829`.
- Auditor: independent human, blinded to provider identity, condition, hypothesis, development results, and Judge answer.
- Agreement: report raw agreement for categorical fields and weighted kappa for 0–3 fields with bootstrap CI; disagreements do not silently rewrite Judge outputs. Report original Judge score, human score, and adjudication separately.
