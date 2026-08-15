# Data Dictionary

This document defines the two CSV files in the first OASPS repository snapshot:

- [`evidence/sources.csv`](evidence/sources.csv), the stable source register;
- [`case-studies/flock-safety/matrix.csv`](case-studies/flock-safety/matrix.csv), the claim-by-claim evidence ledger.

CSV files use UTF-8, a comma delimiter, one header row, and RFC 4180-style quoting. A field containing a comma, quotation mark, or line break must be enclosed in double quotes, and an embedded double quote must be doubled. Blank fields are represented by adjacent delimiters; the strings `null`, `N/A`, and `TBD` are not null markers.

## Common formats

### Dates

Calendar dates use ISO 8601 form `YYYY-MM-DD`, for example `2026-08-14`.

Date-time values use ISO 8601/RFC 3339 form with an explicit timezone, for example `2026-08-14T15:42:00-04:00` or `2026-08-14T19:42:00Z`. A timezone-less timestamp is invalid. `accessed_date` records the calendar date on which a source was retrieved or checked; `retrieved_at` records an exact retrieval time only when that timestamp was captured. Do not infer a timestamp from a date.

### Snapshot hashes and safe formats

`content_sha256` is the SHA-256 digest of the exact stored bytes, written as 64 lowercase hexadecimal characters. It is required exactly when `local_snapshot` is populated, must describe the committed file after any authorized redaction, and remains blank when no local snapshot exists.

Local snapshots use repository-relative paths under `evidence/snapshots/` and one of four UTF-8, non-executable formats: plain text (`.txt`), Markdown (`.md`), JSON (`.json`), or CSV (`.csv`). Do not store PDFs, executable files, scripts, office files, or web archives as evidence snapshots in this repository.

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

### Narrative citation markers

Designated factual sections in repository narratives begin with `<!-- oasps-citations:start -->` and end with `<!-- oasps-citations:end -->`. Within a designated section, each prose paragraph or list item ends with one source marker after the final sentence. A single-source marker is `[SRC-0010]`; a multi-source marker is `[SRC-0010, SRC-0016]`, using a comma followed by one space. IDs may not be duplicated within a marker, and every ID must resolve to the source register. This trailing placement connects the citation to the immediately preceding claim.

An intentionally non-factual block inside a designated section may be exempted only by placing `<!-- oasps-citation-exempt: reason -->` immediately before it. The controlled reasons are `normative`, `methodological`, `editorial`, `question`, and `navigation`. The annotation applies only to the next paragraph or list block and must never exempt a factual claim. Headings and the boundary comments themselves are not paragraphs.

## `evidence/sources.csv`

Columns appear in this exact order:

```text
source_id,title,publisher,url,source_type,published_date,accessed_date,jurisdiction,archived_url,local_snapshot,retrieval_status,retrieved_at,effective_date,content_sha256,notes
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
| `retrieval_status` | Yes | Result of the most recent registered retrieval attempt. | Controlled value from the list below; it describes access, not truth or authority. |
| `retrieved_at` | No | Exact time at which the registered content was retrieved. | ISO 8601/RFC 3339 timestamp with timezone; blank when an exact timestamp was not captured. |
| `effective_date` | No | Exact date on which a law, contract, policy, or version became effective. | ISO date; blank when the source has multiple effective dates or the exact date is not established. Do not substitute `published_date` or `accessed_date`. |
| `content_sha256` | Conditional | Digest of the exact locally stored bytes. | Lowercase 64-hex SHA-256. Required exactly with `local_snapshot`, must match that file, and blank otherwise. |
| `notes` | No | Limits, version conflict, access status, or what the source can prove. | State when material is vendor-authored, high-level only, moved, or unavailable. |

Allowed `retrieval_status` values:

- `Retrieved` — the source content was directly retrieved sufficiently to support its registered use. This does not independently verify the publisher's claims.
- `Partially retrieved` — only part of the source or a limited official extraction was recovered; `notes` identifies the usable portion and limitation.
- `Indexed-only` — only indexed metadata or indexed content was available; it may support an unresolved lead or retrieval-gap statement, not an unqualified substantive finding.
- `Unavailable or access-blocked` — direct access failed and no sufficient content was recovered.
- `Broken link` — the registered URL was confirmed broken, such as an HTTP 404 response.
- `Not rechecked` — a carried-forward register entry was not checked in the current evidence pass.

Any status other than `Retrieved` requires a retrieval-limit explanation in `notes`. `archived_url` and `local_snapshot` remain blank unless the archive or file actually exists; neither may be inferred from indexed text. A source with limited retrieval may be cited only for the portion or access condition its row says is recoverable.

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
claim_id,requirement_id,subject,jurisdiction,responsible_actor,actor_override_reason,finding,documented_policy,technical_control,deployed_configuration,deployment_basis,independent_verification,evidence_label,verified_fact,assessment,known_fact_basis,implementation_state,deployment_evidence_state,historical_as_of,applicability_reason,binding_obligation,last_verified,source_ids,unresolved_question,next_action,notes
```

