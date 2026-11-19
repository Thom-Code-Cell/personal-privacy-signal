"""PPS+ P8: synthetic-only, purpose-bound policy decision *illustrator*.

This is NOT a receiver, identity verification, geolocation engine, camera controller,
legal authorization oracle, OS policy hook or safety interlock. No I/O, sensors,
biometrics, personal identifiers or cryptographic verification are implemented.

All input trust states are *fixture assertions* for negative-policy experiments.
"""

from __future__ import annotations

from typing import Any

OPERATIONS = frozenset(
    {
        "capture",
        "identification",
        "profiling",
        "retention",
        "cloud_upload",
        "training",
        "safety_inference",
        "harmful_downstream_reuse",
    }
)
STATES_DEVICE = frozenset({"ABSENT", "LOCAL_AUTH_ONLY", "SESSION_VERIFIED"})
STATES_BINDING = frozenset({"UNBOUND", "AMBIGUOUS", "INDEPENDENTLY_VERIFIED"})
STATES_VENUE = frozenset(
    {
        "ABSENT",
        "WEB_METADATA_ONLY",
        "SIGNED_ZONE_UNCONFIRMED",
        "EXPIRED",
        "VERIFIED_APPLICABLE",
    }
)
STATES_SAFETY = frozenset({"NONE", "INDEPENDENTLY_AUTHORIZED_NARROW"})
STATES_ENFORCEMENT = frozenset({"SIMULATION", "UNSUPPORTED"})
STATES_CONTEXT = frozenset({"REAL", "GAME_FRAMING"})
ALLOWED_KEYS = frozenset(
    {
        "operation",
        "personal_denies",
        "device_auth",
        "subject_binding",
        "venue_state",
        "venue_denies",
        "independent_legal_basis",
        "safety_authorization",
        "receiver_enforcement",
        "context",
    }
)


def _require_str_enum(name: str, value: Any, allowed: frozenset[str]) -> str:
    if not isinstance(value, str) or value not in allowed:
        raise ValueError(f"Invalid {name}")
    return value


def _validated_operations(name: str, value: Any) -> frozenset[str]:
    if not isinstance(value, list) or len(value) > len(OPERATIONS):
        raise ValueError(f"Invalid {name}")
    if any(not isinstance(v, str) or v not in OPERATIONS for v in value):
        raise ValueError(f"Invalid {name}")
    if len(set(value)) != len(value):
        raise ValueError(f"Duplicate {name}")
    return frozenset(value)


def evaluate_policy(trial: dict[str, Any]) -> dict[str, str]:
    """Evaluate one closed-schema synthetic policy fixture; never control a device.

    Return a candidate *policy* decision and the separate enforcement-evidence state.
    Device/session authentication is **not** personal or camera identity proof.
    Unidentified humans have the same baseline human-safety protection as others.
    """
    if not isinstance(trial, dict) or set(trial) != ALLOWED_KEYS:
        raise ValueError(
            "Unexpected/missing field; raw location, biometrics and identifiers prohibited"
        )
    if len(str(trial)) > 4096:
        raise ValueError("Oversized trial")
    operation = _require_str_enum("operation", trial["operation"], OPERATIONS)
    personal_denies = _validated_operations("personal_denies", trial["personal_denies"])
    device_auth = _require_str_enum("device_auth", trial["device_auth"], STATES_DEVICE)
    subject_binding = _require_str_enum(
        "subject_binding", trial["subject_binding"], STATES_BINDING
    )
    venue_state = _require_str_enum("venue_state", trial["venue_state"], STATES_VENUE)
    venue_denies = _validated_operations("venue_denies", trial["venue_denies"])
    legal_basis = trial["independent_legal_basis"]
    if type(legal_basis) is not bool:
        raise ValueError("Invalid independent_legal_basis")
    safety = _require_str_enum(
        "safety_authorization", trial["safety_authorization"], STATES_SAFETY
    )
    enforcement = _require_str_enum(
        "receiver_enforcement", trial["receiver_enforcement"], STATES_ENFORCEMENT
    )
    _require_str_enum("context", trial["context"], STATES_CONTEXT)

    # A person's protection does not depend on registration, device presence or
    # a vendor's attempted classification of that person.
    if operation == "harmful_downstream_reuse":
        decision, reason = (
            "DENY",
            "Harmful reuse prohibited independently of identity or signal",
        )
    elif venue_state == "VERIFIED_APPLICABLE" and operation in venue_denies:
        decision, reason = "DENY", "Verified, applicable place restriction"
    elif (
        operation in personal_denies
        and device_auth == "SESSION_VERIFIED"
        and subject_binding == "INDEPENDENTLY_VERIFIED"
    ):
        decision, reason = "DENY", "Bound and verified restrictive personal preference"
    elif operation == "safety_inference" and (
        safety == "INDEPENDENTLY_AUTHORIZED_NARROW" and legal_basis
    ):
        decision, reason = (
            "SCOPED_REVIEW",
            "Safety processing remains scope-limited and requires real enforcement",
        )
    else:
        decision, reason = (
            "REVIEW_REQUIRED",
            "No grant inferred; independent policy and legality checks needed",
        )

    return {
        "candidate_decision": decision,
        "reason": reason,
        "actual_enforcement": "UNSUPPORTED"
        if enforcement == "UNSUPPORTED"
        else "SIMULATED_ONLY",
        "identity_claim": "NONE",
        "location_claim": "NONE",
        "person_target_classification": "NEVER_PERFORMED",
        "evidence": "SYNTHETIC_ONLY",
    }
