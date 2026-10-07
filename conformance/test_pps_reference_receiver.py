import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"receiver-kit"))
from pps_reference_receiver import parse_discovery,trust_level
VALID=bytes.fromhex("01010100e7a1a2a3a4a5a6a7a812340b00")
class PpsParserTests(unittest.TestCase):
    def test_valid(self):
        p=parse_discovery(VALID)
        self.assertEqual(p.policy_flags,0x00e7)
        self.assertEqual(p.eid_hex,"a1a2a3a4a5a6a7a8")
        self.assertEqual(trust_level(p),"T0_DISCOVERED_UNVERIFIED")
        self.assertIn("capture_deny",p.restrictions)
        self.assertIn("cloud_upload_deny",p.restrictions)
        self.assertIn("training_deny",p.restrictions)
    def test_wrong_length(self):
        with self.assertRaisesRegex(ValueError,"invalid_length"): parse_discovery(VALID[:-1])
    def test_wrong_version(self):
        with self.assertRaisesRegex(ValueError,"unsupported_wire_version"): parse_discovery(bytes([2])+VALID[1:])
    def test_reserved_nonzero(self):
        with self.assertRaisesRegex(ValueError,"reserved_nonzero"): parse_discovery(VALID[:-1]+bytes([1]))
if __name__=="__main__": unittest.main()
