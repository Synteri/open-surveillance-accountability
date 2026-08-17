#!/usr/bin/env python3
"""Standard-library consistency and publication-safety checks for OASPS."""

from __future__ import annotations

import csv
import hashlib
import io
import re
import subprocess
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path, PurePosixPath
from typing import TextIO
from urllib.parse import unquote, urlsplit


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "0.4.0-draft.1"

CORE_DIRECTORIES = (
    ".github",
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "case-studies/fairfield-connecticut",
    "case-studies/fairfield-connecticut/systems",
    "case-studies/flock-safety/jurisdictions/connecticut",
    "evidence/snapshots",
    "scripts",
    "standard/crosswalks",
    "tests",
)

CORE_FILES = (
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
    "LICENSE.md",
    "METHODOLOGY.md",
    "README.md",
    "ROADMAP.md",
    "STANDARD.md",
    "VERSION",
    "case-studies/fairfield-connecticut/CHANGELOG.md",
    "case-studies/fairfield-connecticut/README.md",
    "case-studies/fairfield-connecticut/UNRESOLVED.md",
    "case-studies/fairfield-connecticut/inventory.csv",
    "case-studies/fairfield-connecticut/systems/automated-traffic-enforcement.md",
    "case-studies/fairfield-connecticut/systems/axon-police-video.md",
    "case-studies/fairfield-connecticut/systems/flock-alpr.md",
    "case-studies/fairfield-connecticut/systems/school-security-cameras.md",
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
    "tests/test_validate.py",
)

ROOT_SPECIAL_FILES = frozenset(
    {".gitignore", "CITATION.cff", "LICENSE-CODE", "LICENSE-CONTENT", "VERSION"}
)
SNAPSHOT_EXTENSIONS = frozenset({".txt", ".md", ".csv", ".json"})
PUBLISHABLE_EXTENSIONS = frozenset(
    {".md", ".csv", ".yml", ".yaml", ".cff", *SNAPSHOT_EXTENSIONS}
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
    "retrieval_status",
    "retrieved_at",
    "effective_date",
    "content_sha256",
    "notes",
)

MATRIX_HEADER = (
    "claim_id",
    "requirement_id",
    "subject",
    "jurisdiction",
    "responsible_actor",
    "actor_override_reason",
    "finding",
    "documented_policy",
    "technical_control",
    "deployed_configuration",
    "deployment_basis",
    "independent_verification",
    "evidence_label",
    "verified_fact",
    "assessment",
    "known_fact_basis",
    "implementation_state",
    "deployment_evidence_state",
    "historical_as_of",
    "applicability_reason",
    "binding_obligation",
    "last_verified",
    "source_ids",
    "unresolved_question",
    "next_action",
    "notes",
)

INVENTORY_HEADER = (
    "system_id",
    "system_name",
    "vendor",
    "operator",
    "technology_category",
    "jurisdiction",
    "public_purpose",
    "documented_capabilities",
    "evidence_label",
    "implementation_state",
    "last_verified",
    "source_ids",
    "authorization_or_policy",
    "retention_or_data_use",
    "sharing_or_access",
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
    "retrieval_status",
)
MATRIX_REQUIRED_FIELDS = (
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
    "unresolved_question",
    "next_action",
)
INVENTORY_REQUIRED_FIELDS = (
    "system_id",
    "system_name",
    "vendor",
    "operator",
    "technology_category",
    "jurisdiction",
    "public_purpose",
    "documented_capabilities",
    "evidence_label",
    "implementation_state",
    "last_verified",
    "authorization_or_policy",
    "retention_or_data_use",
    "sharing_or_access",
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
ALLOWED_RETRIEVAL_STATUSES = frozenset(
    {
        "Retrieved",
        "Partially retrieved",
        "Indexed-only",
        "Unavailable or access-blocked",
        "Broken link",
        "Not rechecked",
    }
)
ALLOWED_ACTORS = frozenset(
    {"Vendor", "Agency", "Legislature", "Court", "Independent oversight", "Shared"}
)
ALLOWED_EVIDENCE_LABELS = frozenset(
    {"Verified", "Vendor-asserted", "Partially verifiable", "Unknown", "Noncompliant"}
)
ALLOWED_INVENTORY_EVIDENCE_LABELS = frozenset(
    {"Verified", "Vendor-asserted", "Partially verifiable", "Unknown"}
)
ALLOWED_ASSESSMENTS = frozenset(
    {"Meets", "Partly meets", "Does not meet", "Unknown", "Not applicable"}
)
ALLOWED_IMPLEMENTATION_STATES = frozenset(
    {
        "Deployed now",
        "Historical",
        "Announced or future",
        "Optional or customer-configurable",
        "Jurisdiction-specific",
        "Unknown",
    }
)
ALLOWED_DEPLOYMENT_EVIDENCE_STATES = frozenset({"Affirmative"})
DEFINITIVE_ASSESSMENTS = frozenset({"Meets", "Partly meets", "Does not meet"})
EXEMPTION_REASONS = frozenset(
    {"normative", "methodological", "editorial", "question", "navigation"}
)

EXPECTED_REQUIREMENT_IDS = frozenset(
    [*(f"OASPS-A{number:02d}" for number in range(1, 5))]
    + [*(f"OASPS-B{number:02d}" for number in range(1, 6))]
    + [*(f"OASPS-C{number:02d}" for number in range(1, 7))]
    + [*(f"OASPS-D{number:02d}" for number in range(1, 7))]
    + [*(f"OASPS-E{number:02d}" for number in range(1, 7))]
    + [*(f"OASPS-F{number:02d}" for number in range(1, 6))]
)
REQUIREMENT_LABELS = (
    "Requirement",
    "Why it matters",
    "Responsible actor",
    "Expected proof",
    "Recognized basis",
    "OASPS extension",
)

SOURCE_ID_RE = re.compile(r"SRC-[0-9]{4}\Z")
SOURCE_TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9])SRC-(?:\[0-9\]\{4\}|[A-Za-z0-9#?_]+(?:-[A-Za-z0-9#?_]+)*)?",
    re.IGNORECASE,
)
CLAIM_ID_RE = re.compile(r"(?:FS-GLOBAL|FS-CT-FAIRFIELD|FS-CT)-[0-9]{3}\Z")
INVENTORY_ID_RE = re.compile(r"CT-FAIRFIELD-SYS-[0-9]{3}\Z")
REQUIREMENT_ID_RE = re.compile(r"OASPS-[A-F][0-9]{2}\Z")
REQUIREMENT_HEADING_RE = re.compile(
    r"^### (?P<id>OASPS-[A-F][0-9]{2}) — (?P<title>\S(?:.*\S)?)$"
)
REQUIREMENT_LABEL_RE = re.compile(
    r"^\*\*(?P<label>" + "|".join(re.escape(label) for label in REQUIREMENT_LABELS)
    + r"):\*\*\s*(?P<value>.*)$"
)
ISO_DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}\Z")
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")

