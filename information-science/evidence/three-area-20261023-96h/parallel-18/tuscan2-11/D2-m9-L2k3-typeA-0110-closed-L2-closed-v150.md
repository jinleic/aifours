# Original Tuscan-2(11), entire m = 9 distance-two branch, part 38: type A (0,1,1,0) closed, so every cell of L2 (k = 3) is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeA-0200-slot-lemma-delta5-closed-v149.md` (SHA256 `733bc33fb9cda5468a13e91d15dd2191822526dd4bbc4b84abc2148a8a4854a7`).

Imports:
- the type A anatomy and Rules A1–A2 of v148 §1–2;
- DP-1 and DP-2, v114 §2;
- RC, v134 §1;
- D2Q (v125 §1) and R3-pair (v130 §1), both of which use (R3).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up

**Parameters.**
- p1 = 5, n2 = n3 = 1, a = 7, b = 4.
- ℓ1 = 5 + u and λ = 5 + p2.
- ℓ2 = A + p3, where A = 15 − p2 − u.
- ℓ3 = 20 − p3 + u.

**F1 rows** (b5 at 15, 20 + p2 and 40 + p3):

| Row | Vertices |
|---|---|
| R0 | ℓ, T_int, b4, t1[1..u] |
| R1 | t1[u..u+4], b5, Λ[1..5] |
| R2 | Λ[5..4+p2], b5, t1[u+4..u+p2−5] |
| R3 | t1[u+p2−5..1], b4, t2[1..A] |
| R4 | t2[A..ℓ2−1], b5, t3[ℓ3−1..u+10] |
| R5 | t3[u+10..u] (pure) |
| R6 | t3[u..1], b4, T_int, ℓ |

- The F1 cuts are v, c1, λ5\*, τ3, α (t2[A]), ζ (t3[u+10]) and c2 (t3[u]).
- V_2 lies in R3 and V_3 in R5.

**F2 rows.**
- q0 = t3-tail, b5 (y0), Λ[λ−1..y1].
- q1 = Λ[y1..1], b5 (10+y1), then t2 downward.
- After that come the rest of t2, then b4 at K := 10 + y1 + ℓ2, then t3.
- V_2 lies in q2 and V_3 in q3.

**Lemma S′ (as v149 Lemma S).** α, ζ and c2 each need a distinct R2-slot. If u + p2 ≥ 5, the slots are t1[u+p2−4..u−1] (4 − p2 vertices) and Λ[6..4+p2] (p2 − 1 vertices), three in all, less Λ[y1] when y1 ≥ 6. So **y1 ≤ 4** whenever u + p2 ≥ 5.

## 2. K ≤ 29: q3 = t3[s..s+10] is pure, with s = 30 − K

**The shift.** R5 and q3 are pure t3-rows of opposite direction. Put δ3 := s − u. DP-1 leaves δ3 ∈ {±4, ±5, ±6}.

**δ3 ∈ {±5, ±6}: DP-2 chains**, exactly as in v146 §2.
- For δ3 > 0: R5 with q2 = t2[K−20..1], b4, t3[1..s], and R4 with q3.
- For δ3 < 0: R6 with q3, and R5 with q0.

**δ3 = 4.** Exchanging R5 with q3 gives the saturated block Q, with P = t3[u..u+3] (in R5 and q2) and P′ = t3[u+11..u+14] (in R4 and q3; its end t3[u+14] carries γ, the q3/q0 cut label).
- Every S-label other than c2 has its t3-arm in q2, as does P.
- v ∉ Q, and w ∉ Q because b4 also lies in q2.
- So Q ∖ {c2} consists of T_int-labels. Their only possible cuts are λ5\* (F1) and γ (F2).
- The cut label λy\* at Λ[y1] would need one t1-vertex with passages in R3 and in R1 or R2, which is impossible.
- Hence |Q| ≤ 3. Contradiction.

**δ3 = −4.** Here u = s + 4 ≥ 5, so Lemma S′ gives y1 ≤ 4.
- **The block.** P = t3[u−4..u−1] lies on the t3-arm, so Q ⊆ S. Its first vertex carries γ1 (the q2/q3 cut), and P′'s last vertex carries ζ.
- **Exclusions.** λ5\* is excluded, since it would need y1 > 5. c2 is excluded, since t3[u] lies in q3 with P.
- **Candidates.** The remaining candidates are τ3, c1, α and κ = L(t2[K−20]), the q1/q2 cut label. RC gives:
  - α and ζ: a t1-arm vertex reaching R2, plus Λ ∈ R1 ∩ q1;
  - κ: {t1-arm (R0, R3), t1[j] (R1, R2), t2[K−20] ∈ R4, P, P′};
  - γ1: {t1-arm (R0, R3), t1[j′] with u < j′ ≤ u+4 (R1, R2), t3[u−4], P′, t2 ∈ R4 ∩ q1}.
