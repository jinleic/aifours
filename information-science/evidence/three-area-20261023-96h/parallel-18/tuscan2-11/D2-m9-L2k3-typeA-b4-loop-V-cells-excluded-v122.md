# Original Tuscan-2(11), entire m = 9 distance-two branch, part 11: L2 type A with b = 4 — the two cells with a v-2-vertex on Λ are excluded

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeA-1100-lambda14-excluded-typeA-b3-closed-v121.md` (SHA256 `870aaefea5dc2f3b7151dc3f312b937e670b10ff728b82014febfdc2213229ab`). Notation is that of v114–v116, and Lemma KS is v120 §1.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. Set-up: type A, b = 4, nΛ = 1

**The cells.** These are (0,1,0,1) and (0,0,1,1). In both, n1 = 0, a = 7 and λ = 15 + p2 ∈ [16, 24]. The free offsets are p2, p3 and y0, with y1 = y0 + p2 − 5.

**F1 rows** (b5 sits at 15 and at 30 + p2; Λ[k] sits at 15 + k):

| Row | Positions | Vertices |
|---|---|---|
| 1 | [10,20] | t1[u..u+4], b5, Λ[1..5] |
| 2 | [20,30] | Λ[5..15] |
| 3 | [30,40] | Λ[15..14+p2], b5, then the walk back along t1 from t1[u+4] (t1[j] at 35 + p2 + u − j; through b4 into t2 if it runs out) |

**F2.** Λ[k] sits at ℓ3 + λ − k. The b5 that ends the Λ-pass has offset y1, so Λ[k] is on a cut exactly when k ≡ y1 (mod 10).

**Λ by Lemma OL.** Here L = λ, φΛ = 5 and ρΛ = 5 + y1. Every window of v115 §1 except ρ ∈ {4, 5, 6} contains s = 5. Also ρ = 5 would need y1 = 0. Hence:
- either **y1 = 1**, and then y0 = 6 − p2 ≥ 1 forces p2 ≤ 4 (p2 = 5 is excluded, since ρ1 ≠ 0);
- or **y1 = 9**, and then y0 = 14 − p2 ≤ 9 forces p2 ∈ {6, 7, 8, 9}.

## 2. y1 = 1

**F2 row.** The cuts of F2 on Λ fall at Λ[1] and Λ[11], so R_A = Λ[11..1] is an F2 row.

**Q.** R_A and row 2 share Λ[5..11]. So Q := L(Λ[1..4]) = L(Λ[12..15]), and Q is saturated. Also E := L(Λ[5]) ∉ Q, because Λ[5] and Λ[12..15] lie together in row 2.

**Rows 1 and 3.** They share b5 and t1[u..u+4], since p2 ≤ 4. Row 1 leaves Λ[1..5]. Row 3 leaves Λ[15..14+p2] and a path X of 5 − p2 vertices beyond t1[u]. Since L(Λ[15]) ∈ Q:

    L(Λ[16..14+p2]) ∪ L(X) = (Q ∖ {L(Λ[15])}) ∪ {E}.

**The two cases.**
- **p2 = 1.** X is a 4-path with three Q-labels. This contradicts Lemma KS.
- **p2 ∈ [2, 4].** Λ[16] is adjacent to Λ[15] ∈ Q, so L(Λ[16]) = E. The paths Λ[17..14+p2] and X then carry three pairwise-saturated labels. So each has at most one vertex, which needs p2 ≤ 3 and p2 ≥ 4 at once. Contradiction.

## 3. y1 = 9

**F2 rows.** The cuts on Λ fall at Λ[9] and Λ[19]. The F2 rows are:

    G_b = Λ[19..9],
    G_a = Λ[9..1], b5, g          (g = t2[ℓ2−1], or b4 if ℓ2 = 1),
    G_c = (a path Z of 14 − p2 vertices), b5, Λ[λ−1..19].

**Exchanges.**
- **G_b and row 2** share Λ[9..15]. So Q′ := L(Λ[5..8]) = L(Λ[16..19]), and Q′ is saturated.
- **Row 1 and G_a** share Λ[1..5] and b5. So L(t1[u..u+4]) = L(Λ[6..9]) ∪ {L(g)}. This 5-path carries the three Q′-labels of Λ[6..8]. They must be pairwise non-adjacent, so they sit on t1[u], t1[u+2] and t1[u+4]. (A fourth Q′-label would be impossible on a 5-path.)
- **Row 3 and G_c** share b5 and Λ[19..14+p2]. So, as a disjoint union:

      L(Z) = L(Λ[15..18]) ⊔ L(t1[u+p2−5..u+4]).

  Here t1[u+4] ∈ Q′. Disjointness from Λ[16..18] forces L(t1[u+4]) = L(Λ[19]). So Z carries all four Q′-labels, pairwise non-adjacent.

**The two cases.**
- **p2 ≥ 8.** Then Z has at most 6 vertices, too few for four non-adjacent vertices. Contradiction.
- **p2 ∈ {6, 7}.** Then t1[u+2] lies in t1[u+p2−5..u+4], and its Q′-label lies in L(Λ[16..18]). That breaks the disjoint union. Contradiction.

## 4. Result

**WRITTEN, (R1)–(R2) only:** L2 type A cells (0,1,0,1) and (0,0,1,1) are impossible.

**Type A residual:** only the b = 4 cells with nΛ = 0, namely (0,2,0,0) and (0,1,1,0), with λ = 5 + p2 ∈ [6, 14].

Types B, C and E, and L1 types 1–4 and 7–12, are as in v119 §4. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
