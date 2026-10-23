# Checkpoint 020 (rqls10 continuation, successor worker)

Recorded 2026-10-19T05:17:28-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process of this worker running (census 05:07:52: none in PGIDs 86952 / 91486, none with cwd in the lane); lane tmp/ empty.

## Events since 019
- 05:06 small stdlib probe fixedb_candidate_verify_v1 selftest (PID 91486, rc 0, 1.84 s; launch 7c6bae80...3efa sent to
  the parent first): exact rational Gram + ray margins; 60-digit refinement of 1e-9-perturbed anchors to 5.4e-61 (v = 7)
  and 5.7e-69 (v = 8) with 49 / 64 rays; random negative NOT_NEAR_SOLUTION. Result d7f0f633...96fc, receipt
  evidence/fixedb_candidate_verify_v1.selftest.receipt.md 3a1321cc...6db4.
- Parent: fixedb_jacobian_v1 and the selftest are SETTLED (hashes match; wrapper-only limitation recorded); terminal
  receipts + census were sent on request; verification boundary: decimal refinement (REFINED) is numerical CANDIDATE
  evidence only, never VERIFIED; a v = 10 hit stops immediately for independent exact/algebraic or certified-interval
  verification. D-9 concerns lane tmp/ (not /tmp) - already worded so in deviations v4 (10d7ca5f...53be).
- Design note evidence/fixedb-unitary-model-proposal-v1.md a0f3c3fd...02b2 frozen (05:10).
- Assay source lineage v1 (5a4e7956...895e) -> v2 (89772deb...dcba, payload slots for targets) -> v3
  (5bb69a05787ae1cc72c2a3628ac4ad67233e901d3c8793e0ef08bd6d7732d3d5, KP skip rule + slot split); diffs in review/; all
  frozen, NONE run. Configs v1/v2 superseded; Phase-1 config evidence/rqls_fixedb_lm_v3.p1.supervisor-config-v1.json
  04caa99c6fec145d4dc7355623ca10ef7f11815ca499f14d6ae30f958787d514.
- Admission request review/rqls10-fixedb-GO-request-v1.md 9a891f0dded332da7a137f654e2000a3c93abee50a2017f9e4cfe682101573b9
  sent to the parent (05:15). Navigation README-addendum-3.md written.

## Waiting on
Parent decision on the Phase-1 request (launch owner, budget). No probes and no numpy until then.

## Next (written work only)
Clock-orbit sub-case of B = Cay(Z_n) (q_ij = Z^j g_i): equivalent to a flat ONB {g_i} with {Z^i g_i} also an ONB, i.e.
a complex Hadamard H with H o F also Hadamard; Fourier-equivalent H reduce to complete mappings (none for n = 10).
Recorded as a possible later restricted item, not pursued numerically without a GO.
