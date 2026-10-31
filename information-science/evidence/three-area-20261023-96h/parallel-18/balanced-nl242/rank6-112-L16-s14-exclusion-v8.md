# Balanced NL242 (3,112) at L = 16 — s = 14 is excluded

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 09:30:30 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file is the successor to `rank6-112-L16-s8-s10-exclusion-v7.md` (ee101e8d…4fd0). It covers (3,112) at L = 16 only, where N_0 ≥ 52 (wt(h_0) ≤ 12). **L = 16 is NOT excluded.**

## 0. Shapes at s = 14, L = 16

The budget leaves 2 extra small values. Either:

- **(i)** P = Σ, with the extra values inside Σ-cosets, and d := dim aff(Σ) = 6; or
- **(ii)** P = Σ ∪ {p}, with p balanced (1,1), every Σ-coset single, and d ∈ {5, 6} (Theorem M).

Every slice-0 statement below depends only on Σ and the residues g mod 3.

## 1. d = 6 is impossible

Lemma H at L = 16 forbids sides of size 1, 2, 3 and 5, so the splits are 4|10, 6|8 and 7|7. This gives the same W-moment equations as v4 P14a / §4.

- **τ ≠ 0.**
  1. The moments give n_0 = 32, n_6 = 18, n_2 = 13 and n_4 = 17.
  2. Each side of a 7|7 split needs N ≥ 40, i.e. X_7 = 1 + 9A_4 − 27A_6 ≤ −56. With A_6 ∈ {0, ±1}, this forces A_4 ≤ −4, so each side contains at least 4 negative planes.
  3. Double counting (each plane lies inside a side for at most 8 of the 32 splits with τ·ω = 1) gives 8n_4^− ≥ 32·2·4, so n_4^− ≥ 32 > 17. ✗
- **τ = 0, G = −1.** The moments give (n_6, n_2, n_0, n_4) = (14, 49, 0, 14). The rigidity theorem of v5 §1 uses only these numbers and the fact that 4-sides are positive planes, both of which hold at L = 16. It forces the e7² configuration with **N_0 = 50 < 52**. ✗
- **τ = 0, G = +1.** Every w is even, so Ψ ≡ 2 (mod 4) and the zeros have |Ψ| = 6. Then ΣΨ² ≥ 52·36 > 896. ✗

## 2. d = 5 is impossible (shape (ii), p outside Π_5)

**Slice values on the p-half.** In a p-active slice the active set inside Π_5 is all 14 Σ-cosets. This is an even number, so the formulas of v3 §1 hold verbatim (the general-a computation gives the same expressions for either parity of a):

```
υ_η(p + v) = 3ε_p F_η(v)   (v ≠ 0),     υ_η(p) = ε_p(3m_η − 64),
```

where m_η is the number of classes ζ ∈ F_2^6/⟨ω⟩ with 3 ∤ Ψ_η(ζ).

- **(C1)** The 31 cosets p + v are pure and vanish in p's inactive slice. So F_η ∈ {0, ±4}, and m_η ≡ 0 (mod 4).
- **(C3)** The T-row of p gives {|υ_{η_1}(p)|, |υ_{η_2}(p)|} ∈ {{2,2}, {4,8}}. Combined with C1, one p-active slice needs **m = 20**.
- **(C2′) m = 20 is impossible for any 14-point Ψ_η.** The classes satisfy Σ Ψ² = 448.
  - **Constant parity (τ = 0).** If w is even: m = 22 + 3j + 6j′. If w is odd: m = 28 − 3m_8 − 9m_12. Both are ≡ 1 (mod 3), so m ≠ 20.
  - **Mixed parity (τ ≠ 0), 16 + 16 classes.** The total is 896 − 48m_A + 48(2j + 4j′ + m_8 + 3m_12) = 448, which needs 48 | 448. It does not. ✗

So d = 5 is impossible. Note that d = 5 forces shape (ii), since shape (i) would have dim aff(P) = 5.

## 3. Theorem P14-16

**s = 14 is impossible at (3,112), L = 16.** ∎

Updated L = 16 status:

- **Excluded:** s ∈ {0, …, 11, 13, 14}, and s = 12 except for d ∈ {4, 5} with τ = 0, G = +1.
- **Open:** s = 12 (d ∈ {4, 5}), s = 15 and s = 16.

**The floor stays L ≥ 16.**

**Dependencies.** v2 (Lemma PP), v3 (§1 formulas, C1/C3), v4 (Lemma H and the moments), v5 (rigidity), v6 and v7, the consolidated proof 6c5ce361, and S0017. Nothing from the NONINPUT set is used.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
