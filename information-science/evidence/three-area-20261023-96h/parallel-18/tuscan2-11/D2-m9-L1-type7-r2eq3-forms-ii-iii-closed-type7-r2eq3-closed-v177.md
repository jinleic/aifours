# Original Tuscan-2(11), entire m = 9 distance-two branch, part 64: forms (ii) and (iii) of v174 are impossible, so L1 type 7 with r2 = 3 is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-lemmaA4-arm-exactness-u-ge-4-type7-formb-closed-v176.md` (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`). It uses:
- the setting, forced shape and F2-rows A, D, C of v174 §2 (SHA256 `b213df8f4eac9cd80331d6f93c56175d0bc67915e5d19c3d92c9575a70054e40`), with its addendum `D2-m9-v174-v176-addendum-1-exposition.md` (SHA256 `ad599fac24eec5636ceb20b84c0f56d9e65ce7f91b8bd8c263fdcf9b21d9b06a`);
- Lemma A4 (u ≥ 4);
- OL (two rows of either face carry each label once).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Setting

**The case.** Type 7, r2 = 3, c′ = 0, with v's G2-V on t1 (n1 = 1), in the sub-case α-i:
- A = t1[x..1], b6(0), Λ[1..10−x];
- D = Λ[10−x..λ−1], b6(λ), t3[1..y];
- C = t3[y..ℓ3−1], b3, t1[ℓ1−1..x];
- x ≠ u and y ≠ u.

**The forced shape (v174 §2).**
- P2 ∈ R3 and P3 ∈ R4, so ℓ1, ℓ3 ≤ 14.
- v = X60, and δ = ℓ1 − ℓ3 ∈ [1, 9].

**Both pure rows are present.** With u ≥ 4 (Lemma A4):
- P1 = 10 − u + ℓ1 ≤ 20, and P1 = 20 would put b3 on a cut, so **P1 ≤ 19**.
- Likewise P4 = 70 + u − ℓ3 ≥ 60, so **P4 ≥ 61**.

**R1 and R6.**
- R1 = t1[u..ℓ1−1], b3, t2[ℓ1+5..u+14], whose t2-part fills the positions P1 + 1..20.
- R6 = t2[ℓ3+5..u+14], b3, t3[ℓ3−1..u], whose t2-part fills the positions 60..P4 − 1.

**Two facts about t2.**
- **(F1)** Every t2[j] with j ∈ [ℓ1 + 5, u + 14] has its S_23-pass at P3 + j ∈ [60 + δ, P4 − 1] ⊆ [61, 69], that is, in the interior of R6.
- **(F2)** Every t2[j] with j ∈ [ℓ3 + 5, u + 14] has its S_23-pass in [60, P4 − 1]. The pass at 60 is t2[ℓ3 + 5], whose label is v.

## 2. Form (ii): x ≤ u − 1

**C against R1.**
- C's t1-part t1[x..ℓ1−1] contains R1's t1-part t1[u..ℓ1−1], and both rows contain b3.
- So R1 ∖ C = t2[ℓ1+5..u+14] and C ∖ R1 = t3[y..ℓ3−1] ∪ t1[x..u−1].
- OL gives L(t3[y..ℓ3−1]) ⊆ L(t2[ℓ1+5..u+14]).

**The contradiction.**
- Take z = t3[ℓ3−1], which lies in t3[y..ℓ3−1].
- Its F1-position P4 + 1 ∈ [62, 70] lies in R6. (If P4 + 1 = 70, z = t3[u] carries c5 on the cut 70, which still belongs to R6.)
- By (F1), L(z) also sits on a t2-vertex whose S_23-pass is in the interior of R6.
- So R6 carries L(z) twice. Impossible.

## 3. Form (iii): y ≤ u − 1 and x ≥ u + 1

**C against R6.**
- C's t3-part t3[y..ℓ3−1] contains R6's t3-part t3[u..ℓ3−1], and both rows contain b3.
- So OL gives L(t1[x..ℓ1−1]) ⊆ L(t2[ℓ3+5..u+14]).

**A against R1.**
- They share t1[u..x].
- So L(t1[1..u−1]) ∪ {v} ∪ L(Λ[1..10−x]) = L(t1[x+1..ℓ1−1]) ∪ {w} ∪ L(t2[ℓ1+5..u+14]).

**The contradiction.**
- c5 = L(t3[u]) lies in S and differs from c1, so c5 ∈ L(t1[1..u−1]).
- Hence c5 lies on t1[x+1..ℓ1−1] or on t2[ℓ1+5..u+14].
  - **c5 on t2[ℓ1+5..u+14].** By (F1), c5 has an S_23-pass in the interior of R6.
  - **c5 on t1[x+1..ℓ1−1].** By the C/R6 relation, c5 lies on some t2[j] with j ∈ [ℓ3 + 5, u + 14]. That vertex is not t2[ℓ3 + 5], whose label is v, so by (F2) c5 again has an S_23-pass in the interior of R6.
- But c5 also lies on R6 at its cut 70. Impossible.

## 4. Type 7 with r2 = 3 is closed

**The sub-cases of v's G2-V on t1 (n1 = 1):**
- α-ii, by v174 §3;
- α-i with x, y ≥ u + 1, by v174 §4, since P1 ≤ 19 and P4 ≥ 61 always hold;
- α-i with x ≤ u − 1, by §2;
- α-i with y ≤ u − 1 and x ≥ u + 1, by §3;
- x = u or y = u, which puts c1 or c5 on an F2-cut.

**The remaining cases:**
- v's G2-V on t3 (n3 = 1), by the row-reversal mirror (type 7 to type 7, exchanging t1 and t3; v155 §5, v157 §2);
- c′ = 1, and c′ = 0 with v's G2-V on Λ, by v172.

**WRITTEN: L1 type 7 with r2 = 3 is impossible.**

## 5. Result

**WRITTEN:** L1 type 7 with r2 ∈ {2, 3} is impossible (v157, and v172–v177).

**OPEN (m = 9, L1):**
- type 7 with r2 = 4 (v with a G2-V on t1 or t3; v173);
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4, 5, 6};
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19].

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
