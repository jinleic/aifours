# Preregistered admission request: rqls_fixedb_lm_v3 Phase 1 (fixed-B unitary model, no orbit symmetry) - NOT run

Recorded 2026-10-19T05:10:54-0700, pins revised to v3 and frozen 2026-10-19T05:14:34-0700 (from /bin/date). Requester ContinueRQLS10b. No numpy/native computation has been
executed for this item (no smoke). Launch owner: to be named by the parent (this worker launches only if named in the
GO). This request covers ONE calibration-plus-pilot run (Phase 1). Any target run with a larger budget (Phase 2) needs a
separate GO computed from Phase 1 timings (section 5).

## 1. Written basis (lane-internal, unreviewed, not parent-accepted)
- Design note evidence/fixedb-unitary-model-proposal-v1.md a0f3c3fd191a2ac5670f477e5a18b99c741cc76b337896c1bbbd8cbfbd4302b2
  (model, relation to the earlier `unsym` RRR path, source screen for Hall-Paige / quantum complete-mapping no-gos for
  Cay(Z_10): none found; B choice Cay(Z_10) primary, Cay(D_5) secondary; headroom; stop rules; verification ladder).
- Settled small probes (parent registry: SETTLED): evidence/fixedb_anchors_v1.receipt.md
  dee13731c6e548854b4222b385bb8d2c1426986344b4d25019de7347f8327d4e (exact v = 7 Huang-Li and v = 8 Zhang-Cao anchors in
  U-form); evidence/fixedb_jacobian_v1.receipt.md 28c2789a54e5001763ad4094dbe0824a95f2629eb6b77d25ec0cad12d0fc1ca4
  (analytic Jacobian = central differences to <= 4.9e-13; anchor tangent counts); evidence/fixedb_candidate_verify_v1.selftest.receipt.md
  3a1321cc5273ff5a12719ea1751c057a3fb92c36a0ae0317a0d99f2468fb6db4 (candidate verifier on perturbed anchors).

## 2. Pins (sha256)
- source code/rqls_fixedb_lm_v3.py 5bb69a05787ae1cc72c2a3628ac4ad67233e901d3c8793e0ef08bd6d7732d3d5 (0444). Lineage (all
  frozen, never run, superseded before submission): v1 5a4e7956dabf1152356b90e1f72eea8394d0930608a35d6228d198ef25e0895e
  (cited by the design note section 5) -> v2 89772debc90894e89bae084583311334c490662dab009f364e2ab6bb1cfadcba (diff
  review/rqls_fixedb_lm_v1_to_v2.diff 08dbc5e34a37ced5a3ab92ac6048b5adb0fde466bf1806fde87900e24876cf38: the 32
  U-payload slots for float-verified v = 10 endpoints are reserved for the target stages W/WD/WS) -> v3 (diff
  review/rqls_fixedb_lm_v2_to_v3.diff 328990850e9b20f03c7a15f43180fdd9a1aadb3f442c1b6d5f1ea38400c88686: in KP only a
  time-skipped run with amp <= 1e-2 fails the gate, skipped 0.1 / 0.3 runs are recorded only; KP slot split
  20 / 30 / 50 % over the v = 7, 8, 10 anchors) + version strings. Protocol, exception classes, exit codes, stop
  receipt, W() cap and LM damping schedule are copied from the parent's code/rqls_wh10_lm_v2.py
  48b186e0a63bdad584ddcc36c198bab67ef9abd813cd55ed744427442e79f38e.
- config evidence/rqls_fixedb_lm_v3.p1.supervisor-config-v1.json 04caa99c6fec145d4dc7355623ca10ef7f11815ca499f14d6ae30f958787d514
  (pins the source and both inputs; the supervisor refuses to launch on any mismatch). The configs
  evidence/rqls_fixedb_lm_v1.p1.supervisor-config-v1.json (69a5cc1f...16e7) and
  evidence/rqls_fixedb_lm_v2.p1.supervisor-config-v1.json (cb78de54...2a62) are superseded and must not be launched.
- inputs evidence/fixedb_anchors_v1.result.json 13d6ed64d8aafde833ce7981d7ed10044b2b06975d425a5778328ea610e22b92;
  evidence/parker_z7p3_classical_v1.result.json 00e991d692e669411a49d45aa1623c52189346dc32acb6fb1feea1858b841c30 (pair 0)
- supervisor code/owned_supervisor_v2.py 1fece595258d7ba448875c407e8b221bdbd01966824dc267147c316ef54115aa; gate
  code/stability_gate_v2.py 1f62874aff9b22657a90f180b81c678117fd703afe2345f7576454e0faae008a (observer
  RUN/control/resource_observer_v3.py fe311f28d122310da004d0968272ae294a99757756b4898f0d9db4cb13f04196)
- tightening 8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20; stop registry review/stop-registry-v2.json
  a47bb3ffbff22c0f15b1d7fba186812c27ac925ec77a73c76b1d7eb3f639acb7 (no relevant stop)
- candidate verifier (post-stop only) code/fixedb_candidate_verify_v1.py 9b915c425e34b00533a0c8bf8b5e6c5a10497f94b18deaad0df30d488f256735

