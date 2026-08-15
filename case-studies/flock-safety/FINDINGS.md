# Flock Safety Narrative Findings

**Case-study version:** `0.4.0-draft.1`

**Evidence last reviewed:** 2026-08-14

## Bottom line

<!-- oasps-citations:start -->
Flock publicly documents meaningful accountability controls. The case study gives those controls credit and does not treat them as fictitious. The remaining concern is whether rights-relevant promises, controls, customer settings, and production behavior can be connected through complete independent evidence. At present, several important layers are only vendor-asserted or partially verifiable. [SRC-0010, SRC-0016, SRC-0017, SRC-0018, SRC-0019]

The evidence does not support a conclusion that Flock or a customer committed wrongdoing. It supports a more precise conclusion: consequential controls should be independently demonstrable, coherently versioned, and attributable to the deployed system rather than inferred from changing vendor prose. [SRC-0010, SRC-0012, SRC-0014, SRC-0015, SRC-0016]
<!-- oasps-citations:end -->

## 1. Documentation does not yet function as one versioned specification

<!-- oasps-citations:start -->
Flock's public materials are distributed across legal policies, trust pages, product pages, terms, and announcements. The live LPR Policy states a seven-day default, while other general privacy and trust materials have described different retention periods and do not establish any particular customer's setting. The visible update date on a dynamic page also cannot establish when each sentence became effective. A reader therefore needs a local contract and current configuration record, not one generic page, to establish deployed retention. [SRC-0010, SRC-0014, SRC-0015, SRC-0016]
<!-- oasps-citations:end -->

This is not evidence of improper retention. It is evidence that rights-relevant documentation needs immutable versions, effective dates, a change history, and explicit labels for `announced`, `rolling out`, `default for new customers`, `optional`, and `universally deployed`.

## 2. Purpose selection is meaningful; universal case linkage is not established

<!-- oasps-citations:start -->
Flock's public material describes required offense-type selection for completed searches. That creates a stronger review predicate than an optional free-text reason and substantially advances OASPS-B02. Publicly recoverable evidence in this build does not establish that every current search is universally linked to a valid case or incident, so OASPS-B03 remains only partly met rather than treated as deployed everywhere. [SRC-0010, SRC-0016, SRC-0018]

The Notion research record referenced an August 13 announcement for future case-code changes, but that article could not be retrieved directly during the repository source audit. The repository therefore withholds the specific rollout timing as an established factual claim and records the gap for later verification. [SRC-0011]
<!-- oasps-citations:end -->

## 3. Search filters create a real accountability tradeoff

<!-- oasps-citations:start -->
Flock states that Search Filters can block legally prohibited immigration and reproductive-care queries before they are processed, stored, or logged. Preventing the search is a meaningful protection. Recording no audit event can also leave oversight without evidence that an impermissible attempt occurred. [SRC-0017]
<!-- oasps-citations:end -->

<!-- oasps-citations:start -->
<!-- oasps-citation-exempt: normative -->
OASPS-C03 proposes a narrower solution: preserve the actor, time, rule triggered, and review path without retaining the prohibited target or unnecessary sensitive query content.

The case study does not claim that Flock currently creates such an event; the reviewed Search Filters material instead says the prohibited query is not logged. [SRC-0017]
<!-- oasps-citations:end -->

## 4. “Tracking” needs a technical definition

<!-- oasps-citations:start -->
Flock trust material prohibits using its system to track individuals, while Enhanced LPR material describes capabilities that can surface convoys, recurring vehicles, multi-geography occurrences, and travel patterns. Those statements need not be contradictory if “tracking” means continuous following, but repeated observations can still enable retrospective trajectory or association inference. [SRC-0015, SRC-0020]
<!-- oasps-citations:end -->

OASPS-A04 therefore asks a vendor to define terms such as `tracking`, `pattern`, `association`, `real-time`, and `deconfliction`, and to explain the inferences possible from repeated observations. The issue is semantic and technical precision, not an unsupported claim that every customer uses a capability to track people.

## 5. California history validates control-plane audit requirements

<!-- oasps-citations:start -->
Flock acknowledged that some California networks were accessible to out-of-state agencies and that earlier logging limitations prevented it from determining the cause in some instances. The company describes later structural controls and permanent logging for sharing-setting changes. [SRC-0021]

The remediation deserves credit. The same history shows why OASPS-C02 requires complete control-plane evidence from the beginning: who changed sharing, when, from what value, to what value, under what authority, and whether the change was later reversed. This repository does not independently verify the current remediation. [SRC-0021]
<!-- oasps-citations:end -->

## 6. Public secondary-use language and contractual rights need alignment