MARKDOWN_LINK_RE = re.compile(
    r"(?<!!)\[[^\]\n]*\]\(\s*(?P<target><[^>\n]+>|[^)\s]+)"
    r"(?:\s+(?:\"[^\"\n]*\"|'[^'\n]*'))?\s*\)"
)
CITATION_START = "<!-- oasps-citations:start -->"
CITATION_END = "<!-- oasps-citations:end -->"
CITATION_REQUIRED_FILES = frozenset(
    {
        "README.md",
        "case-studies/fairfield-connecticut/README.md",
        "case-studies/fairfield-connecticut/UNRESOLVED.md",
        "case-studies/fairfield-connecticut/systems/automated-traffic-enforcement.md",
        "case-studies/fairfield-connecticut/systems/axon-police-video.md",
        "case-studies/fairfield-connecticut/systems/flock-alpr.md",
        "case-studies/fairfield-connecticut/systems/school-security-cameras.md",
        "case-studies/flock-safety/FINDINGS.md",
        "case-studies/flock-safety/README.md",
        "case-studies/flock-safety/SCOPE.md",
        "case-studies/flock-safety/UNRESOLVED.md",
        "case-studies/flock-safety/jurisdictions/connecticut/README.md",
        "case-studies/flock-safety/jurisdictions/connecticut/fairfield.md",
        "standard/crosswalks/convention-108-plus.md",
        "standard/crosswalks/iacp-bja-alpr.md",
        "standard/crosswalks/iso-27701.md",
        "standard/crosswalks/nist-privacy-framework.md",
        "standard/crosswalks/nist-sp-800-53.md",
    }
)
EXEMPTION_RE = re.compile(
    r"<!-- oasps-citation-exempt: (?P<reason>[a-z-]+) -->\Z"
)
CITATION_TAIL_RE = re.compile(
    r"\[(?P<ids>SRC-[0-9]{4}(?:,\s*SRC-[0-9]{4})*)\]\s*\Z"
)
LIST_ITEM_RE = re.compile(r"^\s*(?:[-+*]|[0-9]+\.)\s+(?P<text>.+)$")

VENDOR_TERM_RE = re.compile(
    r"\b(?:Flock(?:\s+Safety|OS)?|Falcon(?:\s+Flex)?|Wing(?:\s+(?:LPR|VMS|Gateway))?|"
    r"Condor(?:\s+PTZ)?)\b",
    re.IGNORECASE,
)
CONTEXTUAL_PLATE_RE = re.compile(
    r"\b(?:license\s+plate|plate|vehicle\s+tag)"
    r"(?:\s+(?:number|no\.?))?\s*(?:is|was|[:#=])?\s*[\"']?"
    r"(?!SRC-|OASPS-)(?=[A-Z0-9-]{5,9}\b)"
    r"(?=[A-Z0-9-]*[A-Z])(?=[A-Z0-9-]*[0-9])"
    r"[A-Z0-9]{1,4}(?:-?[A-Z0-9]{1,4})?\b",
    re.IGNORECASE,
)
CONCRETE_LOCATION_PATTERN = (
    r"(?:"
    r"[0-9]{1,6}\s+[A-Z0-9][A-Z0-9.'-]*"
    r"(?:\s+[A-Z0-9][A-Z0-9.'-]*){0,5}?\s+"
    r"(?:Street|St|Road|Rd|Avenue|Ave|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|"
    r"Highway|Hwy|Parkway|Pkwy|Place|Pl)\.?"
    r"|[-+]?[0-9]{1,2}\.[0-9]{3,}\s*,\s*[-+]?[0-9]{1,3}\.[0-9]{3,}"
    r")"
)
TRAVEL_TRAIL_RE = re.compile(
    r"\b(?:plate|vehicle|driver|person)\b[^\n]{0,120}"
    r"\b(?:seen|observed|detected|located)\b\s+(?:at|near|in)\s+"
    + CONCRETE_LOCATION_PATTERN
    + r"\s*(?:->|→|\bthen\b|\bfollowed\s+by\b)[^\n]{0,80}"
    r"\b(?:seen|observed|detected|located|arrived)\b\s+(?:at|near|in)\s+"
    + CONCRETE_LOCATION_PATTERN,
    re.IGNORECASE,
)
EXPLICIT_TRAIL_RE = re.compile(
    r"\b(?:travel|location|movement)\s+(?:history|trail)\s+(?:for|of)\s+"
    r"(?:plate|vehicle|driver|person)\b[^\n:]{0,80}:\s*[^\n]{0,60}"
    + CONCRETE_LOCATION_PATTERN
    + r"[^\n]{0,60}(?:->|→)[^\n]{0,60}"
    + CONCRETE_LOCATION_PATTERN,
    re.IGNORECASE,
)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bsk_live_[A-Za-z0-9]{16,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{16,}\b"),
    re.compile(
        r"\b(?:api[_ -]?key|access[_ -]?token|auth[_ -]?token|password|secret|credential)"
        r"\s*[:=]\s*[\"']?[A-Za-z0-9/+_.-]{12,}",
        re.IGNORECASE,
    ),
)


