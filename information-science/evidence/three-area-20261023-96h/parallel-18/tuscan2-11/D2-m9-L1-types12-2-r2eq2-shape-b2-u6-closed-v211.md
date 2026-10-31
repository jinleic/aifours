# Original Tuscan-2(11), entire m = 9 distance-two branch: shape (b2) of v209 with u = 6 is impossible

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It is written only from the author's own unquarantined material (Main v215).

It continues `D2-m9-L1-types12-2-r2eq2-shape-b2-u-le-6-v210.md` (SHA256 `cc129dcbeecbab6b7e27dffe0ddf7d6e198d33c751f52b02d07184ce9c7f7a88`).

**Imports:**
- the F1 data of v160 §2 and v165 §2;
- the shared w-shape and the (b2) data of v209 §5;
- v204 §2 (Z0, Z1, the case x < u);
- the anatomy counts of v152: a G1-vertex lies twice in F1, a G2-vertex once in each face, and G3 is empty for type 12.

It uses (R1)–(R2) only. It is written reasoning only: no interpreter, enumeration, program or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Labels when u = 6

By v210, T_int ⊇ {X30, X40, Z1} and |T_int| = 9 − u = 3. So T_int = {X30, X40, Z1}. The eleven labels are the cut labels:
- F1 cuts: c1 (10), v = X20, X30, …, X70, c8 (80), w (ℓ);
- F2 cuts: Z0, Z1.

So S = {c1, c8, X50, X60, X70, Z0}. Since Z0 ∈ S, x < u (v204 §2 (iii)).

## 2. Forced anatomy

Each label meets each F1 row exactly once. F1-cut S- and T_int-labels have three G1-vertices and two G2-vertices; Z0 and Z1 have four G1-vertices and one G2-vertex. t2 and Λ carry G1-vertices; t1, t3 and their arms carry G2-vertices.

A t2-vertex has S_12 + S_23 = P2 + P3, so:
- S_12 ∈ R1 forces S_23 ∈ R5 ∪ R6;
- S_12 ∈ R2 forces S_23 ∈ R4 ∪ R5.

A non-arm Λ-vertex with P+ in R7 has P− in R3 or R4.

Listing the rows each label must still cover, every choice below is forced. Write "t2 (Ri, Rj)" for a t2-vertex with S_12 in Ri and S_23 in Rj.

| label | vertices |
|---|---|
| X60 | t1-arm, Λ-arm, t2[60−P3] (cut 60; S_12 in R1), t2 (R2, R4), t3 in R7 |
| X50 | t1-arm, Λ-arm, t2[50−P3] (cut 50; S_12 in R2), t2 (R1, R6), t3 in R7 |
| X70 | t1-arm, Λ-arm, t3 at the cut 70, t2 (R1, R5), t2 (R2, R4) |
| Z0 | t1[x], Λ-arm, Λ (R4, R7), t2 (R1, R6), t2 (R2, R5) |
| c8 | t1-arm, Λ[λ−u] (cut 80; P− in R3), t3 in R6, t2 (R1, R5), t2 (R2, R4) |
| c1 | t1[u] (cut 10), Λ-arm, t3 in R6, t2 (R2, R5), Λ (R4, R7) |
| X30 | T, t2[P2−30] (cut 30; S_23 in R4), t2 (R1, R5), t3 in R6, t3 in R7 |
| X40 | T, the Λ-vertex at 40 (cut; P+ in R7), t2 (R2, R5), a t1-vertex in R1, t3 in R6 |
| Z1 (α) | T, t3[10−x] in R6, Λ (R3, R7), t2 (R1, R5), t2 (R2, R4) |
| Z1 (β) | T, t3[10−x] in R7, t2 (R3, R4), t2 (R2, R5), t2 (R1, R6) |

v = {b6, t2[P2−20] (cut 20; S_23 in R5), t3 in R6}, and w is as in v209.

Two of these choices need a short reason:
- **X40.** The pure t2-row R2 forces t2 (R2, R5). The two G2-vertices must then cover R1 and R6, and the only G2-vertices in R1 are non-arm t1-vertices.
- **Z1.** Z1's single G2-vertex t3[10−x] lies in R6 (α) or in R7 (β).
  - In (α), R7 needs Λ (R3, R7), and then (R1, R4) is not a t2-pair.
  - In (β), R3 needs t2 (R3, R4), since a t2-vertex with S_12 in R3 has S_23 ≤ 49, and the remaining pairs are forced.

## 3. The positions are forced

**R1 = c1, t1[7..ℓ1−1], b3 (w), t2-part, v.** From the table, eight labels must enter R1:
- X50, Z0 and, in (β), Z1 (S_23 ∈ R6), X60 (at the cut vertex), and X70, c8, X30 and, in (α), Z1 (S_23 ∈ R5) do so through the t2-part;
- X40 does so through a t1-vertex.

