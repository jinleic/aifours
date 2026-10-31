# Original Tuscan-2(11), entire m = 9 distance-two branch: shape (b2) of v209 with u = 5 is impossible

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It is written only from the author's own unquarantined material (Main v215).

It continues `D2-m9-L1-types12-2-r2eq2-shape-b2-u6-closed-v211.md` (SHA256 `248fa30bebd5fad12cb6a278a693c79ec8d5e78e64776a6a313d1dfd0e873a8f`) and uses its conventions and imports.

It uses (R1)–(R2) only. It is written reasoning only: no interpreter, enumeration, program or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The fourth T_int-label

With u = 5, |T_int| = 4 ⊇ {X30, X40, Z1} (v210). The fourth label τ is one of X50, X60, X70 or Z0.

**τ ≠ Z0, and x < u.** If x > u, v204 §2 (ii) puts Z0 in T_int. Its only G2-vertex t1[x] then lies in R1, so R6 must be met by a G1-vertex. The only candidate is a t2-vertex with S_23 in R6, whose S_12 lies in R1. But R1 is already taken. So x < u and Z0 ∈ S.

**τ ≠ X60.** X60 would cover R0, R8 (T) and R1, R5, R6 (cut vertex). That leaves R2, R3, R4 and R7 for one G1-vertex and two G2-vertices. Only R7 holds G2-vertices, so the two G2-vertices cannot both be placed.

**So τ ∈ {X50, X70}, with forced anatomy:**
- τ = X50: T, t2[50−P3] (cut), Λ (R3, R7), a t1-vertex in R1, t3 in R6;
- τ = X70: T, t3 at the cut 70, t2 (R2, R5), t2 (R3, R4), a t1-vertex in R1.

The other labels have the anatomy of v211 §2, including Z1 (α) or (β).

## 2. Positions

R1 must receive eight labels besides c1, v and w:
- X40 and τ arrive through t1-vertices;
- the other six arrive through the t2-part.

So P1 = 13, ℓ1 = 8, P3 = 43, and t1[6], t1[7] carry {X40, τ}. These are adjacent, so **the pair {X40, τ} is used**.

As in v211, count the R6-side of R1's t2-part, the positions 14..k60−1:

| case | R6-side labels | k60 | P2 | status |
|---|---|---|---|---|
| (X50, α) | Z0 | 15 | 32 | continued below |
| (X50, β) | Z0, Z1 | 16 | 33 | excluded below |
| (X70, α) | Z0, X50 | 16 | 33 | continued below |
| (X70, β) | Z0, X50, Z1 | 17 | — | impossible, since P2 + P3 ≤ 76 |

**(X50, β).** Here ℓ2 = 20 and P5 = 75, so t3[k] sits at 75 − k. Z1's vertex t3[10−x] would lie in R7 (positions 71..74) only if x ≥ 6, which contradicts x < u.

**Facts used below.**
- In F2, the t1-vertices t1[6], t1[7] and c1's t1[5] lie in Q1. So the R6 t3-vertices of X40, τ (if τ = X50) and c1 lie in Q0: t3[k] with k ≤ 9 − x.
- Of R6's other t3-labels, v and X30 cannot lie in Q0, Z1 sits on the cut t3[10−x], and c8 may lie in Q0.
- **In case (X50, α) only:** P2 = 32, so t2[1] is the only t2-vertex inside R3 other than X30's cut vertex t2[2]. Hence w = L(t2[1]), and the pairs {v, w} (b6–t2[1]) and {w, X30} (t2[1]t2[2]) are used. Since t3[11] is adjacent to b3 (w), t3[11] carries neither v nor X30.

## 3. Case (X50, α): P2 = 32

Here ℓ2 = 19, λ = 11, P5 = 74, and X70 = t3[4] is at the cut 70.
- P− puts Λ[j] at 43 − j and P+ at 74 + j. So X40 = Λ[3], and the Λ (R3, R7) vertices of Z1 and X50 are Λ[4] and Λ[5] in some order. So **{Z1, X50} is used at Λ[4]Λ[5]**.
- R6's t3-interior, t3[5..11], carries {v, c1, c8, X30, X40, X50, Z1}.
- t3[5..9−x] must contain X40, X50 and c1. So x = 2, and the last R6 t3-labels {v, X30, c8} occupy t3[9..11] with t3[11] = c8; or x = 1, and t3[10..11] = {v, X30}. x = 1 contradicts the t3[11] fact.
- With x = 2: t3[5..7] = {X40, X50, c1} and t3[8] = Z1.
  - X40 and X50 cannot be adjacent there, because the pair {X40, X50} is used at t1[6]t1[7]. So t3[6] = c1.
  - t3[7] ≠ X50, since {X50, Z1} is used. So t3[7] = X40, and {X40, Z1} is used at t3[7]t3[8].
  - That forces Λ[4] ≠ Z1, so Λ[4] = X50. Then Λ[3]Λ[4] repeats the pair {X40, X50}. **Contradiction.**

## 4. Case (X70, α): P2 = 33

Here ℓ2 = 20, λ = 10 and P5 = 75. X70 = t3[5] sits at the cut 70, which lies in Q0 for x ≤ 4.
- X40 = Λ[3]. Z1's Λ (R3, R7) is Λ[4], since Λ[5] is c8 at 80. So the pairs {X40, Z1} and {Z1, c8} are used.
- R6's t3-interior, t3[6..11], carries {v, c1, c8, X30, X40, Z1}. Since t3[6..9−x] ⊇ {X40, c1}, we have x ∈ {1, 2}.

**x = 2.** t3[6..7] = {X40, c1} and t3[8] = Z1. t3[7] ≠ X40, since {X40, Z1} is used, so t3[6] = X40. Then t3[5]t3[6] repeats the pair {X70, X40} of t1[6]t1[7]. **Contradiction.**

**x = 1.** t3[6..8] = {X40, c1, c8} and t3[9] = Z1.
- t3[8] carries neither X40 (pair {X40, Z1}) nor c8 (pair {c8, Z1}), so t3[8] = c1.
- t3[6] carries neither X40 (pair {X70, X40}), so t3[6] = c8 and t3[7] = X40.
- If t1[6] carried X40, then t1[5]t1[6] = {c1, X40} would repeat t3[7]t3[8]. So t1[6] = X70 and t1[7] = X40.
- t1[1] = Z0 (x = 1), so b6–t1[1] uses {v, Z0}. Hence Λ[1] ≠ Z0, so Λ[1] = c1 and Λ[2] = Z0; these are c1's and Z0's Λ (R4, R7) vertices.
- X40 is now adjacent to Z0 (Λ[2]), Z1 (Λ[4]), X70 (t1[6]), w (b3), c8 (t3[6]) and c1 (t3[8]).
- X40's t2 (R2, R5) vertex lies in the chain t2[8..12], which carries exactly {c1, Z0, X40, X70, w} (the five (R2, R5) labels). Wherever X40 sits in this chain, it has a neighbour in {c1, Z0, X70, w}. That repeats a pair already used. **Contradiction.**

## 5. Result

**WRITTEN:** shape (b2) of v209 with u = 5 is impossible. With v211, shape (b2) needs u = 4. By the mirror (v160 §1), the same holds for type 2.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2: shape (b1), and shape (b2) with u = 4;
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
