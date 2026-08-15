# Open Accountability Standard for Public Surveillance Systems

**Version:** OASPS `0.3.0-draft.1`

**Status:** Open draft for private bootstrap review  
**Last substantive research review:** 2026-08-14

OASPS is a proposed vendor-neutral accountability standard. It is not accredited, certified, expert-approved, or a legal determination. Its requirements are written so residents, public bodies, vendors, and independent reviewers can identify the responsible actor and the evidence that would demonstrate implementation.

The standard states what any public surveillance system should do. It contains no Flock-specific finding; those belong in the separate case study.

## How requirements are structured

Each requirement includes:

- **Requirement:** the testable behavior OASPS proposes;
- **Why it matters:** the public-interest risk addressed;
- **Responsible actor:** `Vendor`, `Agency`, `Legislature`, `Court`, `Independent oversight`, or `Shared`;
- **Expected proof:** evidence that could demonstrate the behavior rather than merely assert it;
- **Recognized basis:** established frameworks or guidance that support the general direction;
- **OASPS extension:** the surveillance-specific element, especially where OASPS goes beyond recognized frameworks.

Recognized bases are interpretive anchors, not claims of formal conformity. See the [crosswalks](standard/crosswalks/README.md) and [methodology](METHODOLOGY.md).

## A — Data inventory and derivation

### OASPS-A01 — Public data inventory

**Requirement:** The operator and vendor publish a complete, versioned inventory of raw data, metadata, derived attributes, confidence values, transformations, and retention classes the system creates or uses. The inventory identifies whether each item is collected, derived, searchable, displayed, exported, shared, or used internally.

**Why it matters:** People cannot evaluate a surveillance system when consequential data products are undisclosed or scattered across incomplete product descriptions.

**Responsible actor:** Shared

**Expected proof:** Public schema, field dictionary, data-flow documentation, retention mapping, version history, and independently reviewable implementation evidence.

**Recognized basis:** NIST Privacy Framework 1.0; Convention 108+; ISO/IEC 27701:2025 privacy-management principles.

**OASPS extension:** Explicit inventory of surveillance-derived attributes, confidence values, internal-use fields, and cross-system correlation.

### OASPS-A02 — Derivation and correlation transparency

**Requirement:** The vendor publishes a plain-language and technically meaningful explanation of enrichment, hot-list matching, machine-learning inference, confidence handling, and cross-camera or cross-network correlation, including inputs, outputs, known limitations, and consequential error modes.

**Why it matters:** Derived conclusions can affect people even when the underlying observations appear routine.

**Responsible actor:** Vendor

**Expected proof:** Versioned technical documentation, model or system cards where applicable, representative test cases, threshold and confidence documentation, and authorized independent evaluation.

**Recognized basis:** NIST Privacy Framework 1.0; Convention 108+ transparency and accountability principles; ISO/IEC 27701:2025.

**OASPS extension:** Surveillance-specific disclosure of trajectory, association, pattern, and network-level inference.

### OASPS-A03 — Completeness and pre-use disclosure

**Requirement:** The operator and vendor prohibit operational use of undisclosed rights-relevant data categories or derived attributes. A new category or derivation is documented, reviewed, and publicly disclosed before deployment unless a narrowly defined lawful exception applies.

**Why it matters:** A public inventory has little value if consequential fields can be introduced without notice or review.

**Responsible actor:** Shared

**Expected proof:** Binding policy and contract terms, release gates, change approvals, schema-diff records, and audit evidence showing when new fields became available.

**Recognized basis:** NIST Privacy Framework 1.0 accountability and transparency; Convention 108+ controller accountability; ISO/IEC 27701:2025 change and privacy governance.

**OASPS extension:** An enforceable completeness commitment and pre-deployment disclosure for surveillance-derived capabilities.

### OASPS-A04 — Consequential capability semantics

