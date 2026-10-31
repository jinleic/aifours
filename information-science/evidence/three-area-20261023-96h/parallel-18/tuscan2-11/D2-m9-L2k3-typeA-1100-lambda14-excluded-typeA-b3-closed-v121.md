# Original Tuscan-2(11), entire m = 9 distance-two branch, part 10: L2 type A cell (1,1,0,0) with λ = 14 excluded, so type A with b = 3 is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-K4-saturation-lemma-typeA-1001-excluded-v120.md` (SHA256 `ba738109b9b466f62661d0794a0061a67964f5192606adbeaa9af313b9d29e31`). Notation is that of v114–v116, and Lemma KS is v120 §1.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. The cell

Type A with b = 3, λ = 14 (so p2 = 9) and u ≤ 6. V1 lies on t1, and V2 = t2[j2] with j2 ≤ 6 − u (v115 §3).

**Offsets and lengths.**
- y1 = y0 + 4, so y0 ∈ [1, 5].
- ℓ2 = 6 + p3 − u and ℓ3 = 10 − p3 + u, with ℓ2 + ℓ3 = 16.

**F1 rows:**

| Row | Positions | Vertices |
|---|---|---|
| 1 | [10,20] | t1[u..u+10] |
| 2 | [20,30] | t1[u+10..u+14], b5, Λ[1..5] |
| 3 | [30,40] | Λ[5..13], b5, t1[u+14] |
| 4 | [40,50] | t1[u+14..u+4] |

**F2 positions** (cuts at ≡ ℓ3 − y0):
- t3[j] at j;
- b5 at ℓ3;
- Λ[k] at ℓ3 + 14 − k;
- b5 at ℓ3 + 14;
- t2[j] at 30 − j.

**Two F2 rows:**

    R_a = [ℓ3−y0, ℓ3−y0+10] = t3[ℓ3−y0..ℓ3−1], b5, Λ[13..y0+4],
    R_b = [ℓ3−y0+10, ℓ3−y0+20] = Λ[y0+4..1], b5, t2[ℓ2−1..ℓ2−6+y0].

The form of R_b holds when ℓ2 ≥ 7 − y0. Otherwise R_b contains all of t2_int, including V2, together with b5, so it has two v's. That is impossible.

## 2. Exchanges

- **Rows 1 and 4** share t1[u+4..u+10]. So L(t1[u..u+3]) = L(t1[u+11..u+14]) =: Q, and Q is saturated (Lemma KS, first step).
- **Rows 2 and R_b** share Λ[1..5] and b5. Write Y = L(t1[u+10]), the forward cut at 20. Then:

      L(Λ[6..y0+4]) ∪ L(t2[ℓ2−6+y0..ℓ2−1]) = L(t1[u+10..u+14]) = {Y} ∪ Q.

  The Λ-part has y0 − 1 vertices and the t2-part has 6 − y0. Both are paths, edge-disjoint from the t1-paths that define Q. Two Q-labels can never be adjacent on them.

## 3. Every y0 fails

- **y0 = 1.** Rows 3 and R_a share Λ[5..13] and b5. This gives L(t1[u+14]) = L(t3[ℓ3−1]). Both vertices sit on cuts (positions 40 in F1 and ℓ3 − 1 in F2), so one label has two cuts. Contradiction.
- **y0 = 2.** The t2-part has 4 vertices and the Λ-part is Λ[6]. If Λ[6] = Y, the t2-part carries Q and repeats a pair. Otherwise the t2-part carries three Q-labels and Y, against Lemma KS.
- **y0 = 3.** The edge Λ[6]–Λ[7] must contain Y. Then the 3-vertex t2-part carries three Q-labels. Contradiction.
- **y0 = 4.** The 2-vertex t2-part must contain Y. Then Λ[6..8] carries three Q-labels. Contradiction.
- **y0 = 5.** If t2[ℓ2−1] = Y, then Λ[6..9] carries Q. Otherwise Λ[6..9] carries three Q-labels and Y, against Lemma KS. Contradiction either way.

## 4. Result

**WRITTEN, (R1)–(R2) only:**
- L2 type A cell (1,1,0,0) with λ = 14 is impossible.
- With v116 (K1) and v120, **type A with b ≤ 3 is closed**: b = 2 is n1 = 2, and b = 3 means n1 = 1.

**Remaining type A cells** (b = 4, n1 = 0): (0,2,0,0), (0,1,1,0), (0,1,0,1) and (0,0,1,1). Types B, C and E, and L1 types 1–4 and 7–12, are as in v119 §4.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
