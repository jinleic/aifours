# Odd-cycle obstruction for character-related Schmidt vectors

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` before writing: **Wed Oct 28 18:57:07 PDT 2026**. This rules out a concrete branch of the EXACT five-dimensional system in `frontier-20261028-mub-triple-rank2-reduction-v1.md` SHA **ef00b5db269a3e436365b4b98fd486c32836bbda931f00bba80afcaaea5dfc8c**; it does not prove that system or general 1-RQLS10 impossible.

## 1. General odd-order theorem

Let m>=3 be odd, `omega=exp(2*pi*i/m)`, U the normalized m-dimensional Fourier matrix, and V=D U for an arbitrary diagonal unitary D. On `C2 tensor Cm`, take three product bases: the qubit Z basis times I, the qubit X basis times U, and the qubit Y basis times V.

**Claim:** no vector unbiased to all three bases can have the form

`phi=(|0> tensor a + |1> tensor b)/sqrt(2)`,
`b_t=lambda omega^(k t) a_t` for a phase lambda and a nonzero k mod m.

The theorem allows ANY odd composite m, ANY a and ANY diagonal D. It does not assert that these three product bases are always pairwise mutually unbiased; for the previously specified m=5 chirp they are.

## 2. Proof by two incompatible odd-cycle products

Unbiasedness to the Z product basis makes `|a_t|=|b_t|=1/sqrt(m)`. Define `u=U†a`, `v=U†b`, `u'=V†a`, `v'=V†b`. Multiplication by the character `omega^(k t)` shifts Fourier indices; because D is diagonal and commutes with the character modulation, the SAME nonzero shift d satisfies

`v_j=lambda u_(j-d)`, `v'_j=lambda u'_(j-d)`.

The shift permutation breaks F_m into cycles of length `ell=m/gcd(m,d)`, which is ODD. Unbiasedness to the X product basis gives for every j

`|u_j|²+|v_j|²=2/m`, `Re(conjugate(u_j)v_j)=0`.              (1)

Using |lambda|=1, the first equation around an odd cycle forces EVERY `|u_j|²=1/m`: subtract1/m, then adjacent values change sign, and after an odd number of steps equal their own negatives. Similarly, Y-basis unbiasedness gives

`|u'_j|²+|v'_j|²=2/m`, `Im(conjugate(u'_j)v'_j)=0`,         (2)

and forces each `|u'_j|²=1/m`.

All these coordinates are nonzero. By (1), each phase

`lambda conjugate(u_j) u_(j-d)/(|u_j| |u_(j-d)|)`

is either +i or -i. Their product around a whole cycle is `lambda^ell`, because all u phases telescope. Since ell is odd, `lambda^ell` must be +i or -i. By (2), the analogous phase with u' is either +1 or -1; its cycle product is the SAME `lambda^ell`, now required to be +1 or -1. Contradiction.

No assumption about the phases of a or about a spectral classification enters. The k=0 case would make b proportional to a and is incompatible with the orthogonality forced by the three qubit marginals.

## 3. Consequences at m=3 and m=5

At m=3, common unbiasedness forces `<a,b>=0`, so the three unit numbers `b_t/a_t` sum to zero. Three unit numbers summing to zero form a rotated equilateral triple. EVERY permutation of the three cube roots is affine in t, and the ratio is therefore lambda times a nontrivial character. §2 excludes it. This proves directly that this particular Weyl MUB triple in dimension6 has no common unbiased vector; no claim is made here about other triples or all dimension6 MUBs.

At m=5, suppose additionally the five ratios `b_t/a_t` lie in a single coset of the fifth roots. Their sum is zero by `<a,b>=0`, so the Phi5 relation forces each fifth root to appear exactly once. Thus the ratios are `lambda omega^(sigma(t))` for a permutation sigma. The affine sigma cases are precisely characters and are excluded by §2. There are20 affine and100 non-affine permutations; the latter remain UNRESOLVED. `frontier-20261028-character-ratio-census-v1.py` SHA **e527f8d64176e8603e658ae34e83a43caeabac1b0be8e3dc017681611af31e2c** exhaustively checks these elementary counts, including that all6 permutations for m3 are affine. Continuous non-fifth-root ratios are also untouched.

## 4. Parallel original-vector cyclic-incidence attempt

Separately, `frontier-20261028-cyclic-incidence-search-v1.py` SHA **0d840e3382a6b1121e4cb93523a5488e70e3e7487045a0c479f7797454c0b520** optimized all30 original ONB constraints on the SAME actual complex vectors with a fixed cyclic Latin resolution L and NO uniform-overlap premise. The first row was gauged to I; its required row/column/transversal orthogonalities exactly force two zeros per other vector, which the search imposed. During50 seconds it completed27 restarts plus part of a 28th. The best saved numerical result JSON SHA **cdcc69ee010044ff51030fe9cf2eebcaaa23cd985bfd5db2c0cd8841530d5f07** had worst block-Gram error about **0.3426** and max distinct overlap about **0.9579**. Many runs drifted near parallel vectors or had large constraint errors. No target candidate was found; this is a bounded float exploration, NOT a no-go for the cyclic L or arbitrary L.

## 5. Exact remaining gap

To finish the restricted Weyl/MUB branch, either solve the full coupled 5D equations or exclude the100 non-affine fifth-root permutations AND arbitrary continuous relative phases by a valid all-variable argument. An exact solution would produce an original 100-ray 1-RQLS via the prior caller. Other transversals, noncirculant/nonproduct arrays and general QLS10 remain outside this theorem.
