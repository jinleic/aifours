# Original Tuscan-2(11), entire m = 9 distance-two branch, part 43: L1 type 9 with r2 = 2 is impossible, and by the mirror so is type 3 with r2 = 2

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type10-r2eq2-closed-types4-10-closed-v155.md` (SHA256 `660996ba8be146a445353c9bbb865b1fc880793ccc94bc94f9c8f2d704a1a72f`), uses the notation of v117 and v152, and uses the mirror principle of v155 §5.

The tools are Lemmas DP-1 and DP-2 of v114 §2 (double pass of one thread inside one face), applied here to t1 inside F1, together with (C) and (E). It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type 9: faces and positions

**Rotation and faces.**
- The b6 rotation is (T, t1, Λ+, t2, t3, Λ−), so h1 = t1 and h5 = Λ−.
- F1 = S_T S_12 S_31 P+ and F2 = S_23 P−.
- G1 = {T, t1} and G2 = {t2, t3, Λ} (v152).
- F1 has 2t + 2ℓ1 + ℓ2 + ℓ3 + λ = 10r1 positions, and F2 has ℓ2 + ℓ3 + λ = 10r2.

**F1 positions.** Put B1 = t + ℓ1, C1 = B1 + ℓ2, B2 = C1 + ℓ3 and C2 = B2 + ℓ1.

| Position(s) | Vertex |
|---|---|
| 0 | ℓ |
| 1..t−1 | T_int |
| t | b6 |
| t + j | t1[j] (S_12) |
| B1 | b3 |
| C1 − j | t2[j] |
| C1 | b6 |
| C1 + j | t3[j] |
| B2 | b3 |
| C2 − j | t1[j] (S_31) |
| C2 | b6 |
| C2 + k | Λ[k] (P+) |
| C2 + λ = 10r1 − t | b6 |
| 10r1 − t + 1 .. 10r1 − 1 | T_int |
| 10r1 | ℓ |

**The case r2 = 2.**
- Here r1 = 9, ℓ2 + ℓ3 + λ = 20 and t + ℓ1 = 35.
- So ℓ1 = u + 25, B1 = 35, B2 = 55 − λ and C2 = 80 + u − λ.
- R1 = [10, 20] = t1[u..u+10] and R2 = [20, 30] = t1[u+10..u+20] are forward t1-rows.
- The interior of t1 is t1[1..u+24].

**Double-pass data (v114 §2).**
- Forward cuts of t1 sit at indices j ≡ u.
- Backward cuts sit at j ≡ C2 ≡ u − λ.
- So **ρ ≡ −λ (mod 10)**.

## 2. Exclusion of every ρ

**ρ = 0.** Then t1[u]'s S_31-passage C2 − u ≡ 0 would be a second cut of c1. Impossible.

**ρ ∈ {1, 2, 3}.** DP-1 with s = u and the window [u, u + ρ + 10] ⊆ [1, u + 24].

**ρ ∈ {7, 8, 9}.** DP-1 with s = u + 10 and the window [u + ρ, u + 20] ⊆ [1, u + 24].

**ρ = 5 (λ ∈ {5, 15}).** b3 sits at B2 = 55 − λ ∈ {50, 40}, which is a cut. But w's only cut is ℓ. Impossible.

**ρ = 4 (λ ≡ 6).** DP-2 on B-blocks (v114: window [s, s + ρ + 20] = [u, u + 24] ⊆ [1, u + 24]):
- P1 = t1[u..u+3] and P1′ = t1[u+11..u+14], from R1 and the backward row t1[u+4..u+14];
- P2 = t1[u+10..u+13];
- P2′ = t1[u+21..u+24], from R2 and the backward row t1[u+14..u+24].

This gives m = 4, a contradiction.

**ρ = 6 (λ ≡ 4, so λ ∈ {4, 14}).**
- R2 and the backward row t1[u+6..u+16] give L(t1[u+6..u+9]) = L(t1[u+17..u+20]).
- R1 and the backward row starting at the backward cut t1[u+6] give a 4-vertex path Q with L(Q) = L(t1[u+7..u+10]):
  - **u ≥ 5:** that row is t1[u−4..u+6], and Q = t1[u−4..u−1].
  - **u ≤ 4:** the row runs past index 0. It is t1[u+6..1], b6, Λ[1..4−u], occupying positions 74 − λ to 84 − λ, which is R7 for λ = 4 and R6 for λ = 14. Then Q = (t1[u−1..1], b6, Λ[1..4−u]).
  - In both cases Q shares no vertex with t1[u+6..u+20].
- Apply DP-2 with m = 4:
  - P1 = t1[u+17..u+20];
  - P1′ = (t1[u+9], t1[u+8], t1[u+7], t1[u+6]);
  - P2 = (t1[u+10], t1[u+9], t1[u+8], t1[u+7]);
  - P2′ = Q.

This is a contradiction.

**So type 9 with r2 = 2 is impossible.**

## 3. Type 3 by the mirror

**Type 9 mirrors to type 3.**
- Start from type 9: b6 rotation (T, t1, Λ+, t2, t3, Λ−) and b3 rotation (t1, t2, t3).
- Row reversal gives (T, Λ−, t3, t2, Λ+, t1) and b3 rotation (t3, t2, t1).
- Rename Λ+ ↔ Λ− and t1 ↔ t3. Then b3 becomes (t1, t2, t3), and b6 becomes (T, Λ+, t1, t2, Λ−, t3), which is type 3.

Reversal keeps r1 and r2 (v155 §5). So **type 3 with r2 = 2 is impossible.**

## 4. Result

**WRITTEN:**
- L1 type 9 with r2 = 2 is impossible.
- L1 type 3 with r2 = 2 is impossible (mirror).

**OPEN:**
- L1 types 3 and 9 with r2 ∈ {3, 4};
- types 1, 2, 7, 8, 11 and 12 (v152 restrictions).

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
