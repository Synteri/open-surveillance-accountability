#!/usr/bin/env python3
"""Validate the consistency and safety guardrails of the OASPS repository.

The script intentionally depends only on the Python standard library.  Its
repository root is derived from this file, so it can be invoked from any
working directory.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "0.2.0-draft.1"

REQUIRED_DIRECTORIES = (
    ".github",
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "case-studies",
    "case-studies/flock-safety",
    "case-studies/flock-safety/jurisdictions",
    "case-studies/flock-safety/jurisdictions/connecticut",
    "evidence",
    "evidence/snapshots",
    "scripts",
    "standard",
    "standard/crosswalks",
)

REQUIRED_FILES = (
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/evidence-correction.yml",
    ".github/ISSUE_TEMPLATE/framework-feedback.yml",
    ".github/ISSUE_TEMPLATE/local-evidence.yml",
    ".github/pull_request_template.md",
    ".github/workflows/validate.yml",
    ".gitignore",
    "AGENTS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "DATA-DICTIONARY.md",
    "DISCLAIMER.md",
    "GLOSSARY.md",
    "LICENSE-CODE",
    "LICENSE-CONTENT",
    "METHODOLOGY.md",
    "README.md",
    "ROADMAP.md",
    "STANDARD.md",
    "VERSION",
    "case-studies/flock-safety/CHANGELOG.md",
    "case-studies/flock-safety/FINDINGS.md",
    "case-studies/flock-safety/README.md",
    "case-studies/flock-safety/SCOPE.md",
    "case-studies/flock-safety/UNRESOLVED.md",
    "case-studies/flock-safety/jurisdictions/connecticut/README.md",
    "case-studies/flock-safety/jurisdictions/connecticut/fairfield.md",
    "case-studies/flock-safety/matrix.csv",
    "evidence/README.md",
    "evidence/snapshots/README.md",
    "evidence/sources.csv",
    "scripts/validate.py",
    "standard/crosswalks/README.md",
    "standard/crosswalks/convention-108-plus.md",
    "standard/crosswalks/iacp-bja-alpr.md",
    "standard/crosswalks/iso-27701.md",
    "standard/crosswalks/nist-privacy-framework.md",
    "standard/crosswalks/nist-sp-800-53.md",
)

SOURCE_HEADER = (
    "source_id",
    "title",
    "publisher",
    "url",
    "source_type",
    "published_date",
    "accessed_date",
    "jurisdiction",
    "archived_url",
    "local_snapshot",
    "notes",
)

MATRIX_HEADER = (
    "claim_id",
    "requirement_id",
    "subject",
    "jurisdiction",
    "responsible_actor",
    "finding",
    "documented_policy",
    "technical_control",
    "deployed_configuration",
    "independent_verification",
    "evidence_label",
    "assessment",
    "implementation_state",
    "last_verified",
    "source_ids",
    "unresolved_question",
    "next_action",
    "notes",
)

SOURCE_REQUIRED_FIELDS = (
    "source_id",
    "title",
    "publisher",
    "url",
    "source_type",
    "accessed_date",
    "jurisdiction",
)

MATRIX_REQUIRED_FIELDS = tuple(
    field for field in MATRIX_HEADER if field not in {"source_ids", "notes"}
)

ALLOWED_SOURCE_TYPES = frozenset(
    {
        "Law",
        "Contract",
        "Government record",
        "Vendor legal",
        "Vendor technical",
        "Vendor announcement",
        "Transparency portal",
        "Professional guidance",
        "Security assessment",
        "Research",
        "Reporting",
    }
)

ALLOWED_ACTORS = frozenset(
    {"Vendor", "Agency", "Legislature", "Court", "Independent oversight", "Shared"}
)
ALLOWED_EVIDENCE_LABELS = frozenset(
    {"Verified", "Vendor-asserted", "Partially verifiable", "Unknown", "Noncompliant"}
)
ALLOWED_ASSESSMENTS = frozenset(
    {"Meets", "Partly meets", "Does not meet", "Unknown", "Not applicable"}
)
ALLOWED_IMPLEMENTATION_STATES = frozenset(
    {
        "Deployed now",
        "Announced or future",
        "Optional or customer-configurable",
        "Jurisdiction-specific",
        "Unknown",
    }
)

EXPECTED_REQUIREMENT_IDS = frozenset(
    [*(f"OASPS-A{number:02d}" for number in range(1, 5))]
    + [*(f"OASPS-B{number:02d}" for number in range(1, 6))]
    + [*(f"OASPS-C{number:02d}" for number in range(1, 7))]
    + [*(f"OASPS-D{number:02d}" for number in range(1, 7))]
    + [*(f"OASPS-E{number:02d}" for number in range(1, 7))]
    + [*(f"OASPS-F{number:02d}" for number in range(1, 6))]
)

SOURCE_ID_RE = re.compile(r"SRC-[0-9]{4}\Z")
CLAIM_ID_RE = re.compile(r"(?:FS-GLOBAL|FS-CT|FS-CT-FAIRFIELD)-[0-9]{3}\Z")
REQUIREMENT_ID_RE = re.compile(r"OASPS-[A-F][0-9]{2}\Z")
REQUIREMENT_HEADING_RE = re.compile(r"^###\s+(?P<requirement_id>OASPS-\S+)")
ISO_DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}\Z")

# This intentionally covers ordinary inline Markdown links rather than trying
# to implement a complete Markdown parser.  It handles all repository-local
# links used by this first build, including optional quoted link titles.
MARKDOWN_LINK_RE = re.compile(
    r"(?<!!)\[[^\]\n]*\]\(\s*(?P<target><[^>\n]+>|[^)\s]+)"
    r"(?:\s+(?:\"[^\"\n]*\"|'[^'\n]*'))?\s*\)"
)
BRACKET_RE = re.compile(r"\[[^\]\n]*\]")
BRACKETED_SOURCE_TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9])SRC-[A-Za-z0-9#?-]+", re.IGNORECASE
)

# A deliberately conservative privacy guard.  It catches common US plate
# shapes when explicitly introduced as a plate/tag, plus the distinctive
# California-style 1ABC234 shape.  It does not print the candidate value in an
# error, which avoids repeating potentially sensitive data in CI logs.
CONTEXTUAL_PLATE_RE = re.compile(
    r"\b(?:license\s+plate|plate|vehicle\s+tag)"
    r"(?:\s+(?:number|no\.?))?\s*(?:is|was|[:#=])?\s*[\"']?"
    r"(?P<plate>(?=[A-Z0-9-]{5,9}\b)(?=[A-Z0-9-]*[0-9])"
    r"[A-Z0-9]{1,4}(?:-?[A-Z0-9]{1,4})?)\b",
    re.IGNORECASE,
)
CALIFORNIA_STYLE_PLATE_RE = re.compile(r"\b[0-9][A-Z]{3}[0-9]{3}\b", re.IGNORECASE)

SOURCE_NARRATIVE_FIELDS = (
    "title",
    "publisher",
    "jurisdiction",
    "notes",
)
MATRIX_NARRATIVE_FIELDS = (
    "subject",
    "jurisdiction",
    "finding",
    "documented_policy",
    "technical_control",
    "deployed_configuration",
    "independent_verification",
    "unresolved_question",
    "next_action",
    "notes",
)


class Validator:
    """Collect all useful errors before returning a nonzero status."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, location: str, message: str) -> None:
        self.errors.append(f"{location}: {message}")

    @staticmethod
    def relative(path: Path) -> str:
        try:
            return path.relative_to(ROOT).as_posix()
        except ValueError:
            return str(path)

    def validate_required_tree(self) -> None:
        for relative_path in REQUIRED_DIRECTORIES:
            path = ROOT / relative_path
            if not path.exists():
                self.error(relative_path, "required directory is missing")
            elif not path.is_dir():
                self.error(relative_path, "required path must be a directory")

        for relative_path in REQUIRED_FILES:
            path = ROOT / relative_path
            if not path.exists():
                self.error(relative_path, "required file is missing")
            elif not path.is_file():
                self.error(relative_path, "required path must be a regular file")

        expected_paths = set(REQUIRED_DIRECTORIES) | set(REQUIRED_FILES)
        actual_paths = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if ".git" not in path.relative_to(ROOT).parts
        }
        for relative_path in sorted(actual_paths - expected_paths):
            self.error(
                relative_path,
                "unexpected path is outside the first-build repository structure",
            )

    def validate_version(self) -> None:
        path = ROOT / "VERSION"
        if not path.is_file():
            return
        try:
            contents = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error("VERSION", f"could not read UTF-8 text ({exc})")
            return

        permitted_contents = {
            EXPECTED_VERSION,
            f"{EXPECTED_VERSION}\n",
            f"{EXPECTED_VERSION}\r\n",
        }
        if contents not in permitted_contents:
            self.error(
                "VERSION",
                f"must contain exactly {EXPECTED_VERSION!r} as its only line",
            )

    def read_csv(
        self, relative_path: str, expected_header: tuple[str, ...]
    ) -> list[tuple[int, dict[str, str]]]:
        path = ROOT / relative_path
        if not path.is_file():
            return []

        records: list[tuple[int, dict[str, str]]] = []
        try:
            with path.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.reader(handle)
                try:
                    header = next(reader)
                except StopIteration:
                    self.error(relative_path, "CSV is empty; expected a header row")
                    return []

                if tuple(header) != expected_header:
                    self.error(
                        f"{relative_path}:1",
                        "header must be exactly, in order: " + ",".join(expected_header),
                    )
                    return []

                for row in reader:
                    line_number = reader.line_num
                    if not row or all(not cell.strip() for cell in row):
                        self.error(
                            f"{relative_path}:{line_number}",
                            "blank data rows are not allowed",
                        )
                        continue
                    if len(row) != len(expected_header):
                        self.error(
                            f"{relative_path}:{line_number}",
                            f"expected {len(expected_header)} fields but found {len(row)}",
                        )
                        continue
                    records.append((line_number, dict(zip(expected_header, row))))
        except (OSError, UnicodeError, csv.Error) as exc:
            self.error(relative_path, f"could not parse UTF-8 CSV ({exc})")
            return []

        if not records:
            self.error(relative_path, "must contain at least one data row")
        return records

    def require_fields(
        self,
        relative_path: str,
        line_number: int,
        record: dict[str, str],
        required_fields: tuple[str, ...],
    ) -> None:
        for field in required_fields:
            if not record[field].strip():
                self.error(
                    f"{relative_path}:{line_number}",
                    f"required field {field!r} is blank",
                )

    def validate_iso_date(
        self,
        relative_path: str,
        line_number: int,
        field: str,
        value: str,
    ) -> None:
        if not ISO_DATE_RE.fullmatch(value):
            self.error(
                f"{relative_path}:{line_number}",
                f"{field!r} must use ISO calendar date YYYY-MM-DD",
            )
            return
        try:
            parsed = date.fromisoformat(value)
        except ValueError:
            self.error(
                f"{relative_path}:{line_number}",
                f"{field!r} is not a real calendar date",
            )
            return
        if parsed.isoformat() != value:
            self.error(
                f"{relative_path}:{line_number}",
                f"{field!r} must use canonical YYYY-MM-DD form",
            )

    def validate_no_plate_literal(
        self,
        relative_path: str,
        line_number: int,
        record: dict[str, str],
        narrative_fields: tuple[str, ...],
    ) -> None:
        for field in narrative_fields:
            value = record[field]
            if CONTEXTUAL_PLATE_RE.search(value) or CALIFORNIA_STYLE_PLATE_RE.search(value):
                self.error(
                    f"{relative_path}:{line_number}",
                    f"field {field!r} contains a possible public plate literal; redact it",
                )

    def validate_sources(
        self,
    ) -> tuple[set[str], list[tuple[int, dict[str, str]]]]:
        relative_path = "evidence/sources.csv"
        records = self.read_csv(relative_path, SOURCE_HEADER)
        source_ids: list[str] = []

        for line_number, record in records:
            self.require_fields(
                relative_path, line_number, record, SOURCE_REQUIRED_FIELDS
            )

            source_id = record["source_id"].strip()
            if source_id:
                source_ids.append(source_id)
                if not SOURCE_ID_RE.fullmatch(source_id):
                    self.error(
                        f"{relative_path}:{line_number}",
                        "source_id must match SRC-####",
                    )

            source_type = record["source_type"].strip()
            if source_type and source_type not in ALLOWED_SOURCE_TYPES:
                self.error(
                    f"{relative_path}:{line_number}",
                    f"source_type {source_type!r} is not an allowed value",
                )

            published_date = record["published_date"].strip()
            if published_date:
                self.validate_iso_date(
                    relative_path, line_number, "published_date", published_date
                )

            accessed_date = record["accessed_date"].strip()
            if accessed_date:
                self.validate_iso_date(
                    relative_path, line_number, "accessed_date", accessed_date
                )

            url = record["url"].strip()
            if url and not url.startswith("https://"):
                self.error(
                    f"{relative_path}:{line_number}",
                    "url must begin with https://",
                )

            archived_url = record["archived_url"].strip()
            if archived_url and not archived_url.startswith("https://"):
                self.error(
                    f"{relative_path}:{line_number}",
                    "archived_url must begin with https:// when provided",
                )

            local_snapshot = record["local_snapshot"].strip()
            if local_snapshot:
                self.validate_repository_relative_file(
                    relative_path,
                    line_number,
                    "local_snapshot",
                    local_snapshot,
                )

            self.validate_no_plate_literal(
                relative_path,
                line_number,
                record,
                SOURCE_NARRATIVE_FIELDS,
            )

        for source_id, count in Counter(source_ids).items():
            if count > 1:
                self.error(
                    relative_path,
                    f"source_id {source_id!r} appears {count} times; IDs must be unique",
                )

        return set(source_ids), records

    def validate_repository_relative_file(
        self,
        csv_path: str,
        line_number: int,
        field: str,
        value: str,
    ) -> None:
        candidate_path = Path(value)
        if candidate_path.is_absolute():
            self.error(
                f"{csv_path}:{line_number}",
                f"{field!r} must be a repository-relative path",
            )
            return

        candidate = (ROOT / candidate_path).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError:
            self.error(
                f"{csv_path}:{line_number}",
                f"{field!r} must not escape the repository",
            )
            return
        if not candidate.is_file():
            self.error(
                f"{csv_path}:{line_number}",
                f"{field!r} does not resolve to a committed file",
            )

    def validate_standard(self) -> set[str]:
        path = ROOT / "STANDARD.md"
        if not path.is_file():
            return set()
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error("STANDARD.md", f"could not read UTF-8 text ({exc})")
            return set()

        found_ids: list[str] = []
        for line_number, line in enumerate(text.splitlines(), start=1):
            if not line.startswith("###") or "OASPS-" not in line:
                continue
            match = REQUIREMENT_HEADING_RE.match(line)
            if match is None:
                self.error(
                    f"STANDARD.md:{line_number}",
                    "requirement heading must start with '### OASPS-X##'",
                )
                continue
            requirement_id = match.group("requirement_id")
            if not REQUIREMENT_ID_RE.fullmatch(requirement_id):
                self.error(
                    f"STANDARD.md:{line_number}",
                    f"requirement ID {requirement_id!r} must match OASPS-[A-F]##",
                )
                continue
            found_ids.append(requirement_id)

        counts = Counter(found_ids)
        for requirement_id in sorted(EXPECTED_REQUIREMENT_IDS):
            count = counts[requirement_id]
            if count == 0:
                self.error("STANDARD.md", f"required heading {requirement_id} is missing")
            elif count > 1:
                self.error(
                    "STANDARD.md",
                    f"required heading {requirement_id} appears {count} times; expected once",
                )

        for requirement_id in sorted(counts.keys() - EXPECTED_REQUIREMENT_IDS):
            self.error(
                "STANDARD.md",
                f"unexpected requirement heading {requirement_id}; expected the fixed 32-ID draft set",
            )

        return set(found_ids)

    def validate_matrix(
        self, source_ids: set[str], standard_requirement_ids: set[str]
    ) -> list[tuple[int, dict[str, str]]]:
        relative_path = "case-studies/flock-safety/matrix.csv"
        records = self.read_csv(relative_path, MATRIX_HEADER)
        claim_ids: list[str] = []

        for line_number, record in records:
            self.require_fields(
                relative_path, line_number, record, MATRIX_REQUIRED_FIELDS
            )

            claim_id = record["claim_id"].strip()
            if claim_id:
                claim_ids.append(claim_id)
                if not CLAIM_ID_RE.fullmatch(claim_id):
                    self.error(
                        f"{relative_path}:{line_number}",
                        "claim_id must match FS-GLOBAL-###, FS-CT-###, or "
                        "FS-CT-FAIRFIELD-###",
                    )

            requirement_id = record["requirement_id"].strip()
            if requirement_id:
                if not REQUIREMENT_ID_RE.fullmatch(requirement_id):
                    self.error(
                        f"{relative_path}:{line_number}",
                        "requirement_id must match OASPS-[A-F]##",
                    )
                elif requirement_id not in standard_requirement_ids:
                    self.error(
                        f"{relative_path}:{line_number}",
                        f"requirement_id {requirement_id!r} has no heading in STANDARD.md",
                    )

            self.validate_allowed_value(
                relative_path,
                line_number,
                "responsible_actor",
                record["responsible_actor"].strip(),
                ALLOWED_ACTORS,
            )
            self.validate_allowed_value(
                relative_path,
                line_number,
                "evidence_label",
                record["evidence_label"].strip(),
                ALLOWED_EVIDENCE_LABELS,
            )
            self.validate_allowed_value(
                relative_path,
                line_number,
                "assessment",
                record["assessment"].strip(),
                ALLOWED_ASSESSMENTS,
            )
            self.validate_allowed_value(
                relative_path,
                line_number,
                "implementation_state",
                record["implementation_state"].strip(),
                ALLOWED_IMPLEMENTATION_STATES,
            )

            last_verified = record["last_verified"].strip()
            if last_verified:
                self.validate_iso_date(
                    relative_path, line_number, "last_verified", last_verified
                )

            raw_source_ids = record["source_ids"].strip()
            evidence_label = record["evidence_label"].strip()
            if not raw_source_ids:
                if evidence_label and evidence_label != "Unknown":
                    self.error(
                        f"{relative_path}:{line_number}",
                        "source_ids is required unless evidence_label is Unknown",
                    )
            else:
                tokens = raw_source_ids.split("|")
                if raw_source_ids != "|".join(token.strip() for token in tokens):
                    self.error(
                        f"{relative_path}:{line_number}",
                        "source_ids must be pipe-separated with no surrounding spaces",
                    )
                if len(tokens) != len(set(tokens)):
                    self.error(
                        f"{relative_path}:{line_number}",
                        "source_ids contains a duplicate ID",
                    )
                for source_id in tokens:
                    if not SOURCE_ID_RE.fullmatch(source_id):
                        self.error(
                            f"{relative_path}:{line_number}",
                            f"source reference {source_id!r} must match SRC-####",
                        )
                    elif source_id not in source_ids:
                        self.error(
                            f"{relative_path}:{line_number}",
                            f"source reference {source_id!r} is missing from evidence/sources.csv",
                        )

            self.validate_no_plate_literal(
                relative_path,
                line_number,
                record,
                MATRIX_NARRATIVE_FIELDS,
            )

        for claim_id, count in Counter(claim_ids).items():
            if count > 1:
                self.error(
                    relative_path,
                    f"claim_id {claim_id!r} appears {count} times; IDs must be unique",
                )

        return records

    def validate_allowed_value(
        self,
        relative_path: str,
        line_number: int,
        field: str,
        value: str,
        allowed_values: frozenset[str],
    ) -> None:
        if value and value not in allowed_values:
            self.error(
                f"{relative_path}:{line_number}",
                f"{field} {value!r} is not allowed; choose one of: "
                + ", ".join(sorted(allowed_values)),
            )

    def validate_case_study_citations(self, source_ids: set[str]) -> None:
        case_study_root = ROOT / "case-studies" / "flock-safety"
        if not case_study_root.is_dir():
            return

        for path in sorted(case_study_root.rglob("*.md")):
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                self.error(self.relative(path), f"could not read UTF-8 text ({exc})")
                continue
            for line_number, line in enumerate(text.splitlines(), start=1):
                for bracket in BRACKET_RE.findall(line):
                    for match in BRACKETED_SOURCE_TOKEN_RE.finditer(bracket):
                        source_id = match.group(0)
                        if not SOURCE_ID_RE.fullmatch(source_id):
                            self.error(
                                f"{self.relative(path)}:{line_number}",
                                f"bracketed source citation {source_id!r} must match SRC-####",
                            )
                        elif source_id not in source_ids:
                            self.error(
                                f"{self.relative(path)}:{line_number}",
                                f"bracketed source citation {source_id!r} is missing from "
                                "evidence/sources.csv",
                            )

    def validate_markdown_links(self) -> int:
        markdown_count = 0
        for path in sorted(ROOT.rglob("*.md")):
            if ".git" in path.relative_to(ROOT).parts:
                continue
            markdown_count += 1
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                self.error(self.relative(path), f"could not read UTF-8 text ({exc})")
                continue

            for line_number, line in enumerate(text.splitlines(), start=1):
                for match in MARKDOWN_LINK_RE.finditer(line):
                    raw_target = match.group("target")
                    if raw_target.startswith("<") and raw_target.endswith(">"):
                        raw_target = raw_target[1:-1]
                    target = raw_target.strip()
                    if not target or target.startswith(("#", "//")):
                        continue

                    parsed = urlsplit(target)
                    if parsed.scheme or parsed.netloc:
                        # Includes https:, http:, mailto:, and other non-local links.
                        continue
                    link_path = unquote(parsed.path)
                    if not link_path or link_path.startswith("/"):
                        continue

                    candidate = (path.parent / Path(link_path)).resolve()
                    try:
                        candidate.relative_to(ROOT)
                    except ValueError:
                        self.error(
                            f"{self.relative(path)}:{line_number}",
                            f"relative Markdown link {target!r} escapes the repository",
                        )
                        continue
                    if not candidate.exists():
                        self.error(
                            f"{self.relative(path)}:{line_number}",
                            f"relative Markdown link {target!r} does not resolve",
                        )
        return markdown_count

    def run(self) -> int:
        self.validate_required_tree()
        self.validate_version()
        standard_requirement_ids = self.validate_standard()
        source_ids, source_records = self.validate_sources()
        matrix_records = self.validate_matrix(source_ids, standard_requirement_ids)
        self.validate_case_study_citations(source_ids)
        markdown_count = self.validate_markdown_links()

        if self.errors:
            print(
                f"OASPS repository validation failed with {len(self.errors)} "
                f"error{'s' if len(self.errors) != 1 else ''}:"
            )
            for error in self.errors:
                print(f"  - {error}")
            print("\nFix the listed issues, then run: python scripts/validate.py")
            return 1

        print(
            "OASPS repository validation passed: "
            f"{len(EXPECTED_REQUIREMENT_IDS)} requirements, "
            f"{len(source_records)} sources, "
            f"{len(matrix_records)} matrix rows, and "
            f"{markdown_count} Markdown files checked."
        )
        return 0


def main() -> int:
    return Validator().run()


if __name__ == "__main__":
    sys.exit(main())
