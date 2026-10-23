# Receipt: fixedb_candidate_verify_v1 selftest (initial-scope stdlib probe; Fraction + 60-digit decimal)

Recorded 2026-10-19T05:07:01-0700 (from /bin/date). Owner ContinueRQLS10b. Source code/fixedb_candidate_verify_v1.py
9b915c425e34b00533a0c8bf8b5e6c5a10497f94b18deaad0df30d488f256735 (0444 at 05:06:29, before launch); launch record
evidence/fixedb_candidate_verify_v1.selftest.launch.json 7c6bae801fe1d6c0b33eb715041260f62a0adf7a36982894b8c39998becb3efa
(path + sha sent to the parent before the run); input evidence/fixedb_anchors_v1.result.json
13d6ed64d8aafde833ce7981d7ed10044b2b06975d425a5778328ea610e22b92. Command (cwd lane, tool timeout 0): /bin/bash -c 'echo
START ... PID $$ ...; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B
code/fixedb_candidate_verify_v1.py selftest evidence/fixedb_anchors_v1.result.json
evidence/fixedb_candidate_verify_v1.selftest.result.json 60'. START 2026-10-19T05:06:53-0700, PID 91486 = PGID 91486,
EXIT 0, END 05:06:55 (in-run 1.84 s); single process; lane tmp/ empty. Output (3,286 bytes, born 05:06:55, 0444 at 05:07)
evidence/fixedb_candidate_verify_v1.selftest.result.json d7f0f6333525c6fd0dc03cd63c09c9a9de560566e595b3b7fa772e382a1996fc.
One implementation.

Results (all five gates true):
- Exact (Fraction) check of the double-precision anchors: Gram deviation < 1e-14 on all 3v lines; after a 1e-9 random
  perturbation of every U_k entry (unitarity broken) the exact deviation is in (1e-11, 1e-7) as designed.
- 60-digit refinement (Newton-Schulz polar + chord Gauss-Newton, double-precision Jacobian of the start point):
  v = 7 Huang-Li: max |F| 2.99e-9 -> 3.1e-18 -> 6.3e-27 -> 1.7e-35 -> 5.5e-44 -> 1.5e-52 -> 5.4e-61, REFINED; full
  Gram deviation 5.4e-61; 49 rays; min ray margin 0.7143 (= 5/7 to the shown digits).
  v = 8 Zhang-Cao: 3.7e-9 -> ... -> 5.7e-69 in 7 steps, REFINED; Gram 5.7e-69; 64 rays; min margin 0.5000 (the
  first-order excess 6 at this anchor did not slow the chord iteration).
- Negative control (random unitaries, cyclic B, v = 7): start residual 0.74 -> NOT_NEAR_SOLUTION (no refinement), exact
  Gram deviation > 1e-2.
Scope: validates the verifier on known points; a REFINED status is high-precision numerical evidence of a nearby exact
solution, not a proof (no interval / Kantorovich bound is computed).
