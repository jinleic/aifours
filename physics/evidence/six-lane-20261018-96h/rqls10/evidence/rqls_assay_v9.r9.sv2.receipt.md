# Receipt: rqls_assay_v9 MODE r9 (forced Z_9+1 with in-run anchor; parent GO c406e6b1...06d0)

Recorded 2026-10-19T03:01:41-0700 (from /bin/date). Launch owner ContinueRQLS10b (named in the GO; the parent did not
launch). GO RUN/review/rqls10-v9-r9-parent-GO-v1.json sha256 c406e6b1125fa870ba2eceae352c0707490aafe88d5c87c2df1a51c93f8206d0;
tightening 8ac55669...aa20. Pins re-hashed equal before launch: source e9079686...64db, config a0f04bc0...c3e7,
supervisor 1fece595...15aa, gate 1f62874a...008a, observer fe311f28...4196.

Chain (cwd lane, ONE invocation, tool timeout 0, TMPDIR lane/tmp): CHAIN_START 2026-10-19T02:48:26-0700;
code/stability_gate_v2.py (monitor RUN/control/resource-observer-live-v3.jsonl, projected 20,971,520 B) -> receipt
evidence/stability-gate.v9-r9.v2.json sha256 ac37a6ef3f809afc0bd2d719ab3bbb6c169bb41c4a2b2330af8936cf34bb212a PASS (30 samples,
span 290 s, last age 5 s, max drop 493,916,160 <= 14,899,478,037, fresh free 192,282,927,104) && code/owned_supervisor_v2.py
evidence/rqls_assay_v9.r9.supervisor-config-v2.json. Supervisor PID 55967; child PID 55969 = PGID 55969; start
2026-10-19T02:48:26-0700 (epoch 1792403306.76), abs end epoch 1792405206.76; EXITED rc 0 at 03:00:56 (wall 749.25 s); no
trips, SIGTERM, cancel or error; max RSS 168,656,896 B; min free 192,156,008,448 B; 372 samples; group census empty;
SETTLED. No stop receipt. Independent ps census at 03:01:03 empty; lane tmp/ empty; stdout/stderr empty; CHAIN_EXIT 0.
Outputs (frozen 0444, sha256):
- rqls_assay_v9.r9.sv2.launch.json e7fa113658fd6a54a2cc88fd9b10290c8f72512d4670a829a733ed9070e6465f
- rqls_assay_v9.r9.sv2.result.jsonl 2bbc0defba49a9bd65a1757a4eb45b856f1f025d9d250c6f3e49cc0771d9c154 (670,123 B, 1,808 records)
- rqls_assay_v9.r9.sv2.samples.jsonl bb8c7db1bee5aa4f44a3c283cd93c59da2a162c28764b13ca1242b89f8662d6b
- rqls_assay_v9.r9.sv2.supervisor-receipt.json 9091f64692393c0d546d291bbd7bb2b4c736e95a3fd2ba05ad01b71309388d1c
- rqls_assay_v9.r9.sv2.stdout.txt / .stderr.txt e3b0c442...b855 (empty)
Read-only analysis (frozen before the output existed, self-tested on the v8 JSONL): code/rqls_assay_v9_r9_analysis_v1.py
76fb109d9d9583701366d7f387ecf97e5ad534c2d8f7a6c308fd0bfa5e8e3aca -> evidence/rqls_assay_v9.r9.analysis-v1.json
6ae901e3cd6d505c30c0e4ba0ee7b2dce989680d8dccc67516a0c39286221ce2 (03:01:16, PID 60353, EXIT 0).

Actual results (float, one implementation; numerical only):
- ALL 13 gates PASS before the target: A, C1, C1p, C2, A5 (3.97e-15), C3r (49 rays), C4r (64, 64), KPc (4/4), KRc
  (verified seeds 7012, 7015, 7016, 7018, 7021, 7023 = v7/v8 set); A9 (40/40: exact orthogonal pairs, reduced residual
  <= 1.38e-14, maxdev <= 1.84e-15, 10 rays); A9m (mutant residual 1.732, maxdev 1.0); K9P (amp 1e-3 16/16, 1e-2 16/16,
  0.1 16/16, 0.5 6/16; all verified with 10 rays; 0 converged-not-verified); K9R (128 runs, 2 verified, seeds 95062 and
  95110, 10 rays; 0 converged-not-verified).
- R9 target: 24/24 classes (exact enumeration: 2,025 squares) x 64 starts = 1,536 runs, 0 skips, 0 BAD_CONFIG;
  LM status CONVERGED 10, MAX_ITER 885, STALL 641; full-configuration verified endpoints 10, ALL with 10 rays
  (classical), all 10 in classes that contain a known classical resolution (12 such classes; 0 in the other 12);
  maximal candidates 0. Unverified endpoint residuals: min 0.684, 1% 0.743, 10% 0.816, median 0.887, max 1.065.
- Model-defect screen (parent consumer rule, regardless of LM status): 0 endpoints with reduced residual < 1e-8 and
  full maxdev >= 1e-8; 0 with residual < 1e-10 and maxdev >= 1e-6; max maxdev/residual over all endpoints with
  residual < 1e-6 is 0.70. In-code converged-not-verified count 0 in K9P, K9R and R9.
- The only maximal configurations in the JSONL are the calibration replays C3r (v = 7, 49 rays) and C4r (v = 8, 64 rays).
Scope: scoped UNKNOWN for the forced Z_9+1 ansatz (D_inf = {0}, m* = 0) over these 24 resolution classes x 64 starts;
not nonexistence, no calibrated detection power for maximal basins (random recovery of KNOWN classical points was only
2/128 = 1.6% per start in K9R, much lower than the 19% of Z_7+3); the exact 24-class enumeration is an enumeration of
configurations (B data), not coverage of the continuous quantum solution space.