def is_supported_path(relative_path: str) -> bool:
    """Return whether a repository path belongs to an extensible text lane."""
    pure = PurePosixPath(relative_path)
    if pure.is_absolute() or ".." in pure.parts or not pure.parts:
        return False
    if len(pure.parts) == 1:
        return pure.suffix.lower() == ".md" or relative_path in ROOT_SPECIAL_FILES
    if pure.parts[0] == "standard":
        return pure.suffix.lower() == ".md"
    if pure.parts[0] == "case-studies":
        return pure.suffix.lower() in {".md", ".csv"}
    if pure.parts[0] == "evidence":
        if pure.parts[:2] == ("evidence", "snapshots"):
            return pure.suffix.lower() in SNAPSHOT_EXTENSIONS
        return pure.suffix.lower() in {".md", ".csv"}
    if pure.parts[0] in {"scripts", "tests"}:
        return pure.suffix.lower() == ".py"
    if pure.parts[0] == ".github":
        return pure.suffix.lower() in {".md", ".yml", ".yaml"}
    return False


def is_publishable_path(relative_path: str) -> bool:
    pure = PurePosixPath(relative_path)
    if pure.parts and pure.parts[0] in {"scripts", "tests"}:
        return False
    if relative_path in {".gitignore", "VERSION"}:
        return False
    return pure.suffix.lower() in PUBLISHABLE_EXTENSIONS or relative_path in {
        "LICENSE-CODE",
        "LICENSE-CONTENT",
    }


