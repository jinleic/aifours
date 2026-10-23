# Lane info-2: existence of BTD(12,15;6,2,10;8,6)

Owner: worker `InfoCyclic100`. Contract (read-only): `institute/runs/six-lane-2026-10-16/screening/info-2-btd12-15-contract.json`
(recorded 2026-10-17 07:38:34 PDT). Lane opened 2026-10-17 07:43:31 PDT (host clock, `notes/lane-opened.txt`).
Deadline 2026-10-18 18:31:43 PDT. Only this lane is writable; every prior lane, review input and source is read-only
and is copied, never moved. Nothing is deleted or moved. Programs write only fresh paths with exclusive creation, and
no automatic cleanup is performed. The covering-sequence lane is closed and read-only. No novelty, priority or "first"
claim is made anywhere in this lane; a literature miss is not novelty.

## 1. Frozen plan (written 2026-10-17 07:48-07:50 PDT, BEFORE any search in this lane)

### 1.1 Exact object (contract definitions)
* M is a 12 x 15 matrix (rows = the V = 12 elements, columns = the B = 15 blocks) with entries in {0, 1, 2}.
* (D1) every entry is 0, 1 or 2;
* (D2) every row contains exactly six 1s and exactly two 2s (so seven 0s and row sum R = 10);
* (D3) every column sums to K = 8;
* (D4) every two distinct rows i, k have inner product sum_j m_ij m_kj = Lambda = 6.
* Unrestricted: no automorphism, cyclicity, column-type, distinct-column, resolvability or orbit assumption. Repeated
  columns are ALLOWED (simple = no repeated blocks is an extra condition, Francel-Hurd p.5, layout lines 124-125).
* Equivalent Gram form: M M^T = 8I + 6J with the row compositions above. Row sums alone or the Gram matrix alone do not
  replace (D2).
* Necessary conditions hold: VR = 120 = BK; Lambda(V-1) = 66 = rho1(K-1) + 2 rho2(K-2) = 42 + 24; R = 6 + 2*2.

### 1.2 Sources (parent pins copied to `sources/parent-screen-*`, SHA-256 equal to the parent manifest)
* Rosin, arXiv:2501.17725v1, Table 1 (layout lines 92-106): "(12,15;6,2,10;8,6)?" listed among the Handbook's
  smallest open BTD instances, with no entry in the literature column [Greig, 2002] and none in the CPro1 column.
* Rosin, arXiv:2505.23881v1, Table 1(a) (layout lines 130-135): seven BTDs solved, not this one.
* Francel-Hurd, Australas. J. Combin. 42 (2008) 3-19, pp.3-5 (layout lines 33-40, 48-50, 63-69, 119-127): definition
  as multiset blocks, incidence matrix with row inner products Lambda, row sums R, column sums K; "simple" is extra.
* CPro1 definition file (`parent-screen-cpro1-btd-problem-def.py`, lines 15-16): the instance is in OPEN_INSTANCES.
  Its verifier is not imported or reused here.
* Bounded later-status check (07:44-07:47 PDT): two web searches ("balanced ternary design" BTD(12,15;6,2,10;8,6);
  balanced ternary designs open instances 2025 construction ...) found nothing later than the two Rosin papers.
  A miss is not novelty. The Handbook table itself was not accessed.

### 1.3 Representation and symmetry reductions (each with its completeness argument)
* (S0) Row 0 is 0^7 1^6 2^2 in this order. Complete: permuting columns of a solution gives a solution, and some
  column permutation sorts row 0.
* (S1) Double-lex. Compare entries by 0 < 1 < 2. Rows are lexicographically nondecreasing from top to bottom (each
  row read left to right). Columns are lexicographically nondecreasing from left to right (each column read top to
  bottom).
  * Completeness: (D1)-(D4) are invariant under row and column permutations, so the orbit of a solution under
    S_12 x S_15 is a finite set of solutions. Take the member whose row-major flattening is lexicographically
    smallest.
    * If rows r < r' had row r >lex row r', swapping them changes the flattening first inside row r, where it
      decreases.
    * If columns j < j' had column j >lex column j', let t be the first row where they differ. Rows above t are
      unchanged by the swap, and row t decreases at position j, its first changed position.
    * Either swap would give a smaller flattening, a contradiction. So the minimum satisfies (S1).
  * (S1) implies (S0): row 0 is nondecreasing because columns are lex-ordered by their first entry, and every row has
    composition 0^7 1^6 2^2.
