# Balanced NL242 (3,112) at L = 16, s = 12, d = 5 — the zero slice is a six-character configuration, ĥ_0 = −8g on Σ, and G ∈ 4Z on the Π_5-half

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 09:45:24 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file is the successor to `rank6-112-L16-s12-d5-variants-v12.md` (7aac4fe0…0b7f). It gives structural facts for the open variants (a2), (a3), and (a4) with d_p ≠ d_{p′}. **No new exclusion.**

## 1. Six-character theorem (zero slice)

At s = 12, d = 5 we have τ = 0, G = +1, and the extremum N_0 = 52 with all 15 planes positive (v7 §3).

1. Ψ ≡ 0 (mod 4), and exactly 6 of the 32 classes have 3 ∤ Ψ.
2. Parseval over the classes (384) allows only (m_12, m_8, m_4) ∈ {(0,6,0), (1,3,3), (2,0,6)}.
3. The fourth moment over the classes is 32(3·144 − 24 + 24·15) = 24576. Only (0,6,0) gives 6·8⁴ = 24576; the other two give 33792 and 43008.

So **Ψ ∈ {0, ±8}, with exactly 6 nonzero classes.** Fourier inversion on the 5-flat gives g·1_Σ = (1/4)Σ_{i=1}^{6} ε_i χ_{ζ_i}. For this to be {0, ±1}-valued, every point must have an odd number of negative terms, so Σζ_i = 0 and Πε_i = −1.

One example (hand-checked) is Σ = B_1(0) ∪ B_1(1) ⊆ F_2^5, with g = +1 on the weight-0 and weight-1 points and −1 on the weight-4 and weight-5 points. Its 15 planes are {0, e_i, 1, ē_i} and {e_i, e_j, ē_i, ē_j}, all positive. Uniqueness up to equivalence is **not** claimed.

## 2. Consequences

- **h_0 and its transform.** h_0 = φ(Ψ) = −Ψ/8, so **ĥ_0 = −8·g·1_Σ**. Hence ĥ_0 vanishes at every pure coset, and ĥ_0(x) = −8g(x) on Σ.
- **G on the Π_5-half.** The census c s = 4 − (3/2)G + cĥ_0/2 gives:

  | Coset | G |
  |---|---|
  | Pure Π_5 cosets | 4k − 4 |
  | Σ-coset x (with the T-row c s = −2 + 3Σ′ε + δ′ and c_x g(x) = −δ′) | 4 − 2Σ′ε + 2δ′ ∈ {−4, 0, 4, 8, 12} |
  | A Π_5 balanced coset p′, variant (a3) | ∈ {0, 4, 8} |

  So **G ∈ {−4, 0, 4, 8, 12} on the whole Π_5-half.**
- **Moment equations for (a2) and (a3)** (from v11 and v12, with a ∈ {3, 4}). Write G = 4γ, γ ∈ {−1, …, 3}, over the 32 Π_5-half cosets. Then Σγ = 80 − 4a and Σγ² = 176 − 8a.
  - If γ ∈ {1, 2, 3} only, the solution is (n_1, n_2, n_3) = (2, 24, 6) for a = 3, and (8, 16, 8) for a = 4.
  - So most pure Π_5 cosets have k = 3 and are therefore nonzero in all three slices.
- **(a4) with d_p ≠ d_{p′}** (v12 §3): Σγ = 72 and Σγ² = 176 on the Π_5-half.

Finishing these variants needs the η_0 slice values on the Π_5-half, with Σ fixed as above and arbitrary slice twists. **OPEN.**

**The floor stays L ≥ 16.** The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
