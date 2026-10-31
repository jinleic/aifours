# Balanced NL242 (3,144) at L = 10, (10,0) with ΣΣ ≠ 0 — the case of two 8-relations is excluded

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:18:10 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

This addendum to `rank6-144-L10-ten-coset-partial-v4.md` (fb69ebd9) and `rank6-144-L10-coplanar-exclusion-v5.md` (00254943) handles the case n_8 = 2. **L = 10 at (3,144) is still NOT excluded.**

## 1. Forced relation structure

Write τ := ΣΣ ≠ 0. The two 8-relations are r_1 = Σ∖π_1 and r_2 = Σ∖π_2, where π_1 = {p_1, p_1′} and π_2 = {p_2, p_2′} are pairs summing to τ. Their sum is π_1 ∪ π_2, and Ψ := Σ∖(π_1 ∪ π_2) has 6 points.

**Signs.** V′ = A_4 − 3A_6 + 9A_8 ≥ 13 forces A_8 = 2, so g(r_1) = g(r_2) = g(π_1 ∪ π_2) = +1. The fourth generator X has a coset of 4 relations (two 4-sets and two 6-sets, since Σwt ≤ 40), all with the same sign ξ. Then V′ = 15 when ξ = +1 and V′ = 23 when ξ = −1.

**Shapes.** Solving the size conditions for (|X∩π_1|, |X∩π_2|, |X∩Ψ|) leaves two shapes:

- **(A)** 4-relations X = {p_1, p_2, ψ_1, ψ_2} and X′ = {p_1′, p_2′, ψ_1, ψ_2}; 6-relations {p_1, p_2′} ∪ Ψ″ and {p_1′, p_2} ∪ Ψ″, where Ψ″ = Ψ∖{ψ_1, ψ_2}.
- **(B)** 4-relations {p_1, ψ_a, ψ_b, ψ_c} and {p_1′, ψ_d, ψ_e, ψ_f}. The analogous shape B′ with π_2 is symmetric.

## 2. Slice analysis

In slice η, write u_i := g_η(r_i) = (−1)^{λ_i(η)} and v := g_η(X) = ξ(−1)^{λ_X(η)}. For a pure ā = ΣT_0,

```
υ_η(ā) = (1/8) g_η(T_0) Σ_{r∈R} w(|T_0 Δ r|) g_η(r),     w(m) = (−3)^{(m−1)/2}.
```

**Shape A.**

1. The coset ψ_3 + ψ_4 + ψ_5 has representation sizes 3, 5, 5, 7, 7, 7, 3, 3. Its bracket is −3(1 + vu_1 + vu_2) + 9(u_1 + u_2) − 27(u_1u_2 + v + vu_1u_2). The table over (u_1, u_2, v) allows only (1, 1, −1) → −6, (−1, −1, 1) → −12 and (−1, −1, −1) → 0. The values 9 and 3 are excluded.
2. The pattern rule leaves u_1 = u_2 = 1 and v = −1 in every slice. Hence λ_1 = λ_2 = λ_X ≡ 0 and ξ = −1, so N_0 = 30. All brackets are then independent of η.
3. Two families of brackets vanish at (1, 1, −1):
   - **(iii)** p_1 + ψ + ψ′ with ψ, ψ′ ∈ Ψ″ (sizes 3, 7, 5, 5, 5, 7, 3, 5): 12 cosets.
   - **(iv)** p_1 + ψ_1 + ψ (sizes 3, 7, 5, 5, 3, 5, 5, 7): 16 cosets.
   The analogous families for the other points follow by symmetry. This gives **28 monochromatic cosets**, and ĥ_0 = 0 at each.
4. So 28 × 60.06 = 1682 > 1020 = 64·30 − 30². Contradiction.

**Shape B.**

1. The coset p_2 + ψ_a + ψ_d has bracket −3 + 9u_1(1 + u_2) + 9v(1 + u_1)(1 + u_2) − 27u_2. That forces u_2 = 1 in every slice, i.e. λ_2 ≡ 0.
2. The coset p_1 + ψ_a + ψ_d has bracket (1 + v)(6 − 18u_1). Its pattern must be all zero, since all-±6 would need u_1 ≡ −1. Hence v ≡ −1, λ_X ≡ 0 and ξ = −1, so N_0 = 30.
3. The 9 cosets p_1 + ψ_{abc} + ψ_{def} and the 9 symmetric p_1′ cosets are then monochromatic, with ĥ_0 = 0 at slice 0.
4. So 18 × 60.06 = 1081 > 1020. Contradiction.

**Conclusion (WRITTEN).** The case (10,0), ΣΣ ≠ 0, n_8 = 2 is excluded.

## 3. Remaining at (3,144), L = 10

- **(10,0) with ΣΣ ≠ 0 and n_8 ∈ {0, 1}.** For n_8 = 1, V′ ∈ {15, 23}. For n_8 = 0, V′ = 15 with n_6 ≥ 4.
- **(8,1).**

Neither has been resolved. The floor stays L ≥ 10.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
