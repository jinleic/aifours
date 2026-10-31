# Original Tuscan-2(11), entire m = 9 distance-two branch, part 80: L1 type 12, r2 = 3, c′ = 1, V's on t3 and t2, t3V on an F2-cut — reduction to four explicit shapes

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type12-r2eq3-cprime1-V-on-t3-and-t2-t3V-cut-mu-below-kappa-closed-v192.md` (SHA256 `4047b88988e49a63bf5da6e1da6afe0c449177130a294c784ba56be926a857f4`). It uses the notation of v191 §1 and v192 §1:
- α = P2 − 20, β = 15 − ℓ1, μ = ℓ1 − 5, κ = 15 − ℓ2;
- t3V = t3[20−x] on the F2-cut 20 − x;
- ℓ2 + x ∈ [19,21] and x < ℓ1.

The imports are those of v191, including (G0) and (G-B) of v190 §2 transposed to the pair (R2, R3).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Two general facts for (β3)

**(P) P4 ≤ 49, so R5 is a pure t3-row.**
- If P4 ≥ 51, R4 = [40,50] lies strictly between P3 and P4, so R4 = t2[β..β+10] is a pure t2-row.
- w must meet R4. Its only G1-vertex is t2[jw] with jw < β (jw = β would put w on the cut 40), whose S_23-passage lies in R3. Its b3-passages are P1 ∈ R1 and P4 ∉ R4, and R4 has no G2-vertex.
- So w misses R4. P4 = 50 would put b3 on a cut.

Hence ℓ1 + ℓ2 ≤ 24. By v192, ℓ1 + ℓ2 ≥ 21 (case (G-B): μ > κ, α > β). So:
- **(I1′)** L(t2[1..α]) = L(Λ[κ..μ−1]) ∪ T_int ∪ {w};
- **(I2′)** L(t3[1..ℓ2−5]) = L(Λ[κ+1..μ]) ∪ L(t2[1..β]);
- **(I3′)** R2 against R3 gives L(Λ[1..μ−1]) = L(t2[β+1..α]) ∪ L(Λ[μ+1..λ−1]). Since arm labels are distinct, L(Λ[κ..μ−1]) ⊆ L(t2[β+1..α]) and L(Λ[μ+1..λ−1]) ⊆ L(Λ[1..κ−1]).

**The arm.** Call an S-label of **type I** if its arm vertex lies in Λ[κ+1..μ−1] (arm P− in R3, plus a t2-vertex in (β, α] with S_12 ∈ R2 and S_23 ∈ R4). Call it of **type II** if its arm vertex lies in Λ[μ+1..λ−1] (arm P− in R2, plus a non-arm Λ in Λ[1..κ−1] with P− in R3 and P+ in R6). The arm also holds c7 = Λ[κ] and X30 = Λ[μ]. So:
- #type I = μ − κ − 1 = ℓ1 + ℓ2 − 21;
- #type II = λ − 1 − μ = 9 − α (using α + β + λ = 20).

**(Q) Q0 against R6.** Since 10 − x ≤ ℓ2 − 5, they share b6 and t3[1..10−x], so L(t1[1..x]) = L(t3[11−x..ℓ2−5]) ∪ L(Λ[1..κ]).

## 2. x < u is impossible

If x < u, then t1[1..x] are arm vertices, so by (Q) the non-arm vertices Λ[1..κ−1] carry S-labels.
- Such a label has P− in R3 and P+ in R6 there, so its arm P− lies in R2, and it is of type II.
- Conversely, every type-II label has exactly one non-arm Λ-vertex (a second one would meet R6 twice), lying in Λ[1..κ−1] by (I3′).

So 9 − α = κ − 1 = 14 − ℓ2. Hence α = ℓ2 − 5, i.e. u = ℓ1 − 5. Then x ≤ u − 1 = ℓ1 − 6 and ℓ2 + x ≥ 19 give ℓ1 + ℓ2 ≥ 25, contrary to (P).

## 3. x > u: the labels

(x = u would put c1 on an F2-cut.)

**f1, f2 and X40.**
- Q0 holds b6 and the whole t1-arm. By the arm exchange (v173 §2), L(t1[u+1..x] ∪ t3[1..10−x]) = {w} ∪ T_int.
- So the F2-cut labels f1 := L(t1[x]) and f2 := L(t3[10−x]) lie in T_int, and every S-label is F1-cut.
- **X40 = L(t2[β]) ∈ T_int.** t2[β] covers R2 (S_12 at P2 − β > 20) and R3, R4 (cut 40). This leaves no room for an arm P−, which lies in R2 or R3.
- **X20 = L(t2[α]) ∈ S.** As a T_int label, X20 would have only T and t2[α], whose passages lie in R1, R2 and R4, so it would miss R3.

**f1.**
- R1 holds t1[x], and R5 is a pure t3-row. So f1's G2 are t1[x] and a t3-vertex of R5.
- Its two remaining G1 must cover R2, R3, R4 and R6. That forces t2[j] with β < j < α (R2, R4) and a non-arm Λ[k] with k ≤ κ − 1 (R3, R6).
- So κ ≥ 2 and ℓ2 ≤ 13.

**f2.**
- Its G2 are t3[10−x] (in R6) and a t3-vertex of R5.
- No Λ-vertex is possible, since its P+ would need R6 or R7. So its G1 are T, a t2-vertex below β (R2, R3) and a t2-vertex above α (R1, R4).

**The F1-cut T_int-labels other than X40.**
- Their G1 are T and a t2-vertex below β (R2, R3).
- Their cut is 50 or 60, as 10 and 20 are excluded. So they lie in {X50, X60}.

**S-labels.**
- A type-II label (G1 = arm and non-arm Λ) has its cut at 10 (c1) or 50 (X50). But X50 of type II would need its third G2, a t1-vertex of R1, in the pure F2-row Q1. So type II ⊆ {c1}.
- A type-I label has its cut at 10, 20 or 60. So type I ⊆ {c1, X20, X60}.
- X50 is therefore a T_int-label, and S = {c1, c7, X20, X30} ∪ ({X60} ∩ S), so u ∈ {4,5}.

**The non-arm Λ-vertices.** Among all labels, only f1 and the type-II labels have non-arm Λ-vertices, one each:
- c7 and X30 have arm and t2;
- the other T_int-labels have T and t2's.

So κ − 1 = 1 + #type II. Since #type II = 9 − α ≤ 1, α ≥ 8.

## 4. The four shapes

Write #I = ℓ1 + ℓ2 − 21 and #II = 19 + u − ℓ1 − ℓ2. Then #I + #II = u − 2 and ℓ2 = 13 − #II. This leaves exactly:

| u | ℓ1 | ℓ2 | λ | κ | μ | α | β | type I | type II | x |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 10 | 12 | 7 | 3 | 5 | 8 | 5 | {X20} | {c1} | 7, 8, 9 |
| 4 | 10 | 13 | 6 | 2 | 5 | 9 | 5 | {c1, X20} | ∅ | 6, 7, 8 |
| 5 | 11 | 12 | 8 | 3 | 6 | 8 | 4 | {X20, X60} | {c1} | 7, 8, 9 |
| 5 | 11 | 13 | 7 | 2 | 6 | 9 | 4 | {c1, X20, X60} | ∅ | 6, 7, 8 |

In every shape:
- T_int = {f1, f2, X40, X50} ∪ ({X60} if u = 4);
- P1 = 16, P2 = 16 + ℓ2, P3 = 25 + ℓ1, P4 = P3 + ℓ2 ≤ 49 and P5 = 55 + ℓ2.

## 5. Result

**WRITTEN:** L1 type 12 with r2 = 3, c′ = 1, v's V's on t3 and t2, and t3V on an F2-cut, is impossible outside the four shapes of §4 (each with x > u and the listed x). With v191 and v192, this is the whole of what survives of (β3). The same holds for the type-2 mirror image (v160 §1).

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3:
  - c′ = 0 with one V on each G2-thread;
  - c′ = 1 with V's on (t1, t2) and t1V on an F2-cut;
  - the four (β3) shapes of §4.

  These are in type-12 notation; type 2 is the mirror.
- types 1 and 11 with r1 ∈ {4,5};
- type 8 with r1 ∈ {3,4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
