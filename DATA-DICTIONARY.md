# Data Dictionary

This document defines the two CSV files in the first OASPS repository snapshot:

- [`evidence/sources.csv`](evidence/sources.csv), the stable source register;
- [`case-studies/flock-safety/matrix.csv`](case-studies/flock-safety/matrix.csv), the claim-by-claim evidence ledger.

CSV files use UTF-8, a comma delimiter, one header row, and RFC 4180-style quoting. A field containing a comma, quotation mark, or line break must be enclosed in double quotes, and an embedded double quote must be doubled. Blank fields are represented by adjacent delimiters; the strings `null`, `N/A`, and `TBD` are not null markers.

## Common formats

### Dates

Dates use ISO 8601 calendar form `YYYY-MM-DD`, for example `2026-08-14`. Date-time values are not used in the initial CSV schemas.

### Stable identifiers

| Entity | Format | Example |
|---|---|---|
| Requirement | `OASPS-[A-F][0-9]{2}` | `OASPS-C01` |
| Source | `SRC-[0-9]{4}` | `SRC-0019` |
| Flock global claim | `FS-GLOBAL-[0-9]{3}` | `FS-GLOBAL-014` |
| Connecticut claim | `FS-CT-[0-9]{3}` | `FS-CT-001` |
| Fairfield claim | `FS-CT-FAIRFIELD-[0-9]{3}` | `FS-CT-FAIRFIELD-004` |

Identifiers are unique within their file and are not recycled after publication. A withdrawn item keeps its ID and records its disposition in notes and the relevant changelog.

### Multiple source IDs

`source_ids` in the matrix uses a vertical bar with no surrounding spaces:

```text
SRC-0010|SRC-0016
```

Each token must exist exactly once in `evidence/sources.csv`. A row with no supporting source leaves `source_ids` blank and must use an `Unknown` evidence label with a specific unresolved question. Narrative claims may show multiple IDs as `[SRC-0010, SRC-0016]` for readability.

## `evidence/sources.csv`

Columns appear in this exact order:

```text
source_id,title,publisher,url,source_type,published_date,accessed_date,jurisdiction,archived_url,local_snapshot,notes
```

| Column | Required | Definition | Rules and example |
|---|---:|---|---|
| `source_id` | Yes | Stable source identifier. | Unique `SRC-####`; example `SRC-0033`. |
| `title` | Yes | Human-readable source title. | Use the document or page's actual title where recoverable. |
| `publisher` | Yes | Organization responsible for publication. | Example `Town of Fairfield, Connecticut`. |
| `url` | Yes | Direct public retrieval URL. | Must begin with `https://` in the first build. Link to the supporting page or document, not a search-results page. |
| `source_type` | Yes | Controlled description of the source. | One of the values below. |
| `published_date` | No | Publication, execution, approval, or visible update date. | Blank when no reliable date is available. |
| `accessed_date` | Yes | Date the project last retrieved or checked the source. | ISO date; first build uses `2026-08-14` where checked in the Notion evidence pass. |
| `jurisdiction` | Yes | Geographic or institutional scope. | Use `Global`, `United States`, `Europe`, `Connecticut`, `Fairfield, Connecticut`, `Wilton, Connecticut`, or another explicit scope. |
| `archived_url` | No | Lawful stable archive URL. | Blank when no archive was recorded. Do not invent one. |
| `local_snapshot` | No | Repository-relative path to a lawful local copy. | Blank in the first build unless a reviewed snapshot is actually committed. |
| `notes` | No | Limits, version conflict, access status, or what the source can prove. | State when material is vendor-authored, high-level only, moved, or unavailable. |

Allowed `source_type` values:

- `Law`
- `Contract`
- `Government record`
- `Vendor legal`
- `Vendor technical`
- `Vendor announcement`
- `Transparency portal`
- `Professional guidance`
- `Security assessment`
- `Research`
- `Reporting`

The controlled set may be extended only through a documented schema decision and corresponding validator update.

## `case-studies/flock-safety/matrix.csv`

Columns appear in this exact order:

```text
claim_id,requirement_id,subject,jurisdiction,responsible_actor,finding,documented_policy,technical_control,deployed_configuration,independent_verification,evidence_label,assessment,implementation_state,last_verified,source_ids,unresolved_question,next_action,notes
```

