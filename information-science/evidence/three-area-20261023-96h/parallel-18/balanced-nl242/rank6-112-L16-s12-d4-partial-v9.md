# Balanced NL242 (3,112) at L = 16, s = 12, d = 4 — the equal-inactivity case is excluded; the other case is reduced

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 09:34:13 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file is the successor to `rank6-112-L16-s14-exclusion-v8.md` (7308ea6f…6ce3). It covers (3,112) at L = 16, s = 12 and d = dim aff(Σ) = 4 only. **This sub-case is NOT fully excluded.**

## 0. Shape

From v6 and v7:

- Σ = Π_4 ∖ C, where C is a 2-flat of the 4-flat Π_4;
- τ = 0 and G = +1;
- N_0 ≥ 52.

dim aff(P) = 6 needs two cosets outside Π_4, in distinct nonzero classes e_1 and e_2 of F_2^6/W_4 ≅ F_2^2. The budget 16 − 12 = 4 forces **two (1,1) cosets p and p′**, and every Σ-coset single.

Ψ_η is constant up to sign on the 4-element classes. Over the 16 classes, Σ Ψ_η² = 192, and the parity is constant because τ = 0. Hence (as in v3 C2):

- if G_η = +1: m = 12 − 3m_8 − 9m_12;
- if G_η = −1: m = 12 + 3j.

Either way **m_η ≡ 0 (mod 3) in every slice**.

## 1. Slice values on class e_1

Class e_1 is reached only as T = {p} ∪ E, with E ⊆ Σ even and ΣE = v ∈ W_4. Lemma Φ together with the even part 2^{12} cos(πΨ/3) gives:

| Active count | Value at v ≠ 0 | Value at p |
|---|---|---|
| 13 (p active, p′ inactive) | −6ε_p Z(v) | ε_p(6m − 64) |
| 14 (both active) | 3ε_p Z(v) | ε_p(32 − 3m) |

Here Z(v) := Σ_{ζ: 3|Ψ} (−1)^{ζ·v} over the 16 classes, and Z = −F for v ≠ 0. The 15 pure cosets of class e_1 vanish in p's inactive slice. Lemma SV then gives:

- at count 13: F ∈ {0, ±2}, so m is even;
- at count 14: F ∈ {0, ±4}, so m ≡ 0 (mod 4).

## 2. d_p = d_{p′} (same inactive slice): excluded

Both p-active slices have count 14. The T-row of p (v3 C3) requires {|32 − 3m_1|, |32 − 3m_2|} ∈ {{2,2}, {4,8}}.

- With m ≡ 0 (mod 4), {2,2} is impossible.
- {4,8} forces {m_1, m_2} = {12, 8}. But m ≡ 0 (mod 3) excludes m = 8. ✗

## 3. d_p ≠ d_{p′}: reduced, OPEN

The slices are η_p (p′ only, count 13), η_{p′} (p only, count 13) and η_b (both, count 14).

1. For p: m_{η_{p′}} ≡ 0 (mod 6) and m_{η_b} ≡ 0 (mod 12). The T-row forces m_{η_{p′}} = 12 (|υ| = 8) and m_{η_b} = 12 (|υ| = 4). Symmetrically, m_{η_p} = 12. So **m = 12 in all three slices**.
2. Class e_1 has 12 cosets with ±12 at η_{p′} (since (16·12 − 144)/4 = 12) and 3 with ±12 at η_b (since (192 − 144)/16 = 3). These are disjoint and cover all 15 pure cosets, so **every pure coset of class e_1 has k = 2**. The same holds for class e_2.
3. Class e_1 + e_2 is reached only at η_b. With υ = 3ε_pε_{p′}·Walsh(φ∘Ψ_{η_b})(t), Lemma SV gives values in {0, ±4}·3, with support of size m_{η_b} = 12. So 12 of its cosets have k = 2, and 4 are monochromatic.
4. ĥ_0 vanishes off the Π_4-class, so G = 4 at all 42 cosets with k = 2 (15 + 15 + 12). The second moment (N_0 = 52, total 624) is not yet violated: these classes contribute at least 42·6.25 + 4·30.25 = 383.5. **OPEN.** Finishing this case needs the Π_4-class cosets (the 4 points of C, and Σ, p, p′) in the moment identity Σ G = 416, Σ G² = 3328.

## Status

(3,112) at L = 16 is open only for:

- s = 12 with d = 4 and d_p ≠ d_{p′} (reduced as above);
- s = 12 with d = 5;
- s = 15;
- s = 16.

**The floor stays L ≥ 16.**

**Dependencies.** v2–v8, the consolidated proof 6c5ce361, and S0017. Nothing from the NONINPUT set is used.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