**Requirement:** The vendor defines rights-relevant capability terms such as “tracking,” “real-time,” “pattern,” “association,” and “deconfliction,” and explains what inferences can be produced from repeated observations even when the system does not continuously follow a person or vehicle.

**Why it matters:** Vague terminology can hide the practical difference between a single observation and retrospective trajectory or association analysis.

**Responsible actor:** Vendor

**Expected proof:** Versioned glossary, capability matrix, representative outputs, boundary tests, and documentation connecting marketing and policy terms to actual system behavior.

**Recognized basis:** General transparency and accountability principles in NIST Privacy Framework 1.0, Convention 108+, and ISO/IEC 27701:2025.

**OASPS extension:** A surveillance-specific semantic requirement distinguishing continuous tracking from movement-pattern, association, and trajectory inference.

## B — Purpose limitation and access

### OASPS-B01 — Individual identity and least privilege

**Requirement:** Every human and service account is individually attributable and receives only the access needed for its approved role. Shared credentials are prohibited except for narrowly controlled emergency arrangements.

**Why it matters:** Misuse cannot be prevented or investigated when access is anonymous or broader than necessary.

**Responsible actor:** Shared

**Expected proof:** Authentication design, role definitions, user and service-account inventory, access reviews, privileged-access records, and independent control testing.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, Access Control and Identification and Authentication families; NIST Privacy Framework 1.0; Convention 108+.

**OASPS extension:** Applies attribution and least privilege to agency users, administrators, integrations, and vendor-privileged access.

### OASPS-B02 — Structured search purpose

**Requirement:** Every search or other investigative query includes a structured, reviewable purpose selected or entered before results are returned.

**Why it matters:** A declared purpose creates an accountability predicate that can be reviewed against policy and law.

**Responsible actor:** Shared

**Expected proof:** Required-purpose interface, permitted-purpose vocabulary, query logs linking purpose to user and time, bypass rules, and sampled independent review.

**Recognized basis:** NIST Privacy Framework 1.0 purpose limitation; Convention 108+ lawfulness and proportionality; IACP and BJA ALPR policy guidance.

**OASPS extension:** A mandatory purpose record attached to every surveillance query.

### OASPS-B03 — Case-linked investigative searches

**Requirement:** Investigative searches are linked to a case, incident, or other independently reviewable lawful predicate. Narrow emergency exceptions are time-limited and automatically flagged for prompt review.

**Why it matters:** A general purpose label alone may not establish that a real investigation supports the search.

**Responsible actor:** Shared

**Expected proof:** Enforced case or incident field, validation rules, emergency-bypass records, supervisory review, and samples linked to valid agency records.

**Recognized basis:** Purpose limitation and accountable-use principles in NIST Privacy Framework 1.0, Convention 108+, and ALPR operational guidance.

**OASPS extension:** Explicit case linkage and automatic review of emergency exceptions.

### OASPS-B04 — Protected activity and prohibited uses

**Requirement:** Public law or policy defines prohibited purposes, including surveillance of constitutionally or otherwise legally protected activity without an individualized lawful predicate, and the operator and vendor implement enforceable controls consistent with those prohibitions.

**Why it matters:** Surveillance can chill lawful speech, association, travel, health care, or other protected activity when use limits are vague or voluntary.

**Responsible actor:** Shared

**Expected proof:** Statute, binding policy, contract restrictions, technical filters, exception rules, training, attempted-use records, and independent compliance review.

**Recognized basis:** Convention 108+ lawfulness, proportionality, and independent supervision; NIST Privacy Framework 1.0; IACP and BJA ALPR civil-rights guidance.

**OASPS extension:** Explicit protected-activity safeguards tied to both policy and enforceable technical controls.

### OASPS-B05 — Explicit external sharing

**Requirement:** External access or sharing is disabled unless expressly authorized for a stated purpose, scope, recipient, and duration. Operators publish current sharing relationships and no vendor or agency silently creates automatic access.