* No other symmetry, ordering, partition or orbit assumption is used anywhere.

### 1.4 Implied constraints (proved here BEFORE use; used only in the "strengthened" variants)
Let G = M^T M (15 x 15) and let J be an all-ones matrix.
* M 1 = 10 1, because the row sums are 10.
* M^T 1 = 8 1, because the column sums are 8.
* By (D2) and (D4), M M^T = 8I + 6J.
* Hence G^2 = M^T (8I + 6J) M = 8G + 6 (M^T 1)(1^T M) = 8G + 384 J, and G J = J G = 80 J.

**Lemma P.** Q := I - G/8 + (3/5) J is symmetric and Q^2 = Q.
* Proof: Q^2 = I - G/4 + (6/5) J + G^2/64 - (3/40)(GJ + JG) + (9/25) J^2. Substituting gives
  I - G/4 + (6/5) J + G/8 + 6J - 12J + (27/5) J = I - G/8 + (3/5) J.
* Consequences, using only Q = Q^T = Q^2:
  * (P1) Q_jj = sum_k Q_jk^2 >= Q_jj^2, so 0 <= Q_jj <= 1.
  * (P2) Every 2x2 principal minor of Q is >= 0 (Q = Q^T Q is a Gram matrix), so Q_jk^2 <= Q_jj Q_kk.
* Column j with c_j twos has G_jj = (8 - 2c_j) + 4 c_j = 8 + 2c_j, so Q_jj = 3/5 - c_j/4. For j != k, with
  g_jk = G_jk the column inner product, Q_jk = 3/5 - g_jk/8.

**Corollaries** (exact integer arithmetic, below):
* (C1) [from P1] c_j <= 2 for every column: at most two 2s per column.
* (C2) [from C1] Since sum_j c_j = 24 over 15 columns, the number n_2 of columns with exactly two 2s is >= 9.
* (C3) [from P2] Two columns that both contain two 2s have inner product g in {4, 5}.
  * Proof: |24 - 5g| <= 4.
* (C4) [from P2] A column with two 2s and a column with one 2 have g in {4, 5, 6}.
  * Proof: (24 - 5g)^2 <= 4 · 14 = 56.

These are the only implied constraints. "Plain" variants use only (D1)-(D4) and the symmetry reductions of 1.3.

### 1.5 Witness format and checkers
* Strict format: line 1 is `BTD V B p1 p2 R K L` (decimal integers without leading zeros). Then exactly V lines,
  each with B space-separated entries from {0, 1, 2}, a final LF, no CR, nothing else. For the target:
  `BTD 12 15 6 2 10 8 6` plus 12 lines of 15 entries.
* `code/verify_btd.py`: stdlib only, definition-first. It checks the header, the dimensions and every condition
  (D1)-(D4), including every row's 1-count and 2-count separately and every one of the C(V,2) row pairs. Duplicate
  columns are reported separately and are not a rejection. Optional `--sha256` binding.
* `code/btd_check.c`: an independently written native checker of the same conditions and format, with no shared
  code.
* Controls (both checkers):
  * BTD(3,3;1,1,3;3,2) with rows (2,0,1), (1,2,0), (0,1,2) passes.
  * Francel-Hurd Figure 2 BTD(4;12;3,6,15;5;16) passes.
  * Two published CPro1 BTDs pass: Rosin 2505.23881v1 Figure 4 (16,22;9,1,11;8,5) and Rosin 2501.17725v1 Figure 20
    (12,16;4,4,12;9,8). Each is transcribed from the layout text and passes both checkers, or is reported as a
    transcription failure.
  * Intended-reason mutations: entry 3 (range); a row with a 1 changed to a 2 (row 1-count and 2-count); one entry
    moved within a row (column sum); swapped entries breaking a pair product; header/format mutations; and a
    duplicate-column positive.

### 1.6 Searches and proofs
* (W) CP-SAT witness model, `code/btd_cpsat.py`.
  * OR-Tools 9.15 (lane-local copy `tools/pydeps312`, from the read-only gcdcqs20 lane, run with the uv CPython
    3.12.12 and `PYTHONDONTWRITEBYTECODE=1`).
  * Model: Boolean one-hot cells, (D2) and (D3) as linear equalities, (D4) through Boolean products as linear
    equalities, symmetry (S0). The strengthened variant adds (C1).
  * Native limit `max_time_in_seconds`, `num_workers` <= 4. A CP-SAT INFEASIBLE is recorded as information only
    and is never an exclusion.
