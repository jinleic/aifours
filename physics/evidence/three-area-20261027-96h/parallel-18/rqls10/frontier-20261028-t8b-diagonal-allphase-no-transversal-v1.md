# A non-affine order-eight one-parameter slice has no Fourier transversal

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent replay pin: **Wed Oct 28 22:50:51 PDT 2026**. This closes an entire continuous slice of the non-affine T8B family; it does NOT settle the whole three-parameter family or universal even order.

## 1. Claim

For EVERY unit complex z, let `a=b=c=z` in [Valtonen's T8B family, Proposition3.2](https://arxiv.org/html/2505.22947v1), and set

`d(z)=(1+3z²)/(3z+z³)`.

Both numerator N=1+3z² and denominator D=z(3+z²) are nonzero on the unit circle, and `|d|=1` there. For this source Hadamard, the ordinary Fourier-product QLS8 has **NO orthogonal transversal**, for any source-row order, arbitrary row/column phases and column permutation, regardless of repeated rays. The source proposition's exact Hadamard assertion is named; no root-of-unity assumption is imposed on z or d.

## 2. Finite polynomial reduction

Take a hypothetical transversal. Cyclically rotate physical coordinates so source row0 is coordinate0; shift physical row labels so its column0 cell is at row0. The source matrix is dephased. Row1 must use some column `c∈{1,...,7}` and row7 some distinct `d∈{1,...,7}`. There are `7!*7*6=211680` normalized `(source order,c,d)` choices. The three corresponding actual inner products

`<psi_(0,0),psi_(1,c)>`, `<psi_(0,0),psi_(7,d)>`, `<psi_(1,c),psi_(7,d)>`

must all vanish. Each source entry is a signed monomial in z and d(z), and each conjugate is its inverse on the unit circle. Multiplying each Gram sum by the common nonzero `z³ N D` gives a polynomial over Z[zeta8] of degree at most12; exact coefficient census `frontier-20261028-t8b-diagonal-root-superset-v1.py` SHA **17e28e2f6c8d437f2d6b420e3bec07422a65ec6f225bb2b6f8ae233b36be098a**, result SHA **aea003a22c30fd6c9cf186c44f64cf476667b55330a9b4f0f1ddc70b0e273000**, checks every source order and seven adjacent columns: NONE of35280 adjacent polynomials is identically zero; after removing nonzero z powers and scalar units there are3110 distinct sextics, with summed degrees18660. Thus any actual T parameter is algebraic over Q(zeta8), of degree at most6 there and at most24 over Q. This finite-degree bound is a separate exact consequence, not a numerical observation.

For the no-T proof, exact polynomial division additionally removes ONLY powers of z, `N=1+3z²`, and `D/z=3+z²`, none of which vanish on the unit circle. No roots on the unit circle are discarded.

## 3. Complete exact two/three-cell gate

`frontier-20261028-t8b-diagonal-exact-gcd-v1.py` SHA **04e7b72943e265bc1b9a6d565eaeadb2284b5ccec6f71414e2ea552fcaa737ef**, result SHA **c53bb222a4148fa59381e06379305a0e63cc9f0634912a2507d6b75537e6b2b9**, checks all211680 choices after exact saturation:

```text
205824: first two Gram polynomials coprime modulo 65521;
  5664: their EXACT gcd has roots only in mu8;
   144: third Gram polynomial makes the modular gcd 1;
    48: the EXACT three-polynomial gcd has roots only in mu8;
     0: unresolved.
```

The algebraic-integer embedding maps zeta8 to a primitive eighth root in F_65521. A mod-p coprime gate is used only when the exact leading coefficients remain nonzero modulo p; a hypothetical common algebraic root is integral at the chosen prime and would reduce to a common finite root. If reduction is unsuitable, the program computes the exact Euclidean gcd over Q(zeta8). The exact root-only branch requires explicit checking of all mu8 values, not an inference from modular roots.

`frontier-20261028-t8b-diagonal-exact-gcd-replay-v1.py` SHA **325148218c764a8f21cbebf134f1dc9ce62a11de7dc2271014825b93074f9921**, result SHA **c8f92afe1a7b3443ca716652822b287073629d7cac7558b2a87f0021b6d263e9**, independently rebuilds and saturates all polynomials in the distinct basis `1,i,sqrt2,i sqrt2`, uses prime97/root64 for modular gates and exact Q(i,sqrt2) gcd otherwise, and obtains the same final coverage: 205824 pair-coprime (204300 modular +1524 exact),5664 pair-root8,144 triple-coprime,48 triple-root8, zero unresolved. The two reductions share the source formula and overall mathematical caller.

## 4. Explicit root caller and boundary

For z∈mu8, the 3-parameter grid packet `frontier-20261028-t8b-eighth-phase-grid-no-transversal-v1.md` SHA **1e81c9494b26c6b186b58b13d733a90983ab6dd063b05aed0c86e75eef0cafda** explicitly checks ALL physical source orders for all470 defined `(a,b,c)∈mu8³` points using two full exact arithmetic searches; all eight diagonal triples are defined because D=z(3+z²)≠0 on the unit circle. It is a full reexecution, not a retained per-order proof certificate. Thus every possible root-only branch is actually excluded.

The independent desk replay, source formula, common-factor saturation, modular leading-coefficient argument, degree-six normalization and finite-grid caller all need separate full mathematical/code review. This result covers only T8B(z,z,z), not other dependent triples, other non-affine families, arbitrary order8 K, a general even-order no-go or the original 1-RQLS10 problem.
