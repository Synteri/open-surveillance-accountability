# Roadmap

OASPS is currently a private bootstrap at `0.2.0-draft.1`. This roadmap lists evidence and review work; it is not a promise that a public release, social post, additional case study, or website will occur.

## 1. Complete the private repository bootstrap

- [x] Populate every required standard, methodology, glossary, data, crosswalk, evidence, case-study, jurisdiction, contribution, and validation file with substantive first-pass content.
- [x] Confirm that all factual case-study claims resolve to source IDs and that all controlled values pass validation.
- [x] Review the repository for secrets, plate data, personal travel records, unnecessary personal information, and nonpublic operational details.
- [x] Record unrecoverable sources and translation limits instead of inventing citations.
- [x] Keep the repository private, GitHub Pages disabled, and the bootstrap work unmerged until owner review.

## 2. Establish Fairfield's current state

The repository distinguishes Fairfield's documented 2024 contracted state from its still-unresolved 2026 production state. Before a Fairfield-focused public launch, seek lawful, current evidence for:

- the active contract term, products, renewal state, and amendments;
- the current ALPR retention setting;
- the current local ALPR/Flock policy and training or acknowledgment rules;
- inbound and outbound cross-agency sharing configuration;
- recent search and network audit records;
- public Transparency Portal and Search Audit locations;
- configuration changes and implementation of Connecticut Public Act 26-14.

Any public-record request requires a separate, deliberate decision because the request may identify the requester and become a government record. Do not submit one automatically. Until current evidence is obtained, retain `Unknown` or `Partially verifiable` labels as appropriate.

## 3. Close the highest-value technical evidence gaps

- [ ] Determine whether vendor-privileged access is completely logged and available to independent review.
- [ ] Establish which administrative, API, export, sharing, retention, legal-hold, backup, replica, and machine-learning-ingestion events produce audit records.
- [ ] Clarify how deletion applies to backups, replicas, derived indexes, evidence preservation, exports, and legal holds.
- [ ] Assess whether audited software and configuration can be tied to the deployed production version.
- [ ] Test the feasibility and meaning of OASPS deployment-attestation, auditability, and independent-review requirements without performing unauthorized testing.
- [ ] Keep cybersecurity assurance separate from civil-liberties and rights-use assurance.

## 4. Conduct voluntary adversarial review

Invite and visibly disposition good-faith criticism from at least these perspectives:

- civil-liberties and privacy;
- law enforcement and public safety;
- software, security, and technical feasibility;
- local residents, journalists, public officials, and records practitioners.

Review is voluntary and unpaid at this stage. Feedback is not endorsement unless the reviewer explicitly says so. Publication does not require a paid or formal expert blessing, but serious criticism received should be recorded and handled openly.

## 5. Prepare an owner-approved public draft

Before a public release:

- [ ] Represent the strongest fair pro-Flock response and preserve meaningful safeguards alongside gaps.
- [ ] Separate deployed behavior, customer-configurable behavior, jurisdiction-specific behavior, announced changes, and unknowns.
- [ ] Confirm that every consequential factual finding has a valid, supporting source.
- [ ] Confirm that no wording claims accreditation, certification, expert approval, formal outside-framework conformity, or unsupported wrongdoing.
- [ ] Run `python scripts/validate.py` successfully and inspect links and citations.
- [ ] Obtain explicit owner approval to change visibility and release.

Only after approval should the owner tag `v0.2.0-draft.1` and create release notes that state the standard version, case-study last-verified dates, known limitations, and open-draft status. The bootstrap process must not create a public tag or release.

## 6. Consider initial public sharing

After an approved public-draft release, prepare a low-drama, evidence-forward launch explanation. A possible Facebook launch should state what the project is, what it found, what remains unknown, and how to submit corrections. It must not frame the work as certification, claim expert consensus, or describe an evidence gap as misconduct.

Whether to post on Facebook or any other external channel is a separate explicit owner decision. Repository creation does not authorize external posting.

## 7. Expand only after the first case study is stable

- Consider additional Connecticut jurisdictions and then a small number of jurisdictions with strong public evidence.
- Test whether OASPS remains fair and usable across different vendors, agency sizes, laws, and deployment models before any broader comparison.
- Do not create a vendor scoring leaderboard or expand beyond the Flock ALPR case study merely to appear comprehensive.

## 8. Optional website

GitHub's Markdown rendering is sufficient for the first public draft. Consider a small, accessible website only if repository evidence and versioning are stable and a website would materially improve resident comprehension. Any website should be generated from versioned repository content, preserve source links and evidence labels, and add no new factual claims. GitHub Pages or another deployment requires separate approval.
