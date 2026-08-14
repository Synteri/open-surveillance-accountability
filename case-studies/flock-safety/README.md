# Flock Safety ALPR Case Study

**Case-study version:** `0.2.0-draft.1`  
**Evidence last reviewed:** 2026-08-14  
**Status:** Open draft for private bootstrap review

## Scope

This case study evaluates the **Flock Safety ALPR ecosystem**, not every Flock product and not every customer deployment. The included and excluded capabilities are defined in [`SCOPE.md`](SCOPE.md).

## Current overall conclusion

Flock is not accurately described as having no accountability safeguards. Its public materials describe individual-user search records, required offense-type selection, role-based controls, configurable sharing, search filters, transparency portals, deletion automation, compliance tooling, and continuing security work. Those controls deserve explicit credit while their local configuration and complete production implementation remain separate evidence questions. [SRC-0010, SRC-0016, SRC-0017, SRC-0018, SRC-0019, SRC-0023]

The strongest evidence-bounded concern is narrower: public evidence does not establish a complete, independently verifiable chain from documented promise, to technical control, to local configuration, to the exact behavior deployed for a jurisdiction. Important gaps include exhaustive data and derivation inventory, vendor-privileged access evidence, complete control-plane event coverage, secondary-use boundaries, build and production identity, and rights-focused independent audit access. This is an accountability and evidence gap, not evidence of misconduct. [SRC-0010, SRC-0012, SRC-0013, SRC-0015, SRC-0016, SRC-0020, SRC-0023]

## Strongest safeguards in the current record

- Flock describes attributable LPR searches and mandatory offense-type selection, creating a reviewable statement of purpose for completed searches. [SRC-0010, SRC-0018]
- Search Filters are described as preventing prohibited query categories before results are returned. [SRC-0017]
- Compliance tools and public Transparency Portals are described as capable of exposing policy, sharing, retention, and audit information, although availability, local enablement, and history remain customer-dependent. [SRC-0016]
- The deletion explanation identifies concrete AWS lifecycle and CloudTrail mechanisms and refers to operating-effectiveness testing, which is more specific than a bare deletion promise. The underlying audit report and every storage path are not public in this evidence set. [SRC-0019]
- California remediation material acknowledges earlier sharing and logging limitations and describes added controls, making a real failure mode and response visible even though the remediation is not independently verified here. [SRC-0021]
- State-specific contract provisions can materially strengthen national defaults. Connecticut's legal and contractual layers illustrate why jurisdiction-specific assessment matters. [SRC-0022, SRC-0035, SRC-0037]

## Strongest unresolved accountability gaps

Within the registered source set, the highest-value open questions are:

- Does one versioned public schema cover every collected, derived, searchable, exported, shared, and internally used field? The reviewed policy and product pages do not supply one. [SRC-0010, SRC-0020]
- Does a canonical event inventory cover every search, export, API, administrator, vendor-access, retention, sharing, legal-hold, and model-ingestion action? The reviewed compliance and policy material does not establish complete coverage. [SRC-0010, SRC-0016, SRC-0019]
- What evidence connects reviewed source, model, and configuration to the production deployment for a jurisdiction? The available security announcement does not include that evidence. [SRC-0023]
- How does deletion apply to backups, replicas, caches, derived indexes, evidence stores, exports, and legal holds? The public deletion explanation does not address every path. [SRC-0019]
- Can customers and a rights-focused independent auditor inspect every vendor-privileged access event? The reviewed policy, compliance, and security material does not establish that access. [SRC-0010, SRC-0016, SRC-0023]
- How are broad contractual product-improvement rights narrowed to match the public description of machine-learning use? [SRC-0012, SRC-0014, SRC-0015]
- Where are immutable versions, effective dates, and deployment-state distinctions for every rights-relevant public document? The reviewed live pages do not provide one complete history. [SRC-0010, SRC-0014, SRC-0015, SRC-0016]

See [`UNRESOLVED.md`](UNRESOLVED.md) for the evidence queue.

## Read the evidence

- [`FINDINGS.md`](FINDINGS.md) — narrative findings and fair counterarguments
- [`matrix.csv`](matrix.csv) — one evidence-bounded row per evaluated requirement plus Fairfield context rows
- [`evidence/sources.csv`](../../evidence/sources.csv) — stable source register
- [`jurisdictions/connecticut/fairfield.md`](jurisdictions/connecticut/fairfield.md) — first local implementation record
- [`METHODOLOGY.md`](../../METHODOLOGY.md) — labels, states, responsible actors, and correction rules

## Important limits

This case study does not determine legal compliance, wrongdoing, certification, or product security. A vendor source establishes what Flock publicly states; a local record establishes only the dated fact it contains. Missing public evidence is recorded as `Unknown`, never converted into an accusation.
