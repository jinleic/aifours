# Original Tuscan-2(11), entire m = 9 distance-two branch, part 42: L1 type 10 with r2 = 2 is impossible, so L1 types 10 and 4 are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues:
- `D2-m9-L1-type10-r2eq3-closed-v153.md` (SHA256 `66dcb38b10aad43f86c32f09d2f47f11ba2929163fd208d7cc5bbab29e7902b0`), whose §1 position table is used here;
- `D2-m9-L1-type4-r2eq3-closed-types4-10-r2eq2-only-v154.md` (SHA256 `31797e84f74a22b11243515d606373b7388bc885280ae9f55b609d1a5896b7fa`).

The tools are row coverage (each label once per row, one cut per label), the v152 anatomy and the overlap exchange (Lemma OL of v115 in its plain form):

> If two 11-vertex windows W and R each carry all 11 labels, then L(R ∖ W) = L(W ∖ R).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type 10 with r2 = 2: data

**Rows.** r1 = 9, so F1 has rows R0..R8 with R8 = R_in. F2 = S_23 has 20 positions, so ℓ2 + ℓ3 = 20. F1 has 90 positions, so t + ℓ1 + λ = 35.

**Positions (v153 §1).**
- P1 = t + ℓ1 = 10 + (ℓ1 − u)
- P2 = P1 + ℓ2
- P3 = P2 + λ = 55 − ℓ3
- P4 = 55
- P5 = 55 + ℓ1
- c1 = L(t1[u]) is cut at 10.
- c5 = L(Λ[λ−u]) is cut at 80, so P5 + λ − u = 80 and **λ = u + 25 − ℓ1**.

**Front and tail.**
- Every G2-vertex (t2 or t3) lies before 55.
- Every t1-vertex has one front passage (S_12, before P1) and one tail passage (S_31, at 55 + ℓ1 − j).
- Every Λ-vertex has one front passage (P−, at P2 + λ − k) and one tail passage (P+, at P5 + k).
- T covers R0 and R8.
- The arm vertices t1[1..u] and Λ[λ−u..λ−1] carry exactly S.

**Anatomy (v152, G3 = ∅, r2 = 2).** An F1-cut label has a = 3 G1-vertices and b = 2 G2-vertices. An F2-cut label has a = 4 and b = 1.

**Lemma C1.** ℓ1 − u ∈ [6, 14], and t1[u] passes in R6.
- c1 consists of t1[u], a Λ-arm vertex (in R8 by P+), one more G1-vertex g and two G2-vertices.
- g ≠ T, because R0 is already covered by the cut at 10.
- So R6 and R7 are covered by the S_31-passage of t1[u] (at 55 + ℓ1 − u) and the tail passage of g, one each.
- Suppose t1[u] passed in R7. Then every arm vertex t1[j] with j < u would pass after 70. In particular the t1-arm vertex of c5 would land in R7 or R8, which c5's cut at 80 already covers. That is impossible.
- Hence 60 < 55 + ℓ1 − u < 70.

**Lemma C5.** Suppose every arm passage 55 + ℓ1 − j (1 ≤ j ≤ u) lies in R6. Then c5 = {Λ[λ−u], its t1-arm vertex, one slot vertex t1[i] with i ∈ [ℓ1−4, ℓ1−1], two G2-vertices}. In particular **Λ[λ−u] is c5's only Λ-vertex**.
- The cut of c5 covers R7 and R8, and its arm covers R0 and R6.
- Its third G1-vertex is not T (R0, R8). Its tail passage must lie in R5, which is possible only at 56–59, i.e. at t1[ℓ1−1..ℓ1−4]. P+ starts at 56 + ℓ1 ≥ 62.

**The three cases.** By Lemma C1, ℓ1 ≤ 14 (case A), ℓ1 = 15 (case B) or ℓ1 ≥ 16 (case C).

## 2. Case A: ℓ1 ≤ 14

**Setup.**
- P5 ≤ 69, so R7 = [70, 80] is the pure P+-run Λ[15−ℓ1..25−ℓ1].
- Every arm passage lies in [55 + ℓ1 − u, 54 + ℓ1] ⊆ [61, 68], inside R6. So Lemma C5 applies.
- **e7 := L(Λ[15−ℓ1]) is not an S-label.** Its cut at 70 covers R6, where every S-label already sits through its arm.

**The window W.**
- Let π = P2 + u, the P−-position of Λ[λ−u].
- The P−-positions of the R7-vertices form the window W = [π, π + 10]. Here π + 10 = P2 + u + 10 ≤ P3 − 1 because λ ≥ u + 11.
- W carries all 11 labels, with c5 at π and e7 at π + 10.
- π is not a cut (c5 has its cut at 80). So π = 10a + r with 1 ≤ r ≤ 9, and W meets R_a and R_{a+1}.
- OL gives two exchanges:
  - (OL-a) L([10a, π − 1]) = L([10a + 11, π + 10]);
  - (OL-b) L([π + 11, 10a + 20]) = L([π, 10a + 9]).
- In P−, Λ[λ−u+1..λ−1] lies at [π − u + 1, π − 1], b6 lies at P2 = π − u, and b6 lies at P3 = π + 25 − ℓ1 ≥ π + 11.

