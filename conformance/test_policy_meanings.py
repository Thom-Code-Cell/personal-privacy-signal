"""Literal spec-derived oracles; never derive expectations from parser constants."""

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "receiver-kit"))
from pps_reference_receiver import parse_discovery, trust_level  # noqa: E402

VECTORS = json.loads(
    (ROOT / "conformance/policy-meaning-vectors.json").read_text(encoding="utf-8")
)["vectors"]
BASE = bytes.fromhex("0101010000000000000000000000000000")


class PolicyMeaningTests(unittest.TestCase):
    def test_each_literal_policy_meaning(self):
        self.assertEqual(len(VECTORS), 8)
        for vector in VECTORS:
            with self.subTest(restriction=vector["restriction"]):
                parsed = parse_discovery(bytes.fromhex(vector["hex"]))
                self.assertEqual(parsed.restrictions, (vector["restriction"],))
                self.assertEqual(trust_level(parsed), "T0_DISCOVERED_UNVERIFIED")

    def test_all_combinations_have_exact_meanings(self):
        for flags in range(256):
            expected = tuple(
                vector["restriction"]
                for vector in VECTORS
                if flags & int.from_bytes(bytes.fromhex(vector["hex"])[3:5], "big")
            )
            frame = bytearray(BASE)
            frame[3:5] = flags.to_bytes(2, "big")
            with self.subTest(flags=flags):
                parsed = parse_discovery(frame)
                self.assertEqual(parsed.policy_flags, flags)
                self.assertEqual(parsed.restrictions, expected)
                self.assertEqual(trust_level(parsed), "T0_DISCOVERED_UNVERIFIED")

    def test_zero_flags_are_empty_restrictions_not_trusted_permission(self):
        parsed = parse_discovery(BASE)
        self.assertEqual(parsed.restrictions, ())
        self.assertEqual(trust_level(parsed), "T0_DISCOVERED_UNVERIFIED")
        # No consent/permission engine is implemented; empty restrictions cannot
        # demonstrate one. Integration behaviour remains outside this parser.

    def test_structured_byte_mutations(self):
        accepted = rejected = 0
        for offset in range(17):
            for value in range(256):
                frame = bytearray(BASE)
                frame[offset] = value
                reason = None
                if offset == 0 and value != 1:
                    reason = "unsupported_wire_version"
                elif offset == 1 and value != 1:
                    reason = "unsupported_frame_type"
                elif offset == 2 and value != 1:
                    reason = "unsupported_policy_version"
                elif offset == 3 and value != 0:
                    reason = "reserved_policy_flags"
                elif offset == 15 and value > 15:
                    reason = "reserved_capabilities"
                elif offset == 16 and value != 0:
                    reason = "reserved_nonzero"
                with self.subTest(offset=offset, value=value):
                    if reason:
                        with self.assertRaisesRegex(ValueError, f"^{reason}$"):
                            parse_discovery(frame)
                        rejected += 1
                    else:
                        parsed = parse_discovery(frame)
                        self.assertEqual(
                            trust_level(parsed), "T0_DISCOVERED_UNVERIFIED"
                        )
                        expected = tuple(
                            vector["restriction"]
                            for vector in VECTORS
                            if int.from_bytes(frame[3:5], "big")
                            & int.from_bytes(bytes.fromhex(vector["hex"])[3:5], "big")
                        )
                        self.assertEqual(parsed.restrictions, expected)
                        self.assertEqual(parsed.eid_hex, bytes(frame[5:13]).hex())
                        self.assertEqual(
                            parsed.epoch_hint, int.from_bytes(frame[13:15], "big")
                        )
                        self.assertEqual(parsed.capabilities, frame[15])
                        accepted += 1
        self.assertEqual((accepted, rejected), (2837, 1515))

    def test_all_short_lengths_and_oversize(self):
        for length in range(17):
            with self.subTest(length=length):
                with self.assertRaisesRegex(ValueError, "^invalid_length$"):
                    parse_discovery(BASE[:length])
        for length in (18, 31, 64, 255, 4096):
            with self.subTest(length=length):
                with self.assertRaisesRegex(ValueError, "^invalid_length$"):
                    parse_discovery(BASE + bytes(length - 17))
