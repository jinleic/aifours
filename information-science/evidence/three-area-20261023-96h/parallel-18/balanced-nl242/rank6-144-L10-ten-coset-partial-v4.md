# Balanced NL242 (3,144) at L = 10 — partial exclusion of the (10,0) configuration

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:12:26 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

This packet extends `rank6-144-L10-nine-coset-exclusion-v3.md` (SHA `3e3f02b9…2a7d`). **L = 10 at (3,144) is NOT excluded.**

## 0. Configuration

**(10,0):** P = Σ consists of 10 single-value cosets, all active in every slice. The dependency code R has dimension 3, i.e. 7 nonzero relations, and Σwt ≤ 40.

**Slice values.** For a pure ā = ΣT_0, Lemma Φ at s = 10 gives

```
υ_η(ā) = (1/8) g_η(T_0) Σ_{r∈R} w(|T_0 Δ r|) g_η(r),     w(m) = (−3)^{(m−1)/2},
```

using g_η(T_0 Δ r) = g_η(T_0) g_η(r).

**N_0 condition.** N_0 = (513 + 9V′)/24 ≥ 26 with integrality, where V′ := A_4 − 3A_6 + 9A_8 − 27A_10. This forces V′ ≥ 13 and V′ ≡ 7 (mod 8).

## 1. Excluded sub-cases

**ΣΣ = 0 (n_10 = 1).** The other six relations pair as complements of sizes (4, 6), and V′ ≥ 13 forces G = −1. For two of the three 2-flats, F_1 Δ F_2 must lie in R, so |F_1 ∩ F_2| ∈ {1, 2}. That gives exactly two shapes.

- **Windmill: |F_i ∩ F_j| = 1.** F_1 Δ F_2 = Σ∖F_3, so the three flats share one common point o and Σ = {o} ∪ A_1 ∪ A_2 ∪ A_3, where A_i := F_i ∖ {o}.
  1. Take a slice η ≠ 0 with G_η = −1. One exists, because G_η = −(−1)^{B·η} and B·η = 0 for some nonzero η.
  2. In that slice the pure coset o + x + y, with x ∈ A_i and y ∈ A_j for i ≠ j, has the eight representation sizes 3, 7, 3, 3, 5, 7, 7, 5.
  3. Its value is υ = 3(1 + f_i + f_j)g ∈ {9g, 3g, −3g}, where f := g_η(F). None of these lies in {0, ±6, ±12}. **Excluded.**
- **Co-planar: |F_i ∩ F_j| = 2.** Here F_3 = F_1 Δ F_2, so with F_1 = {a, b, c, d} and F_2 = {a, b, e, f}, F_3 = {c, d, e, f}, and Γ := Σ ∖ (F_1 ∪ F_2) has 4 points. This shape is **NOT excluded**. Partial constraints:
  - The cosets ΣT, T ⊂ Γ with |T| = 3, take ±6 only when G_η = −1; they take −15g or 0 when G_η = +1. Hence G_η ≡ −1 and B = 0.
  - The cosets a + c + g (and their analogues for F_2 and F_3) take the value 3(1 + f_i)g. Hence each f_i is constant in η, i.e. B_i = 0.
  - The cosets a + c + e then exclude f_1 = f_2 = 1.
  - So (f_1, f_2) ∈ {(1, −1), (−1, 1), (−1, −1)} and V′ = 23. No contradiction has been found yet.

**ΣΣ ≠ 0 with three 8-relations (n_8 = 3).**

1. R = {Σ∖π_i, π_i ∪ π_j, Q}, where π_1, π_2, π_3 are disjoint pairs summing to ΣΣ and Q is the remaining 2-flat. V′ ≥ 13 forces g(π_i) = g(Σ) for all i, so every relation has g = +1 at slice 0 (V′ = 31).
2. In slice η, g_η(r) = (−1)^{λ_η(r)}, where λ_η ∈ R* depends linearly on η. Write λ_i := λ(Σ∖π_i).
3. For the pure cosets x + y + z with x ∈ π_i, y ∈ π_j, z ∈ Q, the slice value is (1/8)g[−3(1 + e_i e_j) − 27(e_i + e_j) + 9e_k(1 + e_i)(1 + e_j)]. This lies in {−3g, −12g, 0, 6g} according to (e_i, e_j, e_k).
4. The slice-pattern rule then forces, for every pair {i, j}, that one of λ_i, λ_j is identically zero in η while the other has rank 1. Applied to all three pairs, two of λ_1, λ_2, λ_3 are identically zero. For that pair the map has rank 0. Contradiction.

## 2. Remaining

**(10,0) with ΣΣ ≠ 0 and n_8 ≤ 2** (V′ ∈ {15, 23}), and **(8,1)**. Both are NOT analysed to completion.

## Status

**WRITTEN:** the exclusion of the two (10,0) sub-cases above. The (3,144) floor stays L ≥ 10.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