* (A) CNF encoding A, `code/btd_cnf_a.py` (Python stdlib).
  * Thermometer variables a_ij = [m_ij >= 1] and b_ij = [m_ij = 2], with b -> a.
  * Row: sum_j a_ij = 8 and sum_j b_ij = 2. Column: sum_i (a_ij + b_ij) = 8.
  * Pair (i, k): the count of true products among {a_ij a_kj, a_ij b_kj, b_ij a_kj, b_ij b_kj : j} is 6. This equals
    sum_j m_ij m_kj, since m = a + b.
  * Each product is a fully defined AND; every "exactly k" is a Sinz sequential counter.
  * Symmetry (S1) by lexicographic order on the interleaved thermometer sequences (order-preserving: 0 -> 00,
    1 -> 10, 2 -> 11), with "equal so far" variables.
  * Variant `--strengthen` adds (C1) as sum_i b_ij <= 2.
* (B) CNF encoding B, `code/btd_cnf_b.c` (C), written independently of A, sharing no code with it.
  * One-hot variables z_ij0, z_ij1, z_ij2 with exactly-one.
  * Unary-output totalizers (Bailleux-Boufkhad) for every count. The column weight uses the literal multiset
    {z_ij1, z_ij2, z_ij2}. The pair weight uses product literals with multiplicities 1 (1·1), 2 (1·2 and 2·1) and
    4 (2·2).
  * (S1) is encoded by its own lex scheme over the value order.
  * Optional `--strengthen` adds (C1).
* Solvers: kissat 4.0.4 and cadical 3.0.1 with native time limits and DRAT proofs (binary or ASCII). Proofs are
  checked by drat-trim (and LRAT by lrat-check). These checkers were copied from the parent's read-only
  `review/moqls7-parent-proofcheck-tools-v1` (upstream marijnheule/drat-trim commit 2e3b2dc0) and compiled in
  `bin/`. drat-trim runs with its native time limit. An interrupted proof check is UNKNOWN, never an exclusion.
* Encoding correctness controls, for A and B:
  * Small known BTDs (the controls in 1.5) give SAT, and the decoded matrix passes both checkers.
  * A known solution fixed as unit clauses (after (S1) normalisation) gives SAT.
  * The same solution with one entry changed gives UNSAT.
  * Exact agreement of the number of (S1)-normalised solutions between A, B and an independent stdlib brute-force
    enumerator, on tiny parameter sets where full enumeration is cheap.
* An exclusion claim requires both of:
  1. a complete encoding (A or B; plain preferred, strengthened only with Lemma P as written above) with a completed
     drat-trim/lrat-check VERIFIED UNSAT;
  2. either the other independently written encoding also UNSAT (checked), or a mathematical contradiction.
  A solver UNSAT without a completed check is UNKNOWN.
* Optional mathematical route, recorded as notes and never used as a search assumption: the structure of the rank-3
  projection Q (Lemma P) on the columns.

### 1.7 Run order, stop rules, resources
1. Checker controls (1.5).
2. Encoding controls (1.6).
3. W: CP-SAT witness search with (S0), plain and strengthened, at most 4 workers in total, <= 30 min each. In
   parallel within the 4-CPU cap: kissat on A-strengthened and A-plain (1 CPU each, `--time` <= 3600 s) with proof
   output.
4. On any solver UNSAT: check the proof with drat-trim, then run encoding B (and the other variant) for the second
   route.
5. Stop rule: on ANY witness from any search, stop all runs, verify it with both checkers, pin it under `certs/`
   with its SHA-256, and message Main immediately.
6. Resources:
   * <= 4 CPU processes (a CP-SAT worker counts as one CPU) and <= 8 GiB;
   * <= 10 GiB new lane data. DRAT files are size-checked at every checkpoint, and a run whose proof would exceed
     6 GiB is stopped with its native limit set from the measured growth;
   * checkpoints <= 30 min, chunks <= 3 h, initial cycle <= 3 h (to about 11:00 PDT);
   * thread variables = 1;
   * native limits or SIGTERM plus a bounded wait only; never SIGKILL or subprocess.run(timeout=...).
7. Outcomes:
   * witness: existence, after parent checking;
   * verified UNSAT under the 1.6 rule: nonexistence claim for the parent to check;
   * otherwise UNKNOWN, with a recorded obstruction and a changed representation before any further long run.

## 2. Status
(written below the freeze only; interim at 08:42 PDT, final update in Section 4)

