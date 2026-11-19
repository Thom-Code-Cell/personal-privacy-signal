#!/usr/bin/env python3
"""Validate proposed P7 scenario metadata only. Not a policy or enforcement test."""

from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
FILE = BASE / "conformance" / "fixtures" / "p7-governance-scenarios.json"
REQUIRED = {f"P7-{i:02d}" for i in range(1, 15)}
ALLOWED = {
    "PROHIBIT",
    "LIMITED_EXTERNAL_APPROVAL",
    "NO_CONSENT_INFERENCE",
    "NO_TRUST_UPGRADE",
    "AUDIT_REQUIRED",
}


def validate() -> int:
    data = json.loads(FILE.read_text(encoding="utf-8"))
    assert data.get("status") == "PROPOSED_NOT_MEASURED", "Incorrect evidence status"
    assert data.get("executable_enforcement") is False, (
        "Must not claim runtime enforcement"
    )
    entries = data["scenarios"]
    ids = [entry["id"] for entry in entries]
    assert len(ids) == len(set(ids)), "Duplicate scenario IDs"
    assert set(ids) == REQUIRED, (
        f"Missing/unexpected P7 IDs: {sorted(set(ids) ^ REQUIRED)}"
    )
    for entry in entries:
        assert (
            entry.get("title") and entry.get("risk") and entry.get("expected_control")
        ), entry
        assert entry.get("expected_result") in ALLOWED, entry
        assert entry.get("status") == "NOT_MEASURED", entry
        assert entry.get("real_human_data") is False, entry
        assert entry.get("requires_independent_enforcement_test") is True, entry
        assert "target_coordinates" not in entry and "weapon_command" not in entry, (
            entry
        )
    index = {entry["id"]: entry for entry in entries}
    assert index["P7-01"]["expected_result"] == "NO_CONSENT_INFERENCE"
    assert index["P7-07"]["expected_result"] == "PROHIBIT"
    assert index["P7-08"]["expected_result"] == "NO_TRUST_UPGRADE"
    assert index["P7-11"]["expected_result"] == "PROHIBIT"
    assert index["P7-05"]["expected_result"] == "LIMITED_EXTERNAL_APPROVAL"
    assert index["P7-13"]["expected_result"] == "NO_CONSENT_INFERENCE"
    return len(entries)


if __name__ == "__main__":
    print(f"P7 FIXTURE-STRUCTURE PASS: {validate()} proposed scenarios")
    print("NOT RUN: policy engine, model, OS/firmware, safety or device enforcement")
