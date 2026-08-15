# Crosswalk: NIST Privacy Framework 1.0

**Baseline:** NIST, *NIST Privacy Framework: A Tool for Improving Privacy Through Enterprise Risk Management, Version 1.0*, published 2020-01-16 (`SRC-0001`).
**Tracked draft, not baseline:** NIST Privacy Framework 1.1 Initial Public Draft (CSWP 40), dated 2025-04-14 (`SRC-0008`).
**Last reviewed:** 2026-08-14

<!-- oasps-citations:start -->
NIST Privacy Framework 1.0 remains this crosswalk's stable baseline. NIST's CSRC publication page identifies 1.1 as an Initial Public Draft, so OASPS tracks it for a future update but does not treat it as final or use it as the normative mapping baseline. This mapping uses the 1.0 high-level Functions—Identify-P, Govern-P, Control-P, Communicate-P, and Protect-P—and does not claim that NIST contains OASPS-specific surveillance requirements. [SRC-0001, SRC-0008]
<!-- oasps-citations:end -->

| NIST Privacy Framework concept | Related OASPS requirements | OASPS surveillance-specific extension |
|---|---|---|
| Data processing inventory and risk understanding (`Identify-P`) | OASPS-A01–A04, OASPS-D01 | Publish raw, metadata, derived, inference, confidence, correlation, and capability-semantics information for a public surveillance deployment. |
| Governance, policies, legal requirements, and risk strategy (`Govern-P`) | OASPS-B04, OASPS-D02, OASPS-D05–D06, OASPS-F01–F05 | Tie surveillance capability to democratic authorization, responsible actors, visible objections, suspension triggers, and remedies. |
| Individual and organizational control of data processing (`Control-P`) | OASPS-B01–B05, OASPS-D01–D05 | Require structured investigative purpose, case linkage, protected-activity restrictions, visible sharing, and separation of evidence preservation from population-scale retention. |
| Transparency and communication (`Communicate-P`) | OASPS-A01–A04, OASPS-C06, OASPS-E02, OASPS-E05 | Publish a deployment-specific account rather than relying on generic vendor prose; preserve version and rollout distinctions. |
| Safeguards against privacy events (`Protect-P`) | OASPS-B01, OASPS-C01–C05, OASPS-D04, OASPS-E03–E06 | Demand tamper-resistant rights-relevant logs, deletion evidence across copies, deployment identity, and independent testing. |

## Strongly grounded areas

- inventory and data-processing transparency;
- privacy-risk governance and accountability;
- purpose limitation and manageable processing preferences;
- data minimization, retention, and deletion discipline;
- protective access and audit controls;
- communication of privacy practices.

## OASPS additions requiring separate validation

NIST Privacy Framework 1.0 does not by itself establish OASPS's exact requirements for public inspectability, the restricted-review exception test, reproducible builds, cryptographic deployment attestation, privacy-preserving logs of prohibited attempts, complete vendor-access observability, democratic authorization, or automatic suspension. Those are surveillance-specific OASPS proposals that require policy, public-law, and technical review.

This crosswalk is not a NIST conformity assessment.
