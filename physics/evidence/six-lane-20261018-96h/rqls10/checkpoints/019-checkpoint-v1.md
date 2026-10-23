# Checkpoint 019 (rqls10 continuation, successor worker)

Recorded 2026-10-19T05:02:09-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process of this worker running; lane tmp/ empty.

## Events since 018
- Parent IRC 04:50 / ~04:55: both small probes (wh10_flat_system_v1, fixedb_anchors_v1) hash-verified and registered
  SETTLED with a late-registration note; launch-record path + sha must be sent to the parent AT launch even for small
  probes (done for fixedb_jacobian_v1); output-freeze delays go into deviations v4. Anchor reproduction accepted only as
  a control. Next deliverable: frozen design + preregistered admission request (calibrated budget, immediate stop
  rules, disk/RSS bounds, exact / high-precision verification of any 100-ray candidate) before any numpy work.
- Scout UnsymPathScout (read-only) report: the earlier unsymmetric path (rqls_assay_v3/v4/v8 `unsym`) is RRR over 100
  free unit vectors with Gram residuals on all 30 lines; its only v = 10 use was v3 stage T4 (Parker, Cay(D_5),
  Cay(Z_10) x 2 seeds x 20000 iterations): all MAX_ITER at error 0.47-0.50, never polished, no verified endpoint; v = 10
  sensitivity explicitly NOT qualified (missed known classical points). v4 sens1/sens2 configs were never launched.
- 04:53 small stdlib probe fixedb_jacobian_v1 (PID 86952, rc 0, 10.3 s; launch 218f628b...402d sent to parent first):
  analytic Jacobian of the fixed-B model matches central differences (<= 4.9e-13 rel.); tangent counts: Huang-Li v = 7
  anchor excess 0 (rank 246/252, kernel = gauge 6), Zhang-Cao v = 8 anchor first-order excess 6 (kernel 12, gauge 6),
  classical cyclic v = 7 point rigid. Result 598282a4...4bfa, receipt evidence/fixedb_jacobian_v1.receipt.md
  28c2789a54e5001763ad4094dbe0824a95f2629eb6b77d25ec0cad12d0fc1ca4.
- Draft assay source code/rqls_fixedb_lm_v1.py frozen 0444 at 05:02 (5a4e7956dabf1152356b90e1f72eea8394d0930608a35d6228d198ef25e0895e);
  NOT run (no GO). Stages S/N/C/KP/KR/S8 (calibration, gated) and W = Cay(Z_10), WD = Cay(D_5), WS seeded (targets);
  immediate exit 7 / 8 copied from rqls_wh10_lm_v2; MODE full | target.

## Next
1. Stdlib candidate verifier (exact rational Gram + ray margin of stored doubles; high-precision chord-Newton
   refinement + full Gram at >= 60 digits), tested on perturbed v = 7 / 8 anchors (small probe, launch record to parent).
2. Design note evidence/fixedb-unitary-model-proposal-v1.md (source screen, B choice / headroom, model, calibration
   ladder, budget, stop rules, verification ladder), supervisor config, admission request in review/.
3. Deviations v4 (late output freezes 04:31 / 04:40; tmp download moved to sources/).
