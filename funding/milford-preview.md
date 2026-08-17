# Milford ALPR assessment preview

**Review date:** 2026-08-16

**Scope:** five selected OASPS criteria
**Purpose:** show the form of a paid assessment without completing one for free

> **Illustrative preview only. This is not a completed independent assessment. It examines a small set of published records and policy commitments. It does not verify operational configuration, compliance, effectiveness, or the absence of safeguards for which public evidence has not been located.**

## Reading the preview

`Documented fact` means the cited source states or records the point. `Preliminary disposition` is a bounded interpretation of that evidence under the named OASPS criterion. `Missing evidence` identifies what the public source set does not establish. Missing evidence is not evidence that a safeguard is absent.

The paid assessment would apply all 32 criteria, test the evidence by layer, crosswalk current law and policy, issue targeted records requests, and publish both a readable report and machine-readable evidence output. This preview gives no overall score or conclusion.

## Evidence snapshot

<!-- oasps-citations:start -->
Milford's current Real Time Information Center page links both a Flock LPR transparency portal and a Milford Police ALPR policy. A 2025 traffic-enforcement procurement addendum also stated that Milford Police used Flock Safety for LPR technology, but that addendum concerned a separate automated traffic-enforcement program and does not establish the present LPR scope or configuration. [SRC-0053, SRC-0069]

The Milford policy describes query-purpose fields, case identifiers, sharing conditions, transaction records, quarterly audits, and a 30-day retention ceiling. Its displayed effective date reads `03/02/20026`, so this preview does not infer a corrected effective date or treat policy text as proof of implementation. [SRC-0054]

Connecticut Public reported a contentious August 3 meeting and later consideration of a moratorium. At review time, the official agenda center did not supply approved minutes that establish the exact motion, vote, conditions, or later meeting date. The city's regular-meeting schedule lists August 3 and September 14; circulating August 19 or August 27 dates remain `NEEDS_VERIFICATION` unless an official notice is produced. [SRC-0055, SRC-0072, SRC-0073]
<!-- oasps-citations:end -->

## Five-criterion preview

### 1. [OASPS-F01: explicit democratic authorization](../STANDARD.md#oasps-f01--explicit-democratic-authorization)

**Documented fact.**

<!-- oasps-citations:start -->
Milford publicly identifies an ALPR program, and a February 2026 Board of Finance record attributes to the police chief that a license-plate-reader expense was omitted from the proposed budget because the city remained within a current contract year. The record does not identify the vendor, amount, term, scope, locations, configuration, executed agreement, or original authorization chain. [SRC-0053, SRC-0071]
<!-- oasps-citations:end -->

**Preliminary disposition:** `Unknown`. The source set documents public acknowledgment and a contract-year reference, but it is insufficient to reconstruct the current authorization, procurement, renewal, inventory, and material-change history.

**Missing evidence:** executed contract and amendments; purchase orders and payments; approval minutes; current device and location inventory; renewal and material-change records. No absence is inferred.

**What the paid review would obtain and test:** the complete procurement and approval chain, then map each approved capability and change to the current deployment inventory.

### 2. [OASPS-B02: structured search purpose](../STANDARD.md#oasps-b02--structured-search-purpose)

**Documented fact.**

<!-- oasps-citations:start -->
The Milford policy requires individual credentials and says a user must enter a reason or offense and an associated case or incident number when querying the system. The public policy does not establish whether those fields are technically enforced, accurately completed, or checked against valid cases in current operation. [SRC-0054]
<!-- oasps-citations:end -->

**Preliminary disposition:** `Partly meets at the policy layer; operating state unknown`. The written rule creates a reviewable predicate, but implementation and purpose validity are not established.

**Missing evidence:** current interface configuration; required-field behavior; a lawfully reviewable sample tying reasons to valid cases; supervisor review and remediation records. No absence is inferred.

**What the paid review would obtain and test:** a configuration export and bounded audit sample, with sensitive content minimized, to test whether purpose fields are required, meaningful, and reviewed.

### 3. [OASPS-B05: explicit external sharing](../STANDARD.md#oasps-b05--explicit-external-sharing)

**Documented fact.**

<!-- oasps-citations:start -->
The Milford policy says the department will not opt into a national online ALPR database, limits access or sharing to law-enforcement purposes, and requires an out-of-state agency to declare that Connecticut statutory restrictions will be followed before sharing. The public source set does not establish Milford's current inbound or outbound network topology, reciprocal access, approvals, durations, or actual external searches. [SRC-0054]
<!-- oasps-citations:end -->

**Preliminary disposition:** `Partly meets at the policy layer; deployment state unknown`. The policy contains relevant restrictions, while present configuration and sharing history remain unverified.

**Missing evidence:** current sharing export; agency-by-agency authorizations; memoranda or agreements; change history; external-query records and review results. No absence or improper sharing is inferred.

