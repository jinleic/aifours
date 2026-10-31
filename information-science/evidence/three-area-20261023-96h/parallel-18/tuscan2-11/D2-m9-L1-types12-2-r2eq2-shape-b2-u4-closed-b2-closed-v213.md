# Original Tuscan-2(11), entire m = 9 distance-two branch: shape (b2) of v209 with u = 4 is impossible, so shape (b2) is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It is written only from the author's own unquarantined material (Main v215).

It continues `D2-m9-L1-types12-2-r2eq2-shape-b2-u5-closed-v212.md` (SHA256 `8f21ff284efbd597beece037053d1148c5e1c90f93c38bbe5b372990d59589b2`). It uses the conventions and imports of v211/v212, together with (PC) (v185 §2): H has exactly one edge for each of the 55 label pairs, so each label is adjacent to every other label exactly once.

It uses (R1)–(R2) only. It is written reasoning only: no interpreter, enumeration, program or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Labels

With u = 4, |T_int| = 5 ⊇ {X30, X40, Z1}.
- The arguments of v212 §1 do not depend on u. They give x < u, Z0 ∈ S and X60 ∉ T_int.
- Hence T_int = {X30, X40, Z1, X50, X70} and S = {c1, c8, X60, Z0}.
- X50 and X70 have the T_int anatomy of v212 §1, and the other labels have that of v211 §2.

## 2. Positions

R1 must receive X40, X50 and X70 through t1-vertices; each has its only R1-vertex on t1. It must receive X60, Z0, c8, X30 and Z1 through the t2-part.

So P1 = 14, ℓ1 = 8, P3 = 43, t1[4] = c1, and t1[5..7] carry {X40, X50, X70}.

The R6-side of the t2-part, positions 15..k60−1:
- In (β) it holds Z0 and Z1. That gives k60 = 17, but P2 + P3 ≤ 76, so (β) is impossible.
- In (α) it holds Z0 alone. That gives k60 = 16, P2 + P3 = 76 and **P2 = 33**.

So ℓ2 = 19, λ = 10, P4 = 62, P5 = 74 and ℓ3 = 12. Then:
- **t3.** F1 puts t3[k] at 74 − k. t3[4] = X70 sits at the cut 70. R6's t3-interior is t3[5..11], and R7's t3-vertices are t3[1..3].
- **t2.** t2[j] has S_12 at 33 − j and S_23 at 43 + j. The cuts are t2[3] = X30, t2[7] = X50 (S_23 at 50), t2[13] = v (S_12 at 20) and t2[17] = X60 (S_23 at 60). The (R2, R4)-vertices are t2[4..6], and the (R2, R5)-vertices are t2[8..12].
- **Λ.** P− puts Λ[j] at 43 − j and P+ at 74 + j. The arm is Λ[6..9], and X40 = Λ[3] is at the cut 40.

## 3. X40 and X60 are never adjacent

**X40's vertices and their neighbours:**
- its T-vertex: neighbours are T-vertices (carrying T_int labels), b6 (v) or ℓ (w);
- Λ[3]: neighbours Λ[2] and Λ[4], both non-arm;
- its t2 (R2, R5) vertex in t2[8..12]: neighbours in t2[7..13];
- its t1-vertex in t1[5..7]: neighbours in t1[4..7] or b3;
- its t3 (R6) vertex in t3[5..11]: neighbours in t3[4..11] or b3.

**X60's vertices:**
- its t1-arm vertex in t1[1..3];
- its Λ-arm vertex in Λ[6..9];
- t2[17], and its t2 (R2, R4) vertex in t2[4..6];
- its t3 (R7) vertex in t3[1..3].

X60 is not in T_int, and none of its vertices is a neighbour of any X40-vertex. The relevant index ranges are disjoint or non-adjacent: t1[1..3] against t1[4..7] (t1[4] is c1); Λ[6..9] against Λ[2..4]; t2[4..6] and t2[17] against t2[7..13]; t3[1..3] against t3[4..11] (t3[4] is X70).

So the pair {X40, X60} labels no edge of H. This contradicts (PC). **Shape (b2) with u = 4 is impossible.**

## 4. Result

**WRITTEN:** shape (b2) of v209 is impossible for u = 4 (here), u = 5 (v212) and u = 6 (v211), and u ≤ 6 by v210. **Shape (b2) is closed.** By the mirror (v160 §1), the same holds for type 2.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2, shape (b1) only;
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
