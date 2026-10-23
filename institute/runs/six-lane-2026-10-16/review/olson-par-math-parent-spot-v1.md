# Parent mathematical spot check: the PAR closure core

Recorded 2026-10-17T18:35:41-07:00. This is a direct mathematical reading by the parent, not a machine proof or final acceptance. Both hostile CLI reviews remain pending. It neither verifies the census programs nor proves ordered Olson.

## Pinned read set

- `inverse-parity/mixdef-low/c2/proof-R4-closure.md`: `74929e9c40ebe893ab7466e4960be739b701c3739e2236b4ada79490690333f6`; LF14–50.
- `inverse-parity/mixdef-low/c2/proof-Rstar-r3.md`: `acdde81fd4bdc46b0739082c0cc4c08be2ca5fd7b78b18b5a3d81cf71f054e2b`; LF25–63 and LF173–198.
- `inverse-run-count/proof-RUNS.md`: `e3682f4d02ab0062cddfda8d4199f4307860936581cf75b843a93e91dec40661`; LF400–414.

## Lemma R4: independent calculation

Assume the source's setting and previously stated kill lemma KL, with k ≤ p, g ≥ 1, 1 ≤ B ≤ g, nonempty free set F = Z0+, X = phi(F) ≥ 0, X + m(F) ≤ g, and the R*** inequality 2X + alpha ≥ 2g + s + S_Z. Every run has phi_t ≤ g−1 and bh_t ≤ s.

1. F is proper since BH([k]) = k−2g = B+s+1 > 0 while BH(F) ≤ 0. Thus m(F) ≥ 1 and X ≤ g−1. Free aligned runs have phi_t ≥ 1; all other free runs have phi_t ≥ 0. Hence their number n_d ≤ X.
2. Let C be the total mass of free anti runs. Then C ≥ alpha, D(F) = S_Z+n_d−C, and delta+ = −BH(F) = 2X−S_Z−n_d+C ≥ 2g+s−n_d ≥ g+s+1. Also alpha ≥ 2m(F)+s+S_Z ≥ s+2, so s ≤ B−2 ≤ g−2.
3. The positive-bh set Y is a disjoint union of paths, because the nonpositive-bh set contains F. Its total BH is B+s+1+delta, where delta ≥ delta+. Taking the heavier alternating class of each path produces an independent set with BH > s+1. Greedy accumulation, using 1 ≤ bh_t ≤ s, produces an independent N with s+1 ≤ BH(N) ≤ 2s and |N| ≥ 2.
4. If phi(N) ≤ p−k+g−1+|N|, the proper nonempty complement S' has c(S') = p−k+2g−phi(N)+|N| ≥ g+1 and BH(S') ≤ B. KL applies.
5. Otherwise integrality gives phi(N) ≥ p−k+g+|N| ≥ g+2. For S = F ∪ N, BH(S) ≤ −(g+s+1)+2s = s−g−1 < 0, so S is proper. Now c(S) ≥ X+phi(N)+1 ≥ g+3 and KL applies again.

**Ordering clarification, not a counterexample:** source closure LF32–34 writes the lower bound on c(S) before establishing S is proper. Establish BH(S)<0 first, as in step 5 above; then m(S)≥1 is justified. No additional hypothesis is needed.

## Lemma M0: the monotonicity used by the assembly

For each proper run pattern, removing one positive and one negative rotation from a mixed run decreases each effective count E+ and E− by one. Adding two identical reflections to an existing constant reflection run preserves all reflection-run parities and values, and raises H and h(P) by one. Therefore

    g'_P(E−1) = min(p−m, E+m+h−p, floor((E−1)/2)) ≤ g_P(E).

The integer intervals, and hence their images mod p, are contained in the original windows. The pattern phase is unchanged, so avoidance transfers in the required direction. The same calculation covers the empty pattern (m=0). The r_t≥3 condition keeps the shortened rotation run nonempty; a (1,1)-pair is not shortened. Both kappa and B decrease by one, leaving g=kappa−B unchanged. This does not preserve every inherited inequality, and the source explicitly says so: any later invocation must use results valid without those inherited hypotheses.

## What remains to check before acceptance

- The two CLI reviewers must check the whole import chain and the PAR assembly, including the B=0 branch after M0 and the precise hypotheses of Lemma OR, K0/K1/K1'/KB and S1'/A1'.
- The above algebra is conditional on the source's KL and interval-domain statements. It does not replace their reviewed proofs.
- No finite census or synthetic case is a hypothesis of the written R4 argument.
