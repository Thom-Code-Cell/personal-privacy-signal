"""P8 tests exercise synthetic privacy decisions, never physical or military systems."""

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "pps_p8_reference", ROOT / "receiver-kit" / "pps_identity_location_reference.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def baseline(**changes):
    trial = {
        "operation": "identification",
        "personal_denies": [],
        "device_auth": "ABSENT",
        "subject_binding": "UNBOUND",
        "venue_state": "ABSENT",
        "venue_denies": [],
        "independent_legal_basis": False,
        "safety_authorization": "NONE",
        "receiver_enforcement": "SIMULATION",
        "context": "REAL",
    }
    trial.update(changes)
    return trial


class PPSIdentityLocationTest(unittest.TestCase):
    def test_fixtures(self):
        records = json.loads(
            (
                ROOT
                / "conformance"
                / "fixtures"
                / "p8-identity-location-scenarios.json"
            ).read_text("utf-8")
        )
        self.assertEqual(records["status"], "PROPOSED_SYNTHETIC_ONLY")
        self.assertEqual(records["hardware_validation"], "NOT_MEASURED")
        ids = []
        for case in records["cases"]:
            ids.append(case["id"])
            actual = MODULE.evaluate_policy(case["trial"])
            self.assertEqual(
                actual["candidate_decision"], case["expected_decision"], case["id"]
            )
            self.assertEqual(
                actual["actual_enforcement"], case["expected_enforcement"], case["id"]
            )
            self.assertEqual(actual["identity_claim"], "NONE")
            self.assertEqual(actual["location_claim"], "NONE")
            self.assertEqual(actual["evidence"], "SYNTHETIC_ONLY")
            self.assertFalse(
                any(
                    k in str(case["trial"]).lower()
                    for k in (
                        "face_template",
                        "gps",
                        "latitude",
                        "longitude",
                        "national_id",
                    )
                )
            )
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 20)

    def test_no_device_cannot_grant_identification(self):
        self.assertEqual(
            MODULE.evaluate_policy(baseline())["candidate_decision"], "REVIEW_REQUIRED"
        )

    def test_local_biometric_auth_does_not_identify_camera_subject(self):
        trial = baseline(
            device_auth="LOCAL_AUTH_ONLY",
            personal_denies=["identification"],
            subject_binding="UNBOUND",
        )
        self.assertEqual(
            MODULE.evaluate_policy(trial)["candidate_decision"], "REVIEW_REQUIRED"
        )

    def test_signal_absence_does_not_clear_building_restriction(self):
        trial = baseline(
            operation="profiling",
            venue_state="VERIFIED_APPLICABLE",
            venue_denies=["profiling"],
        )
        self.assertEqual(MODULE.evaluate_policy(trial)["candidate_decision"], "DENY")

    def test_website_claim_alone_not_enforceable_place_authority(self):
        trial = baseline(
            operation="profiling",
            venue_state="WEB_METADATA_ONLY",
            venue_denies=["profiling"],
        )
        self.assertEqual(
            MODULE.evaluate_policy(trial)["candidate_decision"], "REVIEW_REQUIRED"
        )

    def test_unverified_signal_not_anonymous_kill_switch(self):
        trial = baseline(
            personal_denies=["identification"],
            device_auth="ABSENT",
            subject_binding="AMBIGUOUS",
        )
        self.assertEqual(
            MODULE.evaluate_policy(trial)["candidate_decision"], "REVIEW_REQUIRED"
        )

    def test_game_framing_cannot_allow_harmful_reuse(self):
        for context in ("REAL", "GAME_FRAMING"):
            trial = baseline(operation="harmful_downstream_reuse", context=context)
            self.assertEqual(
                MODULE.evaluate_policy(trial)["candidate_decision"], "DENY"
            )

    def test_emergency_claim_does_not_override_place_policy(self):
        trial = baseline(
            operation="safety_inference",
            venue_state="VERIFIED_APPLICABLE",
            venue_denies=["safety_inference"],
            safety_authorization="INDEPENDENTLY_AUTHORIZED_NARROW",
            independent_legal_basis=True,
        )
        self.assertEqual(MODULE.evaluate_policy(trial)["candidate_decision"], "DENY")

    def test_recipient_never_claims_real_enforcement(self):
        trial = baseline(
            operation="harmful_downstream_reuse", receiver_enforcement="UNSUPPORTED"
        )
        result = MODULE.evaluate_policy(trial)
        self.assertEqual(result["candidate_decision"], "DENY")
        self.assertEqual(result["actual_enforcement"], "UNSUPPORTED")

    def test_raw_biometrics_and_location_rejected(self):
        for field in (
            "face_template",
            "gps",
            "latitude",
            "longitude",
            "national_id",
            "face_embedding",
            "tracking_identifier",
        ):
            with self.subTest(field=field), self.assertRaises(ValueError):
                MODULE.evaluate_policy(baseline(**{field: "sensitive"}))

    def test_malformed_values_rejected(self):
        for change in (
            {"personal_denies": ["identification", "identification"]},
            {"independent_legal_basis": "true"},
            {"device_auth": "SPOOFED"},
            {"operation": "weapon_command"},
            {"venue_state": None},
        ):
            with self.subTest(change=change), self.assertRaises(ValueError):
                MODULE.evaluate_policy(baseline(**change))


if __name__ == "__main__":
    unittest.main()