* **Result candidate: BTD(12,15;6,2,10;8,6) does NOT exist.** This is a mathematical proof and is UNTRUSTED until
  the parent's verdict. No novelty, priority or significance claim is made.
  * r1, `notes/nonexistence-proof.md` (837a26ea…a7e5), 08:26. Parent reviews: Codex ACCEPT-WITH-FIXES (one minor),
    Claude ACCEPT.
  * r2, `notes/nonexistence-proof-r2.md` (37795ae7…5dc0), frozen 08:40:50. It is Steps 1-7 of r1 plus the reviewer's
    three-line closure. Lemma D (det of every 3x3 principal minor of H = 40I - 5M^TM + 24J is a perfect square)
    meets det H[{a,b,k}] = 210 - (4x^2 + 2xy + 4y^2), which takes the values -150, 50, 150 and 200.
  * Exact checkers: `code/proof_check.py` (r1, PASS) and `code/proof_check_r2.py` (r2, PASS).
  * Supporting Gram-level CP-SAT cross-check: INFEASIBLE with Lemma D, FEASIBLE without it.
* **No witness:** CP-SAT (S0 + (C1), 2 workers) UNKNOWN at 1800 s.
* **Independent SAT route** (plain encoding A or B: definition plus (S1) only, no proof-derived clauses):
  * A-plain level-1 kissat with binary DRAT is running under its native 3600 s limit;
  * B-plain level 1 was stopped at 190 s (UNKNOWN);
  * earlier no-proof runs on the (C1) variants were UNKNOWN at 1800 s.

  An exclusion from this route requires a completed drat-trim VERIFIED; otherwise it is UNKNOWN.
* **Supporting only (not independent; proof-derived clauses):** the level 2/3 runs (L2 stopped, L3 running under its
  native limit).

## 3. Log (host clock, PDT)
- 07:39:58 contract read (the parent message arrived after 07:38:34); 07:43:31 lane created.
- 07:44-07:47 bounded later-status check (1.2). Parent pins copied with SHA-256 equal to the manifest. drat-trim.c,
  lrat-check.c and upstream-commit.json copied from the parent tools pin (SHA-256 d834b649…c2ee, bf07c2ac…8a95).
  `tools/pydeps312` copied (132 MB, OR-Tools 9.15.6755). Import test only, no search.
- 07:48 bin/drat-trim and bin/lrat-check compiled (cc -O2).
- Before writing 1.4 and 1.6: pen-and-paper analysis of Lemma P only. No computation has been run on the target.
- 07:50:19 freeze receipt (`notes/freeze-receipt.txt`, README SHA-256 72ddcfb5…c4cb). The 1.0 heading first carried a
  placeholder time "08:0x"; it was replaced by the host-clock "07:50" BEFORE the receipt was written.
- 07:51:50 checker controls (`controls/checkers-v1/checker-controls.json`): CHECKER-CONTROLS PASS, 21/21 as intended.
  - Published designs pass both `verify_btd.py` and `bin/btd_check` (`code/btd_check.c`):
    - BTD(3,3;1,1,3;3,2), rows (2,0,1), (1,2,0), (0,1,2);
    - Francel-Hurd Fig. 2, BTD(4,12;3,6,15;5,16);
    - CPro1 2505 Fig. 4, BTD(16,22;9,1,11;8,5);
    - CPro1 2501 Fig. 20, BTD(12,16;4,4,12;9,8);
    - CPro1 2501 Fig. 19, BTD(14,21;6,3,12;8,6).

    These are transcribed by line range from the SHA-checked layout texts. In the layout text each caption follows
    its matrix.
  - A doubled tiny design with repeated columns passes, and the duplicates are reported.
  - Mutations fail for the intended reason: range, row-count, column-sum, pair-product, header R, and format
    (leading zero, missing LF, extra line, CR, double space, dropped row, tabs). Binding to wrong parameters and to a
    wrong SHA fails.
- 07:52:28-07:54:33 CP-SAT controls (`controls/cpsat-v1/`, 2 workers, 120 s):
  - (3,3;1,1,3;3,2), (4,12;3,6,15;5,16), (4,8;2,3,8;4,6) and (6,6;2,1,4;4,2) were solved in < 0.02 s, and each
    witness passes both checkers;
  - (12,16;4,4,12;9,8) was UNKNOWN at 120 s.

  `btd_cpsat.py` was then edited only to stop echoing the solver log to stdout (`log_to_stdout = False`); the
  current SHA-256 is 0e648550…e2cb, re-checked on (3,3;1,1,3;3,2) in `controls/cpsat-v2`.