**Why it matters:** Sharing can expand a local surveillance system into a much larger network without meaningful local awareness or approval.

**Responsible actor:** Shared

**Expected proof:** Sharing policy, recipient and network inventory, approval records, time limits, configuration export, change logs, revocation records, and independent review.

**Recognized basis:** Convention 108+ data-flow safeguards; NIST Privacy Framework 1.0; NIST SP 800-53 Rev. 5, Release 5.2.0, Access Control family; ALPR dissemination guidance.

**OASPS extension:** Publicly inspectable surveillance-sharing topology and a prohibition on hidden or automatic access.

## C — Auditability

### OASPS-C01 — Complete use and data-action logs

**Requirement:** The system creates tamper-resistant records for searches, exports, alerts, hot-list actions, API and integration access, administrative data access, and vendor-privileged data access.

**Why it matters:** Consequential use cannot be reconstructed when important data actions leave no durable evidence.

**Responsible actor:** Shared

**Expected proof:** Canonical audit-event schema, immutable or tamper-evident records, administrator-separation controls, sample exports, integrity tests, and independent completeness testing.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, Audit and Accountability family; NIST SP 800-53A Rev. 5, Release 5.2.0; ISO/IEC 27701:2025 accountability.

**OASPS extension:** Explicit coverage of vendor, API, export, alert, and surveillance-specific data actions.

### OASPS-C02 — Control-plane observability

**Requirement:** The system logs every rights-relevant configuration change, including sharing, retention, filters, feature enablement, hot lists, user roles, vendor privileges, evidence preservation, and legal holds.

**Why it matters:** A safe written policy does not reveal whether configuration changes silently altered actual behavior.

**Responsible actor:** Shared

**Expected proof:** Versioned configuration history, actor and timestamp for every change, before-and-after values, tamper-evidence, customer-accessible exports, and independent completeness tests.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, Configuration Management and Audit and Accountability families; NIST SP 800-53A Rev. 5, Release 5.2.0, assessment concepts.

**OASPS extension:** Complete rights-relevant surveillance control-plane evidence, including vendor and local configuration changes.

### OASPS-C03 — Privacy-preserving prohibited-attempt logs

**Requirement:** When the system blocks a prohibited search or action, it records a tamper-resistant audit event sufficient to identify the actor, rule triggered, time, and review path without retaining unnecessary sensitive query content.

**Why it matters:** Blocking misuse protects the target, but recording no event can prevent oversight from detecting attempted misuse.

**Responsible actor:** Vendor

**Expected proof:** Blocked-action event schema, privacy design, sample records, retention rule, alert and review workflow, and authorized independent testing.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, Audit and Accountability concepts.

**OASPS extension:** A surveillance-specific balance between preventing a prohibited query and preserving privacy-safe evidence of the attempt.

### OASPS-C04 — Audit evidence retention

**Requirement:** Audit evidence is retained long enough for meaningful supervisory, public-record, judicial, and independent review, with a published retention period for each event class.

**Why it matters:** Logs that disappear before an investigation or audit begins cannot provide accountability.

**Responsible actor:** Shared

**Expected proof:** Event-class retention schedule, storage and deletion controls, legal-hold rules, public-view duration, internal-view duration, and independent operating-effectiveness tests.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, Audit and Accountability; NIST SP 800-53A Rev. 5, Release 5.2.0; ISO/IEC 27701:2025 accountability.

**OASPS extension:** Separates internal audit retention from the shorter history that may appear on a public portal.

### OASPS-C05 — Complete independent audit access

**Requirement:** A genuinely independent auditor can inspect the complete rights-relevant audit record under enforceable access rights, subject to proportionate safeguards, rather than receiving only agency- or vendor-selected excerpts.

**Why it matters:** Selective evidence cannot establish that logging is complete or that misuse and configuration changes are handled consistently.

**Responsible actor:** Shared

