# Evaluation Methodology

## Purpose

This methodology explains how OASPS evaluates a public surveillance system without collapsing public statements, technical controls, local configuration, and independent proof into one score. It is designed to make disagreement inspectable: a reader should be able to identify the requirement, the responsible actor, the evidence, the judgment, the date, and the next evidence needed.

OASPS does not calculate a single vendor score. Different responsibilities belong to different actors, and a platform-level safeguard may be present while a local agency configures or documents it differently.

## Unit of analysis

Each row in a case-study matrix evaluates one requirement against one defined subject and jurisdiction. A row must remain narrow enough that its evidence label and assessment do not hide materially different conditions.

For example, a vendor's documented national retention default, a retention term listed in an order form, an executed customer agreement, and a current production configuration are different facts. They may require separate rows or a row that explicitly separates every evidence layer.

## Source hierarchy

Use the strongest available evidence in this order where practical:

1. statutes, regulations, court records, signed public contracts, procurement records, agency policies, and public audit records;
2. vendor legal terms, product policies, transparency portals, technical or security documentation, and official product announcements;
3. independent security assessments, research, civil-liberties analysis, investigative reporting, and public-record investigations;
4. reproducible observation or authorized testing of public or customer-visible behavior;
5. marketing material, only as evidence of what the publisher asserts.

The order is a preference, not an automatic truth ranking. A municipal meeting packet containing an order form is strong evidence of the terms presented for approval, but without execution evidence it cannot establish an executed agreement or a production configuration. A vendor technical page may accurately describe a platform capability but cannot, by itself, prove that a particular agency enabled it.

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
| `Not applicable` | The requirement does not apply to the stated subject, actor, or jurisdiction, with the reason recorded in `applicability_reason`. |

## Implementation states

Every row uses exactly one state:

- `Deployed now`: evidence describes behavior currently in operation within the row's scope.
- `Announced or future`: the behavior is planned, rolling out, promised, or scheduled but not established as universally deployed.
- `Optional or customer-configurable`: the capability exists, but customer or administrator choice determines whether or how it operates.
- `Jurisdiction-specific`: the behavior depends on a contract, law, policy, or configuration tied to a jurisdiction.
- `Historical`: evidence establishes a past state but does not establish that the state remains current.
- `Unknown`: current implementation cannot be established.

`Jurisdiction-specific` identifies a currently evidenced jurisdiction-dependent condition; it is not a substitute for timing. A past-only fact uses `Historical` and records the date or period it describes in `historical_as_of`. `last_verified` remains the date on which the evaluator checked the evidence, not the date when the historical condition existed.

`Deployed now` requires `deployment_evidence_state` to be exactly `Affirmative` and requires a nonblank `deployment_basis` identifying cited evidence of current operation within the row's scope. The controlled state is blank for every other implementation state. It records an affirmative evidence posture without implying independent verification. A generic product description, old contract, announced default, neighboring deployment, or unresolved current state cannot establish `Affirmative`.

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

The `evidence_label` records the row's evidentiary posture. `Verified`, `Vendor-asserted`, `Partially verifiable`, and `Unknown` describe how well the underlying fact is established. `Noncompliant` is reserved for evidence establishing failure against a cited binding obligation; it is not a confidence level. The `assessment` separately compares the supported facts with the OASPS requirement. These fields must not be combined.

Examples:

- An executed public contract can make a historical retention term `Verified`, while the assessment against a short-retention requirement may be `Does not meet`.
- A meaningful deletion design may be `Partially verifiable` and `Partly meets` because public evidence does not cover every backup or replica.
- A missing current configuration is `Unknown` and `Unknown`, not `Noncompliant`.

## Matrix semantic evidence fields

The matrix uses explicit fields to make cross-field reasoning reviewable rather than hiding it in free-form notes:

- `verified_fact` states the exact fact directly established by cited evidence when the row uses `Verified`; it distinguishes a verified document or statement from independently verified product behavior.
- `known_fact_basis` identifies the narrow, separately known fact sufficient for a definitive assessment when `Unknown` evidence is paired with `Meets`, `Partly meets`, or `Does not meet`. That combination requires at least one resolved `source_ids` value; `known_fact_basis` is blank for every other combination.
- `deployment_basis` identifies affirmative evidence for `Deployed now`; it is not satisfied by a policy promise or a capability description alone.
- `deployment_evidence_state` is the conditional controlled field `Affirmative` exactly when cited `deployment_basis` evidence supports current-in-scope deployment. It is blank for every other implementation state and does not imply independent verification.
- `historical_as_of` records the ISO date established by a `Historical` row.
- `applicability_reason` explains why `Not applicable` is the correct comparison rather than `Unknown` and states what the context row does and does not assess.
- `binding_obligation` identifies the specific applicable legal, contractual, or other enforceable duty required before `Noncompliant` may be used; the obligation must be supported by `source_ids`.
- `actor_override_reason` explains why a case-study row assigns a different responsible actor from the corresponding standard requirement without reassigning the standard itself.

