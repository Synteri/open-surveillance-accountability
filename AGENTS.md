# Instructions for repository agents

These instructions apply to every automated or assisted change in this repository. The project is an evidence-forward public draft, not a software product, certification program, or venue for unsupported accusations.

## Governing sources

1. Released GitHub tags are the authoritative public versions after an approved public release.
2. Before release, the repository is the implementation copy and the private OASPS research workspace is the source for factual and policy content.
3. Research notes do not silently become accepted claims. Moving research into this repository must be visible in a commit or pull request.
4. Do not add a new OASPS requirement, change a responsible actor, or materially change an assessment without documenting the reason in the pull request and changelog.

## Evidence rules

- Never invent a fact, source, source ID, quotation, date, implementation detail, or review outcome.
- Preserve `Unknown` when public evidence is insufficient. Missing evidence is not evidence of misconduct or noncompliance.
- Keep evidence strength separate from the assessment against a requirement. A vendor statement can establish what the vendor says without independently proving production behavior.
- Keep documented policy, technical control, deployed configuration, independent verification, and announced future behavior separate.
- Preserve credible positive findings and conflicting documentation. Do not select only the evidence that supports a preferred conclusion.
- Consequential factual narrative sections are bounded by `<!-- oasps-citations:start -->` and `<!-- oasps-citations:end -->`. Within those sections, each prose paragraph or list item must end with one or more source IDs in brackets, such as `[SRC-0007]`.
- A deliberately normative, methodological, editorial, question-only, or navigation paragraph inside a designated factual section may be exempted only by placing an immediately preceding `<!-- oasps-citation-exempt: reason -->` comment, where `reason` is `normative`, `methodological`, `editorial`, `question`, or `navigation`. The annotation applies only to the next paragraph or list block and must never be used to exempt a factual claim.
- Every cited source ID must exist in `evidence/sources.csv` and must support the claim immediately before it.
- Use stable identifiers. Never recycle a published requirement, source, or finding ID; mark withdrawn items and explain the withdrawal.
- Prefer short paraphrases to quotations. Label marketing material as vendor evidence, not independent verification.
- Do not make legal conclusions beyond a careful summary of cited law and records.

## Scope and editorial rules

- Keep `STANDARD.md` vendor-neutral. Flock-specific and Fairfield-specific findings belong only in their case-study files.
- Write for ordinary residents first. Explain necessary technical terms in plain language and add them to `GLOSSARY.md` when appropriate.
- Assign responsibility accurately among Vendor, Agency, Legislature, Court, Independent oversight, and Shared.
- Do not describe OASPS as accredited, certified, expert-approved, or formally conformant with an outside framework.
- Do not state or imply that Flock Safety, Fairfield, an agency, an officer, or any other party committed wrongdoing unless direct, appropriately cited evidence supports the precise statement.
- Keep recognized-framework crosswalks modest. Do not reproduce copyrighted standards or invent clause-level mappings without lawful access to the complete text.
- Keep the first build mostly Markdown and CSV with one small validation script. Do not add a website, database, API, scraper, map, or deployment system without an explicit project decision.

## Privacy, security, and safety

- Never commit credentials, tokens, internal-only system details, nonpublic technical material, raw plate numbers, personal travel records, requester home addresses, private email addresses, or unnecessary personal data.
- Redact public records before committing them when they contain personal contact information or unrelated personal data.
- Do not publish instructions for defeating, damaging, exploiting, or bypassing surveillance systems.
- Do not conduct unauthorized testing against Flock Safety, Fairfield, or any agency system. Route potential vulnerabilities through responsible disclosure.
- Mention public camera locations only when they are already lawfully public and necessary to an accountability claim; default to aggregate or policy-level discussion.

## Repository and release controls

- Do not change repository visibility, enable GitHub Pages, create or push a tag, create a GitHub Release, merge the bootstrap pull request, or announce/post the project without explicit owner instruction.
- Do not contact vendors, agencies, reviewers, or other third parties, and do not submit public-record requests, without separate authorization.
- Do not rewrite released history.
- Treat contributor feedback as voluntary criticism or evidence, not endorsement, unless the contributor explicitly authorizes an endorsement statement.

## Required checks before handoff

1. Run `python -m unittest discover -s tests -v` and `python scripts/validate.py` from the repository root.
2. Inspect changed links, source IDs, controlled values, dates, and citations.
3. Confirm that no secrets, plate data, personal travel records, unnecessary personal information, or nonpublic operational details were added.
4. Review the diff for unsupported claims and accidental publication, certification, conformity, endorsement, or wrongdoing language.
5. Report the validation result, unresolved source gaps, and any part of the research material that could not be translated faithfully.

If validation cannot run or fails, do not hide the result. Explain the limitation and leave the repository state reviewable.