class Validator:
    """Collect actionable validation errors without exposing sensitive matches."""

    def __init__(self, root: Path | None = None, stream: TextIO | None = None) -> None:
        self.root = (root or DEFAULT_ROOT).resolve()
        self.stream = stream or sys.stdout
        self.errors: list[str] = []
        self.tracked_paths: set[str] = set()
        self.inventory: set[str] = set()
        self.text_cache: dict[str, str] = {}
        self.source_count = 0
        self.matrix_count = 0
        self.jurisdiction_inventory_count = 0
        self.global_matrix_coverage = 0

    def error(self, location: str, message: str) -> None:
        self.errors.append(f"{location}: {message}")

    def git_paths(self, *arguments: str) -> set[str] | None:
        try:
            result = subprocess.run(
                ["git", "-C", str(self.root), *arguments],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
        except OSError:
            self.error("repository inventory", "git is unavailable")
            return None
        if result.returncode != 0:
            self.error("repository inventory", "git could not enumerate repository paths")
            return None
        try:
            decoded = result.stdout.decode("utf-8")
        except UnicodeDecodeError:
            self.error("repository inventory", "git returned a non-UTF-8 path")
            return None
        return {item for item in decoded.split("\0") if item}

    def discover_inventory(self) -> None:
        tracked = self.git_paths("ls-files", "-z")
        candidates = self.git_paths("ls-files", "--others", "--exclude-standard", "-z")
        if tracked is None or candidates is None:
            return
        self.tracked_paths = tracked
        for relative_path in sorted(tracked):
            if not is_supported_path(relative_path):
                self.error(relative_path, "tracked file is outside the supported path inventory")
        self.inventory = {path for path in tracked if is_supported_path(path)}
        self.inventory.update(path for path in candidates if is_supported_path(path))

    def validate_core_paths(self) -> None:
        for relative_path in CORE_DIRECTORIES:
            if not (self.root / PurePosixPath(relative_path)).is_dir():
                self.error(relative_path, "required core directory is missing")
        for relative_path in CORE_FILES:
            path = self.root / PurePosixPath(relative_path)
            if relative_path not in self.inventory:
                self.error(relative_path, "required core file is absent from repository inventory")
            elif not path.is_file():
                self.error(relative_path, "required core path is not a regular file")

    def validate_utf8_text(self) -> None:
        for relative_path in sorted(self.inventory):
            path = self.root / PurePosixPath(relative_path)
            if not path.is_file():
                self.error(relative_path, "inventory path is missing or not a regular file")
                continue
            try:
                raw = path.read_bytes()
                text = raw.decode("utf-8")
            except (OSError, UnicodeDecodeError):
                self.error(relative_path, "supported text file must be readable UTF-8")
                continue
            if "\x00" in text:
                self.error(relative_path, "supported text file contains a NUL byte")
                continue
            self.text_cache[relative_path] = text

    def text(self, relative_path: str) -> str | None:
        return self.text_cache.get(relative_path)

    def validate_version(self) -> None:
        contents = self.text("VERSION")
        if contents is not None and contents not in {
            EXPECTED_VERSION,
            EXPECTED_VERSION + "\n",
            EXPECTED_VERSION + "\r\n",
        }:
            self.error("VERSION", f"must contain exactly {EXPECTED_VERSION!r} as its only line")

    def validate_citation_metadata(self) -> None:
        text = self.text("CITATION.cff")
        if text is None:
            return
        top_level_license_lines = [
            line for line in text.splitlines() if line.startswith("license:")
        ]
        if top_level_license_lines != ["license: CC-BY-4.0"]:
            self.error(
                "CITATION.cff",
                "root license must be the single value CC-BY-4.0; "
                "validation code is separately file-scoped MIT",
            )

    def read_csv(
        self, relative_path: str, expected_header: tuple[str, ...]
    ) -> list[tuple[int, dict[str, str]]]:
        text = self.text(relative_path)
        if text is None:
            return []
        if text.startswith("\ufeff"):
            text = text[1:]
        records: list[tuple[int, dict[str, str]]] = []
        try:
            reader = csv.reader(io.StringIO(text, newline=""))
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
                if not row or all(not value.strip() for value in row):
                    self.error(f"{relative_path}:{line_number}", "blank data rows are not allowed")
                    continue
                if len(row) != len(expected_header):
                    self.error(
                        f"{relative_path}:{line_number}",
                        f"expected {len(expected_header)} fields but found {len(row)}",
                    )
                    continue
                records.append((line_number, dict(zip(expected_header, row))))
        except csv.Error:
            self.error(relative_path, "CSV could not be parsed")
            return []
        if not records:
            self.error(relative_path, "must contain at least one data row")
        return records

    def require_fields(
        self,
        relative_path: str,
        line_number: int,
        record: dict[str, str],
        fields: tuple[str, ...],
    ) -> None:
        for field in fields:
            if not record[field].strip():
                self.error(f"{relative_path}:{line_number}", f"required field {field!r} is blank")

    def validate_allowed(
        self,
        relative_path: str,
        line_number: int,
        field: str,
        value: str,
        allowed: frozenset[str],
    ) -> None:
        if value and value not in allowed:
            self.error(f"{relative_path}:{line_number}", f"{field!r} is not an allowed value")

    def validate_iso_date(
        self, relative_path: str, line_number: int, field: str, value: str
    ) -> None:
        try:
            valid = bool(ISO_DATE_RE.fullmatch(value)) and date.fromisoformat(value).isoformat() == value
        except ValueError:
            valid = False
        if not valid:
            self.error(
                f"{relative_path}:{line_number}",
                f"{field!r} must be a real ISO calendar date in YYYY-MM-DD form",
            )

    def validate_iso_datetime(
        self, relative_path: str, line_number: int, field: str, value: str
    ) -> None:
        candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
        try:
            parsed = datetime.fromisoformat(candidate)
            valid = "T" in value and parsed.tzinfo is not None and parsed.utcoffset() is not None
        except ValueError:
            valid = False
        if not valid:
            self.error(
                f"{relative_path}:{line_number}",
                f"{field!r} must be an ISO 8601 datetime with a timezone",
            )

    def validate_sources(self) -> tuple[set[str], int]:
        relative_path = "evidence/sources.csv"
        records = self.read_csv(relative_path, SOURCE_HEADER)
        all_ids: list[str] = []
        valid_ids: set[str] = set()
        for line_number, record in records:
            self.require_fields(relative_path, line_number, record, SOURCE_REQUIRED_FIELDS)
            source_id = record["source_id"].strip()
            if source_id:
                all_ids.append(source_id)
                if SOURCE_ID_RE.fullmatch(source_id):
                    valid_ids.add(source_id)
                else:
                    self.error(f"{relative_path}:{line_number}", "source_id must match SRC-####")
            self.validate_allowed(
                relative_path,
                line_number,
                "source_type",
                record["source_type"].strip(),
                ALLOWED_SOURCE_TYPES,
            )
            self.validate_allowed(
                relative_path,
                line_number,
                "retrieval_status",
                record["retrieval_status"].strip(),
                ALLOWED_RETRIEVAL_STATUSES,
            )
            retrieval_status = record["retrieval_status"].strip()
            if retrieval_status in ALLOWED_RETRIEVAL_STATUSES - {"Retrieved"}:
                if not record["notes"].strip():
                    self.error(
                        f"{relative_path}:{line_number}",
                        "a limited retrieval_status requires a nonblank notes explanation",
                    )
            for field in ("published_date", "accessed_date", "effective_date"):
                value = record[field].strip()
                if value:
                    self.validate_iso_date(relative_path, line_number, field, value)
            retrieved_at = record["retrieved_at"].strip()
            if retrieved_at:
                self.validate_iso_datetime(relative_path, line_number, "retrieved_at", retrieved_at)
            for field in ("url", "archived_url"):
                value = record[field].strip()
                if value and not value.startswith("https://"):
                    self.error(f"{relative_path}:{line_number}", f"{field!r} must begin with https://")
            self.validate_snapshot(relative_path, line_number, record)
        for source_id, count in Counter(all_ids).items():
            if count > 1:
                self.error(relative_path, f"source_id {source_id!r} appears {count} times")
        return valid_ids, len(records)

    def validate_snapshot(
        self, relative_path: str, line_number: int, record: dict[str, str]
    ) -> None:
        local_snapshot = record["local_snapshot"].strip()
        digest = record["content_sha256"].strip()
        location = f"{relative_path}:{line_number}"
        if not local_snapshot:
            if digest:
                self.error(location, "content_sha256 must be blank without local_snapshot")
            return
        pure = PurePosixPath(local_snapshot)
        if (
            pure.is_absolute()
            or ".." in pure.parts
            or "\\" in local_snapshot
            or pure.parts[:2] != ("evidence", "snapshots")
        ):
            self.error(location, "local_snapshot must stay safely under evidence/snapshots")
            return
        if pure.suffix.lower() not in SNAPSHOT_EXTENSIONS:
            self.error(location, "local_snapshot must use a permitted UTF-8 text extension")
        if local_snapshot not in self.inventory:
            self.error(location, "local_snapshot must be present in the repository inventory")
        candidate = (self.root / pure).resolve()
        snapshot_root = (self.root / "evidence" / "snapshots").resolve()
        try:
            candidate.relative_to(snapshot_root)
        except ValueError:
            self.error(location, "local_snapshot resolves outside evidence/snapshots")
            return
        if not digest:
            self.error(location, "content_sha256 is required when local_snapshot is set")
            return
        if not SHA256_RE.fullmatch(digest):
            self.error(location, "content_sha256 must be 64 lowercase hexadecimal characters")
            return
        try:
            actual = hashlib.sha256(candidate.read_bytes()).hexdigest()
        except OSError:
            self.error(location, "local_snapshot could not be read for hashing")
            return
        if actual != digest:
            self.error(location, "content_sha256 does not match local_snapshot bytes")

    def validate_standard(self) -> tuple[set[str], dict[str, str]]:
        text = self.text("STANDARD.md")
        if text is None:
            return set(), {}
        blocks: list[tuple[str, int, list[str]]] = []
        current_id: str | None = None
        current_line = 0
        current_body: list[str] = []

        def finish() -> None:
            nonlocal current_id, current_line, current_body
            if current_id is not None:
                blocks.append((current_id, current_line, current_body))
            current_id, current_line, current_body = None, 0, []

        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.startswith("### "):
                finish()
                if "OASPS-" not in line:
                    continue
                match = REQUIREMENT_HEADING_RE.fullmatch(line)
                if match is None:
                    self.error(
                        f"STANDARD.md:{line_number}",
                        "requirement heading must be '### OASPS-X## — Nonblank title'",
                    )
                    continue
                current_id = match.group("id")
                current_line = line_number
                current_body = [match.group("title")]
            elif current_id is not None:
                current_body.append(line)
        finish()

        counts = Counter(requirement_id for requirement_id, _, _ in blocks)
        for requirement_id in sorted(EXPECTED_REQUIREMENT_IDS):
            count = counts[requirement_id]
            if count != 1:
                self.error(
                    "STANDARD.md",
                    f"required heading {requirement_id} must appear exactly once (found {count})",
                )
        for requirement_id in sorted(counts.keys() - EXPECTED_REQUIREMENT_IDS):
            self.error("STANDARD.md", f"unexpected requirement heading {requirement_id}")

        actors: dict[str, str] = {}
        for requirement_id, heading_line, body in blocks:
            values: dict[str, list[str]] = {label: [] for label in REQUIREMENT_LABELS}
            for line in body:
                match = REQUIREMENT_LABEL_RE.fullmatch(line)
                if match:
                    values[match.group("label")].append(match.group("value").strip())
            for label in REQUIREMENT_LABELS:
                found = values[label]
                if len(found) != 1 or not found[0]:
                    self.error(
                        f"STANDARD.md:{heading_line}",
                        f"{requirement_id} must contain exactly one nonblank {label!r} label",
                    )
            actor_values = values["Responsible actor"]
            if len(actor_values) == 1 and actor_values[0]:
                actor = actor_values[0]
                if actor not in ALLOWED_ACTORS:
                    self.error(
                        f"STANDARD.md:{heading_line}",
                        f"{requirement_id} has an uncontrolled responsible actor",
                    )
                else:
                    actors[requirement_id] = actor
            if VENDOR_TERM_RE.search("\n".join(body)):
                self.error(
                    f"STANDARD.md:{heading_line}",
                    f"{requirement_id} contains a vendor-specific term",
                )
        return set(counts), actors

    def validate_matrix(
        self, source_ids: set[str], requirement_ids: set[str], requirement_actors: dict[str, str]
    ) -> int:
        relative_path = "case-studies/flock-safety/matrix.csv"
        records = self.read_csv(relative_path, MATRIX_HEADER)
        claim_ids: list[str] = []
        global_requirement_counts: Counter[str] = Counter()
        for line_number, record in records:
            location = f"{relative_path}:{line_number}"
            self.require_fields(relative_path, line_number, record, MATRIX_REQUIRED_FIELDS)
            claim_id = record["claim_id"].strip()
            if claim_id:
                claim_ids.append(claim_id)
                if not CLAIM_ID_RE.fullmatch(claim_id):
                    self.error(location, "claim_id has an invalid format")
            requirement_id = record["requirement_id"].strip()
            if requirement_id:
                if not REQUIREMENT_ID_RE.fullmatch(requirement_id):
                    self.error(location, "requirement_id must match OASPS-[A-F]##")
                elif requirement_id not in requirement_ids:
                    self.error(location, "requirement_id has no heading in STANDARD.md")
            if (
                claim_id.startswith("FS-GLOBAL-")
                and CLAIM_ID_RE.fullmatch(claim_id)
                and requirement_id in requirement_ids
            ):
                global_requirement_counts[requirement_id] += 1

            actor = record["responsible_actor"].strip()
            evidence = record["evidence_label"].strip()
            assessment = record["assessment"].strip()
            state = record["implementation_state"].strip()
            deployment_evidence_state = record["deployment_evidence_state"].strip()
            self.validate_allowed(relative_path, line_number, "responsible_actor", actor, ALLOWED_ACTORS)
            self.validate_allowed(
                relative_path, line_number, "evidence_label", evidence, ALLOWED_EVIDENCE_LABELS
            )
            self.validate_allowed(
                relative_path, line_number, "assessment", assessment, ALLOWED_ASSESSMENTS
            )
            self.validate_allowed(
                relative_path,
                line_number,
                "implementation_state",
                state,
                ALLOWED_IMPLEMENTATION_STATES,
            )
            self.validate_allowed(
                relative_path,
                line_number,
                "deployment_evidence_state",
                deployment_evidence_state,
                ALLOWED_DEPLOYMENT_EVIDENCE_STATES,
            )
            last_verified = record["last_verified"].strip()
            if last_verified:
                self.validate_iso_date(relative_path, line_number, "last_verified", last_verified)

            resolved_source_ids = self.validate_matrix_sources(
                relative_path, line_number, record["source_ids"].strip(), source_ids
            )
            has_sources = bool(resolved_source_ids)
            if evidence and evidence != "Unknown" and not has_sources:
                self.error(location, "source_ids is required unless evidence_label is Unknown")

            expected_actor = requirement_actors.get(requirement_id)
            mismatch = bool(expected_actor and actor and actor != expected_actor)
            self.conditional_field(
                location,
                record,
                "actor_override_reason",
                mismatch,
                "responsible_actor differs from the STANDARD requirement",
            )
            self.conditional_field(
                location,
                record,
                "deployment_basis",
                state == "Deployed now",
                "implementation_state is Deployed now",
            )
            self.conditional_field(
                location,
                record,
                "deployment_evidence_state",
                state == "Deployed now",
                "implementation_state is Deployed now",
            )
            self.conditional_field(
                location,
                record,
                "applicability_reason",
                assessment == "Not applicable",
                "assessment is Not applicable",
            )
            self.conditional_field(
                location,
                record,
                "verified_fact",
                evidence == "Verified",
                "evidence_label is Verified",
            )
            known_basis_needed = evidence == "Unknown" and assessment in DEFINITIVE_ASSESSMENTS
            self.conditional_field(
                location,
                record,
                "known_fact_basis",
                known_basis_needed,
                "Unknown evidence has a definitive assessment",
            )
            if known_basis_needed and not has_sources:
                self.error(
                    location,
                    "known_fact_basis requires at least one resolved source_id",
                )
            self.conditional_field(
                location,
                record,
                "binding_obligation",
                evidence == "Noncompliant",
                "evidence_label is Noncompliant",
            )
            self.conditional_field(
                location,
                record,
                "historical_as_of",
                state == "Historical",
                "implementation_state is Historical",
            )

            if evidence == "Verified" and not has_sources:
                self.error(location, "Verified evidence requires source_ids")
            if evidence == "Noncompliant":
                if not has_sources:
                    self.error(location, "Noncompliant evidence requires source_ids")
                if assessment != "Does not meet":
                    self.error(location, "Noncompliant evidence requires assessment 'Does not meet'")
            if state == "Deployed now":
                if not has_sources:
                    self.error(location, "Deployed now requires source_ids")
            historical_as_of = record["historical_as_of"].strip()
            if historical_as_of:
                self.validate_iso_date(relative_path, line_number, "historical_as_of", historical_as_of)

        for claim_id, count in Counter(claim_ids).items():
            if count > 1:
                self.error(relative_path, f"claim_id {claim_id!r} appears {count} times")
        for requirement_id in sorted(requirement_ids):
            count = global_requirement_counts[requirement_id]
            if count != 1:
                self.error(
                    relative_path,
                    f"canonical FS-GLOBAL coverage for {requirement_id} "
                    f"must appear exactly once (found {count})",
                )
        self.global_matrix_coverage = sum(
            global_requirement_counts[requirement_id] == 1
            for requirement_id in requirement_ids
        )
        return len(records)

    def validate_jurisdiction_inventory(self, source_ids: set[str]) -> int:
        """Validate Fairfield's jurisdiction-level system-discovery inventory."""
        relative_path = "case-studies/fairfield-connecticut/inventory.csv"
        records = self.read_csv(relative_path, INVENTORY_HEADER)
        system_ids: list[str] = []
        for line_number, record in records:
            location = f"{relative_path}:{line_number}"
            self.require_fields(
                relative_path, line_number, record, INVENTORY_REQUIRED_FIELDS
            )
            system_id = record["system_id"].strip()
            if system_id:
                system_ids.append(system_id)
                if not INVENTORY_ID_RE.fullmatch(system_id):
                    self.error(
                        location,
                        "system_id must match CT-FAIRFIELD-SYS-###",
                    )

            evidence = record["evidence_label"].strip()
            state = record["implementation_state"].strip()
            jurisdiction = record["jurisdiction"].strip()
            if jurisdiction and jurisdiction != "Fairfield, Connecticut":
                self.error(
                    location,
                    "jurisdiction must be exactly 'Fairfield, Connecticut'",
                )
            self.validate_allowed(
                relative_path,
                line_number,
                "evidence_label",
                evidence,
                ALLOWED_INVENTORY_EVIDENCE_LABELS,
            )
            self.validate_allowed(
                relative_path,
                line_number,
                "implementation_state",
                state,
                ALLOWED_IMPLEMENTATION_STATES,
            )

            last_verified = record["last_verified"].strip()
            if last_verified:
                self.validate_iso_date(
                    relative_path, line_number, "last_verified", last_verified
                )
            resolved_source_ids = self.validate_matrix_sources(
                relative_path,
                line_number,
                record["source_ids"].strip(),
                source_ids,
            )
            source_required = evidence != "Unknown" or state == "Deployed now"
            if source_required and not resolved_source_ids:
                self.error(
                    location,
                    "source_ids is required for non-Unknown evidence or Deployed now state",
                )

            current_state_incomplete = evidence != "Verified" or state != "Deployed now"
            if current_state_incomplete:
                if not record["unresolved_question"].strip():
                    self.error(
                        location,
                        "unresolved_question is required when current state is incomplete",
                    )
                if not record["next_action"].strip():
                    self.error(
                        location,
                        "next_action is required when current state is incomplete",
                    )

        for system_id, count in Counter(system_ids).items():
            if count > 1:
                self.error(
                    relative_path,
                    f"system_id {system_id!r} appears {count} times",
                )
        return len(records)

    def conditional_field(
        self,
        location: str,
        record: dict[str, str],
        field: str,
        required: bool,
        reason: str,
    ) -> None:
        value = record[field].strip()
        if required and not value:
            self.error(location, f"{field} is required when {reason}")
        elif not required and value:
            self.error(location, f"{field} must be blank unless {reason}")

    def validate_matrix_sources(
        self,
        relative_path: str,
        line_number: int,
        raw: str,
        known_ids: set[str],
    ) -> list[str]:
        if not raw:
            return []
        location = f"{relative_path}:{line_number}"
        tokens = raw.split("|")
        if raw != "|".join(token.strip() for token in tokens):
            self.error(location, "source_ids must use pipes with no surrounding spaces")
        if len(tokens) != len(set(tokens)):
            self.error(location, "source_ids contains a duplicate ID")
        resolved: list[str] = []
        for token in tokens:
            if not SOURCE_ID_RE.fullmatch(token):
                self.error(location, "source_ids contains a malformed source ID")
            elif token not in known_ids:
                self.error(location, f"source reference {token!r} is missing from evidence/sources.csv")
            else:
                resolved.append(token)
        return resolved

    def validate_repository_source_tokens(self, source_ids: set[str]) -> None:
        for relative_path in sorted(self.inventory):
            if not is_publishable_path(relative_path):
                continue
            text = self.text(relative_path)
            if text is None:
                continue
            for match in SOURCE_TOKEN_RE.finditer(text):
                token = match.group(0)
                if token in {"SRC-####", "SRC-[0-9]{4}"}:
                    continue
                line_number = text.count("\n", 0, match.start()) + 1
                if not SOURCE_ID_RE.fullmatch(token):
                    self.error(
                        f"{relative_path}:{line_number}",
                        f"source token {token!r} is malformed; expected SRC-####",
                    )
                elif token not in source_ids:
                    self.error(
                        f"{relative_path}:{line_number}",
                        f"source token {token!r} is missing from evidence/sources.csv",
                    )

    def validate_citation_sections(self, source_ids: set[str]) -> None:
        for relative_path in sorted(CITATION_REQUIRED_FILES):
            text = self.text(relative_path)
            if text is None:
                continue
            stripped_lines = {line.strip() for line in text.splitlines()}
            if CITATION_START not in stripped_lines or CITATION_END not in stripped_lines:
                self.error(
                    relative_path,
                    "designated evidence-bearing narrative must contain at least one "
                    "balanced citation section",
                )
        for relative_path in sorted(self.inventory):
            if relative_path.endswith(".md") and is_publishable_path(relative_path):
                text = self.text(relative_path)
                if text is not None:
                    self.validate_citation_file(relative_path, text, source_ids)

    def validate_citation_file(
        self, relative_path: str, text: str, source_ids: set[str]
    ) -> None:
        in_section = False
        in_fence = False
        pending_exemption: str | None = None
        unit: list[str] = []
        unit_line = 0
        unit_kind = ""
        unit_exempt = False
        exempt_list_block = False

        def flush() -> None:
            nonlocal unit, unit_line, unit_kind, unit_exempt
            if not unit:
                return
            prose = " ".join(part.strip() for part in unit).strip()
            if unit_exempt:
                unit_exempt = False
            else:
                match = CITATION_TAIL_RE.search(prose)
                if match is None:
                    self.error(
                        f"{relative_path}:{unit_line}",
                        "prose in a marked citation section must end with [SRC-####]",
                    )
                else:
                    citation_ids = re.findall(r"SRC-[0-9]{4}", match.group("ids"))
                    if match.group("ids") != ", ".join(citation_ids):
                        self.error(
                            f"{relative_path}:{unit_line}",
                            "trailing citations must use a comma followed by one space",
                        )
                    if len(citation_ids) != len(set(citation_ids)):
                        self.error(
                            f"{relative_path}:{unit_line}",
                            "trailing citation contains a duplicate source ID",
                        )
                    for source_id in citation_ids:
                        if source_id not in source_ids:
                            self.error(
                                f"{relative_path}:{unit_line}",
                                f"trailing citation {source_id!r} is missing from evidence/sources.csv",
                            )
            unit, unit_line, unit_kind = [], 0, ""

        for line_number, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if stripped == CITATION_START:
                flush()
                if in_section:
                    self.error(f"{relative_path}:{line_number}", "citation sections must not nest")
                in_section = True
                in_fence = False
                exempt_list_block = False
                continue
            if stripped == CITATION_END:
                flush()
                if not in_section:
                    self.error(f"{relative_path}:{line_number}", "citation end marker has no start")
                if pending_exemption is not None:
                    self.error(
                        f"{relative_path}:{line_number}",
                        "citation exemption is not immediately followed by prose",
                    )
                    pending_exemption = None
                in_section = False
                in_fence = False
                exempt_list_block = False
                continue
            exemption_match = EXEMPTION_RE.fullmatch(stripped)
            if exemption_match is not None:
                flush()
                exempt_list_block = False
                if not in_section:
                    self.error(f"{relative_path}:{line_number}", "citation exemption is outside a marked section")
                elif exemption_match.group("reason") not in EXEMPTION_REASONS:
                    self.error(f"{relative_path}:{line_number}", "citation exemption reason is not allowed")
                elif pending_exemption is not None:
                    self.error(f"{relative_path}:{line_number}", "citation exemption is not immediately followed by prose")
                else:
                    pending_exemption = exemption_match.group("reason")
                continue
            if not in_section:
                continue
            list_match = LIST_ITEM_RE.match(line)
            exemption_target_is_prose = not (
                not stripped
                or stripped.startswith(("```", "~~~", "#", "<!--", "|", "<"))
                or re.fullmatch(r"[-*_]{3,}", stripped)
                or re.fullmatch(r"\|?(?:\s*:?-+:?\s*\|)+", stripped)
            )
            if pending_exemption is not None:
                if (exemption_target_is_prose or list_match is not None) and not in_fence:
                    if list_match is not None:
                        exempt_list_block = True
                    else:
                        unit_exempt = True
                    pending_exemption = None
                else:
                    self.error(
                        f"{relative_path}:{line_number}",
                        "citation exemption is not immediately followed by prose",
                    )
                    pending_exemption = None
            if stripped.startswith("```") or stripped.startswith("~~~"):
                flush()
                exempt_list_block = False
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if not stripped:
                flush()
                exempt_list_block = False
                continue
            if (
                stripped.startswith(("#", "<!--", "|", "<"))
                or re.fullmatch(r"[-*_]{3,}", stripped)
                or re.fullmatch(r"\|?(?:\s*:?-+:?\s*\|)+", stripped)
            ):
                flush()
                exempt_list_block = False
                continue
            if list_match:
                flush()
                unit = [list_match.group("text")]
                unit_line = line_number
                unit_kind = "list"
                unit_exempt = exempt_list_block
                continue
            if unit_kind == "list" and not line[:1].isspace():
                flush()
                exempt_list_block = False
            if not unit:
                unit_line = line_number
                unit_kind = "paragraph"
            unit.append(stripped)
        flush()
        if in_section:
            self.error(relative_path, "citation start marker has no matching end marker")
        if pending_exemption is not None:
            self.error(relative_path, "citation exemption is not immediately followed by prose")

    def validate_markdown_links(self) -> None:
        for relative_path in sorted(self.inventory):
            if not relative_path.endswith(".md"):
                continue
            text = self.text(relative_path)
            if text is None:
                continue
            path = self.root / PurePosixPath(relative_path)
            for line_number, line in enumerate(text.splitlines(), start=1):
                for match in MARKDOWN_LINK_RE.finditer(line):
                    target = match.group("target").strip("<>")
                    if not target or target.startswith(("#", "//")):
                        continue
                    parsed = urlsplit(target)
                    if parsed.scheme or parsed.netloc:
                        continue
                    link_path = unquote(parsed.path)
                    if not link_path or link_path.startswith("/"):
                        continue
                    candidate = (path.parent / Path(link_path)).resolve()
                    try:
                        candidate.relative_to(self.root)
                    except ValueError:
                        self.error(
                            f"{relative_path}:{line_number}",
                            "relative Markdown link escapes the repository",
                        )
                        continue
                    if not candidate.exists():
                        self.error(
                            f"{relative_path}:{line_number}",
                            "relative Markdown link does not resolve",
                        )

    def validate_sensitive_content(self) -> None:
        for relative_path in sorted(self.inventory):
            if not is_publishable_path(relative_path):
                continue
            text = self.text(relative_path)
            if text is None:
                continue
            checks = (
                ("possible public plate literal; redact it", CONTEXTUAL_PLATE_RE),
                ("possible explicit travel or location trail; remove or aggregate it", TRAVEL_TRAIL_RE),
                ("possible explicit travel or location trail; remove or aggregate it", EXPLICIT_TRAIL_RE),
            )
            reported: set[str] = set()
            for message, pattern in checks:
                match = pattern.search(text)
                if match and message not in reported:
                    line_number = text.count("\n", 0, match.start()) + 1
                    self.error(f"{relative_path}:{line_number}", message)
                    reported.add(message)
            for pattern in SECRET_PATTERNS:
                match = pattern.search(text)
                if match is not None:
                    line_number = text.count("\n", 0, match.start()) + 1
                    self.error(
                        f"{relative_path}:{line_number}",
                        "possible secret or credential detected; remove it",
                    )
                    break

    def validate(self) -> list[str]:
        self.errors = []
        self.text_cache = {}
        self.discover_inventory()
        self.validate_core_paths()
        self.validate_utf8_text()
        self.validate_version()
        self.validate_citation_metadata()
        requirement_ids, requirement_actors = self.validate_standard()
        source_ids, self.source_count = self.validate_sources()
        self.jurisdiction_inventory_count = self.validate_jurisdiction_inventory(source_ids)
        self.matrix_count = self.validate_matrix(source_ids, requirement_ids, requirement_actors)
        self.validate_repository_source_tokens(source_ids)
        self.validate_citation_sections(source_ids)
        self.validate_markdown_links()
        self.validate_sensitive_content()
        return self.errors

    def run(self) -> int:
        self.validate()
        if self.errors:
            print(
                f"OASPS repository validation failed with {len(self.errors)} "
                f"error{'s' if len(self.errors) != 1 else ''}:",
                file=self.stream,
            )
            for error in self.errors:
                print(f"  - {error}", file=self.stream)
            print("\nFix the listed issues, then run: python scripts/validate.py", file=self.stream)
            return 1
        print(
            "OASPS repository validation passed: "
            f"{len(EXPECTED_REQUIREMENT_IDS)} requirements, "
            f"{self.global_matrix_coverage}/{len(EXPECTED_REQUIREMENT_IDS)} canonical "
            f"FS-GLOBAL requirements covered, {self.source_count} sources, "
            f"{self.matrix_count} matrix rows, {self.jurisdiction_inventory_count} "
            f"Fairfield inventory rows, and "
            f"{len(self.inventory)} supported repository files checked.",
            file=self.stream,
        )
        return 0


def main() -> int:
    return Validator().run()


if __name__ == "__main__":
    sys.exit(main())
