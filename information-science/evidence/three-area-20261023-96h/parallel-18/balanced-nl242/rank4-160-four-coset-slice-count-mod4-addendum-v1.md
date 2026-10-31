# Addendum to `rank4-160-four-coset-strata-Q-shape-and-R-side-reduction-v1.md` — a mod-4 slice count and row-uniform parity

Owner **InfoBalancedNL242-2**, slot info-6. Last actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:00:04 PDT 2026**. The post-write clock is recorded in checkpoint 056.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no claims of formal status or novelty. No program was run.

**Base packet:** `rank4-160-four-coset-strata-Q-shape-and-R-side-reduction-v1.md`, SHA `5517814f…7962`. **Inputs:** the same admitted S0017 cut, plus Proposition F and Theorem E of `u-class-L-parity-and-rank4-160-coset-projection-v1.md` (SHA `7cecd509…0c9b`).

## 1. Slices

Use coordinates a = (ā, β) with V = {(0, β)}, and dual x = (ξ, η) with V^⊥ = {(ξ, 0)}.

For η ≠ 0 we have q = 0 on slice η. By S0017 (3):

```
u(ξ,η) ≡ −h_η(ξ) (mod 3),   h_η(ξ) := Σ_ā g_η(ā)(−1)^{ā·ξ},   g_η(ā) := Σ_β δ(ā,β)(−1)^{β·η}.
```

So m_η := |supp(a) ∩ slice η| = #{ξ : h_η(ξ) ≡ 0}. Summing over all slices,

  Z_3(δ) = N_+ + Σ_{η≠0} m_η.

## 2. Lemma S (mod-4 slice count)

**Lemma S.** At (2,160), suppose every small S-value lies in the cosets of a set Σ* that is an affine 2-flat or a subset of one. Then **L + 4N_+ ≡ 0 (mod 8)**. In particular, if N_+ = 0 then L ≡ 0 (mod 8).

*Proof.*

1. For η ≠ 0, put s := |supp g_η|, where supp g_η ⊆ Σ*. The proof of Theorem E gives m_η = 16, 0, 8, 4 for s = 0, 1, 2, 3.
2. If s = 4, then supp g_η is the whole flat, so its sum is zero, and m_η = 6 + 6Π g_η ∈ {0, 12}.
3. Hence m_η ≡ 0 (mod 4) for every η ≠ 0, so Z_3 ≡ N_+ (mod 4).
4. Proposition F gives Z_3 = 100 + L/2 + 3N_+. Hence 100 + L/2 + 3N_+ ≡ N_+ (mod 4), i.e. L/2 + 2N_+ ≡ 0 (mod 4), i.e. L + 4N_+ ≡ 0 (mod 8). ∎

**Corollary S.** Consider the |Σ| = 4 strata of Theorem E, where N_+ = 0.

- In the strata with **L = 12**, i.e. (α, L, u) = (6, 12, 8) and (4, 12, 16), at least one coset OUTSIDE Σ carries small values. Such a coset has λ ≡ μ (mod 3) and (λ, μ) ≠ (0, 0), so λ + μ ≥ 2. Hence L_Σ ≤ 10.
- Only the stratum (α, L, u) = (4, 16, 8) may have all small values inside the four Σ-cosets.

## 3. Lemma U (row-uniform parity, any (2,160) target)

**Lemma U.** For every η and every coset ā, with

- υ_η(ā) := (1/32) Σ_β S(ā,β)(−1)^{β·η}
- ω_η(ā) := (1/32) Σ_β R(ā,β)(−1)^{β·η},

we have υ_η(ā) ≡ ω_η(ā) ≡ |supp(u) ∩ slice η| (mod 2). The common parity is independent of ā.

Write T = −4 + 8τ with τ ∈ {±1, ±3}. For η ≠ 0 this means υ_η(ā) = c_ā τ̂_ā(η)/4, so τ̂_ā(η) ≡ 4m_η (mod 8) for every ā.

*Proof.* υ_η and ω_η are the 4-variable Walsh transforms of the slice restrictions of u and of a. These are {0, ±1}-functions, and their supports are complementary in a 16-point slice. Every Walsh value of a {0, ±1}-function has the parity of its support size. ∎

**Consequence for cosets with no small value** (stated WRITTEN, not yet exploited). On such a coset, τ = 3ε_ā for a ±1 function ε_ā, whatever the value of D̄. Then ε̂_ā(η) ≡ 4m_η (mod 8) for every η ≠ 0.

- If the coset has k = 8, then ε_ā is balanced, and every Walsh value of ε_ā is ≡ 0 (mod 4), so deg ε_ā^B ≤ 3.
- In that case η ↦ ε̂_ā(η)/4 mod 2 is the affine function P_ā(0) + c(ā)·η, where c(ā) ∈ F_2^4 is the vector of cubic ANF coefficients of f = ε_ā^B. *Proof sketch.*
  - ε̂(η)/4 ≡ wt(f + ℓ_η)/2 (mod 2).
  - For g of degree ≤ 3 on F_2^4, inclusion–exclusion over ANF monomials gives wt(g) ≡ 2·#{cubic monomials} + 2·#{pairs of monomials whose variable sets cover all of [4]} (mod 4).
  - Adding ℓ_η changes only the linear monomials. Among the covering pairs, only (cubic [4]∖i, linear x_i) involve them. So the count changes by Σ_i c_i η_i (mod 2).
- For k = 8, P_ā(0) = (wt f mod 4)/2 = 0, while υ_0(ā) = s_ā = −2c_ā is even. Hence the existence of such a pure coset forces α even and m_η ≡ c(ā)·η (mod 2) for all η. All pure k = 8 cosets therefore share one cubic-coefficient vector c.

## 4. Status

**WRITTEN:** Lemma S, Corollary S and Lemma U, with its consequence.

**Not proved:** exclusion of any |Σ| = 4 stratum, any |Σ| ≥ 5 case, or the (2,160) type. The (24,24,2) gap and the original problem remain OPEN.

**First unproved step.** In the (4, 16, 8) stratum, with all small values inside Σ, use the 15 slice counts m_η ∈ {0, 4, 8, 12, 16}, which must total 108. Combine them with the shared cubic vector c and the per-row R census. In the L = 12 strata, use the forced off-Σ coset.

Novelty is UNCLEARED. All earlier findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT; no early park.
