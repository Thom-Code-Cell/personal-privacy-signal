"""PPS v0.1 candidate T0 discovery parser. No authentication or subject binding."""
from dataclasses import dataclass
WIRE_VERSION=1
FRAME_TYPE_MOBILE_PERSON=1
FRAME_LEN=17
POLICY_BITS={1:"capture_deny",2:"identification_deny",4:"profiling_deny",8:"emotion_inference_deny",16:"retention_deny",32:"cloud_upload_deny",64:"training_deny",128:"commercial_use_deny"}
@dataclass(frozen=True)
class PpsDiscovery:
    wire_version:int; frame_type:int; policy_version:int; policy_flags:int; eid_hex:str; epoch_hint:int; capabilities:int; restrictions:tuple
def parse_discovery(payload):
    if len(payload)!=FRAME_LEN: raise ValueError("invalid_length")
    if payload[0]!=WIRE_VERSION: raise ValueError("unsupported_wire_version")
    if payload[1]!=FRAME_TYPE_MOBILE_PERSON: raise ValueError("unsupported_frame_type")
    if payload[16]!=0: raise ValueError("reserved_nonzero")
    flags=int.from_bytes(payload[3:5],"big")
    restrictions=tuple(name for bit,name in POLICY_BITS.items() if flags & bit)
    return PpsDiscovery(payload[0],payload[1],payload[2],flags,payload[5:13].hex(),int.from_bytes(payload[13:15],"big"),payload[15],restrictions)
def trust_level(_parsed):
    return "T0_DISCOVERED_UNVERIFIED"
