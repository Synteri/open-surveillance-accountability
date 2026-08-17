# Fairfield, Connecticut surveillance-system inventory

**Case-study version:** `0.4.0-draft.1`

**Inventory date:** 2026-08-15

<!-- oasps-citations:start -->
Fairfield's public record describes multiple distinct camera-surveillance programs with different purposes and governance records: a Flock ALPR procurement record whose current operation remains incompletely established; a currently active Altumint school-zone speed-enforcement program; current Axon body-worn and in-vehicle programs and their core digital-evidence workflow; and a historically documented Police Safe Corridor school-area camera program whose 2026 status is unknown. The sources do not establish one unified surveillance network, every named Axon feature as enabled, a replacement of Flock by Axon, or current operation of every historical acquisition. [SRC-0032, SRC-0033, SRC-0041, SRC-0042, SRC-0043, SRC-0047, SRC-0048, SRC-0049]
<!-- oasps-citations:end -->

This case study answers a bounded discovery question: **What camera-based public surveillance systems does Fairfield appear to operate or have recently operated, what can the public record establish about each one, and what remains unknown?** It does not score every system against every OASPS requirement.

## Two complementary case-study axes

- A **vendor-level study** follows one technology ecosystem across products, policies, and jurisdictions. The existing [Flock Safety case study](../flock-safety/README.md) and its [claim matrix](../flock-safety/matrix.csv) use that axis.
- A **jurisdiction-level inventory** identifies distinct systems within one public body, records the best-supported current state, and exposes the next evidence needed. This Fairfield module uses that axis.

The [Flock ALPR system page](systems/flock-alpr.md) cross-links the existing Fairfield/Flock record. It does not copy, rescore, or silently change the Flock matrix.

## Inventory at a glance

<!-- oasps-citations:start -->
- **Flock ALPR ecosystem:** 2024 board approval and a 30-day order-form term are documented, while general Connecticut provisions specify 21 days or a shorter customer-requested period for covered public-agency ALPR data. Current Fairfield execution, configuration, retention, sharing, search activity, audit surface, and operation remain incompletely established. [SRC-0022, SRC-0032, SRC-0033]
- **Automated traffic enforcement:** Fairfield reports an active Altumint school-zone speed program in six approved groupings, with trained Town citation review and explicit ordinance rules for purpose, appeal, disclosure, retention, destruction, FOIA treatment, and reporting. [SRC-0038, SRC-0039, SRC-0040, SRC-0041, SRC-0042]
- **Axon police video:** current policy documents body-worn cameras, patrol-vehicle cameras, their core evidence workflow, and named Axon features; current counts, models, complete licensing and configuration, actual control performance, and any Axon ALPR use remain unknown. [SRC-0043, SRC-0044, SRC-0045, SRC-0051]
- **Police Safe Corridor school-area cameras:** primary records establish authorization and at least partial installation through late 2024, but not a current vendor, approved or deployed count, retention rule, complete analytics, or 2026 status. [SRC-0047, SRC-0048, SRC-0049, SRC-0050]
<!-- oasps-citations:end -->

The machine-readable record separates Axon's capture devices and digital-evidence services into distinct rows. See [`inventory.csv`](inventory.csv) for all six system records and [the data dictionary](../../DATA-DICTIONARY.md) for exact field semantics.

## Why compare systems within one town?

Jurisdiction-level comparison tests whether the inventory method remains vendor-neutral. The same municipality can authorize, operate, retain, disclose, and oversee different surveillance systems through very different mechanisms.

Fairfield's automated traffic-enforcement ordinance is a useful example because it makes review, appeal, disclosure, retention, destruction, public-record treatment, and annual reporting unusually explicit. The contrast helps identify which questions to ask of other systems; it is not, by itself, a finding that another system is deficient or misused.

## Evidence boundaries

- Acquisition, approval, or contracted capability is not automatically current deployment or enabled configuration.
- A described feature is not proof of actual use, accuracy, or complete coverage.
- `Historical` means a past state is established while current operation is not.
- `Unknown` is preserved when public evidence cannot answer the question; it is not evidence of misconduct.
- Exact camera locations, plate data, travel histories, private contact details, and nonpublic operational information are outside this inventory.

## Read the system pages

1. [Flock ALPR ecosystem](systems/flock-alpr.md)
2. [Automated traffic enforcement cameras](systems/automated-traffic-enforcement.md)
3. [Axon police video systems](systems/axon-police-video.md)
4. [Police Safe Corridor school-area cameras](systems/school-security-cameras.md)

Open questions are consolidated in [UNRESOLVED.md](UNRESOLVED.md), source metadata is in the repository [source register](../../evidence/sources.csv), and module history is in [CHANGELOG.md](CHANGELOG.md).