**Expected proof:** Auditor mandate, access terms, full event inventory, unfiltered export mechanism, sampling protocol, findings, exceptions, and published disposition where lawful.

**Recognized basis:** NIST SP 800-53A Rev. 5, Release 5.2.0, assessment methodology; Convention 108+ independent supervision; ISO/IEC 27701:2025 accountability.

**OASPS extension:** Rights-focused access to complete use and control-plane evidence, beyond ordinary cybersecurity assurance.

### OASPS-C06 — Privacy-preserving public reporting

**Requirement:** Operators publish recurring, privacy-preserving aggregate reports detailed enough to show use volume, purpose categories, sharing, alerts, retention, blocked actions, audit findings, and material policy drift.

**Why it matters:** The public needs meaningful visibility without publication of plate data, travel histories, or other sensitive records.

**Responsible actor:** Shared

**Expected proof:** Public portal or reports, reporting schema, update schedule, historical archive, privacy review, and reconciliation to internal audit totals.

**Recognized basis:** NIST Privacy Framework 1.0 transparency; Convention 108+ transparency and accountability; ALPR policy guidance.

**OASPS extension:** Aggregate reporting designed to detect surveillance-policy drift while protecting individuals.

## D — Data lifecycle

### OASPS-D01 — Data minimization by default

**Requirement:** The system collects and retains only the data necessary for a defined, authorized purpose, and the safest reasonable settings are the default rather than optional.

**Why it matters:** Population-scale surveillance risk grows with unnecessary fields, reach, and duration.

**Responsible actor:** Shared

**Expected proof:** Data-minimization analysis, default configuration, disabled-by-default features, field and retention rationale, and deployment configuration evidence.

**Recognized basis:** NIST Privacy Framework 1.0; Convention 108+ data minimization and proportionality; ISO/IEC 27701:2025.

**OASPS extension:** Applies minimization to surveillance defaults, derived fields, and network-scale capabilities.

### OASPS-D02 — Short, deployment-specific retention

**Requirement:** Ordinary surveillance data has a short default retention period. Every jurisdiction-specific override is explicitly approved and disclosed through a timestamped record of the actual deployed setting.

**Why it matters:** Generic vendor policy cannot establish how long a particular community's data is retained.

**Responsible actor:** Shared

**Expected proof:** Default policy, local approval, contract term, current configuration export, configuration-change history, and public retention statement.

**Recognized basis:** NIST Privacy Framework 1.0; Convention 108+ proportionality and minimization; ISO/IEC 27701:2025; ALPR retention and purging guidance.

**OASPS extension:** Requires a deployment-specific configuration record rather than inference from vendor-wide prose.

### OASPS-D03 — Separate evidence preservation

**Requirement:** Records needed for a specific investigation or legal duty are preserved through a separate, case-linked process rather than by extending ordinary population-scale retention.

**Why it matters:** Legitimate evidence needs do not justify retaining everyone's observations for longer periods.

**Responsible actor:** Shared

**Expected proof:** Case-linked preservation workflow, authorization and expiry rules, preserved-record inventory, legal-hold audit trail, and deletion after the preservation purpose ends.

**Recognized basis:** Data minimization, purpose limitation, and retention principles in NIST Privacy Framework 1.0, Convention 108+, and ALPR guidance.

**OASPS extension:** Explicit technical and governance separation between evidence preservation and ordinary surveillance retention.

### OASPS-D04 — Verifiable deletion across storage paths

**Requirement:** Deletion removes or irreversibly renders inaccessible the covered data from primary stores, replicas, backups, caches, derived indexes, exports under vendor control, and other recovery paths, subject only to documented lawful holds.

**Why it matters:** A nominal deletion date is misleading if the data remains recoverable elsewhere.

**Responsible actor:** Shared

**Expected proof:** Storage map, lifecycle configuration, deletion events, backup and replica rules, recovery tests, legal-hold records, and independent operating-effectiveness assessment.

