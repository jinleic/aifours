# Original Tuscan-2(11), entire m = 9 distance-two branch: shape (b1) of v209 — forced label classes, x < u excluded, and the x > u remainder reduced to two cells

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It is written only from the author's own unquarantined material (Main v215).

It continues `D2-m9-L1-types12-2-r2eq2-shape-b2-u4-closed-b2-closed-v213.md` (SHA256 `df5d33404a6fa5c0f52aa13da297708f2abf166b411e90621d0fa7ddd20f08e3`). It uses the conventions and imports of v211, the (b1) data of v209 §5, and v204 §2 for Z0 and Z1.

It uses (R1)–(R2) only. It is written reasoning only: no interpreter, enumeration, program or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Data of (b1)

v = {b6, a t1-vertex in R1, t2[60−P3] (cut 60)}, with S_12 of the cut vertex in R2. P3 ∈ R4 and P2 + P3 ∈ {84, 85, 86}. Since P3 = 25 + u + P1, the quantity s′ := u + P2 lies in [41, 44] (s′ = 40 would put c8's vertex on the cut 40), and P1 ∈ [15, 19].

**Consequences:**
- The arm Λ[λ−1..λ−u] sits at P− positions P2+1..s′, so it crosses 40. X40 is an arm label (S), and c8's vertex Λ[λ−u] has P− in R4.
- Every non-arm Λ-vertex has P− in R4 and P+ in R7.
- A t2-vertex has S_12 + S_23 = P2 + P3 ∈ [84, 86]. So S_12 ∈ R1 gives S_23 ∈ R6; S_12 ∈ R2 gives S_23 ∈ R5 or R6; S_12 ∈ R3 gives S_23 ∈ R4 or R5.
- The F1 cut labels are c1, X20 = t2[P2−20], X30, X40, X50 = t2[50−P3], v (60), X70 (t3 at 70), c8 and w. Z0 and Z1 are the F2 cut labels.

## 2. Forced classes and anatomy

The row-coverage argument of v211 §2 gives the following.

| label | class | vertices |
|---|---|---|
| X20 | S | t1-arm, Λ-arm with P− in R4, t2[P2−20] (rows R1, R2, R6), t2 (R3, R5), t3 in R7 |
| X50 | T_int | T, t2[50−P3] (R3, R4, R5), t2 (R2, R6), a t1-vertex in R1, t3 in R7 |
| X70 | T_int | T, t3 at the cut 70, t2 (R2, R5), t2 (R3, R4), a t1-vertex in R1 |
| Z1 | T_int | T, t3[10−x] **in R7**, t2 (R1, R6), t2 (R2, R5), t2 (R3, R4) |
| c8 | S | t1-arm, Λ[λ−u] (P− in R4, cut 80), a t1-vertex in R1, t2 (R2, R6), t2 (R3, R5) |
| X40 | S | t1-arm, the arm vertex at 40, t2 (R1, R6), t2 (R2, R5), t3 in R7 |
| X30 if S | S | t1-arm, Λ-arm with P− in R4, t2[P2−30], t2 (R1, R6), t3 in R7 |
| X30 if T_int | T_int | T, t2[P2−30], Λ (R4, R7), a t1-vertex in R1, t3 in R6 |
| Z0 if S (x < u) | S | t1[x], Λ-arm with P− in R3, Λ (R4, R7), t2 (R1, R6), t2 (R2, R5) |
| Z0 if T_int (x > u) | T_int | T, t1[x] in R1, t2 (R2, R6), Λ (R4, R7), t2 (R3, R5) |
| c1 | S | t1[u] (cut 10) and Λ-arm, then either (shape R3) arm in R3, t3 in R6, t2 (R2, R5), Λ (R4, R7); or (shape R4) arm in R4, t3 in R7, t2 (R2, R6), t2 (R3, R5) |

Why the classes are forced:
- **X20 ∉ T_int.** It would need two G2-vertices among R3, R4, R5 and R7, but only R7 has G2-vertices.
- **X50 ∉ S.** Its arm vertex would have to be in R3 or R4, but both rows are already taken.
- **X70 ∉ S.** R1 could then be covered neither by a t2-vertex (R6 is taken) nor by a t1-vertex (b = 2 is used up).
- **Z1 has its G2-vertex in R7.** If it were in R6, R1 could not be covered, since t2 (R1, R6) would repeat R6.
- **c8's second G2-vertex is a t1-vertex in R1.** A t3-vertex in R6 would block t2 (R1, R6).

## 3. Counting R1 and R6

R1 = c1, t1[u+1..ℓ1−1], b3 (w), a t2-part at P1+1..19, X20.
- The t1-part carries v, c8, X50 and X70, plus X30 if X30 is T_int and Z0 if Z0 is T_int.
- The t2-part carries X40 and Z1, plus X30 if S and Z0 if S. All of these have S_23 in R6.

So **P1 = 15 + [X30 ∈ T_int] + [Z0 ∈ T_int]**.

R6's t2-vertices with S_12 in R2's interior (21..P2+P3−61) carry exactly the labels with t2 (R2, R6): c8, X50, c1 in shape R4, and Z0 if T_int. Hence **P2 + P3 = 83 + [c1 in shape R4] + [Z0 ∈ T_int]**, and P2 + P3 ≥ 84 needs at least one of the two.

|S| = u gives **u = 4 + [X30 ∈ S] + [Z0 ∈ S]**. In every case P3 = 46.

## 4. x < u is impossible

Suppose Z0 ∈ S, i.e. x < u.
- X70's t1-vertex t1[j] has j > u > x, so its F2 position 20 − j lies in Q1. Its other G2-vertex, the t3-vertex at the cut 70, is t3[ℓ2 − 15], since F1 puts t3[k] at P5 − k with P5 = 55 + ℓ2. That vertex must lie in Q0: ℓ2 − 15 ≤ 9 − x, i.e. **x ≤ 24 − ℓ2**.
- Z1's vertex t3[10−x] must lie in R7: P5 − 10 + x ≥ 71, i.e. **x ≥ 26 − ℓ2**.

These contradict each other. **So x > u, and Z0 ∈ T_int.**

## 5. The remaining cells (x > u)

With Z0 ∈ T_int: P1 = 15 + 1 + [X30 ∈ T_int], P2 + P3 = 84 + c with c := [c1 in shape R4], P3 = 46 and P2 = 38 + c.
- **Cell I-a.** X30 ∈ S: u = 5, P1 = 16, ℓ1 = 11, ℓ3 = 9, ℓ2 = 22 + c, λ = 8 − c.
- **Cell I-b.** X30 ∈ T_int: u = 4, P1 = 17, ℓ1 = 11, ℓ3 = 9, ℓ2 = 21 + c, λ = 8 − c.

In both cells x ∈ {7, 8}. The reason:
- In F2 (b6 at 0, t3[j] at j, b3 at 9, t1[j] at 20 − j), X70's t3-vertex t3[ℓ2−15] lies in Q1, so X70's t1-vertex lies in Q0: index j < x.
- v and c8 each have their other F2 incidence in Q0 (b6, and the t1-arm vertex respectively). So their R1 t1-vertices lie in Q1: j > x.
- In cell I-b, X30's t3 (R6) vertex is t3[7+c..8], which lies in Q1. So X30's t1-vertex has j < x.
- The R1 t1-indices are u+1..10. At least two of them lie above x (v, c8), and at least one (X70; two in cell I-b) lies below x. This leaves x ∈ {7, 8}.

## 6. Result

**WRITTEN:**
- In shape (b1) of v209: the classes and anatomy of §2;
- x < u is impossible (§4);
- what survives is only cells I-a (u = 5) and I-b (u = 4), with x ∈ {7, 8} and c ∈ {0, 1}.

By the mirror (v160 §1), the same holds for type 2.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2: shape (b1), cells I-a and I-b;
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
