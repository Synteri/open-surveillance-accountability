# Open Accountability Standard for Public Surveillance Systems

**OASPS is an open draft, not a certification or an accusation.** It proposes a practical way for residents and independent reviewers to ask what a public surveillance system does, who can use it, what evidence exists, and what remains unknown.

If government can see the public through a surveillance system, the public should have meaningful ways to see through that system.

## Why this exists

Public agencies increasingly use systems that can collect observations, connect them across time or place, share them with other organizations, and preserve them for investigations. A resident should not need to be a privacy lawyer or software engineer to understand the rules that govern those systems.

OASPS turns that concern into specific, testable requirements. It asks for clear data inventories, limited purposes, attributable access, durable audits, disciplined retention and deletion, public inspectability of rights-relevant safeguards by default, public authorization, and meaningful remedies. A component may be temporarily restricted to qualified independent reviewers only under a narrow, publicly governed security exception—not merely because it is proprietary. OASPS also assigns each responsibility to the actor that can actually satisfy it: vendor, agency, legislature, court, independent oversight body, or a combination of them.

## What OASPS is—and is not

OASPS is:

- a vendor-neutral draft accountability standard;
- a method for separating evidence from judgment;
- a public source register and claim-by-claim case-study ledger;
- an invitation to correct facts and challenge the framework in public.

OASPS is not:

- an accredited standard, certification, legal opinion, or security authorization;
- a finding that any vendor, agency, or individual committed wrongdoing;
- a scoring leaderboard or a substitute for a court, regulator, or elected body;
- a request to expose credentials, sensitive security details, plate data, or personal travel records.

## Current draft

This repository packages **OASPS `0.4.0-draft.1`** as an open public working draft released for review, correction, and good-faith criticism. It is not a stable standard, certification, legal determination, or finding of wrongdoing. The `main` branch is a working draft, not a tagged stable release. [STANDARD.md](STANDARD.md) states requirements for any public surveillance system. Case studies then use two complementary axes: [the Flock Safety vendor study](case-studies/flock-safety/README.md) evaluates the defined ALPR ecosystem, while [the Fairfield jurisdiction inventory](case-studies/fairfield-connecticut/README.md) discovers distinct systems within one town without scoring each against every requirement.

<!-- oasps-citations:start -->
The current evidence supports a deliberately balanced conclusion: Flock documents and appears to implement several meaningful safeguards, including attributable searches, purpose selection, configurable sharing, transparency tools, and deletion controls. Important rights-relevant layers nevertheless remain dependent on vendor or agency statements rather than a complete, independently verifiable chain from written promise to deployed behavior. This is an evidence and observability gap, not evidence of misconduct. [SRC-0010, SRC-0016, SRC-0018, SRC-0019, SRC-0021]

Within the Flock vendor study, Fairfield, Connecticut is the first local implementation record. Public municipal records establish that the Board of Selectmen approved the agreement in 2024; an order form included in the meeting packet lists the package's cost and product mix and a 30-day retention term presented for approval. The packet does not independently establish execution of the displayed order form, deployed configuration, or current operation. The current 2026 contract, configuration, retention, sharing, search history, and audit surface remain explicitly unknown. See [the Fairfield record](case-studies/flock-safety/jurisdictions/connecticut/fairfield.md) for the claim-by-claim distinction. [SRC-0032, SRC-0033, SRC-0034, SRC-0036]

The jurisdiction inventory adds separate records for Fairfield's current Altumint school-zone speed-enforcement program, current Axon body-worn and in-vehicle programs and their core digital-evidence workflow, and the historically documented Police Safe Corridor school-area camera program. It preserves separate vendors, purposes, evidence strengths, and implementation states; it does not treat the records as one unified network, assume every named Axon feature is enabled, or say Axon replaced Flock. [SRC-0038, SRC-0039, SRC-0041, SRC-0042, SRC-0043, SRC-0047, SRC-0048, SRC-0049]
<!-- oasps-citations:end -->

## Start here

1. To commission or fund a Connecticut ALPR review, start with the [funding and commissioning package](funding/README.md).
2. Read the [standard](STANDARD.md) for the proposed requirements.
3. Read the [methodology](METHODOLOGY.md) to understand evidence labels, assessments, implementation states, dates, and unknowns.
4. Read the [Flock Safety vendor case study](case-studies/flock-safety/README.md), its [narrative findings](case-studies/flock-safety/FINDINGS.md), and the machine-readable [claim matrix](case-studies/flock-safety/matrix.csv).
5. Read the [Fairfield jurisdiction inventory](case-studies/fairfield-connecticut/README.md), its [system pages](case-studies/fairfield-connecticut/systems/), and the machine-readable [inventory](case-studies/fairfield-connecticut/inventory.csv).
6. Use the [Fairfield Flock record](case-studies/flock-safety/jurisdictions/connecticut/fairfield.md) when claim-level ALPR detail is needed; the jurisdiction inventory cross-links rather than duplicates it.
7. Resolve every citation through the [source register](evidence/sources.csv) and consult the [data dictionary](DATA-DICTIONARY.md) for exact field meanings.

Additional context:

- [Recognized-framework crosswalks](standard/crosswalks/README.md)
- [Glossary](GLOSSARY.md)
- [Unresolved research queue](case-studies/flock-safety/UNRESOLVED.md)
- [Fairfield unresolved evidence](case-studies/fairfield-connecticut/UNRESOLVED.md)
- [Roadmap](ROADMAP.md)
- [Project limitations](DISCLAIMER.md)

## How evidence is handled

Each Flock claim-matrix row answers two separate questions:

1. **How well do we know the underlying fact?** This is the evidence label: `Verified`, `Vendor-asserted`, `Partially verifiable`, `Unknown`, or `Noncompliant`.
2. **How does the observed behavior compare with the requirement?** This is the assessment: `Meets`, `Partly meets`, `Does not meet`, `Unknown`, or `Not applicable`.

The project does not turn absent public evidence into a negative finding. Conflicting sources remain visible. Marketing material establishes what a vendor publicly states; it does not establish the complete production implementation. Current behavior, optional configuration, jurisdiction-specific rules, and announced future changes remain separate.

Fairfield inventory rows use the same evidence-label and implementation-state vocabularies, but they deliberately omit an OASPS assessment. They identify systems and current evidence posture; they are not abbreviated compliance findings.

## Review and corrections

Voluntary review is welcome and is not treated as endorsement. Use the issue forms to submit an [evidence correction](https://github.com/Synteri/open-surveillance-accountability/issues/new?template=evidence-correction.yml), [framework criticism](https://github.com/Synteri/open-surveillance-accountability/issues/new?template=framework-feedback.yml), or [local evidence](https://github.com/Synteri/open-surveillance-accountability/issues/new?template=local-evidence.yml). Technical objections and focused revisions may also be proposed through pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) before sharing records.

Do not submit plate numbers, private travel records, requester home addresses, private email addresses, credentials, nonpublic system details, or instructions for bypassing surveillance systems.

## Version, citation, and licenses

- Current repository version: [`VERSION`](VERSION)
- Change history: [`CHANGELOG.md`](CHANGELOG.md)
- Preferred citation metadata: [`CITATION.cff`](CITATION.cff)
- Split-license overview: [`LICENSE.md`](LICENSE.md)
- Documentation and structured factual content: [CC BY 4.0](LICENSE-CONTENT)
- Validation code: [MIT](LICENSE-CODE)

Read [DISCLAIMER.md](DISCLAIMER.md) before relying on this work for legal, procurement, security, or operational decisions.
