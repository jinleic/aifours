# An odd-coset determinant obstruction in every even dimension 2m

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:48:30 PDT 2026. This generalizes the C6 result `frontier-20261029-cyclic15-two-coset-determinant-no-go-v1.md` SHA-256 `b03725b2d3e562ebe70fd2e3e40ef71e167a960a5a3ba866c462ca1bf6fa8463`. It excludes a **paired-basis ansatz**, not arbitrary even-order Fourier-product transversals or arbitrary QLSs.

## Theorem

Let m be odd, `omega=exp(2 pi i/m)`, and U a unitary on C^(2m) whose eigenvalues, with multiplicity, consist of two complete m-root cosets

`alpha omega^k` and `beta omega^k`, k=0,…,m−1, with `|alpha|=|beta|=1`.

Let integer shifts `d1,…,dm` be partitioned into P and M such that for some r

`d_i ≡ r (mod m)` for i in P, and `d_i ≡ -r (mod m)` for i in M.

If, with `rho=beta/alpha`,

`rho^(sum_(i in P) d_i) = rho^(sum_(i in M) d_i)`,

then there is **no** ONB of the form

`v1,U^(-d1)v1, v2,U^(-d2)v2, …, vm,U^(-dm)vm`.

No restriction is imposed on the vector entries or phases; the two spectral cosets may coincide. In particular the phase condition holds for arbitrary alpha,beta whenever the two integer shift sums are equal.

## Proof

Order an eigenbasis into the two m-element cosets. Let `x^h_(k,i)` be the coordinate of v_i in coset h=A,B and row k. Define

`Y_h[k,i]=sqrt(2) x^h_(k,i)` for i in P,

`Y_h[k,i]=sqrt(2) omega^(r k) x^h_(k,i)` for i in M.

The 2m displayed basis columns form a unitary matrix. Their row diagonal identities give row norm 1 for Y_h. For k≠l, put delta=k−l. The contributions for i∈P have common factor `1+omega^(-r delta)`; those for i∈M have factor `1+omega^(r delta)`, which becomes the same factor after the indicated change of column phase. Since m is odd, `-1` is not an m-th root of unity, so the common factor never vanishes. Thus the rows of each Y_h are orthonormal: **Y_A and Y_B are unitary**.

Let `Omega=diag(omega^(-r k))_(k=0..m-1)`, and let diagonal m×m matrices D1,D2 have entries

`D1_i=1, D2_i=rho^(d_i)` for i∈P;

`D1_i=rho^(d_i), D2_i=1` for i∈M.

Cross-orthogonality of the A and B rows is exactly

`Y_A D1 Y_B† + Omega Y_A D2 Y_B† Omega† = 0`.

The two summands are invertible, and the assumed phase condition gives them the same determinant. Yet one is the negative of the other, and m is odd, so their determinants must be opposite. Contradiction.

## A direct Fourier-operator consequence

For any odd m, the ordinary cyclic Fourier diagonal `U=diag(zeta_(2m)^j)_(j=0..2m-1)` has the required two m-root cosets with `rho=zeta_(2m)`. Thus the theorem excludes any paired ONB whose shifts occupy two opposite residue classes modulo m and whose P/M shift-sum difference is divisible by 2m.

For example, in dimension 10 take P shifts `(1,1,6)` and M shifts `(4,4)`: the sums are both 8 and the residues are ±1 modulo 5, so no such paired ONB exists for the ordinary 10-point Fourier diagonal. This is a real all-complex-phase restriction on a proposed Fourier-product source basis, but an arbitrary Fourier-product transversal need not produce such a pairing. No universal even-order transversal claim follows.

The row-phase identities and determinant argument require independent written review; no formal-kernel verification, external review or novelty claim is asserted.