- 07:55:36 W started: CP-SAT target, strengthened (C1), (S0), 2 workers, 1800 s, seed 0
  (`runs/cpsat-target-v1/strength-s0-w2-seed0.*`).
- 07:56:14-07:58:57 brute-force counts (`controls/brute-v1/`, `code/brute_count.py`, independent stdlib):
  - S1 counts for (3,3;1,1,3;3,2), (3,4;2,1,4;3,3), (3,6;2,2,6;3,4), (3,3;1,2,5;5,8), (5,5;1,2,5;5,4),
    (6,6;2,1,4;4,2), (4,8;2,3,8;4,6), (4,12;3,3,9;3,4), (5,10;2,4,10;5,8) =
    1, 1, 2, 1, 1, 3, 8, 11, 24;
  - with no symmetry / with S0 only, for the first four: 12/2, 48/4, 900/10, 6/2.
- 07:56:32-07:59:28 encoding A (`controls/encA-v1/`) and encoding B (`controls/encB-v1/`) enumerate exactly the same
  counts on every one of these instances (S1, S0 and no symmetry), by blocking-clause enumeration with cadical.
- 07:56:58 target CNFs A (`runs/encA-target-v1/`):
  - plain S1: 35687 vars, 133629 clauses, SHA-256 15337bc2…22c6;
  - strengthened S1: 136929 clauses, ffa867d9…37ca.

  07:57:00 kissat started on A-strengthened (no proof, `--time=1800`).
- 07:58:28-07:58:45: a fifth CPU-bound process ran briefly (the B count controls, while CP-SAT 2 + brute 1 + kissat 1
  were running). This was 17 s over the 4-process cap; no later overlap.
- 07:59:34-07:59:38 realistic-size controls (`controls/encfix-v1/fix-controls.json`): FIX-CONTROLS PASS.
  - Each published design (4x12, 12x16, 14x21, 16x22) was brought to double-lex form, fixed by unit clauses, and
    gives SAT in both A and B; the decoded matrix equals the input and passes `verify_btd.py`.
  - Changing one entry gives UNSAT in both encodings.
- 07:59:54 target CNFs B (`runs/encB-target-v1/`):
  - plain S1: 41039 vars, 244771 clauses, e9b80829…dbb8;
  - strengthened: 246691 clauses, 19176a91…53ac.

  07:59:55 kissat started on B-strengthened (no proof, 1800 s). CPU now 4 (CP-SAT 2, kissat 2).

## 1.8 Amendment (written 08:14:18 PDT, BEFORE any run of the variants below; sections 1.1-1.7 unchanged)
* Candidate mathematical contradiction: `notes/nonexistence-proof.md` (pen-and-paper, written between about 08:00 and
  08:13 while the first runs were going; file times are on disk).
  * It derives, from the definition alone, Lemma P / H = 40I - 5G + 24J (H^2 = 40H, PSD, rank 3) and the column-type
    counts.
  * Lemma D: every 3x3 principal minor of H has a perfect-square determinant, because
    det(N)^2 = 2^28 det H[S]/25 for the complementary 12 x 12 integer submatrix N.
  * From these: at most two classes of type-2 columns, so n_2 is 9 or 10, and a finite contradiction in both cases.
  * It is UNTRUSTED until parent review. `code/proof_check.py` re-checks every identity and the finite case analysis
    by exact rational arithmetic and exhaustive enumeration: Lemma D on random instances, all type-2 triple
    patterns, every n_2 in 9..12, every class split, all p-assignments, and both the rank-one and the finitary
    pairwise sign models.
* New encoding variants (target parameters only), `btd_cnf_a.py --lemmas 2|3`. They add implied clauses on
  column-pair inner products g_jk:
  * Level 2:
    * (C3) and (C4) (Step 2(b));
    * the type-2 column distribution of Step 4;
    * the class rule of Step 5.

    These need only H^2 = 40H, H **1** = 0 and positive semidefiniteness.
  * Level 3 adds Lemma D's consequence: no three type-2 columns with pairwise g = 5 (Steps 6-7).
  * The clause semantics are tested by `code/lemma_encoding_controls.py` against an independent reference evaluator,
    using the `--lemma-test` mode (D2-D4 omitted).
  * The default output of `btd_cnf_a.py` without the new options is unchanged. The clause bodies are byte-compared
    with the v1 outputs; v1 is archived in `archive/code/btd_cnf_a.v1.py`.
