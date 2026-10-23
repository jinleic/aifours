# Checkpoint 007 (rqls10 continuation)

Recorded 2026-10-19T01:37:03-0700. Owner ContinueRQLS10.

## Claim / actual result
- Target OPEN / UNKNOWN; no candidate.
- v8 R7 (GO 272e6ba6...): SETTLED, rc 0. All gates (A, C1, C1p, C2, A5, C3r, C4r, KPc, KRc) passed before R7; the
  v = 7 / v = 8 maximal replays and the KRc seeds reproduced v3 / v7 exactly. R7 actual: 256 distinct forced Z_7+3
  configurations, 2048 runs completed, 0 skips; 261 verified endpoints (164 configurations), all with 10 rays;
  0 maximal candidates. Scoped UNKNOWN, no detection power claimed.
- W8 native LM v2 frozen; separate GO requested (v1 is an unrun draft superseded for the supervisor GO/SIGTERM protocol;
  its config rqls_w8_lm_v1.supervisor-config-v2.json must not be used).

## Files (sha256)
- evidence/rqls_assay_v8.r7.sv2.receipt.md: b82516124b3a0f4a9ef6714b8a6b7648fea175ad996291c3944c989510fb4e5c
- evidence/rqls_assay_v8.r7.sv2.result.jsonl: f6bdb6f403f1c7433de1bdc8db21411d5e40fea45455eb2a7c94c4f24b72a2dd
- evidence/rqls_assay_v8.r7.sv2.supervisor-receipt.json: dddb7e66a081b4b99db3fb14dc73cb40d72db2df0845e8106ed67201d77b5601
- evidence/stability-gate.v8-r7.v2.json: dd514e229301ddac213cfefcb2b1187fcd3bf5009d5c263e3eef8be02653ab32
- code/rqls_w8_lm_v2.py: d336e2e3d3fdbc0afe9cc1e55232524466152e4369519e47a387cc9caf061ca2
- evidence/rqls_w8_lm_v2.supervisor-config-v2.json: 84c93e519a54a4808248830879f782c248d000ba58714c8d7c5f998f954438d4
- code/rqls_w8_lm_v1.py: b34ee34a363bb5a3279847759e33dbd9faade9f882f5cfbc121aaaf894899a66
- evidence/rqls_w8_lm_v1.supervisor-config-v2.json: 419f605e7a82830d256d9116f335f54a8270170619bb11a8316b2894fc6fdf04
- evidence/w8-wh5-c2-orbit-ansatz-addendum-1.md: 213f2fa7115d84c47b42c0237165a44c7d579d1f577498450ef97c092edc2fc9

## Blocker
W8 LM GO pending. No process running.
