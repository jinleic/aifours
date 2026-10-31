# One complete 15th-root two-coset spectrum is impossible over all fields

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:44:16 PDT 2026. This rules out one spectral family for a cyclic-equivariant G6 lift with **arbitrary** complex phases and real spectral populations; it does not rule out all cyclic spectra, symmetry-breaking lifts or 1RQLS10.

## Statement

Under the cyclic hypotheses of `frontier-20261029-cyclic15-unrestricted-multiplicity-v1.md` SHA-256 `128c8d68c92ef4db22169b0376e7a97758efa4ef18cdb086ecf4914de5482de7`, U cannot have a six-eigenvalue spectrum of the form

`{zeta^(a+5k), zeta^(b+5k): k=0,1,2}`

when the two exponents within each U^5 eigenspace differ by `±3` modulo 15. For example the spectrum `(0,2,5,7,10,12)` is excluded. No assumption is made on the number field or rationality of the v2,v5,v7 populations.

## Proof

Every U^5 eigenspace has dimension 2. The field-free row-imbalance theorem `frontier-20261029-cyclic15-row-imbalance-v1.md` SHA-256 `5fd6191eb69c5720eaf5a272b98693249578a41cab90571ec7b73260e09aef04` applies to each eigenspace. Its two v5 populations sum to 1/3 and lie at distance at least

`delta=(1/3) sqrt((3 sqrt(5)-5)/10) > 1/12`

from 1/6. Hence in each U^5 eigenspace one coordinate has v5 population strictly greater than 1/4.

The three chosen high-population coordinates belong to only two original 3-cosets of eigenvalues. By pigeonhole, two of them lie in the same coset. Their distinct eigenvalue exponents differ by 5 or 10. For such a pair, all three coefficients `|1+zeta^(d Delta)|` for d=2,5,7 have magnitude 1. Row orthogonality, the triangle inequality and Cauchy–Schwarz would therefore give

`sqrt(p5_j p5_k) <= sqrt(p2_j p2_k)+sqrt(p7_j p7_k) <= sqrt((1/2-p5_j)(1/2-p5_k))`.

But both p5 populations are greater than 1/4, so the left side is strictly greater than the right side. Contradiction.

The proof uses the cyclic ONB caller and row-imbalance lemma but no finite-source restriction. The other two-coset class, where the same-U^5 exponents differ by ±6, remains open in this all-field scope. Independent written review and novelty clearance remain required.
