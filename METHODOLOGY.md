# Evaluation Methodology

## Purpose

This methodology explains how OASPS evaluates a public surveillance system without collapsing public statements, technical controls, local configuration, and independent proof into one score. It is designed to make disagreement inspectable: a reader should be able to identify the requirement, the responsible actor, the evidence, the judgment, the date, and the next evidence needed.

OASPS does not calculate a single vendor score. Different responsibilities belong to different actors, and a platform-level safeguard may be present while a local agency configures or documents it differently.

## Unit of analysis

Each row in a case-study matrix evaluates one requirement against one defined subject and jurisdiction. A row must remain narrow enough that its evidence label and assessment do not hide materially different conditions.

For example, a vendor's documented national retention default, a customer's contracted retention setting, and a current production configuration are three different facts. They may require three rows or a row that explicitly separates all three evidence layers.

## Source hierarchy

Use the strongest available evidence in this order where practical:

1. statutes, regulations, court records, signed public contracts, procurement records, agency policies, and public audit records;
2. vendor legal terms, product policies, transparency portals, technical or security documentation, and official product announcements;
3. independent security assessments, research, civil-liberties analysis, investigative reporting, and public-record investigations;
4. reproducible observation or authorized testing of public or customer-visible behavior;
5. marketing material, only as evidence of what the publisher asserts.

The order is a preference, not an automatic truth ranking. A signed 2024 contract is strong evidence of the 2024 contracted state but cannot establish the 2026 production configuration. A vendor technical page may accurately describe a platform capability but cannot, by itself, prove that a particular agency enabled it.

## Evidence labels

Every matrix row uses exactly one evidence label.

| Label | Meaning |
|---|---|
| `Verified` | Primary evidence supports the fact and the relevant behavior or record is independently checkable within the row's stated scope. |
| `Vendor-asserted` | The vendor states the behavior, but outsiders cannot independently establish the complete implementation. |
| `Partially verifiable` | Some meaningful external evidence exists, but an important layer, period, event class, configuration, or implementation detail remains opaque. |
| `Unknown` | Public evidence is insufficient to determine the relevant behavior. Unknown is not a negative finding. |
| `Noncompliant` | Available evidence establishes failure against a binding legal, contractual, or policy obligation identified in the row. This label is not used merely because a system falls short of a proposed OASPS requirement. |

`Noncompliant` is an evidence label only when the evidence establishes noncompliance with an applicable obligation. A proposed-standard gap is normally expressed through the assessment `Does not meet`, paired with the evidence label that describes how well the underlying facts are known.

## Assessment labels

The assessment answers how the observed behavior compares with the OASPS requirement.

| Assessment | Meaning |
|---|---|
| `Meets` | Evidence within the stated scope establishes the requirement is satisfied. |
| `Partly meets` | Meaningful parts are satisfied, but a material element, actor, event class, deployment layer, or proof remains incomplete. |
| `Does not meet` | Evidence establishes that the observed behavior falls short of the proposed requirement. This is not automatically a statement of illegality or misconduct. |
| `Unknown` | The evidence cannot support a comparison. |
| `Not applicable` | The requirement does not apply to the stated subject, actor, or jurisdiction, with the reason recorded in notes. |

## Implementation states

Every row uses exactly one state:

- `Deployed now`: evidence describes behavior currently in operation within the row's scope.
- `Announced or future`: the behavior is planned, rolling out, promised, or scheduled but not established as universally deployed.
- `Optional or customer-configurable`: the capability exists, but customer or administrator choice determines whether or how it operates.
- `Jurisdiction-specific`: the behavior depends on a contract, law, policy, or configuration tied to a jurisdiction.
- `Unknown`: current implementation cannot be established.

Historical facts may still use `Jurisdiction-specific` when the date and historical limitation are explicit in the finding and `last_verified` fields. The notes must not imply that a historical state is current.

## Responsible actors

Each requirement and matrix row assigns responsibility using exactly one allowed value:

- `Vendor`
- `Agency`
- `Legislature`
- `Court`
- `Independent oversight`
- `Shared`

Use `Shared` when satisfying the requirement requires coordinated action by more than one actor. Do not convert a legislative, judicial, procurement, or agency obligation into a vendor-only score.

## Four evidence layers

Every matrix row separates:

1. **Documented policy** — what a statute, contract, policy, term, or public statement says.
2. **Technical control** — what mechanism is described or observed to enforce, record, prevent, or verify behavior.
3. **Deployed configuration** — the version, setting, jurisdictional choice, customer state, or production condition actually in scope.
4. **Independent verification** — what an external reviewer can establish without relying exclusively on the responsible actor's assertion.

Text in one layer must not silently populate another. A policy promise does not prove a technical control; a platform capability does not prove local enablement; a security audit does not automatically establish civil-liberties outcomes or production identity.

## Evidence and judgment remain separate

