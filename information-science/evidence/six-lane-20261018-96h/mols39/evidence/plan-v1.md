# MOLS(39) lane — plan v1 and wave-1 GO request (2026-10-19T01:16:19-0700, ContinueCFR21)

Contract: NEW RUN/screening/info-2-mols39-contract-v1.json (e40e96ef…). Target: six MOLS of order 39; initial route a
7 x 39 difference matrix over cyclic Z_39 (sufficient, not necessary). Current table value N(39) >= 5. STOP registry:
evidence/stop-registry-v1.json (4f8e36bed87402180c5992f5c7e979fb1a0753a16ac0466f38f9feaebd0c7ccf). Deviations: evidence/deviations-v1.json (51e13c7c0cbdb7fdc15ed568c168fc99f1bd075d9aff88bb09c787aa302fcd80).

## 1. Facts measured so far (frozen stdlib probes; receipts under evidence/probes/)
* a1 (anchor DM_39_6_1, Sage/Handbook III.3.61): valid DM6; untwisted automorphism group exactly
  G6 = <(16,(012)(345)), (-1,id)> (order 6, exact and modulo constants); orbits 1+2+6x6; no row is a bijection
  (so the anchor plus a zero row is not a DM7).
* a2: the published (35,7;1) DM (Sym2026 Ex.3, transcribed from the pinned PDF text) is a valid DM7; its untwisted
  automorphism group is exactly <(1,(12)(34)(56))> (pure involution fixing the zero row) = the 2-SOLSSOM-type model.
  Sage DM_55_7_1 has group <(1, 6-cycle), (-1,id)> of order 12.
* Encoder controls (code/sym_dm_cnf_v1.py 0adb0376…): every known object satisfies every clause of its model and
  every intended mutation violates exactly the intended clause families: c1 (8 n=13 cases), c2 (8 n=35/39 cases; one
  degenerate mutation = deviation M39-D1), c3 (corrected anchor mutation), c4 (exact-reproduction models).

## 2. Representation (exact; frozen in the encoder docstring)
Group G of pairs (mu, pi) acting exactly on column vectors, optional normalised zero row, columns labelled by a
bijective row-pair difference; one-hot row variables, auxiliary difference variables, DM exactly-one constraints for all
21 pairs, generator transport clauses. A satisfying assignment <-> a G-invariant DM with the stated labelling/units.
Models (models/*.json, hashes in evidence/controls-v1/manifest.json and below):
| model | group | role |
|---|---|---|
| z13_g6, z13_g3, z13_z6p, z13_m1 | n=13 analogues | positive controls (linear DMs are instances) |
| z39_g6six (+ _fixrow0) | anchor G6 on 6 rows, exact vectors | behavioural positive control / exact reproduction |
| z35_m1_gauged (+ _fixh) | pure involution (12)(34)(56), gauge: fixed column = zero column | same-mechanism anchor (DM35) |
| z39_m1_gauged | same as DM35 model at n=39 | target (a solution also gives a 2-SOLSSOM(39)) |
| z39_z6p_gauged | <(16,pi), (1,(03)(14)(25))> | target (2-SOLSSOM-compatible, order-3 multiplier) |
| z39_g3 | <(16,pi)> | target |
| z39_g6 | <(16,pi), (-1,id)> | target (anchor group plus a fixed zero row) |
Gauges are justified in each model's notes (translation of row pairs/orbits by constants compatible with G).

## 3. Heuristic expected solution counts [HEURISTIC; random-assignment model conditioned on bijective rows and
automatic sum/nonzero relations; calibration: old-lane Z21 DM6 Z5-model predicted ~38, observed 96]
z35_m1_gauged ~5e1 (DM35 exists); z39_m1_gauged ~6e4; z39_g3 ~5e6 (ungauged); z39_z6p_gauged ~2.5e1;
z39_g6 ~5; z39_g6six (6 rows) ~3e15. These are NOT evidence of existence; they only order the models.

## 4. Wave-1 GO request (item mols39-w1; controls and calibration only, no Z39 seven-row target run)
Step A (stdlib, sequential): CNF generation with the frozen encoder, deterministic, outputs > 16 MiB:
  write z39_g6six, z39_g6six_fixrow0, z35_m1_gauged, z35_m1_gauged_fixh -> evidence/cnf-v1/<model>.cnf
  (each ~25-35 MB, total <= 150 MB; ~10 s each). n=13 CNFs already written (<=1.4 MB each).
Step B: code/make_jobs_v1.py (c6c7a7c9…) builds job JSONs from a pinned wave spec; each job run by
  code/run_native_v2.py (633f4a6e…): fail-closed pins, STOP-marker check, chunk-fit, free >= 12.2e9 + projection,
  long-job observer v3 stability rule, 10 s RSS/disk/STOP sampling, byte caps (stdout 16 MiB, stderr 1 MiB),
  owned SIGTERM to own pgid + 120 s bounded wait, never SIGKILL. Solvers: CaDiCaL 3.0.1 (601c9fa8…),
  Kissat 4.0.4 (05d6f3e9…), self time limits (-t / --time), -q, deterministic seeds.
  J1-J4 cadical seed 1, z13_{g6,g3,z6p,m1}, budget 60 s each (sequential)
  J5 cadical seed 1, z39_g6six, budget 1800 s            (anchor-model behavioural control)
  J6 cadical seed 1, z39_g6six_fixrow0, budget 600 s     (anchor exact reproduction)
  J7 cadical seed 1, z35_m1_gauged_fixh, budget 600 s    (DM35 exact reproduction)
  J8 cadical seed 1 and J9 kissat seed 1, z35_m1_gauged, budget 3540 s each, in parallel, long_job=true
     (same-mechanism calibration: can the method find a (35,7;1) DM from scratch?)
  At most 2 solver processes; RSS cap 1.8 GiB each (lane total <= 4 GiB); projected retained disk <= 300 MB.
Step C: every SAT output -> code/verify_solution_v1.py (1723e8f6…): decode, full clause evaluation, checker A
  (cfr21 code/check_dm_mols_cfr_v1.py, accepted controls). Acceptance: J1-J7 SAT and VALID; for J6/J7 report
  whether the decoded column set equals the anchor/DM35. J8/J9 SAT = calibration success; UNKNOWN = inconclusive.
Stop rules: any control UNSAT/INVALID -> STOP marker, engine defect report; any unexpected resource trigger -> STOP.
Scientific consequence of wave 1: none for the target (controls only); it decides whether wave 2 (Z39 targets:
  z39_m1_gauged, z39_z6p_gauged, z39_g3, z39_g6; CaDiCaL/Kissat seeds; 3 h chunks; stop all on first SAT) is
  worth requesting.