**(i) P3 ≤ 10a + 20.**
- Then P3 ∈ [π + 11, 10a + 20], so v lies in the left side of (OL-b). Hence v ∈ L([π, 10a + 9]).
- If r ≥ u, then P2 ∈ [10a, π − 1], so by (OL-a) v ∈ L([10a + 11, π + 10]). Now v occurs twice in W, which is impossible.
- If r ≤ u − 1, then [10a, π − 1] lies inside the Λ-arm run, so the left side of (OL-a) is ⊆ S. But the right side contains e7 (at π + 10), which is not an S-label. Impossible.

**(ii) P3 > 10a + 20.**
- [π + 11, 10a + 20] lies inside P− and carries Λ-vertices other than Λ[λ−u].
- By (OL-b), c5 (at π) has such a Λ-vertex. This contradicts Lemma C5.

**Case A is impossible.**

## 3. Case B: ℓ1 = 15

**Setup.**
- P5 = 70, so v's cut lies at the b6-corner P5 (c = 1, c′ = 0). Hence n2 + n3 = 1 and n1 + nΛ = 1.
- R6 = t1[10..1], b6, and every arm passage 70 − j lies in R6. So Lemma C5 applies.

**The slots t1[11..14] (S_31-positions 56–59) are taken by exactly v, c5 and the two non-v F2-cut labels.**
- **v.** b6 covers R0 (corner t), R6 and R7 (the cut at P5) and R8 (corner P6). So the single tail passage of v's G1-V cannot lie in R6–R8. It cannot lie at 60 either (a second cut), and P+ starts at 71. Hence it lies at 56–59, which is a slot.
- **c5.** It holds a slot by Lemma C5.
- **Each non-v F2-cut label X (two of them, since c′ = 0).**
  - If X ∈ T_int, T covers R0 and R8, and its three G1 tails lie in three distinct rows among R5, R6 and R7, one in each. The R5 tail lies at 56–59.
  - If X ∈ S, its arms cover R0, R6 and R8, and its two further G1 tails lie in R5 and R7, one in each. The R5 tail lies at 56–59.
  - Either way X holds a slot.
- These are four distinct labels on four slots, and none of them has an F1-cut at 20: v is cut at 70, c5 at 80, and X has its cut in F2.

**The window W′.**
- The vertices of R6 (b6 and t1[1..10]) also form the window W′ = [t, t + 10] of S_T S_12.
- W′ ∖ R1 = [t, 9] carries v and S ∖ {c1}, and R1 ∖ W′ = [21 − u, 20].
- If u ≥ 5, then b3 (at P1 = 25 − u ≤ 20) lies in R1 ∖ W′, so by OL w ∈ {v} ∪ S. Impossible.
- So u ≤ 4. Then position 20 is t1[10 + u], a slot vertex with an F1-cut at 20. By the slot census above, no such label exists.

**Case B is impossible.**

## 4. Case C: ℓ1 ≥ 16

**Setup.** P5 ≥ 71, so R6 = [60, 70] is the pure S_31-run t1[ℓ1−5..ℓ1−15]. Its S_12-positions form the window W′ = [P1 − 15, P1 − 5], where P1 = 10 + (ℓ1 − u) ∈ [16, 24].

**Exchange with R1.**
- W′ ∖ R1 = [P1 − 15, 9] carries t1[ℓ1−15..u−1], which are arm vertices, so its labels lie in S.
- R1 ∖ W′ = [P1 − 4, 20].
- If P1 ≤ 20, then b3 ∈ R1 ∖ W′ and w ∈ S, which is impossible. So P1 ∈ [21, 24].
- Then R1 ∖ W′ consists of t1-vertices, and the cut vertex at 20 is t1[20 − t]. Its label f2 lies in S.

**The label f2.**
- Since 20 − t > u, t1[20 − t] is not an arm vertex. So f2 has exactly three G1-vertices: its t1-arm vertex, its Λ-arm vertex and t1[20 − t].
- Its tail passages are:
  - one arm passage (in R6 or R7);
  - Λ-arm (R8);
  - t1[20 − t] at 35 + P1 ∈ [56, 59] (R5).
- So one of R6 and R7 is not covered. Impossible.

**Case C is impossible.**

## 5. Type 4 by the mirror

**Reversal.** Reversing every row of an eligible array gives an eligible array. It reverses every face walk, so it mirrors the rotation system and keeps T, ℓ, v = b6, w = b3, r1 and r2 (v117 §2: the type list is closed under the mirror).

**Type 4 goes to type 10.**
- Start from type 4: b6 rotation (T, Λ+, t1, t3, Λ−, t2) and b3 rotation (t1, t2, t3).
- The mirror is (T, t2, Λ−, t3, t1, Λ+) with b3 rotation (t3, t2, t1).
- Rename Λ+ ↔ Λ− and t1 ↔ t2. Then b3 becomes (t3, t1, t2) = (t1, t2, t3) cyclically, and b6 becomes (T, t1, Λ+, t3, t2, Λ−), which is type 10.

So a type-4 array with r2 = 2 would mirror to a type-10 array with r2 = 2, which §§2–4 exclude.

## 6. Result

**WRITTEN:**
- L1 type 10 with r2 = 2 is impossible.
- With v152 (r2 ≤ 3), F0 (r2 ≥ 2), v153 and v154: **L1 type 10 and L1 type 4 are impossible.**
- Type 4 with r2 = 2 is settled through the mirror of §5. Type 4 with r2 = 3 has the direct proof of v154.

**OPEN:** L1 types 1–3, 7–9, 11 and 12 (v152 restrictions). The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
