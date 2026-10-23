# Receipt: rqls_w8_lm_v2 (W8 WH_p (x) C^2 orbit LM; parent GO 3d7ab8d4...10ad)

Recorded 2026-10-19T01:38:36-0700. GO institute/runs/six-lane-2026-10-18-96h/review/rqls10-w8-lm-parent-GO-v1.json sha256
3d7ab8d4c8d7233be6cdc3d79dc9262a420b3611f4e8dae984d2ed02294e10ad; tightening 8ac55669...aa20. Pins equal (source d336e2e3...,
config 84c93e51..., supervisor 1fece595..., gate 1f62874a...).
Launch: stability-gate.w8-lm.v2.json sha256 a2c1d9010deea8cd643b7c1922ea5cd4cadd8e851eb95b2ac954468e4d4cd71f PASS (30 samples, span 290 s,
age 3 s) && owned_supervisor_v2; supervisor PID 37255, child PID 37258 = PGID 37258, start 2026-10-19T01:37:38-0700; EXITED
rc 0, wall 38.3 s, no trips/SIGTERM/cancel/error, max RSS 39,583,744 B, group census empty, SETTLED; independent ps census
empty afterwards; stdout/stderr empty.
PROCESS DEVIATION (recorded, harmless): the tool layer delivered a second invocation of the same launch chain
(CHAIN_START 2026-10-19T01:37:42-0700) whose stability gate failed with FileExistsError on the exclusive gate receipt
(exit 1), so its supervisor never started; a ps census at 01:38:01 showed exactly one W8 supervisor (37255) and one
child (37258). The gate receipt belongs to the first (actual) launch at 01:37:38.
Outputs frozen 0444 (sha256):
- rqls_w8_lm_v2.sv2.launch.json: d6dc8a9d3dd01396f6af102c95f7260c519a004fa859669c86a5e63891e91820
- rqls_w8_lm_v2.sv2.result.jsonl: 0931945fc658fb27c9aba75bc2fbc2b4112896c4a86fad9b9d2317ddf5b54f83
- rqls_w8_lm_v2.sv2.samples.jsonl: 80d23f92041872977e82a2667d5cee93a126fe83b902329cd2a66657b0fed0d5
- rqls_w8_lm_v2.sv2.stderr.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_w8_lm_v2.sv2.stdout.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_w8_lm_v2.sv2.supervisor-receipt.json: bf0e2c5171a51f39a74b4e786299ecffc1bd45fcd59b99a9aa7d5b54a2df25ee

Actual results (float, one implementation; numerical only):
- P (relaxed positive, p = 5, rows + columns only): 32 runs, 30 verified (27 with 100 rays, 3 with 50 rays), 0
  reduced-zero/full mismatches -> gate PASS. The reduction and verifier agree on the relaxed problem.
- N (negative, p = 3, full): 128 runs, 0 verified, all STALL, min residual 0.296 -> gate PASS.
- W (target, p = 5, full): 512 runs, 0 verified, 510 STALL + 2 MAX_ITER, min residual 0.139 (min full maxdev 0.101),
  0 reduced-zero-not-verified (no model defect seen), 0 maximal candidates.
Scope: scoped UNKNOWN for the WH_5 (x) C^2 orbit ansatz. That LM never got below residual 0.139 while the relaxed
problem is solved in 30/32 starts suggests the ansatz may be infeasible [INFERENCE]; this is not a proof and gives no
detection power.
