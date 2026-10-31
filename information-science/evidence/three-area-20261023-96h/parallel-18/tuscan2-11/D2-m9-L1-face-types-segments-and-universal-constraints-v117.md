# Original Tuscan-2(11), entire m = 9 distance-two branch, part 6: L1 — the twelve rotation types, the v-segment decomposition, and the universal constraints

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-universal-offset-parametrization-and-kills-v116.md` (SHA256 `dcaca8479d52bc975f319f4e8aae7b6ae35f821f4f9eae7ff233f6d85e29b335`). Lemmas DP-1, DP-2 and OL (v114 §2, v115 §1) apply verbatim.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. Setting (v94 §5.1)

**The graph H.**
- Label v has the branch b6 of degree 6 and two 2-vertices V.
- Label w has the branch b3 of degree 3, the leaf ℓ (the w-cut) and three 2-vertices W.
- The other nine labels have five 2-vertices each.
- H consists of the tail T (from ℓ to b6, length t ≤ 9), three threads t1, t2, t3 from b6 to b3 (lengths ℓ1, ℓ2, ℓ3), and a loop Λ at b6 whose ends are not rotation-adjacent.
- These lengths satisfy t + ℓ1 + ℓ2 + ℓ3 + λ = 55.
- The array is connected and has 11 rows. Exactness (one edge per pair) and one cut per label hold.

**Rotations.**
- At b3 the rotation is (t1, t2, t3), which names the threads.
- At b6 the rotation is (T, h1, h2, h3, h4, h5).

**Arms.** R_out = ℓ, T_int, b6, h1[1..u] and R_in = h5[u..1], b6, T_int, ℓ, with u = 10 − t. Both arms carry S = X ∖ ({v, w} ∪ L(T_int)). They contain no v and no w, so they stay inside the paths of h1 and h5 and meet no V or W.

## 2. The six v-segments and the twelve types

**The v-segments.** Cutting the faces at the six corners of b6 gives six segments:
- S_T = T⁻ ℓ T, of length 2t, with ℓ on a cut;
- the two passes P+ (leaving b6 by Λ+) and P− (leaving by Λ−), of length λ each;
- S_12 = t1 b3 t2⁻, S_23 = t2 b3 t3⁻ and S_31 = t3 b3 t1⁻, of lengths ℓ1+ℓ2, ℓ2+ℓ3 and ℓ3+ℓ1.

**The successor rule.** The segment arriving at b6 along a half-edge h is followed by the segment leaving along σ(h).

**The types.** Use cyclic relabelling of the threads (which preserves b3's rotation) and reversal of the loop to normalise b6's rotation to (T, h1..h5):
- Λ+ comes before Λ−;
- Λ± occupy the non-consecutive positions {1,3}, {1,4}, {1,5}, {2,4}, {2,5} or {3,5};
- the threads appear in the order (t1,t2,t3) or (t1,t3,t2).

Tracing each of the twelve types:

| # | (h1..h5) | Faces |
|---|---|---|
| 1 | Λ+ t1 Λ− t2 t3 | {S_T P+ S_23}, {S_12 S_31 P−} |
| 2 | Λ+ t1 Λ− t3 t2 | {S_T P+ S_31 P− S_12}, {S_23} |
| 3 | Λ+ t1 t2 Λ− t3 | {S_T P+ S_31 S_23}, {S_12 P−} |
| 4 | Λ+ t1 t3 Λ− t2 | {S_T P+ S_23 P− S_12}, {S_31} |
| 5 | Λ+ t1 t2 t3 Λ− | {S_T P+}, {S_12 S_31 S_23 P−} |
| 6 | Λ+ t1 t3 t2 Λ− | {S_T P+}, {S_12 P−}, {S_23}, {S_31} (F = 4) |
| 7 | t1 Λ+ t2 Λ− t3 | {S_T S_12 P− S_23}, {S_31 P+} |
| 8 | t1 Λ+ t3 Λ− t2 | {S_T S_12}, {S_23 P− S_31 P+} |
| 9 | t1 Λ+ t2 t3 Λ− | {S_T S_12 S_31 P+}, {S_23 P−} |
| 10 | t1 Λ+ t3 t2 Λ− | {S_T S_12 P− S_31 P+}, {S_23} |
| 11 | t1 t2 Λ+ t3 Λ− | {S_T S_12 P+}, {S_23 P− S_31} |
| 12 | t1 t3 Λ+ t2 Λ− | {S_T S_12 P− S_23 P+}, {S_31} |

Row reversal maps types to types, so the list is closed under the mirror.

## 3. Universal constraints

**(L-a) Offsets.** Give each b6-corner its offset in its face's cut grid.
- The corners (h5→T) and (T→h1) have offsets u and t.
- v's cut lies either on one b6-corner (offset 0) or on one V-passage.

Consecutive v-passages lie in consecutive rows (v114 (I)). So a b6→b6 segment with n inside V-passages, start offset q_s and end offset q_e has length 10(n+1) + q_e − q_s. If v's cut lies strictly inside the segment, add 10. If a segment ends on the cut, take q_e = 10; if it starts on the cut, take q_s = 0.

**(L-b) Counts.** Let n1, n2, n3 and nΛ count the V's on t1, t2, t3 and Λ. Then n1 + n2 + n3 + nΛ = 2. The number of rows of each face equals the number of v-passages in it, plus one if v's cut lies in it.

**(L-c) Thread and loop lengths.** Lemma OL applies to t1, t2, t3 and Λ:
- every one of them has length ≤ 26;
- a length ≥ 21 forces ρ ∈ {4, 6};
- the arm path h1 has forward cuts at ≡ u, and h5 has backward cuts at ≡ u.

So the v115 arm table applies to whichever thread or loop end is h1, and its mirror to h5.

**(L-d) A single-segment face.** In types 2, 4, 6, 10 and 12, some face is a single segment S_{i,i+1} = t_i b3 t_{i+1}⁻. It is a cycle through b6 and b3 only. Its rows each need one v, and the only v-passages are one b6-corner and the V's on t_i and t_{i+1}. So:
- the face has 1 + n_i + n_{i+1} rows, plus one if it contains v's cut;
- that number must be ≥ 2, so n_i + n_{i+1} ≥ 1 or v's cut lies in the face.

**(L-e) Tail-loop face.** In types 5 and 6, F1 = ℓ T b6 Λ b6 T ℓ: the tail face wraps the loop exactly as F_T does in L2 with k = 1 (v95 §2), with the labels of the leaf and the loop branch exchanged. Its middle rows lie inside Λ and each needs a V and a W on Λ. So r(F1) = 2 + (number of W on Λ), and the number of V on Λ equals r(F1) − 2 − [v's cut in F1].

## 4. Status

**WRITTEN:**
- the L1 rotation types and faces (§2);
- the six-segment decomposition and constraints (L-a)–(L-e) (§3).

**Exact L1 gap at this packet:**
- all twelve types;
- every (n1, n2, n3, nΛ) with sum 2;
- every position of v's cut;
- every u;
- every corner offset subject to (L-a)–(L-e);
- the OL windows and the arm table;
- the remaining row-level tests (V-placement, alternation of w, exchanges).

No L1 cell is excluded yet.

**Open in the v143 branch:** the L2 (k = 3) residual of v116 §4, and this L1 family. The v143 ceiling is unchanged:
- no support-9 statement is made;
- every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
