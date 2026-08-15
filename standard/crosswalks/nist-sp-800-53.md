# Crosswalk: NIST SP 800-53 Rev. 5 and SP 800-53A Rev. 5 — Release 5.2.0

**Baseline:** NIST SP 800-53 Rev. 5, *Security and Privacy Controls for Information Systems and Organizations*, Release 5.2.0 (`SRC-0002`), and NIST SP 800-53A Rev. 5, *Assessing Security and Privacy Controls in Information Systems and Organizations*, Release 5.2.0 (`SRC-0003`).
**Last reviewed:** 2026-08-14

<!-- oasps-citations:start -->
NIST issued Release 5.2.0 for both publications on 2025-08-27. SP 800-53 provides a catalog of security and privacy controls; SP 800-53A provides corresponding assessment procedures. OASPS borrows the discipline of separating a stated control from evidence that the control is implemented and effective. [SRC-0002, SRC-0003]
<!-- oasps-citations:end -->

| NIST control or assessment area | Related OASPS requirements | OASPS surveillance-specific extension |
|---|---|---|
| Access Control (AC) and Identification and Authentication (IA) | OASPS-B01–B05 | Attach an attributable investigative predicate to surveillance use and make cross-agency access visible, not merely authenticated. |
| Audit and Accountability (AU) | OASPS-C01–C06 | Cover searches, exports, sharing, roles, retention, legal holds, vendor access, APIs, configuration, ML ingestion, and privacy-preserving blocked-attempt events. |
| Assessment, Authorization, and Monitoring (CA) | OASPS-C05, OASPS-E04, OASPS-E06, OASPS-F02 | Give a genuinely independent reviewer access to rights-relevant evidence and link assessed artifacts to the deployed system. |
| Configuration Management (CM) | OASPS-C02, OASPS-E03–E05 | Treat rights-relevant configuration and public documentation as versioned, attestable state. |
| PII Processing and Transparency (PT) | OASPS-A01–A04, OASPS-D01–D06 | Publish derived surveillance attributes and explicitly govern secondary use, deletion paths, and contract-to-policy consistency. |
| System and Services Acquisition (SA) and Supply Chain Risk Management (SR) | OASPS-E01–E06, OASPS-F03 | Default to public inspectability for rights-relevant components; permit temporary restricted review only under E01's complete, independently governed exception test. |
| System and Information Integrity (SI) | OASPS-C01–C03, OASPS-E03–E06 | Preserve trustworthy evidence of production identity, rights-relevant changes, and attempted prohibited actions. |
| SP 800-53A assessment discipline | All requirements, especially OASPS-C05 and OASPS-E01–E06 | Distinguish policy, mechanism, local configuration, and independent evidence for every case-study judgment. |

## Limits

OASPS does not claim that selecting or assessing NIST controls proves a surveillance deployment meets OASPS, protects civil liberties, or complies with law. A cybersecurity assessment may be valuable while leaving purpose, local use, public oversight, and remedy outside its scope.

NIST's assurance and assessment concepts do not themselves establish OASPS-E01's public-disclosure default or its component-specific security-risk, public-authority, time-limit, complete-access, and public-reporting conditions. No control-by-control conformity claim is made here. A future crosswalk may add carefully reviewed control identifiers using the official NIST catalog, but only after qualified assessment review.
