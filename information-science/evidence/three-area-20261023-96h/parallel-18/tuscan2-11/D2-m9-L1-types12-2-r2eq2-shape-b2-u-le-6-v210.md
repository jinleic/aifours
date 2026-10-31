# Original Tuscan-2(11), entire m = 9 distance-two branch: in shape (b2) of v209, |T_int| ≥ 3, so u ≤ 6

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. Per Main v215, it is written only from the author's own unquarantined material.

It continues `D2-m9-L1-types12-2-r2eq2-cprime0-b3-in-Q1-l2-ge-16-P2-31-40-reduced-to-two-shapes-v209.md` (SHA256 `395812bb73bf3b0409c63837b617ff1633abc0a4bfd454e996c1afff72af9685`).

**Imports:**
- the type-12, r2 = 2 F1 data of v160 §2 and v165 §2;
- the R8 anatomy: R8 = c8, the Λ-arm, b6, T_int, ℓ (v204, SHA256 `79a93d0974841c512910d7a2418011e498fb7989145a143bac39d8e1d5af40ce`);
- v204 §2 (ii)/(iii) for the F2-cut label Z1 = L(t3[10−x]).

It uses (R1)–(R2) only. It is written reasoning only: no interpreter, enumeration, program or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Data of (b2)

- v = X20, P2 ∈ R3 and P3 ∈ R4, with P2 + P3 ∈ {74, 75, 76}, 32 ≤ P2 ≤ 39 and u + P2 ∈ [36, 44] (v209 §5).
- Since P3 = 25 + u + P1 (from P1 = 10 − u + ℓ1 and P3 = 35 + ℓ1) and P1 ≥ 11, we get u + P2 ≤ 40.
- u + P2 = 40 would put the arm vertex Λ[λ−u] on the cut 40. Its label c8 already has its cut at 80, so this is impossible. Hence **s′ := u + P2 ∈ [36, 39]**.
- P− runs Λ[λ−j] at P2 + j. So R3 = [30, 40] reads:
  - X30 = t2[P2−30], then t2[P2−31..1];
  - b6 at P2;
  - the Λ-arm Λ[λ−1..λ−u] at P2+1..s′;
  - 40 − s′ ≥ 1 non-arm Λ-vertices at s′+1..40, the last carrying X40.

## 2. Three distinct T_int-labels

**X30 and X40.** R3 and R8 share exactly b6 and the arm Λ[λ−u..λ−1]. Cancelling them gives

  L(t2[1..P2−30]) ∪ L(Λ at positions s′+1..40) = T_int ∪ {w},

with both sides of size 10 − u. X30 and X40 lie on the left. Neither is w, because w's cut is ℓ. So **X30, X40 ∈ T_int**.

**Z1.** Z1 ∈ T_int:
- if x > u, this is v204 §2 (ii);
- if x < u, v204 §2 (iii) gives Z1 ∈ {w} ∪ T_int ∪ L(t1[x+1..u]). Here Z1 ≠ w, and Z1 ∉ S, because an S-label has its t1-arm vertex as a second G2-vertex while Z1 has b = 1.

The labels X30, X40 and Z1 have distinct cuts (30, 40 and an F2 cut), so they are distinct. Hence |T_int| = 9 − u ≥ 3, and **u ≤ 6**.

## 3. Result

**WRITTEN:** shape (b2) of v209 needs u ∈ {4, 5, 6}. Together with A4 this excludes u = 7, which the (b2) data otherwise allow (s′ = 39, P2 = 32). By the mirror (v160 §1), the same holds for type 2.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2: shape (b1), and shape (b2) with u ∈ {4, 5, 6};
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