So R1's t1-part, positions 11..P1−1, is exactly {X40}. Hence P1 = 12, ℓ1 = 8 and t1[7] carries X40.

**P2 and P3.**
- P3 = 25 + u + P1 = 43.
- The S_12 position of the cut vertex t2[60−P3] is k60 = P2 + P3 − 60.
- The R1 positions 13..k60−1 have S_23 in R6. They hold exactly X50 and Z0 in (α), and X50, Z0 and Z1 in (β).

**(β) is impossible.**
- Here k60 = 16, so P2 + P3 = 76 and P2 = 33, with ℓ2 = 21, λ = 10 and P5 = 76.
- F1 puts t3[k] at P5 − k = 76 − k. The cut 70 is X70 = t3[6], and Z1's vertex t3[10−x] at 66 + x lies in R7. So x ≥ 5, hence x = 5, since x < u.
- X40's t3-vertex lies in R6, at t3[k] with 7 ≤ k ≤ 11. In F2 it sits at position k > 10 − x = 5, so in Q1.
- X40's other G2-vertex, t1[7], sits at F2 position 13, also in Q1. So X40 appears twice in Q1 and not at all in Q0. **Contradiction.**

**(α).** Here k60 = 15, so P2 + P3 = 75, P2 = 32, ℓ2 = 20, ℓ3 = 12, λ = 11, P4 = 63 and P5 = 75. Z1's vertex t3[10−x] sits at 65 + x in R6 and not on the cut 70, so x ≤ 4.

**Λ.**
- P− puts Λ[j] at 43 − j and P+ puts it at 75 + j.
- Λ[3] is at 40, so X40 = L(Λ[3]).
- Z1's Λ (R3, R7) needs 3 ≤ j ≤ 5. j = 3 is X40 and j = 5 is c8 at 80, so **Z1 = L(Λ[4])**.

## 4. F2 forces the t3-labels

F2 puts t3[j] at j, b3 at 12, t1[j] at 20 − j and b6 at 0. Its rows are Q0 = [−x, 10−x] and Q1 = [10−x, 20−x], with cuts t1[x] (Z0) and t3[10−x] (Z1); x ≤ 4.

R6 holds t3[11..6] at positions 64..69 and t3[5] = X70 at the cut 70. R7 holds t3[4..1] at 71..74.

| label | its other G2-vertex | so its t3-vertex lies in |
|---|---|---|
| X40 | t1[7] at F2 position 13, in Q1 | Q0: t3[k] with 6 ≤ k ≤ 9 − x |
| c1 | t1[6] at 14, in Q1 | Q0: t3[k] with 6 ≤ k ≤ 9 − x |
| v | b6 in Q0 | Q1 |
| X30 | its R7 t3-vertex (k ≤ 4) in Q0 | Q1, for the R6 t3-vertex |

So t3[6..9−x] (4 − x vertices) contains X40 and c1, which needs x ≤ 2. R6's t3-labels are {v, c1, c8, X30, X40, Z1}:
- v and X30 cannot lie in Q0 (table);
- Z1 sits on the cut t3[10−x];
- c8 may lie in Q0, when its t1-arm vertex is in Q1.

So **x = 2 with t3[6..7] = {X40, c1}**, or **x = 1 with t3[6..8] = {X40, c1, c8}**. In both cases Z1 = L(t3[10−x]).

**Two facts used below.** w's t2[jw′] (R3, R4) has S_12 in R3 = [30, 40]. The only t2-vertices there are t2[2] (X30, at 30) and t2[1] (at 31), so w = L(t2[1]). Its edges give the pairs {v, w} (with b6) and {w, X30} (with t2[2]).

## 5. A repeated pair

**x = 2.** t3[6], t3[7] carry {X40, c1}, and t3[7] is adjacent to t3[8] = Z1.
- If t3[7] carries X40, the pair {X40, Z1} appears at t3[7]t3[8] and also at Λ[3]Λ[4].
- If t3[7] carries c1, then t3[6] carries X40, and the pair {X40, c1} appears at t3[6]t3[7] and also at t1[6]t1[7], since t1[6] carries c1 = L(t1[u]) and t1[7] carries X40.

**x = 1.** t3[10..11] carry the remaining R6 t3-labels {v, X30}, and t3[11] is adjacent to b3 (w). Then:
- the pair {v, w} also lies on b6–t2[1];
- the pair {X30, w} also lies on t2[1]t2[2].

In every case one unordered pair labels two physical edges of H, which is impossible because H has one edge per pair. **So shape (b2) with u = 6 is impossible.**

## 6. Result

**WRITTEN:** shape (b2) of v209 needs u ∈ {4, 5}. By the mirror (v160 §1), the same holds for type 2.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2: shape (b1), and shape (b2) with u ∈ {4, 5};
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
