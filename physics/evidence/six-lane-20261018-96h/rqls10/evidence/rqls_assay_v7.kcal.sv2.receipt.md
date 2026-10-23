# Receipt: rqls_assay_v7 K-only calibration (parent GO 01d5132c...428a)

Recorded 2026-10-19T01:13:08-0700. GO institute/runs/six-lane-2026-10-18-96h/review/rqls10-v7-kcal-parent-GO-v1.json sha256
01d5132cc3c5bc35117940d7d2a90f67123c4b9ea1e237847727dc274a59428a. Calibration only; no target search.

Chain (cwd lane, tool timeout 0, TMPDIR lane/tmp): stability_gate_v2 (projected 20,971,520 B) && owned_supervisor_v2 +
evidence/rqls_assay_v7.kcal.supervisor-config-v2.json (3057885c...); child code/rqls_assay_v7.py fed4be6a....
Gate receipt evidence/stability-gate.v7-kcal.v2.json sha256 b31bc0a2d4ae1b6e18246ed79190e4e1f5417fdd517c9ce73a3b885ec4eadb38: PASS
(30 samples, span 290 s, last age 10 s, max drop 131,813,376 <= 15,006,544,405).
Supervisor PID 28934; child PID 28936 = PGID 28936; start 2026-10-19T01:11:13-0700 (epoch 1792397473.34); wall 90.57 s;
EXITED, rc 0, no trips/SIGTERM/cancel/error, max RSS 86,360,064 B, 45 samples, group census empty, SETTLED;
independent ps census empty; no stop receipt. Outputs frozen 0444 (sha256):
- rqls_assay_v7.kcal.sv2.launch.json: 46fc26f8162e250e72e6c8c37aca6d60b975d116f2b70e419ea2415b7269a5ef
- rqls_assay_v7.kcal.sv2.result.jsonl: 22b7e4fcc94dd96cf8b46c52a56c49aa641d72d7eea9d9e9413b222ca71fa7f7
- rqls_assay_v7.kcal.sv2.samples.jsonl: 3271e0fdadce1050ca684965fc137b855da17e3700f065d851c17b7afd5fddd3
- rqls_assay_v7.kcal.sv2.stderr.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v7.kcal.sv2.stdout.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v7.kcal.sv2.supervisor-receipt.json: 7ffedfefad2da423ed3098b54cf3a0208bec36ccd6c54d0d0e46b06eeac75327

Results (float; one implementation / one exact-arithmetic-free float program; numerical only):
- Gates A (7/7), C1, C1p, C2, A5 PASS. Anchors: reduced residual at the four classical instances 4.0e-15..5.1e-15.
- KP (classical anchor + amp * N(0,1) on all 161 parameters, 4 instances x 4 seeds, LM <= 200 iterations):
  amp 1e-3: 16/16 recovered; 1e-2: 16/16; 0.1: 16/16 (start residual ~1.6); 0.5: 13/16 (start residual ~15-16);
  every recovered point verifies on the full 100-cell configuration with 10 rays (classical).
- KR (256 random starts, first 8 = v5 K instances): 48/256 verified (18.8%), all classical (10 rays);
  115 MAX_ITER, 93 STALL; min residual 2.0e-15.
Interpretation: the Reduced parametrisation, its Jacobian and the LM are sound near the anchor (no debugging needed),
and random-start recovery of known forced-form Z_7+3 solutions is ~19% per start on these instances, i.e. sensitivity
for this ansatz is now qualified (numerically). The v5 smoke's 0/8 was a small-sample miss. All solutions found are
classical, consistent with the local-rigidity result. This does not bear on maximal solutions; target runs (R7/R9)
still require a new parent GO.
