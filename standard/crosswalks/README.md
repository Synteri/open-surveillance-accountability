# Recognized-Framework Crosswalks

OASPS is intended to be a surveillance-specific extension of established privacy, security, assessment, professional, and human-rights guidance. These crosswalks show conceptual overlap and the places where OASPS deliberately asks for more.

They do **not** establish certification, accreditation, formal conformity, legal compliance, or endorsement by any standards body. The mappings are interpretive drafts and should receive qualified review before OASPS reaches version 1.0.

## Crosswalks

- [NIST Privacy Framework 1.0](nist-privacy-framework.md)
- [NIST SP 800-53 Rev. 5 and SP 800-53A Rev. 5](nist-sp-800-53.md)
- [Council of Europe Convention 108+](convention-108-plus.md)
- [IACP and Bureau of Justice Assistance ALPR guidance](iacp-bja-alpr.md)
- [ISO/IEC 27701](iso-27701.md)

## How to read them

Each crosswalk separates:

1. a recognized concept or control area;
2. the related OASPS requirement IDs;
3. the surveillance-specific extension OASPS proposes;
4. a caution against overstating the mapping.

Crosswalk sources are registered in [`evidence/sources.csv`](../../evidence/sources.csv). Open materials are linked directly. ISO references remain high-level because this repository does not contain or reproduce licensed ISO text.

## Overall interpretation

OASPS requirements concerning inventory, transparency, purpose limitation, authentication, least privilege, retention, deletion, auditable controls, privacy-by-design, and independent oversight have strong recognized foundations. OASPS is most novel or demanding where it requires complete rights-relevant control-plane evidence, privacy-preserving records of blocked prohibited actions, independently inspectable software, reproducible builds, deployment attestation, automatic suspension triggers, and procurement terms that prevent trade-secret claims from defeating oversight.

Those extensions are proposals, not claims that an outside framework already requires OASPS's exact implementation.
