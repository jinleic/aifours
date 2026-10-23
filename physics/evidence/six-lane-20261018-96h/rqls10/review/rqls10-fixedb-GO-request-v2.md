# Admission request v2: rqls_fixedb_lm_v4 - bounded behaviour qualification Q1, then Phase 1 - NOT run

Recorded 2026-10-19T05:25:33-0700 (from /bin/date). Requester ContinueRQLS10b. Supersedes review/rqls10-fixedb-GO-request-v1.md
(9a891f0dded332da7a137f654e2000a3c93abee50a2017f9e4cfe682101573b9), which pinned v3; the parent put v3 on HOLD (lm() ignored
SIGTERM, the stage end and BUDGET for up to 300 iterations x 12 damping retries, so an in-progress run could overrun its
stage and the supervisor's 120 s settle window). No numpy/native computation has been executed for any version. Launch
owner: to be named by the parent. Everything in request v1 not changed below still applies (written basis, model,
gates, stop rules 7/8/3/4/6/2, candidate path, claims).

## 1. Pins (sha256)
- source code/rqls_fixedb_lm_v4.py 816884478ae6eb163c328db9c6f3984d7a447260ddbda0e4887d4f5a7310470e (0444, 727 lines); diff
  review/rqls_fixedb_lm_v3_to_v4.diff 504f5e852118fe4297bbdc2477e176e8f9409fc6d8c52e68a0b8cfd649d7dd32 against v3
  5bb69a05787ae1cc72c2a3628ac4ad67233e901d3c8793e0ef08bd6d7732d3d5 (earlier lineage and diffs as in request v1). No model,
  schedule or dependency change.
- Q1 config evidence/rqls_fixedb_lm_v4.q1.supervisor-config-v2.json 7cb4a51c1444e9208be0e9134fb5b7e270f152c03c2a5f2d24e61d93ad0fd382
  (supersedes q1 config-v1 3af8de20...6777, never launched: NW / NWD raised from 64 / 32 to 1000 / 1000 so that the W
  and WD stages are time-limited and scenario (a) cannot be skipped by reaching the run cap early)
- Phase 1 config evidence/rqls_fixedb_lm_v4.p1.supervisor-config-v1.json 0198d79743f87174d80a9ef8edf4f21e6d4d6d9c965b415b29e1249c9cc0ff46
  (same argv as v3 Phase 1: MODE full, BUDGET 2400, NN 64, NC 64, NKR 64, NKR10 32, N8 128, NW 64, NWD 32, NS 32;
  max_wall 2700 s). Configs for v1, v2 and v3 are superseded and must not be launched.
- Both configs pin the source and the inputs evidence/fixedb_anchors_v1.result.json 13d6ed64...2b95 and
  evidence/parker_z7p3_classical_v1.result.json 00e991d6...1c30; supervisor, gate, observer, tightening and stop registry
  as in request v1.

## 2. The v4 fix (minimal; old files untouched)
- lm(Pr, U, end) uses dl = min(stage end, T0 + BUDGET) and checks the SIGTERM flag and dl before each outer iteration,
  after the normal-equation assembly, before each damping retry and after each linear solve. On a hit it returns
  status TERMINATED or DEADLINE with the last ACCEPTED iterate (finite) and its residual - never CONVERGED. A run that
  converged before the check keeps CONVERGED.
- run_one(..., end) receives the stage end from random_stage, near_stage (per-anchor sub-slot) and the WS loop; it still
  evaluates the endpoint (full float Gram of all 3v lines, rays) and writes the record; candidate (exit 7) and model
  defect (exit 8) keep priority; then, if the run was TERMINATED or the flag is set, TermStop -> stop receipt
  TERMINATED_UNKNOWN, exit 5. over() raises TermStop at every run boundary once the flag is set, and gate() raises it
  instead of evaluating a gate, so no new run starts and no gate is evaluated after a SIGTERM.
- Wall-time claim, corrected: stage clocks bound the START of runs; an in-progress LM run stops at the next check after
  its stage end, BUDGET or SIGTERM, i.e. after at most one normal-equation assembly or one solve + retraction + residual
  (not measured; estimated well below 1 s at v = 10), plus the endpoint evaluation (full Gram + ray count). The S-stage
  self-tests contain no LM run (expected seconds).

## 3. Q1: bounded behaviour qualification (requested first)
argv: MODE target, BUDGET 900 s (NN, NC, NKR, NKR10, N8 = 1 are unused in target mode), NW 1000, NWD 1000, NS 8; supervisor
max_wall 700 s, settle 120 s. Plan: S 0-60 s, KP 60-360 s (gated; v = 7, 8, 10 anchors), W 360-612 s, WD 612-738 s,
WS 738-780 s, reserve 120 s. Scenarios exercised: (a) child-side DEADLINE inside a v = 10 LM run at the W stage end
(~612 s); (b) supervisor DEADLINE trip at ~700 s -> SIGTERM to the process group during a WD LM run.
Proposed pass criteria (parent to confirm): pins OK and GO sent; gates S_input_pins, S_jacobian, S_anchors and
KP_near_anchor PASS (if a gate fails, Q1 ends with exit 3 and is inconclusive for (a)/(b)); the W summary shows one run
with st = DEADLINE and the W summary is written within 2 s after the planned W end; after the SIGTERM the child writes
at most the interrupted run's record (st = TERMINATED, finite md) and exits 5 with stop receipt TERMINATED_UNKNOWN within
5 s of the supervisor's signal (supervisor status EXITED_AFTER_SIGTERM); empty-child census afterwards; 0 model
defects. A 100-ray v = 10 candidate during Q1 still stops with exit 7 (candidate path of request v1 section 4).
Resources: one child, RSS expected < 300 MB, JSONL < 1 MB, output trip 9 MiB, projected 20 MiB.

## 4. Phase 1 (after Q1 is accepted; separate GO)
Unchanged from request v1 section 3 except the source/config pins above and the corrected wall-time statement.
Phase 2 (target mode, larger budget) remains a later, separately sized request.
