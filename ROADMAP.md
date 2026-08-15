# Roadmap

OASPS `0.4.0-draft.1` is an open public working draft released for review, correction, and good-faith criticism. It is not a stable standard, certification, legal determination, or finding of wrongdoing. This roadmap lists evidence and review work; it is not a promise that a tagged release, social post, additional case study, or website will occur.

## 1. Complete the private bootstrap and public-draft preparation

- [x] Populate every required standard, methodology, glossary, data, crosswalk, evidence, case-study, jurisdiction, contribution, and validation file with substantive first-pass content.
- [x] Confirm that all factual case-study claims resolve to source IDs and that all controlled values pass validation.
- [x] Review the repository for secrets, plate data, personal travel records, unnecessary personal information, and nonpublic operational details.
- [x] Record unrecoverable sources and translation limits instead of inventing citations.
- [x] Kept the repository private, GitHub Pages disabled, and the bootstrap work unmerged until owner review.
- [x] Complete independent review of the `0.3.0-draft.1` remediation, including validator enforcement, evidence metadata, matrix semantics, exact standards baselines, and the revised public-inspectability rule.
- [x] Obtain explicit owner approval to change repository visibility and publish the open public working draft.

## 2. Establish Fairfield's current Flock ALPR state

The repository distinguishes Fairfield's documented 2024 board approval and order-form terms presented for approval from its still-unresolved execution, production configuration, and current 2026 operation. Before a Fairfield-focused public launch, seek lawful, current evidence for:

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
- [ ] Test whether OASPS-E01's component-specific security-risk finding, independent-public-authority approval, public notice, time limit, periodic review, complete reviewer access, and public reporting conditions are legally and technically workable together.
- [ ] Test the feasibility and meaning of OASPS deployment-attestation, auditability, and independent-review requirements without performing unauthorized testing.
- [ ] Keep cybersecurity assurance separate from civil-liberties and rights-use assurance.

## 4. Conduct public adversarial review

Invite and visibly disposition good-faith criticism from at least these perspectives:

- civil-liberties and privacy;
- law enforcement and public safety;
- software, security, and technical feasibility;
- local residents, journalists, public officials, and records practitioners.

Review is voluntary and unpaid at this stage. Feedback is not endorsement unless the reviewer explicitly says so. Publication does not require a paid or formal expert blessing, but serious criticism received should be recorded and handled openly.

## 5. Improve the evidence and consider a later tagged release

The initial open public working draft is published from `main` without a tag or GitHub Release. Public adversarial review and evidence improvement come next; a later tagged release is optional and requires a separate owner decision. Before any later tagged release:

- [ ] Reassess the strongest fair pro-Flock response and preserve meaningful safeguards alongside gaps after public criticism.
- [ ] Recheck distinctions among deployed behavior, customer-configurable behavior, jurisdiction-specific behavior, announced changes, and unknowns.
- [ ] Confirm that every consequential factual finding still has a valid, supporting source.
- [ ] Confirm that no wording claims accreditation, certification, expert approval, formal outside-framework conformity, or unsupported wrongdoing.
- [ ] Run `python -m unittest discover -s tests -v` and `python scripts/validate.py` successfully, then inspect links and citations.
- [ ] Obtain explicit owner approval for the specific tag and GitHub Release.

If the owner later approves a tagged release, its release notes should state the standard version, case-study last-verified dates, known limitations, and open-draft status. A tag or GitHub Release is not required for the initial open public working draft.

## 6. Consider initial public sharing

For any separately approved public sharing, prepare a low-drama, evidence-forward explanation. A possible Facebook communication should state what the project is, what it found, what remains unknown, and how to submit corrections. It must not frame the work as certification, claim expert consensus, or describe an evidence gap as misconduct.

Whether to post on Facebook or any other external channel is a separate explicit owner decision. Repository creation does not authorize external posting.

## 7. Test the jurisdiction-level inventory before expanding it

- [x] Add Fairfield as the first jurisdiction-level inventory while preserving the separate Flock vendor study.
- [x] Keep distinct local technologies, vendors, purposes, evidence labels, and implementation states separate, without prematurely scoring every system.
- [ ] Review whether Fairfield's inventory schema and system-page structure make proposals, historical deployments, current policy, and current operation understandable to residents.
- [ ] Resolve the highest-value Fairfield evidence gaps where public material later becomes available, without automatically submitting records requests or publishing sensitive locations.
- [ ] Consider another jurisdiction only after the Fairfield model proves understandable, maintainable, and evidence-bounded.
- [ ] Test whether OASPS remains fair and usable across different vendors, agency sizes, laws, and deployment models before any broader comparison.
- Do not create a vendor scoring leaderboard or expand merely to appear comprehensive.

## 8. Optional website

GitHub's Markdown rendering is sufficient for the first public draft. Consider a small, accessible website only if repository evidence and versioning are stable and a website would materially improve resident comprehension. Any website should be generated from versioned repository content, preserve source links and evidence labels, and add no new factual claims. GitHub Pages or another deployment requires separate approval.

## 9. Deferred policy questions

The `0.4.0-draft.1` working draft does not decide a complete material-failure taxonomy, individual notice and contestability rules, heightened authorization tiers for intrusive searches, or recurring democratic sunset and necessity review. These remain candidates for separately scoped public-law, civil-liberties, public-safety, and technical review rather than silent additions to the current draft.
