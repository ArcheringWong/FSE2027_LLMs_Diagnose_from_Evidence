# Missing and Failure Policy

- Technical no-response after the already frozen retry policy: `MISSING_TECHNICAL`. The affected model×incident triplet is excluded from behavioral numerators and denominators; counts and reasons are reported by model and condition. It is never repeatedly rerun to improve completeness.
- Incident aggregation: average complete model triplets within incident. If none remain, the incident is absent from the behavioral estimand and reported as technical attrition. Both complete-case and conservative identification bounds are reported as sensitivity.
- Parse failure after the single deterministic recovery: `INVALID_PARSE`; no semantic repair. It is an observed behavioral output, included as incorrect/invalid with canonical sentinel `INVALID_PARSE`.
- JSON-schema failure: `INVALID_SCHEMA`; included as incorrect/invalid with its canonical sentinel. No Judge or LLM repair.
- Panel-invalid evidence IDs: never autocorrect. Retain raw IDs and count them; remove non-panel IDs from valid-ID Jaccard/role sets. If the primary fields otherwise satisfy schema, entity/fault correctness remains scorable. An ID with invalid JSON type/pattern is a schema failure.
