# Flock Safety Case-Study Scope

## Included

The `0.2.0-draft.1` case study evaluates the Flock Safety ALPR ecosystem where the current source record permits, including:

- ALPR image capture and observation data;
- plate interpretation, confidence information, and vehicle descriptors;
- hot-list matching, alerts, lookups, and searches;
- vehicle-oriented visual, multi-location, convoy, association, and pattern search functions;
- search purpose, offense type, case linkage, and prohibited-search filters;
- cross-agency and network sharing;
- user, administrator, vendor, API, and control-plane auditability;
- retention, evidence preservation, deletion, backup, replica, export, and legal-hold questions;
- public Transparency Portals and audit reporting;
- relevant customer, state-specific, privacy, and API terms;
- independent software, security, build, and deployment evidence where publicly available.

## Excluded

The first case study does not evaluate:

- drones;
- audio or acoustic-detection products;
- Nova or other non-ALPR people-search modules;
- general video people search;
- non-ALPR uses of Condor, Wing, or other video products;
- every Flock hardware product or cybersecurity control;
- every agency, jurisdiction, contract, configuration, or user action;
- the location, coverage, or defeat of individual cameras;
- the lawfulness of a particular investigation or search;
- comparative scoring against other surveillance vendors.

Fairfield's 2024 procurement included products beyond the ALPR scope. Those products are named only to define the local contract accurately; they are not silently folded into the Flock ALPR assessment. [SRC-0033]

## Subjects and jurisdictions

`FS-GLOBAL-###` rows evaluate public platform-level evidence. They do not prove a customer's configuration.

`FS-CT-###` rows evaluate Connecticut-wide legal or deployment evidence when added.

`FS-CT-FAIRFIELD-###` rows evaluate Fairfield-specific records. A Fairfield row does not establish behavior in another agency, and a neighboring agency's portal does not establish Fairfield's outbound sharing or actual searches.

## Review date

The initial evidence cut is 2026-08-14. Dynamic vendor pages, portals, laws, contracts, and configurations may change after that date. Every finding must be read with its `last_verified` date.
