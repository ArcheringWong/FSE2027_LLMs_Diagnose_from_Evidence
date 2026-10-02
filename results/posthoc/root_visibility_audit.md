# Root-Visibility Audit

**Status:** POST-HOC DESCRIPTIVE SUPPORTING ANALYSIS  
**Population:** 57 final eligible LOCALIZATION_DEMANDING Targeted-KO panels  
**Subject outputs used for classification:** No

## Mechanical rule

The audit inspects only model-visible alert and evidence-card fields. Text mentions use the frozen canonical root name and any exact same-identity visible name already present in `entity_canonicalization_v1.json`, after its frozen deterministic normalization (Unicode NFKC, casefolding, outer trim, whitespace collapse, and quote/dash normalization). No fuzzy matching, semantic inference, or post-freeze alias creation is used. Mention counts are counts of model-visible fields/cards containing at least one exact frozen term, not raw repeated substring occurrences inside a field. Card-entity identity is resolved with the frozen entity resolver and must match the frozen gold canonical identity.

## Results

- Targeted-KO panels with root visible in any model-visible content: **57/57**.
- Panels with root visible in evidence observation text: **57/57**.
- Panels retaining at least one evidence card whose entity resolves to the frozen gold canonical identity: **20/57**.
- Panels with root visible in the top-level alert: **0/57**.
- Root-name mention fields/cards by modality: topology=58, trace=0, metric=0, log/event=0, alert=0, other=0.

## Interpretation boundary

The Targeted-KO intervention did not remove the root entity from model-visible context. Root identity remained visible through retained context, predominantly topology. RootLocal-KO therefore intervenes on root-local anomalous evidence cards rather than eliminating all visibility of the answer entity. It still does not separately identify diagnostic anomaly content from the salience and ownership cues conveyed by root-local evidence cards. This audit does not establish that entity exposure is fully controlled or that anomaly content is isolated.
