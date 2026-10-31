# Original Tuscan-2(11), entire m = 9 distance-two branch, part 62: consolidated status after v168–v174 (L1 types 3 and 9 closed, type 7 reduced) and an updated atlas of the open L1 cells

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It supersedes the status and atlas sections of `D2-m9-consolidated-status-L1-open-cell-atlas-v167.md` (SHA256 `bad9940e229cc254441587898b67f66bc24b96030bfeae8630c163b533247f9b`).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. New packets since v167

| Packet | SHA256 | Content |
|---|---|---|
| v168 | `4b082a4653d5ab2e2738220d7634eb7c738c318de242fa60e75104b2cc1acc82` | type 9, r2 = 3, λ = 14, u = 4 closed |
| v169 | `0ffe0db4b6a95e7cd360d50808d49c2f322b6e94ba0929259748f244ff2414f4` | type 9, r2 = 3, λ = 14, u ≥ 5 closed; types 3 and 9 with r2 = 3 closed |
| v170 | `94d814050b7585809f8ede7b7668b03191eb317a947d8438a51683854a969e44` | type 9, r2 = 4, λ ∈ {12, 13, 14} closed |
| v171 | `54aec9aebe264883a00663ade463a01f3d08cb63baa446f3a80e0ed9ebbf06e2` | type 9, r2 = 4, λ ∈ [21, 24] closed; **L1 types 3 and 9 closed** |
| v172 | `6bca223beb5517ee4350ed85fde5422c9284520df01c1aeef85701607b67c802` | type 7, r2 = 3: Lemma T7; c′ = 1 and v's G2-V on Λ closed |
| v173 | `0f399e93d91f26c7f5b0e7e9d8614601e84668f0b053360151e6a95f59ab93d8` | type 7, r2 = 4: Lemma T7′; nΛ = 2 (c′ = 0) and nΛ = 1 (c′ = 1) closed; u ≥ 2 in type 7 |
| v174 | `b213df8f4eac9cd80331d6f93c56175d0bc67915e5d19c3d92c9575a70054e40` | type 7, r2 = 3: P2 ≥ 31, P3 ≤ 49; forced shape for v's G2-V on t1; α-ii and the wide α-i with P1 ≤ 19 closed |

## 2. Closed (all WRITTEN, unreviewed)

**Whole classes.**
- **L2 (k = 3):** every cell (v114–v150; consolidated in v151).
- **L4-B:** closed (v112, v113).

**L1 by type.**

| Type | Closed | Sources |
|---|---|---|
| 5 and 6 | all | v118 |
| 4 and 10 | all | v153–v155 |
| **3 and 9** | **all** | v156 (r2 = 2); v158, v159, v168, v169 (r2 = 3); v166, v170, v171 (r2 = 4) |
| 7 | r2 = 2 | v157 |
| 7 | r2 = 3 except c′ = 0 with v's G2-V on t1 or t3, in the α-i forms of v174 §5 | v172, v174 |
| 7 | r2 = 4 except v having a G2-V on t1 or t3 | v173 |
| 1 and 11 | r1 = 3 | v161, v162 |
| 8 | r1 = 6 | v163 |
| 8 | r1 = 5 except ℓ1 − u ∈ [11, 19] | v164 |

**General tools (all WRITTEN):**
- face-group anatomy (v152);
- the row-reversal mirror (v155 §5);
- Lemma 2R (v160 §2);
- Lemma DP★ (v165 §1).
- **New in this window:**
  - the F2-block copy (the F2-face reads the F1-runs of the G2-threads, possibly reversed);
  - the adjacent-duplicate rule: a label with two vertices in one face separated only by vertices whose labels are cut in the other face lies twice in one row;
  - Lemmas T7 and T7′ (nested t2-parts of R1 and R_{r1−2});
  - the arm exchange (an F2-row holding b6 and a whole arm has {w} ∪ T_int on its other vertices);
  - the c1/c5 two-pass bound (v174 §1).

## 3. Atlas of the open L1 cells

| Type(s) | Cell | Proved restrictions | Blocker |
|---|---|---|---|
| 7 (and mirror) | r2 = 3, c′ = 0, n1 = 1 (or n3 = 1) | P2 ∈ R3, P3 ∈ R4, v = X60 with its t2-vertex on the cut 60; open only in three α-i forms (v174 §5). | Each form needs a long exchange chain. DP-2 is blocked because the forward t1-row R2 contains b3. |
| 7 | r2 = 4, v with a G2-V on t1 or t3 | Lemma T7′ and the arm exchange apply whenever all non-arm t1/t3-vertices lie in the two b6-rows of F2 (v173). | The F2-rows between the two b6-rows contain t1/t3 vertices with unrestricted labels. |
| 2, 12 | r2 = 2 | Type 12: ℓ1 ≤ u + 9, ℓ2 ≥ 5, and no F1-row lies inside the t3-run (v160, v165). | Sub-cases (i′) and (ii-b) of the v167 exploration, and ℓ2 ≥ 15. |
| 2, 12 | r2 ∈ {3, 4} | — | Cross-face DP on t1 and t3. |
| 1, 11 | r1 ∈ {4, 5, 6} | ℓ3 = 65 − 10r1 − u. For r1 = 6, every S-label is F1-cut (not packeted). | The t3 double pass is short. |
| 8 | r1 ∈ {3, 4} | — | Interleaved t3/Λ double passes in F2. |
| 8 | r1 = 5 | ℓ1 − u ∈ [11, 19] (v164) | Only one pure t1-row and one pure t2-row in F1. The F2 arm structure resembles type 7 (not packeted). |

## 4. Statement scope

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
