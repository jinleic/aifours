# Level five: a positive six-source determinant settles the actual 3-to-5 quotient

Owner MathKacMoody. Verbatim observed clock immediately before creation: **Sun Oct 25 03:53:14 PDT 2026** (`/bin/date`). NEW successor; all earlier pinned packets remain unchanged.

**Status: WRITTEN-checked-in-kernel, pending fresh independent reconstruction and parent disposition.** All finite checks below used integer arithmetic and `fractions.Fraction` in this owner's persistent eval kernel. No native scientific program, solver, background job, external model, network publication, nested agent or git operation was launched. SymPy was unavailable; it was not installed. This is not proof-assistant/kernel certification, a blind/different-vendor review, a novelty decision, or a general Serre theorem.

## 1. Verdict and exact imports

Let S be the full complex Serre quotient for

    A(r,s) = [[2,-1,-1],[-1,2,-1],[-r,-s,2]],

with l=sl3 on nodes 1,2 and original D3=[f3,-]. For EVERY integer r,s>=2, the actual invariant map

    D3 : S5^l -> S_(5,5,4)

is injective. In particular the genuine quotient by the previously supported U=span{X,Y,Z},

    S5^l/U -> T8/D3(U), dimensions 3 -> 5,

has trivial kernel. This proves the requested quotient verdict without guessing three complementary quotient coordinates: a new complete six-source determinant proves the stronger full-source statement directly. The old three-plane determinant is not used to infer the other columns.

Together with the separately supported row-one theorem (and the classical zero-source affine corner), this settles ONLY the invariant primitive type at full degree (5,5,5) for all positive integer r,s. The OTHER SEVEN primitive-map obligations remain open in general. H13 is still EXTRA for the earlier A(2,1)/(1,2) whole-band consequence. B4, H223, F64 and H13 are NOT premises of the invariant theorem here.

Named mathematical imports, rather than undeclared rank assumptions:

1. The positive elimination identifies the free positive level model with L(V), V=ad(sl3), and the actual ideals through level five are those of `level5-structural-interface-v1.md` §§2,6.
2. Free Lie algebras embed in their tensor enveloping algebras (PBW). Finite sl3 modules are semisimple.
3. The exact free invariant multiplicity is dim L5(V)^l=6, proved by the written PBW/Witt/Weyl calculation in that interface §5.
4. For r,s>=2 the ACTUAL T5 has no invariant and the ACTUAL T4 has no adjoint. Thus the six free invariants and all eight free adjoint-highest target lines survive unchanged. These are the representation-theoretic statements of the interface §6, not a free-space replacement of an actual quotient.
5. The ORIGINAL local bracket, including its central level action, is the one derived in the row-one candidate §6 and reproduced in §4 below.

The structural-interface source is pinned at SHA256 `ef56a3c2406f80924ce7a1b5bb9e4ac904398088a1f06c4f68cb4833738bcc44`; the row-one candidate at `e85cf5c87652d85fdb5e392d908ccb786e4adfa8a1e41b135b2c472539719a3c`, operative with its editorial addendum `df229221f405cda40460ec26fa490b82f9b802cabc657921862434684050b74e`. The former three-plane packet is pinned at `33296b7fb42b57dd44b68eeb875d9ae225c5a895dee290c97a58f562a5294409`. The positive quotient verdict below is NEW and does not inherit those packets' reviews.

## 2. A completely explicit rational six-source set

Use the following zero-based basis b_i of traceless 3x3 matrices:

|i|0|1|2|3|4|5|6|7|
|---|---|---|---|---|---|---|---|---|
|b_i|E12|E21|E23|E32|E13|E31|H1=diag(1,-1,0)|H2=diag(0,1,-1)|
|c_i=3b^i|3E21|3E12|3E32|3E23|3E31|3E13|2H1+H2|H1+2H2|

Here b^i is trace-dual to b_i; hence Tr(c_i b_j)=3 delta_ij. Write u_i for the positive generator labelled by b_i. For a five-index tuple i=(i0,...,i4), put

    R(i)=[u_i0,[u_i1,[u_i2,[u_i3,u_i4]]]].

Every sum in this section runs independently over i0,...,i4=0,...,7. Define six raw invariants F_j by the indicated trace coefficient multiplying R(i):

