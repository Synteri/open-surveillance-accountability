# Glossary

This glossary uses plain language for terms that appear in the standard and case study. Definitions describe how OASPS uses each term; they are not legal conclusions or universal industry definitions.

## Agency

The government department, authority, or other public body that buys, operates, configures, or uses a surveillance system.

## ALPR

**Automated license plate reader.** A camera-and-software system that captures images of vehicles or plates and creates searchable observations that commonly include a plate interpretation, time, and location. Systems may also create vehicle descriptors or other derived information.

## Announced or future

An implementation state for a control or behavior that has been promised, scheduled, or is rolling out but is not established as universally deployed in the evaluated scope.

## Applicability reason

The `applicability_reason` field explaining why an OASPS requirement does not apply to the row's stated subject, actor, or jurisdiction. It is required for `Not applicable`, blank for every other assessment, and cannot be replaced by missing evidence, which is `Unknown`.

## Assessment

The evaluator's comparison between observed behavior and an OASPS requirement: `Meets`, `Partly meets`, `Does not meet`, `Unknown`, or `Not applicable`. It is separate from confidence in the evidence.

## Actor override reason

The `actor_override_reason` field explaining why a case-study row assigns a different responsible actor from the corresponding requirement in `STANDARD.md`. It is present exactly when the actors differ and narrows the row's scope; it does not silently change the standard's actor assignment.

## Audit event

A record that a consequential action or change occurred, such as a search, export, share, role change, retention change, vendor access, or legal hold.

## Audit log

An ordered set of audit events used to reconstruct who did what, when, under what stated purpose, and with what result. An accountability-grade log should resist alteration and preserve enough context for meaningful review.

## Backup

A copy retained to restore data or service after loss. A deletion claim is incomplete if it does not explain whether and when deleted data disappears from backups.

## Binding obligation

The specific applicable statute, regulation, contract term, order, or other enforceable duty identified in `binding_obligation` and supported by the row's `source_ids`. The field is present for `Noncompliant` and blank for every other evidence label; falling short of OASPS alone is not enough.

## Case code

An identifier that links a search or action to an investigation, incident, or other authorized matter. A case code may improve reviewability but does not by itself prove the case exists or the search was lawful.

## Citation-bounded section

A factual narrative region between `<!-- oasps-citations:start -->` and `<!-- oasps-citations:end -->`. Each factual paragraph or list item inside the region ends with source IDs that support the immediately preceding claim.

## Citation exception

An immediately preceding comment in the form `<!-- oasps-citation-exempt: reason -->` that exempts only the next genuinely nonfactual paragraph or list block inside a citation-bounded section. Allowed reasons are `normative`, `methodological`, `editorial`, `question`, and `navigation`; the exception cannot be used for a factual claim.

## Confidence value

A number or category expressing how certain a system is about a machine-generated interpretation, such as a plate reading or vehicle attribute.

## Control plane

The administrative layer used to configure a system: users, roles, sharing relationships, retention, search filters, enabled features, legal holds, integrations, and similar settings. Control-plane activity can change rights-relevant behavior without changing an ordinary user's search screen.

## Cross-agency sharing

An arrangement that allows one agency to access, query, receive, or otherwise use data associated with another agency or network.

## Deployment basis

The `deployment_basis` field identifying the cited evidence that affirmatively supports current operation within the row's scope. It is required for `Deployed now` and blank for every other implementation state. A policy promise, old contract, product capability, or neighboring deployment does not by itself justify `Deployed now`.

## Deployment evidence state

The conditional controlled matrix field `deployment_evidence_state`. Its only nonblank value is `Affirmative`, required exactly when `implementation_state` is `Deployed now` and blank for every other implementation state. It means the cited `deployment_basis` affirmatively supports current-in-scope deployment; it does not imply independent verification.

## Deployed configuration

The version and settings actually operating for the evaluated subject. It is distinct from a vendor's generic capability, recommended default, or written policy.

## Deployment attestation

Cryptographic or equivalent evidence linking reviewed software and configuration to the version operating in production for a defined system or jurisdiction.

## Derived attribute

Information created from raw observations, such as a vehicle type, color, likely association, recurring pattern, route, convoy relationship, or confidence score.

## Documentation integrity

The ability to determine what a rights-relevant public document said, when it took effect, how it changed, and which deployed versions or customers it describes.

## Evidence label

The record's evidentiary posture. `Verified`, `Vendor-asserted`, `Partially verifiable`, and `Unknown` describe how well an underlying fact is established. `Noncompliant` is reserved for a sourced finding that an identified binding obligation was not met; it is not a confidence level.

## Evidence preservation

A case-linked process that keeps selected records for an active investigation or legal duty while ordinary data continues to expire under its normal retention rule. The process should have authorization, audit, expiry, and deletion controls.

## Export

A copy of data removed from the ordinary application interface, for example as a file, report, API response, or transfer to another system. Exports may have different retention and deletion behavior from the original record.

## Hot list

A list of plates or vehicle identifiers that can trigger an alert when a system records a possible match. The list's source, legal basis, accuracy, duration, and update history affect accountability.

## Historical

An implementation state for a past condition established by evidence that does not establish the condition remains current. A historical row must identify the relevant past date or period in `historical_as_of`.

## Historical as of