The `evidence_label` describes confidence in the underlying facts. The `assessment` compares those facts with the OASPS requirement. These fields must not be combined.

Examples:

- A public contract can make a historical retention setting `Verified`, while the assessment against a short-retention requirement may be `Does not meet`.
- A meaningful deletion design may be `Partially verifiable` and `Partly meets` because public evidence does not cover every backup or replica.
- A missing current configuration is `Unknown` and `Unknown`, not `Noncompliant`.

## Documentation and implementation timing

Rights-relevant documentation should identify a version, effective date, publication date, immutable archive, and change history. Evaluators must distinguish:

- announced behavior;
- behavior rolling out;
- a default for new customers;
- an optional feature;
- a jurisdiction-specific rule;
- universal deployment;
- the current configuration of the evaluated agency.

When public documents conflict, preserve the conflict, cite each source, state what each can establish, and use the narrower conclusion. Do not select whichever document best supports a preferred thesis.

## Last-verified dates

`last_verified` is the date on which the evaluator last checked the cited evidence for the row, formatted `YYYY-MM-DD`. It is not necessarily the publication date, effective date, contract date, or date of the behavior.

Every case-study narrative should state its review date. A later reader must treat time-sensitive platform and jurisdiction findings as a dated snapshot.

## Source IDs and citations

All evidence receives a stable `SRC-####` identifier in [`evidence/sources.csv`](evidence/sources.csv). IDs are never recycled after publication. If a source is withdrawn or becomes unavailable, retain the row, record the new status in notes, and replace a claim only through visible review history.

Rules:

- Each consequential factual paragraph in Flock or Fairfield narrative files ends with one or more supporting source IDs in brackets, such as `[SRC-0010]` or `[SRC-0010, SRC-0016]`.
- Every cited source ID must resolve to exactly one source-register row.
- The cited source must support the claim immediately before it.
- Multiple IDs in `matrix.csv` are pipe-separated, such as `SRC-0010|SRC-0016`.
- Short quotations are used only when necessary. Paraphrase is preferred.
- A vendor source proves the vendor's public statement, not the complete production implementation.
- A factual claim without a recoverable source is removed from narrative findings or preserved as an explicit unresolved question.

## Legal floor and independent verifiability

Case studies keep two questions distinct:

1. Does available evidence establish compliance with an applicable statute, regulation, binding contract, or local policy?
2. Can the public or a genuinely independent reviewer establish rights-relevant behavior from evidence that does not depend primarily on agency or vendor assertion?

A deployment may be legally compliant and independently under-verifiable. Conversely, transparency alone does not establish legal compliance. OASPS is not legal advice and does not issue legal conclusions beyond careful summaries of cited materials.

## Treatment of unknowns

Unknown is a valid result and a public research target. It is not proof of concealment, misconduct, or failure.

For an unknown row:

- describe exactly what public evidence does and does not establish;
- identify the missing artifact or observation;
- record a narrow `unresolved_question`;
- record a lawful, proportionate `next_action`;
- avoid inferring current state from an old contract, a neighboring agency, or a generic platform default.

No records request, external contact, or unauthorized test is performed automatically as part of this repository.

## Row construction procedure

For each proposed requirement:

1. define one falsifiable claim and the subject/jurisdiction;
2. assign the responsible actor;
3. collect the strongest lawful public evidence already available;
4. fill documented policy, technical control, deployed configuration, and independent verification separately;
5. assign one evidence label, one assessment, and one implementation state;
6. record the date and supporting source IDs;
7. state the unresolved question and next lawful evidence action;
8. check the narrative wording against the row and cited source;
9. run `python scripts/validate.py` before handoff.

## Corrections and disputes

Corrections are made visibly through issues, pull requests, commits, and changelog entries.

- Evidence corrections should identify the claim or source ID, proposed correction, source, date checked, and impact on the finding.
- Framework criticism should identify the requirement, responsible actor, objection, proposed wording or disposition, and relevant basis.
- Conflicting evidence remains documented until the conflict is resolved.
- Substantive objections and their disposition should be preserved even when no change is made.
- Feedback is not endorsement unless the contributor explicitly authorizes that description.

## Privacy, security, and research limits

Do not commit credentials, raw plate numbers, personal travel records, requester addresses, private email addresses, nonpublic operational details, or exploitation instructions. Redact records before inclusion. Do not conduct unauthorized testing, defeat or bypass cameras, or turn public camera information into a tracking aid.

Public camera locations are referenced only when already lawfully public and genuinely necessary to an accountability claim; aggregate and policy-level analysis is the default.

## Method limitations

OASPS `0.2.0-draft.1` has not completed independent privacy, public-law, or software-assurance review. Its recognized-framework crosswalks are interpretive and do not establish formal conformity. The Flock case study is a dated evidence review of a defined ALPR scope, not an evaluation of every Flock product or every customer deployment.
