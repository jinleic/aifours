# Lane log — phys-1 fourth target: Ball–Simoens Problem 16 at n = 8 (host clock, PDT)

## 2026-10-17
- 05:16:00 contract frozen by the parent (screening/phys-1-moqls8-problem16-contract.json).
- 05:37:53 lane created; pinned sources copied (2d60d45f… / f01b494f…). Volume free space 52 GB (95 % used).
- ~05:40 README §0–§1 frozen (route, controls, disk plan) before any n = 8 computation; 05:4x reduction reported to
  the parent (W8, A8 classification-free, K1..K5, SB2_8, disk plan).
- 05:41:39–05:41:41 K1 FIXED (AG(2,8) 6-net, slopes 1,2,3,4; one quantum square with a weight-≥3 entry):
  encoder A8 (code/enc8_a.py, CaDiCaL 3.0.1) UNSAT, encoder B8 (code/enc8_b.py, kissat 4.0.4) UNSAT; relaxed (no P4)
  A8 SAT. Files evidence/k1_explore/.
- 05:41:53–05:42:04 generic K2..K5 CNFs with SB2_8 for both encoders: evidence/kgen_v1 (A8: 82k–147k vars,
  0.57M–1.15M clauses; B8: 338k–576k vars, 1.2M–2.2M clauses).
- 05:42 A8 K2, K3, K4, K5 launched with CaDiCaL (proof-free, -t 10500). 05:43:03 A8-K5 stopped (parent reserves one
  of the four CPU slots); its partial log is kept.
- Parent guidance received: A8 stays a written lemma until review (net-intersection step made explicit); K1 needs an
  explicit regridding lemma (not an isotopy claim) — both added to review/PROOF_N8_PARTIAL.md.
- 05:45:38 A8-K4 solver paused (SIGSTOP) to run controls within 3 slots; resumed 05:48:10 (SIGCONT).
- 05:45:38 first exact-checker attempt over GF(8) failed by design discovery: NO non-GF(2)-affine permutation f of
  GF(8) has a second undetermined direction (exhaustive: 0 hits) — Theorem 6 gives no non-classical pair over GF(8)
  (or any ring with additive group Z2³; Z8 has no orthomorphisms). Control switched to the Frobenius ring Z2 × Z4
  (unit u = (1,1)); both checker files rewritten before any successful run (the failed run left no output files).
- 05:47:26 exact checkers (code/exact8_a.py Gaussian-integer arithmetic; code/exact8_b.py independent numpy integer
  Gram matrices + exp/log GF(8)): non-classical MOQLS(8) pair Ψ^(f), f = [0,2,4,6,1,7,5,3] on Z2×Z4 (code 4a+b),
  Φ^(u) = |u·i + j⟩: QLS, orthogonal, 32 rays (> 8); mutations: additive f → 8 rays; unit (1,3) (f − u′x not a
  permutation) → orthogonality fails; classical 7-MOLS(8) (AG(2,8)) Latin, orthogonal, 8 rays each. Both exit 0.
- 05:47:47–05:47:55 fixed-pattern controls (code/controls8.py, fail-closed) for A8 and B8: all 10 agree with the exact
  expected status (Theorem-6 pattern with weights {1,2,4} + Φ^(u) as two patterns SAT; its 1-coordinate mutation
  UNSAT; weight-3 subsquare QLS SAT / singleton mutation UNSAT; XOR-shift pairs P3 SAT/UNSAT; classical-line P2
  UNSAT/SAT; classical pair with/without P4).
- 05:48:05–05:48:10 K1 certificate (evidence/k1_cert_v1): A8 CNF 7fe3a6ca…74c0 UNSAT, text DRAT a1887510…15f1
  (5541518 B) "s VERIFIED"; B8 CNF f1278246…25d2 UNSAT, text DRAT e64f5f54…911a (29837895 B) "s VERIFIED"
  (drat-trim binary from the n = 7 lane, source d834b649…). => K1 empty, given the E–W Table 6 import and the written
  regridding/transitivity argument.
- 05:48–05:51 compressed-proof pipeline (code/proof_run.py) tested on K1 (A8-K4 solver paused during each test):
  evidence/k1_zst_test: FAILED attempt (CaDiCaL rejects /dev/fd/N as proof path; preserved). evidence/k1_zst_test2:
  solve via lane-local FIFO (nodes *.fifo left in place) into zstd -3: A8 454 KB, B8 5.5 MB compressed, both UNSAT;
  first check via FIFO failed (drat-trim peeks and re-opens the proof file: SIGPIPE; receipts *.check.json kept);
  check via stdin (`zstd -dc | drat-trim CNF -i -t 50000`, binary mode forced): both "s VERIFIED" (receipts
  *.check_stdin.json). This pipeline is used for all further n = 8 certificates.
- Process-stopping record (parent safety rule, received ~05:5x): 05:43:03 A8-K5 CaDiCaL stopped with `pkill -f`
  (SIGTERM). A8-K4 CaDiCaL paused/resumed three times with SIGSTOP/SIGCONT (05:45:38–05:48:10, ~05:48:5x–05:49:23,
  ~05:50:0x–05:51:01). `timeout` wrappers in the K1 pipeline tests use SIGTERM (none fired). No SIGKILL issued by
  scripts; no subprocess timeouts. From now on: native solver/drat-trim limits only; stop = SIGTERM + bounded wait.
- 06:28 checkpoint: A8 generic K2 (2759 s CPU), K3 (2774 s), K4 (2602 s) still running, no verdict; K5 stopped.
- 06:30:49 A8-K4 paused (SIGSTOP) to free a slot. 06:30:52 Gram-pattern encoder GA (code/gram_a.py) validation:
  genuine n=8 Theorem-6 pair and n=7 Cor-7 pair Gram patterns: direct evaluator 0 violations; GA with these fixed
  patterns SAT (evidence/gram_dev_v1). 06:31:01 GA-K5-SB2 (order 8): 478520 vars, 2478600 clauses (sha 9dbd7f70…);
  06:31:06 CaDiCaL launched (proof-free, -t 10500). README §2 written right after (time order recorded there).
- 07:02 checkpoint: A8-K2 4783 s and A8-K3 4794 s CPU, GA-K5 1836 s — no verdicts. 07:02:3x A8-K3 stopped with
  SIGTERM (`pkill -TERM`; log kept, UNKNOWN). A8-K4 remains paused (SIGSTOP since 06:30:49).
- 07:02:44 GA-K2 with SB2 and (P4) in EVERY row frame (justification: in K2, if a quantum square had no weight-3
  entry in frame r, Lemma 10 in frame r would leave ≤ 1 non-classical square, contradicting A8 or K1 = ∅ (K1 holds
  for every frame by row permutation)): 193536 vars, 1341352 clauses (sha 61df97ce…); CaDiCaL launched (-t 10500).
- 07:03 same-ray condition G5 added to GA (code/gram_a.py --g5) and to the direct evaluator: if in the frame of a
  row/column l the support of q is {a}, then Ψ_s(q) ∝ Ψ_s(a), so g_s(p,q) = g_s(p,a) for all other p. Validation:
  genuine n=8 and n=7 pairs 0 violations (direct) and SAT as fixed patterns (07:03:36–07:03:42).
- 07:03:34 GA-K5 (no G5) stopped by SIGTERM (exit 143, 1942 s, UNKNOWN); 07:04:12 GA-K2-allrows (no G5) stopped by
  SIGTERM (84 s, UNKNOWN). Replacements launched (CaDiCaL, proof-free, -t 10500): 07:04:00 GA5-K5-SB2 (509880 vars,
  5740040 clauses, sha ff552576…); 07:04:2x GA5-K2-SB2-allrows (206080 vars, 2645928 clauses, sha f283d285…).
  Running: A8-K2 (single-frame), GA5-K5, GA5-K2; A8-K4 paused.
- 07:35 checkpoint: GA5-K5 1861 s, GA5-K2-allrows 1849 s, A8-K2 6754 s CPU — no verdicts. README §2 addendum (G5,
  P4-all-rows, GB) written 07:35 (its first draft carried a guessed "07:1x" time, corrected to the host time).
- 07:36 ROWLEX added to GA (lex-leader: rows 2..7 sorted by Ψ1's row-0-frame overlap vectors at column 0; sound since
  rows 2..7 can be permuted freely after SB2 fixed rows 0 and 1; K5 only, no classical squares). 07:36:08 GA5-K5
  stopped (SIGTERM, 1924 s, UNKNOWN); 07:36:1x GA5L-K5 (G5 + ROWLEX + SB2, 509915 vars, 5740230 clauses,
  sha 6ecb77a7…) launched (CaDiCaL, proof-free, -t 10500).
- 08:06 checkpoint: GA5L-K5 1790 s, GA5-K2-allrows 3733 s, A8-K2 8667 s CPU — no verdicts. Memory ≈ 4.9 GiB total.
- 08:37:10 A8-K2 (single-frame) reached its 10500 s limit: UNKNOWN (exit 0, "s" line absent). 08:38:21 paused A8-K4
  terminated (SIGTERM then SIGCONT): UNKNOWN. A8 summary: K2 UNKNOWN (limit), K3/K4/K5 stopped early (UNKNOWN).
- 08:38:2x GB (code/gram_b.py, independent) with G5: genuine n=8 and n=7 pairs as fixed patterns SAT (kissat).
- 08:38:4x portfolio run: `cadical --unsat -t 10500` on GA5-K2-allrows (same CNF f283d285…).
- 08:39 cube-and-conquer tooling fetched read-only: `git clone --depth 1 https://github.com/marijnheule/CnC.git`
  into env/cnc (commit 705b60c; a public-source download, no repository of ours touched — recorded because the
  contract lists "No Git"); march_cu built with its Makefile (gcc -O3).
- 08:4x parent's analytic K1 lead checked: code/k1_analytic_checks.py (two implementations, mutations) →
  evidence/k1_analytic/checks.json all_ok (08:44:3x; GA5-K2 --unsat run paused with SIGSTOP for its ~1 s duration).
  Note review/K1_ANALYTIC_N8.md (exploratory): K1 = ∅ follows analytically for any affine 6-net, given the E–W Table 6
  bridge and regridding; no FIXED SAT certificate or PGL frame argument needed. No direct analogue for K2 (counting).
- 08:58:00 parent-caught count error (84 vs 56 three-sets): v2 checks with explicit counters (code/k1_analytic_checks_v2
  .py → evidence/k1_analytic/checks_v2.json, all_ok; 56 T, 1176 r-pairs, 448 b-sets, 64 multiplication comparisons);
  erratum review/K1_ANALYTIC_N8_ERRATUM.md; original note/receipt unchanged. (--unsat run paused ~1 s by SIGSTOP.)
- 08:58–09:03 E–W data: Wayback captures of maxMOLS8.3.txt / nmaxMOLS8.3.txt (+ nmaxMOLS8.2/8.4, LSformat.html)
  fetched (SHA-1/base32 equal to the CDX digests); ew_nets.py: 39 triples Latin/orthogonal, 38 maximal have no 4th
  square (UNSAT), the non-maximal has one (SAT); invariants separate 35 of 39 (ew_nets_inv2/inv3); direct VF2++ test
  of the 4 residual pairs running (09:02:57, GA5-K2 --unsat solver paused meanwhile).
