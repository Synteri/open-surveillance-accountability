# Recognized-Framework Crosswalks

OASPS is intended to be a surveillance-specific extension of established privacy, security, assessment, professional, and human-rights guidance. These crosswalks show conceptual overlap and the places where OASPS deliberately asks for more.

They do **not** establish certification, accreditation, formal conformity, legal compliance, or endorsement by any standards body. The mappings are interpretive drafts and should receive qualified review before OASPS reaches version 1.0.

**Last reviewed:** 2026-08-14

## Fixed baselines for this draft

| Crosswalk | Baseline |
|---|---|
| NIST Privacy Framework | Version 1.0 is the stable baseline; Version 1.1 Initial Public Draft is tracked only and is not treated as final. |
| NIST SP 800-53 / 800-53A | SP 800-53 Rev. 5, Release 5.2.0, and SP 800-53A Rev. 5, Release 5.2.0. |
| Convention 108+ | Council of Europe consolidated modernised Convention 108 text: ETS No. 108 as amended by Protocol CETS No. 223. |
| IACP/BJA ALPR guidance | The official 2012 OJP/NIJ-sponsored operational-guidance record, NCJ 239604, and the February 2017 BJA LPR policy-development template. |
| ISO/IEC 27701 | ISO/IEC 27701:2025, Edition 2, at official public-overview level only. |

## Crosswalks

- [NIST Privacy Framework 1.0](nist-privacy-framework.md)
- [NIST SP 800-53 Rev. 5 and SP 800-53A Rev. 5, Release 5.2.0](nist-sp-800-53.md)
- [Council of Europe Convention 108+](convention-108-plus.md)
- [IACP and Bureau of Justice Assistance ALPR guidance](iacp-bja-alpr.md)
- [ISO/IEC 27701:2025, Edition 2](iso-27701.md)

## How to read them

Each crosswalk separates:

1. a recognized concept or control area;
2. the related OASPS requirement IDs;
3. the surveillance-specific extension OASPS proposes;
4. a caution against overstating the mapping.

Crosswalk sources are registered in [`evidence/sources.csv`](../../evidence/sources.csv). Open materials are linked directly. ISO references remain high-level because this repository does not contain or reproduce licensed ISO text.

## Overall interpretation

OASPS requirements concerning inventory, transparency, purpose limitation, authentication, least privilege, retention, deletion, auditable controls, privacy-by-design, and independent oversight have strong recognized foundations. OASPS is most novel or demanding where it requires public inspectability by default, a narrow independently governed test for temporary restricted review, complete rights-relevant control-plane evidence, privacy-preserving records of blocked prohibited actions, reproducible builds, deployment attestation, automatic suspension triggers, and procurement terms that prevent trade-secret claims from defeating oversight.

Those extensions are proposals, not claims that an outside framework already requires OASPS's exact implementation.
