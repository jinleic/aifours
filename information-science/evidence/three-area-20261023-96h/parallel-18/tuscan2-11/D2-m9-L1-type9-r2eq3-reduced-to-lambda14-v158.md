# Original Tuscan-2(11), entire m = 9 distance-two branch, part 45: L1 type 9 with r2 = 3 is reduced to λ = 14 (types 3 and 9 by the mirror)

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type7-r2eq2-closed-v157.md` (SHA256 `458dce9de731858686a408c773870eb593a854937e2f5b1f46ac08bb40c724f2`). It uses:
- the type-9 position table of v156 §1;
- the v152 anatomy;
- Lemmas DP-1 and DP-2 of v114;
- the overlap exchange;
- the mirror principle of v155 §5.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Data for type 9 with r2 = 3

**Dimensions.** r1 = 8, t + ℓ1 = 25 (so ℓ1 = u + 15), and ℓ2 + ℓ3 + λ = 30.

**F1 positions (v156 §1).**
- B1 = 25 is b3.
- C1 = 25 + ℓ2 is b6.
- B2 = 55 − λ is b3.
- C2 = 70 + u − λ is b6.
- C3 = 70 + u is b6.
- t1[j] lies at 10 − u + j (S_12) and at C2 − j (S_31).
- Λ[k] lies at C2 + k (P+), so Λ[λ−u] is the cut at 70.

**Rows.** R1 = t1[u..u+10] is a pure forward t1-row, and R7 = R_in.

**v's parameters (v152).**
- r2 = 2 + n2 + n3 + nΛ + c′ = 3 and r1 = 8.
- Either c = 1, n1 = 1 and one G2-V; or c′ = 1, n1 = 2 and no G2-V.

**Anatomy.** An F1-cut label has a = 2 G1-vertices and b = 3 G2-vertices; an F2-cut label has a = 3 and b = 2. Here G1 = {T, t1}.

## 2. The admissible λ

**The shift.** The double pass of t1 has ρ ≡ −λ (mod 10). Its interior is t1[1..u+14].
- **ρ = 0** puts t1[u]'s S_31-passage on a cut.
- **ρ ∈ {1, 2, 3}** is killed by DP-1 with R1 and the backward row t1[u+ρ..u+ρ+10].
- **ρ ∈ {7, 8, 9}** is killed by DP-1 with R1 and the backward row starting at index u + ρ − 10. When that index is ≤ 0, the row continues through b6 = C2 into P+. Then the C-difference is the path t1[u−1..1], b6, Λ[…] of size 10 − ρ:
  - for size 1, the same label sits on two cuts;
  - for sizes 2 and 3, (E) applies, the two difference paths being disjoint.
- **ρ = 5** puts b3 at B2 ≡ 0, on a cut.
- So λ ≡ 4 or 6 (mod 10).

**λ ≥ 12 (from c5).**
- c5's t1-arm vertex t1[j5] (j5 ≤ u − 1) passes at C2 − j5.
- This passage must avoid R6 and R7 (c5's cut at 70) and the cut at 60. So 70 + u − λ − j5 ≤ 59, which gives λ ≥ 12.

**λ ≤ 24.**
- For 25 < λ < 35, both b3-corners B1 = 25 and B2 lie in R2. That puts w twice in R2.
- λ = 25 puts b3 on the cut 30.

**Hence λ ∈ {14, 16, 24}.**

## 3. λ = 16 is impossible

**Rows.** B2 = 39 and C2 = 54 + u. So R4 = [40, 50] = t1[u+14..u+4] is a pure backward t1-row, and t1[u+14] is the cut at 40.

**Two kinds of label.**
- R1 ∩ R4 = t1[u+4..u+10]. Every label lies in R1 and in R4, once each. So each label is of one of two kinds:
  - **(A)** it has a vertex in t1[u+4..u+10];
  - **(B)** it has a vertex in t1[u..u+3] and a vertex in t1[u+11..u+14].
- The label X of the cut vertex t1[u+14] sits in R4 at 40. So it has no vertex in t1[u+4..u+10] ⊆ R4, and it is of kind (B).

**X is impossible.**
- X is F1-cut (at 40).
- If X ∉ {v, w}, its two G1-vertices are t1[u+14] and some t1[i] with i ∈ [u, u+3]:
  - i = u makes X = c1, which has its cut at 10;
  - otherwise X carries neither T nor a t1-arm vertex (index ≤ u), so X is neither a T_int-label nor an S-label.
- X ≠ w, because w's cut is ℓ.
- X = v would need c = 1 together with two t1-V's, against n1 = 1 when c = 1.

**So λ = 16 is impossible.**

## 4. λ = 24 is impossible

**Rows.** B2 = 31 and C2 = 46 + u.
- R2 = t1[u+10..u+14], b3 (25), then positions 26..30 (t2, b6 = C1, t3, ending at the cut vertex at 30).
- R3 = (vertex at 30), b3 (31), t1[u+14..u+6] (32..40).
- R4 = [40, 50] is:
  - t1[u+6..1], b6, Λ[1..4−u] when u ≤ 4;
  - t1[u+6..u−4] when u ≥ 5.

**Exchanges.**
- R2 and R3 share t1[u+10..u+14], b3 and the vertex at 30. So L(positions 26..29) = L(t1[u+6..u+9]).
- R1 and R4 share t1[u..u+6]. So L(t1[u+7..u+10]) = L(Q), where Q is the 4-path R4 ∖ R1:
  - Q = (t1[u−1..1], b6, Λ[1..4−u]) when u ≤ 4;
  - Q = t1[u−4..u−1] when u ≥ 5.

**DP-2 with m = 4.**
- P1 = positions 26..29 (a path of t2-, b6- and t3-vertices);
- P1′ = (t1[u+9], t1[u+8], t1[u+7], t1[u+6]);
- P2 = (t1[u+10], t1[u+9], t1[u+8], t1[u+7]);
- P2′ = Q.

**The DP-2 hypotheses hold.** The edges of Q are t1-edges between indices ≤ u − 1, the edge t1[1]–b6 at C2, b6–Λ[1] and Λ-edges. None of these is an edge of P1, P1′ or P2.

**So λ = 24 is impossible.**

## 5. Result

**WRITTEN:**
- L1 type 9 with r2 = 3 survives only with **λ = 14** (so ℓ2 + ℓ3 = 16, B2 = 41, C2 = 56 + u).
- By the mirror (v156 §3), the same holds for type 3 with r2 = 3.

**OPEN:**
- types 3 and 9 with r2 = 3 and λ = 14;
- types 3 and 9 with r2 = 4;
- type 7 with r2 ∈ {3, 4};
- types 2 and 12 with r2 ∈ {2, 3, 4};
- types 1, 8 and 11 (v152 restrictions).

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
