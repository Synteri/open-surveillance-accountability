# Evidence Snapshot Policy

The first repository build stores source links and metadata, not source-document copies.

Add a local snapshot only when all of the following are true:

1. the material was obtained lawfully and may be redistributed;
2. preserving a changing public source is necessary to support a consequential claim;
3. the copy contains no credentials, raw plate numbers, personal travel records, requester address, private email, or unrelated personal data;
4. required redactions are complete and documented;
5. the original publisher, title, retrieval date, source ID, and original URL remain clear;
6. the repository's content license does not misrepresent third-party copyright or licensing.

If redistribution rights are uncertain, do not commit the document. Record the retrieval date, description, and lawful access note in the source register or an issue instead. A checksum proves file identity, not truth or permission to redistribute, and the repository records one only for a committed local snapshot that the validator can verify.

Snapshots must use descriptive filenames without personal data and must be reviewed before commit. Use repository-relative paths under `evidence/snapshots/` and only UTF-8 `.txt`, `.md`, `.json`, or `.csv`. Do not store PDFs, executable files, scripts, office files, or web archives.

After any authorized redaction, compute SHA-256 over the exact bytes that would be committed and record the lowercase 64-hex digest in `content_sha256`. Record `retrieved_at` only when the exact retrieval timestamp and timezone are known. Do not infer it from `accessed_date`, and leave both timestamp and hash fields blank when the exact evidence is absent.

No snapshot is present in `0.3.0-draft.1`.
