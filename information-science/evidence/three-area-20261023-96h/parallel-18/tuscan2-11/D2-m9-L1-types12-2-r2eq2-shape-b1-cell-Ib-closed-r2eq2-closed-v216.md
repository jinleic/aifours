# Original Tuscan-2(11), entire m = 9 distance-two branch: shape (b1), cell I-b is impossible, so types 12 and 2 with r2 = 2 are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It is written only from the author's own unquarantined material (Main v215).

The number v216 is in the owner's own packet series; it is not a parent direction.

It continues `D2-m9-L1-types12-2-r2eq2-shape-b1-cell-Ia-closed-v215.md` (SHA256 `0185a61bdf26da99b26dd06c3bf96793d33b98f26d82e1891831a711ab742106`). It uses the v214 §2 anatomy table, the v214 §5 F2 facts and (PC) (v185 §2).

It uses (R1)–(R2) only. It is written reasoning only: no interpreter, enumeration, program or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Cell I-b

**Parameters:**
- u = 4, so S = {c1, c8, X40, X20} and T_int = {Z1, X50, X70, X30, Z0};
- x ∈ {7, 8};
- P1 = 17, P2 = 38 + c, P3 = 46, ℓ1 = 11, ℓ3 = 9, ℓ2 = 21 + c, λ = 8 − c, P5 = 76 + c, with c = [c1 in shape R4].

**The threads:**
- **t1.** The arm is t1[1..4], with t1[4] = c1. The R1-vertices t1[5..10] carry {v, c8, X50, X70, X30} and Z0 = t1[x]. X70 and X30 lie below x, v and c8 lie above x (v214 §5), and X50 lies above x exactly when x = 7.
- **t3.** F1 puts t3[k] at P5 − k, so X70 = t3[6+c]. R6's t3-interior is {t3[7], t3[8]} when c = 0 and {t3[8]} when c = 1. Its labels are X30, together with c1 when c = 0. So **t3[8] = X30 when c = 1**, and t3[7..8] = {X30, c1} when c = 0.
- **Λ.** P− puts Λ[j] at 46 − j. The arm is Λ[4−c..7−c], with c8 = Λ[4−c] and X40 = Λ[6]. The non-arm vertices Λ[1..3−c] carry the (R4, R7) labels Z0, X30 and, when c = 0, c1.

**(PC) at v gives t1[1] = X20.** X20 can meet v only through b6–t1[1]. The reasons are as in owner-v215 §3:
- its t3-vertex lies in Q1 at an index ≥ 3;
- its t2-vertices t2[18+c] and the (R3, R5) one are not adjacent to v's t2[14];
- it has no T- or non-arm Λ-vertex, and Λ[λ−1] carries c1 (when c = 0) or X40 (when c = 1).

## 2. c = 0 is impossible

Here the R4-arm consists of Λ[4] (c8, at 42) and Λ[5] (at 41). The only other label whose arm lies in R4 is X20, so Λ[5] = X20. Then Λ[4]Λ[5] uses the pair {c8, X20}, and Λ[5]Λ[6] uses {X20, X40}.

t1[2] carries c8 or X40, and it is adjacent to t1[1] = X20. Either choice repeats one of those two pairs. **Contradiction.**

## 3. c = 1 is impossible

Here X70 = t3[7] and X30 = t3[8] are adjacent, so the pair {X70, X30} is used.

**x = 7.** Below x lie exactly t1[5..6] = {X70, X30}. These are adjacent, which repeats {X70, X30}. **Contradiction.**

**x = 8.** First, (PC) at v forces the following.
- F2 gives t3[1] = w and t3[2] = Z1.
- c1's only possible contact with v is t2[15], an (R2, R6) vertex, so t2[15] = c1. X40 meets v at Λ[6].
- If v = t1[10], then v would meet w both at b3 and at t3[1]. So v = t1[9], with neighbours Z0 (t1[8]) and c8 (t1[10]).
- X50 lies below x and is not t3[1] or t2[15], so it can meet v only at T_1. Hence T_1 = X50.
- X30 must then meet v at Λ[1]. So Λ[1] = X30, Λ[2] = Z0, and the pair {X30, Z0} is used.

Next, t1[5..7] = {X70, X30, X50}.
- X70 and X30 cannot be adjacent here, so X50 = t1[6].
- t1[7] is adjacent to t1[8] = Z0, so t1[7] ≠ X30. Hence t1[7] = X70 and t1[5] = X30.

Now X30 is already adjacent to:
- v and Z0 (via Λ[1]);
- c1 and X50 (via t1[5]);
- X70 and w (via t3[8] and b3).

By (PC), its T-vertex must supply two new neighbours. That vertex lies among T_2..T_5, since T_1 = X50. Its neighbours are T_int labels, or w at ℓ. The only T_int label not yet adjacent to X30 is Z1, so at most one of the two neighbours is new. **Contradiction.**

## 4. Result

**WRITTEN:**
- Cell I-b is impossible. With owner-v215 (cell I-a) and v214, **shape (b1) of v209 is impossible**.
- With v210–v213 (shape (b2)), v209, v208, v207, v205, v203 and v200–v202, **L1 types 12 and 2 with r2 = 2 are closed** (type 2 by the mirror, v160 §1).
- Together with v199 (r2 = 3, α3 k = 1, outside the v21 freeze), v185 (r2 = 4) and the earlier r2 = 3 closures, **L1 types 12 and 2 are closed** in the author's own chain. That chain is unreviewed, and the review-frozen residual of v169-A §7 is unchanged.

**OPEN (m = 9, L1):**
- types 1 and 11 with r1 ∈ {4, 5};
- type 8 with r1 ∈ {3, 4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried, and so is the Main217 parent process MAJOR. This candidate needs its own complete source-bound gate.
