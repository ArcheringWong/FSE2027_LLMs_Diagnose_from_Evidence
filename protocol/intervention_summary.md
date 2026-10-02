# Intervention summary

## Full

The Full condition is a constructed evidence panel, not an unfiltered dump of
all incident telemetry. It contains diagnostic evidence plus three neutral
context cards validated before subject-model execution.

## Targeted-KO

For the 57 localization incidents, RootLocal-KO replaces root-local anomalous
cards with validated same-incident items that are non-root, outside the
propagation chain, and do not introduce a severe alternative fault. The alert,
topology, downstream symptoms, unrelated context, and neutral slots are
retained. Root identity remains visible through retained topology in all 57
localization KO panels.

For the 13 same-service fault-identification incidents, FaultEvidence-KO
normalizes the fault-specific evidence while retaining root identity and
modality. Metric targets use real same-entity, same-metric baseline-like
observations from the pre-alert period; trace targets use a normal or OK
same-service exemplar. Synthetic values and cross-entity fallback are not
used.

## Matched neutral Placebo

Placebo keeps diagnostic cards object-identical and replaces the three neutral
slots with other validated neutral items from the same incident. Replacements
are matched slot-wise on modality, abstraction level, benign/stable status,
temporal compatibility, approximate length, numeric/textual form, and panel
position. Placebo is matched to Full's neutral slots, not one-for-one to the
number of cards changed by Targeted-KO.

## Controls and interpretation

Across conditions, card identifiers, cardinality, role slots, and ordering are
fixed. Rendered prompt lengths remain within 10% of Full; the observed maximum
deviation is 5.4%. Localization panels contain a median of 12 cards and
Targeted-KO replaces a median of 2; Placebo replaces exactly 3. Fault panels
contain a median of 10 cards and Targeted-KO replaces a median of 3.

Gold annotations were used offline to identify candidate diagnostic roles and
to score predictions. Gold conclusions, role labels, target annotations, and
candidate-validity judgments were never included in subject prompts.

The contrast identifies response to the designated evidence bundle relative to
the implemented neutral replacement. It does not separately identify anomaly
semantics from card-level entity ownership/salience, and it is not a measure of
hidden reasoning or chain-of-thought faithfulness.

