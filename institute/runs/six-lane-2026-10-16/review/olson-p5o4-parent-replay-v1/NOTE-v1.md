# NOTE-v1: parent replay of worker claim C5' (ordered Olson, D_10, p = 5, four odd blocks): final

Desk: `review/olson-p5o4-parent-replay-v1/` (created with exist_ok=False at 08:33 PDT 2026-10-18). Written after host
clock 10:01:11 PDT 2026-10-18. This note covers only correctness. It makes no novelty claim.
Machine-readable companion: `RESULT-v1.json`, which pins this note and every desk file. The primary deliverable
published earlier is `RESULT-primary-v1.json` (7dfe21eb…b911) with `NOTE-primary-v1.md` (844575b6…234f). This note
supersedes it only by adding the completed route 2.

**Verdict: CONFIRMED.** Every avoider in D has all its rotation letters in one {rho_c, rho_-c}, c != 0. Two routes give
this result:
- **Route 1** (own proved filter (d) plus the ordered DP) covers all of D.
- **Route 2** (no filter: the ordered DP on every labelled representation of every stratum H = 0..7) also covers all of
  D. It uses only fact (a).

Both routes find the same 640 avoider classes, i.e. 11,120 avoiding labelled representations. There is no non-rigid
avoider and no mixed class. Every avoiding representation was re-confirmed by a naive check of all 43,758 index
subsets. The parent avoider list, mapped to the worker's line format, is **byte-identical** to the worker's
`dp_avoiders.txt` (SHA-256 78a91ba2…5967, 640 lines, per H: 80/160/320/80). No discrepancy was found.

Scope: this establishes C5' on D as a finite exact statement, conditional on the correctness of this parent code. The
worker's reduction C5 → C5' (PLAN-v1 §2, R1/R2 via PM*) is **not** re-audited here.

## 1. Definitions used (PLAN-v1 §1–3, SHA 7d7793cb…0588)

D_10 = {(v,e) : v ∈ Z_5, e = ±1} with (v,e)(v',e') = (v + e v', e e'); rho_x = (x,+1), sigma_y = (y,−1); e = (0,+1).

D consists of the linear words R_1 S_1 R_2 S_2 R_3 S_3 R_4 S_4 of length 18, where:
- S_i = sigma_{y_i}^{l_i} with l_i = 2a_i + 1;
- each R_i is a possibly empty run of rotations rho_x, with x = 0 allowed;
- adjacent y_i may be equal.

Let H = Σ a_i. The number of rotation letters is then R = 14 − 2H, so H ranges over 0..7.

A word is **solved** if some indices i_1 < … < i_10 give w_{i_1}⋯w_{i_10} = e. Otherwise it is an **avoider**. It is
**rigid** if all its rotation letters lie in one set {rho_c, rho_−c}, c ≠ 0.

A **labelled representation** is a tuple (H; l-tuple; 4-tuple of run multisets; y-tuple). Its word writes each run in
ascending value order. Distinct labelled representations can spell the same raw word: PC-k2 below has 6. So
representation counts are not raw-word counts. Every word of D has at least one labelled representation, so covering
all labelled representations covers D. A **class** is (H; run-multiset 4-tuple; y-tuple).

## 2. Facts used, with proofs

(a) **Runs are multisets.** Let w = A U B, where U is a run of rotations, and let w' = A U' B with U' a rearrangement of
U. Fix a value-preserving bijection π from the positions of U to the positions of U'. Map a selection I in w to
I' = (I∩A) ∪ π(I∩U) ∪ (I∩B). This map is a bijection between selections and preserves their size. The rotations
commute: rho_x rho_x' = (x + x', +1). So the selected part of U multiplies to rho_{Σ x}, and so does its image in U'.
The two products (∏A-part)·rho_{Σx}·(∏B-part) are therefore equal, and w and w' have the same set of 10-subword
products. **Route 2 uses only this fact.**

(b) sigma_y² = (y + (−1)y, +1) = e. So any j letters chosen from sigma_y^l multiply to sigma_y^{j mod 2}.

(c) **H ≥ 5 ⇒ solved.** Choose k_i ≤ a_i with Σ k_i = 5, and select 2k_i letters of S_i. This is possible since
2a_i ≤ l_i − 1. The subword is ∏ sigma_{y_i}^{2k_i}, which equals e by (b), and it has length 10.

