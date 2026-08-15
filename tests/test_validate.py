"""Regression tests for the OASPS repository validator."""

from __future__ import annotations

import csv
import hashlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate import (
    CITATION_REQUIRED_FILES,
    CORE_DIRECTORIES,
    CORE_FILES,
    DEFAULT_ROOT,
    EXPECTED_REQUIREMENT_IDS,
    INVENTORY_HEADER,
    MATRIX_HEADER,
    SOURCE_HEADER,
    Validator,
)


class RepositoryFixture:
    """A complete, valid, untracked OASPS repository in a temporary Git repo."""

    def __init__(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "repository"
        self.root.mkdir()
        subprocess.run(
            ["git", "init", "-q", str(self.root)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for directory in CORE_DIRECTORIES:
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        for relative_path in CORE_FILES:
            path = self.root / relative_path
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.suffix == ".md":
                contents = "# Fixture\n"
            elif path.suffix in {".yml", ".yaml", ".cff"}:
                contents = "name: fixture\n"
            else:
                contents = "fixture\n"
            path.write_text(contents, encoding="utf-8")
        self.write(
            ".gitignore",
            "__pycache__/\n*.py[cod]\n.venv/\n.vscode/\n.coverage\nhtmlcov/\n"
            "evidence/local-*.md\n",
        )
        self.write("VERSION", "0.4.0-draft.1\n")
        self.write("CITATION.cff", "cff-version: 1.2.0\nlicense: CC-BY-4.0\n")
        for relative_path in CITATION_REQUIRED_FILES:
            self.write(
                relative_path,
                "# Fixture\n\n"
                "<!-- oasps-citations:start -->\n\n"
                "A fixture fact. [SRC-0001]\n\n"
                "<!-- oasps-citations:end -->\n",
            )
        self.write("STANDARD.md", self.standard_text())
        self.write_sources([self.source_row()])
        self.write_inventory([self.inventory_row()])
        self.write_matrix(
            self.global_matrix_rows(), complete_global_coverage=False
        )

    def close(self) -> None:
        self.temporary.cleanup()

    def write(self, relative_path: str, contents: str) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents, encoding="utf-8", newline="")

    def write_bytes(self, relative_path: str, contents: bytes) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(contents)

    @staticmethod
    def standard_text() -> str:
        blocks = ["# Fixture standard", ""]
        for requirement_id in sorted(EXPECTED_REQUIREMENT_IDS):
            blocks.extend(
                [
                    f"### {requirement_id} — Requirement title",
                    "",
                    "**Requirement:** A testable behavior is proposed.",
                    "",
                    "**Why it matters:** The behavior protects public accountability.",
                    "",
                    "**Responsible actor:** Shared",
                    "",
                    "**Expected proof:** Public records and review evidence.",
                    "",
                    "**Recognized basis:** General accountability guidance.",
                    "",
                    "**OASPS extension:** A surveillance-specific safeguard.",
                    "",
                ]
            )
        return "\n".join(blocks)

    @staticmethod
    def source_row(**updates: str) -> dict[str, str]:
        row = {field: "" for field in SOURCE_HEADER}
        row.update(
            {
                "source_id": "SRC-0001",
                "title": "Fixture source",
                "publisher": "Fixture publisher",
                "url": "https://example.com/source",
                "source_type": "Research",
                "published_date": "2026-08-13",
                "accessed_date": "2026-08-14",
                "jurisdiction": "Global",
                "retrieval_status": "Retrieved",
                "retrieved_at": "2026-08-14T12:00:00-04:00",
                "effective_date": "2026-08-13",
                "notes": "Fixture metadata.",
            }
        )
        row.update(updates)
        return row

    @staticmethod
    def matrix_row(**updates: str) -> dict[str, str]:
        row = {field: "" for field in MATRIX_HEADER}
        row.update(
            {
                "claim_id": "FS-GLOBAL-001",
                "requirement_id": "OASPS-A01",
                "subject": "Fixture system",
                "jurisdiction": "Global",
                "responsible_actor": "Shared",
                "finding": "An evidence-bounded fixture finding.",
                "documented_policy": "The fixture policy states a safeguard.",
                "technical_control": "A fixture control is documented.",
                "deployed_configuration": "The reviewed configuration is enabled.",
                "deployment_basis": "A dated configuration record.",
                "independent_verification": "The fixture record can be inspected.",
                "evidence_label": "Verified",
                "verified_fact": "The cited record contains the stated term.",
                "assessment": "Partly meets",
                "implementation_state": "Deployed now",
                "deployment_evidence_state": "Affirmative",
                "last_verified": "2026-08-14",
                "source_ids": "SRC-0001",
                "unresolved_question": "What additional proof is available?",
                "next_action": "Review another lawful public record.",
            }
        )
        row.update(updates)
        if (
            "implementation_state" in updates
            and "deployment_evidence_state" not in updates
        ):
            row["deployment_evidence_state"] = (
                "Affirmative" if row["implementation_state"] == "Deployed now" else ""
            )
        return row

    @staticmethod
    def inventory_row(**updates: str) -> dict[str, str]:
        row = {field: "" for field in INVENTORY_HEADER}
        row.update(
            {
                "system_id": "CT-FAIRFIELD-SYS-001",
                "system_name": "Fixture jurisdiction system",
                "vendor": "Fixture vendor",
                "operator": "Fixture agency",
                "technology_category": "Fixture camera technology",
                "jurisdiction": "Fairfield, Connecticut",
                "public_purpose": "A bounded public-safety purpose.",
                "documented_capabilities": "A dated record documents image capture.",
                "evidence_label": "Verified",
                "implementation_state": "Deployed now",
                "last_verified": "2026-08-15",
                "source_ids": "SRC-0001",
                "authorization_or_policy": "A dated public authorization record.",
                "retention_or_data_use": "A bounded public retention rule.",
                "sharing_or_access": "A bounded public access rule.",
                "notes": "Fixture inventory record.",
            }
        )
        row.update(updates)
        return row

    def global_matrix_rows(self) -> list[dict[str, str]]:
        return [
            self.matrix_row(
                claim_id=f"FS-GLOBAL-{number:03d}",
                requirement_id=requirement_id,
            )
            for number, requirement_id in enumerate(
                sorted(EXPECTED_REQUIREMENT_IDS), start=1
            )
        ]

    def write_sources(self, rows: list[dict[str, str]], header=SOURCE_HEADER) -> None:
        self._write_csv("evidence/sources.csv", header, rows)

    def write_matrix(
        self,
        rows: list[dict[str, str]],
        header=MATRIX_HEADER,
        complete_global_coverage: bool = True,
    ) -> None:
        if complete_global_coverage and tuple(header) == MATRIX_HEADER:
            canonical_rows = self.global_matrix_rows()
            canonical_claim_ids = {row["claim_id"] for row in canonical_rows}
            completed_rows: list[dict[str, str]] = []
            for canonical_row in canonical_rows:
                replacements = [
                    row
                    for row in rows
                    if row.get("claim_id") == canonical_row["claim_id"]
                ]
                completed_rows.extend(replacements or [canonical_row])
            completed_rows.extend(
                row for row in rows if row.get("claim_id") not in canonical_claim_ids
            )
            rows = completed_rows
        self._write_csv("case-studies/flock-safety/matrix.csv", header, rows)

    def write_inventory(
        self, rows: list[dict[str, str]], header=INVENTORY_HEADER
    ) -> None:
        self._write_csv("case-studies/fairfield-connecticut/inventory.csv", header, rows)

    def _write_csv(self, relative_path: str, header, rows: list[dict[str, str]]) -> None:
        buffer = io.StringIO(newline="")
        writer = csv.DictWriter(buffer, fieldnames=header, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        self.write(relative_path, buffer.getvalue())

    def track(self, relative_path: str) -> None:
        subprocess.run(
            ["git", "-C", str(self.root), "add", "--", relative_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = RepositoryFixture()
        self.addCleanup(self.fixture.close)

    def errors(self) -> list[str]:
        return Validator(self.fixture.root, stream=io.StringIO()).validate()

    def assert_valid(self) -> None:
        self.assertEqual([], self.errors())

    def assert_error(self, fragment: str) -> str:
        joined = "\n".join(self.errors())
        self.assertIn(fragment, joined)
        return joined

    def test_complete_fixture_passes(self) -> None:
        self.fixture.write("standard/future/additional-crosswalk.md", "# Additional crosswalk\n")
        self.fixture.write("case-studies/future/README.md", "# Future case\n")
        self.assert_valid()

    def test_cli_runs_from_an_unrelated_working_directory(self) -> None:
        shutil.copyfile(DEFAULT_ROOT / "scripts/validate.py", self.fixture.root / "scripts/validate.py")
        result = subprocess.run(
            [sys.executable, str(self.fixture.root / "scripts/validate.py")],
            cwd=self.fixture.root.parent,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("validation passed", result.stdout)

    def test_ignored_supported_artifact_is_not_in_inventory_or_scanned(self) -> None:
        self.fixture.write_bytes("evidence/local-note.md", b"\xff\xfe private")
        self.assert_valid()

    def test_ignored_dot_venv_directory_does_not_fail(self) -> None:
        self.fixture.write_bytes(".venv/cache/private.md", b"\xff\xfe ignored")
        self.assert_valid()

    def test_additional_jurisdiction_document_and_test_file_are_permitted(self) -> None:
        self.fixture.write(
            "case-studies/future/jurisdictions/example/README.md",
            "# Example jurisdiction\n",
        )
        self.fixture.write("tests/test_future.py", '"""Future validator test."""\n')
        self.assert_valid()

    def test_unsupported_untracked_candidate_is_not_published(self) -> None:
        self.fixture.write_bytes("assets/draft.bin", b"\xff\xfe")
        self.assert_valid()

    def test_unsupported_tracked_file_fails(self) -> None:
        self.fixture.write("config.toml", "enabled = true\n")
        self.fixture.track("config.toml")
        self.assert_error("tracked file is outside the supported path inventory")

    def test_missing_core_file_fails(self) -> None:
        (self.fixture.root / "README.md").unlink()
        self.assert_error("required core file is absent")

    def test_non_utf8_supported_file_fails(self) -> None:
        self.fixture.write_bytes("README.md", b"\xff\xfe")
        self.assert_error("must be readable UTF-8")

    def test_wrong_version_fails(self) -> None:
        self.fixture.write("VERSION", "0.2.0-draft.1\n")
        self.assert_error("0.4.0-draft.1")

    def test_citation_metadata_uses_single_content_license(self) -> None:
        self.fixture.write(
            "CITATION.cff",
            "cff-version: 1.2.0\n"
            "license:\n"
            "  - CC-BY-4.0\n"
            "  - MIT\n",
        )
        self.assert_error("root license must be the single value CC-BY-4.0")

    def test_source_header_order_is_exact(self) -> None:
        header = list(SOURCE_HEADER)
        header[0], header[1] = header[1], header[0]
        self.fixture.write_sources([self.fixture.source_row()], header)
        self.assert_error("header must be exactly, in order")

    def test_matrix_header_order_is_exact(self) -> None:
        header = list(MATRIX_HEADER)
        header[-1], header[-2] = header[-2], header[-1]
        self.fixture.write_matrix([self.fixture.matrix_row()], header)
        self.assert_error("header must be exactly, in order")

    def test_inventory_header_order_is_exact(self) -> None:
        header = list(INVENTORY_HEADER)
        header[-1], header[-2] = header[-2], header[-1]
        self.fixture.write_inventory([self.fixture.inventory_row()], header)
        self.assert_error("header must be exactly, in order")

    def test_inventory_schema_literal_is_stable(self) -> None:
        self.assertEqual(
            INVENTORY_HEADER,
            (
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
            ),
        )

    def test_inventory_ids_must_be_formatted_and_unique(self) -> None:
        self.fixture.write_inventory(
            [
                self.fixture.inventory_row(system_id="FAIRFIELD-1"),
                self.fixture.inventory_row(),
                self.fixture.inventory_row(),
            ]
        )
        joined = self.assert_error("system_id must match CT-FAIRFIELD-SYS-###")
        self.assertIn("appears 2 times", joined)

    def test_inventory_controlled_values_dates_and_sources(self) -> None:
        self.fixture.write_inventory(
            [
                self.fixture.inventory_row(
                    evidence_label="Reported",
                    implementation_state="Maybe current",
                    last_verified="2026-02-30",
                    source_ids="SRC-9999",
                )
            ]
        )
        joined = self.assert_error("'evidence_label' is not an allowed value")
        self.assertIn("'implementation_state' is not an allowed value", joined)
        self.assertIn("real ISO calendar date", joined)
        self.assertIn("is missing from evidence/sources.csv", joined)

    def test_inventory_jurisdiction_is_fairfield(self) -> None:
        self.fixture.write_inventory(
            [self.fixture.inventory_row(jurisdiction="Boston, Massachusetts")]
        )
        self.assert_error("jurisdiction must be exactly 'Fairfield, Connecticut'")

    def test_deployed_inventory_requires_a_resolved_source(self) -> None:
        self.fixture.write_inventory(
            [
                self.fixture.inventory_row(
                    evidence_label="Unknown",
                    implementation_state="Deployed now",
                    source_ids="",
                    unresolved_question="What public record establishes current deployment?",
                    next_action="Review a later-published current agency inventory.",
                )
            ]
        )
        self.assert_error(
            "source_ids is required for non-Unknown evidence or Deployed now state"
        )

    def test_incomplete_inventory_requires_question_and_next_action(self) -> None:
        for evidence_label, implementation_state in (
            ("Partially verifiable", "Deployed now"),
            ("Verified", "Historical"),
        ):
            with self.subTest(
                evidence_label=evidence_label,
                implementation_state=implementation_state,
            ):
                self.fixture.write_inventory(
                    [
                        self.fixture.inventory_row(
                            evidence_label=evidence_label,
                            implementation_state=implementation_state,
                            unresolved_question="",
                            next_action="",
                        )
                    ]
                )
                joined = self.assert_error(
                    "unresolved_question is required when current state is incomplete"
                )
                self.assertIn(
                    "next_action is required when current state is incomplete", joined
                )

    def test_source_required_fields_and_id_format(self) -> None:
        self.fixture.write_sources([self.fixture.source_row(source_id="SRC-12", publisher="")])
        joined = self.assert_error("required field 'publisher' is blank")
        self.assertIn("source_id must match SRC-####", joined)

    def test_duplicate_source_id_fails(self) -> None:
        self.fixture.write_sources([self.fixture.source_row(), self.fixture.source_row()])
        self.assert_error("appears 2 times")

    def test_source_controlled_values_fail(self) -> None:
        self.fixture.write_sources(
            [self.fixture.source_row(source_type="Blog", retrieval_status="Maybe")]
        )
        joined = self.assert_error("'source_type' is not an allowed value")
        self.assertIn("'retrieval_status' is not an allowed value", joined)

    def test_source_dates_must_be_real_iso_dates(self) -> None:
        self.fixture.write_sources(
            [self.fixture.source_row(published_date="2026-02-30", effective_date="08/14/2026")]
        )
        joined = self.assert_error("'published_date' must be a real ISO calendar date")
        self.assertIn("'effective_date' must be a real ISO calendar date", joined)

    def test_retrieved_at_requires_timezone(self) -> None:
        self.fixture.write_sources(
            [self.fixture.source_row(retrieved_at="2026-08-14T12:00:00")]
        )
        self.assert_error("ISO 8601 datetime with a timezone")

    def test_limited_retrieval_status_requires_notes(self) -> None:
        self.fixture.write_sources(
            [self.fixture.source_row(retrieval_status="Indexed-only", notes="")]
        )
        self.assert_error("limited retrieval_status requires a nonblank notes explanation")

    def test_valid_snapshot_and_computed_hash_pass(self) -> None:
        snapshot = "evidence/snapshots/source-0001.txt"
        payload = b"Lawfully preserved public text.\n"
        self.fixture.write_bytes(snapshot, payload)
        self.fixture.write_sources(
            [
                self.fixture.source_row(
                    local_snapshot=snapshot,
                    content_sha256=hashlib.sha256(payload).hexdigest(),
                )
            ]
        )
        self.assert_valid()

    def test_snapshot_and_hash_are_reciprocal(self) -> None:
        self.fixture.write("evidence/snapshots/source-0001.txt", "public text\n")
        self.fixture.write_sources(
            [self.fixture.source_row(local_snapshot="evidence/snapshots/source-0001.txt")]
        )
        self.assert_error("content_sha256 is required")
        self.fixture.write_sources([self.fixture.source_row(content_sha256="0" * 64)])
        self.assert_error("content_sha256 must be blank without local_snapshot")

    def test_snapshot_path_extension_and_inventory_are_restricted(self) -> None:
        self.fixture.write_bytes("evidence/snapshots/source.pdf", b"not a pdf")
        self.fixture.write_sources(
            [
                self.fixture.source_row(
                    local_snapshot="evidence/snapshots/source.pdf",
                    content_sha256=hashlib.sha256(b"not a pdf").hexdigest(),
                )
            ]
        )
        joined = self.assert_error("permitted UTF-8 text extension")
        self.assertIn("must be present in the repository inventory", joined)

    def test_snapshot_hash_must_be_lowercase_and_match(self) -> None:
        snapshot = "evidence/snapshots/source.txt"
        self.fixture.write(snapshot, "public text\n")
        self.fixture.write_sources(
            [self.fixture.source_row(local_snapshot=snapshot, content_sha256="A" * 64)]
        )
        self.assert_error("64 lowercase hexadecimal")
        self.fixture.write_sources(
            [self.fixture.source_row(local_snapshot=snapshot, content_sha256="0" * 64)]
        )
        self.assert_error("does not match local_snapshot bytes")

    def test_snapshot_cannot_escape_snapshot_directory(self) -> None:
        self.fixture.write_sources(
            [
                self.fixture.source_row(
                    local_snapshot="evidence/snapshots/../../README.md",
                    content_sha256="0" * 64,
                )
            ]
        )
        self.assert_error("stay safely under evidence/snapshots")

    def test_all_requirement_headings_are_required_once(self) -> None:
        text = self.fixture.standard_text()
        block_start = text.index("### OASPS-A01")
        next_block = text.index("### OASPS-A02")
        self.fixture.write("STANDARD.md", text[:block_start] + text[next_block:])
        self.assert_error("OASPS-A01 must appear exactly once (found 0)")

    def test_requirement_heading_format_is_strict(self) -> None:
        text = self.fixture.standard_text().replace(
            "### OASPS-A01 — Requirement title", "### OASPS-A01 - Requirement title", 1
        )
        self.fixture.write("STANDARD.md", text)
        self.assert_error("requirement heading must be")

    def test_requirement_has_exactly_six_nonblank_labels(self) -> None:
        text = self.fixture.standard_text().replace(
            "**Expected proof:** Public records and review evidence.", "**Expected proof:**", 1
        )
        self.fixture.write("STANDARD.md", text)
        self.assert_error("exactly one nonblank 'Expected proof' label")

        text = self.fixture.standard_text().replace(
            "**Expected proof:** Public records and review evidence.",
            "**Expected proof:** Public records and review evidence.\n\n"
            "**Expected proof:** A duplicate field.",
            1,
        )
        self.fixture.write("STANDARD.md", text)
        self.assert_error("exactly one nonblank 'Expected proof' label")

        text = self.fixture.standard_text().replace(
            "**Expected proof:** Public records and review evidence.\n\n", "", 1
        )
        self.fixture.write("STANDARD.md", text)
        self.assert_error("exactly one nonblank 'Expected proof' label")

    def test_requirement_actor_is_controlled(self) -> None:
        text = self.fixture.standard_text().replace(
            "**Responsible actor:** Shared", "**Responsible actor:** Everyone", 1
        )
        self.fixture.write("STANDARD.md", text)
        self.assert_error("uncontrolled responsible actor")

    def test_requirement_blocks_reject_vendor_specific_terms(self) -> None:
        text = self.fixture.standard_text().replace(
            "A testable behavior is proposed.", "A Flock Safety behavior is proposed.", 1
        )
        self.fixture.write("STANDARD.md", text)
        self.assert_error("contains a vendor-specific term")

        text = self.fixture.standard_text().replace(
            "### OASPS-A01 — Requirement title",
            "### OASPS-A01 — Flock Safety requirement",
            1,
        )
        self.fixture.write("STANDARD.md", text)
        self.assert_error("contains a vendor-specific term")

    def test_complete_global_requirement_coverage_passes(self) -> None:
        self.fixture.write_matrix(
            self.fixture.global_matrix_rows(), complete_global_coverage=False
        )
        stream = io.StringIO()
        validator = Validator(self.fixture.root, stream=stream)
        self.assertEqual(0, validator.run(), stream.getvalue())
        self.assertIn(
            "32/32 canonical FS-GLOBAL requirements covered", stream.getvalue()
        )

    def test_missing_global_requirement_coverage_fails(self) -> None:
        rows = self.fixture.global_matrix_rows()
        missing_requirement = rows.pop()["requirement_id"]
        self.fixture.write_matrix(rows, complete_global_coverage=False)
        self.assert_error(
            f"canonical FS-GLOBAL coverage for {missing_requirement} "
            "must appear exactly once (found 0)"
        )

    def test_duplicate_global_requirement_coverage_fails(self) -> None:
        rows = self.fixture.global_matrix_rows()
        duplicate_requirement = rows[0]["requirement_id"]
        rows.append(
            self.fixture.matrix_row(
                claim_id="FS-GLOBAL-999",
                requirement_id=duplicate_requirement,
            )
        )
        self.fixture.write_matrix(rows, complete_global_coverage=False)
        self.assert_error(
            f"canonical FS-GLOBAL coverage for {duplicate_requirement} "
            "must appear exactly once (found 2)"
        )

    def test_additional_local_context_rows_do_not_affect_global_coverage(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    claim_id="FS-CT-FAIRFIELD-999",
                    requirement_id="OASPS-A01",
                    jurisdiction="Fairfield, Connecticut",
                )
            ]
        )
        self.assert_valid()

    def test_matrix_ids_must_be_formatted_unique_and_resolved(self) -> None:
        first = self.fixture.matrix_row(claim_id="CLAIM-1", requirement_id="OASPS-Z99")
        second = self.fixture.matrix_row(claim_id="CLAIM-1")
        self.fixture.write_matrix([first, second])
        joined = self.assert_error("claim_id has an invalid format")
        self.assertIn("requirement_id must match", joined)
        self.assertIn("appears 2 times", joined)

    def test_matrix_controlled_values_fail(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    responsible_actor="Operator",
                    evidence_label="Certain",
                    assessment="Good",
                    implementation_state="Current",
                    deployment_evidence_state="Unclear",
                )
            ]
        )
        joined = self.assert_error("'responsible_actor' is not an allowed value")
        self.assertIn("'evidence_label' is not an allowed value", joined)
        self.assertIn("'assessment' is not an allowed value", joined)
        self.assertIn("'implementation_state' is not an allowed value", joined)
        self.assertIn("'deployment_evidence_state' is not an allowed value", joined)

    def test_matrix_source_references_must_be_formatted_and_resolve(self) -> None:
        self.fixture.write_matrix([self.fixture.matrix_row(source_ids="SRC-9999|SRC-12")])
        joined = self.assert_error("is missing from evidence/sources.csv")
        self.assertIn("malformed source ID", joined)

    def test_not_applicable_requires_reason_and_rejects_extraneous_reason(self) -> None:
        self.fixture.write_matrix(
            [self.fixture.matrix_row(assessment="Not applicable", applicability_reason="")]
        )
        self.assert_error("applicability_reason is required")
        self.fixture.write_matrix(
            [self.fixture.matrix_row(assessment="Partly meets", applicability_reason="Not needed")]
        )
        self.assert_error("applicability_reason must be blank")

    def test_actor_override_reason_tracks_standard_actor_mismatch(self) -> None:
        self.fixture.write_matrix(
            [self.fixture.matrix_row(responsible_actor="Vendor", actor_override_reason="")]
        )
        self.assert_error("actor_override_reason is required")
        self.fixture.write_matrix(
            [self.fixture.matrix_row(actor_override_reason="No mismatch exists")]
        )
        self.assert_error("actor_override_reason must be blank")

    def test_deployed_now_invariants(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    deployment_basis="",
                    deployed_configuration="Unknown current state.",
                    deployment_evidence_state="",
                    source_ids="",
                )
            ]
        )
        joined = self.assert_error("deployment_basis is required")
        self.assertIn("Deployed now requires source_ids", joined)
        self.assertIn("deployment_evidence_state is required", joined)

    def test_deployment_evidence_state_is_conditional(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    implementation_state="Unknown",
                    deployment_basis="",
                    deployment_evidence_state="Affirmative",
                )
            ]
        )
        self.assert_error("deployment_evidence_state must be blank")

    def test_deployment_basis_must_be_blank_for_other_states(self) -> None:
        self.fixture.write_matrix(
            [self.fixture.matrix_row(implementation_state="Unknown", deployment_basis="A basis")]
        )
        self.assert_error("deployment_basis must be blank")

    def test_verified_evidence_requires_fact_and_sources(self) -> None:
        self.fixture.write_matrix(
            [self.fixture.matrix_row(verified_fact="", source_ids="", implementation_state="Unknown", deployment_basis="")]
        )
        joined = self.assert_error("verified_fact is required")
        self.assertIn("Verified evidence requires source_ids", joined)

    def test_noncompliant_invariants_and_conditional_binding_field(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    evidence_label="Noncompliant",
                    verified_fact="",
                    binding_obligation="",
                    assessment="Partly meets",
                )
            ]
        )
        joined = self.assert_error("binding_obligation is required")
        self.assertIn("requires assessment 'Does not meet'", joined)
        self.fixture.write_matrix([self.fixture.matrix_row(binding_obligation="A law")])
        self.assert_error("binding_obligation must be blank")

    def test_unknown_evidence_with_definitive_assessment_requires_basis(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    evidence_label="Unknown",
                    verified_fact="",
                    assessment="Meets",
                    known_fact_basis="",
                )
            ]
        )
        self.assert_error("known_fact_basis is required")
        self.fixture.write_matrix([self.fixture.matrix_row(known_fact_basis="Not needed")])
        self.assert_error("known_fact_basis must be blank")

    def test_known_fact_basis_requires_resolved_source(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    evidence_label="Unknown",
                    verified_fact="",
                    assessment="Meets",
                    known_fact_basis="A narrow known fact supports the assessment.",
                    implementation_state="Unknown",
                    deployment_basis="",
                    source_ids="",
                )
            ]
        )
        self.assert_error(
            "known_fact_basis requires at least one resolved source_id"
        )

    def test_known_fact_basis_with_resolved_source_passes(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    evidence_label="Unknown",
                    verified_fact="",
                    assessment="Partly meets",
                    known_fact_basis="A cited record establishes the narrow known fact.",
                    implementation_state="Unknown",
                    deployment_basis="",
                    source_ids="SRC-0001",
                )
            ]
        )
        self.assert_valid()

    def test_unknown_assessment_does_not_require_basis_or_source(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    evidence_label="Unknown",
                    verified_fact="",
                    assessment="Unknown",
                    known_fact_basis="",
                    implementation_state="Unknown",
                    deployment_basis="",
                    source_ids="",
                )
            ]
        )
        self.assert_valid()

    def test_historical_state_requires_iso_as_of_and_no_deployment_basis(self) -> None:
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    implementation_state="Historical",
                    deployment_basis="",
                    historical_as_of="",
                )
            ]
        )
        self.assert_error("historical_as_of is required")
        self.fixture.write_matrix(
            [
                self.fixture.matrix_row(
                    implementation_state="Historical",
                    deployment_basis="",
                    historical_as_of="2026-02-30",
                )
            ]
        )
        self.assert_error("'historical_as_of' must be a real ISO calendar date")

    def test_valid_conditional_matrix_variants_pass(self) -> None:
        variants = (
            self.fixture.matrix_row(
                assessment="Not applicable",
                applicability_reason="The requirement does not govern this context.",
            ),
            self.fixture.matrix_row(
                responsible_actor="Vendor",
                actor_override_reason="This claim evaluates the vendor-controlled portion.",
            ),
            self.fixture.matrix_row(
                evidence_label="Noncompliant",
                verified_fact="",
                assessment="Does not meet",
                binding_obligation="A cited binding obligation applies.",
            ),
            self.fixture.matrix_row(
                evidence_label="Unknown",
                verified_fact="",
                assessment="Meets",
                known_fact_basis="A cited record establishes the narrow assessed fact.",
            ),
            self.fixture.matrix_row(
                implementation_state="Historical",
                deployment_basis="",
                historical_as_of="2026-08-13",
            ),
        )
        for row in variants:
            with self.subTest(row=row):
                self.fixture.write_matrix([row])
                self.assert_valid()

    def test_repository_source_tokens_resolve_and_placeholder_is_allowed(self) -> None:
        self.fixture.write(
            "ROADMAP.md",
            "# Sources\n\nUse SRC-#### as a placeholder and SRC-[0-9]{4} as the format.\n",
        )
        self.assert_valid()
        self.fixture.write("ROADMAP.md", "# Sources\n\nMissing source SRC-9999.\n")
        self.assert_error("source token 'SRC-9999' is missing")
        self.fixture.write("ROADMAP.md", "# Sources\n\nMalformed source SRC-12.\n")
        self.assert_error("source token 'SRC-12' is malformed")
        self.fixture.write("ROADMAP.md", "# Sources\n\nMalformed source SRC-.\n")
        self.assert_error("source token 'SRC-' is malformed")

    def test_designated_factual_file_requires_citation_markers(self) -> None:
        for relative_path in (
            "case-studies/flock-safety/FINDINGS.md",
            "case-studies/fairfield-connecticut/systems/automated-traffic-enforcement.md",
        ):
            with self.subTest(relative_path=relative_path):
                self.fixture.write(
                    relative_path,
                    "# Findings\n\nA factual narrative without citation boundaries.\n",
                )
                self.assert_error(
                    "designated evidence-bearing narrative must contain at least one "
                    "balanced citation section"
                )
                self.fixture.write(
                    relative_path,
                    "# Evidence\n\n"
                    "<!-- oasps-citations:start -->\n\n"
                    "A factual paragraph. [SRC-0001]\n\n"
                    "<!-- oasps-citations:end -->\n",
                )

    def test_marked_citation_sections_accept_citations_and_exemptions(self) -> None:
        self.fixture.write(
            "README.md",
            "# Evidence\n\n"
            "<!-- oasps-citations:start -->\n\n"
            "A factual paragraph. [SRC-0001]\n\n"
            "- A factual list item. [SRC-0001]\n\n"
            "<!-- oasps-citation-exempt: editorial -->\n"
            "An explicitly editorial paragraph.\n\n"
            "<!-- oasps-citation-exempt: editorial -->\n"
            "- An explicitly editorial list item.\n"
            "- A second item in the same contiguous editorial list.\n\n"
            "<!-- oasps-citations:end -->\n",
        )
        self.assert_valid()

    def test_citation_exemption_must_touch_the_exempt_paragraph(self) -> None:
        for separator in ("\n", "## Intervening heading\n", "<!-- unrelated -->\n"):
            with self.subTest(separator=separator):
                self.fixture.write(
                    "README.md",
                    "<!-- oasps-citations:start -->\n"
                    "<!-- oasps-citation-exempt: editorial -->\n"
                    f"{separator}An uncited factual paragraph.\n"
                    "<!-- oasps-citations:end -->\n",
                )
                self.assert_error("citation exemption is not immediately followed by prose")

    def test_citation_list_exemption_stops_after_the_contiguous_list(self) -> None:
        self.fixture.write(
            "README.md",
            "<!-- oasps-citations:start -->\n"
            "<!-- oasps-citation-exempt: editorial -->\n"
            "- An editorial list item.\n"
            "- Another editorial list item.\n\n"
            "An uncited factual paragraph.\n"
            "<!-- oasps-citations:end -->\n",
        )
        self.assert_error("prose in a marked citation section must end")

    def test_marked_prose_requires_trailing_citation(self) -> None:
        self.fixture.write(
            "README.md",
            "<!-- oasps-citations:start -->\nA factual paragraph without a citation.\n"
            "<!-- oasps-citations:end -->\n",
        )
        self.assert_error("must end with [SRC-####]")

    def test_trailing_citation_format_and_duplicates_are_rejected(self) -> None:
        self.fixture.write(
            "README.md",
            "<!-- oasps-citations:start -->\n"
            "A factual paragraph. [SRC-0001,SRC-0001]\n"
            "<!-- oasps-citations:end -->\n",
        )
        joined = self.assert_error("comma followed by one space")
        self.assertIn("duplicate source ID", joined)

    def test_citation_marker_and_exemption_syntax_is_balanced_and_controlled(self) -> None:
        self.fixture.write(
            "README.md",
            "<!-- oasps-citations:start -->\n"
            "<!-- oasps-citation-exempt: opinion -->\nText.\n",
        )
        joined = self.assert_error("exemption reason is not allowed")
        self.assertIn("start marker has no matching end marker", joined)

    def test_undesignated_methodology_file_may_omit_markers(self) -> None:
        self.fixture.write(
            "METHODOLOGY.md",
            "# Marker documentation\n\n"
            "Use `<!-- oasps-citations:start -->` to begin a section.\n\n"
            "A sentence mentions <!-- oasps-citations:end --> without making a boundary.\n\n"
            "Use `<!-- oasps-citation-exempt: editorial -->` immediately before prose.\n",
        )
        self.assert_valid()

    def test_relative_markdown_links_resolve_and_cannot_escape(self) -> None:
        self.fixture.write("ROADMAP.md", "[Missing](missing.md)\n")
        self.assert_error("relative Markdown link does not resolve")
        outside = self.fixture.root.parent / "outside.md"
        outside.write_text("outside\n", encoding="utf-8")
        self.fixture.write("ROADMAP.md", "[Outside](../outside.md)\n")
        self.assert_error("relative Markdown link escapes the repository")

    def test_sensitive_plate_detection_does_not_echo_value(self) -> None:
        sensitive = "ABC-1234"
        self.fixture.write("ROADMAP.md", f"A license plate was {sensitive}.\n")
        joined = self.assert_error("possible public plate literal")
        self.assertNotIn(sensitive, joined)

    def test_secret_detection_does_not_echo_value(self) -> None:
        sensitive = "SuperSecretValue12345"
        self.fixture.write("ROADMAP.md", f"api_key={sensitive}\n")
        joined = self.assert_error("possible secret or credential")
        self.assertNotIn(sensitive, joined)

    def test_explicit_travel_trail_detection_does_not_echo_content(self) -> None:
        sensitive = "Vehicle was observed at 10 Main Street then detected at 20 Main Street."
        self.fixture.write("ROADMAP.md", sensitive + "\n")
        joined = self.assert_error("possible explicit travel or location trail")
        self.assertNotIn(sensitive, joined)

    def test_explicit_labeled_personal_trail_is_detected(self) -> None:
        sensitive = "Location history for vehicle A1B2C3: 10 Main Street -> 20 Main Street"
        self.fixture.write("ROADMAP.md", sensitive + "\n")
        joined = self.assert_error("possible explicit travel or location trail")
        self.assertNotIn(sensitive, joined)

    def test_sensitive_rules_allow_identifiers_dates_and_process_prose(self) -> None:
        self.fixture.write(
            "METHODOLOGY.md",
            "plate SRC-0001\n"
            "plate 2026-08\n"
            "build 1ABC234\n"
            "A vehicle was observed by one test stage then detected by another.\n"
            "A vehicle was observed in one test stage then detected in another.\n"
            "movement history: raw -> normalized\n"
            "movement history for vehicle schema: raw -> normalized\n",
        )
        self.assert_valid()

    def test_text_snapshot_receives_source_and_sensitive_content_checks(self) -> None:
        snapshot = "evidence/snapshots/new-source.txt"
        self.fixture.write(snapshot, "Unresolved reference SRC-9999.\n")
        self.assert_error("source token 'SRC-9999' is missing")

        sensitive = "ABC-1234"
        self.fixture.write(snapshot, f"A license plate was {sensitive}.\n")
        joined = self.assert_error("possible public plate literal")
        self.assertNotIn(sensitive, joined)

    def test_workflow_is_pinned_and_runs_tests_before_validation(self) -> None:
        workflow = (DEFAULT_ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        self.assertIn("actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4", workflow)
        self.assertIn("actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5", workflow)
        self.assertIn('python-version: "3.12"', workflow)
        self.assertLess(
            workflow.index("python -m unittest discover -s tests -v"),
            workflow.index("python scripts/validate.py"),
        )


if __name__ == "__main__":
    unittest.main()
