# Original Tuscan-2(11), entire m = 9 distance-two branch, part 52: Lemma DP★ (two pure rows kill a double pass), and L1 types 12 and 2 with r2 = 2 need ℓ2 ≥ 5 (type 12) and ℓ1 ≥ 5 (type 2)

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type8-r1eq5-a-outside-11-19-closed-v164.md` (SHA256 `d7faebb6520629fbc880c0f165484f46c49b0424acda3eda0be2cd31576acdb3`). It packages as one lemma the argument already used in v156, v161, v162 and v164, and applies it once more.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Lemma DP★

**Hypotheses.**
- θ is a thread or the loop, with interior θ[1..L−1].
- Its two passes run in opposite directions, in faces F and F′ (possibly F′ = F).
- F contains two consecutive pure θ-rows θ[s..s+10] and θ[s+10..s+20], with 1 ≤ s and s + 20 ≤ L − 1.
- Every F′-row used below is a path of H that shares no vertex with these two F-rows. (This holds automatically if F′ ≠ F. If F′ = F, it must be checked in each use.)

The F′-rows used are the backward rows starting at a backward cut. Where they run past θ's ends, they continue along F′ through the end vertex.

**Conclusion.** The configuration is impossible.

**Proof.** Let ρ be the double-pass shift (v114 §2).
- **ρ = 0** puts two cut passages on one vertex.
- **ρ ∈ {1, 2, 3}:** DP-1 with θ[s..s+10] and the interior backward row θ[s+ρ..s+ρ+10].
- **ρ ∈ {7, 8, 9}:** DP-1 with θ[s+10..s+20] and the interior backward row θ[s+ρ..s+ρ+10].
- **ρ = 4 or 5:** DP-2 on B-blocks:
  - P1 = θ[s..s+ρ−1] and P1′ = θ[s+11..s+10+ρ], from the backward row θ[s+ρ..s+ρ+10];
  - P2 = θ[s+10..s+9+ρ];
  - P2′ = the backward row θ[s+10+ρ..s+20+ρ] at indices s+21..s+20+ρ. This row may run past index L along F′. Its common part with θ[s+10..s+20] is the interior segment θ[s+10+ρ..s+20], so P2′ is a path.
- **ρ = 6:** DP-2 on C-blocks:
  - P1 = θ[s+17..s+20];
  - P1′ = (θ[s+9], …, θ[s+6]), from the backward row θ[s+6..s+16];
  - P2 = (θ[s+10], …, θ[s+7]);
  - P2′ = the backward row θ[s−4..s+6] at indices s−4..s−1. This row may run below index 1 along F′. Its common part with θ[s..s+10] is θ[s..s+6].

In each DP-2 chain, P2′ lies at indices, or at F′-vertices, disjoint from P1, P1′ and P2, so its edges are new. ∎

## 2. Application: type 12 with r2 = 2 and ℓ2 ≤ 4

**Data (v160 §2 and the type-12 table).**
- F1 = S_T S_12 P− S_23 P+ has 90 positions.
- λ = 25 + u − ℓ2.
- P+ runs Λ[1..λ−1] at P5 + k, with P5 = 55 + ℓ2, so Λ[λ−u] is the cut at 80.
- P− runs Λ[k] at P3 − k, with P3 = 35 + ℓ1. Both passes of Λ lie in F1, in opposite directions.

**Two pure rows.** If ℓ2 ≤ 4, then P5 ≤ 59. So R6 = [60, 70] = Λ[5−ℓ2..15−ℓ2] and R7 = [70, 80] = Λ[15−ℓ2..25−ℓ2] are consecutive pure forward Λ-rows, with s = 5 − ℓ2 ≥ 1 and s + 20 = λ − u ≤ λ − 1.

**Disjointness.** Every backward row used lies within [P2 − 4, P3 + 3], and P2 − 4 ≥ 7:
- The interior rows lie inside P−.
- The B-chain row runs past the Λ−-end through b6 = P2 into the S_12 t2-run. Its lowest position is P3 − s − 24 = P2 + u − 4 (ρ = 4), or P2 + u − 5 (ρ = 5).
- The C-chain row runs past the Λ+-end through b6 = P3 into the S_23 t2-run, up to P3 + 4 − s ≤ P3 + 3.

Since ℓ1 ≤ u + 9 (v160 §2) and u ≤ 9, we have P3 = 35 + ℓ1 ≤ 53. So every backward row used lies before position 57 and meets neither R6 nor R7.

**Conclusion.** Lemma DP★ applies, so **type 12 with r2 = 2 and ℓ2 ≤ 4 is impossible**.

## 3. Type 2 by the mirror

Row reversal maps type 2 to type 12 and exchanges t1 with t2 (v160 §1). So **type 2 with r2 = 2 and ℓ1 ≤ 4 is impossible**.

## 4. Result

**WRITTEN:**
- Lemma DP★.
- Types 12 and 2 with r2 = 2 need ℓ2 ≥ 5 (type 12) and ℓ1 ≥ 5 (type 2).
- Together with v160 §2: in type 12, ℓ1 ≤ u + 9; in type 2, ℓ2 ≤ u + 9.

**OPEN (m = 9, L1):**
- types 2 and 12 (the r2 = 2 remainder, and r2 ∈ {3, 4});
- type 7 with r2 ∈ {3, 4};
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19];
- types 1 and 11 with r1 ∈ {4, 5, 6};
- types 3 and 9 with r2 = 3 (λ = 14, u ≥ 4) and with r2 = 4.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
