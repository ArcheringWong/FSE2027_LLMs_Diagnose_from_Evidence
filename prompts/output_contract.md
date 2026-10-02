# Subject Output Contract

The primary structured fields are `root_entity`, `fault_type`, and `evidence_ids`.

- `root_entity`: best-supported root-cause entity.
- `fault_type`: best-supported fault type.
- `evidence_ids`: IDs present in the supplied panel only; nonexistent IDs are recorded as invalid and are never repaired.
- `diagnosis_summary`: concise evidence-grounded diagnosis, recommended maximum 2–3 sentences.
- `confidence`: number in `[0,1]`, recorded descriptively only.

No chain-of-thought, hidden reasoning, private step-by-step reasoning, debate, or self-consistency trace is requested.