The ISO date in `historical_as_of` when a `Historical` row's condition existed. It is required for `Historical`, blank for every other implementation state, and differs from `last_verified`, which records when the evaluator checked the evidence.

## Independent oversight

Review performed by a body that is meaningfully separate from the agency or vendor whose conduct is being evaluated and has sufficient access, authority, competence, and freedom from conflicts.

## Independent public authority

A public body with legal independence, relevant competence, and authority to approve, time-limit, and periodically review a component-specific restriction on public inspectability. A vendor, customer, or confidential reviewer does not qualify merely by declaring itself independent.

## Independent verification

Evidence an external reviewer can check without relying exclusively on the statement of the actor responsible for the behavior. Independence is contextual: a cybersecurity audit may not evaluate civil-liberties use controls.

## Legal hold

A direction to preserve specific information that would otherwise be deleted, usually because of litigation, investigation, or another legal duty.

## Known fact basis

The `known_fact_basis` field identifying the narrow, separately known fact sufficient for a definitive assessment when an `Unknown` evidence label is paired with `Meets`, `Partly meets`, or `Does not meet`. It is blank for every other evidence/assessment combination and must not turn partial, indexed-only, unavailable, or broken-link evidence into a stronger fact.

## Least privilege

Giving a person, service, or integration only the access needed for its authorized function, for no longer than needed.

## Local policy

A rule adopted by an agency, municipality, governing board, or other jurisdiction-specific authority. A local policy may be stricter than a vendor's national default.

## Machine-learning ingestion

The movement of customer-derived or system-generated data into a process used to train, tune, evaluate, or improve a machine-learning model.

## Metadata

Information about an observation rather than its main visible content, such as time, location, camera identifier, user, confidence, or system version.

## Noncompliant

An evidence label used only when available evidence establishes failure against an identified binding legal, contractual, or policy obligation. Falling short of a proposed OASPS requirement is not automatically legal noncompliance.

## Optional or customer-configurable

An implementation state in which a capability exists but a customer or administrator determines whether or how it operates.

## Pattern-of-life analysis

Inferring routines, relationships, or recurring behavior by combining observations across time, place, or systems.

## Privacy-preserving audit event

A record designed to show that a consequential action occurred without retaining unnecessary sensitive content. For example, a blocked prohibited search could record the user, time, rule triggered, and review outcome without preserving the prohibited target.

## Production identity

Evidence of the exact software, model, policy, and configuration version serving real users at a given time.

## Purpose limitation

Restricting collection, search, sharing, and reuse to defined and authorized purposes instead of allowing unrelated later use.

## Public inspectability

The default OASPS-E01 condition in which the public can examine rights-relevant data schemas, collected and derived fields, authorization and access-control logic, audit-event semantics, retention and deletion behavior, sharing controls, inference and correlation behavior, prohibited-use enforcement, configuration and change semantics, and test evidence closely enough to understand and challenge whether safeguards exist and operate.

## Replica

An operational copy of data maintained for availability, performance, search, or geographic distribution. Replicas may be distinct from backups and must be considered in deletion claims.

## Responsible actor

The actor able and obligated to satisfy a requirement: `Vendor`, `Agency`, `Legislature`, `Court`, `Independent oversight`, or `Shared`.

## Restricted auditor-only access

A temporary, component-specific exception to public inspectability under OASPS-E01. It is permitted only when every E01 condition is established, including concrete security risk, independent-public-authority approval, public scope and general reason, time limit and review, complete enforceable qualified-reviewer access, and public reporting to the greatest lawful extent. Trade-secret status alone is insufficient.

## Retention

How long data remains available before ordinary deletion, including any different period for exports, evidence preservation, backups, replicas, indexes, or legal holds.

## Rights-relevant

Capable of materially affecting privacy, civil rights, civil liberties, access to remedy, or the public's ability to understand and challenge government surveillance.

## Search filter

A product or policy control that blocks, limits, or flags searches matching a prohibited category or rule.

## Secondary use

Use of collected data for a purpose beyond the original public-agency task, such as product improvement, model training, analytics, or unrelated investigation.

## Source ID

A stable identifier in the format `SRC-####` that connects a claim to one row in the repository's source register.

## Tamper-resistant

Designed so unauthorized alteration or deletion is prevented, made difficult, or reliably detectable. It does not mean that no authorized change is possible.

## Trajectory reconstruction

Combining location-and-time observations to infer the route or movement of a vehicle or person. It can occur retrospectively even when no single camera continuously follows a subject.

## Transparency portal

A public interface through which a vendor or agency may publish policy, retention, sharing, usage aggregates, or audit information. The fields and history exposed publicly may differ from internal records.

## Vendor-asserted

An evidence label meaning the vendor publicly states a behavior but complete implementation is not independently established.

## Vendor-privileged access

Access by vendor personnel or services beyond ordinary agency-user permissions, often for support, maintenance, security, or system administration.

## Verified fact

The exact fact directly established by cited evidence and recorded in `verified_fact` when a matrix row uses the evidence label `Verified`. It distinguishes a verified document or published statement from independently verified product behavior, stays within the cited evidence's subject, date, jurisdiction, and retrieval limits, and is blank for every other evidence label.

## Versioned public change history

An immutable or reliably archived record of changes to rights-relevant documentation or behavior, including versions, effective dates, and deployment scope.