| Column | Required | Definition | Rules and example |
|---|---:|---|---|
| `claim_id` | Yes | Stable identifier for the evaluated claim. | Unique `FS-GLOBAL-###`, `FS-CT-###`, or `FS-CT-FAIRFIELD-###`. |
| `requirement_id` | Yes | OASPS requirement being evaluated. | Must resolve to a heading in `STANDARD.md`. A local factual row that informs multiple requirements uses the most direct requirement and explains cross-cutting relevance in notes. |
| `subject` | Yes | System, capability, agency, contract, or deployment evaluated. | Example `Flock ALPR platform — search purpose`. |
| `jurisdiction` | Yes | Scope of the finding. | Example `Global` or `Fairfield, Connecticut`. |
| `responsible_actor` | Yes | Actor able or obligated to satisfy the requirement. | Controlled values below. |
| `actor_override_reason` | Conditional | Why the row uses an actor different from the requirement's actor in `STANDARD.md`. | Required exactly when the actors differ; blank otherwise. Describe the narrower row scope, not a reassignment of the standard. |
| `finding` | Yes | Concise evidence-bounded conclusion. | Must distinguish assertion, capability, configuration, and current unknowns. |
| `documented_policy` | Yes | What written policy, contract, law, term, or announcement says. | Use `No public evidence located` when that absence is itself the scoped result; do not write `N/A` unless the row is assessed `Not applicable`. |
| `technical_control` | Yes | Described or observed enforcement, logging, prevention, or verification mechanism. | State `Unknown from public evidence` when appropriate. |
| `deployed_configuration` | Yes | Version, local setting, rollout state, or production condition in scope. | Historical conditions include the date; current unknowns remain explicit. Current deployment evidence is represented explicitly by `deployment_evidence_state` and `deployment_basis`, not inferred from wording in this field. |
| `deployment_basis` | Conditional | Evidence basis for treating behavior as deployed now. | Required for `Deployed now`; identify the cited material and preserve vendor, scope, rollout, and customer-configuration limits. Blank for every other implementation state. |
| `independent_verification` | Yes | What an external party can establish and the boundary of that proof. | Distinguish primary records from vendor claims and NDA-gated assessments. |
| `evidence_label` | Yes | Confidence in the underlying fact. | Controlled values below. |
| `verified_fact` | Conditional | Exact fact directly established by the cited evidence. | Required for `Verified`; distinguish a verified published statement or document comparison from independently verified product behavior. Blank for other labels. |
| `assessment` | Yes | Comparison with the requirement. | Controlled values below. |
| `known_fact_basis` | Conditional | Narrow basis for a definitive assessment made despite an `Unknown` evidence label. | Required only when `Unknown` is paired with `Meets`, `Partly meets`, or `Does not meet`; identify the separately known fact sufficient for that limited assessment. Blank for `Unknown` or `Not applicable` assessments and for all other evidence labels. |
| `implementation_state` | Yes | Timing or configurability of behavior. | Controlled values below. |
| `deployment_evidence_state` | Conditional | Controlled indicator that the cited `deployment_basis` affirmatively supports current deployment within the row's scope. | The only nonblank value is `Affirmative`. Required exactly for `Deployed now` and blank for every other implementation state. It records the evidence posture and does not imply independent verification. |
| `historical_as_of` | Conditional | Date of the past-only state represented by a `Historical` row. | Required for `Historical` and blank otherwise; ISO date. It is not the later evidence-check date. |
| `applicability_reason` | Conditional | Why comparison with the requirement is not meaningful for this row. | Required for `Not applicable` and blank otherwise. A context row must identify what it does and does not assess. |
| `binding_obligation` | Conditional | Binding law, contract, order, or other enforceable duty violated by a `Noncompliant` finding. | Required for `Noncompliant`, supported by `source_ids`, and blank otherwise. `Does not meet` the proposed OASPS standard is not legal noncompliance. |
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
- `Historical`
- `Announced or future`
- `Optional or customer-configurable`
- `Jurisdiction-specific`
- `Unknown`

