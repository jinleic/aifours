# An open nonaffine CH10 patch: generically 100 rays and no Fourier transversal

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:46:19 PDT 2026**. This concerns a nonempty local patch of one source family, not every point of that family, every even Fourier product, or unrestricted 1RQLS10.

## Statement

Consider the three-parameter nonaffine matrix `Y_10_3_278` of [Bruzda's public source](https://github.com/matrix-toolbox/chm/blob/main/CHM_SINKHORN/Y_10_3_278.m), at unit phases `a=e^(i alpha)`, `b=e^(i beta)`, `c=e^(i gamma)`. There is a connected open neighborhood D of `(alpha,beta,gamma)=(0,2pi/3,0)` such that:

1. Every matrix in D is complex Hadamard and outside both 2×5 and 5×2 Diţă types.
2. Outside a closed nowhere-dense measure-zero subset of D, the cyclic Fourier-product QLS has 100 distinct rays and no orthogonal transversal for EVERY source-row order simultaneously.
3. Outside a further measure-zero subset, K is also non-Butson, since its dephased cross-ratio c is not a root of unity.

This is a genuine nonaffine three-real-parameter local statement, but it does not say the exceptional set is empty. The source calls the ambient family nonaffine; our conclusion relies on its explicit formulas, local Hadamard verification and the named analytic zero-set theorem, not a novelty assertion.

## Exact seed and local unit-modulus domain

Put `P=a+b`, `D0=ab-a-b`, `C0=ab-a²b-ab²`, and

`N=-a+2a²-b+4ab-a²b+2b²-ab²`.

The source's radical u satisfies `D0 u²-N u+C0=0`. At `a=1,b=omega=zeta3`, on the specified radical branch, `u=1`, `q=-1`, `r=omega²`, `s=omega`, `t=omega`; all denominators and radicands used here are nonzero. Exact source substitution and the 90 seed Gram identities are recorded in `frontier-20261028-y10-nonaffine-seed-v1.py` SHA **7438c1258c1b9da11432788bf32d1b1461e342915675f0da2af2a73cbe18238b** and independent seed replay SHA **db16e99a630165cc8dbd3cafa863967b81ecacff1ae98db2512e9bc33e62f2f8**.

For unit a,b, `C0=(ab)^2 conjugate(D0)` and `N/(ab)` is real. Setting `u=ab v` transforms the u quadratic into `D0 v²-[N/(ab)]v+conjugate(D0)=0`. At the seed `D0=-1` and `N/(ab)=1`; hence, strictly in a neighborhood, its roots have unit modulus. Let `p=-|a+b|²` and `r=(p-i sqrt(4-p²))/2`. Near the seed, `-2<p<0`, so |r|=1. Put `W=1-conjugate(u)-conjugate(a)-conjugate(b)`; the u quadratic gives the exact identity `|W|²=2-|a+b|²=|1+r|²`. Thus the source's `q=(1+r)/W` is unit, and its formula for r agrees with this r. If `D_s=1+r-q`, then `q(1+r)-r=q r conjugate(D_s)`, so `s=[q(1+r)-r]/D_s` is unit.

To see t is unit, set `T=u+a+b`. The identities `|T-(a+b)|²=1` and `|1-conjugate(T)|²=2-|a+b|²` imply `(1-conjugate(P))T+(1-P)conjugate(T)=0`. From the source formulas,

`s = r T/[q conjugate(T)]` and `r u+r+s+r s = r [1-P+T/conjugate(T)]`.

The preceding relation gives `|1-P+T/conjugate(T)|²=|P|²`. Therefore `t=-r u P/[b(r u+r+s+r s)]` is unit. All relevant denominators remain nonzero in a sufficiently small open neighborhood of the seed, and the selected branches are real analytic there. c is arbitrary unit throughout this local neighborhood.

## Exact generic-Gram certificate

The entries of the source matrix are monomials in unit `a,b,c,u,q,r,s,t` with signs. `frontier-20261028-y10-nonaffine-symbolic-gram-v1.py` SHA **c1ba1fe0c1a5d38b69879e269afd50fcf6c3fc37eec8f37159cb1d384a98a38a**, result SHA **d7c03aaa61f9946d28cd8eef446d02e8387bf36c96c78b580ab7fe5bd56a2d47**, substitutes the rational q,s,t formulas, clears denominators and exactly reduces the 186 c-Laurent coefficients of all90 row/column Grams modulo the u and r quadratics, with ZERO remainders. A separate power-recurrence reduction `frontier-20261028-y10-nonaffine-symbolic-gram-recurrence-v1.py` SHA **9f280127fcf12d34786fa9a35418d80a274e53586ceff44aa9fd1d7e565266ca**, result SHA **bb7d245d141c35caffa612560552645d2e75ec4227b1e02668f1e3895b47d7d1**, obtains the same 186 zero remainders by a different elimination algorithm. These two scripts share the source expression transcription and rational substitutions, so their agreement is not an independent source transcription. Together with the unit-modulus argument, this verifies Hadamardness on D without importing the source's family claim.

## Non-Diţă and generic maximal no-T conclusions

The seed belongs to BH(10,6), so the m=2,p=5 field obstruction makes it no-T in every source-row order. Its literal sixth-root exponent matrix has exactly TWO 5+5 row-ratio pairs and TWO 5+5 column-ratio pairs, checked by `frontier-20261028-y10-seed-dita-ratios-v1.py` SHA **4808abab0748aec7f7a3dd1c806257f17e6949feeb0a0189f51bb99416a898a1**, result SHA **1d9b573e56895ff2594d8a9c592a11b6a0c133e59fff92194aed3c517e815138**. Each Diţă orientation requires five disjoint such pairs in the corresponding axis. Because there are finitely many candidate pairs/partitions and missing ratio equalities persist locally, shrink D so neither orientation occurs anywhere in D.

The analytic-family theorem `frontier-20261028-analytic-family-generic-no-transversal-v1.md` SHA **ee91ec781300233fdfc1437137b7a3b0af1e5cc9ffe9d16f58a5c2aa4e2086f4** now gives no-T in all source orders off a closed nowhere-dense null set. For distinctness, `frontier-20261028-y10-nonaffine-seed-slice-allphase-no-transversal-v1.md` SHA **a4908c9fa34279a3663b5a03ba2f3b20d26f04781eb658af090aac74d626f700** proves that on `a=1,b=omega`, any nonroot c produces 100 rays for every source order; such c occur arbitrarily near1. For every pair of cells and every source order, the analytic function `1-|<psi_i,psi_j>|²` is therefore nonzero at such a point. Its zero set is null and nowhere dense; the finite union over all pairs/orders establishes generic 100-ray maximality simultaneously. Finally c itself is a dephased cross-ratio, so nonroot c implies non-Butson; root c occupies a countable union of null hypersurfaces in D.

The entire local unit-modulus derivation, polynomial reduction, actual source transcription, field seed, 100-ray slice and analytic zero-set import require independent full review. No conclusion is asserted at exceptional points or for other connected components of the source family.