These fields enforce several invariants. `Verified` requires `verified_fact`, which is blank for every other evidence label. `Unknown` evidence paired with `Meets`, `Partly meets`, or `Does not meet` requires `known_fact_basis` and at least one resolved `source_ids` value; `known_fact_basis` is blank for every other combination. An ordinary `Unknown` evidence plus `Unknown` assessment row remains source-optional. `Deployed now` requires `deployment_evidence_state` to be exactly `Affirmative` and requires a nonblank `deployment_basis`; both fields are blank for every other implementation state. `Affirmative` means the cited basis supports current-in-scope deployment and does not imply independent verification. `Historical` requires `historical_as_of`, which is blank for every other state, and cannot imply current operation. `Not applicable` requires `applicability_reason`, which is blank for every other assessment. `Noncompliant` requires `binding_obligation`, which is blank for every other evidence label. An actor difference requires `actor_override_reason`, which is blank when the row and standard actors match. Blank required justification is not neutral evidence; when a required fact cannot be established, the row remains `Unknown` or uses the narrower supported label.

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

- Consequential factual narrative sections are explicitly bounded by `<!-- oasps-citations:start -->` and `<!-- oasps-citations:end -->`.
- Inside a bounded section, each factual prose paragraph or list item ends with one or more supporting source IDs in brackets, such as `[SRC-0010]` or `[SRC-0010, SRC-0016]`.
- Every cited source ID must resolve to exactly one source-register row.
- The cited source must support the claim immediately before it.
- Multiple IDs in `matrix.csv` are pipe-separated, such as `SRC-0010|SRC-0016`.
- Short quotations are used only when necessary. Paraphrase is preferred.
- A vendor source proves the vendor's public statement, not the complete production implementation.
- A factual claim without a recoverable source is removed from narrative findings or preserved as an explicit unresolved question.

An intentionally nonfactual block inside a bounded section may be exempted only by an immediately preceding comment in the exact form `<!-- oasps-citation-exempt: reason -->`. The controlled reasons are `normative`, `methodological`, `editorial`, `question`, and `navigation`. The comment applies only to the next paragraph or list block. It cannot exempt a factual claim, and it cannot be used as a blanket exception for a section. This explicit convention makes citation enforcement deterministic without pretending software can infer whether arbitrary prose is factual.

The validator uses an explicit manifest of the repository's current evidence-bearing narrative files. CI requires each manifest file to contain at least one balanced citation section and validates prose paragraphs, contiguous list items, controlled exemptions, and source IDs inside marked sections. Files outside the manifest are not required to contain markers. CI does not classify arbitrary prose, prove that every factual sentence falls inside a marked section, or determine that a cited source substantively supports the claim. Human pull-request review remains responsible for section-boundary completeness and evidentiary sufficiency.

## Legal floor and independent verifiability

Case studies keep two questions distinct:

1. Does available evidence establish compliance with an applicable statute, regulation, binding contract, or local policy?
2. Can the public or a genuinely independent reviewer establish rights-relevant behavior from evidence that does not depend primarily on agency or vendor assertion?

A deployment may be legally compliant and independently under-verifiable. Conversely, transparency alone does not establish legal compliance. OASPS is not legal advice and does not issue legal conclusions beyond careful summaries of cited materials.

## Public inspectability and restricted review

OASPS-E01 treats public inspectability as the default for rights-relevant data schemas, collected and derived fields, authorization and access-control logic, audit-event semantics, retention and deletion behavior, sharing controls, inference and correlation behavior, prohibited-use enforcement, configuration and change semantics, and the evidence needed to test them. Confidential auditor access is not a permanent substitute merely because implementation is proprietary.

Restricted auditor-only access may supplement or temporarily replace public disclosure for a component only when every E01 condition is established: a concrete component-specific security risk rather than trade-secret status alone; approval by an independent public authority; public identification of the withheld scope and general reason; a time limit and periodic review; complete enforceable access for qualified independent reviewers; and public methods, scope, findings, exceptions, remediation status, and retest results to the greatest lawful extent. The restriction cannot hide whether a safeguard exists or operates.

Case studies assess each condition separately. Evidence of a confidential security assessment may establish that some review occurred without establishing rights-focused scope, independence, complete access, public-authority approval, time limitation, public reporting, or production correspondence. Missing proof remains `Unknown`; it is not converted into misconduct, illegality, or proof that a safeguard is absent.

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
5. populate each conditional semantic field only when its trigger applies: `verified_fact`, `known_fact_basis`, `deployment_basis`, `deployment_evidence_state`, `historical_as_of`, `applicability_reason`, `binding_obligation`, or `actor_override_reason`;
6. assign one evidence label, one assessment, and one implementation state only after checking their cross-field invariants;
7. record the last-verified date and supporting source IDs;
8. state the unresolved question and next lawful evidence action;
9. check the narrative wording against the row and cited source;
10. run the repository tests and `python scripts/validate.py` before handoff.

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

OASPS `0.4.0-draft.1` has not completed independent privacy, public-law, or software-assurance review. Its recognized-framework crosswalks are interpretive and do not establish formal conformity. The Flock case study is a dated evidence review of a defined ALPR scope, not an evaluation of every Flock product or every customer deployment. The Fairfield inventory is a system-discovery record, not a requirement-by-requirement assessment.
