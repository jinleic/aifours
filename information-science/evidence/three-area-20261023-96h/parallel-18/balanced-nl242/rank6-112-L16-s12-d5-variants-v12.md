# Balanced NL242 (3,112) at L = 16, s = 12, d = 5 — variant (c) and variant (a4) with d_p = d_{p′} are excluded

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 09:42:08 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file is the successor to `rank6-112-L16-s12-d5-partial-v11.md` (d45cd945…fc47). It covers (3,112), L = 16, s = 12, d = 5 only. **This sub-case is NOT fully excluded.**

## 1. Variant (c): excluded

In variant (c), p is a (3,0) or (0,3) coset outside Π_5, active in all three slices, and y is a 2-valued Σ-coset active only at η_y.

- **T-row of p.** For η ≠ 0, Σ_β T χ = (12 + t_4)χ_4, or (t_4 − 4)χ_4 in the (0,3) case. So |υ_η(p)| ∈ {2, 4} in every slice.
- **At η_y.** Here a = 12 (all of Σ is active) and υ(p) = ε_p(3m − 64), with m ≡ 0 (mod 3) because τ = 0 (v11 lemma). So |3m − 64| ∈ {1, 8, 10, …} and never 2 or 4. ✗

## 2. Variant (a4) with d_p = d_{p′}: excluded

Here p and p′ are (1,1) cosets outside Π_5 with the same inactive slice η_0, and δ := p + p′ ∈ W_5 ∖ 0. The p-half cosets vanish at η_0. In η_1 and η_2, 14 points are active.

- **Slice values (Lemma Φ, s = 14).** For pure ā = p + v (v ∉ {0, δ}):
  ```
  υ = −(3/2)·ε_p·H(v),   H(v) := F(v) + εF(v + δ),   ε := ε_p ε_{p′}.
  ```
  Also υ(p) = ε_p(32 − (3/2)K), where K := m + εF(δ) ≥ 0.
- **Autocorrelation.** Σ_v F(v)F(v + δ) = 32F(δ), so Σ_v H² = 64K and H(0) = K, H(δ) = εK. Over the 15 pure pairs {v, v + δ}: Σ H² = 32K − K².
- **Pattern rule.** There is a zero at η_0, so |H| ∈ {0, 8} on the pure pairs. Hence K(32 − K) ≡ 0 (mod 64).
- **T-row of p.** The values {|32 − 1.5K|} over η_1, η_2 must be {2,2} or {4,8}, so K ∈ {20, 24, 16}. The congruence above leaves {16, 24}. So one slice has K = 24 (3 pairs, 6 cosets at ±12) and the other K = 16 (4 pairs, 8 cosets).
- **Moments.** On the p-half, 14 pure cosets have k = 2 and G = 4. p and p′ have G = 4 (Δ = ±48). The other 16 pure cosets are monochromatic with G ∈ {−4, 12}; let a of them have G = 12. Then:

  | Half | Σ G | Σ G² |
  |---|---|---|
  | p-half | 16a | 512 + 128a |
  | Π_5-half | 416 − 16a | 2816 − 128a |

  Cauchy–Schwarz on the Π_5-half gives (26 − a)² ≤ 16(22 − a), i.e. (a − 18)² ≤ 0. So a = 18, which exceeds 16. ✗

## 3. Variant (a4) with d_p ≠ d_{p′}: reduced, OPEN

The single-carrier slices η_p and η_{p′} have a = 12. The T-rows force m_{η_p} = m_{η_{p′}} = 24 and K_{η_b} = 24. p′'s inactive-slice T-row also gives F_{η_{p′}}(δ) = 0.

Total slice energy on the 30 pure p-half cosets is 1728 + 1728 + 864 = 4320 = 108t_3 + 144t_2, with t_2 + t_3 ≤ 30. So **t_2 = 30**: every pure p-half coset has k = 2 and G = 4. The Π_5-half then has Σ G = 288 and Σ G² = 2816, which is consistent with Cauchy–Schwarz. **OPEN.**

## Status at (3,112), L = 16

Open:

- s = 12, d = 5: variants (a2), (a3), and (a4) with d_p ≠ d_{p′};
- s = 15;
- s = 16.

**The floor stays L ≥ 16.**

**Dependencies.** v3, v7, v10, v11, the consolidated proof 6c5ce361, and S0017. Nothing from the NONINPUT set is used.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