(d) **Pairs plus a zero-sum sub-multiset.** Suppose j ≤ H and the rotation multiset M has a sub-multiset T with
|T| = 10 − 2j and Σ T ≡ 0 (mod 5). Then the word is solved:
- choose k_i ≤ a_i with Σ k_i = j and select 2k_i letters of each S_i;
- select any positions carrying the values of T.

In index order the selection reads (sel R_1)(sel S_1)…(sel R_4)(sel S_4). Each sel S_i equals sigma^{2k_i} = e, and the
sel R_i multiply to rho_{ΣT} = e. The length is (10 − 2j) + 2j = 10. Fact (c) is the case j = 5, T = ∅.

How (d) is used: route 1 uses (d) only to skip representations, never to declare an avoider. It depends only on
(H, M), so it skips a whole run-multiset 4-tuple together with all C(H+3,3)·625 of its (l, y) completions. Route 2
checked every representation that (d) skipped: there were 0 violations.

## 3. Code (own, written from §1–3 definitions; no worker code read, imported, copied or run)

`src/olson_p5o4_replay_v2.cpp` (SHA 89abe678…6b68), built with clang++ -O2 -std=c++17 -Wall -Wextra with no warnings,
into `bin/replay_v2` (SHA 4bb26b02…1cf8):
- **Group.** MUL comes from the law. A self-test checks the axioms, the dihedral relations and non-commutativity
  (0 failures, 60 non-commuting ordered pairs).
- **DP.** r[c] ⊆ D_10 (a 10-bit mask) is the set of products of c-letter subsequences of the prefix read so far. For each
  letter g, set r[c] ← r[c] ∪ r[c−1]·g for c = 10..1. The word is solved iff e ∈ r[10].
- **Naive check.** All C(18,10) = 43,758 index subsets, multiplied out with MUL.
- **`enum` mode (route 1).**
  - (d) is decided per (H, M) by its own subset-size/sum loop;
  - all C(R+19,19) 4-tuples of run multisets (20 counts) are enumerated explicitly;
  - each (d)-surviving tuple has all its (l, y) completions decided by the DP;
  - the DP runs prefix-shared and also from scratch, and the two verdicts are compared representation by representation.
- **`brute` mode (route 2).**
  - one stratum H at a time, split into shards by tuple index mod n;
  - every (l, y) completion of every tuple is decided by the prefix-shared DP;
  - every 1009th representation is re-decided from scratch;
  - any avoider inside a (d)-solved tuple is counted as a filter violation.

`src/indep_check_v1.py` is an independent Python implementation of (d) (itertools over expanded multisets), the
closed-form counts, and a naive D_10 check with its own group law. `src/compare_v3.py` does the final comparison and
aggregation. It requires exact strata 0..7 and the per-H Python totals, and takes route 2 from an explicit run manifest.
`src/make_result_v4.py` assembles `RESULT-v1.json`.

`bin/replay_v1` (source v1, SHA d0f7860b…6521) differs from v2 only in the CLI of the brute mode. Its enumeration list
outputs are byte-identical to v2's. Its controls report identical verdict fields; only the timing fields differ.

Process disclosures:
- The read tool displayed all of PLAN-v1, not only §1–3, so I saw the worker's plan-time counts. They were used only for
  the comparison at the end.
- Draft sources were edited in place before their first compile or execution: the v1 .cpp,
  run_brute_shards_v2.sh, the never-run compare_v1.py and NOTE-primary-v1.md before it was hashed.
- compare_v1/v2 and make_result_v1/v2/v3 were never executed and are superseded.

## 4. Counts (exact; route 1 `out/enum-clean-v2/summary.json`, route 2 `out/compare-v3/compare.json`)

Abbreviations: **4-tuples** are run-multiset 4-tuples; **reps** are labelled representations.