* Run plan after the four current runs end:
  * (a) proof_check;
  * (b) lemma controls;
  * (c) kissat on A-L3 and A-L2 with binary DRAT, `--time=3600`, proof size checked at every checkpoint;
  * (d) the current UNKNOWN plain/(C1) runs may be extended without proof (`--time` <= 10800) to learn whether they
    finish. A proof would then be produced by a deterministic re-run.
  * An UNSAT under level 2 or 3 is an exclusion only together with the written proofs of the lemmas it uses, and
    only after drat-trim VERIFIED. The level is always stated with the result.
* Stop rules and resources unchanged.

## 3b. Log continued (host clock, PDT)
- 08:25:36 W ended: CP-SAT target (strengthened (C1), S0, 2 workers, seed 0) UNKNOWN at 1800 s, 61486 conflicts.
  No witness. `runs/cpsat-target-v1/strength-s0-w2-seed0.json`.
- 08:26:00-08:26:01 `code/proof_check.py` (aacf1c5f…7f85) gave PROOF-CHECK PASS; receipt
  `evidence/proof-check-v1.json` (ca6a918b…57d3). Checks C1-C5:
  - n2 = 9, classes 5+4: 180 assignments satisfy the H row relations, all PSD with sum Y_kk = 40, and 0 survive the
    rank-one and the pairwise-finitary integrality models;
  - every other class split for n2 = 9..12: 0 row-relation solutions.
- 08:26:00-08:26:59 `code/lemma_encoding_controls.py` (`controls/lemma-v1/lemma-controls.json`): LEMMA-CONTROLS
  PASS. The encoding-A lemma clauses agree with an independent reference evaluator on 26 matrices at each level:
  - level 2: 12 SAT, 14 UNSAT;
  - level 3: 9 SAT, 17 UNSAT, including 3 searched matrices that are level-2 SAT and level-3 UNSAT.
- 08:26:18 candidate proof reported to Main: `notes/nonexistence-proof.md` sha256
  837a26eaaf76a0406a1701ab02ca2b4616abdec927eafc062dcc578a3ba9e7a5.
- 08:27:14 encoding-A generator v2 (4c898…570c82a; v1 archived). The plain and (C1) clause bodies are byte-identical
  to v1 (body sha256 f5a945f5… and b0d4eaa8…). New target CNFs `runs/encA-target-v2/`:
  - A-L2-S1: 308544 clauses, 1361dece…39be;
  - A-L3-S1: 308999 clauses, 20574272…d222.
- 08:27:31 kissat with binary DRAT started on A-L3 and A-L2, as supporting runs (`--time=3600`). 08:27:07 the
  A-(C1) no-proof run ended UNKNOWN at 1800 s (30.85M conflicts).
- Parent instruction, received between 08:27:51 and 08:28:44:
  - r1 of the proof note is frozen (any fix goes to a new r2 file);
  - first, the level-1 DRAT route: the plain encoding with S1 only and no implied clauses, kissat `--time` with
    binary DRAT, then drat-trim with native `-t`;
  - levels 2/3 only as labelled supporting runs;
  - an optional finite cross-check in a different style, keeping proof_check.py frozen.
- 08:29:44 A-L2 and A-L3 stopped by SIGTERM (graceful) to give level 1 priority and to save disk. Both UNKNOWN after
  about 130 s; partial proofs 167 MB and 157 MB are kept. 08:29:55 the B-(C1) no-proof run ended UNKNOWN at 1800 s.
- 08:30:26-08:30:27 DRAT pipeline control (`code/drat_pipeline.py`: kissat proof -> FIFO -> zstd -3;
  `controls/drat-pipeline-v1/`):
  - the 12x16 fixed design with one flipped entry is UNSAT, and `zstd -dc | bin/drat-trim CNF -i` reads the proof
    from stdin and prints "s VERIFIED";
  - the unflipped fixed design is SAT.
- 08:30:42 LEVEL 1 started, two runs into `runs/level1-drat-v1/`:
  - kissat `--time=3600` with binary DRAT through zstd on A-plain-S1 (15337bc2…22c6);
  - the same on B-plain-S1 (e9b80829…dbb8).
- Measured proof rate: about 1.3 MB/s compressed per run, 2.5 MB/s raw (B partial: 479,199,232 raw bytes in 190 s,
  compression about 1.9x). A one-hour proof would be about 4.8 GB compressed (9 GB raw) per run. That is within the
  disk cap for one run, but drat-trim keeps the whole proof in memory and would then exceed the 8 GiB memory cap.