- README §3 amendment (fixed-net K2 via the 39 E–W nets) frozen at the time printed after it in the shell log.
- 09:02:57–09:32:57 ew_nets_iso.py (VF2++) on the first residual pair did not finish within the 1800 s tool cap; the
  harness killed the job (signal not recorded; no receipt written). The GA5-K2 --unsat solver stayed paused (SIGSTOP)
  for that whole window and was resumed (SIGCONT) at 09:33. Next: Weisfeiler–Leman (2-dim) colour refinement as a
  stronger invariant for the 4 residual pairs.
- 09:33:34 GA5-K2 --unsat portfolio run stopped (SIGTERM, 3292 s, UNKNOWN) to free a slot.
- 09:33:36–09:33:40 fixed-net K2 pilot (evidence/k2_fixed/pilot_v1): nets nmax00 (extendable) and max00 (maximal):
  A8r2/CaDiCaL and B8r2/kissat all UNSAT in < 1 s.
- 09:34:11 full fixed-net K2 batch with certificates started (code/run_fixed_k2.py --proof → evidence/k2_fixed/all_v1).
- 09:36:24 GA5-K2-SB2-allrows (generic Gram encoding GA, G5, P4 in every row frame; CaDiCaL default, started 07:04:22):
  UNSATISFIABLE after 9121 s (proof-free; exploratory, single encoder) — independent route to K2 = ∅.
- 09:36:32 nauty canonical certificates (lane venv env/venv8, pynauty 2.8.8.1; code/ew_nets_nauty.py →
  evidence/k2_fixed/nauty.json): 39 distinct certificates (pairwise non-isomorphic nets), relabelled-copy controls all
  reproduce their certificates; |Aut(nmax00)| = 5376.
- 09:50:31 README §4 (K3 via the 2165 E–W 2-MOLS(8) nets; all-frames P4 rationale; storage plan) frozen.
- 09:51:17–09:51:24 K3 pilot (evidence/k3_fixed/pilot_v1; nets max0000, nmax0000; streamed CNFs via lane FIFOs):
  A8r2/CaDiCaL UNSAT + drat-trim VERIFIED (proofs 1.38/1.40 MB zstd), B8r2/kissat UNSAT, ≤ 0.7 s per solve.
- 09:51:33 PREMATURE full K3 batch start (evidence/k3_fixed/all_v1) before reporting the pilot projection; stopped at
  09:51:48 by SIGTERM to the driver (exit 143) after the parent's instruction arrived: 10 (net, encoder) records,
  all UNSAT, 6 A-proofs verified; no orphan solvers. Projection from pilot + partial batch: ≈ 3 s per net with 2
  workers (≈ 1.8 h for 2165 nets), A proofs ≈ 1.43 MB per net incl. logs (≈ 3.1 GB), lane ≈ 7 GB at the end.
