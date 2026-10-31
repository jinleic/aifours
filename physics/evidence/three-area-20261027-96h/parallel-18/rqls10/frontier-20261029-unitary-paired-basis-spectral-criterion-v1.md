# A sharp spectral criterion for a uniformly shifted paired ONB

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:50:08 PDT 2026. This is an elementary all-variable classification of a particular paired-source ansatz; it does **not** settle arbitrary Fourier-product transversals or QLS10.

## Exact criterion

For any unitary A on C^(2m), there is an ONB of the form

`v1,A v1, v2,A v2, …, vm,A vm`

if and only if the spectrum of A, counted with multiplicities, is invariant under `lambda -> -lambda`. The same criterion applies when each pair is allowed to use either A or A^(-1): reverse the order of an A^(-1)-pair to orient every pair consistently.

**Necessity.** Let W be the m-dimensional span of the first vector of each pair. Then A maps W isometrically onto W-perpendicular. In the decomposition `W ⊕ W-perpendicular`, unitarity forces A to have block form `[[0,C],[B,0]]` with B,C unitary: the lower-right block vanishes from the off-diagonal unitarity equation. Conjugation by `diag(I,-I)` sends A to −A, so their spectra agree.

**Sufficiency.** Pair an orthonormal eigenbasis of each eigenvalue lambda with one for −lambda. For each eigenvector pair `(e+,e-)`, take `v=(e++e-)/sqrt(2)`; then `A v=lambda(e+-e-)/sqrt(2)`. The resulting pairs form an ONB.

## Sharp ordinary-Fourier corollary

Let `D=diag(zeta_n^j)_(j=0..n-1)` for even n, and put `q=n/gcd(n,d)`. An ONB whose vectors pair by D^d or D^(-d) exists **if and only if q is even**. For q odd, D^d has only odd-order eigenvalues and cannot have a negation-invariant spectrum. For q even, the ordinary Fourier basis itself gives a **flat** example: D^d permutes its columns in even q-cycles, and consecutive vertices of each cycle can be paired.

At n=10, even shifts d have odd q (5, or 1 for d=0) and are impossible; odd shifts have even q and the flat Fourier-basis pairing exists. The positive example is a source ONB, not a transversal or maximal 1RQLS10.

The more general odd-coset determinant theorem `frontier-20261029-odd-coset-paired-basis-obstruction-v1.md` SHA-256 `ccab99a88d0b734ad2cb5a7b27e408e57cba4a33cef4b5bec31acab06fb2e0d5` also treats certain **unequal** shifts not reducible to one common ±d. Both results need independent review and make no novelty or formal-kernel claim.