<!-- oasps-citations:start -->
Flock public materials describe a narrow internal machine-learning use of a small portion of de-identified or separated imagery. The general customer terms grant broader rights to use Customer Data to support and improve products and services. The API terms also preserve significant proprietary and use restrictions. [SRC-0012, SRC-0013, SRC-0014, SRC-0015]

This is best characterized as a contract-to-policy governance tension, not evidence of undisclosed training. OASPS-D06 asks enforceable terms to match the narrower public promise, while OASPS-D05 asks for an ingestion inventory, authorization, logs, retention rules, and independent review. [SRC-0012, SRC-0014, SRC-0015]
<!-- oasps-citations:end -->

## 7. Deletion evidence is unusually concrete but incomplete

<!-- oasps-citations:start -->
Flock describes automated AWS S3 lifecycle deletion, CloudTrail deletion events with tamper-resistant timestamps, and annual SOC 2 Type II testing of the deletion control. That is more concrete evidence than a simple policy promise and should score above ordinary vendor assertion. [SRC-0019]

The cited page does not provide the underlying audit report or a complete public account of backups, replicas, caches, derived indexes, separately preserved evidence, exports, and legal holds. The finding is therefore `Partially verifiable` and `Partly meets`, not fully verified and not dismissed. [SRC-0019]
<!-- oasps-citations:end -->

## 8. Security testing is not the same as rights-focused assurance

<!-- oasps-citations:start -->
Flock states that it retained Bishop Fox for broad adversarial security testing. The source available here is Flock's announcement, not a Bishop Fox report, test scope, findings, or retest result. [SRC-0023]
<!-- oasps-citations:end -->

Security testing can provide genuine assurance while leaving civil-liberties use controls, purpose validity, local sharing, vendor-privileged access, and production identity outside scope. OASPS-E06 gives the announced testing credit but does not label its outcomes independently verified.

## 9. Public inspectability is the default; restricted-review status remains unknown

<!-- oasps-citations:start -->
Flock's customer and API terms describe core methods as proprietary and restrict reverse engineering or extraction, while Flock's security announcement describes controlled independent testing. The registered evidence does not provide a component-specific security-risk decision, independent-public-authority approval, time limit, complete enforceable access terms, or public methods, scope, findings, remediation, and retest results for a rights-focused review. [SRC-0012, SRC-0013, SRC-0023]
<!-- oasps-citations:end -->

<!-- oasps-citations:start -->
Under revised OASPS-E01, this evidence does not establish either the public-inspectability default or every condition for a temporary restricted-review exception. The E01 comparison therefore remains `Unknown`. That is an evidence boundary, not a claim that safeguards are absent, that restricted access is unjustified, or that Flock committed wrongdoing. [SRC-0012, SRC-0013, SRC-0023]
<!-- oasps-citations:end -->

## 10. Connecticut strengthens the floor but does not answer every OASPS question

<!-- oasps-citations:start -->
Connecticut Public Act 26-14 establishes ALPR rules with provision-specific effective dates, including restrictions related to enumerated actual or perceived characteristics, First Amendment activity, immigration enforcement, and reproductive or gender-affirming care. Flock also publishes Connecticut-specific contractual provisions. A later act amended part of Public Act 26-14, so the original act is not read in isolation. [SRC-0022, SRC-0035, SRC-0037]

These protections matter and should be scored separately from the national baseline. They do not by themselves establish Fairfield's current configuration or answer OASPS questions about exhaustive data derivation, vendor-privileged access, build identity, production attestation, and complete independent audit evidence. [SRC-0022, SRC-0035, SRC-0037]
<!-- oasps-citations:end -->

## Strongest fair pro-Flock response

<!-- oasps-citations:start -->
A fair review should say plainly that Flock appears to be doing more than a simplistic “black-box vendor” description suggests. Search actions are attributable; offense types are required; sharing and retention can be controlled; search filters can prevent prohibited categories; compliance and transparency tools exist; deletion has a described technical mechanism; state-specific protections can be stronger; and the vendor has publicly discussed remediation and further safeguards. [SRC-0010, SRC-0016, SRC-0017, SRC-0018, SRC-0019, SRC-0021, SRC-0022, SRC-0023]
<!-- oasps-citations:end -->

The OASPS response is not that those controls are fake. It is that consequential safeguards should be independently demonstrable and connected to a specific deployed version and configuration.

## Matrix interpretation

The accompanying [`matrix.csv`](matrix.csv) keeps evidence quality separate from assessment. A row can `Meets` a proposed requirement while remaining only `Partially verifiable`; a documented gap can `Does not meet` without being labeled legally `Noncompliant`; and missing current evidence remains `Unknown`.