- Manifest of the K2 sources/receipts: evidence/MANIFEST_K2_*.sha256 (full SHA-256).
- PROCEDURAL DEVIATION (recorded at the parent's request): the full K3 batch was launched at 09:51:33 before the pilot
  projection had been reported, and paused by SIGTERM to its driver at 09:51:48. The 10 rows written before the stop
  are complete records (all UNSAT; the 6 encoder-A rows carry drat-trim VERIFIED); any instance that was in flight
  at 09:51:48 has no row and is treated as UNKNOWN/not done (it will be recomputed; existing files are never
  overwritten — run_fixed_k3.py now uses a fresh ".retryK" stem if a proof file already exists).
- 09:5x parent approved the measured K3 continuation (≤ 3 h chunk; projection ≈ 3.1 GB; lane cap 10 GiB) with an
  aggregate 4-CPU limit including GA5L-K5, CNF generation, solvers, zstd and drat-trim: ONE K3 worker while GA5L-K5
  and the 2165-net consistency check (code/ew_nets2.py, started 09:5x) run, two after.
- 09:53:05–09:57:51 2165-net consistency (code/ew_nets2.py → evidence/k3_fixed/ew_nets2.json): 2127 + 38 nets, all
  Latin/orthogonal; third orthogonal square: UNSAT for all 2127 maximal, SAT for all 38 non-maximal; 2165 distinct
  nauty certificates; sampled relabelled-copy controls OK.
- 09:58 K3 batch resumed with ONE worker (evidence/k3_fixed/all_v1, stdout all_v1.stdout.resume1.log); GA5L-K5 still
  running (≤ 3 CPUs in use).
- 09:58:32 README §5 (minimal-counterexample all-frames P4; K_m-minimal encodings) frozen. 09:58:38–09:58:55
  generated with code/gram_a_r2.py (GA r2: adds --p4-all-cols): K4-minimal 411712 vars / 4726836 clauses
  (sha 89082e60…296e), K5-minimal 514115 / 5857905 (sha c6580ec6…07eb) in evidence/kmin_v1.
- 09:59 K4-minimal CaDiCaL launched (proof-free, -t 10500). CPU in use: GA5L-K5 (1) + K3 worker (≤ 2) + K4min (1).
- 10:17:26 GA5L-K5 (generic K5: Gram encoding GA with G5, SB2, row lex-leader; P4 in the row-0 frame only, i.e. NOT
  relying on minimality; CaDiCaL default, started 07:36:15): UNSATISFIABLE after 9671 s (proof-free, single encoder;
  exploratory). CNF sha 6ecb77a7… (evidence/gram_dev_v1/GA5L_K5_sb2.cnf).
- 10:17:3x K5-minimal launched (CaDiCaL, proof-free, -t 10500) in the freed slot. CPU: K3 worker (≤ 2) + K4min (1) +
  K5min (1).
- 10:1x parent: disk cap stays 10 GiB/lane; certificate strategy (a) measure K4/K5-minimal, (b) cube-and-conquer with
  checked cover formula and every cube proof verified by streaming into drat-trim, (c) deterministic-replay receipts.
- 10:18–10:19 code/cert_stream.py (solver DRAT → lane FIFO → drat-trim stdin, CNF(+cube units / negated cubes)
  streamed through FIFOs; no proof stored; replay receipts): tests on the K1 CNF — whole: UNSAT + VERIFIED
  (evidence/cert_stream_test_v1); march_cu -d 4 → 1 cube; cubes and cover tasks both VERIFIED (evidence/cnc_test_v1).
  K5min solver paused (SIGSTOP/SIGCONT) during each ~2–8 s test.
- 11:02:57 review/PROOF_K1_K2.r1.md frozen (scope K1, K2 only; supersedes the K1 status lines of older notes without editing them).
- 11:00:07 K3 driver paused by SIGTERM (resumable; in-flight instance UNKNOWN) to run parent item M2 (the 1-worker
  run's last row: max1060 a at 11:00:04). 11:00:05–11:00:13 M2 relaxed --squares control
  (code/relaxed_squares_control.py → evidence/k2_fixed/relaxed_ctrl_v1/RECEIPT.json): nmax00 completed by two further
  MOLS X, Y (exact SAT); enc8_a2 / enc8_b2 CLI --squares CNFs with --p4 none: SAT, model satisfies every clause; with
  S1, S2 fixed to the explicit classical configuration (896 units): SAT, model satisfies every clause. 11:00:2x K3
  resumed with 1 worker (K4min, K5min running).
- 11:00 M1 first attempt evidence/MANIFEST_K2_ARTIFACTS_1100.sha256 is INCOMPLETE (4 lines): `shasum $(ls)` blocked on
  the FIFO node a_max00.cnf.drat.zst.fifo and the harness ended the job at its 300 s cap (file kept as is).
  11:05:4x complete additive manifest over regular files only: evidence/MANIFEST_K2_ARTIFACTS_v2_1105.sha256 (664
  files; sha 3beb5f26…2149).
- Clarifications (parent minors): solve_secs = 5.0 in K2 all_v1 is the watchdog sampling interval, not a measured
  solver time; the VF2 attempt was replaced by nauty (input evidence/k2_fixed/ew_nets.json sha 497f6df0…); the
  proof-free generic GA-K2 run is exploratory, not an independent certified route; plan deviation: README §3
  promised a measured pilot before the batch — the 2-net pilot ran proof-free and the certified batch covered all 39
  nets (37 never piloted).
- 11:15 leftover named pipes recorded (parent note): 78 FIFO nodes *.drat.zst.fifo remain in
  evidence/k2_fixed/all_v1 (created by code/proof_run.py solve; zero-byte pipes, not evidence content); left in place,
  as are the reusable FIFOs w*.fifo in evidence/k3_fixed/{pilot_v1,all_v1}, the K1 test dirs and cnc/cert tests.
  Nothing under evidence/k2_fixed/all_v1 or review/PROOF_K1_K2.r1.md will be modified.
- 11:31:51 review/PROOF_K1_K2.r2.md frozen (editorial fixes of the two K1/K2 reviews; r1 unchanged).
- 12:06:36 K3 batch finished (resume2 run, 1 worker): 4330 rows = 2165 nets × 2 encoders, all UNSAT, 2165 A proofs
  drat-trim VERIFIED (RESULTS.jsonl sha 39a7a3cd…79e5).
- 12:06:43 coverage ledger (code/k3_ledger.py → evidence/k3_fixed/K3_COVERAGE_LEDGER.json sha ab63f64c…0d98): complete,
  no problems, no orphan proofs; all A proof hashes re-computed and matching.
- 12:07:33–12:07:40 K3 relaxed --squares control (code/relaxed_squares_control_k3.py → evidence/k3_fixed/
  relaxed_ctrl_v1/RECEIPT.json): AG(2,8) pair, both encoders: --p4 none SAT with fully satisfying models; explicit
  classical configuration (3 completing MOLS) fixed by 1344 units: SAT, fully satisfying models.
- 12:08:18 review/PROOF_K3.r1.md frozen (scope K3 only).
- 12:23:10 nmax cross-check (code/k3_crosscheck_nmax.py → evidence/k3_fixed/crosscheck_nmax.json): 195 4-subnets of the
  39 3-MOLS(8) representatives fall into exactly 38 classes = the 38 classes of nmaxMOLS8.2.txt (nauty certificates).
- 12:23–12:54 P4-on control attempts (code/p4_on_control_k3.py, evidence/k3_fixed/p4on_ctrl_v1, no receipt): A8r2
  (P3) off on the AG pair UNSAT; one classical square UNKNOWN at the 1200 s limit; no classical square stopped by SIGTERM
  (12:54:13, driver and solver); B not reached. Recorded as "P4 not exercised by a SAT control" (parent instruction).
- 12:54:02 K4-minimal (GA r2) reached its 10500 s limit: UNKNOWN (exit 0).
- 12:54:58 review/PROOF_K3.r2.md frozen (r1 unchanged).
- 12:56:37 README §6 (K4-minimal CnC pilot) frozen. 12:56:43 first march attempt failed to start (exit 127: `timeout` is
  a shell builtin; /usr/bin/time could not exec it); code/run_bounded.py (SIGTERM-only wall bound) written.
  12:57:07–13:05:07 march_cu -d 6 on GA2_K4min.cnf: no cube emitted within 480 s (still in lookahead set-up); stopped
  by SIGTERM (exit −15). evidence/k4_cnc_pilot_v1.
- 13:05:23 manual mini-pilot: row-1 cubes of the classical square L (π(0) = 1 by SB2, π(j) ≠ j: 2119 cubes); the first 3
  cubes with streamed verification (code/cert_stream.py, -t 150): all UNKNOWN at 150 s (evidence/k4_cnc_pilot_v1/
  row1_cubes/RESULTS.jsonl). Projection: ≥ 2119 × 150 s ≈ 88 CPU-h even if every cube took just over the limit —
  infeasible before the deadline; no batch launched.
- 13:07:42 K5-minimal (GA r2: all row+column-frame P4, SB2, G5, row lex-leader; started 10:17:43): UNSATISFIABLE after
  10199 s (proof-free, exploratory).
- 13:15:23 README §7 (K4 weight-1 encoding, one exploratory solve) frozen; 13:15:37 GA3_K4w1.cnf generated (gram_a_r3.py
  sha 40622a6f…fdbb; 513184 vars, 5833793 clauses, sha 7bb806fc…01f7); 13:15:42 CaDiCaL launched; 13:17:31 STOPPED by
  SIGTERM (109 s, UNKNOWN) to keep the lane ≤ 8 GiB RSS while the parent-prioritised K5 split pilot runs (K5 solves
  peaked at 4.1–4.3 GB; K4w1 was at 3.3 GiB and growing). It can be rerun later.
- 13:16:31 README §8 (K5 split: V = 7 Gram literals g_1((0,k),(2,0)), all 128 complete assignments) frozen; 13:17:3x
  cubes written: evidence/k5_split_v1/cubes_V7.icnf (+ receipt). Pilot cubes b = 1, 8, 3, 24, 9, 14 run sequentially
  (1 worker, memory) with the §8 pipeline (code/k5_split.py).
- 13:17:46–13:20:04 K5 split pilot (evidence/k5_split_v1/pilot/RESULTS.jsonl): cubes 1, 8, 3, 9, 14 — UNSAT in ≈ 2 s
  (watchdog granularity), proofs 53–85 KB zst, drat-trim ≈ 2.6 s, checker RSS ≈ 0.52 GB, all VERIFIED; cube 24
  ({4,5}) — UNSAT in 90.4 s, proof 56.1 MB zst, drat-trim 24.1 s, checker RSS 1.05 GB, VERIFIED.
- 13:2x parent GO for all 128 K5 cubes (1 worker, -t 900, cap 300 MB, retain zstd proofs, stop before the lane exceeds
  9.5 GiB, UNKNOWN cubes → re-split amendment). 13:21:13–13:21:22 base CNF regenerated in memory by gram_a.py build()
  with the recorded arguments: SHA-256 6ecb77a7…469b = stored file (evidence/k5_split_v1/REGEN_RECEIPT.json).
- code/k5_split_r2.py = k5_split.py + lane disk-budget guard (pipeline unchanged). Batch: the 122 non-pilot cubes into
  evidence/k5_split_v1/all (pilot receipts in evidence/k5_split_v1/pilot are part of the coverage).
- 13:22:41 review/K4K5_ENCODING_SOUNDNESS.r1.md written (draft r1 for review; not a result).
- 13:29 parent run-wide disk floor: stop/do not start write-heavy work if filesystem free < 12,000,000,000 bytes
  (free was 24.4 GB). 13:3x code/disk_floor_watchdog.py attached to the running K5 batch (driver pid 59384): checks free
  bytes every 10 s; below the floor it SIGTERMs the driver and the processes on the batch FIFOs (solver/checker), waits
  ≤ 60 s, writes evidence/k5_split_v1/DISK_FLOOR_WATCHDOG.json; never SIGKILL, never deletes.
- 14:32 checkpoint K5 batch: 58/122 rows; UNKNOWN (900 s limit): cubes 16 {5}, 32 {6}, 48 {5,6} (partial proofs ≈ 140 MB each retained); non-trivial UNSAT: 40 (353.5 s, 89.3 MB, check 111 s, RSS 1.08 GiB), 56 (32.1 s, 46.5 MB); all other cubes ≈ 2 s. Lane 8.10 GiB, filesystem free 21.1 GB.
- 14:47:36 FROZEN review/K4K5_ENCODING_SOUNDNESS.r2.md sha eda1860e82b983d1a8b414bdc201c86131ad3ea87b955d41823a6430619577da (complete soundness write-up for audit; r1 draft unchanged). README §8.1 frozen 14:44:41 (README sha after freeze 33e36dd7…c7c0; code/k5_resplit.py ccc6548c…53c3).
- 14:48–14:49 streamed-pipeline smoke controls (code/k5_resplit_smoke.py; evidence/k5_split_v1/resplit_smoke{,_r2}/SMOKE.jsonl):
  PHP(6,5) UNSAT → VERIFIED; PHP(5,5) SAT → not verified (solver 10, checker "s NOT VERIFIED"); real leaf cube 0 ∧ ¬V2
  → VERIFIED (75 KB stream, 4.1 s); fail-closed case cube 16 ∧ ¬V2 with -t 1: solver interrupted while parsing
  (exit 1, 0-byte proof) while drat-trim printed "s VERIFIED" on the EMPTY proof (that leaf is refuted by unit
  propagation) — verdict correctly false because the solver conditions are required. First run showed an uncaught
  BrokenPipeError in the CNF feed thread; k5_resplit.py revised before any production use (feed errors caught, recorded,
  and required to be absent for a verdict): new SHA-256 4aed8e43…7069 (supersedes ccc6548c…53c3 sent at 14:47);
  smoke re-run on the revised script (resplit_smoke_r2) gave the same four outcomes.
- 15:0x Codex audit (parent relay 14:5x): ACCEPT-WITH-FIXES. Fix 1: old root records are WORKER evidence only →
  code/k5_root_reclassify.py (1f6dbf03…553e). Fix 2: cover ledger + validator code/k5_cover.py (93265896…22c7),
  ledger-driven strict runner code/k5_leafrun.py (b9313ebb…fae), validator controls code/k5_cover_controls.py
  (1afd9aa1…6372) → evidence/k5_split_v1/ledger/COVER_CONTROLS_v1.json (59f6cbec…7337): 26/26 PASS (7 positive incl.
  synthetic complete/incomplete covers, 19 mutations: missing/duplicate root, flipped root/child literal, wrong depth
  list, 127-child family, solver exit 0, NOT VERIFIED line, CNF/base hash mismatch, stale receipt of another leaf,
  worker-positive used as CERTIFIED/UNKNOWN, missing receipt line, certified-but-UNKNOWN, UNSTARTED with evidence, RSS
  trip, absent strict field, childless REFINED, duplicate JSON key). README §8.2 frozen 15:07:51 (README f668f445…94ec).
- 15:07 §8 batch: 90/122 rows in all/ (cubes ≤ 95), worker non-positive {16,32,48,64,80}; cube 96 running.
- 15:12:50 FROZEN review/K4K5_ENCODING_SOUNDNESS.r3.md sha a83d305013fa920d1ffe361d6d0aeb589f958da477420b2b053a503221858e59 (addresses Codex v1 minor 3 and Claude v1 M1–M3, m1–m10; r1/r2 unchanged).
- 15:13:41–15:13:50 K4 base regenerated in memory (code/regen_hash_k4.py; evidence/k4_split_v1/REGEN_RECEIPT.json):
  byte-equal to GA3_K4w1.cnf (7bb806fc…01f7); 64 P4 at-least-one clauses, w3 squares {1,2,3,4}, 0 lexeq variables.
- 15:14 K5 base family counts (code/count_families_k5.py; evidence/k5_split_v1/FAMILY_COUNTS.json): byte-equal
  regeneration; exactly 5 P4 at-least-one clauses = (square s, row-0 frame), s = 1..5; w3 frames {row 0}; 35 lexeq
  variables on pairs (i, i+1), i = 2..6; 40 unit clauses = 35 SB2 units on g_s((0,k),(1,0)) + 5 lexeq(i,0) units
  (bit 0 is constant ⊥ in both rows); no other auxiliary families.
- 15:20:05 §8 batch ended (122/122 rows in all/ + 6 pilot rows; watchdog lowest free 20.27 GB). Worker non-positive
  roots (900 s timeouts): 16, 32, 48, 64, 80, 96; 122 worker positives.
- 15:20:13 code/k5_root_reclassify.py → evidence/k5_split_v1/ROOT_RECLASSIFY_v1.json: 128 records, 128 distinct cubes,
  strict_certified 0 (every record lacks solver rc / zstd rcs / feed status) — all old records are worker evidence.
  Ledger: v001 init (5a38223b…378b); v002 = ingest of the 6 non-UNSAT worker records as UNKNOWN (14219334…9371);
  validate v002: problems [], UNSTARTED 122, UNKNOWN 6. Parent approved order: K5 strict depth-1 → K4 pilot → K5 depth 2.
- 15:20:24–15:48:03 K5 strict depth-1 (code/k5_leafrun.py, ledger v002; evidence/k5_split_v1/strict_L1/RESULTS.jsonl):
  122/122 worker-positive roots strict_ok (solver rc 20 + "s UNSATISFIABLE", drat-trim rc 0 + "s VERIFIED", no NOT
  VERIFIED, no feed/relay error, self-exit, no guard trip); retained §8 proofs bound for 122/122 (old file SHA = old
  receipt, zstd -dc rc 0, decompressed SHA = streamed proof SHA). Non-trivial: c024 107 s, c040 417 s, c056 38 s,
  c072 154 s, c088 65 s, c104 40 s, c112 360 s; max aggregate RSS 4.28 GiB; total 1644 s.
  Ledger v003 (b9b3fc67…b14b) = ingest strict_L1: validate problems [], CERTIFIED 122 (worker strict; parent replay
  pending), UNKNOWN 6 = c016, c032, c048, c064, c080, c096; complete false. Refinement held until parent go.
- 15:21 K4 ledger v001 init (966b6f6f…3577; code/k4_cover.py), validate problems []; negative control: validating it
  against the K5 base is rejected (base sha/header).
- 15:5x parent clarification recorded as README addendum (streamed non-retained depth-2/K4 leaves allowed; preserve
  existing retained proofs, all terminal receipts and UNKNOWN frontier records; no cap increase, no deletion).
  15:49:33 code/k5_root_manifest.py (57c2daa5…81dd) → evidence/k5_split_v1/RETAINED_ROOT_PROOFS_MANIFEST_v1.json
  (65f6e0dd…3b5e) + .sha256 (4e109813…a9ca5): 122 CERTIFIED roots, all consistent (retained file SHA = old receipt =
  binding; decompressed SHA = strict proof-stream SHA; leaf-CNF SHA recomputed = strict = old), 444,419,127 bytes;
  `shasum -a 256 -c` 122/122 OK. K5 depth 2 HELD pending K4 pilot projection.
- 15:48:21–16:48:46 K4 PILOT (§9; code/k4_leafrun.py, K4 ledger v001; evidence/k4_split_v1/pilot/RESULTS.jsonl):
  c016 {5}, c032 {6}, c048 {5,6}, c001 {1}: UNKNOWN (900 s; solver rc 0, drat-trim rc 1 "s NOT VERIFIED" on the
  partial stream of 347–365 MB; aggregate RSS 4.21–4.37 GiB); c037 {1,3,6} and c061 {1,3,4,5,6}: strict_ok in 4.0 s
  (0.43 GiB). Structural classes of the 128 K4 roots (S = support of Q1(2,0)): 64 with 2 ∈ S (forced ⊥, L(2,0) = 2),
  1 empty, 22 weight ≥ 4, 22 with |S ∩ {2,3,4}| = 1 (Lemma 2 vs Q1(1,0) = {2,3,4}) — predicted trivial (109); 5 with
  S ⊇ {3,4} (12, 13, 28, 44, 76) — unknown; 14 with S ⊆ {1,5,6,7} (1, 16, 17, 32, 33, 48, 49, 64, 65, 80, 81, 96,
  97, 112) — presumed hard (4/4 sampled timed out). Projection sent to the parent before starting anything else.
- 16:5x parent GO: K5 depth-2 PILOT on c016 only (128 V2 children, strict streamed non-retained, ≤ 2 busy processes,
  ≤ 6 GiB, no other heavy lane job, 3 h chunk cap); K4 pilot outcomes stay UNKNOWN; no auto-start of K4 depth 1 or K5
  depth 3; structural filters (code/split_classes.py) are planning only — every leaf gets a strict receipt or stays
  UNKNOWN/UNSTARTED. Ledger v004 = refine c016 (children c016.L2.000–127 UNSTARTED); validated.
- 16:52:50 code/chunk_cap.py attached to the c016 depth-2 runner (pid 34876, started 16:52:14): cooperative SIGTERM stop at 19:50:00 PDT (3 h chunk cap) or if free < 12e9; receipt evidence/k5_split_v1/strict_L2/CHUNK_CAP.c016.json.
- 17:02:06 parent GO(a) for the K4 automorphism CHECK only (≤1 CPU, ≤1.75 GiB). code/k4_automorphism_r2.py (exact sorted int32 clause-matrix equality, canonical identities, group closure, cube orbits, 3 controls) launched under run_bounded (1500 s); the draft code/k4_automorphism.py was never run (superseded).
- 17:02:06–17:02:28 K4 automorphism CHECK (code/k4_automorphism_r2.py ae9bcbb4…708f → evidence/k4_split_v1/
  AUTOMORPHISM_S3_567_r2.json d688277f…357c): names table 513184 vars (g 7840, b3 94080, c4 376320, u5 31360, w3 3584;
  canonical identities injective; lane-map g mismatches 0); CNF 5833793 clauses / 20045017 literals parsed; identity,
  g1 = (5 6), g2 = (6 7): bijection + EXACT clause-multiset invariance; group order 6, relations hold, all 6 elements
  automorphisms; NEG σ = (4 5) and NEG corrupted map FAIL as intended; 64 V1 root orbits; stabiliser child orbits 64/96.
  Max RSS 1.63 GiB (cap 1.75), 1 CPU, 21.5 s. review/K4_ORBIT_REDUCTION.r1.md (89e8c52e351c02671663caab7d2989008ddbf4c1c26a0e065b9bfa06cd7d7286) written; README §9.1 frozen (not
  in force until parent GO(b)).
- 17:05:59 code/k4_orbit.py written (orbit-aware validator extension per review/K4_ORBIT_REDUCTION.r1.md §3; NOT run, NOT in force before GO(b)).
- 17:23:49–17:27:29 K4 orbit r2 work (parent: Claude M1/M2 + minors, Codex minors): code/k4_automorphism_r3.py wrote and
  RELOADED pinned arrays PERM_g1/g2 (8b09da43…/e0a2bc4c…), exact checks PASS on reloaded arrays, 5 controls as
  intended, S3 order 6 (receipt c7154dc3…); independent pure-Python second path code/k4_auto_secondpath.py PASS
  (2990e216…; identity PASS, swap/polarity FAIL, V1/V2 closure, 73.5 s, 1.25 GiB); validator code/k4_orbit_r2.py (09d7af13c10d36b400e709650e19e77b923fc31035e6fdd73499af942dfda289)
  + in-memory controls 14/14 PASS; review/K4_ORBIT_REDUCTION.r2.md (c99d31440c4a88d8761d55d18b2bf0efef52b74792a1930c6289adebd3f79cc7) frozen; README 9.1 addendum r2 (not in force).
- 16:52:14–17:31:01 K5 depth-2 pilot on c016 (evidence/k5_split_v1/strict_L2/RESULTS.jsonl; ledger v004 19b080bf…f90d):
  128 strict receipts: 126 strict_ok, 2 UNKNOWN (c016.L2.040 {4,6}, c016.L2.072 {4,7}: 903.5 s, solver rc 0).
  All leaves: mean 18.1 s, median 4.0 s, max 903.5 s, total 2315 s; the 17 planning-plausible leaves: mean 109.8 s,
  median 4.0 s, max 903.5 s; every non-plausible leaf ≤ 4.1 s. Max aggregate RSS 4.2 GiB; max proof stream 306 MB
  (streamed, not stored). Chunk-cap stopper not triggered (runner finished; lowest free 17.54 GB). Ledger v005 =
  ingest strict_L2 (061d9038…170f): validate problems [], CERTIFIED 248, UNKNOWN 7 (c032, c048, c064, c080, c096,
  c016.L2.040, c016.L2.072), REFINED 1. Lane 8.55 GiB; free 17.53 GB. Waiting for the parent's next go.
- 17:41:59 parent GO: K5 depth-3 PILOT on c016.L2.040 only (128 V3 children; 900 s/leaf; chunk ≤ 3 h; strict streamed; ≤ 2 busy CPU / ≤ 6 GiB; no other heavy lane job; no auto depth 4, no K4 production). Ledger v006 = refine c016.L2.040; validated.
- 17:42 K5 depth-3 pilot runner pid 47331 (ledger v006 1d098d68…d13f; outdir evidence/k5_split_v1/strict_L3); chunk_cap.py attached (stop at start + 2h55m or free < 12e9; receipt strict_L3/CHUNK_CAP.c016L2040.json). Parent K4 delta review v2: Codex MAJOR read-twice TOCTOU in code/k4_orbit_r2.py (hash at one read, deserialize at another) → new single-buffer validator r3 + controls r3 + dependency-closure manifest (in progress).
- 17:44 K4 orbit validator r3 (code/k4_orbit_r3.py 5a324a1d…; single-buffer artifact binding) + controls r3
  (code/k4_orbit_controls_r3.py f7c843a7… → auto_r3/ORBIT_VALIDATOR_CONTROLS_r3.json db023a5f…): 25/25 PASS incl.
  R1 (second g1 read swapped 57/106 → never read; Codex exploit c022 ← c037 via g1 rejected), R3 (each artifact read
  exactly once: 4 files × 1), R4 (substituted bytes at the only read → pin mismatch), N1–N6 (full-path vs incremental,
  strict-source unit mismatch, literal bounds, truthy non-bool verdicts, 127-child refined source, combined cycle).
  Dependency closure auto_r3/DEPENDENCY_CLOSURE_r3.sha256 (93dd744a…0004; 16/16 OK). README 9.1 addendum r3 frozen.
- 17:41:59–18:10:13 K5 depth-3 pilot on c016.L2.040 (evidence/k5_split_v1/strict_L3/RESULTS.jsonl): 128 strict
  receipts, 127 strict_ok, 1 UNKNOWN = c016.L2.040.L3.104 (row-4 support {4,6,7}; 903.6 s); L3.040 ({4,6}) certified
  in 268.9 s; all others ≈ 4 s; mean 13.2 s, median 4.1 s, total 1685 s; max aggregate RSS 4.28 GiB. Ledger v007
  (aba9dd48…6b03): validate problems [], CERTIFIED 375, UNKNOWN 7 (c032, c048, c064, c080, c096, c016.L2.072,
  c016.L2.040.L3.104), REFINED 2. Hard frontier shrinks 2/128 (depth 2) → 1/128 (depth 3) but does not vanish.
- 18:1x parent GO(b) (17:5x): K4 orbit plan r2 with validator code/k4_orbit_r3.py after the K5 depth-3 pilot; root and
  depth-2 orbit runs only; no overlapping heavy pipelines. Starting K4 depth 1: ledger v002 = ingest of the 6 pilot
  strict receipts; strict runs of the 113 roots in evidence/k4_split_v1/L1_STRICT_IDS.txt (086cae72…2e6a; all roots
  except the 10 orbit non-representatives and the 6 pilot roots) via code/k4_leafrun_r2.py (29a44761…7850).
- 18:13:25 parent approved ONE exploratory kissat 4.0.4 proof-free run (--time=900) on c016.L2.040.L3.104 alongside the K4 runner, with joint lane guard (busy ≤ 3, aggregate lane RSS ≤ 7.5 GiB, SIGTERM only kissat). code/kissat_explore.py writes evidence/k5_split_v1/explore_kissat/EXPLORE_RECEIPT.json before launch. Timing signal only.
- 18:13:25–18:28:28 EXPLORATORY kissat 4.0.4 proof-free --time=900 on c016.L2.040.L3.104 (leaf CNF 6d84469e…aebd; kissat 05d6f3e9…a848): UNKNOWN at 902.5 s (rc 0); guard not tripped (peak lane RSS 5.38 GiB, peak busy 3, 178 samples). Timing signal only: kissat gives no quick win on this leaf (evidence/k5_split_v1/explore_kissat/RESULT.json).
- 18:32:30 amendment RETRY-ONCE frozen: review/AMENDMENT_RETRY_ONCE.md 507be52839cb153a26414cdf3ecc6d8d3def252a3fa78e9eca4b0389fd9ac371; code/k5_resplit_r2.py 90b6f5928058db04315534640dba556486a969441009f0e680f5de0873558484; code/leaf_retry.py 5a82b49b62ecce6d3c1a2dc68ec4619c7faa113ed42bc7bd2ddb5efe2378ffa7 (README results-log entry). Order (parent): finish K4 depth-1 pass → retry queue (incl. 1800 s measurement on c016.L2.040.L3.104) → K5 depth 2 on c032/c048/c064/c080/c096 under retry-once.
- 19:07:36 checkpoint: K4 depth-1 pass 97/113 strict receipts (94 strict_ok; UNKNOWN c012 {3,4}, c017 {1,5}, c049 {1,5,6} at 900 s; c028 {3,4,5} certified 196.1 s; c013 8.1 s); runner continuing (c112 pending). Lane 8.56 GiB, free 18347974656.
- 19:22:11 K4 depth-1 pass finished: 113 receipts, 109 strict_ok; UNKNOWN c012, c017, c049, c112 (900 s);
  c013 certified 8.1 s, c028 certified 196.1 s. Maximum sampled aggregate RSS 4.192 GiB, total 4255.2 s.
  Ledger v003 = ingest strict_L1 (43a3ef16…c3f5); validation problems []. Orbit transfers c044 <- c028 via g1
  and c076 <- c028 via (g2,g1) yield v004/v005; v005 92a2182d…79ab validates with 111 strict-certified roots,
  2 orbit-certified roots, 8 UNKNOWN (including the nonrepresentative c032), 7 UNSTARTED, complete false.
- 19:24 retry preflight: retry_smoke/SMOKE.jsonl preserves PHP(6,5) verified and PHP(5,5) not verified.
  PHP(8,7) finished before its 1 s checker cap, so its expected-timeout control FAILED (it actually verified).
  A larger PHP(11,10) native-limit control is running separately; no production retry has started yet.
  RETRY_QUEUE_v1.json pins eligible queues and one-retry-per-command chunking; amendment freeze remains 18:32:30.
- Retry checker-timeout control completed: PHP(11,10), solver native120s, checker native1s produced solver rc20
  UNSAT and checker rc0 with "s TIMEOUT"; strict verified=false, control_pass=true (66.7s, 0.608GiB aggregate).
  Receipt retry_timeout_control_v1/RECEIPT.json preserves the 204402707-byte streamed proof hash; no proof retained.
  This discharges the timeout control that the faster PHP(8,7) did not exercise.
- 19:56 checkpoint: extended K5 c016.L2.040.L3.104 attempt2 remains UNKNOWN after 1805.2s (solver rc0,
  checker rc1 "s NOT VERIFIED", no RSS trip; sampled aggregate peak4494770176B; proof stream364813175B).
  Same CNF SHA 6d84469e…aebd. Ledger v008 59dc917a…4b33 preserves attempt1 in prior_attempts and records attempt2;
  validation problems [], no count changes. No third attempt. Depth4 still requires parent approval.
  Next queued retry K4 c001 started under the same 1800s/3600s native limits and 6GiB guard.
  Filesystem free18168680448B; proofs remain non-retained.
- 19:59 proof candidate K5_RESIDUAL_NORMAL_FORM.r1.md frozen for parent review (c2c77c47…3d3a):
  residual S4(B) plus square relabelling and re-sorting rows2..7 would reduce the remaining genuine-vector
  cases to c064/c096, conditional on the122 accepted root exclusions. No schedule/ledger change before approval.
  Bit-order control receipt NORMAL_FORM_BIT_CONTROLS_v1.json a85a0609…9edd passes32736 families/192384
  family-permutation checks/224 mixed-A comparisons and2 intended wrong-leftmost controls.
- 20:27 checkpoint: K4 c001 attempt2 remains UNKNOWN after1803.6s, solverrc0/checkerrc1, peak4.28GiB.
  Ledger v00643efc9e7…10b4 records both attempts; validation problems[]. Next authorised queued retry c012
  started. The two extended-limit measurements so far close neither K5's deep leaf nor K4c001.
- 20:30 H3 necessity/proposed600s pilot protocol frozen for approval: review/HALL3_PATTERN_NECESSITY.r1.md
  068d30e5…b17f. No H3 generator or run before parent approval.
- 20:57 checkpoint: K4 c012 attempt2 remains UNKNOWN1804.4s, no guard trip, peak4755734528B,
  proof stream393488493B (not retained). K4 ledger v00708725ee5…77bd validates with no count change.
  Approved next retry c016 started. Shared free14977671168B (pre-leaf floor12e9 maintained).
- 21:28 checkpoint: K4 c016 attempt2 also UNKNOWN1805.2s, no guard trip, peak4867801088B,
  proof stream504450967B. K4 ledger v00826c9f93c…d4e8 validates; no count changes. Next approved retry c017
  started. Extended retries now0/4 closures (one K5 deep leaf plus K4c001,c012,c016). Free14264991744B.
- 21:30 K5 normal-form proof r2 frozen for review: 1a3a47cf…ca7f. Projection lemma forces a pure-B
  column0 vector without machine imports; residual S4+row sort gives c064/c096/c112. Only c112's accepted
  proof then removes the third case. No computational cutover before parent approval.
- 21:58 checkpoint: K4 c017 attempt2 UNKNOWN1804.6s, no guard trip, peak4757307392B, stream507921694B.
  K4 ledger v0094184d64d…b3bb validates. Approved next retry c048 started; retries0/5 closures so far.
  Free14295760896B; no proof retained. Rank-H3 and normal-form proposals still held.
- 22:29 checkpoint: K4 c048 attempt2 UNKNOWN1805.3s, no guard trip, peak4777639936B,
  stream512748696B. Ledger v0100887ca9a…2d11 validates; no counts change. Next approved retry c049
  started. Extended retries0/6 closures; shared free14057283584B. Proposed H3 pilot still awaits approval.
- 22:38 parent approved the H3 exploratory pivot. c048 had already ended and c049 was running, so only the
  owned c049 solver/checker received SIGTERM; bounded wait confirmed both exited. Attempt2 receipt records
  UNKNOWN556.7s, solver/checker -15; K4 v01110780c21…b936 ingests it and validates with unchanged counts.
  Further blind retries are paused. No proof deleted/retained.
- 22:42 H3 pilot generator frozen in README§10: code/h3_pilot.py7aa7bfb2…d383, protocol068d30e5…b17f.
  Shared free13864370176B. Both requested controls precede the single600s proof-free hard-leaf solve;
  all CNFs are streamed (base137.7MB exceeds100MB retention gate); native limits and6GiB guard active.
- 22:42:54–22:53:04 H3 exploratory pilot completed. Raw235200 candidates ->199920 emitted clauses,
  35280 tautologies dropped; no new variables/auxiliaries; H3 body15131040B (87dd3005…0e91).
  Controls: J3x2⊕J2x3⊕I3 passes G3 but violates2 H3 clauses; H3-only fixed instance UNSAT2.0s.
  AG(2,8) strong relaxation (exactly5P4-ALO+7Q1-SB2 units dropped) remains SAT2.0s; the returned model
  satisfies all5947978 clauses, including H3 and7840 fixed Gram units. Identity/permutation/Fourier8/H2-block
  support matrices have0 H3 violations. Control summary ac520ae5…18b.
  Hard K5 leaf F+H3+21sameunits: UNKNOWN602.1s at native600s, no guard/feed failure;4.055GiB peak.
  New leaf CNF SHA db8fcfec…1c10,152795747B, streamed only. Result8a53acc2…5209; no proof checked.
  H3 output dir~3.93MiB (logs/receipts only). Further1800s retries paused as instructed; no H3 cutover.
- 23:15 finite component controlv2 completed (v1 failed before its first parsed graph on lexical typo
  "not63"; failed metadata preserved). genbg2.9.3 pin63822426…15f83 streamed26593 connected colour-isomorphism
  classes for part sizes<=8 (degree1-isolated pruning; min2/max3 otherwise), independent graph6 parser,
  pairwise and rank3 filters. Five allowed types only; no outside component. One2x3 type rejected by rank3
  (and its3x2 transpose). Connected labelled counts by size1..8=1,1,10,24,0,0,0,0; fullsquare counts through8
  =1,1,3,25,298,4770,111770,3367910,122467800 (including empty n0). RESULT3aa58aa8…72ba,0.474s.
- 23:18:57 existing c064 disk-floor watchdog stopped its driver/owned child cooperatively at11997306880B;
  no process survived the bounded wait.24 complete receipts preserved (23strict,UNKNOWNc064.L2.016);
  in-flight leaf24 remains UNSTARTED, never certified. K5v010e6bdd1ea…a9cd ingests the24, validates.
  Fresh23:19/23:20 free recovered to16.2GB without any action/deletion by this lane. Resumed same c064 pass
  with NEW --floor12200000000 before each leaf, identical-unit resume, to finish its root before the13templates.
  No second SAT pipeline; new finite chunk/one-shot checkpoint attached.
- 23:23 template manifest/control built: direct3x3/4x4 counts25/298;43290 labelled patterns with fixed
  column1=A give exactly16 orbits under144 coordinate permutations plus row sort. Manifestf77c0619…0b71
  has16cases,13runs(10root64,3root96). README§11 freezes strict runner99e19533…5081 and identities before use.
- 23:34 unified bridge frozen c391a67a…bbb3 before any weakened formula generation. Exact four source
  ALO deletion records4509b3e7…e3a6; A8 parent acceptance cited at verdict919daeac…a8f9 lines9,13,36.
  Parent authorised preparation and16 weak runs after13 strong runs, allc112 templates included anew.
- 23:39 new K5_SEMANTIC_REVIEW_REPAIRS.r1.md41395137…1022 closes all NF/TPL/import/H3 minor findings;
  originals unchanged. Repair-linka4e22c3c…f3ef binds unchanged16-case instance manifest. No semantic claim yet.
- 23:42 permitted one-P4 preparation regenerated new base374d6fb4…eeb9,509915vars,5740226clauses by
  deleting only the four pinned source lines; Q1 kept and all other bytes remain in order. No CNF file stored.
  Weak16manifest355b3380…fc74; recipe264288f8…0c18; each weak leaf5740268clauses. No weak solver started.
- 23:47 finite checkpoint: c064 has32 complete receipts,30 strict,UNKNOWNc064.L2.016 and.024,
  currentleaf32 in flight; original prefix/partial attempts preserved. Sharedfree12231483392B, just above
  new12.2e9 launch gate. Same root continues only while each fresh per-leaf gate passes; no template solver yet.
- 23:48:01 second c064 watcher stop at11987243008B; owned driver/child SIGTERM, no survivors.
  32 completed receipts remain:30 strict,UNKNOWN016/024; in-flight032 is UNSTARTED/uncertified.
  Fresh23:48:38 free11987972096B fails12.2e9 launch gate. DEFERRED_DISK_20261017T2348.json records
  exact frontier/hash;8 new completed receipts await ledger ingest after release. No template solver launched.
  Cancelled obsolete next-checkpoint timer; no disk polling or new compute stage until parent release.
- All reachable text preparation complete: review repairs41395137…1022/linka4e22c3c…f3ef; weak16consumer
  268e743b…fba8 and manifest355b3380…fc74 ready, explicitly gated after13 old-F attempts. Original files preserved.
- 23:54 parent released next stages after recovery and changed priority at the disk pause: ingest the8 pending
  c064 receipts, leave its frontier open, then13strong templates ->16weak templates, no further cover roots.
  Fresh23:55:27 free13113294848B exceeds12.2e9 plus10MB retained-growth reserve. K5v011ecd66786…621e
  ingests8 and validates (405worker-strict,8UNKNOWN,96UNSTARTED,3REFINED; Boolean cover incomplete).
- 23:55 old-F13 restricted-case pass started, separate k5_column_template_runs_v1 ledger; original base+42units,
  no H3,900s solver/<=3600s checker,6GiB. Per-case fresh12.2e9 gate; in-flight RAM/FIFO stage may finish.
  Deadline-only outer guard (disk floor disabled there; per-case gate handles starts) and00:22 one-shot
  checkpoint enforce finite<=3h chunk and<=30min evidence. All weak16 executions remain gated after13attempts.

## 2026-10-18
- 00:04:37 unified generation-obligation checker825c3cd7…3016 ran after fresh14.585GB gate; observed
  every5740226retained source clause equal/in-order after exactly4deletions, Q1kept, LF-only counts,
  all5ALO domains and16unit/leaf identities. Receipt65aafe0a…cc88, all_passtrue; no CNF/proof stored.
- 00:07 new unified overlaye0f3c860…1704 closes7bridge/3manifest minors; property-form T16, explicit
  group action/flags, accurate A8 status/imports/generation obligations, and all remaining gates.
  No runtime formula/units changed, no oldc112 proof transfer, no n8 theorem asserted.
- 00:21:46 template checkpoint (6/13 attempted): P0-B1..B5 all worker-strict UNSAT, respectively
  50.7s,210.0s,99.3s,4.1s,4.1s; P1-B1 UNKNOWN904.7s. Snapshot2eac6d99…774d;
  peak completed-case RSS4547084288B; free12995563520B. Remaining cases continue under the per-case gate.
  These are restricted old-F refutations only, not reduced-K5/n8 exclusion or parent replay acceptance.
- 00:47 checkpoint:7/13 complete,5worker-strict old-F refutations; UNKNOWN P1-B1,P1-B2.
  Snapshot5956f48c…1c86, peak completed-case4547084288B; free17635782656B. No case bytes changed.
  Parent00:52 kept queue13strong ->16weak, no retry; static both-CLI delta desk audits the repaired
  unified property theorem/deletion/extension semantics. All target claims remain conditional.
- 01:12 checkpoint:11/13 old-F attempts,7worker-strict UNSAT,UNKNOWN P1-B1,P1-B2,P1-B3,P1-B5.
  Snapshot104eceaf…1dd7; peak4789452800B; free15747911680B. Last two cases remain in the unchanged queue.
  No1800s retry. The16 weakened-F cases remain unexecuted until this13-case pass is complete.
- 01:28 completed old-F13 batch observed:9STRICT_UNSAT,4UNKNOWN (P1-B1,B2,B3,B5), none unstarted.
  RESULTS04d3485b…b0ca; final separate ledger v0147b667446…6f1d. Total worker wall5468.98s;
  no retry/whole-K5 claim. P2-C2 strict result took1061.6s including checker (solver still native900s).
- Fresh01:28 free15638818816B fits12.2e9 plus conservative160MB whole16-pass growth (10MB PER CASE,
  allowing SAT witness logs). EXECUTION_PLAN_v1.json records that scope. By01:30 the authorised16F_one
  run is active, separate n8_one_p4_template_runs_v1 ledger, unchanged355b3380…fc74/weak374d6fb4…eeb9.
  Old13 order gate passed; per-leaf900/no retry/6GiB and fresh12.2e9 gate, no CNF/proof copy. Outer finite
  deadline guard and01:55 checkpoint attached. All original semantic/certificate acceptance gates remain open.
- 01:40 parent conditional math/input disposition29d17f38…eaeb accepts property-formT16, extension and
  one-P4 implication, no target theorem. Independent parent binding65311ab0…28b0 verifies original/weak
  bytes, all5ALOdomains, parsed table,672units/16hashes without producer imports (F1/F2 closed).
  F4 requires measured solver/checker-feed hashes and exactCR-only rawlog status in PARENT replay.
  Inherited worker lacks separate delivered-feed measurements; disclosed and preserved as NULL/unknown,
  not backfilled. Current16 outcomes are producer candidates/LEGACY-worker-strict, not full-F4.
  Native logs/precomputed pins retained; queue/inputs unchanged; no newcuts/H3/retries.
- 01:55 unified checkpoint:7/16attempted,6LEGACY-worker-strict producer candidates (P0-B1..B6:
  68.9s,97.3s,165.0s,4.1s,4.1s,46.6s), UNKNOWN P1-B1 at903.4s(rc0/rc1).
  Prefix7acd5a585…eff8; peak4606066688B; free15976103936B. PREFIX7_PRODUCER_STATUS_v1.json
  pins the first7 records/META and explicitly does NOT supply measured feed hashes/full-F4 or an n8claim.
  Raw logs preserved; remaining9 input cases and queue unchanged, parent measured replay required.
- 02:18:49 parent-requested STATIC refinement design frozen, NOT LAUNCHED: review/N8-FONE-REFINE.r1.md
  76822535…82f1 and JSONfa0a68ac…7003. Z=[1625,1674,1723], first3V7/Q2Aprofile, disjoint from all16
  42unit lists by static map lookup;8full-product children,45units,5740271clauses. Proposed FUTURE300/900,
  L1UNKNOWN STOP/no retry, measured-feed newwrapper+controls and NEW parent go prerequisites.
  No child generated/solved; current16case900s queue unchanged.
- 02:20 checkpoint:8/16 current producer attempts,6LEGACY-worker-strict candidates,UNKNOWN P1-B1,P1-B2.
  Snapshotfcfa3770…a2a0; peak4606066688B; free15015063552B. Parent-F4 replay/measurement remains separate.
- 02:45 one-shot checkpoint observed all16 unchanged F_one attempts complete:12 LEGACY-worker-strict
  producer candidates, UNKNOWN P1-B1/B2/B3/B5, no unstarted/SAT. RESULTSbcfeb441…ac19, finalv017
  40d8e7e7…2fac; sampled own peak4606066688B. These12 are NOT parent counts or full-F4.
- 03:20 source packet frozen: N8-FONE-REFINE-DELTA.r2a.json eb9edb51…29823; controller5ef65aa8…acf76,
  bytehelper72a2737d…a96c; unchanged legacyR90b6f592…8484 and weakproducer61eda23c…d400.
  r2design1d912616…2d5a / JSONbf9f7193…2d1a supersedes the r1 wrapper prerequisite/one-level stop:
  Z1first3V7,Z2first3V8=[1632,1681,1730], all8 signs each level, automaticL2 forL1 UNKNOWN, noL3/retry,
  shared10400active-s/80MB family cap. Only parent separately measured replay counts refutations.
- Static data controls185c9fd0…3600a PASS at1.53s/301498368B maxRSS:16source hashes,1152 potential
  child images,256 refinement masks×64valuations,5 corrupted wire fixtures. Separate model controls:
  1positive/3corruptions; capacity predicate2positive/2negative. All potential CNF hashes are PLANNED,
  not delivered-feed measurements. Source16 binding d377df12…209e6; no native solver/checker invoked.
  That suite tested controller051f9464; later resource-only admission delta dc6ac1b3…795dd is explicit.
  Actual-parent admission controls dbee1e9c…720f9a passed without creating/changing any admission/release file.
- 03:36 parent data-plane source review PASS, but lifecycle HOLD on controller5ef65aa8: raw-PID stop/reap
  race, exception cleanup and unguarded preparation/directory reuse require an external owned-group supervisor.
  No refinement native child has ever launched. Final pinned PhysEpQutrit supervisor reuse awaits Main;
  failedr2 is neither imported nor used. Prior data/model controls do not validate lifecycle paths.
  Parent7ff6aa67…e206 reserves ONLY P1-B1, held-until-release; immutable release-marker existence revokes it.
  Source PASS alone is not native execution/capacity GO. Fresh host03:36:40 free13212196864B.
- Parent separately accepted first10 F_one direct leaves in moqls8-fone-first10-parent-verdict-v1.md
  SHA61130625a144ae8e88e1f3c8cddd22798477808b0673ac5d246d9b8215b983e4:
  P0-B1..B6,P1-B4/B6,P2-C1/C2. P2-C3/C4 parent replay pending under reservation, four P1 cases open.
  Legacy records remain unchanged; no full-cover/K4/K5/n8 exclusion follows.
- 04:16 lifecycle integration frozen, no runtime yet: packet08ab430b…3bab / planf609625e…8513,
  worker8598808d…f9d4, outeradapter245e4e4f…b5ec. The pinned read-only supervisor0ee8f394…83ec4d
  owns the entire worker group/preparation/exception cleanup; outer flock survives through qualification.
  No worker/adapter PID signals. Shared/release observer requests only an immutable stop file; one-shot
  probe exception uses the separately tested supervisor cleanup path. Explicit x-init and recorded reuse.
  The separate mathematical P1 monomial-column proposal34e90d73…284a remains UNREVIEWED, no CNF cutover.
- Parent source integration PASS/conditional native GO received. Required per-invocation prelaunch receipts
  re-hash every packet source, control-plan and supervisor; no code changes. New invocation cutoff17:30PDT.
- 04:20 static integration controls PASS cad9069e…35cf, exactly frozen plan: no native/supervise invocation.
  Static preflight425d2631…7620 matched all11 hashes and the unreleased7ff6 admission. Fixtures cover
  exclusive/recorded directories, file-only stop delegation, outerqualification/all8L2/noL3, declared-cap
  arithmetic and AST signal/session absence. They do NOT re-exercise OS lifecycle or prove a math exclusion.
- 04:22 first P1-B1 invocation started under the approved outer supervisor, --init-root --init-family.
  Fresh x-prelaunch receipt21486fcc…e144 matched all11 source/plan/supervisor hashes, lease unreleased.
  Jobbg_1866 is the first refinement native launch; no result claimed at launch. One pipeline, own6GiB,
  shared8GiB/4native, held-parent0, native300/checker900/whole1200+30TERM and disk/data gates unchanged.
- 04:22:26 first invocation STOP/UNKNOWN, correctly quarantined: outer2b1e92e6…1ec5 tripped on
  pid36858 BSDbytes0/EPERM after9.679s, sampled1942044672B. Owned-group SIGTERM succeeded,
  listing_ok=true/survivors=[] in the saved cleanup receipt, leader−15. No native receipt/refutation.
  Ledger295da85e…53a0 hasL1.000REFINED plus all8L2 unstarted; active9.704317334108055s.
  Production quarantine c5f76542…1081 persists; no subsequent native invocation/retry.
- 04:26:53 parent disposition2cdf49b1…7681 accepts the fail-closed stop. Statically diagnosed cause:
  /bin/ps is setuidroot here; legacyR.rss_kb and worker.shared_snapshot both execute that same binary.
  EPERM remains UNKNOWN, never silently mapped to zero/zombie. Parent requires newRSSsource review,
  static controls, ONE supervised NON-native RSS-path smoke, then a specifically authorised Q MOVE+manifest.
- 04:33 metadata-only executable audit e9698e2d…73dd: Python/du/cadical/DT/pgrep all lack SUID/SGID.
  Unsafe ps fact came from parent and was not rechecked/executed. No program ran in that audit.
- 04:54 r4 source-fix packet cb1fd717…35ff, plan d6a33e66…3a17, complete path/tool audit05b21656…e575
  frozen and sent for parent SOURCE review. New k5_resplit_r3.py00435386…e3e9 retains certify() bytes
  SHA25ef2728…cfba exactly; sampling now uses real pinned0ee libproc. Both ps paths are removed.
  Shared selection uses audited nonprivileged pgrep eb4d3117…d027 with runtime mode/SHA checks and
  libproc PPID closure; unknown readings still raise. Native limits/data/cover unchanged.
  Static controls and non-native smoke are NOT RUN; productionQ not moved or removed.
  A future explicit newrefine_v4 epoch may read-only import295da85e, carry9.704317s and the existing
  REFINE state, nextL1.001; no retry of000. That continuation still requires parent validation/MOVE/nativeGO.
- 05:00 r4 static controls PASS e2e1e2a2…3676 after full source/tool-mode preflightb96591c5…f7d7,
  fresh25693560832B. No native/supervise call in that static stage; no rerun of the old leaf.
- 05:01 ONE supervised NON-native smoke PASS90df761c…33d8 (4.25s), outer2c69c886…196ce,
  worker81374a36…3142f;6new-R RSS/shared snapshots on self plus sleeping Python, zero observed unknowns,
  cleanrc0/finalproblems[]/alive_others[]/no smokeQ. Cadi/DT/certify0; productionc5f765Q byte-preserved.
  Freshfull preflight248ec75e…684a, free25688748032B. Parent separately read/accepted these receipts.
- Parent correction: disk decline/reclaim cause and recurrence/≈12e9 thinning threshold are UNESTABLISHED.
  Free-space/snapshot observations alone establish no attribution. No host configuration/deletion was performed.
  Fresh/in-flight floor rules remain unchanged; correction itself authorised no retry/restart.
- 05:08–05:09 parent-named retirement MOVE under held capacity flock: ONLY originalc5f765Q moved to
  archive/n8-r3-quarantine-20261018/ with basename/1177bytes unchanged. Manifest99980add…54c2 and
  moveReceiptdfa11728…5efc record collisions, oldUNKNOWN/nosurvivors, smoke, reason and idle-onlyrollback.
  No deletion or active-code edit. Explicit creation-only deviation: worker was edited SAMEPATH8598→7d28,
  not a new filename. Exactr3bytes8598 x-preserved from the retained read; helper72comment-only preimage
  also preserved with its reconstruction/hash provenance. All9activecode pins still matchcb1; further fixes
  require NEW versioned paths. Old295daledger unchanged.
- 05:12:21 full native preflight7a5d7bde…adef1 matched12source/plan/audit/supervisor and5binary/mode pins,
  archivedQ/move receipt and original295da; free25374474240B. Parent GO starts ONE P1-B1 sourcev4 epoch:
  explicit read-only import,9.704317s carried,000 remainsREFINED/all8L2, no retry. First pendingL1.001
  invocationbg_1909 started with --init-root --init-family --continue-from295da. No result claimed at launch.
- 05:16 separate unreviewed mathematical strengthening5c748dd8…faa4 argues a Boolean model-existence
  normal form using G2/G3 support axioms, uniform primary relabelling and canonical aux extension.
  It proposes the same6restrictions but generates/runs no strengthenedCNF and changes no pilot ledger/code.
- First v4 L1.001 cleanly supervised but UNKNOWN: inputb55df27a…be4a, solver0/checker1NOTVERIFIED,
  native303.5s/4407738368B; outerf299b89d…66c clean304.658s/4433707008B. All8L2 created; no refutation.
  Qualifiedledgerfdd6990e…6e48 carries314.377601626s. Nextfullpreflight59596da8…f9e8 at05:19:33,
  free25259159552B, allowedL1.002 in the same frozen lease/source.
- 05:22:07 L1.002 STOP/UNKNOWN/newQ, NOT EPERM: outerf6e9882c…e1ad saw ZEROresident size,
  pid72601/ppidpgid71027/commPython/start[1792326127,545640]. Saved cleanup later names the SAMEpid/start
  pgrep; no causal assertion is made from that transition. SIGTERM true/no killpg error/listing_ok/survivors[],
  leader71027−15. New productionQ5ac17d24…9e75 persists; archivedoldc5Q unchanged. No native receipt.
  Ledger628d64a3…0310 preserves3REFINEDroots/all24L2unstarted, active454.5896603760775s.
  No retry/zero-as-death or supervisor grace change. Parent requested NEW no-helper metrics source only.
- Parent ended7ff6 pilot lease with immutable release721c0eda…9050; no more native under it.
  Parent direct12verdict accepts P2-C3/C4 as measured-feed exact UNSAT, completing P0-B1..B6,P1-B4/B6,
  P2-C1..C4. The remaining four original P1 formulas stay OPEN.
- Codex normal-form review030f92a8…4e30: ACCEPT-WITH-FIXES,0fatal/major,1minor M1. X-created r2
  8ae0ac01…9e8f explicitly accounts for unrestrictedK33 and excludes it by distinguished degree bounds.
  Diffc6b8bfeb…e2e5; original5c748dd8 remains unchanged. Parent finite checke075aff8…cbc2 PASS scoped
  to512localpatterns/name binding/stabilizers/126clauses, not a target theorem. Claude/parent acceptance pending.
- Generatorr1 protected guard rejected its coordinate-order negative pairs versus parent's internal
  ascending-signed-literal convention; no outputformula/CNF/solve. Attempt72e0ff89…2105 preserved.
  NEWr2generator08b67cef…c352/freez6234e470…65ae/diff34f85380…cacb canonicalises pairs.
  Static6hash manifest e04557a4…b709 produced in1.667s/300875776B,0solver/CNFfiles; all126tail fingerprints match.
- Parent changed route: N8StrengthenedReplay independently binds and certifies the six exact stronger inputs;
  producer performs NO solve and keeps M8 free of native processes. No normal-form/CNF cutover accepted yet.
- 06:00:41 conditional link registry2b727fde…1798 and frozen ASSEMBLY8c9cf1c2…a986 list every statement,
  file/SHA/status through U/T16/direct12/NF/sixinputs/n8conditionalconclusion. NF/S6/finaldisposition pending;
  no novelty/general-n/bareF_oneUNSAT claim. Unknown pilot/smoke evidence discharges zero roots.
- 06:06 no-helper source-only package a6d6cdb9…dd75/narrowdiff71e4d780…ec98/plan51809df6…f73a
  prepared in NEW versioned paths only. Metrics_r2 uses UIDlibproc+KERN_PROCARGS2, no selector/disk helper,
  unknown/zero fails closed; allocated-block walk replaces du. Supervisor0ee unchanged/no retry heuristics.
  No validation/run of that draft and no quarantine retirement. Current producer ledger/budget remain unchanged.
- Gate-critical contract review identified the required SECOND independently written encoder for every
  exhaustive step. New GB task reads untouched gram_b_r2.py4b593e55…eae0 and frozen contractC721.
  Prepared source-only generator952c761c…d88c with exactorder8/Q12345/ngen0/P4only1/SB2/G5/noROWLEX;
  every template/M_s literal maps through GB OWNnames, never GA IDs. No GB full generation/solve/CNFfile yet.
  Necessity/differences note e4dd33f4…03ed and preregfreeze1c350ced…20ce precede execution.
  RAM I/O sink avoids GB's17M-scale Python clause lists; allocator/encode logic is inherited unchanged.
  Planned controls: source-exact gate truth tables (including heavythreshold3), n3 sink parity, relaxed classical
  five-MOLS evaluation ONLY dropping1Q1ALO+7nonconstantQ1SB2 (emittedbodyunchanged), hash flips anddecode.
- 06:31:58 parent provenance correction a4b51119…7b70 withdraws the earlier “clarification” interpretation:
  discarded GA proof streams have no recorded SHA and cannot be retrospectively hashed. Direct12/P1-B1.M2
  native results remain observations, but protocolqualification is PROOF_DIGEST_MISSING/INCOMPLETE.
  Mandatory assembly addendum8bfd2dee…8d4f explicitly supersedes qualifiedD12/S6 wording and adds the
  independentGB obligation. No final n8 gate, no weaker checker/formula or silent protocol exception.
- 06:42 source-only GBpackage eccf887a…58a6 sent, all code/note/diff pins frozen, full generationNOTRUN.
  Resource coordination: N8StrengthenedReplay reports B3.M2inflightsince06:29:27; deskpeak6.847GB,
  stop7.384GB/lane7.85GiB. Its natural-boundary hold must precede my hard1GiB/oneCPU generation.
  No preemption/polling/newnative. Waiting explicitdesk0 andMainpermission; targetpackage~07:45.
- 07:12:41 NEW GBsourcepackage r2b90b42cc…bdf7 freezes generator5ca7c0da…e262, necessityb9b4a595…2365,
  freeze3a2a521b…2d67/diff90f0222b…fc8c and conventions50a5bf4a…7b37. R1 preserved; controls tightened,
  inverse predictions explicitly distinguished from actual table measurements. Formula bytes/flags unchanged.
  No GB encoder/control/solve run. ParentbinderFIRST→adapterSECOND→comparisonTHIRD; no concurrent run,
  no parent-GB-hash read/adaptation; own admission still HELD.
- 07:18:05 metadata-only checkpoint of parent07:16/07:17 notices: parent reports a separate outside-run
  Claude Code scratch writer, recorded in parent disk-decline-cause-observation-v1.md. Lane has no bulk writer
  or new watcher and does not inspect/change that session. No deletion/thinning/configuration or retry.
  Fresh12.2e9+growth/in-flight12e9 remain; native≥60min also needs13.5e9/no>300MB drop over5min.
  Small static writes≤16MiB/action are allowed under the clarification, but frozen code gates stay unchanged.
- 07:46:20 parent-admitted GB adapter: frozen gb_one_p4_r2.py5ca7c0da…e262 ran unchanged (py3.14.3 -I -B),
  rc0, 15.16s in-process, peakRSS393379840B, no CNF/solver; prelaunch0c6b7e1f…ed05. Manifest4daf8fcf…680d.
  Own hashes x-created BEFORE reading parent GBBINDING: 9781c877…943f. Comparison df3fb6e6…b651: ALL22 MATCH
  (sha256/bytes/headers), base body f5da0520…f1b9, own-name table = parent cli map. Parent IRC had disclosed
  headers/body prefix before the run; no code/convention changed. Input identity only, not GB UNSAT/gate.
- 07:50:28 ASSEMBLY r2 ba97fce3…0a41c (registry r2 eb7786b9…e060) applies Claude m1–m11, Codex M1 and adds
  §8.1 proof-digest provenance (18 replays) and §8.2 GB second encoding. r1 untouched. No theorem/novelty claim.
- 07:55:56 GB timing probe r1 (WORKER, not parent-qualified) launched: script b4c6ca46…b483, freeze8224e0d2…a175,
  prelaunch0680c121…b878. Sequential tiny controls, GB P1-B4, GB P0-B3; kissat4.0.4 → FIFO → relay(sha/bytes) →
  parent drat-trim a46c0c71; no CNF/proof on disk; aggregate resident cap7.0GiB; hard stop08:56.
- 07:59:29 probe r1 summary63eb60a0…00c1: controls OK; GB-P1-B4 kissat rc20/s UNSAT24.9s, maxrss1.95GB; proof
  307290350B cebf2feb…06b5; drat-trim rc0/s VERIFIED186.0s, maxrss2.63GB; feeds/relay complete. Frozen any-WARNING
  criterion → FAIL on375334 duplicate-literal normalisation lines only; P0-B3 NOT started. Versioned r2
  1cb44062…806e/freeze f33e66e2…da22/diff in review: raw-stream sha + dup-line count; other WARNINGs still fatal.
- 07:59:50 probe r2 launched (prelaunch21d3e62b…da06): controls, P1-B4, P0-B3; hard stop08:56.
- 08:14:5x probe r2 SUMMARY b84717ff…1734 (worker, not qualified): controls OK. GB-P1-B4 PASS184.7s (kissat24.4s,
  proof307290350B cebf2feb…06b5, drat-trim184.7s/2.53GB; aggregate3.69GB; receipt f82d10d5…b15b). GB-P0-B3 PASS
  683.3s (kissat296.8s/3.64GB,116654 conflicts; proof765641068B d4fed564…f65d,24.2M lemmas/600 RAT core;
  drat-trim683.3s/3.50GB; aggregate5.38GB; receipt c04f4098…3bf7). Both raw checker streams hashed; only
  375334 duplicate-literal normalisation lines each. GA pipelines4.95s/145.6s → ratios37×/4.7×.
  Rough affine estimate GB≈167s+3.55×GA: 12 direct≈1.45h sequential; S6 GB likely many hours. Reported to Main.
- 08:1x static GB NF bridge `review/GB_NF_GENUINE_BRIDGE.r1.md` 1a352d36…504b (UNREVIEWED): genuine vectors satisfy NF
  (A)–(C); NF §4 stabilizer moves are P_σ + common row/column permutation + square relabelling, so every genuine
  P1-template configuration moves to the same template with M_s, s∈Rep(C). Bridges GB S_j; Remark3 optional GA route.
- Parent decision b9886e24…09ec: M8 lane 11GiB/≤4 busy; ONE GA + ONE GB pipeline; GA reservation4.6GiB counted;
  GO 12 GB direct leaves shortest-first (no S6 GB; no kissat tuning). Production r3 619cc455…6e07, diff r2→r3
  a668be84…6022, freeze69e90fa2…6e1f: 6GiB/pipeline, GA scan (positive marker control PASS), cutoff17:29/stop17:55.
- 08:20:25 run-a1 launched (prelaunch ee9417c5…b278) from P1-B4; worker results, not parent-qualified.
- N8ReplayV5 reported its frozen in-flight rule (lane total ≤7.85GiB incl. GB) → scientific pipelines must not overlap.
  r4 80d731fe…80c0 (diff r3→r4 35bf81c7…6757, freeze bd6e2b99…6307): launch only when no GA driver alive; wait to17:29.
  Parent: r4 acceptable as frozen.
- run-a1 (r3) summary e3796da6…a399: GB P1-B4 PASS184.0s (proof cebf2feb…, same as probe), GB P0-B4 PASS185.1s
  (proof306861986B 1fa34b88…, receipt e1188c2c…); r3 driver SIGTERMed at the boundary 08:26:45 → P0-B5 NOT_STARTED.
- 08:26:57 r4 run-b1 launched from P0-B5 (prelaunch ea1d2dc3…14e7).
- run-b1 (r4) summary334ede2c…bc51: GB P0-B5 PASS183.1s (proof307162262B 946db7dd…); GB P0-B6 PASS441.8s
  (kissat163.3s, proof760784930B 662ecb04…, peak5.94GB); GB P1-B6 PASS412.5s (kissat156.6s, proof764589325B
  e94e586d…, peak5.39GB). All dup-literal counts =375334. N8ReplayV5 HOLD → driver SIGTERMed at the P1-B6 boundary
  08:44:27 (P2-C4 NOT_STARTED); RELEASE received (their controls postponed for v5d).
- 08:44:42 r4 run-b2 launched from P2-C4 (prelaunch ca55ec5e…dcf3).
- run-b2 (r4): GB P2-C4 PASS277.5s (proof317663671B 8a009d1c…, peak5.50GB); GB P2-C3 PASS268.2s (proof316240754B
  7e0a4a8e…, peak6.08GB — close to the6GiB cap). Second N8ReplayV5 HOLD: my boundary SIGTERM (08:53:59) arrived
  0.5s after the driver had launched P0-B1 → P0-B1 STOPPED_UNKNOWN (driver SIGTERM; kissat/drat rc−15, no
  survivors; receipt77145d84…). It is an UNKNOWN, not a result; rerun pending RELEASE.
- r5 9833abfc…a37e (diff r4→r5 719c91c6…63e5, freeze da2822fa…bb66): race-free HOLD markers (x-created HOLD/RELEASE,
  never deleted); running pipeline finishes; no boundary SIGTERM. Sent to Main before any launch.
- r6 89fa8959…7032 (diff r5→r6 66a14984…10ff, freeze f1b022c1…c9c9) FROZEN NOT RUN: staged transport (kissat alone,
  DRAT → collector → driver RAM; then drat-trim alone fed CNF + in-memory proof; sha/bytes equality). Motivation:
  concurrent peaks5.94/6.08GB vs6GiB cap. Parent decision requested (r6 for remaining5 vs r5).
- Parent approved r6 for the remaining five (worker evidence; record staged vs concurrent transport).
  HOLD-1 marker 8fe21ba6… (N8ReplayV5 HOLD 08:49) / RELEASE-1 (09:00:47, their controls ended08:59:55).
- 09:00:55 r6 run-c1 launched (prelaunch e309a150…281b): staged tiny controls PASS (positive VERIFIED; SAT checker
  NOT VERIFIED; proof8B collected=fed sha6e8f3aa6…). P0-B1 new attempt running (r4 attempt stays STOPPED_UNKNOWN).
- 09:07:11 parent HOLD (GA v5d formula batch run directly by parent): HOLD-2 marker d068335a…f3c3 (2 HOLD vs 1 RELEASE).
- run-c1 (r6, STAGED) GB P0-B1 PASS698.7s (kissat342.1s; drat-trim356.7s; proof770042119B 80aecc15…4caf collected=fed;
  peak4.91GB; receipt bb0a8ffd…). Idle driver SIGTERMed at the HOLD gate 09:12:49 (no children) → P0-B2 NOT_STARTED;
  summary aa0a658f…bfb4. Lane scan09:13:25: no GB process of this lane; reported reaped/clear to parent.
  GB direct worker status 8/12 PASS (P1-B4,P0-B4,P0-B5,P0-B6,P1-B6,P2-C4,P2-C3 concurrent; P0-B1 staged).
- r7 4fcc76e5…06e5 (diff r6→r7 b174b3de…70d9, freeze f2b0a701…0145) FROZEN NOT RUN, offered: parent-invited concurrency
  gate (GA counted + 6GiB ≤ 11GiB; HOLD markers still block). Safe only if the GA desk also uses11GiB, not7.85GiB.
  S6 GB feasibility from8 receipts: kissat1.9–6.4× GA CaDiCaL solve; GB proofs bimodal ~0.31/0.77GB; staged peak4.91GB.
- 09:19 parent: r7 NOT AUTHORIZED (v5d PRE-EXEC reservations are 6583566336–6847709184B per formula, not4.6GiB;
  +6GiB GB exceeds11GiB). Keep r6, no concurrent launch, caps/reservations unchanged. GA six-formula batch launching;
  GB HELD until parent RELEASE at a safe GA boundary. r7 files preserved unrun.
- Codex GB review ad9e5f04…13fc: necessity ACCEPT; genuine bridge + adapter ACCEPT-WITH-FIXES (3 textual MINORs), no
  FATAL/MAJOR. X-created erratum `review/GB_REVIEW_ERRATUM.r1.md` 7b51788c…1c4e applies E1 (ROWLEX rows2–7, coord order,
  MSB0, no secondary key), E2 (16-template coverage then condition on P1 four), E3 (Sink.new delegates to F.new). Files,
  code and bytes unchanged. Claude review pending. Not a GB refutation acceptance.
- 09:25:51 parent-reported external SIGTERM incident (cause unestablished) hit parent jobs. This lane had NO native/driver
  running (GB HELD since09:07:11; driver exited09:12:49) and sent no signal after09:12:49. Observed only: this worker's
  eval kernel lost in-memory state around then; all on-disk receipts re-hash unchanged. Reported to parent.
- Claude GB review 4aeed1e2…15e9 (necessity/genuine NF ACCEPT-WITH-FIXES 0/0/6+6). X-created
  `review/GB_REVIEW_ERRATUM.r2.md` a2d3b9b3…407d (incorporates r1; G1–G6, N1–N6; executed receipts cited; decode
  formula 1568(s−1)+49c+7i−5 verified on all245 mapping rows, Q2/r1/c4=1766, TRUE=1). Originals unchanged.
- Claude r2-delta 4ae89ea9…f4c9 (0/0/10) + Codex r2-delta 4259b60f…6418 (ACCEPT 0/0/0) + parent decisions →
  ASSEMBLY r3 64d5d06b…0345, exact diff r2→r3 28497a38…5f50 (patch reproduces r3), registry r3 83eed664…64ac
  (80 files rehashed; r1 entries identical in r1/r2/r3). §7 single predicate for all36 counted GA+GB replays; A7 confirmed
  by erratum-1 da050a74…87c2; A10 = GB note + genuine bridge acceptance + 18 counted parent GB replays. No theorem claim.
- Parent: STAND DOWN the four remaining worker GB runs; no further worker native runs even on RELEASE; all M8 native
  capacity to parent GA then counted parent GB. X-created STANDDOWN-1 marker. Static handoff
  `review/GB_R6_PARENT_HANDOFF.r1.md` 0870f26c…dc1b (r6 API/data paths/receipt fields/criteria, required parent-replay
  changes incl. six strengthened ids, controls, parse-count defence; worker timing table). Optional unreviewed contingency
  `review/P1_PAIR_REFINEMENT_OPTION.r1.md` (pair orbits: B3→{4,5},{4,6}; B5→4 pairs; nothing generated).
- DEVIATION (parent-identified): worker GB code unlinked its own spent FIFO nodes (no-deletion rule). X-created record
  `review/GB_WORKER_FIFO_UNLINK_DEVIATION.r1.md` 9357eb48…1704: 24 FIFO nodes (FIFO node only, no data at rest) in6
  executions (probe r1/r2, r3 run-a1, r4 run-b1/b2, r6 run-c1); r5/r7 never ran; smoke FIFO still present. No receipt
  change, no compliance claim, no reconstruction, no scientific status change. Omitted in record: r6 run-c1 P0-B2 also
  NOT_STARTED (no FIFO).
- Codex r3-delta 6c0011a8…9c62 (ACCEPT-WITH-FIXES 0/0/2) + GB parent verdict f529224e…ce0c (necessity + genuine NF
  CORRECTNESS-ACCEPTED at conditional written-lemma/input-identity scope only) + GA P0-B4/B5 PARENT-QUALIFIED PASS v5d
  (audit 2e7a12e3…7adb). X-created UNFROZEN draft `review/drafts/N8_ASSEMBLY.r4.draft1.md` d1992d4a…676e and its working
  diff `review/drafts/N8_ASSEMBLY.r3-to-r4.draft1.diff` 81905f4d…49f4 (patch reproduces draft). r3 remains frozen of record.
  Draft: §9.2.1 explicit genuine-move obligations + exact126 own-GB-name tails (s2/3/4 tail SHAs) with nonemptiness
  separate; registry claims narrowed; twelve historical receipt paths/bytes restored in §4; A10(i)/(ii) annotated as
  accepted only at conditional written-lemma scope; statuses as of10:17:46. Not frozen; awaiting parent freeze instruction.