**Recognized basis:** NIST Privacy Framework 1.0; Convention 108+ retention limitation; ISO/IEC 27701:2025 lifecycle governance.

**OASPS extension:** Explicit proof covering replicas, backups, derived indexes, caches, evidence stores, and legal holds.

### OASPS-D05 — Narrow secondary and machine-learning use

**Requirement:** Secondary use, product improvement, and machine-learning ingestion are separately disclosed, purpose-limited, narrowly authorized, logged, and prohibited unless an enforceable legal or contractual basis permits them.

**Why it matters:** Data collected for public safety should not silently become general product-development or model-training material.

**Responsible actor:** Shared

**Expected proof:** Binding contract and policy, data-flow and ingestion inventory, consent or authorization record, de-identification tests, access and ingestion logs, retention rules, and independent review.

**Recognized basis:** NIST Privacy Framework 1.0 purpose limitation; Convention 108+ lawfulness and compatible use; ISO/IEC 27701:2025.

**OASPS extension:** Explicit surveillance-data and model-training governance, including ingestion observability.

### OASPS-D06 — Contract-to-policy consistency

**Requirement:** Enforceable contracts, licenses, and product terms do not grant materially broader rights over surveillance data than public policies and privacy promises describe. Conflicts are resolved in favor of the narrower publicly accountable use before deployment.

**Why it matters:** A reassuring public explanation is not controlling when the contract permits substantially broader use.

**Responsible actor:** Shared

**Expected proof:** Clause-level comparison of contract, policy, product documentation, and local authorization; revision history; conflict-resolution rule; and independent legal or procurement review.

**Recognized basis:** General accountability, transparency, and demonstrable-governance principles in ISO/IEC 27701:2025, NIST Privacy Framework 1.0, and Convention 108+.

**OASPS extension:** An explicit enforceable alignment test between public promises and contractual data rights.

## E — Software and deployment verifiability

### OASPS-E01 — Publicly inspectable rights-relevant implementation

**Requirement:** Public inspectability is the default for rights-relevant data schemas; collected and derived fields; authorization and access-control logic; audit-event semantics; retention and deletion behavior; sharing controls; inference and correlation behavior; prohibited-use enforcement; configuration and change semantics; and the evidence needed to test those behaviors. Restricted auditor-only access may supplement or temporarily replace public disclosure for a component only when a concrete security risk—not trade-secret or proprietary status alone—justifies the restriction; an independent public authority approves it; the withheld scope and general reason are public; the restriction is time-limited and periodically reviewed; qualified independent reviewers receive complete, enforceable access; and the review's methods, scope, findings, exceptions, remediation status, and retest results are public to the greatest lawful extent. A restriction cannot conceal whether a safeguard exists or operates.

**Why it matters:** Policy promises and confidential review alone cannot give the public durable accountability when consequential safeguards and inferences remain indefinitely hidden or when the existence and operation of a safeguard cannot be checked.

**Responsible actor:** Vendor

**Expected proof:** Public schemas, source, rules, semantics, behavior descriptions, build material, and test evidence for the listed rights-relevant components. For each temporary restricted component: the concrete security-risk finding; independent-public-authority approval; public withheld-scope and general-reason notice; start, end, and periodic-review records; complete enforceable reviewer-access terms; and public methods, scope, findings, exceptions, remediation status, and retest results to the greatest lawful extent.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, assurance, System and Services Acquisition, and System and Information Integrity concepts; NIST SP 800-53A Rev. 5, Release 5.2.0, assessment discipline.

**OASPS extension:** Public inspectability as the default, plus a conjunctive and independently governed test for temporary component-specific restriction. The cited frameworks do not themselves establish this exact disclosure rule, which requires specialist public-law, security, and implementation review.

### OASPS-E02 — Published interfaces and data flows

