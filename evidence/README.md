# Evidence Register

[`sources.csv`](sources.csv) is the repository's single stable register for sources used by the standard crosswalks, Flock Safety case study, and Fairfield implementation record.

## What a source row means

A source row records identity, retrieval metadata, scope, and limitations. Inclusion does not endorse the source or prove every statement it contains. A vendor page supports what the vendor publicly states; an executed historical contract supports the terms it contains at that time but not a later production configuration; a municipal meeting packet containing an order form supports the terms presented for approval unless execution evidence exists; and a directly retrieved transparency portal supports only the fields exposed at the recorded check. Indexed-only portal material is an unresolved lead unless the relevant content is recovered in a durable lawful form.

Source IDs are permanent. If a URL changes, becomes unavailable, or is superseded, keep the original ID and document the change rather than silently reassigning it.

## Retrieval metadata

`retrieval_status` distinguishes direct retrieval from partial retrieval, indexed-only material, access failure, a broken link, or a source not rechecked in the current pass. `accessed_date` records the day of the retrieval or check. `retrieved_at` is more precise and remains blank unless an exact timestamp with timezone was captured.

`published_date`, `effective_date`, and `accessed_date` are different facts. Do not infer an effective date from publication, or an exact retrieval timestamp from the accessed date. `archived_url` remains blank unless the archive actually exists. `local_snapshot` and `content_sha256` are populated together only when the file exists and its exact digest can be verified. A limited retrieval status must be explained in `notes` and limits what the row can support.

## Citation use

- Designated factual sections use `<!-- oasps-citations:start -->` and `<!-- oasps-citations:end -->` boundaries.
- Every factual paragraph or list item inside a designated section ends with source IDs in brackets.
- An immediately preceding `<!-- oasps-citation-exempt: reason -->` may exempt only a normative, methodological, editorial, question-only, or navigation block, using the controlled reasons documented in the data dictionary.
- Narrative markers use `[SRC-0010]` or `[SRC-0010, SRC-0016]` with a comma and one space.
- Matrix rows use pipe-separated source IDs.
- Every cited ID must resolve to one register row.
- Conflicts cite each relevant source and describe the difference.
- Missing evidence produces an explicit unknown or withheld claim, not an invented citation.
- `Indexed-only`, `Unavailable or access-blocked`, and `Broken link` entries support only the recoverable indexed fact, access condition, or unresolved lead described in their notes.

See [`DATA-DICTIONARY.md`](../DATA-DICTIONARY.md) for exact columns and controlled values.

## Sensitive material

Do not add credentials, plate numbers, personal travel histories, private contact information, nonpublic operational details, or unredacted records containing unnecessary personal data. Prefer a stable public URL plus metadata. Follow [`snapshots/README.md`](snapshots/README.md) before storing a local copy.