## 3. Run (argv in the config): MODE full, BUDGET 2400 s, NN 64, NC 64, NKR 64, NKR10 32, N8 128, NW 64, NWD 32, NS 32
Model: q_ij = U_i e_j, U_0 = I; residual = M[p,p], M[p,pi(p)] of M = U_i^* U_i' (2 v^2 (v-1) reals); zero-diagonal
skew-Hermitian charts; analytic Jacobian; LM <= 300 iterations per start (damping as rqls_wh10_lm_v2). EVERY endpoint:
full float Gram of all v rows, v columns, v B-classes; float-verified = deviation < 1e-8; rays merged at
1 - |<q,q'>|^2 < 1e-7, minsep recorded.
Gates, all before any target start (GATE_FAIL_STOP receipt, exit 3, on failure):
 S   pins; Jacobian vs central differences at Haar-random U (cyclic 4, 5, 7, 10; XOR 8; Cay(D_5)) < 1e-9; block normal
     equations vs dense (v = 5, 7) < 1e-12; retraction unitarity < 1e-12; float anchors (Huang-Li v = 7: 49 rays;
     Zhang-Cao v = 8: 64 rays; classical Parker v = 10: 10 rays) residual and full Gram < 1e-12, U_0 = I, mutation >= 0.01.
 N   Cay(Z_4), Cay(Z_6) x 64 random starts: >= 1 run, 0 float-verified, 0 defects (imports: Zhang-Cao Sec. 3 citing
     Ball-Simoens - every 1-RQLS(4) classical and Cay(Z_4) has no transversal; no 1-RQLS(6)).
 C   Cay(Z_5) x 64: >= 1 run, 0 defects, every float-verified endpoint has exactly 5 rays (import: 1-RQLS(5) classical).
 KP  near-anchor recovery at the three anchors, amp 1e-3, 1e-2, 0.1, 0.3 x 4 seeds (slot 300 s split 20 / 30 / 50 %):
     all 8 runs with amp <= 1e-2 per anchor run (none time-skipped) and float-verified, with 49 rays (v = 7) and 64 rays
     (v = 8); v = 10 rays recorded; 0 defects.
 KR  random starts on cyclic v = 7 and XOR v = 8 (64 each) and the Parker v = 10 B (32): >= 1 run each, 0 defects; counts
     and ray histograms recorded, NOT detection power for v = 10 targets.
Recorded without gate: S8 = Cay(Z_8) x 128 (first even order where a cyclic-B solution is open to the requester).
Targets (pilot size in Phase 1): W = Cay(Z_10), B(i,j) = (j - i) mod 10, x 64; WD = Cay(D_5) x 32; WS = up to 32 starts
seeded at float-verified non-maximal W/WD endpoints (+ expm(0.05 g)). Unstarted runs are written as SKIPPED_TIME.
Stage clocks: S 60, N 120, C 60, KP 300, KR 900 (cyclic7 15 %, XOR8 25 %, Parker10 60 %), S8 420; remainder
R = 2400 - 1980 = 420 s split W 252, WD 126, WS 42; 120 s reserve. Supervisor max_wall 2700 s, settle 120 s, sample 2 s.

## 4. Stop rules (immediate; flush before exit)
- 7 CANDIDATE_UNVERIFIED_STOP: any v = 10 endpoint (any stage, including KP/KR on the Parker B) float-verified with 100
  rays and minsep > 1e-6; U (full precision), B, seed written in the JSONL record first.
- 8 MODEL_DEFECT_STOP: LM residual < 1e-10 with full deviation >= 1e-8 (any stage); U written.
- 3 gate failure; 4 JSONL cap 8 MiB; 5 SIGTERM (flag honoured between runs); 6 no "GO" line; 2 exception (traceback
  recorded). A separate exclusive stop receipt is written on every non-zero exit after GO.
- After exit 7: nothing is claimed. Requester freezes the record and notifies the parent at once; (i) exact rational
  Gram + all pairwise ray margins of the stored doubles (verifier `candidate` mode; stdlib, initial scope), (ii) 60-digit
  refinement + full Gram (same script; at v = 10 the pure-Python Cholesky may exceed 300 s -> only under a parent GO),
  (iii) independent exact/algebraic or certified-interval verification by three independent checkers chosen by the
  parent. Status REFINED from (ii) is numerical CANDIDATE evidence, never labelled VERIFIED.

## 5. Resources and calibrated budget
- One child process (single-threaded BLAS via env), RSS expected < 300 MB (largest arrays at v = 10: 810 x 810 normal
  matrix, 45 x 180 x 180 pair blocks; trip 2 GiB); JSONL expected < 2 MB (U payload capped at 32 v = 10 and 8 S8
  endpoints), hard cap 8 MiB in code, output trip 9 MiB; projected reservation 20 MiB; free-disk trip 12.2 GB, launch
  minimum 12,220,971,520 B; settle-by epoch 1792731393 (2026-10-22T21:56:33-0700) respected by the supervisor fit check.
- Launch (only by the GO-named owner): fresh code/stability_gate_v2.py (projected 20,971,520 B) &&
  code/owned_supervisor_v2.py evidence/rqls_fixedb_lm_v3.p1.supervisor-config-v1.json, tool timeout 0; launch-record
  path + sha sent to the parent at launch; terminal receipt + census sent on return.
- Phase 2 (NOT requested here): MODE target (gates S and KP rerun, then W/WD/WS). Budget B2 chosen by the parent; counts
  derived from Phase 1: NW = floor(0.6 (B2 - 480) / mean_s(W)), NWD = floor(0.3 (B2 - 480) / mean_s(WD)), NS = floor(0.1
  (B2 - 480) / mean_s(W)), using the Phase 1 per-run means recorded in the W / WD summaries.

## 6. Known limits of this request
- The numpy source has never been executed; implementation errors are caught by gate S (Jacobian, normal-equation
  assembly, anchors) before any target start, at a cost of <= 60 s.
- Stage timings are estimates; the stage clocks bound wall time, so low throughput shows up as SKIPPED_TIME, not overrun.
- Claims: target misses are a scoped UNKNOWN for this model and these B's (never nonexistence); recovery rates are not
  detection power; S8 is an observation; no novelty/priority claims; one implementation.
