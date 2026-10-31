# Original Tuscan-2(11), entire m = 9 distance-two branch, part 71: consolidated status after v176–v183 (L1 type 7, type 8 with r1 = 5, and types 1/11 with r1 = 6 closed) and an updated atlas of the open L1 cells

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It supersedes the status and atlas sections of `D2-m9-consolidated-status-L1-types3-9-closed-type7-reduced-atlas-v175.md` (SHA256 `9e800e98a6bd766d178031ec75dd81d8199202533a30b7b16c5fb3a2b3cb9167`).

It is a bookkeeping record of written candidates only: no interpreter, enumeration, solver or search was used. Nothing here is reviewed, formal or novelty-cleared. Every SHA256 below was taken live with `shasum -a 256`.

## 1. New packets since v175

| Packet | SHA256 | Content |
|---|---|---|
| v176 | `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021` | Lemma A4 (arm exactness): u ≥ 4 in every open L1 type; form (b) of v174 closed |
| addendum-1 | `ad599fac24eec5636ceb20b84c0f56d9e65ce7f91b8bd8c263fdcf9b21d9b06a` | exposition addendum to v174 §2 and v176 |
| v177 | `6997ee0e94802c406c350b3a6d5bf69f4872233a2bb97b1936f02b2a8f11c68c` | type 7, r2 = 3: forms (ii) and (iii) closed; **type 7 with r2 = 3 closed** |
| v178 | `a41c8e7f0fe6593befd2d88d87b3da3ea56ca4ff5196d6681f134f5896e70c78` | type 7, r2 = 4: ℓ1, ℓ3 ≥ 7; four c′ = 0 v-patterns removed; cases (P) and (Q) left |
| v179 | `432c612df1c416a65ff411a42731aaa16d8e10405c73e8aba3408d3c73d7f228` | type 7, r2 = 4: case (Q) with the cut at 20 or 50 closed |
| v180 | `2f73f1ec54be8e77b7526abc95bc8e229fc6eddf0c16ced5bc4966d7d0f7180f` | type 7, r2 = 4: case (Q) with the cut at 30 or 40 closed; **case (Q) closed** |
| v181 | `8bcc54a6f8e96f340caba4f864b13b99d248e75104393abda8ea9ad2ab6c9ade` | type 7, r2 = 4: case (P) closed; **L1 type 7 closed** |
| v182 | `4592b9040db2cd2577bd47bcb34044b6a07b5aa81dfc16f7110f5a086366dc6a` | **type 8 with r1 = 5 closed** |
| v183 | `9149af2ce08b5c3d7b3fe5e47f6014cd146d76e3a0fbd95214a156d942a314f4` | **types 11 and 1 with r1 = 6 closed** |

## 2. Closed (all WRITTEN, unreviewed)

**Whole classes.**
- **L2 (k = 3):** every cell (v114–v150; consolidated in v151).
- **L4-B:** closed (v112, v113).

**L1 by type.**

| Type | Closed | Sources |
|---|---|---|
| 5 and 6 | all | v118 |
| 4 and 10 | all | v153–v155 |
| 3 and 9 | all | v156, v158, v159, v166, v168–v171 |
| **7** | **all** | v157 (r2 = 2); v172, v174, v176, v177 (r2 = 3); v173, v178–v181 (r2 = 4) |
| 1 and 11 | r1 = 3 and r1 = 6 | v161, v162; v183 |
| 8 | r1 = 5 and r1 = 6 | v164, v182; v163 |

**General tools (all WRITTEN):**
- face-group anatomy and (K-w) (v152);
- the row-reversal mirror (v155 §5);
- Lemma DP★ (v165 §1) and Lemma A4 (v176 §1);
- the arm exchange (v172 §2, v173 §2).
- **New in v178–v183:**
  - **The grid lemma.** Take a pure F1-row along a thread whose other pass lies in F2, with end labels that are not F2-cut. Exactly one F2-cut lies strictly inside it. The two F2-rows meeting there leave difference paths of sizes d and 10 − d, so d ∈ {4,5,6}, by "one cut per label" and (E) (v179 §1, v181 §3, v182 §2, v183 §3).
  - **The a/b dichotomy in type 7.** It compares S_12- and S_23-passes of one t2-vertex (v181 §2).
  - **The W-rule.** When w's b3-passages fill two F2-rows, its G2-W's fill the others. This bounds w's Λ- and t3-vertices (v183 §2).

## 3. Atlas of the open L1 cells

| Type(s) | Cell | Proved restrictions | Blocker |
|---|---|---|---|
| 2, 12 | r2 = 2 | Type 12: ℓ1 ≤ u + 9, ℓ2 ≥ 5, and no F1-row lies inside the t3-run (v160, v165). | Sub-cases (i′) and (ii-b) of the v167 exploration, and ℓ2 ≥ 15. |
| 2, 12 | r2 ∈ {3,4} | u ≥ 4 (v176) | Cross-face double passes on t1 and t3. |
| 1, 11 | r1 = 5 | u ≥ 4, ℓ3 = 15 − u. With c = 1 and v's G2-V on t1: the six F2-rows X, Y−, Y, W, W+, T1 and Z3 = 20 − x + y. Not packeted. | The short t3 double pass in F2. F2-cut S-labels may sit on the arms. |
| 1, 11 | r1 = 4 | u ≥ 4, ℓ3 = 25 − u ∈ [16,21] | Too short for DP★ on t3. |
| 8 | r1 = 4 | u ≥ 4. With a = ℓ1 − u ≥ 11 (by the mirror), R1 is pure and x = u + d with d ∈ [4,6], so u ∈ {4,5}. In case (A) with v on Λ, two pure Λ F2-rows lie at shift ρ ∈ [4,9]. Not packeted. | The interleaved t3/Λ double passes in F2. |
| 8 | r1 = 3 | c = 0, n1 + n2 = 1, n3 + nΛ = 1 (not packeted) | ℓ3 + λ = 35 − u, with both double passes in F2. |

## 4. Statement scope

- The support-9 statement ("every eligible original T2(11) array with support 9 is impossible") is **not** made, because the cells of §3 are open.
- Every m in 10..110 is unresolved.
- The original Tuscan-2(11) target is UNMET: there is no literal table and no all-array contradiction.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