- 08:33:52 B-plain level 1 stopped by SIGTERM to keep disk for A-plain: UNKNOWN at 189.7 s, partial proof 252094031
  bytes, sha256 e77418947c72ca82b055ca7b8146808f2ae0c4641ae1b3f4d772663cd839c78b (kept; not a certificate).
  Decision: A-plain level 1 runs until its compressed proof reaches about 1.3 GB (about 2.5 GB raw, about
  08:47 PDT), the largest size drat-trim can plausibly check within 8 GiB. If it has not finished by then, it is
  stopped and reported as UNKNOWN.
- 08:34 started, as supporting work: `code/gram_cpsat_crosscheck.py`, a CP-SAT search over the whole 15x15 integer
  matrix H (H1 = 0, H^2 = 40H, diagonal pattern, entries = -1 mod 5, 2x2 bounds), with and without Lemma D tables,
  300 s per split, 1 worker each. CPU: A-plain kissat, its zstd, 2 CP-SAT.
- 08:34:28-08:34:48 Gram cross-check (`runs/gram-crosscheck-v1/`, `code/gram_cpsat_crosscheck.py` v1 b9544f69…d2ce;
  supporting evidence only):
  - with Lemma D tables, all four splits are INFEASIBLE in presolve (0 conflicts);
  - without them, all four splits are FEASIBLE. The returned H satisfy H1 = 0 and H^2 = 40H exactly but violate
    Lemma D in 326, 266, 214 and 197 triples.

  So Lemma D is the essential obstruction at Gram level, consistent with the proof. The script later gained a
  `--diag-only` option (not run).
- 08:35:25 supporting level-3 run started: kissat `--time=3600` on A-L3-S1 through the DRAT pipeline
  (`runs/level3-drat-v1/`).
- 08:36:26 encoding B v2 compiled to the NEW binary `bin/btd_cnf_b_v2` (09333f01…4ebd); v1 source and binary
  archived. It adds the `-lemmas` and `-lemmatest` options. No CNF has been generated with it, and it is not used
  further: the parent asked for no more proof-derived levels.
- Parent message, received between 08:36:26 and 08:38:07: an exploratory lead for BTD(14,18;7,1,9;7,4). It is
  stored verbatim in `notes/parent-lead-btd14-18-received.txt`, as a note only; no work was done on it.
- Parent message, received between 08:38:07 and 08:38:43:
  - both reviews of r1 returned. Codex: ACCEPT-WITH-FIXES, one minor indexing point at r1 Step 8(i). Claude:
    ACCEPT, editorial minors, plus a short closure after Step 7;
  - freeze ONE r2 with the short closure and a nine-case table, keeping r1 untouched;
  - write a new exact checker;
  - start no more proof-derived SAT levels;
  - keep the already-started runs and their native limits.

  The plain encoding with a proof is the independent SAT route, and UNKNOWN is acceptable.

  Review notes read, read-only: `review/btd12-15-claude-complete-review-v1.note.md` (46ee1d00…0481) and
  `review/btd12-15-codex-hostile-review-v1.note.md` (64e10184…cb22).
- 08:40:00 `code/proof_check_r2.py` (5b3c77be…cb30) gave PROOF-CHECK-R2 PASS; receipt
  `evidence/proof-check-r2-v1.json` (8b3ce010…126b).
  - It checks with stdlib integers and Fraction only, no grid and no randomness: the Step 1 algebra; A·A^-1 = I and
    det A = 2^37·5; the Lemma D factor 2^28/25 (symbolic entry identity, plus 3 explicit P); c <= 2 and the four
    splits; the Step 4 multisets; the Step 5 values; det(5I - J) = 50; and the nine-case table.
  - The nine determinants are -150, 50, 50, 50, 200, 150, 50, 150, 50, none a nonnegative square. This agrees with
    my hand computation.
  - This run was a fifth process for under one second, beside 2 kissat and 2 zstd. The zstd processes are I/O-bound
    helpers.
- 08:40:50 r2 frozen: `notes/nonexistence-proof-r2.md` sha256
  37795ae73be939e38bb628c0e05cba5ed95aba6e89c9dad4c706a420e3725dc0 (receipt `notes/freeze-receipt-r2.txt`). r1 is
  unchanged (837a26ea…a7e5). Reported to Main at 08:41.