| Column | Required | Definition | Rules and example |
|---|---:|---|---|
| `claim_id` | Yes | Stable identifier for the evaluated claim. | Unique `FS-GLOBAL-###`, `FS-CT-###`, or `FS-CT-FAIRFIELD-###`. |
| `requirement_id` | Yes | OASPS requirement being evaluated. | Must resolve to a heading in `STANDARD.md`. A local factual row that informs multiple requirements uses the most direct requirement and explains cross-cutting relevance in notes. |
| `subject` | Yes | System, capability, agency, contract, or deployment evaluated. | Example `Flock ALPR platform — search purpose`. |
| `jurisdiction` | Yes | Scope of the finding. | Example `Global` or `Fairfield, Connecticut`. |
| `responsible_actor` | Yes | Actor able or obligated to satisfy the requirement. | Controlled values below. |
| `finding` | Yes | Concise evidence-bounded conclusion. | Must distinguish assertion, capability, configuration, and current unknowns. |
| `documented_policy` | Yes | What written policy, contract, law, term, or announcement says. | Use `No public evidence located` when that absence is itself the scoped result; do not write `N/A` unless the row is assessed `Not applicable`. |
| `technical_control` | Yes | Described or observed enforcement, logging, prevention, or verification mechanism. | State `Unknown from public evidence` when appropriate. |
| `deployed_configuration` | Yes | Version, local setting, rollout state, or production condition in scope. | Historical conditions include the date; current unknowns remain explicit. |
| `independent_verification` | Yes | What an external party can establish and the boundary of that proof. | Distinguish primary records from vendor claims and NDA-gated assessments. |
| `evidence_label` | Yes | Confidence in the underlying fact. | Controlled values below. |
| `assessment` | Yes | Comparison with the requirement. | Controlled values below. |
| `implementation_state` | Yes | Timing or configurability of behavior. | Controlled values below. |
| `last_verified` | Yes | Date the cited evidence was last checked. | ISO date. It is not necessarily the behavior or publication date. |
| `source_ids` | Conditional | Supporting source identifiers. | Required for any row not labeled `Unknown`; pipe-separated and resolvable. An `Unknown` row may still cite evidence that establishes only the gap. |
| `unresolved_question` | Yes | Exact fact or proof still missing. | Use `None within current scope` only when the row genuinely has no material open question. |
| `next_action` | Yes | Lawful, proportionate evidence step. | Must not direct unauthorized testing, contact, or records submission by an automated agent. |
| `notes` | No | Scope qualifications, legal-floor distinction, conflicts, or history. | Avoid unsupported conclusions. |

Allowed `responsible_actor` values:

- `Vendor`
- `Agency`
- `Legislature`
- `Court`
- `Independent oversight`
- `Shared`

Allowed `evidence_label` values:

- `Verified`
- `Vendor-asserted`
- `Partially verifiable`
- `Unknown`
- `Noncompliant`

Allowed `assessment` values:

- `Meets`
- `Partly meets`
- `Does not meet`
- `Unknown`
- `Not applicable`

Allowed `implementation_state` values:

- `Deployed now`
- `Announced or future`
- `Optional or customer-configurable`
- `Jurisdiction-specific`
- `Unknown`

## Example matrix row

```csv
claim_id,requirement_id,subject,jurisdiction,responsible_actor,finding,documented_policy,technical_control,deployed_configuration,independent_verification,evidence_label,assessment,implementation_state,last_verified,source_ids,unresolved_question,next_action,notes
FS-GLOBAL-001,OASPS-A01,Flock ALPR platform — data inventory,Global,Vendor,"Public materials identify several collected and derived fields but no single exhaustive versioned schema was located.","The LPR policy names core observation fields; product material describes additional derived search capabilities.","Public pages describe plate interpretation, confidence filtering, hot-list matching, and vehicle-oriented search functions.","Feature-dependent; no complete production field inventory is public.","An external reader can compare public pages but cannot establish every production field or derivation.",Partially verifiable,Partly meets,Deployed now,2026-08-14,SRC-0010|SRC-0020,"Which collected, derived, searchable, exported, and internally used fields exist in each deployed version?","Obtain a versioned field and data-flow inventory through lawful public documentation or independent review.","Vendor sources establish public descriptions, not exhaustive production behavior."
```

## Validation expectations

`python scripts/validate.py` checks:

- exact header order;
- required fields;
- unique and correctly formatted IDs;
- controlled values;
- ISO dates;
- source-reference resolution;
- requirement-reference resolution;
- case-study narrative source-ID resolution;
- required repository files and practical internal Markdown links.

Passing validation establishes repository consistency, not factual truth, legal compliance, accreditation, or security assurance.
