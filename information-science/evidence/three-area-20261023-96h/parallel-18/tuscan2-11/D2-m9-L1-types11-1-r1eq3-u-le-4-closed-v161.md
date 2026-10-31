# Original Tuscan-2(11), entire m = 9 distance-two branch, part 48: L1 types 11 and 1 with r1 = 3 are impossible for u ≤ 4, and reduced to one residue window for u ≥ 5

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-consolidated-status-L1-progress-two-row-lemma-exact-gap-v160.md` (SHA256 `3597c7633dcbf620c46f532ef3f7ba38e42627f029a738c4119bb3b96e888cff`). It uses:
- v117 and v152;
- Lemmas DP-1 and DP-2 of v114 §2;
- the overlap exchange;
- the mirror principle of v155 §5.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type 11 with r1 = 3: data

**Rotation and faces.**
- The b6 rotation is (T, t1, t2, Λ+, t3, Λ−). So h1 = t1, h5 = Λ−.
- F1 = S_T S_12 P+ and F2 = S_23 P− S_31.
- G1 = {T}, G2 = {t1, t2, Λ} and G3 = {t3} (v152).

**Lengths.**
- r1 = 3 + n1 + n2 + nΛ + c = 3, so n1 = n2 = nΛ = c = 0.
- F1 has 2t + ℓ1 + ℓ2 + λ = 30 positions, so ℓ1 + ℓ2 + λ = 10 + 2u.
- F2 has ℓ1 + ℓ2 + λ + 2ℓ3 = 80 positions, so **ℓ3 = 35 − u**. The interior of t3 is t3[1..34−u].

**F2 in order.**
- b6 (corner t1→t2), then t2[1..ℓ2−1], then b3.
- Then t3[ℓ3−1..1] (the S_23-pass, backward), then b6 = Z3.
- Then Λ[λ−1..1] (P−), then b6 = Z2 = Z3 + λ.
- Then t3[1..ℓ3−1] (the S_31-pass, forward), then b3, then t1[ℓ1−1..1], and back to the first b6.

So t3[j] lies at Z2 + j (forward) and at Z3 − j (backward). Both passes lie in F2, in opposite directions. The double-pass shift is ρ ≡ Z2 + Z3 (mod 10). Forward cuts sit at indices j ≡ φ, and s1 ∈ [1, 10] denotes the least positive such index.

**Beyond the ends of t3.**
- Beyond index 0, the backward pass continues into b6 = Z3 and then Λ[λ−1], Λ[λ−2], ….
- Beyond index ℓ3, the backward pass continues into b3 and then t2[ℓ2−1], ….

## 2. DP-1

**ρ = 0** is impossible.

**ρ ∈ {1, 2, 3}** is excluded by DP-1 with interior windows [s, s + ρ + 10], s ≡ φ. The admissible s form [1, 24 − u − ρ], of length ≥ 12 for u ≤ 9.

**ρ ∈ {7, 8, 9}** is excluded by DP-1 with interior windows [s + ρ − 10, s + 10]. The admissible s form [11 − ρ, 24 − u].

**So ρ ∈ {4, 5, 6}.**

## 3. DP-2 chains for s ∈ [1, 14 − u], s ≡ φ

In all three chains, the forward rows [s, s+10] and [s+10, s+20] are interior (s + 20 ≤ 34 − u).

**ρ = 4.**
- The equalities L([s, s+3]) = L([s+11, s+14]) and L([s+10, s+13]) = L(P2′) come from the backward rows [s+4, s+14] and [s+14, s+24].
- The second backward row may run beyond index ℓ3 into b3, t2, ….
- Its common part with [s+10, s+20] is the interior segment [s+14, s+20]. So P2′, the part of that backward row at indices s+21..s+24, is a 4-vertex path.
- DP-2 with m = 4:
  - P1 = [s, s+3];
  - P1′ = [s+11, s+14];
  - P2 = [s+10, s+13];
  - P2′ as above.

**ρ = 5.** The same chain with blocks of size 5:
- P1 = [s, s+4];
- P1′ = [s+11, s+15];
- P2 = [s+10, s+14];
- P2′ = the backward row [s+15, s+25] at indices s+21..s+25.

This is DP-2 with m = 5.

**ρ = 6.**
- The forward row [s+10, s+20] with the interior backward row [s+6, s+16] gives L(t3[s+6..s+9]) = L(t3[s+17..s+20]).
- The forward row [s, s+10] with the backward row [s−4, s+6] gives L(t3[s+7..s+10]) = L(Q). Here:
  - Q = t3[s−4..s−1] when s ≥ 5;
  - otherwise Q = (t3[s−1..1], b6, Λ[λ−1..λ−4+s]), a 4-vertex path through Z3.
  - If λ is too short for this row, the row would contain b6 twice (at Z3 and Z2), which is impossible for a row.
- DP-2 with m = 4:
  - P1 = t3[s+17..s+20];
  - P1′ = (t3[s+9], t3[s+8], t3[s+7], t3[s+6]);
  - P2 = (t3[s+10], …, t3[s+7]);
  - P2′ = Q.

**DP-2 hypotheses.** In each chain:
- P1 and P1′ are disjoint;
- P2 = (y, q1, …) with y adjacent to q1 on t3;
- the edges of P2′ lie at other indices or outside t3, so they differ from those of P1, P1′ and P2.

**Each chain is a contradiction.**

## 4. Result

**Type 11 with r1 = 3:**
- When u ≤ 4, every residue φ has an s ≡ φ in [1, 14 − u] ⊇ [1, 10]. So **type 11 with r1 = 3 and u ≤ 4 is impossible**.
- When u ≥ 5, the survivors must have ρ ∈ {4, 5, 6} and s1 ∈ [15 − u, 10].

**Type 1 (mirror).** Row reversal maps type 1 to type 11:
- type 1's rotation (T, Λ+, t1, Λ−, t2, t3) reverses to (T, t3, t2, Λ−, t1, Λ+);
- renaming Λ+ ↔ Λ− and t1 ↔ t3 gives (T, t1, t2, Λ+, t3, Λ−);
- b3 stays (t1, t2, t3) cyclically.

Reversal keeps r1 and u. So the same holds for type 1 with r1 = 3.

**WRITTEN:**
- L1 types 1 and 11 with r1 = 3 and u ≤ 4 are impossible.
- For u ≥ 5 they are reduced to ρ ∈ {4, 5, 6} with the first forward t3-cut index in [15 − u, 10].

**OPEN (m = 9, L1):**
- types 1 and 11: r1 = 3 with u ≥ 5 (residue window above), and r1 ∈ {4, 5, 6};
- type 8;
- types 2 and 12;
- type 7 with r2 ∈ {3, 4};
- types 3 and 9 with r2 = 3 (λ = 14, u ≥ 4) and with r2 = 4.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
