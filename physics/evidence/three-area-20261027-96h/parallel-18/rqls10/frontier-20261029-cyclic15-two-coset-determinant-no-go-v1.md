# A determinant obstruction excludes every two-coset cyclic spectrum

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:45:51 PDT 2026. This strengthens `frontier-20261029-cyclic15-short-two-coset-no-go-v1.md` SHA-256 `29aa9aa0930a2ca393ed34ad823388bc0a72cf562cd7616795a02468293cc3bb`: **both** short and long two-coset spectra fail, with no rationality, field or phase restriction. Other cyclic spectra and symmetry-breaking G6 lifts remain open.

## Standalone linear-algebra theorem

Let `omega=exp(2 pi i/3)` and let U be any unitary on C6 whose eigenvalues, with multiplicity, can be arranged as

`alpha, alpha omega, alpha omega², beta, beta omega, beta omega²`,

where `|alpha|=|beta|=1`; the two cosets may even coincide. Then there do not exist vectors v2,v5,v7 such that

`v2, U^(-2)v2, v5, U^(-5)v5, v7, U^(-7)v7`

form an ONB. The theorem requires neither U^15=I nor a graph or number-field hypothesis.

## Proof by 3×3 determinants

In an eigenbasis ordered by the two displayed triples, write `x^h_(k,d)=<e_(h,k),v_d>` for h=A,B, k=0,1,2 and d=2,5,7. Put `rho=beta/alpha` and form 3×3 matrices

`Y_h[k,:] = sqrt(2) (x^h_(k,2), x^h_(k,5), omega^(-k)x^h_(k,7))`.

The six basis columns form a unitary matrix, so every row has norm 1. Within one spectral triple and for k≠l, its row inner product is

`sum_d x^h_(k,d) conjugate(x^h_(l,d)) [1+omega^(-d(k-l))]`.

Since 2,5≡2 and 7≡1 modulo 3, and for nonzero delta modulo 3, `1+omega^delta=-omega^(2 delta)` and `1+omega^(-delta)=-omega^delta`, this inner product is a nonzero scalar times the corresponding row inner product of Y_h. The diagonal row norms are also 1. Therefore **both Y_A and Y_B are unitary**, without any flat-amplitude assumption.

Let `Omega=diag(1,omega,omega²)`, `D1=diag(1,1,rho^7)` and `D2=diag(rho²,rho^5,1)`. Cross-orthogonality of the two spectral triples gives the matrix identity

`Y_A D1 Y_B† + Omega Y_A D2 Y_B† Omega† = 0`.

Indeed, with delta=k−l, the coefficients for d=2,5 are `1+rho^d omega^delta`; for d=7 the phase in Y makes the coefficient `rho^7+omega^delta`.

Both 3×3 summands are invertible, and their determinants are **equal**:

`det(Y_A D1 Y_B†) = det(Y_A) det(Y_B†) rho^7`

and the second determinant has the same value, since `det(D2)=rho^(2+5)=rho^7` and conjugation by Omega does not change determinant. But the displayed matrix identity makes one 3×3 summand the negative of the other, which would make their determinants **opposite**. A nonzero complex number cannot equal its negative. Contradiction.

## Consequences and boundary

In particular a cyclic lift of `Circ(15;±2,±5,±7)` cannot have any spectrum consisting of two complete 3-cosets of 15th roots, including the previously open ±6 class. The last two spectral classes in the exact Q(sqrt(5)) census `frontier-20261029-cyclic15-qroot5-spectral-no-go-v1.md` SHA-256 `c1fbebf579b539548557d9b57e270bdc985775dc72b58876c9bc736962ef523b` can be excluded directly by this determinant argument rather than by the earlier flat-Hadamard classification.

This theorem allows arbitrary phases and spectral populations, and does not rely on the triangle-span or resultant certificates. It still assumes the two-coset spectrum and does not exclude other spectra, noncyclic lifts, or general QLS10. The row-phase identity and determinant caller require independent written review; no external, formal-kernel or novelty claim is made.
