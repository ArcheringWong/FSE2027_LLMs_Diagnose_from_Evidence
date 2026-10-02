# Judge Protocol v1

## Scope

Judge only: fault-mechanism semantic correctness, causal-explanation quality, evidence-grounding quality, and unsupported diagnostic claims. Deterministic code alone evaluates exact entity, evidence-ID membership, JSON/schema validity, and taxonomy synonym match.

## Blinding and input

Exclude provider/model name, condition label, Full/KO/Placebo indicator, gold condition label, hypothesis, development results, and sibling-condition outputs. Present only an opaque `judge_unit_id`, incident alert, exactly the evidence visible to the subject, the subject diagnosis, and the gold semantic reference. Randomize presentation order by SHA-256 rank before judging.

## Rubric

- `fault_semantic_correct`: `yes` only when the mechanism is substantively equivalent to gold; `no` for contradiction, generic symptom, or different mechanism; `cannot_determine` only for genuine insufficiency.
- `causal_explanation_quality` 0–3: 0 absent/contradictory; 1 assertion only; 2 plausible causal link with partial specificity; 3 coherent gold-compatible chain with appropriate scope.
- `evidence_grounding` 0–3: 0 unsupported/contradicted; 1 weak generic tie; 2 multiple relevant links with minor gaps; 3 claims trace explicitly and correctly to visible evidence.
- `unsupported_claim`: yes when a material diagnostic claim lacks visible support or conflicts with it.
- `reason`: at most 60 words, referring only to visible evidence and rubric.

`JUDGE_MODEL_ID = TO_BE_FROZEN`. No Judge call is authorized until an append-only pre-Judge amendment freezes immutable model ID, endpoint scope, decoding, and prompt hash. Judge outputs never overwrite deterministic scores.
