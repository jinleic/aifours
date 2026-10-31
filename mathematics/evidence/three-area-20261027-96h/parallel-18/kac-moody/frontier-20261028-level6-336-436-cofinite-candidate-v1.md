# Level six: cofinite injectivity for the (3,3), (4,3) and (3,4) primitive types

Owner MathKacMoody-2, original math-3. Actual `/bin/date` returned before this new write: **Wed Oct 28 22:05:01 PDT 2026**. **WRITTEN plus exact-integer certificate, UNREVIEWED.** No parent adoption, independent-model/human/formal verification, novelty or priority claim.

## 1. Exact statement and source cut

For integers r,s>=6 and every allowed full complex Cartan realization C of the original A(r,s), put S=G_C/J and P_(a,b,6)=ker f1 intersect ker f2 in the ACTUAL degree (a,b,6). At the same full-Cartan/free-Levi and lowering interfaces named in `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` (Sections 0–4), and at the two stored actual-minor inputs pinned below:

- The ENTIRE D3 map on P_(3,3,6) is injective except possibly at **7998** pairs (r,s) in the integer quadrant r,s>=6.
- The ENTIRE D3 map on P_(4,3,6) is injective except possibly at **6480** such pairs. Node exchange gives the same bound for P_(3,4,6).

These are bounds on a sufficient certificate's finite exceptional locus, NOT counts or existence claims for actual kernels. We have not resolved those finite loci here. No all-parameter statement, other primitive type, small-row regime min(r,s)<=5, F6/B6, arbitrary-GCM/all-level conjecture, H13 authentication or novelty follows.

The actual-source identification remains a separate named input: for r,s>=6 neither node-3 seed occurs through level six, so the source/target are the fixed free-Levi spaces at these degrees. The source lowest multiplicities are 109 at (3,3,6) and 107 at (4,3,6). The independent exact character calculation `frontier-20261028-level6-character-census-v1.json`, SHA `36cce754401b70c57984fe78245f9a25679d75d053874ea95991cbaaa2f3d88d`, checks these from Witt and the finite-sl3 Weyl-denominator formula; it is not a map proof.

## 2. Small exact algebra replaces large resultants

Put x=r-6,y=s-6. Each pair consists of TWO actual maximal minors of the same affine matrix, with exact rational coefficient tables. Remove their displayed positive linear factors (x+4), (x+5), (y+4), (y+5), with exactly the multiplicities in the algebra certificate; divide by a nonzero rational scalar. None of those factors vanishes on x,y>=0.

For (3,3,6), the residual pair A,B has total degrees 86 and 93. For (4,3,6), the initial residual degrees 87 and 88 have a common degree-7 factor F. Its constant term and every coefficient are positive; exact convolution removes F from both, leaving total degrees 80 and 81. F is the product (up to a positive constant) of

    76x^3+222x^2y+2402x^2+192xy^2+4394xy+24459x
    +50y^3+1808y^2+21204y+80724

and

    208x^4+872x^3y+9006x^3+1248x^2y^2+26976x^2y+142507x^2
    +752xy^3+25050xy^2+274288xy+983103x
    +160y^4+7332y^3+123907y^2+916794y+2502444.

These displays explain positivity; the exact coefficient table and its full product check are controlling inputs.

For BOTH final residual pairs:

1. The x-leading coefficients of A and B are nonzero CONSTANTS. Thus a hypothetical nonconstant common factor in Q[x,y] cannot depend on y alone, and its positive x-degree survives specialization y=0.
2. Modulo p=1009, both x-degrees survive and the certificate supplies explicit u,v with **u A(x,0)+v B(x,0)=1**. Every coefficient of this identity is replayed using only Python integers. Hence A(x,0),B(x,0) are coprime over Q, so A,B are coprime over Q[x,y].
3. They also have no common component over C: a common complex factor has algebraic coefficients and its Galois orbit product would yield a common Q-factor (or equivalently use invariance of the coprime resultant under scalar extension).
4. Projective plane Bezout therefore bounds their distinct common affine complex points by deg(A)deg(B), respectively 86*93=7998 and 80*81=6480. A rank-deficient parameter pair makes both maximal minors zero, hence belongs to this finite common-zero set. Positive removed factors cannot add any point in the quadrant.

This proves both cofinite statements at the source/minor input cut. It uses only Gauss' lemma/specialization, finite-field polynomial Bezout identities and projective Bezout's degree bound; no genus, Faltings, Hilbert irreducibility, numerical magnitude or selected-row rank extrapolation is used.

## 3. Pinned evidence and precise assurance

| Pair | Algebra certificate SHA-256 | Standard-library replay SHA-256 |
|---|---|---|
| (3,3,6) | `16308113e822d8895dac571d08da8590cd9fe7585d5a5d22fb235a8c05bcb604` | `bdbabd86ee39aafeeae82027857be74552c5ffcfaf3e658b4f9d5171b8472ff9` |
| (4,3,6) | `e2d7a5aa3a6d274444d07e882957a5a374484e0e60cef3404c845336e308db28` | `59ccacb634e8d9b8e6bdcecd46b6eb4a4f295153991c92d095a1d5bcff908bbb` |

The files are `frontier-20261028-level6-336-fast-pair-algebra-v1.json`, its `...-algebra-independent-replay-v1.json`, and the corresponding `436` pair. Each algebra certificate pins BOTH complete stored minor coefficient tables and their common pencil identity.

Producer `frontier-20261028-level6-fast-pair.py`, SHA `b4f613644778a02eddf75685db8793a3470aa5da4c8ea1c967b750f24fb0c4e0`, uses owner-local python-flint 0.9.0. The independently authored replay `frontier-20261028-level6-coprime-pair-replay.py`, SHA `de8d1d42bf4026f803346834df3c79a0f53296edaddb4643824297e24c023551`, imports NO FLINT/SymPy/producer: it checks every exact rational coefficient product back to both pinned minor tables, every positivity and leading-coefficient condition, primality, degree preservation and the full modular Bezout identity. BOTH returned PASS in the call ending **Wed Oct 28 22:04:02 PDT 2026**.

That replay certifies **polynomial algebra only**, NOT the equality of a stored coefficient table with its matrix determinant or actual Lie-algebra source/target. Those stay separate scientific review obligations. All earlier immutable process findings and quarantines remain historical; no held output is accepted as a premise. Direct resultant work may later resolve the finite exceptional set, but no unfinished computation is used in this theorem.

**END — complete cofinite polynomial/minor argument at named source inputs; all-parameter conclusion still open for these types.**