| H | R | l-tuples | multisets M | (d)-solved M | surviving M (rigid/non-rigid) | 4-tuples = C(R+19,19) | surviving 4-tuples | reps (formula) | route 1: counted via (d) | route 1: by DP | route 2: by DP | avoiding reps (both routes) | avoider classes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 14 | 1 | 3060 | 3060 | 0 | 818,809,200 | 0 | 511,755,750,000 | 511,755,750,000 | 0 | 511,755,750,000 | 0 | 0 |
| 1 | 12 | 4 | 1820 | 1816 | 4 (4/0) | 141,120,525 | 17,600 | 352,801,312,500 | 352,757,312,500 | 44,000,000 | 352,801,312,500 | 320 | 80 |
| 2 | 10 | 10 | 1001 | 989 | 12 (8/4) | 20,030,010 | 13,640 | 125,187,562,500 | 125,102,312,500 | 85,250,000 | 125,187,562,500 | 1,600 | 160 |
| 3 | 8 | 20 | 495 | 483 | 12 (8/4) | 2,220,075 | 7,956 | 27,750,937,500 | 27,651,487,500 | 99,450,000 | 27,750,937,500 | 6,400 | 320 |
| 4 | 6 | 35 | 210 | 202 | 8 (4/4) | 177,100 | 1,232 | 3,874,062,500 | 3,847,112,500 | 26,950,000 | 3,874,062,500 | 2,800 | 80 |
| Σ 0–4 | | | 6586 | 6550 | 36 | 982,356,910 | 40,428 | **1,021,369,625,000** | 1,021,113,975,000 | 255,650,000 | **1,021,369,625,000** | 11,120 | 640 |
| 5–7 | 4,2,0 | 56,84,120 | 86 | 86 | 0 | 9,066 | 0 | 321,025,000 | 321,025,000 | 0 | 321,025,000 | 0 | 0 |

- **H = 0..4 totals.** Labelled representations total Σ C(H+3,3)·C(R+19,19)·625 = 1,021,369,625,000, which equals the
  task's closed form. Classes total 982,356,910 × 625 = 613,973,068,750.
- **Full domain H = 0..7.** 1,021,690,650,000 representations, all decided individually by route 2.
- **Independent checks.** Python recomputed every per-H number. The survivor-multiset lists of C++ and Python are
  identical (36 = 36).
- **Mixed classes.** None in either route: every class has either all of its C(H+3,3) l-tuples avoiding or none.
- **Multiplicity mapping.**
  - A run-multiset 4-tuple c stands for ∏_i (|R_i|!/∏_x c_{i,x}!) sequence-run representations, and all of them have
    the same verdict by (a).
  - Summed over 4-tuples, this gives C(R+3,3)·5^R. The enumerator checked this by explicit summation: 2,889,994,531,250,000
    sequence-run representations for H = 0..4, and 2,889,995,310,075,000 for H = 0..7.
  - In route 1, a (d)-solved 4-tuple stands for exactly C(H+3,3)·625 representations, all solved by (d).
  - Every other representation in route 1, and every representation in route 2, was decided individually by the DP.

## 5. Results and comparison with the worker

- **Avoiders.** All 640 avoider classes are rigid. Census by rotation multiset M, where c ranges over 1..4 and each H
  has 4 multisets:

  | H | M | classes per M | classes for this H |
  |---|---|---|---|
  | 1 | {c⁹, (−c)³} | 20 | 80 |
  | 2 | {c⁹, (−c)¹} | 40 | 160 |
  | 3 | {c⁸} | 80 | 320 |
  | 4 | {c⁶} | 20 | 80 |

- **Survivors without avoiders.** The 12 non-rigid survivor multisets have no avoider. Neither do {c⁸,(−c)²} at H = 2
  and {c⁷,(−c)¹} at H = 3.
- **Route 2 agrees with route 1 on every stratum.** Its per-H avoider class sets are equal to route 1's. It has 0 filter
  violations, 0 mixed classes, and 0 prefix-vs-scratch mismatches over 1,012,577,463 re-checks.
- **Comparison with the worker.** I mapped each class to the worker's line `H=..|dist=c0,..,c4/…/…/…|y=y1y2y3y4`.
  - The two lists are equal as sets, and equal per H.
  - They are in the same order (the worker file is sorted).
  - The mapped file is byte-identical to the worker's file: SHA 78a91ba2…5967 in both.
  - Comparator self-tests: dropping a line, altering a y, an empty list and a non-rigid injection are all detected.
- **Naive confirmation.** Every one of the 11,120 avoiding representations was re-decided by the naive check. All
  11,120 avoid under both DP and naive.

## 6. Controls