Allowed nonblank `deployment_evidence_state` value:

- `Affirmative`

## Matrix conditional-field invariants

- `actor_override_reason` is present only when `responsible_actor` differs from the actor assigned to `requirement_id` in `STANDARD.md`.
- `deployment_basis` is present for every `Deployed now` row and blank for all other states.
- `deployment_evidence_state` is exactly `Affirmative` for every `Deployed now` row and blank for all other states; it indicates that the cited `deployment_basis` affirmatively supports current-in-scope deployment without implying independent verification.
- `verified_fact` is present for every `Verified` row and blank for all other evidence labels.
- `known_fact_basis` is required only when `Unknown` evidence is paired with the definitive assessment `Meets`, `Partly meets`, or `Does not meet`; it is blank for every other combination.
- `historical_as_of` is present for every `Historical` row and blank for all other states.
- `applicability_reason` is present for every `Not applicable` assessment and blank otherwise.
- `binding_obligation` is present for every `Noncompliant` evidence label and blank otherwise.
- `evidence_label`, `assessment`, and `implementation_state` answer different questions and must not be inferred from one another.

## Example matrix row

```csv
claim_id,requirement_id,subject,jurisdiction,responsible_actor,actor_override_reason,finding,documented_policy,technical_control,deployed_configuration,deployment_basis,independent_verification,evidence_label,verified_fact,assessment,known_fact_basis,implementation_state,deployment_evidence_state,historical_as_of,applicability_reason,binding_obligation,last_verified,source_ids,unresolved_question,next_action,notes
FS-GLOBAL-001,OASPS-A01,Flock ALPR platform — data inventory,Global,Shared,,"Public materials identify several collected and derived fields but no single exhaustive versioned schema was located.","The LPR policy names core observation fields; product material describes additional derived search capabilities.","Public pages describe plate interpretation, confidence filtering, hot-list matching, and vehicle-oriented search functions.","Feature-dependent; no complete production field inventory is public.",,"An external reader can compare public pages but cannot establish every production field or derivation.",Partially verifiable,,Partly meets,,Optional or customer-configurable,,,,,2026-08-14,SRC-0010|SRC-0020,"Which collected, derived, searchable, exported, and internally used fields exist in each deployed version?","Obtain a versioned field and data-flow inventory through lawful public documentation or independent review.","Vendor sources establish public descriptions, not exhaustive production behavior."
```

## Validation expectations

`python scripts/validate.py` checks:

- exact header order;
- required fields;
- unique and correctly formatted IDs;
- controlled values;
- ISO dates and timezone-bearing timestamps;
- lowercase 64-hex SHA-256 values and local-snapshot hash requirements;
- retrieval-status notes and conditional matrix-field invariants;
- source-reference resolution;
- requirement-reference resolution;
- case-study narrative citation-marker syntax and source-ID resolution;
- required repository files and practical internal Markdown links.

Passing validation establishes repository consistency, not factual truth, legal compliance, accreditation, or security assurance.
