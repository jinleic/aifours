# Balanced NL242 (3,112) at L = 16, s = 12, d = 4 — the remaining case d_p ≠ d_{p′} is excluded by a class moment bound

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 09:35:58 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file completes the open case of `rank6-112-L16-s12-d4-partial-v9.md` (b489d713…4bcf), which stays unchanged. It covers (3,112), L = 16, s = 12, d = 4 only.

## Setting (from v9 §3)

Recall:

- N_0 = 52, since both admissible slice-0 shapes give exactly 13 zero classes of size 4;
- every pure coset of classes e_1 and e_2 has k = 2 (30 cosets);
- 12 cosets of class e_1 + e_2 have k = 2, and its other 4 are monochromatic;
- ĥ_0 vanishes off the Π_4-class.

So G = 4k − 4 + cĥ_0/3 = 4 at the 42 cosets with k = 2, and G ∈ {−4, 12} at the 4 monochromatic ones. Let a be the number of those 4 with G = 12.

**The P-cosets p and p′.** By v9 §3, the T-row of p has Δ = t_3 − t_4 = ±48, so t_3 + t_4 = −8. Then c_p s_p = (−12 + 4 + t_3 + t_4)/8 = −2. Since ĥ_0(p) = 0, the census identity c s = 4 − (3/2)G + cĥ_0/2 gives **G(p) = 4**. The same holds for p′.

## Moment bound

Over all 64 cosets, Σ G = 8N_0 = 416 and Σ G² = 64N_0 = 3328.

| Classes | Σ G | Σ G² |
|---|---|---|
| e_1 and e_2 (32 cosets, including p and p′) | 128 | 512 |
| e_1 + e_2 | 48 + (16a − 16) | 192 + (128a + 64) |
| Π_4-class (16 cosets: Σ and the 4 points of C), by subtraction | 256 − 16a | 2560 − 128a |

Cauchy–Schwarz on the Π_4-class gives (256 − 16a)² ≤ 16(2560 − 128a). That is, (16 − a)² ≤ 160 − 8a, i.e. a² − 24a + 96 ≤ 0, i.e. a ∈ [12 − √48, 12 + √48] ≈ [5.07, 18.93]. But 0 ≤ a ≤ 4. ✗

## Theorem P12d4-16

**s = 12 with d = 4 is impossible at (3,112), L = 16.** Both cases are excluded: d_p = d_{p′} by v9 §2, and d_p ≠ d_{p′} here. ∎

Updated L = 16 status:

- **Excluded:** s ∈ {0, …, 11, 13, 14}; s = 12 with d ∈ {4, 6}; s = 12 with τ ≠ 0 or G = −1.
- **Open:** s = 12 with d = 5 (τ = 0, G = +1, N_0 = 52 extremal), s = 15 and s = 16.

**The floor stays L ≥ 16.**

**Dependencies.** v9, v7, v6, the consolidated proof 6c5ce361 (census, second-moment identities, Lemma SV), and S0017. Nothing from the NONINPUT set is used.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