|j|coefficient in F_j=sum coefficient*R(i)|F_j in terms of S_j|
|---|---|---|
|1|Tr(c_i0 c_i1 c_i2 c_i3 c_i4)|-27 S1|
|2|Tr(c_i0 c_i1 c_i3 c_i2 c_i4)|27 S2|
|3|Tr(c_i0 c_i2 c_i1 c_i3 c_i4)|-27 S3|
|4|Tr(c_i0 c_i2 c_i3 c_i1 c_i4)|81 S4|
|5|Tr(c_i0 c_i2) Tr(c_i1 c_i3 c_i4)|-81 S5|
|6|Tr(c_i0 c_i3) Tr(c_i1 c_i2 c_i4)|-27 S6|

These equations DEFINE S1,...,S6 over Q. No unspecified projection or basis search is part of the definition. Invariance follows because each trace contraction is invariant in (V*)^tensor5 and the right-normed bracket is equivariant. Thus every S_j lies in the free invariant space and survives to the actual invariant space by import 4. A direct integer check also annihilated every source by E12,E21,E23,E32,H1,H2.

In the tensor embedding, the respective nonzero coefficient counts are 1688,1676,1888,1232,1392,1768. These counts are reproducibility metadata, not the independence proof. Independence follows from the nonzero detector determinant below. Together with the named dimension-six import this makes the S_j a BASIS of the WHOLE actual source.

## 3. Six target coefficient detectors, with the actual-quotient justification

For an associative tensor word w=(j0,j1,j2,j3), let [w] denote its coefficient in the PBW tensor embedding of L4(V). Use, in this order,

    w1=(0,0,1,2), w2=(0,0,2,1), w3=(0,1,0,2),
    w4=(0,1,4,6), w5=(0,1,6,4), w6=(0,2,2,3).

Thus the first detector reads the coefficient of u_E12 u_E12 u_E21 u_E23, not a commutative monomial. Repeated labels are intentional.

A tensor coefficient need not annihilate every non-adjoint target relation. That is NOT assumed. Instead, for an invariant source the whole-W map x -> [w_x,S_j] is l-equivariant. Its value at f3=w_E13 lies in the adjoint-highest multiplicity space of L4(V). The actual T4 has NO adjoint. Hence this entire free adjoint-highest space maps isomorphically to its actual image. The six detectors are defined there by this inverse, then the displayed free tensor coefficient. In particular an actual zero D3 image necessarily makes every detector zero. No relation from another isotypic component can create a false kernel implication.

## 4. Exact original lowering recurrence

Set

    a=(r+s)/2, b=(r-s)/2, c=2-r-s.

The letters a,b,c in §§4-6 are scalars, not full-degree coordinates or basis indices. The derived original local bracket is

    [w_x,u_y] = a[x,y] + b(xy+yx-(2/3)Tr(xy)I) - Tr(xy) z0,
    [z0,u_y] = c u_y,     f3=w_E13.

The first two terms in the first line are actual level-zero Levi vectors. For a tensor Lie polynomial P=sum p_i u_i0...u_i(n-1), n>=2, its degree-(n-1) lowering tensor is obtained by summing, for EACH i<j, the original tensor with slot i deleted and slot j replaced by the matrix-labelled generator

    L_x(i,j) = a[[x,b_i],b_j]
             + b[x b_i+b_i x,b_j]
             - c Tr(x b_i) b_j.                       (4.1)

All other slots keep their order. For the theorem x=E13. Expand L_x(i,j) in the fixed b-basis and sum its scalar coefficients.

Proof of (4.1): apply the commutator derivation [w_x,-] to a tensor word and move each resulting level-zero element to the right. Its commutator with each later generator gives exactly the displayed ordered pair i<j. The final terms with a level-zero factor on the right cancel on every homogeneous Lie polynomial of degree>=2: their coefficient is the ordinary tensor derivation sending generators to scalar components of [w_x,u_y]; a scalar-valued generator derivation kills all Lie brackets of degree>=2. The trace subtraction in the Jordan term commutes with b_j and therefore disappears only INSIDE this matrix commutator. The central term contributes once for each later slot, so the full level action is retained, not replaced by a degree-one action.

This recurrence is affine in the ORIGINAL row parameters. It neither assumes a negative current-algebra representation nor replaces lowering by positive evaluation. Integer/Fraction controls reconstructed D_x B_y=(6a-2c)[x,y]+6b d(x,y) for ALL eight basis y, and the frozen first detectors epsilon4(D_x X)=216c x and epsilon4(D_x Y)=0.

## 5. The complete six-by-six detector matrix

