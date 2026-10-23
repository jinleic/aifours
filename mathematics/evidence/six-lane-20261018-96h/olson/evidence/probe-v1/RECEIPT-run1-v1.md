# s1full_profile_probe_v1 run1: post-run receipt (aid only; never a premise)

Written after /bin/date 2026-10-19T00:03:02-0700.  Owner ContinueOlson.
- Source code/s1full_profile_probe_v1.py sha256 7d87a31072cfa3b23c3782a71a3801c2c810cdde4f2e146c0cc665135ece4742 (frozen
  23:56:33, before execution).  Pre-launch record evidence/probe-v1/LAUNCH-RECORD-pre-v1.json
  117b5a787e329fcd37cb95e4ca6d86979859832ea5d72104666a8aa070905e7a.
- Launch: START 2026-10-18T23:57:30-0700, END 2026-10-19T00:02:08-0700 (shell /bin/date reads), EXIT 0, tool wall
  278.05 s, self budget 270 s (checked between work units; last unit ended at 277.858 s by its own clock).
  Identity: the launch line's $! echo printed empty (whole AND-list was backgrounded as one job: a recording defect, not a
  science issue); one ps census at about 23:58:41 showed PID 16900, PPID 61118, PGID 16900, argv
  'Python -B code/s1full_profile_probe_v1.py evidence/probe-v1/run1.jsonl' (Homebrew Python 3.14.3).  The process was
  observed only through its exit and outputs afterwards; no signal was sent.
- Env: TMPDIR=lane tmp/, PYTHONDONTWRITEBYTECODE=1, single-thread BLAS vars.  Fresh free 191,686,348 KiB at start.
- Outputs: evidence/probe-v1/run1.jsonl sha256 901a8000772bf6f0b2beec7521e9163ef1687d5e6d1f97622156287081abd253
  (118 lines, 19,277 B); run1.stdout.txt empty (e3b0c442...b855).

## Results (exact DP per candidate, inside the RESTRICTED representation only)

- POS controls (outside P1; p = 13, 19, 31 with delta' = (p+2)/3, D' = (2p-2)/3): each has exactly 2 survivors: the
  parent-checked family g^(p+3)(3g)^(p-1) (S_Q = 3^((p-1)/3), t' = 2) and g^(2p-1)(cg)^3 with c = (2p+1)/3 (S_Q = [c],
  t' = c-1).  Detection works; the second family is a further (ZP)-without-(S1) example at kappa = (2p+1)/3 (aid only).
- NEG controls (accepted S1(g) range: (13,3), (19,5), (29,7), (31,7), every even D in [delta+1, 2delta-2]): 0 survivors.
- NEW (P1 holds, S1(g) does not): COMPLETE with 0 survivors for every even D in [delta+1, 2delta-2] at
  (p, delta) = (31,9), (37,9), (37,11), (41,11), (43,11), (43,13), (47,11), (47,13), (53,13), (53,15), (59,13), (59,15),
  (59,17), (61,13), (61,15); (61,17) D <= 28 complete, D = 30 BUDGET_STOP (UNKNOWN), D = 32 NOT_STARTED; (61,19)
  NOT_STARTED (all D).  First uncovered terminal kappa = 20 at p = 31 is in the complete set.
- Restriction (binding scope of every NEW statement above): candidates are only those T = (g^m S_Q) u (g^t' Y) with Q a
  length-(p+delta) index-1 proper zero-sum, t' < min S_Q, Y odd in [3, D+1], sum(Q') = 2p, D even in [delta+1, 2delta-2].
  These restrictions are consequences of the unreviewed written reductions R0, MC, NO-BIG, I=1, t' < min S_Q (lane
  derivation, 2026-10-19 00:0x) plus accepted S1(g) steps 1-3; if any reduction is wrong, configurations outside the
  representation were NOT tested.  No statement about p outside the list.  Not a proof of S1-full.
