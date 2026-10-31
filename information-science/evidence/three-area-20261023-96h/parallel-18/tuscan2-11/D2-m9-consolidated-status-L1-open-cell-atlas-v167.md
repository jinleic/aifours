# Original Tuscan-2(11), entire m = 9 distance-two branch, part 54: consolidated status after v152–v166, and an atlas of the open L1 cells

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It supersedes the status sections of `D2-m9-consolidated-status-L1-progress-two-row-lemma-exact-gap-v160.md` (SHA256 `3597c7633dcbf620c46f532ef3f7ba38e42627f029a738c4119bb3b96e888cff`). All pins of v110–v165 are listed in `park-v2-addendum-23.json` (SHA256 `c3bba5433fd46e95036f7c15dddf47eaac20cf64db61fa3c57524455b31ba099`). The v166 pin is `4e6381c2cf9052bdc55357853efa837f76b1340cbce1c9f71e09ebfcf66e4f0e`.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Closed (all WRITTEN, unreviewed)

**Whole classes.**
- **L2 (k = 3):** every cell (v114–v150; consolidated in v151).
- **L4-B:** closed (v112, v113).

**L1 by type.**

| Type | Closed | Sources |
|---|---|---|
| 5 and 6 | all | v118 |
| 4 and 10 | all | v153, v154, v155; r2 = 1 by F0, r2 = 4 by (K-S) |
| 3 and 9 | r2 = 2 | v156 |
| 3 and 9 | r2 = 3 except λ = 14 with u ≥ 4 | v158, v159 |
| 7 | r2 = 2 | v157 |
| 1 and 11 | r1 = 3 | v161, v162 |
| 8 | r1 = 6 | v163 (count) |
| 8 | r1 = 5 except ℓ1 − u ∈ [11, 19] | v164 |

**General tools (all WRITTEN):**
- face-group anatomy and the counts (K-w) and (K-S) (v152);
- the row-reversal mirror pairs (1, 11), (2, 12), (3, 9) and (4, 10), with 7 and 8 self-mirror (v155 §5, v156 §3, v160 §1, v161 §4);
- Lemma 2R for two-row faces (v160 §2);
- Lemma DP★: two consecutive pure rows of a double-passed thread are impossible, given disjoint partner rows (v165 §1).

## 2. Atlas of the open L1 cells

Each row lists what is proved about the cell and what blocked further progress in this round.

| Type(s) | Cell | Proved restrictions | Blocker |
|---|---|---|---|
| 3, 9 | r2 = 3 | λ = 14, u ≥ 4 (v158, v159). For u ≥ 5 the label roles are forced (written; not packeted). | Every row count is consistent. Needs a finer exchange, such as the F2-block reversal identity between the F1-run t2⁻ b6 t3⁺ and the F2-run t2⁺ b3 t3⁻. |
| 3, 9 | r2 = 4 | λ ∈ {12, 13, 14} with ℓ2 ≥ 5, or λ ∈ {21, …, 24} with λ ≤ 20 + u. Positions 16–20 of R1 carry {c5, X20, X30, X40, X50}, and t1[u+1..u+4] carries the F2-cut labels (v166). | Single pure rows only; DP-2 is unavailable. |
| 7 | r2 = 3 | — | The t2 runs have length u + 14, so at most one pure row each when u ≤ 6. |
| 7 | r2 = 4 | — | t2 is short (u + 4); F1 is G2-heavy. |
| 2, 12 | r2 = 2 | Type 12: ℓ1 ≤ u + 9 (Cor. 2R), ℓ2 ≥ 5 (v165), and no F1-row inside the t3-run; type 2 by the mirror. Exploration (not packeted): for ℓ2 ≤ 14 the P−-copy of the pure row R7 leaves only two sub-cases, plus ℓ2 ≥ 15. | Sub-cases (i′) and (ii-b), and ℓ2 ≥ 15. |
| 2, 12 | r2 ∈ {3, 4} | — | Cross-face DP on t1 and t3 (ℓ1 + ℓ3 = 30 or 40). |
| 1, 11 | r1 ∈ {4, 5, 6} | ℓ3 = 65 − 10r1 − u. For r1 = 6: u ≤ 4, c = 1, n1 = n3 = 0, and every S-label is F1-cut (written; not packeted). | The t3 double pass is short. Each long G2-thread needs two pure rows for DP★. |
| 8 | r1 ∈ {3, 4} | — | Interleaved t3/Λ double passes in F2 (ℓ3 + λ = 35 − u or 25 − u). |
| 8 | r1 = 5 | ℓ1 − u ∈ [11, 19] (v164) | Only one pure t1-row and one pure t2-row in F1. |

## 3. Statement scope

- The support-9 statement ("every eligible original T2(11) array with support 9 is impossible") is **not** made, because the cells above are open.
- Every m in 10..110 is unresolved.
- The original Tuscan-2(11) target is UNMET: there is no literal table and no all-array contradiction.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
