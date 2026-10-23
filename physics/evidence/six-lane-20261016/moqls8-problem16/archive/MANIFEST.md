# Lane archive manifest

## 2026-10-18 — named r3 quarantine retirement

Parent explicitly authorised this MOVE after source/delta pin review, static PASS and the one non-native smoke.
Collision checks and source hashing ran under the capacity flock at host2026-10-18T05:08:11-07:00; the destination
directory was fresh and x-created. No invocation was active in this lane's reserved pipeline. No deletion occurred.

- Source: `evidence/N8_FONE_REFINE_R3_QUARANTINE.json`
- Destination: `archive/n8-r3-quarantine-20261018/N8_FONE_REFINE_R3_QUARANTINE.json`
- Bytes:1177
- SHA-256: `c5f76542ff09bbac3a4ea75a4ed2eb22787feb07a60388e8b87354d2f34c1081`
- Method: tool MOVE of ONLY the named quarantine; basename and bytes preserved, no overwrite.
- Reason: retire a correctly fail-closed historical quarantine after the setuid-ps RSS paths were removed and
  their non-setuid replacements passed the authorised validation. This does NOT reclassify the old leaf as UNSAT.
- Old result: P1-B1.L1.000 remains UNKNOWN; old ledger `refine_v3/P1-B1/LEDGER.v003.json` SHA
  `295da85e9ea32a738dc57096d16c900854cd55de7165e107d781928f659753a0` remains unchanged/REFINED with all8L2.
- Old no-survivor evidence: `evidence/N8_FONE_R3.P1-B1.1792322536667751000.json` SHA
  `2b1e92e617b584cb875635d93a26d697b971507d85ea085c9551c819ebae1ec5`; owned-group SIGTERM, survivors[],
  listing_ok=true, killpg_error=null, leader−15. Parent disposition SHA
  `2cdf49b1d03374323c89bac62fba6c7c09aa6856c47db120d7e124aac0217681` confirms the UNKNOWN and correct stop.
- Static validation: `evidence/n8_refine_r4_static_controls_v1/RESULT.json` SHA
  `e2e1e2a2169504e8717a5942d00d9336bb927904f54c6c95a789f7b9c0ab3676`.
- Non-native smoke: `evidence/N8_NOSETUID_R4_SMOKE.result.json` SHA
  `90df761c8508c32642805dafa40651dff6cc5273aa602f014d5698278ce033d8`; clean/zero observed unknown probes.
  Its outer record SHA `2c69c886f93e038f29e0ffa828f6e7b07824fa7e7b5e10ec2a47699ed84196ce` has rc0,
  final problems[]/alive_others[], no smoke quarantine. Production quarantine was byte-preserved during that smoke.

Rollback: ONLY while no invocation is active and while holding the same capacity flock, verify the destination
SHA above and confirm the original path is absent. Then, from this lane, restore it by MOVE (never overwrite a
new quarantine):

```sh
mv archive/n8-r3-quarantine-20261018/N8_FONE_REFINE_R3_QUARANTINE.json evidence/N8_FONE_REFINE_R3_QUARANTINE.json
```

## Creation-only deviation and exact r3 source preservation

`code/run_n8_fone_refine.py` was edited **at the same active path**, not created under a new filename, between
r3 SHA `8598808d14601658751961bc1d157cd3ac2c38847b4d4c0d159e6172bd72f9d4` (23858bytes) and r4 SHA
`7d28ecbe1ac9fdf1c31ff0559ad6fb14349b9938e9c3e4842f2064f8e6cf0b3b` (25068bytes). This is a creation-only
discipline deviation. The exact r3 bytes, captured before the r4 edit and retained in the host eval state, are now
x-preserved at `archive/n8-r3-quarantine-20261018/run_n8_fone_refine.r3-preserved.py`, SHA
`8598808d14601658751961bc1d157cd3ac2c38847b4d4c0d159e6172bd72f9d4`. They are historical evidence,
NOT the active production file and not permission to rerun the failed leaf.

The same-path helper header also had a comment-only change from72a2737d…a96c to d9f191bf…7853. Its exact
r3 file is x-preserved as `archive/n8-r3-quarantine-20261018/n8_fone_refine_bytes.r3-preserved.py`,2272bytes,
SHA `72a2737d944f6727ba2176de4def66f60164c989d0d4b833948f9f7cd1efa96c`. This copy was reconstructed by
reversing ONLY the recorded two-line comment delta, then required to match the pinned72a2737d hash; it was not
represented as an independently retained snapshot. The data functions and child bytes are unchanged.

Parent has frozen ALL active code. Any further fix MUST use a separately versioned path and a new review;
no further in-place active-code edits are authorised. Archive source copies are never run as production.
