# Current evidence and security boundaries

This is the current branch's evidence index; earlier reports remain historical.
Every result must identify its exact head and whether local, CI or physical evidence.
The parser API returns restrictions, not consent, identity or an enforced decision.

| Property | Implementation / evidence | Permitted claim |
|---|---|---|
| 17-byte syntax, supported fields, flag meaning | Python parser; spec-derived unit vectors and structured mutations | tested synthetic T0 parsing only |
| Zero flags | empty restriction tuple, always T0 | no affirmative consent inferred; no permission engine exists |
| Capability flags | decoded bytes only | no evidence any declared mechanism actually ran |
| BLE discovery stack / assigned transport identifier | absent | NOT_IMPLEMENTED; no registered PPS BLE allocation claimed |
| Authenticated origin / freshness / replay protection | absent | UNSUPPORTED; epoch_hint is not authentication |
| Person or venue binding / authority | absent | NOT_MEASURED; proximity or valid signature alone proves neither |
| EID generation/rotation / unlinkability | requirements only, no lifecycle implementation | NOT_MEASURED; no anonymity guarantee |
| Policy resolver / key recovery / canonical T1 representation | not implemented | UNSUPPORTED; hashing alone authenticates nothing |
| Capture/storage/upload/training enforcement | absent | UNSUPPORTED; no control over uncooperative devices |
| Android Mobile Binding external lab assertions | source artifacts missing in this repository | REPORTED_EXTERNALLY_NOT_VERIFIED_HERE |
| Vuzix and other physical device validation | none in this branch | NOT_MEASURED |
| License scope / patent clearance | license reference exists; authority/inventory review pending | no new grant or FTO conclusion |

## State and operation boundaries for the current implementation

| State/property | Available here | Protected operations and reporting boundary |
|---|---|---|
| Invalid or unsupported frame | ValueError | reject parsing; rejection is never consent or permission |
| DISCOVERED_UNVERIFIED | only successful parser trust result | report syntactic restrictions only; do not claim identity, authenticity or enforcement |
| UNSEEN, EXPIRED/DISCONNECTED | no lifecycle/timeout engine | do not infer permission from absence; no validity extension claim |
| AUTHENTICATED_UNBOUND | not implemented | no T1 result or camera-to-person assertion |
| AMBIGUOUS, BOUND_LOW/HIGH_CONFIDENCE | not implemented | no T2 result, no automatic subject selection |
| Safety exception | not implemented | a radio assertion authorizes no emergency override |

This table bounds present claims; it does not invent a normative resolver or an
anonymous kill switch. Candidate privacy restrictions and availability/safety
requirements still need an explicit reviewed integration design. A UI notice is
not a blocked operation. No missing signal overrides independently applicable rules.

## Required profile decisions before implementation or higher claims

1. State × operation × trust × policy-conflict × exception decision table, including
   malformed, unknown, lost, stale and multi-subject cases; no permissive ambiguity.
2. Exact canonical policy bytes and cross-language vectors; algorithms, key authority,
   establishment, rotation, expiry, revocation, compromise recovery and authenticated
   version negotiation. No custom cryptography or implicit trust in SHA-256.
3. Explicit laboratory transport parameters, ownership/assignment status, maximum
   input lengths and concrete per-target CPU, RAM, queue, retry and UI budgets.
4. Replay/flood/relay and downgrade measurements, including tradeoffs between
   restrictive privacy outcomes and safety/availability; independent second implementation.
5. Binding ground truth and error/coverage thresholds; actual downstream enforcement
   by domain; override authorization, duration and auditable restoration.

No arbitrary number in a planning example becomes a normative budget. Frozen
versions are not silently redefined. Use the existing proposal/change process.

## Privacy verification before a field claim (IR-06)

Predeclare passive observer capabilities and a no-PPS baseline. Inspect BLE public/
random address behaviour jointly with EID rotation, rare policy/capability patterns,
time/location trajectories and cross-transport links. Define linkage success,
uncertainty and residual risk rather than claiming rotation equals anonymity.
Measure storage/network behaviour and deletion; use synthetic records first.
Keep raw EIDs, consent/contact keys and movement traces outside Git/CI; assess
small aggregates for reidentification. No participant collection is authorized here.