- 08:44 decision request to Main: Lean formalization of r2, and stopping the supporting A-L3 run.
- Parent approval received between 08:44 and 08:45:
  - SIGTERM to A-L3 only;
  - a bounded (<= 3 h) Lean 4 / Mathlib formalization of the full r2 in this lane, <= 2 CPU and 8 GiB (lane
    aggregate <= 4 CPU), read-only Mathlib cache, Lean 4.34.1;
  - forbidden: native_decide, ofReduceBool, sorry/admit, new axioms, oracles. Allowed final axioms: propext,
    Classical.choice, Quot.sound;
  - the root must state the explicit 12x15 ternary matrix nonexistence;
  - r2 and proof_check_r2.py stay frozen;
  - no BTD14 work.
- 08:45:05 A-L3 stopped by SIGTERM: UNKNOWN/INTERRUPTED at 579.5 s (kissat exit -15). The partial proof (415436607
  bytes compressed, sha256 fb07bb2fd4e98cc44256ef00a5f900b80bcf0b91c61471fa5d3b9257749848c0) and the logs are kept.
  This is not a certificate and never an UNSAT.
- 08:47 `lean-kernel/` created: `lean_env.sh` (same logic as the parent's mcdsqs38 one, with BTD_BUILD), and
  `build_module.sh` (fresh BTD_BUILD and BTD_LOGS per round; refuses an existing log).
- 08:48-08:56 development rounds `build-dev-01` .. `build-dev-11` on `BTDKernel/Dev.lean` (now retired to
  `lean-kernel/archive/Dev.lean`).
  - Round 11 compiles the whole proof with no error: H^2 = 40H, Cauchy-Schwarz on rows of H, the column-type
    counts, the class bound via sum_k (H_ak + 1)(H_ak + 6) = 250, Lemma D via `Matrix.det_one_sub_mul_comm` over Q
    with the explicit inverse of 8I + 6J, and the nine-case closure.
  - The only warnings are deprecations.
- 09:02:16 a stray `leanchecker --help` (pid 46600; it treats `--help` as a module name and waits) was ended with
  SIGTERM.
- 09:00-09:02 final modules `BTDKernel/{Target, Proof, Audit, Controls, ControlFail}.lean`, dev build round 12/13:
  - `#print axioms BTD12.Audit.root` gives [propext, Classical.choice, Quot.sound];
  - the controls accept BTD(3,3;1,1,3;3,2) and reject two mutations;
  - ControlFail fails as intended.
- 09:03:19 `lean-kernel/manifest.json` written (sha256 2318819c…771d), pinning the sources, scripts, lean and
  leanchecker binaries, and Mathlib.olean plus the four imported Mathlib oleans.
- 09:03:2x `lean-kernel/replay.py r01` started: clean rebuild into `replay-r01/`, then `leanchecker --fresh` on Audit
  and Controls.
- 09:03:27 checkpoint: A-plain level 1 at 1866 s has a 2.08 GB compressed proof. The lane uses 3.5 GB; the projected
  total is below 6 GB.
- 09:03:22-09:13:14 `lean-kernel/replay.py r01`: VERDICT PASS. `replay-r01/result.json` sha256
  4fccfacd1c9288ded9aaa295a7a021423d9e8c10f721c371daed757af414e493.
  - The pinned files match manifest.json (2318819c…771d), and `BTDKernel/` holds exactly the five pinned Lean files.
  - The source scan (byte-identical copy of the parent-lane scanner 8e9eb834…af5bb) passes its controls with no hit;
    `replay-r01/scan.json` ccb03a64…d935.
  - Target, Proof, Controls and Audit build with exit 0 and no error. Olean sha256 values: Target a490c455…c7f5,
    Proof 66546ee2…aca5c, Controls 2375904a…b918, Audit c56e87ca…bd34d. Peak RSS <= 3.11 GB; Proof took 11.2 s.
  - `#print axioms`:
    - BTD12.Audit.root, BTD12.Audit.root_statement and BTD12.lemmaD: [propext, Classical.choice, Quot.sound];
    - the controls: the same set.
  - The Audit log shows the explicit root statement: no 12x15 integer matrix with entries in {0,1,2}, row counts
    six 1s and two 2s, column sums 8, and distinct-row inner products 6.
  - The negative control ControlFail fails as intended: decide refutes the mutated matrix, norm_num fails on the
    D = 100 side condition, and no olean is written.
  - `leanchecker --fresh -v` exits 0 with the replay marker:
    - BTDKernel.Audit: 285.1 s, peak RSS 3.50 GB;
    - BTDKernel.Controls: 286.5 s.

    Both re-check the whole import closure, Mathlib included, in a fresh kernel environment.
