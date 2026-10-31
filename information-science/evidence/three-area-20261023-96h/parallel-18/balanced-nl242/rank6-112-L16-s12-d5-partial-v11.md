# Balanced NL242 (3,112) at L = 16, s = 12, d = 5 — partial reduction (variants (a1) and (b) excluded; four variants open)

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 09:38:33 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file follows `rank6-112-L16-s12-d4-exclusion-v10.md` (c52b0f65…7e62). It covers (3,112), L = 16, s = 12, d = 5 only. **This sub-case is NOT excluded.**

## 0. Setting

From v7 §3:

- Σ ⊆ Π_5 = a + W_5, with τ = 0 and G = +1;
- N_0 = 52 exactly, at the extremum: every plane and every 8-relation positive, every 6-relation negative.

The budget beyond the 12 single values is 4, and at least one P-coset lies outside Π_5. The variants are:

- **(a)** one (1,1) coset p outside Π_5, plus one of:
  - (a1) a 3-valued Σ-coset;
  - (a2) two 2-valued Σ-cosets;
  - (a3) a (1,1) coset p′ inside Π_5;
  - (a4) a (1,1) coset p′ outside Π_5;
- **(b)** one (2,2) coset outside Π_5;
- **(c)** one (3,0)/(0,3) coset outside Π_5, plus one 2-valued Σ-coset.

## 1. Congruence lemma for m (classes of F_2^6/⟨ω⟩, Σ_classes Ψ² = 32a)

Let A be the active set in Π_5 with |A| = a.

| a | Parity | Result |
|---|---|---|
| 12 | constant (τ_A = 0) | m ≡ 0 (mod 3) (v3 C2) |
| 11 | — | 9(32 − m) + m + 24(3z_9 + n_5 + 2n_7 + 5n_11) = 352, so m ≡ 1 (mod 3) |
| 13 | — | 288 − 8m + 24(…) = 416, so m ≡ 2 (mod 3) |
| 10 | 16 + 16 classes (τ_A = y + y′ ≠ 0) | 3m_A − m = 16 + 6j + 3m_8, so m = 24 is impossible and m = 20 is possible |

In every case the p-half formulas υ(p + v) = 3ε_p F(v) and υ(p) = ε_p(3m − 64) hold, for either parity of a.

## 2. Exclusions

- **(b).** The (2,2) coset is active only at η^*, where |υ(p)| = |−24 − 8|/8 = 4. That forces m = 20. But a = 12 there, so m ≡ 0 (mod 3). ✗
- **(a1).** Lemma SV and the T-row of p (v3 C1/C3) force {m_1, m_2} = {20, 24} over the two p-active slices.
  - If the 3-valued coset is active in both p-active slices, then a = 12 in both, and m = 20 is impossible. ✗
  - If it is inactive in one of them, that slice has a = 11, so m ≡ 1 (mod 3) and m ∉ {20, 24}. ✗

## 3. Open variants and forced data

- **(a2).** Survives only if both 2-valued cosets are active in the same p-active slice (a = 12, m = 24), with the other p-active slice at a = 10 and m = 20.
- **(a3).** Survives only if p′ is active in exactly one p-active slice (a = 13, m = 20), with the other at a = 12 and m = 24.

In both of these, the p-half carries 27 cosets with k = 2 (G = 4) and 4 monochromatic cosets, and G(p) = 4. The class moment bound then gives a ∈ {3, 4} for the number of monochromatic cosets with G = 12, and forces near-constant G (mean 8 to 8.5, total variance 120 or 256) on the Π_5-half. **No contradiction yet.**

- **(a4)** (two outside (1,1) cosets) and **(c)** ((3,0) coset active in all slices) are **not analysed**.

## Status

At (3,112), L = 16, the open cases are:

- s = 12 with d = 5, variants (a2), (a3), (a4) and (c);
- s = 15;
- s = 16.

**The floor stays L ≥ 16.**

**Dependencies.** v3, v7, v10, the consolidated proof 6c5ce361, and S0017. Nothing from the NONINPUT set is used.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
