# Conformance claim checklist

Record PASS / FAIL / NOT_MEASURED / NOT_APPLICABLE (with reason), exact commit and
test reference per item. This is a review aid, not certification.

- [ ] Identify protocol/profile, implementation, environment and bounded claim.
- [ ] Map every claimed requirement to positive and negative cases.
- [ ] Validate lengths, reserved fields, malformed inputs and unsupported versions.
- [ ] Separate receipt, origin authentication, freshness, binding and enforcement.
- [ ] Test stale/replayed/forged/conflicting/ambiguous or absent inputs.
- [ ] Preserve UNBOUND/AMBIGUOUS; absence is never permission.
- [ ] BLE: measure scan loss, interference, relay, power and permission limits.
- [ ] QR proposals: test copying/substitution, payload bounds and unsafe URLs.
- [ ] Authenticated proposals: test key rotation/revocation and downgrade.
- [ ] Device claims: record supported SDK/firmware and physical setup.
- [ ] Enforcement: trace policy to actual capture/storage/upload/training paths.
- [ ] Independently assess privacy, linkability, accessibility and failure feedback.
- [ ] Publish sanitized reproduction; disclose conflicts and missing evidence.

Parser CI supports only its synthetic T0 scope. Reuse existing
[vectors](../conformance/PPS-TEST-VECTORS-v0.1.md) and
[validation protocol](../docs/review/PPS-INDEPENDENT-VALIDATION-PROTOCOL-v0.1.md).
