# Triple-layer Gram note v3: erratum to v2 and sharpened bound (written research only)

Supplements `cycle2/triple-layer-gram-note-v1.md` (4a68eeef659a05f925d12b0da2221501cc71ed52d4427c0e83483ddb0ee427bc) and `cycle2/triple-layer-gram-note-v2.md` (cd4cac0d33da60fbaf0cda196e12be474453154dde5388758da6e2bca3bf4f4e). Both stay unchanged. Written after host clock read 2026-10-18T14:5x-0700. No probe, list or native work. Hypotheses and notation as in v1 §0.

## Erratum: v2 C5 is WITHDRAWN as a restriction

v2's bound q_AB <= 6.49 + 1.53 N2 is implied by elementary incidence counting, so it restricts nothing.

- Each row r of A_j lies in 1 + n2(r) other quads and in n2(r) pair blocks.
- So the QP blocks of other columns have 4 + 2 N2(A_j) incidences with A_j, and likewise with B_j.
- A block counted in q_AB uses one incidence on each side. Hence q_AB <= (8 + 2 N2)/2 = 4 + N2, which is below 6.49 + 1.53 N2 for every N2 >= 0.

v2's sentence "C5 is a genuine global restriction" is wrong; this erratum replaces it. C2' and C3' of v2 are unaffected.

## C2* (sharper ms09 expansion bound, by Cauchy-Schwarz over the 34 triples)

For a row set S with |S| = k and N2 = N2(S), let a_T = |T ∩ S| for each of the 34 triples T. Then:

1. Σ_T a_T = Σ_{r in S} tT(r) = 6k - 2 N2.
2. Σ_T C(a_T, 2) = C(k, 2) - e_QP(S), since every pair is covered exactly once (L = 0).
3. Cauchy-Schwarz: Σ_T a_T^2 >= (Σ_T a_T)^2 / 34.

Combining these with e_QP(S) = (6k + 4 N2 - cut_QP(S))/2 gives

    cut_QP(S)  >=  f(k, N2) := k + k^2/17 + 6 N2 - (12 k N2 - 2 N2^2)/17.

f is exactly invariant under (k, N2) -> (19 - k, 6 - N2); expanding 17 f on both sides gives the same polynomial. C2* is at least as strong as v1's C2, because it uses the optimal centering instead of 3k/19. It is the PSD content of TG on the test vectors 1_S - α1, optimized over α.

**Where it is non-trivial.** Elementary counting allows e_QP(S) up to 3k + 2 N2, the case where every QP neighbor of S lies in S. C2* forces at least f(k, N2) of the QP-degree of S to leave S. So C2* binds only for near-closed sets: sets containing most of the QP neighborhoods of their rows.
- **C3 as a special case.** For closed sets it gives C3 directly. f > 0 when k <= 8, since then 6 - 12k/17 > 0. For k = 9, f >= 9 + 81/17 - 6·(6/17) > 0. For k >= 10, use the symmetry.
- **No other check.** No other application has been checked.

## Status

- Lemma TG (v1), C1-C3 (v1), C2' and C3' (v2) and C2* (v3) are rigorous.
- v2's C5 is withdrawn.
- Nothing has been evaluated on any configuration, so pruning strength is unknown.
- No uniform obstruction is known. The v1 §4 analysis (items 1-3) stands. The 151 lane-original open M2 cases remain open.