**Requirement:** The vendor publishes interfaces and end-to-end data-flow documentation sufficient to understand consequential collection, transformation, access, sharing, retention, deletion, and secondary use.

**Why it matters:** Reviewers cannot test rights-relevant behavior without knowing where data enters, changes, moves, and leaves.

**Responsible actor:** Vendor

**Expected proof:** Versioned architecture and data-flow diagrams, API specifications, integration inventory, trust boundaries, event mapping, and independently reviewed correspondence to implementation.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, System and Services Acquisition, Configuration Management, and privacy-transparency concepts.

**OASPS extension:** A public rights-relevant data-flow view spanning vendor, agency, networks, APIs, and secondary use.

### OASPS-E03 — Reproducible or attestable builds

**Requirement:** Rights-relevant software components use reproducible builds where technically feasible or another independently testable process that identifies exactly what artifact was reviewed.

**Why it matters:** An audit of unidentified or unreconstructable software cannot be reliably repeated.

**Responsible actor:** Vendor

**Expected proof:** Source revision, dependency lock, build recipe, signed artifact digest, reproducibility result or documented alternative assurance, and independent test report.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, Configuration Management, System and Services Acquisition, and System Integrity assurance concepts.

**OASPS extension:** Reproducible or equivalent build identity for rights-relevant surveillance components; specialist validation is required before v1.0.

### OASPS-E04 — Production deployment attestation

**Requirement:** A cryptographic or comparably strong attestation links the reviewed software, model, policy configuration, and control set to the production deployment serving each jurisdiction.

**Why it matters:** A successful audit does not prove that the audited artifact or configuration is running in production.

**Responsible actor:** Vendor

**Expected proof:** Signed artifact and configuration identities, deployment attestations, jurisdiction mapping, change history, verifier procedure, and independent spot checks.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, Configuration Management, assessment, acquisition, and system-integrity concepts.

**OASPS extension:** Jurisdiction-specific production identity for rights-relevant code and configuration; this is a deliberately strict proposal requiring specialist review.

### OASPS-E05 — Versioned rights-relevant documentation

**Requirement:** Every public rights-relevant policy, specification, capability description, and configuration statement has a version, effective date, immutable archive, and machine-readable change history that distinguishes announced, rolling out, default-for-new, optional, and universally deployed behavior.

**Why it matters:** Readers cannot determine current behavior when live pages change silently or future promises are presented as deployed controls.

**Responsible actor:** Shared

**Expected proof:** Immutable document archive, effective dates, signed or hashed versions, machine-readable changelog, deployment-status vocabulary, and correspondence to local configuration.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, Configuration Management and accountability concepts; ISO/IEC 27701:2025 continual-improvement and governance principles.

**OASPS extension:** Treats public documentation integrity and deployment-state language as auditable rights-relevant controls.

### OASPS-E06 — Vulnerability disclosure and adversarial testing

**Requirement:** The vendor operates a coordinated vulnerability-disclosure process and permits recurring independent adversarial testing of security and rights-relevant safeguards, with tracked remediation and a public summary where lawful.

**Why it matters:** Complex systems need credible ways to discover and correct failures before they cause lasting harm.

**Responsible actor:** Vendor

**Expected proof:** Disclosure policy, safe-harbor terms, independent test scope, findings, remediation records, retest results, and a public summary that does not expose exploitable details.

**Recognized basis:** NIST SP 800-53 Rev. 5, Release 5.2.0, System and Information Integrity, Assessment/Authorization/Monitoring, and acquisition assurance concepts.

**OASPS extension:** Connects adversarial testing and remediation to rights-relevant safeguards as well as conventional cybersecurity.

## F — Governance and remedy

### OASPS-F01 — Explicit democratic authorization

**Requirement:** A public surveillance capability receives explicit, capability-specific authorization through an accountable democratic process before deployment or material expansion; procurement alone is insufficient.

**Why it matters:** Purchasing a tool should not silently decide major questions about public surveillance power.