**What the paid review would obtain and test:** the current sharing topology and change history, then compare each relationship with documented authority and applicable restrictions.

### 4. [OASPS-D02: short, deployment-specific retention](../STANDARD.md#oasps-d02--short-deployment-specific-retention)

**Documented fact.**

<!-- oasps-citations:start -->
The Milford policy sets a maximum 30-day retention period. Public Act 26-14, read with its later amendment in Public Act 26-76, creates staged statewide ALPR requirements, including a 21-day retention limit for the relevant provisions beginning October 1, 2026. The policy does not establish Milford's current production setting, deletion behavior, exports, backups, exceptions, or readiness for the later limit. [SRC-0054, SRC-0035, SRC-0037]
<!-- oasps-citations:end -->

**Preliminary disposition:** `Partly meets at the policy layer; current configuration unknown`. This is not a finding of present noncompliance.

**Missing evidence:** timestamped retention setting; configuration history; deletion logs; treatment of downloads, derived data, backups, and lawful holds; documented transition plan. No absence is inferred.

**What the paid review would obtain and test:** a current configuration record and deletion evidence, then crosswalk each retained copy and exception against the effective requirements at the relevant date.

### 5. [OASPS-C01: complete use and data-action logs](../STANDARD.md#oasps-c01--complete-use-and-data-action-logs)

**Documented fact.**

<!-- oasps-citations:start -->
The Milford policy calls for transaction records and quarterly audits. Have I Been Flocked reports importing 7,976 Milford organization-audit records covering January through November 2025, while also describing completeness, delay, and redaction limits. Those records concern database searches and do not establish vehicle passages, results, stops, investigations, full event coverage, audit completion, remediation, or current 2026 use. [SRC-0054, SRC-0076, SRC-0078]
<!-- oasps-citations:end -->

**Preliminary disposition:** `Policy partially addresses the criterion; historical records demonstrate some search logging; conformity remains unknown.` The records do not establish tamper resistance, event completeness, or coverage of exports, alerts, administration, APIs, or vendor access.

**Missing evidence:** canonical event inventory; current search, export, alert, sharing, role, configuration, administrator, and vendor-access logs; quarterly audit reports; completeness tests; findings and remediation. No absence is inferred.

**What the paid review would obtain and test:** the event schema, recent bounded logs, audit workpapers, and remediation records, with an explicit test of whether every rights-relevant action is attributable and reviewable.

## What this preview supports

This source set is sufficient to frame high-value questions and records requests. It is not sufficient to declare the Milford deployment compliant, noncompliant, safe, harmful, effective, or ineffective.

The [$5,000 Full Independent Assessment](offers.md#5000-full-independent-assessment-default) is the default paid path for completing the evidence collection, all-criterion analysis, records-request package, recommendations, public summary, and machine-readable output.

## Public source key

The bracketed source IDs above resolve directly here. Full access dates and source notes are in the repository's [source register](../evidence/sources.csv).

- [SRC-0035: Connecticut Public Act 26-14](https://www.cga.ct.gov/2026/act/pa/pdf/2026PA-00014-R00SB-00397-PA.pdf)
- [SRC-0037: Connecticut Public Act 26-76](https://www.cga.ct.gov/2026/act/Pa/pdf/2026PA-00076-R00SB-00477-PA.PDF)
- [SRC-0053: Milford Real Time Information Center](https://www.milfordct.us/921/Real-Time-Information-Center)
- [SRC-0054: Milford Police ALPR policy](https://www.milfordct.us/DocumentCenter/View/4089/Milford-Police-ALPR-Policy)
- [SRC-0055: Milford Board of Aldermen agenda center](https://www.milfordct.us/agendacenter)
- [SRC-0069: Milford RFP 1830 Addendum 1](https://www.milfordct.us/DocumentCenter/View/2338/RFP-1830---ADDENDUM-1---ATESD-Program-on-behalf-of-the-City-of-Milford-Police-Department-PDF)
- [SRC-0071: Milford February 17, 2026 Board of Finance minutes](https://www.milfordct.us/AgendaCenter/ViewFile/Minutes/_02172026-1707)
- [SRC-0072: Connecticut Public reporting on Milford's August debate](https://www.ctpublic.org/2026-08-07/ct-flock-cameras-technology-regulation)
- [SRC-0073: Milford 2026 Board of Aldermen meeting schedule](https://www.milfordct.us/DocumentCenter/View/3414/ALDERMEN-MEETING-DATES-2026)
- [SRC-0076: Have I Been Flocked Milford audit-data update](https://haveibeenflocked.com/news/milford-ct-pd-jun2026)
- [SRC-0078: Have I Been Flocked project overview and method limits](https://haveibeenflocked.com/)
