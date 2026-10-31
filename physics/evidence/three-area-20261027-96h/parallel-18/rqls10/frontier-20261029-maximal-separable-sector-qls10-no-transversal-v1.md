# An explicit 100-ray, individually separable QLS10 with no transversal

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:06:31 PDT 2026**. This demonstrates that the additive-sector obstruction genuinely applies at maximal ray count. It is NOT a 1-resolvable QLS10 construction.

## Explicit array

Work in `C² tensor C⁵`. Put `zeta=zeta5`, `sigma=(0,1,3,2,4)`, `eta=(3+4i)/5`, and `W=diag(eta,1,1,1,1)`. Define unit vectors

`v_(r,c)(t)=zeta^(r t+c sigma(t))/sqrt(5)`, for `r,c,t in Z5`,

and index rows by `(a,r)` and columns by `(b,c)` with `a,b in Z2`. Set

`psi_((a,r),(b,c)) = |a xor b> tensor W^a v_(r,c)`.

Every row is an ONB: its two b-blocks occupy different C⁵ sectors, and each 5-vector block is an ONB. Every column is an ONB by the same reasoning using the two values of a. The permutation sigma makes each fixed-r and each fixed-c family v orthogonal.

The array has exactly 100 distinct rays. Within the 25 rays v, any coincidence forces `Delta r+Delta c=0` from coordinate1 and `2 Delta r+3 Delta c=0` from coordinate2; hence both differences vanish mod5. All25 rays Wv are also distinct. No Wv ray equals a v ray, since comparing coordinate0 with any unchanged coordinate would force eta to be a fifth root of unity, whereas `eta+conjugate(eta)=6/5` is not an integer. In each sector one of the 5×5 blocks consists of v rays and the other of Wv rays; the two sectors are orthogonal. Thus the four blocks supply 100 distinct rays, and every ray is individually separable across the stated C² tensor C⁵ split.

Nevertheless the array has **NO orthogonal transversal**. Every cell lies in sector `H_(a xor b)`, and each of the two sectors has dimension5. In any transversal ONB, each sector must occur five times, but summing `a xor b` along a transversal gives `5+5=0 mod2`, while five cells in sector1 give `1 mod2`. This is the n=5,G=Z2 case of `frontier-20261029-additive-sector-qls-obstruction-v1.md` SHA **d1916f268d6e8b7de9b497c6aa099bc1b92ef88ca8716ee1583ed6c6544fff15**.

This example also shows that an array of individually separable rays need not be an array-level QLS5 tensor QLS2: any such tensor array has at most50 rays.

## Exact original-vector checks

`frontier-20261029-sector-maximal-example-v1.py` SHA **633a66ad2abe976f363f8108c26466134b9ac72d568ab641aba33a647a2ddd79**, result SHA **28b7871367ad9b0a6e6e0076c747939ed2f8966825bc9296061575d2ff6ae90b**, checks 100 vector norms, 450 row Grams, 450 column Grams and all4950 distinct-ray pairs in exact `Z[zeta5,i]`, scaling each vector uniformly by `5 sqrt(5)`.

An independently implemented original-vector replay `frontier-20261029-sector-maximal-example-replay-v1.py` SHA **638a3814892a26f37878288dd8c4eef2e8e6be59c9cfc9966fd75cb19a03fe80**, result SHA **dbf118148d2cd05b9b73ddd8638517008492b4c21be12aaff2974f10513fe8d8**, uses `Z[zeta20]/(x⁸-x⁶+x⁴-x²+1)` and checks the same 100/450/450/4950 counts. These are exact arithmetic checks and written proofs, not a formal proof, human/cross-model review or novelty clearance. Independent review of the vectors and sector caller is requested; other QLS10s may be 1-resolvable.