Let M_ij=[w_i]D3(S_j). Expanding ONLY the explicit definitions in §2 by the right-normed commutator and using (4.1) gives the following matrix. Every entry was checked exactly in the owner's eval kernel; all 36 entries, not sampled parameter values, are specified here.

    M =
    [ 18b,                 -27a+9b+18c,    -81a+45b+27c, -9a+9b+3c,    -9a+15b,       -81a+63b+54c ]
    [ -18a-24b+9c,          9a-9b-18c,     -45a-51b+18c, -9a-9b+3c,    -21a-15b+12c,  36a-60b-36c ]
    [ 9a-21b-18c,           36a+24b,        63a-21b-18c,  18a+4b-3c,    21a-3b-6c,     99a+3b-36c  ]
    [ -10b-12c,             27a-7b-15c,     27a-19b-39c,  9a-b-6c,      6a+2b-6c,      9a+9b       ]
    [ 10b+9c,               -36a-2b+18c,   -27a+b+36c,   -12a-2b+7c,   -6a-6b+6c,     -9a-15b-6c  ]
    [ 9a+15b-18c,           36a-18c,        63a+15b-54c,  18a-4b-9c,    9a-3b-6c,      81a-15b-36c ]

An entry is reconstructible by a finite sum over at most 8^5 index tuples, sixteen signed right-normed tensor permutations, and ten ordered lowering pairs; no missing linear solve defines it. The accompanying `level5-full-invariant-arithmetic-v1.json` gives the same entries as integer triples (coefficient of a,b,c), together with the determinant coefficients.

## 6. A coefficientwise positive determinant on the ENTIRE quadrant

Put u=r-1 and v=s-1. Then

    a=1+(u+v)/2, b=(u-v)/2, c=-(u+v).

The exact symbolic determinant is

    det M = -43740 P(u,v),                            (6.1)

where P has zero constant term and the following coefficient triangle. In row d the entries are the coefficients of u^d, u^(d-1)v, ..., v^d, respectively:

|d|coefficients, in decreasing u-degree|
|---|---|
|1|3645, 3645|
|2|17496, 38718, 18306|
|3|33561, 114804, 118341, 36774|
|4|32184, 148365, 239004, 158895, 36972|
|5|15438, 89052, 195747, 202992, 99540, 18621|
|6|2964, 20414, 56828, 80639, 61380, 23913, 3762|

This is a polynomial identity, not numerical interpolation or a diagonal-rank inference. It was computed with a subset/permutation determinant recurrence over exact integer coefficient dictionaries after substituting into 2M; explicitly det(2M)=-2799360 P, and 2799360/2^6=43740. There are no omitted nonzero coefficients. EVERY displayed coefficient is a positive integer. Therefore P(u,v)>0 whenever u,v>0 (indeed whenever u,v>=0 and u+v>0). In particular det M is nonzero for every integer r,s>=2, including the diagonal, with NO appeal to a continuity argument or the classical diagonal theorem.

If a linear combination of the six actual S_j had D3 image zero, §3 would force M times its coefficient vector to vanish. Equation (6.1) forces all coefficients zero. Hence the six sources are independent, form the whole dimension-six source, and D3 is injective on it. This proves the theorem in §1.

## 7. Literal quotient conclusion and unchanged residuals

Retain the previously supported actual three-plane U and its injective original image. If a class x+U is killed by the induced quotient map, then D3 x=D3 u for some u in U. Full injectivity just proved gives x=u. Thus the ACTUAL 3-to-5 quotient kernel is zero. No parameter-independent quotient basis or affine five-by-three quotient matrix is claimed or needed.

The seven nontrivial primitive types at (2,2,5),(3,2,5),(2,3,5),(3,3,5),(4,3,5),(3,4,5),(4,4,5) still require their own actual map verdicts at original-row parameters ar+bs>=10. The companion source-geometry packet begins their classification; source multiplicity is not an injectivity proof. Universal F5, the whole B5 band without these maps/B4, outside-band (4,4,6), and general Serre equality are NOT concluded. H13 remains an extra input for the optional A(2,1)/(1,2) band corollary, not authenticated by this new invariant argument.

## 8. Reconstruction gate

A fresh reviewer must reconstruct: the trace-dual normalization and all six raw-source scales; source invariance; the ordered-pair recurrence with its rightmost cancellation and actual central level action; all 36 affine entries; the complete determinant triangle and its scale; and the actual-isotypic quotient argument. Checking only the positive signs of a copied polynomial or only a numerical matrix is insufficient. Same-harness exact arithmetic is disclosed as such; it does not confer formal/kernel, independent-vendor or novelty acceptance. All parent errata, the scientific-launch HOLD and frozen deadline remain binding.
