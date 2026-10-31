# Exact methods for the large level-seven lowest types

Owner **MathKacMoody-2**, original math-3. Actual native `/bin/date` observed before this immutable write: **Thu Oct 29 06:16:27 PDT 2026**. **NEW WRITTEN METHOD LEMMAS supporting exact computations; independent mathematical/code review and parent disposition PENDING.** This document proves why the new programs certify what they claim. It proves no Kac–Moody theorem by itself.

## 1. Complete free lowest sources from a modular kernel

Fix a root(a,b,7) of the free Lie algebra L(M) on the actual level-one adjoint module M, with the ordered letters u0,...,u7 of root degrees(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2). Let Lyn be the Lyndon words of that root and P_w the standard bracketing of w in the tensor algebra. Classical Lyndon theory (named import) gives: {P_w} is a basis of L_(a,b,7)(M), and P_w=w+(strictly larger words).

**Lemma 1.1 (row restriction).** For any root, the linear map from Lie elements to their coefficients at Lyndon words is injective. Indeed for X=sum c_u P_u, the coefficient of a Lyndon word v is c_v plus a combination of c_u with u<v. This matrix is unitriangular.

Therefore x=sum c_w P_w satisfies f1x=f2x=0 iff the coefficients of f1x and f2x at all target Lyndon words vanish: the f_i are derivations preserving the free Lie subalgebra, so f_ix is again a Lie element. `frontier-20261029-level7-modular-lowest-source.py` builds exactly these rows for EVERY source Lyndon word.

**Lemma 1.2 (exact lift certificate).** Suppose integer vectors c^(1),...,c^(k) satisfy: (i) each tensor vector x_i=sum c^(i)_w P_w is killed by f1 and f2, checked in exact integer tensor coordinates; (ii) the c^(i) restricted to k pivot Lyndon coordinates form a nonzero diagonal matrix; (iii) k equals the exact Witt/Weyl lowest multiplicity of the root. Then {x_i} is a basis of the ENTIRE free lowest space.

Proof: (ii) gives independence; (i) gives membership; finite-sl3 complete reducibility and the character identify the lowest-space dimension with k. A modular computation is used only to PROPOSE the vectors; rational reconstruction errors cannot pass (i)–(iii). If (i) fails, more primes are used. No prime-dependence remains in the certified statement.

## 2. Canonical pencils and digit splitting

The general generator applies the same canonical contraction formula as the earlier invariant generator, with roots(n,n) replaced by(a,b): mixed-Cartan RIGHT transport of F3, eight theta-negative words, finite-Levi trace-pair inverse Gram and outer brackets with the eight level-one letters. Every source and output is checked f1/f2-lowest, every right degree-zero tail must cancel, and the image of EVERY source vector is reconstructed in EVERY tensor-word coordinate by arbitrary-integer matrix identities.

**Lemma 2.1 (digit splitting).** Write each source vector v=sum_t d_t R^t with signed digits |d_t|<=R/2. All operators are linear. If every int64 operation on each digit satisfies its asserted bound, then sum_t T(d_t)R^t=T(v) exactly. The v2 programs perform every zero test and every reconstruction on these recombined arbitrary integers, never on an individual digit alone.

The LEFT replay uses the different literal transport of the pinned left core: local brackets are moved to PREFIXES using u g=g u-[g,u], local F3 data are derived from cyclic positive words, and negative words are applied directly. It uses a different digit radix in v2. It also checks Lie membership of every source vector by the Dynkin–Specht–Wever criterion theta(v)=7v for the left-normed bracketing map theta in degree7 (a named classical import).

## 3. Exact bivariate determinants

Let A,B,C be integer matrices after positive row scalings L_i, so Z(x,y)=prod_i L_i det(A_0+xB_0+yC_0) is the scaled canonical determinant.

**Lemma 3.1 (coefficient bound).** Every coefficient of det(A+xB+yC) has absolute value at most min(prod_rows,prod_columns), where prod_rows=prod_i(||a_i||+||b_i||+||c_i||) over rows and prod_columns is the analogous column product. Proof: multilinearity expands the determinant into determinants whose rows (or columns) are chosen from a_i,b_i,c_i; each monomial coefficient is a sum of such determinants; Hadamard's inequality bounds each, and the sum over choices is at most the displayed product.

**Lemma 3.2 (one characteristic polynomial per node).** If B is invertible modulo p, then modulo p

    det(A+xB+yC)=det(B) charpoly(-(B^-1A+yB^-1C))(x).

Otherwise, for each node y with M=A+yC invertible,

    det(M+xB)=det(M) sum_i (-1)^i e_(m-i) x^i,  e=charpoly(M^-1B).

Both are exact polynomial identities over F_p. For m+1 distinct nodes, a Vandermonde inverse gives every coefficient of Z modulo p; entries of total degree>m are checked zero.

**Lemma 3.3 (exact reconstruction).** If the prime product exceeds twice the Lemma3.1 bound, symmetric CRT reconstructs every integer coefficient exactly. The v2 program chooses primes BEFORE reconstruction from that bound. The separate replay computes complete residue tables modulo12 DISJOINT primes with the OPPOSITE charpoly variable and requires that the pinned exact table reduce to them. This is a reproduction check; the proof is Lemma3.3.

The method was validated on the earlier root(3,3,7) determinant: it reproduced ALL36304 coefficients obtained by full grid interpolation, and a pencil computed in a DIFFERENT source basis by the new generator gave the identical determinant, as it must because the determinant of an endomorphism is basis-independent.

## 4. Actual-parameter certificates for tensor sources

The tensor-source producer/replay implement the same mathematics as the earlier small-type certificates: the least uniform bound b0 where the translated free determinant has a nonzero constant and only positive coefficients; ALL fixed-lowest-seed nested descendants below b0, projected by the compact finite-Levi Gram to the ENTIRE one-seed lowest ideal; whole one-seed quotient row pencils with nonnegative univariate determinant certificates; and all remaining two-seed corners computed on the ENTIRE actual quotient. The mathematical inputs are `frontier-20261029-whole-seed-ideal-lowest-projection-v1.md`, `frontier-20261029-quotient-stable-contraction-descent-v1.md` and Sections3–4 of `frontier-20261029-level7-33-all-parameters-candidate-v1.md`.

Row polynomials are produced exactly by an exact rational characteristic polynomial and checked at two exact rational determinants; the replay verifies the complete univariate identity modulo enough primes to exceed twice a row-Hadamard bound for the scaled polynomial. Large matrices are recorded by SHA-256 of canonical exact serializations and recomputed by different algorithms. The v2 programs recombine base-2^30 (producer) and base-2^26 (replay) digits exactly in seed cross products.

The tensor pipeline was cross-validated on type(3,1,7): its free polynomial, ideal ranks, row polynomials and corner determinants agree EXACTLY with the earlier Lyndon-source pipeline.

## 5. Assurance

All arithmetic is exact; floating point is used nowhere. Shared NumPy/FLINT libraries and same-owner implementations are trust boundaries, not independent-library or formal verification. These lemmas certify computations relative to the named classical inputs; actual Kac–Moody consequences additionally require the actual-source/PBW, projection and descent lemmas and independent scientific review. No parent, formal/kernel, configured-family/human, B7, novelty or priority acceptance is claimed. Original deadline2026-10-31T21:23:27Z is unchanged.

**END — exact method lemmas for complete large-type sources, pencils, determinants and actual certificates.**
