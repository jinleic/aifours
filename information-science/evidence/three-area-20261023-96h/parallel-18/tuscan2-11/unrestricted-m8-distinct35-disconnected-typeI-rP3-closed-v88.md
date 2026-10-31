# Actual Tuscan11 distinct 3+5, disconnected, Type I with r_P = 3 — the remaining two/one cases excluded, so Type I is closed

Actual `/bin/date` before this body: **Mon Oct 26 12:36:49 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

| Packet | SHA256 | Used for |
|---|---|---|
| v80 | `e7c267afe00cb5c6909162da1d97ac4c93f30b875ca295badd0ff24ad2822dd2` | Lemma B |
| v82 | `f62ba5909ef95b4529296bd977bc69b6fd7c0c6bf7a6e6dc7e643115caa74c08` | notation; two/one reductions; one/one excluded |
| v87 | `0c605172ac121a374293603c33a51784a41c52aeb55fc278b6efac1b3a77f58b` | pure variant: (3,7) and (2,8) excluded; through-b_w variant defined |
| v81 | `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08` | Lemma L; offset lemma |
| v77 | `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7` | Lemma U; pair uniqueness |

Pair uniqueness implies that the labels adjacent to the v-vertices are pairwise distinct, and likewise for the w-vertices.

## 2. The through-b_w variant is impossible (all four pairs)

In this variant P's rows are:
- R_P0 = D[π..t−1], w, C[z−1..1], v, A[1..p];
- R_P1 = A[p..p+10], inside A;
- R_P2 = A[p+10..x−1], w, D[1..π].

**Where the copies lie** (by Lemma W):
- R_P0's w is b_w, so a_w ∉ A[1..p]. Hence a_w ∈ (p, 10−b1).
- The cross v-copies are u (on D, with ω < u < π) and v3. R_P1 needs a v, which can only be v3. So v3 ∈ A(p, p+10), and also v3 ∈ A(10−b1, x) because it is Q3's v.
- The offset lemma on R_P2/Q1 gives π ≤ ω+6 = g1+1 ≤ 9. Hence x−1 = 19+p−π ≥ p+10 > v3.

**There is no v–w edge in H:**

| v-vertex | w-vertex | Why not adjacent |
|---|---|---|
| b_v | b_w | A, B and C all have length > 1 |
| b_v | s_w | s_w > b1 ≥ 2 |
| b_v | a_w | a_w > p ≥ 1 |
| s_v | b_w | s_v < b1+10 ≤ 13 |
| u | b_w | u ∉ {1, t−1}, since ω ≥ 2 and u < π ≤ t−1 |
| v3 | b_w | v3 < x−1 |
| s_v | s_w | separated by the O-cut B[g1] |
| v3 | a_w | separated by the O-cut A[10−b1] |

D carries no w-copy. This contradicts Lemma U (exactly one v–w edge). **The through-b_w variant is impossible.**

## 3. Pure variant, (b1, g1) = (3, 8): excluded

Here t = 11 and ω = 3.
- 𝒪_L = L(D[1..3]) = {o_b, ℓD3, o3} and 𝒪_U = L(C[1..2]).
- The six O-cuts force ℓA7 = o3.
- Q1 = B[13..14], w, D[10..3] forces o3 ∈ L(D[4..10]).

So o3's three cross-path vertices are D-lo, D-hi and A7, and it has no C-vertex.

R_P0 against Y0 gives L(C[3..j]) ⊔ L(A[1..p]) = L(B[1..8]) ∋ o3. But p < 7, so A7 ∉ A[1..p]. **Contradiction.**

The general pattern: whenever g1 = 8 in the pure variant, the label ℓA[10−b1] = o3 has no vertex in R_P0. v87 §3 is the case b1 = 2.

## 4. Pure variant, (b1, g1) = (2, 7): excluded

Here t = 9 and ω = 2.

**Fixed structure.**
- D1 = o_b and D2 = ℓD2.
- B[3..6] carries {w, pA, pC, ℓD2}, with B3 ∈ {pA, pC}, because both pairs {o_b, w} and {o_b, ℓD2} are already used.
- The lower vertices of pA and pC are not adjacent, because B13–B14 = {pA, pC}.

**w already meets pA and pC.** In each of the eight admissible orders of B[3..6], s_w's two neighbours contain exactly one of pA, pC, and B14 is the other. So w is already adjacent to both pA and pC.

**Constraints on A.** R_P0 against X0 gives 𝒪_U ⊆ L(A[p+1..8]) and A[1..p] ⊆ {w, pA, ℓD2, ℓB7}, with A[p] = pA and the A w-copy in A[1..p−1].

**The case p = 2.** Then a_w = A1 sits next to A2 = pA, which repeats the pair {w, pA}.

**The case p ≥ 3.** Here a_w = A1 is forced: every other position puts a_w next to pA or next to s_w's other neighbour. So b_v–A1 is the unique v–w edge. The exchanges with Y0 and with Q1 (that is, R_P1 against B[7..14]) then fix A[p..8] and D[3..π].
- **p = 3:**
  - x = 9 forces u = D3 next to D4 = pD, which repeats v–pD (b_v–B1).
  - x = 10 puts v at A[x−1], a second v–w edge.
- **p = 4, x = 9:**
  - u = D3 is forced.
  - The v- and w-neighbour budgets force C7 = v, C8 = pA and C11 = o*.
  - That leaves C[9..10] carrying {ℓD2, ℓB7}, the same pair as A[2..3]. Contradiction.
- **p = 4, x = 10:** u = D3 is next to D4 = pD, which repeats v–pD.
- **p = 4, x = 11:** A10 = ℓB7 is next to b_w, which repeats the pair {w, ℓB7}.

Every case fails.

## 5. Result

v87 and §§3–4 exclude the pure variant for all four pairs (b1, g1). §2 excludes the through-b_w variant. So **the two/one sub-case is impossible.** By the Type I reversal symmetry (v80 §4), so is the one/two sub-case.

The other sub-cases are already closed: two/two by Lemma B (v80) and one/one by v82. **Type I with r_P = 3 is therefore impossible.** Together with v60 (r_P = 2) and v81 (r_P = 4), **every Type I configuration is excluded** (WRITTEN).

**Owner-written residual** (assuming the unreviewed bodies v47–v88 are correct):
- R1–R4 are empty.
- R5 is reduced to **Type II with r_P = 2**.
- R6: all m ≥ 9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
