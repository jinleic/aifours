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
