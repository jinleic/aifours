# Original Tuscan-2(11), entire m = 9 distance-two branch, part 44: L1 type 7 with r2 = 2 is impossible

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type9-r2eq2-closed-type3-r2eq2-mirror-v156.md` (SHA256 `68723267d48a313351e1cecdce398fb5a2b1c3e34b41ed30f16eaf1c49747828`). It uses:
- the notation of v117 and v152;
- Lemmas DP-1 and DP-2 of v114 §2;
- the overlap exchange (two 11-vertex windows carrying all labels have L(R ∖ W) = L(W ∖ R));
- the mirror principle of v155 §5.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type 7: data

**Rotation and faces.**
- The b6 rotation is (T, t1, Λ+, t2, Λ−, t3), so h1 = t1 and h5 = t3.
- F1 = S_T S_12 P− S_23 and F2 = P+ S_31.
- G1 = {T, t2} and G2 = {t1, t3, Λ}.
- F1 has 2t + ℓ1 + 2ℓ2 + λ + ℓ3 positions, and F2 has λ + ℓ3 + ℓ1.

**r2 = 2.**
- Then r1 = 9, t + ℓ2 = 35 (so ℓ2 = u + 25), and λ + ℓ1 + ℓ3 = 20.
- By v152, r2 = 2 + n1 + n3 + nΛ + c′. Hence n1 = n3 = nΛ = 0 and c′ = 0. So v's cut lies in F1, and v has two V's, both on t2.

**F1 positions.**

| Position(s) | Vertex |
|---|---|
| 0 | ℓ |
| 1..t−1 | T_int |
| t | b6 |
| t + j | t1[j] |
| P1 = t + ℓ1 | b3 |
| 35 + ℓ1 − j | t2[j] (S_12) |
| P2 = 35 + ℓ1 | b6 |
| P2 + λ − k | Λ[k] |
| P3 = 55 − ℓ3 | b6 |
| 55 − ℓ3 + j | t2[j] (S_23) |
| P4 = 80 + u − ℓ3 | b3 |
| 80 + u − j | t3[j] |
| 80 + u | b6 |
| 81 + u .. 89 | T_int |
| 90 | ℓ |

**Consequences of the table.**
- The S_12-run of t2 is [11 + ℓ1 − u, 34 + ℓ1], and the S_23-run is [56 − ℓ3, 79 + u − ℓ3].
- Put δ = ℓ1 − ℓ3. The two passages of t2[j] are reflections: S_12-position p and S_23-position 90 + δ − p.
- The cuts are c1 = L(t1[u]) at 10 and c5 = L(t3[u]) at 80.

**The S-labels.** Each S-label has a t1-arm vertex and a t3-arm vertex, both in G2.
- An F2-cut label has only one G2-vertex (v152 anatomy, r2 = 2). So every S-label is F1-cut, with b = 2 (its two arms) and a = 3.
- T would repeat R0 and R8. So the three G1-vertices of an S-label are t2-vertices.

**ℓ1 ≤ 10 and ℓ3 ≤ 10.**
- In R1 = [10, 20], the S-labels other than c1, together with v, can occur only through t2-vertices.
- v's b6-corners lie at t, P2 ≥ 37, P3 and 80 + u.
- So R1 holds at least u t2-vertices, i.e. 20 − P1 = 10 + u − ℓ1 ≥ u, which gives ℓ1 ≤ 10.
- The same argument applied to R7 gives ℓ3 ≤ 10.

## 2. The double pass of t2

**Setting.** t2 has interior t2[1..u+24] and both passes in F1, so the double-pass shift is ρ ≡ δ (mod 10).
- **ρ = 0** is impossible, by DP-1.
- **ρ ∈ {1, 2, 3}** is excluded by DP-1. Its window fits for every residue, since the admissible starts form [1, u + 14 − ρ], an interval of length ≥ 12.
- **ρ ∈ {7, 8, 9}** is excluded the same way, with starts in [11 − ρ, u + 14].

**Remaining shifts.** Since ℓ1, ℓ3 ∈ [u + 1, 10], |δ| ≤ 8. So δ ∈ {±4, ±5, ±6}.

**Mirror.** Row reversal maps type 7 to type 7 with t1 and t3 exchanged (v155 §5), so it sends δ to −δ. **Assume δ ∈ {4, 5, 6}.** Then ℓ3 ≤ 10 − δ, and ℓ1 = ℓ3 + δ ≥ 6.

**Pure t2-rows.**
- R2 = [20, 30] and R3 = [30, 40] lie in the S_12-run [11 + ℓ1 − u, 34 + ℓ1], because 6 ≤ ℓ1 ≤ 10 ≤ u + 9.
- R6 = [60, 70] lies in the S_23-run [56 − ℓ3, 79 + u − ℓ3], because ℓ3 ≤ 10 ≤ u + 9.
- The S_23-images of R2 and R3 are W2 = [60 + δ, 70 + δ] and W3 = [50 + δ, 60 + δ]. Both lie inside the S_23-run:
  - 70 + δ ≤ 79 + u − ℓ3 is equivalent to ℓ1 = ℓ3 + δ ≤ u + 9;
  - 50 + δ ≥ 56 − ℓ3 is equivalent to ℓ1 ≥ 6.
- W2 and W3 carry all 11 labels.

**δ = 4.**
- R6 against W2 gives L(S_23[60..63]) = L(S_23[71..74]).
- R5 against W3 gives L(F1[50..53]) = L(S_23[61..64]).
- DP-2 with m = 4:
  - P1 = F1[50..53];
  - P1′ = S_23[61..64];
  - P2 = S_23[60..63];
  - P2′ = S_23[71..74].

**δ = 5.**
- R6 against W2 gives L(S_23[60..64]) = L(S_23[71..75]).
- R5 against W3 gives L(F1[50..54]) = L(S_23[61..65]).
- DP-2 with m = 5:
  - P1 = F1[50..54];
  - P1′ = S_23[61..65];
  - P2 = S_23[60..64];
  - P2′ = S_23[71..75].

**δ = 6.**
- R6 against W3 gives L(S_23[56..59]) = L(S_23[67..70]).
- R7 against W2 gives L(F1[77..80]) = L(S_23[66..69]).
- DP-2 with m = 4:
  - P1 = S_23[56..59];
  - P1′ = S_23[67..70];
  - P2 = S_23[66..69];
  - P2′ = F1[77..80].

**The DP-2 hypotheses hold in each case.**
- P1 and P1′ are disjoint paths.
- P2 = (y, q1, …, q_{m−1}) with y the F1-neighbour of q1.
- The edges of P2′ differ from those of P1, P1′ and P2.
  - P2′ lies at F1-positions in [71, 80]. Each of its edges occurs in F1 at its own position pair there.
  - An edge on t2 (or joining t2 to b3) occurs a second time only at an S_12 position pair inside [10, 25]. This follows from the reflection p ↦ 90 + δ − p, and from (P1, P1 + 1) ⊆ [11, 20] for the b3-edge.
  - A t3-edge occurs only once in F1.
  - P1, P1′ and P2 use only position pairs inside [50, 70].

Notation: S_23[a..b] and F1[a..b] both denote the F1-positions a..b. S_23 is written when these positions lie in the S_23-run of t2.

Each case is a contradiction.

**So type 7 with r2 = 2 is impossible.**

## 3. Result

**WRITTEN:** L1 type 7 with r2 = 2 is impossible.

**OPEN:**
- L1 type 7 with r2 ∈ {3, 4};
- types 3 and 9 with r2 ∈ {3, 4};
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
