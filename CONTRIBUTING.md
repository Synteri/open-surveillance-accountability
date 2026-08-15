# Contributing to OASPS

OASPS `0.4.0-draft.1` is an open public working draft released for review, correction, and good-faith criticism. It is not a stable standard, certification, legal determination, or finding of wrongdoing. Careful disagreement, corrections, local records, and technical criticism are welcome through public issues and pull requests. Review is voluntary and unpaid at this stage.

Submitting feedback does **not** mean that you endorse OASPS, its findings, or its author. The project will not describe your participation as endorsement unless you explicitly authorize that description. You may participate using only your GitHub username.

## Choose the right contribution path

Use the repository's [issue forms](https://github.com/Synteri/open-surveillance-accountability/issues/new/choose) for:

- **Evidence correction:** a claim, date, source, quotation, or characterization is wrong, unsupported, or out of date.
- **Framework feedback:** a requirement is unnecessary, insufficient, unfair, unclear, infeasible, or assigned to the wrong responsible actor.
- **Local evidence:** a contract, policy, audit, public-record response, transparency portal, statute, or other jurisdiction-specific record may change an assessment.
- **Technical feasibility:** use the framework-feedback form to explain why a proposed safeguard is impossible, ineffective, underspecified, or needs a better implementation path.

Use a pull request when you can propose a specific, reviewable change. A pull request should identify the affected requirement, finding, or source IDs and explain what the evidence establishes and what remains unknown.

## Evidence standards

Good submissions make it possible for another reader to inspect the basis for a change. When available, include:

- the stable source URL or a lawful public archive URL;
- title, publisher, publication date, and access date;
- the exact claim or stable ID affected;
- a short explanation of what the source supports and what it does not support;
- jurisdiction and relevant date range;
- any conflict with an existing source;
- whether the material is primary evidence, vendor material, independent research, or reporting.

A vendor page supports a statement about what the vendor publicly says. It does not, by itself, establish the complete production implementation. Missing public evidence should remain `Unknown`; it should not be converted into a negative finding.

If a source URL is unavailable, describe the record and how it can lawfully be verified. Do not invent a replacement citation. Maintainers may withhold a factual change until a recoverable source is available.

## Privacy and safety

Do not submit or upload:

- raw license-plate numbers or images containing readable plates;
- personal travel histories or location trails;
- names or contact details of ordinary individuals when unnecessary to the claim;
- requester home addresses, private email addresses, credentials, or authentication tokens;
- nonpublic technical or operational material;
- exploit instructions or results from unauthorized testing.

Redact unrelated personal information from public records before sharing them. If a document cannot be shared safely, describe it at a high level and ask the maintainer for a private, responsible review path. Potential vulnerabilities should be handled through responsible disclosure, not a public issue.

## Pull-request checklist

Before opening a pull request:

1. Keep the standard vendor-neutral and put product-specific findings in the appropriate case-study directory.
2. Use existing controlled values and stable ID formats from `DATA-DICTIONARY.md`.
3. Add every new source to `evidence/sources.csv` before citing its source ID.
4. Put consequential factual sections between `<!-- oasps-citations:start -->` and `<!-- oasps-citations:end -->`, and end each factual paragraph or list item in those sections with supporting source IDs. An immediately preceding `<!-- oasps-citation-exempt: reason -->` comment may exempt only a genuinely normative, methodological, editorial, question-only, or navigation block; see `AGENTS.md` for the controlled reasons.
5. Preserve positive findings, source conflicts, and unresolved questions.
6. Update the relevant changelog when meaning, evidence, or an assessment changes.
7. Run `python -m unittest discover -s tests -v` and `python scripts/validate.py`, and report both results in the pull request.

## Review and disposition

Substantive objections should remain visible through issue, pull-request, or changelog history. Maintainers may accept, revise, defer, or decline a proposal, but should explain the disposition of serious criticism. Acceptance means only that a change met the project's evidence and editorial rules; it is not a certification of any vendor or agency.

By contributing, you agree that your contribution may be distributed under the repository's applicable license: CC BY 4.0 for documentation and structured factual content, and MIT for validation code. Do not contribute material you do not have the right to share under those terms.
