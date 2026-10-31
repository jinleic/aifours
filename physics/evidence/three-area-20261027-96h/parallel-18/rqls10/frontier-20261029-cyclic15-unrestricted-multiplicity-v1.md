# A field-free multiplicity restriction on a cyclic 6D complement

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:27:34 PDT 2026. No rationality or number-field assumption is used. This concerns only **unitary-cyclic-equivariant** 45-distinct-ray representations of `G6=Circ(15;±2,±5,±7)`, not arbitrary G6 representations or 1RQLS10.

## Claim

If such a representation exists and U implements translation by one vertex, then U^5 has all three cube-root eigenvalues, and their multiplicities must be a permutation of **(3,2,1)** or **(2,2,2)**. In particular multiplicities (4,1,1) are impossible.

## Proof

As in `frontier-20261029-cyclic15-rational-spectral-no-go-v1.md` SHA-256 `bb0d0cf314b2c7c94afddb99a3bfdfe44d7f16a28251f197e464215cf9b49ada`, the projector system is irreducible, U^15 is scalar, and after rephasing U^15=I. At vertex 0, write the six normalized ONB rays as `v_d, U^(-d)v_d`, d=2,5,7. Orthogonality of `v5` and `U^(-5)v5` forces its total population in each of the three U^5 eigenspaces to be 1/3, so all three eigenspaces occur.

Suppose two of these eigenspaces are one-dimensional. Let their normalized U eigenvectors be e_j,e_k, with eigenvalues lambda_j,lambda_k. Write `p_dj=|<e_j,v_d>|²`. Singleton status gives `p5_j=p5_k=1/3`. The diagonal ONB identities give

`p2_j+p7_j=p2_k+p7_k=1/6`.

In the inner product of ONB rows j and k, the v5 pair contributes a complex number of magnitude exactly 1/3: the two U^5 eigenvalues are distinct cube roots, and `|1+omega|=|1+omega²|=1`. For d=2,7 the paired-column coefficients have magnitude `|1+(lambda_k/lambda_j)^d|<2`, since lambda_k/lambda_j is a nontrivial 15th root and both 2 and 7 are coprime to 15. Cauchy–Schwarz bounds the sum of the magnitudes of these two contributions by **strictly less than**

`2 [sqrt(p2_j p2_k)+sqrt(p7_j p7_k)] <= 2 sqrt((1/6)(1/6)) = 1/3`.

They cannot cancel the v5 contribution, contradicting orthogonality of the two rows. The only partitions of 6 into three positive multiplicities that do not have two singleton parts are (3,2,1) and (2,2,2).

## Scope

This allows arbitrary complex phases, irrational or transcendental populations, and any spectral number field, but it still requires the full cyclic unitary action and distinct rays. It does not address cyclic actions with the surviving multiplicities, symmetry-breaking realizations or the other 25 QLS cells. The irreducibility caller and row-orthogonality argument need independent written review; no external, formal-kernel or novelty claim is made.