**Responsible actor:** Shared

**Expected proof:** Statute, ordinance, public meeting record, approved policy, capability and risk disclosure, vote or delegated authorization, and records of later material-change review.

**Recognized basis:** Governance and accountability principles in Convention 108+, ISO/IEC 27701:2025, NIST Privacy Framework 1.0, and ALPR policy guidance.

**OASPS extension:** Capability-specific democratic authorization and renewed review for material expansion.

### OASPS-F02 — Independent oversight

**Requirement:** Oversight exists outside the agency operating the system and has authority, expertise, access, and resources to review rights-relevant use, configuration, contracts, and audit evidence.

**Why it matters:** Self-review alone cannot provide credible accountability for consequential surveillance powers.

**Responsible actor:** Independent oversight

**Expected proof:** Legal mandate, appointment and independence rules, access authority, audit plan, reports, findings, corrective actions, and public dispositions where lawful.

**Recognized basis:** Convention 108+ independent and effective supervision; ISO/IEC 27701:2025 accountability; NIST privacy-governance concepts.

**OASPS extension:** Complete rights/use and control-plane oversight, not merely cybersecurity or agency-selected review.

### OASPS-F03 — Oversight survives trade-secret claims

**Requirement:** Procurement and vendor contracts contain an enforceable public-interest oversight carveout so trade-secret or proprietary-rights claims cannot prevent qualified review of rights-relevant functionality.

**Why it matters:** Proprietary status should not make government surveillance behavior unreviewable.

**Responsible actor:** Shared

**Expected proof:** Contract clause, auditor access rights, confidentiality safeguards, dispute process, records-disclosure treatment, and evidence that qualified review can occur.

**Recognized basis:** General accountability and demonstrable-control principles in ISO/IEC 27701:2025, NIST Privacy Framework 1.0, and Convention 108+.

**OASPS extension:** An explicit procurement limit on trade-secret objections; this requires procurement and public-law review.

### OASPS-F04 — Restriction or suspension on material failure

**Requirement:** Material failure of a rights-relevant control triggers prompt restriction or suspension of the affected capability until the failure is contained, independently reviewed, and corrected.

**Why it matters:** A safeguard has little force when known serious failures can continue without operational consequence.

**Responsible actor:** Shared

**Expected proof:** Defined trigger criteria, automated and manual restriction controls, incident records, authority matrix, remediation plan, independent clearance, and restoration record.

**Recognized basis:** Accountability, corrective-action, monitoring, and continual-improvement concepts in NIST and ISO privacy and security frameworks.

**OASPS extension:** Mandatory operational consequences tied specifically to material surveillance-accountability failures; expert validation is required.

### OASPS-F05 — Meaningful penalties and remedies

**Requirement:** Intentional misuse, concealment, retaliation, and material control failures carry meaningful disciplinary, contractual, civil, judicial, or other lawful remedies for affected people and the public.

**Why it matters:** Rules without enforceable consequences or avenues for correction do not provide meaningful accountability.

**Responsible actor:** Shared

**Expected proof:** Statute, contract, policy, complaint process, investigation authority, available remedies, enforcement records, notice rules, and appeal or judicial-review path.

**Recognized basis:** Convention 108+ accountability and effective-supervision principles; ISO/IEC 27701:2025 governance; applicable law.

**OASPS extension:** Makes misuse and concealment remedies an explicit standard element; the exact legal form remains jurisdiction-specific and requires legal review.

## Interpretation and review gates

OASPS deliberately goes beyond recognized frameworks in several areas. Before version 1.0, the requirements for independent code access, reproducible builds, deployment attestation, complete vendor and control-plane logs, blocked-attempt evidence, mandatory suspension, trade-secret limits, and remedies need independent software-assurance, privacy, public-law, procurement, and public-safety review.

Objections should be recorded and resolved visibly. Review is voluntary and is not endorsement unless a reviewer explicitly says so.
