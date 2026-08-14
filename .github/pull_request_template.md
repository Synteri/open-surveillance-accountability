## Contribution type

- [ ] Evidence correction or source update
- [ ] Framework or responsible-actor change
- [ ] Technical-feasibility improvement
- [ ] Local evidence or jurisdiction update
- [ ] Editorial, glossary, tooling, or repository-maintenance change

## Summary

Describe the change in plain language. Explain why it is needed and what a resident or reviewer should understand differently after it is accepted.

## Affected material

List every affected requirement ID, finding ID, source ID, jurisdiction, and file. If this introduces a new requirement or materially changes an assessment, explain the decision and update the appropriate changelog.

## Evidence and reasoning

For each factual change:

- link the primary or strongest available source;
- give its publisher, relevant date, and access date;
- explain exactly what it supports and what it does not support;
- identify conflicts with existing sources;
- distinguish documented policy, technical control, deployed configuration, independent verification, and announced future behavior.

Do not infer production behavior solely from vendor prose. Do not turn missing public evidence into a negative finding.

## Uncertainty and fair treatment

What remains `Unknown`, `Partially verifiable`, customer-configurable, jurisdiction-specific, or time-sensitive? Which positive findings or reasonable counterarguments must remain visible?

## Privacy, security, and publication checklist

- [ ] I added no raw plate data, personal travel records, unnecessary personal information, credentials, nonpublic operational material, or exploit instructions.
- [ ] I did not rely on or describe unauthorized testing.
- [ ] Every new source ID exists in `evidence/sources.csv` and directly supports the claim that cites it.
- [ ] Consequential factual paragraphs in case-study narratives end with supporting source IDs.
- [ ] The change does not claim accreditation, certification, expert approval, formal outside-framework conformity, endorsement, or unsupported wrongdoing.
- [ ] The change does not enable publication, GitHub Pages, deployment, tagging, release creation, or external posting.
- [ ] I have the right to contribute the submitted material under CC BY 4.0 for content or MIT for code.

## Validation

Run from the repository root and paste the outcome:

```text
python scripts/validate.py
```

If validation could not run or a check remains unresolved, explain why. Do not hide a failed check.

## Review is not endorsement

- [ ] I understand that submitting, reviewing, or accepting this contribution does not imply endorsement of OASPS, its author, or any finding unless separately and explicitly stated.
