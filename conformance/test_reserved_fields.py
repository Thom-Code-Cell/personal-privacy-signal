"""Negative vectors for reserved semantics; no radio or authentication test."""

import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "receiver-kit"))
from pps_reference_receiver import parse_discovery, trust_level  # noqa: E402

VALID = bytes.fromhex("01010100e7a1a2a3a4a5a6a7a812340b00")


class ReservedFieldsTests(unittest.TestCase):
    def test_every_unsupported_policy_version(self):
        for version in range(256):
            if version != 1:
                with self.assertRaisesRegex(ValueError, "unsupported_policy_version"):
                    parse_discovery(VALID[:2] + bytes([version]) + VALID[3:])

    def test_each_reserved_flag(self):
        for bit in range(8, 16):
            frame = bytearray(VALID)
            frame[3:5] = (1 << bit).to_bytes(2, "big")
            with self.assertRaisesRegex(ValueError, "reserved_policy_flags"):
                parse_discovery(frame)

    def test_each_reserved_capability(self):
        for bit in range(4, 8):
            frame = bytearray(VALID)
            frame[15] = 1 << bit
            with self.assertRaisesRegex(ValueError, "reserved_capabilities"):
                parse_discovery(frame)

    def test_all_supported_flags_remain_t0(self):
        for flags in range(256):
            frame = bytearray(VALID)
            frame[3:5] = flags.to_bytes(2, "big")
            parsed = parse_discovery(frame)
            self.assertEqual(trust_level(parsed), "T0_DISCOVERED_UNVERIFIED")
            self.assertEqual(len(parsed.restrictions), flags.bit_count())

    def test_seeded_malformed_corpus(self):
        rng = random.Random(20261021)
        for _ in range(10000):
            frame = rng.randbytes(rng.randrange(65))
            try:
                parsed = parse_discovery(frame)
            except ValueError:
                continue
            self.assertEqual(trust_level(parsed), "T0_DISCOVERED_UNVERIFIED")
            self.assertEqual(len(frame), 17)

    def test_wrong_frame_type(self):
        with self.assertRaisesRegex(ValueError, "unsupported_frame_type"):
            parse_discovery(VALID[:1] + b"\x02" + VALID[2:])