**PC-k2 = r1⁹ s0⁷ r4 s0** (length 18).
- Its maximal blocks are r1⁹ | s0⁷ | r4 | s0. There are two maximal reflection blocks, s0⁷ and s0, both odd. Cyclically
  they do not merge, since the first letter r1 differs from the last letter s0. So o_F = 2 for its maximal
  decomposition, **not 4**.
- It is in D only through non-maximal 4-block representations. These split s0⁷ into 3 odd parts with empty R_2, R_3 and
  equal y: l ∈ {(1,1,5,1), (1,3,3,1), (1,5,1,1), (3,1,3,1), (3,3,1,1), (5,1,1,1)}, with H = 2, runs (1⁹, ∅, ∅, {4}) and
  y = 0000. Exactly 6 of the class's 10 l-tuples spell PC-k2 literally.
- All 10 l-tuples avoid by both DP and naive. Python's naive check also confirms all 10.

**Avoiders found here.** A1 = H=1 runs 4/4/4/1⁹ y=0000 (4 l-tuples), A2 = H=3 runs -/-/4/4⁷ y=0020 (20) and A3 = H=4
runs 4/4/4/444 y=0243 (35). All of their l-tuples avoid under the C++ DP, the C++ naive check and the Python naive check.

**Random agreement checks.** Let S1 be 20,000 random domain representations and S2 20,000 random representations over
survivor multisets. DP and naive disagree 0 times in each.

**(d) never fires wrongly on samples.** S3 covers each of the 6,636 (d)-solved multisets for H = 0..7. Each got 30 random
completions, all DP-solved, and 1 completion that is also naive-solved. Route 2 then checked (d) exhaustively.

**Negative controls.** Each of these changes the outcome from 640 avoider classes to 0, and each flips PC-k2:
- **N1, untwisted law (v + v', e e').** 0 avoiders, and PC-k2 becomes solvable under both DP and naive.
- **N2, target length 8.** 0 avoiders, and PC-k2 becomes solvable.
- **N3, wrong parity rule in (d).** Each odd block is credited with (l+1)/2 identity pairs, i.e. its odd leftover letter
  is treated as cancelling. Then every representation is skipped as solved, giving 0 avoiders, and PC-k2 is filtered.

A1–A3 are solvable under N1 and N2 for every l-tuple, and N3 filters them. The rigidity predicate's unit tests (with
non-rigid cases) report 0 failures.

## 7. Runs, resources and the 09:25:51 interruption

Every native step was a separate process under ulimit -t, with /usr/bin/time -l, and at most 2 ran at once. Max RSS was
at most 3.0 MB for C++ and 23 MB for Python.

| step | wall |
|---|---|
| route-1 enumeration | 26.3 s |
| each bug enumeration | ≤ 26.5 s |
| controls | 0.5 s |
| naive check of all avoiders | 3.2 s |
| route-2 shards, sum of elapsed (each at ≈100% CPU) | 5,191 s |
| H = 0 route-2 shard (each) | ≈ 417 s |
| H = 1 route-2 shard (each) | ≈ 455 s |
| H = 2 route-2 shard (each) | ≈ 341 s |
| H = 3 route-2 shard | 160.5 s |

Every run that the verdict rests on exited 0. The last C++ process ended at 10:00:51 PDT; the Python aggregation ran at
10:01:03, and RESULT-v1.json is assembled after this note.

**Interruption.**
- At 09:25:51 PDT the first route-2 launcher (xargs in `run_brute_shards_v2.sh`) received an external SIGTERM. Its
  cause was not established by this desk, and this desk sent no signal before 09:28:03.
- `brute-H2-s1of2-v2` was stopped by it.
- `brute-H2-s0of2-v2` survived as an orphan. This desk stopped it with SIGTERM at 09:28:03 (exit=143). Both are
  UNKNOWN; their (empty) outputs are kept and not used.
- The first rerun attempt at 09:28:51 failed before anything ran: os.setsid gave EPERM.
- The rerun at 09:52:30 used `src/detach_v1.py` (fork + setsid) to start `run_brute_rerun_v3.sh`. It ran H = 2 (2 shards)
  and H = 3 as `*-v2r2`, and all three shards exited 0 by 10:00:51.
- Route 1 and every control had finished before the interruption.
