# Evidence Register

[`sources.csv`](sources.csv) is the repository's single stable register for sources used by the standard crosswalks, Flock Safety case study, and Fairfield implementation record.

## What a source row means

A source row records identity, retrieval metadata, scope, and limitations. Inclusion does not endorse the source or prove every statement it contains. A vendor page supports what the vendor publicly states; an old contract supports the contracted state at that time; a transparency portal supports only the fields and historical snapshot it exposes.

Source IDs are permanent. If a URL changes, becomes unavailable, or is superseded, keep the original ID and document the change rather than silently reassigning it.

## Citation use

- Narrative factual paragraphs end with source IDs in brackets.
- Matrix rows use pipe-separated source IDs.
- Every cited ID must resolve to one register row.
- Conflicts cite each relevant source and describe the difference.
- Missing evidence produces an explicit unknown or withheld claim, not an invented citation.

See [`DATA-DICTIONARY.md`](../DATA-DICTIONARY.md) for exact columns and controlled values.

## Sensitive material

Do not add credentials, plate numbers, personal travel histories, private contact information, nonpublic operational details, or unredacted records containing unnecessary personal data. Prefer a stable public URL plus metadata. Follow [`snapshots/README.md`](snapshots/README.md) before storing a local copy.
