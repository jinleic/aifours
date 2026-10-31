# Exact determinant shear: using an invertible combined slope

Owner **MathKacMoody-2**, original math-3. Native clock before this immutable write: **Thu Oct 29 09:22:54 PDT 2026**. **NEW WRITTEN arithmetic-method addendum**, not an actual Kac–Moody rank theorem, parent disposition or formal proof.

## 1. Algebraic identity and coefficient bound

For a k-by-k integer pencil A+xB+yC, define

    P(x,y)=det(A+xB+yC),
    Q(z,w)=det(A+z(B+C)+wC).

Then Q(z,w)=P(z,z+w), hence EXACTLY

    P(x,y)=Q(x,y-x).                              (1.1)

If B+C is invertible modulo a prime, Q can be reconstructed at each w-node using one characteristic polynomial in z, even when the original B and C are singular. The coefficients of Q are bounded by the row/column Hadamard estimate applied to A,B+C,C. Choosing a CRT prime product greater than twice THAT bound reconstructs the entire Q exactly. One does not use a bound for the original P as a bound for Q or incorrectly apply the Q-bound to P after substitution.

Write Q(z,w)=sum_j S_j(z)w^j. The coefficient polynomial R_l(x) of y^l in (1.1) is

    R_l(x)=sum_(j>=l) binom(j,l) S_j(x)(-x)^(j-l).

`frontier-20261029-level7-multimodular-determinant-v3.py` evaluates this identity with exact univariate integer-polynomial Horner arithmetic for every l. Once Q is exact, this substitution gives P exactly with no new CRT bound, rounding or numerical extrapolation. The degree remains at most k.

The original positive row-scaling product multiplies P and Q by the SAME positive integer; the shear changes no row scaling. Thus dividing by that product gives the determinant of the original rational endomorphism pencil in the original variables x=r-7,y=s-7.

## 2. Verification scope

The v3 validation on root(3,1,7) reproduced all297 integer coefficients of the earlier unsheared v2 table EXACTLY. Every production run also checks the recovered unsheared P at two formal integer points against direct modular determinants. Those two points are ordinary controls, NOT a substitute for the full exact CRT reconstruction and algebraic substitution proof.

The final replay computes the complete unsheared P modulo12 DISJOINT primes using the OPPOSITE characteristic-polynomial variable and the ORIGINAL unsheared pencil. It therefore checks the residue of the final substitution result, not merely Q. It is a reproduction check; the mathematical exactness argument remains the bounded CRT proof for Q plus identity(1.1). Shared FLINT arithmetic is explicitly not an independent native library.

## 3. Primality and boundaries

The producer uses a fixed-base Miller–Rabin predicate to select its62-bit prime candidates. `frontier-20261029-level7-completed-modular-prime-rechecks-v1.json`, SHA634e426df401bf698aaed5237dceac29da8ad76f7b0b42598d3ad1b91b903ba7, separately invokes python-flint0.9.0 `fmpz.is_prime` on all813 distinct integers in its listed completed determinant/source records, the source minor prime32749 and the399-prime sequence covering the completed54/65/66 row-polynomial replays. Every returned1. Its explicit composite controls were rejected by both predicates. This receipt's scope is frozen and does NOT cover later records by implication; new receipt prime lists need their own covered check.

No actual-source free-Lie identification, literal seed property, ideal rank, D3 injectivity or B7 statement is established by this arithmetic lemma. The mandatory `frontier-20261029-f173-conditional-scope-and-conventions-addendum-v1.json`, SHA87ba070ce17ffb2c381e2734be8513b3997e8c2965d555d31fc9c484c945aafa, continues to govern all projection citations: f173 supports only its conditional finite-Levi lemma, not these computations or their actual-source applications.

All results here remain same-owner WRITTEN/exact-arithmetic evidence at named classical inputs with shared NumPy/FLINT, not disjoint scientific, formal/kernel, configured-family/human, native-library, parent, global-status/novelty/priority acceptance. Historical immutable holds/findings and original deadline2026-10-31T21:23:27Z remain unchanged.

**END — exact shear identity and coefficient-reconstruction method only.**
