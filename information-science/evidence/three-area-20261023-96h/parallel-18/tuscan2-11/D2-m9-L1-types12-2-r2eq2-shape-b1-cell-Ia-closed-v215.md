# Original Tuscan-2(11), entire m = 9 distance-two branch: shape (b1), cell I-a of v214 is impossible

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It is written only from the author's own unquarantined material (Main v215).

The number v215 is in the owner's own packet series; it is not the parent's direction v215.

It continues `D2-m9-L1-types12-2-r2eq2-shape-b1-classes-x-lt-u-closed-reduction-v214.md` (SHA256 `d26ec66861ed278dc68f20ee8862d2a68e63df44dbbb1e3d0476408256beadbd`) and uses its §2 anatomy table and (PC) (v185 §2).

It uses (R1)–(R2) only. It is written reasoning only: no interpreter, enumeration, program or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Cell I-a

**Parameters:**
- u = 5, so S = {c1, c8, X40, X20, X30} and T_int = {Z1, X50, X70, Z0};
- x ∈ {7, 8} (x > u);
- P1 = 16, P2 = 38 + c, P3 = 46, ℓ1 = 11, ℓ2 = 22 + c, λ = 8 − c, P5 = 77 + c, with c ∈ {0, 1}.

**Positions:**
- The t2-vertex t2[j] has S_12 at 38 + c − j and S_23 at 46 + j.
- v's t2-vertex is t2[60 − P3] = t2[14]. Its neighbours are:
  - t2[13], an (R2, R5)-vertex, carrying a label from {X40, w, X70, Z1, c1};
  - t2[15], an (R2, R6)-vertex, carrying a label from {c8, X50, Z0, c1}.
- v's t1-vertex lies above x (v204/v214 F2 argument), so its t1-neighbours lie in t1[x..11]. Those carry Z0 = t1[x], c8 and X50, or b3 (w).

## 2. The neighbours of b6

b6 is v's branch vertex, and its neighbours are the following.

| neighbour | label |
|---|---|
| t1[1] | an S-label (arm) |
| t3[1] | in Q0 by v214 §5. The S-labels X20 and X30 have their t1-arm vertex in Q0, so their t3 (R7) vertex lies in Q1 at index ≥ 11 − x ≥ 2. Hence t3[1] is neither X20 nor X30. |
| t2[1] | an (R3, R4)-label from {w, X70, Z1} |
| Λ[1] | non-arm: Z0, or c1 when c = 0 |
| Λ[λ−1] | the arm vertex next to b6. When c = 0 it is the unique R3-arm vertex Λ[7], carrying c1 (shape R3). When c = 1 it is Λ[6], carrying X40. |
| T_1 | a T_int label |

## 3. v cannot meet both X20 and X30

X20's vertices are: its t1-arm vertex, its Λ-arm vertex in R4, t2[18+c], t2 (R3, R5) ∈ t2[5..7+c], and t3 in R7.

X30's vertices are: its t1-arm vertex, its Λ-arm vertex in R4, t2[8+c], t2 (R1, R6) ∈ t2[19+c..21+c], and t3 in R7.

Neither label is T_int, and neither appears among the possible labels of t3[1], t2[1], Λ[1], Λ[λ−1], T_1, t2[13], t2[15] or v's t1-neighbours (§§1-2). So each of X20 and X30 can be adjacent to v only through b6–t1[1].

By (PC), v is adjacent to each other label exactly once, so both X20 and X30 would have to be t1[1]. **Contradiction.** So cell I-a is impossible.

## 4. Result

**WRITTEN:** shape (b1), cell I-a (u = 5) is impossible. What remains of shape (b1) is cell I-b (u = 4, X30 ∈ T_int, x ∈ {7, 8}, c ∈ {0, 1}). By the mirror (v160 §1), the same holds for type 2.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2: shape (b1), cell I-b;
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
