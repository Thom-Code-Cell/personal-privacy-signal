"""Prove that the spec oracle detects every pairwise meaning swap, in memory only."""

import io
import itertools
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "receiver-kit"))
import pps_reference_receiver as receiver  # noqa: E402


def run_oracle():
    suite = unittest.defaultTestLoader.discover(
        str(ROOT / "conformance"), pattern="test_policy_meanings.py"
    )
    return unittest.TextTestRunner(stream=io.StringIO()).run(suite)


if __name__ == "__main__":
    baseline = run_oracle()
    if not baseline.wasSuccessful():
        raise SystemExit("FAIL: unmodified parser did not pass the policy oracle")
    original = dict(receiver.POLICY_BITS)
    detected = 0
    try:
        for left, right in itertools.combinations(sorted(original), 2):
            receiver.POLICY_BITS.clear()
            receiver.POLICY_BITS.update(original)
            receiver.POLICY_BITS[left], receiver.POLICY_BITS[right] = (
                original[right],
                original[left],
            )
            result = run_oracle()
            if result.errors or not result.failures:
                raise SystemExit(
                    f"FAIL: swap {left}/{right} was not an assertion failure"
                )
            detected += 1
    finally:
        receiver.POLICY_BITS.clear()
        receiver.POLICY_BITS.update(original)
    if detected != 28 or not run_oracle().wasSuccessful():
        raise SystemExit("FAIL: incomplete mutations or baseline restoration")
    print("PASS: all 28 pairwise meaning swaps detected; original parser restored")