- **The relation p3 = 9 + p2 − y1.** κ needs K − 20 > A, which means p2 ≥ 2. When p2 = 1, t2[A] would carry two cuts.

The pairs completing Q = {γ1, ζ, ·, ·}:

| Pair | Why it fails |
|---|---|
| {c1, τ3} | ζ needs a position in R2's arm range [p2+7, 10] non-adjacent to c1 (position p2 + 6) and to τ3 (position 11). That leaves [p2+8, 9]. For p2 ≥ 2 this is empty. For p2 = 1 it forces positions 7, 9, 11, two gaps of 2 sharing a label, against D2Q. |
| {c1, α} | ζ and α need non-adjacent positions in [p2+8, 10], which has 3 − p2 < 3 positions. |
| {τ3, α} | ζ and α need non-adjacent positions in [p2+7, 9], which has 3 − p2 < 3 positions. |
| {κ, α} | Needs p2 = 1, which is excluded. |
| {κ, c1} | In R2, κ and γ1 occupy non-adjacent vertices of t1[u+2..u+4], away from c1. This forces positions t1[u+4], t1[u+2], t1[u]: two gaps of 2 sharing a label, against D2Q. |
| {κ, τ3} | See below. |

**The pair {κ, τ3}.**
- In R0, ζ's arm vertex must avoid τ3's t1[u+p2−5], which forces p2 = 2 and ζ = t1[u−1].
- Then τ3 and ζ are both Λ ∈ R1 ∩ q1 inside Λ[1..y1−1] and non-adjacent, which forces y1 = 4 and the vertices {Λ[1], Λ[3]}.
- So the pair {τ3, ζ} is realised at distance two in both orders at Λ[2], and again at t1[u−2], where t1[u−3] and t1[u−1] carry τ3 and ζ.
- Both middles are non-cut 2-vertices, so R3-pair gives a contradiction.

## 3. K ≥ 30

**K = 30.** b4 lies on the q2/q3 cut.
- R5's blocks against q3 and q0 have sizes u and 10 − u, so DP-1 gives u ∈ {4, 5, 6}.
- R3 against q2 gives a block of size u + p2 − 5. Size 0 puts t2[10] on two cuts, so u + p2 ≥ 9.
- Then K = 10 + y1 + ℓ2 = 30 gives p3 = 5 + p2 + u − y1 ≥ 5 + 9 − 4 = 10, using Lemma S′. Contradiction.

**K ≥ 31.** q2 = t2[K−30..K−20] is pure. Exchanging q2 with R4 and R3, and R5 with q0 and q3, gives four blocks:
- size e = 20 − p3 − y1, and its complement 10 − e;
- size d3 = 15 − p3 + p2 − y1, and its complement 10 − d3.

DP-1 gives e, d3 ∈ {4, 5, 6}, and d3 = e + p2 − 5.
- If u + p2 ≥ 6: Rule A1 gives p2 ≤ 4 and Lemma S′ gives y1 ≤ 4. Then p3 = 20 − e − y1 ≥ 10. Contradiction.
- If u + p2 ≤ 5: then p2 ≤ 3, and d3 ≥ 4 forces p2 = 3, u = 2 and e = 6. So u + p2 = 5, Lemma S′ applies, and y1 ≤ 4. Then p3 = 14 − y1 ≥ 10. Contradiction.

## 4. Result

**WRITTEN, uses (R3) through D2Q and R3-pair at δ3 = −4:** type A (0,1,1,0) is impossible.

**Hence every cell of L2 (k = 3) is closed:**

| Type | Closed principally in |
|---|---|
| A | v114, v120–v122, v148–v150 |
| B | v123, v143–v147 |
| C | v128–v137, v142 |
| E | v124–v128, v132–v134, v138–v141 |

The cross-type packets v116 and v124 also contribute.

**OPEN in the m = 9 branch:** L1 types 1–4 and 7–12 (types 5 and 6 are closed in v118, L4-B in v113). So the support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
