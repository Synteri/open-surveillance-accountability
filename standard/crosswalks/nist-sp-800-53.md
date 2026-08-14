# Crosswalk: NIST SP 800-53 Rev. 5 and SP 800-53A Rev. 5

**Recognized sources:** NIST SP 800-53 Rev. 5 (`SRC-0002`) and NIST SP 800-53A Rev. 5 (`SRC-0003`).

NIST SP 800-53 provides a catalog of security and privacy controls. SP 800-53A provides assessment procedures for determining whether controls are implemented and operating as intended. OASPS borrows the discipline of separating a stated control from evidence that the control is implemented and effective.

| NIST control or assessment area | Related OASPS requirements | OASPS surveillance-specific extension |
|---|---|---|
| Access Control (AC) and Identification and Authentication (IA) | OASPS-B01–B05 | Attach an attributable investigative predicate to surveillance use and make cross-agency access visible, not merely authenticated. |
| Audit and Accountability (AU) | OASPS-C01–C06 | Cover searches, exports, sharing, roles, retention, legal holds, vendor access, APIs, configuration, ML ingestion, and privacy-preserving blocked-attempt events. |
| Assessment, Authorization, and Monitoring (CA) | OASPS-C05, OASPS-E04, OASPS-E06, OASPS-F02 | Give a genuinely independent reviewer access to rights-relevant evidence and link assessed artifacts to the deployed system. |
| Configuration Management (CM) | OASPS-C02, OASPS-E03–E05 | Treat rights-relevant configuration and public documentation as versioned, attestable state. |
| PII Processing and Transparency (PT) | OASPS-A01–A04, OASPS-D01–D06 | Publish derived surveillance attributes and explicitly govern secondary use, deletion paths, and contract-to-policy consistency. |
| System and Services Acquisition (SA) and Supply Chain Risk Management (SR) | OASPS-E01–E06, OASPS-F03 | Build enforceable independent review rights into procurement rather than allowing proprietary restrictions to end oversight. |
| System and Information Integrity (SI) | OASPS-C01–C03, OASPS-E03–E06 | Preserve trustworthy evidence of production identity, rights-relevant changes, and attempted prohibited actions. |
| SP 800-53A assessment discipline | All requirements, especially OASPS-C05 and OASPS-E01–E06 | Distinguish policy, mechanism, local configuration, and independent evidence for every case-study judgment. |

## Limits

OASPS does not claim that selecting or assessing NIST controls proves a surveillance deployment meets OASPS, protects civil liberties, or complies with law. A cybersecurity assessment may be valuable while leaving purpose, local use, public oversight, and remedy outside its scope.

No control-by-control conformity claim is made here. A future crosswalk may add carefully reviewed control identifiers using the official NIST catalog, but only after qualified assessment review.
