# An exact irrational-population control for the cyclic-15 obstruction

**WRITTEN + EXACT-RATIONAL-INTERVAL-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:14:44 PDT 2026. This is a positive solution of a **necessary linear population relaxation**, not a set of orthogonal vectors or a 6D lift.

## Exact control

Take the six spectral exponents `a_j=j`, j=0,…,5, so the eigenvalues would be `zeta_15^j`. Put

`A=(1+sqrt(5))/4`,

`h=cos(2 pi/15)=(1+sqrt(5)+sqrt(30-6sqrt(5)))/8`,

`t=cos(7 pi/15)=(sqrt(30-6sqrt(5))-1-sqrt(5))/8`,

`B=1/2+h`, `C=1/2-t`, and define

`b=1/9`, `e=2/9`, `c=(1/4-A b)/B`, `a=1/2-b-c`,

`f=(1/4-A e)/C`, `d=1/2-e-f`.

Set the population rows

`p2=(a,b,c,c,b,a)`, `p7=(d,e,f,f,e,d)`,

`p5_j=1/2-p2_j-p7_j`.

All 18 entries are strictly positive, and each of the three rows sums to 1. They satisfy

`sum_j p2_j zeta_15^(-2j)=0`, `sum_j p7_j zeta_15^(-7j)=0`,

and the p5 population in each residue class of j modulo 3 is exactly 1/3. They therefore satisfy the normalization, per-coordinate ONB diagonal, and three paired-ray moment constraints used in the rational-spectral obstruction.

## Written check and exact positivity

By pair symmetry about j=5/2, the two complex moment sums reduce to real cosine sums. For p2 the relevant cosine coefficients for the three pairs are `-1/2`, `cos(2 pi/5)`, and h; for p7 they are `1/2`, `-cos(2 pi/5)`, and t. Since `A=1/2+cos(2 pi/5)`, the definitions give `A b+B c=1/4` and `A e+C f=1/4`, which make the two moments zero. Also `b+e=1/3`, and p2,p7 each sum to 1; hence p5 has total 1/3 in every residue class modulo 3.

`frontier-20261029-cyclic15-population-control-v1.py` SHA-256 `cf9ae2a079947facf22771ec063e91e804be453cc08f448e4d61ddc444859ea8` uses only rational interval arithmetic to bound the two radicals and certify every entry strictly between 0 and 1/2. Its output `frontier-20261029-cyclic15-population-control-v1.json` SHA-256 `bd02de09a61a5639b13cd3a7962090161bf6965b78013155bc8bc9453f3dd157` is **PASS** at 02:14:44 PDT. The moment identities themselves are the written symbolic calculation above.

At least one p2 entry must be irrational: all six are positive, but the support `{0,1,2,3,4,5}` contains no complete 3-cycle or 5-cycle of 15th roots. The nonnegative rational cyclotomic-support lemma in `frontier-20261029-cyclic15-rational-spectral-no-go-v1.md` SHA-256 `bb0d0cf314b2c7c94afddb99a3bfdfe44d7f16a28251f197e464215cf9b49ada` would otherwise forbid its vanishing sum. The displayed values lie in the real cyclotomic field and are outside the disjoint-field hypothesis, as they must be.

## Interpretation

This provides an exact counterexample to extending the rational support argument using only positivity and those diagonal/moment constraints: a non-two-coset spectrum can satisfy them with irrational populations. It does **not** satisfy or claim the additional cross-column phase, Gram, distinct-ray, cyclic-realization or QLS conditions. Independent written review of the trigonometric identities and interval caller is required; no formal or novelty claim is made.
