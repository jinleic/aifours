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
(written below the freeze only)

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
