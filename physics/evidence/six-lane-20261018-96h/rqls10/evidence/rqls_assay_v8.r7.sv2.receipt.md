# Receipt: rqls_assay_v8 R7 target assay (parent GO 272e6ba6...ee26)

Recorded 2026-10-19T01:36:37-0700. GO institute/runs/six-lane-2026-10-18-96h/review/rqls10-v8-r7-target-parent-GO-v1.json sha256
272e6ba677ad832347c218c9bb0a296622ffba6e5f71c8f6e6916a4fe72bee26; tightening 8ac55669...aa20. Pins re-hashed equal at launch
(v8 0988a73b..., config a763a6a7..., supervisor 1fece595..., gate 1f62874a...).

Chain (cwd lane, tool timeout 0, TMPDIR lane/tmp): stability_gate_v2 (projected 20,971,520 B) && owned_supervisor_v2.
Gate receipt evidence/stability-gate.v8-r7.v2.json sha256 dd514e229301ddac213cfefcb2b1187fcd3bf5009d5c263e3eef8be02653ab32: PASS (30 samples,
span 290 s, age 8 s, max drop 30,584,832 <= 14,982,401,557). Supervisor PID 32593; child PID 32595 = PGID 32595; start
2026-10-19T01:23:22-0700 (epoch 1792398203.00); CHAIN_END 2026-10-19T01:36:12-0700; wall 768.99 s; EXITED rc 0; no trips,
SIGTERM, cancel or error; max RSS 178,601,984 B; 382 samples; group census empty; SETTLED; independent ps census empty;
no stop receipt; stdout/stderr empty. Outputs frozen 0444 (sha256):
- rqls_assay_v8.r7.sv2.launch.json: e8c6ce67ec548b3339f17b74d2acb3d3a21fc8e4aaae8d800561d1f7f4b947fb
- rqls_assay_v8.r7.sv2.result.jsonl: f6bdb6f403f1c7433de1bdc8db21411d5e40fea45455eb2a7c94c4f24b72a2dd
- rqls_assay_v8.r7.sv2.samples.jsonl: 08d8b338c957d7170755a78fc059381ccd86c2c4de3b0d803cad8b365f989ec3
- rqls_assay_v8.r7.sv2.stderr.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v8.r7.sv2.stdout.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v8.r7.sv2.supervisor-receipt.json: dddb7e66a081b4b99db3fb14dc73cb40d72db2df0845e8106ed67201d77b5601

Actual results (float, one implementation; numerical only):
- Gates, all PASS before R7: A, C1 (0/2 verified), C1p (0/2; polish residuals 2.10, 2.26), C2 (3/3 verified, 5 rays),
  A5 (reduced residual 3.97e-15, maxdev 1.32e-15, 10 rays), C3r (v3 seed 33 replay: maximal, 49 rays), C4r (seeds 41, 44:
  both maximal, 64 rays), KPc (4/4 verified, 10 rays), KRc (32 runs; verified seeds 7012, 7015, 7016, 7018, 7021, 7023 =
  exactly the v7 set).
- R7: 256 distinct configurations generated in 256 attempts (0 BAD_CONFIG, 0 duplicates); 2048 runs started and
  completed, 0 budget skips (child elapsed 768.84 s of 1800 s). LM status: 261 CONVERGED, 966 MAX_ITER, 821 STALL.
  Full-configuration verified endpoints: 261 (in 164 of the 256 configurations), every one with exactly 10 distinct
  rays; maximal candidates: 0. Unverified final residuals range about 0.86-1.0 (quantiles in the JSONL).
Scope: this is a scoped UNKNOWN for the forced Z_7+3 ansatz over these 256 random configurations and starts. It is not
evidence of nonexistence and carries no calibrated detection power for maximal configurations (the recovery rates of
known classical points do not transfer). The 261 verified 10-ray endpoints are non-maximal solutions.
