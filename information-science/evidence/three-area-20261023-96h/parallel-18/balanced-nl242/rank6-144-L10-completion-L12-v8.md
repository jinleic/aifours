# Balanced NL242 (3,144) — completion of the L = 10 case analysis: (10,0) with n_8 = 0 and (8,1) are excluded, so L ≥ 12

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:25:41 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** The residue type (polar rank 6, weight 144) only. The type, the (24,24,2) gap and the original problem remain OPEN.

## 0. Inputs and tools

The tools are those of `rank6-lifted-floors-consolidated-proof-v1.md` (6c5ce361):

- S0017 only, with Theorem A, Lemma B, Lemma O, Lemma Φ, Lemma SV, Theorem M and (★);
- the slice-pattern rule: per pure coset, all zero, a single ±12, or all three ±6;
- coset activity per slice;
- the census and second moment Σ_ā (G − N_0/8)² = 64N_0 − N_0².

At L = 10: wt(h_0) ≤ 38, so N_0 ≥ 26. Also |P| ≥ 7, dim aff(P) = 6, and s ≥ 4.

## 1. (10,0) with ΣΣ ≠ 0 and no 8-relation

R has 7 relations of sizes 4 and 6, and V′ = A_4 − 3A_6 = 15, since V′ ≡ 7 (mod 8) and V′ ≤ 19.

**Signs.** g restricted to R is a character, so the set of relations with g = −1 is empty or has exactly 4 elements. This forces n_4 = 3 and n_6 = 4, with all 2-flats positive and all 6-relations negative.

- (2,5) would need 6 negative relations.
- (1,6) gives V′ ≤ 7.

**Shape.** The three 2-flats are co-planar: blocks B_1, B_2, B_3, with F_1 = B_1 ∪ B_2 and so on. A 6-relation Z meets each block once and takes three further points t_1, t_2, t_3. Since Σwt = 36, exactly one point q lies in no relation.

**Contradiction.** The pure coset q + t_1 + t_2 has representation sizes 3, 7, 7, 7, 5, 5, 5, 5, so its bracket is

```
−3 − 27(f_1 + f_2 + f_1f_2) + 9ζ(1 + f_1)(1 + f_2).
```

The only value allowed in any slice is −6, at f_1 = f_2 = ζ = 1. That requires ζ = g_η(Z) = −(−1)^{λ_Z(η)} = +1, i.e. λ_Z(η) = 1, for all three η ≠ 0. That is impossible for a linear functional. **Excluded.**

## 2. (8,1)

Σ consists of 8 single-value cosets, and p is a balanced (1,1) coset, active in 2 slices and inactive in η_0.

**dim aff(Σ) = 6 with Σ zero-sum, G = +1 (C2-type).**

1. In η_0, all 55 pure triple cosets need G_{η_0} = −1, and they then take the value −6g. So in the p-active slices they must be ±6 as well.
2. There R(P) = {0, Σ, r_p, Σ Δ r_p} with r_p = T_p ∪ {p}, where T_p is a triple. The cosets with |T ∩ T_p| = 1 have bracket −3 + 9(G + ρ + Gρ), which forces G_η = ρ_η = 1 in both p-active slices.
3. Hence B = 0, so G_{η_0} = +1. Contradiction.

**dim aff(Σ) = 6 with a zero-sum 6-subset Σ_6 of sign −1 (C1-type).**

1. In η_0, the type-(a) cosets force G6 = −1. The type-(c) cosets x + q_1 + q_2 then take the value 12g, so they must vanish in both p-active slices.
2. Write r_p = T_p ∪ {p} with a = |T_p ∩ Σ_6| and b = |T_p ∩ {q_1, q_2}|. The admissible (a, b), up to r_p ↔ Σ_6 Δ r_p, are (3,0), (2,1), (1,2) and (3,2).
3. Vanishing requires −3 − 27G6 + ρ(w(s_1) + G6·w(s_2)) = 0. Here (s_1, s_2) = (2 + a − b, 10 − a − b) if x ∈ T_p and (4 + a − b, 8 − a − b) otherwise.
4. Every admissible (a, b), with both signs of G6, fails for some x. Hand table: (3,0) gives 36 or −18; (2,1) fails for x ∉ T_p with 0 or 18; (1,2) gives 28 or −26; (3,2) gives −12 or 6. None equals the required ±24, ±30 or 0 combination.

**dim aff(Σ) = 5,** so p lies in no relation and every coset p + x + y is active only in the two p-active slices.

- **Three co-planar 2-flats plus Γ = {g_1, g_2}.** The coset p + g_1 + g_2 has bracket −3 − 27S with S ∈ {3, −1}. That gives 21 or −6 in both p-active slices. Forbidden.
- **Two disjoint 2-flats F, F′.** The coset p + x + y, with x ∈ F and y ∈ F′, has bracket −3 + 9(f + f′) − 27ff′ ∈ {−12, 24, −48}. That is never 0, so two nonzero entries appear. Forbidden.
- **One 2-flat F and two 6-relations Z, Z′.** For {x, y} = F ∖ Z the bracket −3(1 + f) + 81ζ + 9ζf takes values in {84, −96, 72, −72}. Each of these gives a forbidden value.

**(8,1) is excluded.**

## 3. Theorem T144 (L = 10 is impossible at (3,144); hence L ≥ 12)

By §0, the admissible (s, |P∖Σ|) at L = 10 are (4,3), (5,2), (6,1), (6,2), (7,0), (7,1), (8,0), (8,1), (9,0) and (10,0). Each one is excluded:

| Configuration | Excluded in |
|---|---|
| (4,3), (5,2), (6,1), (7,0) | zero counts N_0 < 26, given affine independence (`rank6-144-L10-partial-reduction-v1.md`, f576731b) |
| (6,2) with a +1 flat | (★) (f576731b) |
| (6,2)-b, (7,1), (8,0)-C1′ remainder | slice patterns (`…-slice-pattern-reduction-v2.md`, f689a454) |
| (8,0)-C2′ and C1′ sub-cases | f576731b |
| (9,0) | `…-nine-coset-exclusion-v3.md` (3e3f02b9) |
| (10,0): windmill, n_8 = 3 | `…-ten-coset-partial-v4.md` (fb69ebd9) |
| (10,0): co-planar | `…-coplanar-exclusion-v5.md` (00254943) |
| (10,0): n_8 = 2 | `…-two-eight-relations-exclusion-v6.md` (a29f04d8) |
| (10,0): n_8 = 1 | `…-one-eight-relation-exclusion-v7.md` (4dd31596) |
| (10,0): n_8 = 0, and (8,1) | this file |

Since L is even and L ≠ 8 (Theorem S), we get **(3,144): L ≥ 12.** ∎

**Assurance caveat.** This conclusion rests on a long chain of hand case analyses (v1–v8 plus the consolidated lemmas). Each was checked by hand, and two draft errors were caught before pinning (checkpoints 069 and 070). An independent entire review of the whole chain is REQUIRED before any adoption. This is a WRITTEN author candidate only.

## Own WRITTEN rank-6 floors (unreviewed)

| Type | Floor |
|---|---|
| (3,112) | L ≥ 14 |
| (3,144) | L ≥ 12 |
| (3,128) | untouched (admitted L ≥ 8) |

The (24,24,2) gap and the original problem remain OPEN. Novelty and priority are UNCLEARED. All findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR, the cadence MAJORs, the checkpoint-054 attribution MINOR and the checkpoint-059 s = 6 erratum MINOR. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
