# Joint privacy-budget inversion beyond the fixed-ratio window

**AUTHOR CANDIDATE — WRITTEN with bounded exact arithmetic checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:30:22 PDT 2026`.

## 1. Contract and precisely named dependencies

For the original ALL-law, ALL-event, FULL closed l1-unit-diamond privacy class define `b_max(j,ell)` as the supremum of b=e^(-epsilon) for which a law satisfies `J=E|X|^2<=j` and `L=E||X||_1<=ell`; define epsilon_min=-log b_max. Let j>0, ell>0 both tend to 0.

This written candidate depends on four UNREVIEWED pinned results:

* `frontier-20261028-joint-budget-privacy-inversion-v1.md`, SHA-256 `376f8c4f3991512619af91f10a2b2559a27bd96c13df83e50942581ab40d7e05`, for the fixed positive ell/sqrt(j) window;
* `frontier-20261028-mixed-degree-three-regime-crossover-v1.md`, SHA-256 `712f291cdd97525ca9776f77150c03ee12130d309933ea406c46c921c0996085`, for variable-weight supercritical actual upper laws and all-law scalar lower values;
* `frontier-20261028-supercritical-moment-allocation-v1.md`, SHA-256 `25936be05e3b9c09107459369abb60cdf494938c0db1eb6976560d14258193c1`, for the J/L allocation when kappa is bounded or tends to zero;
* `frontier-20261028-elementary-mixed-budget-bounds-v1.md`, SHA-256 `071501a2cf2a81fd5dd4b2f062bd07ec0615e49f5da38f97fc8549f80285161c`, for all-law finite-b J-only and L-only budget bounds.

No formal verification, independent review, novelty claim or parent adoption is made. In particular, no unreviewed import is silently promoted.

## 2. New arbitrary-ratio mean-dominated window

Assume

    ell/sqrt(j) ->0,       r=j/ell>0.                                    (1)

The ratio r need NOT converge; it may approach 0, a positive constant, infinity, or oscillate. Define

    F(r)= (27/4) r(1-2r)^2    for 0<r<1/6,
          1/2                  for r>=1/6.                                (2)

Then the candidate exact FIRST-ORDER asymptotic is

    b_max(j,ell)=ell^3 F(j/ell)[1+o(1)],
    epsilon_min=3log(1/ell)-log F(j/ell)+o(1).                            (3)

The relative o(1) in (3) includes r->0, where F(r)->0; it is not merely an absolute error. Special cases:

* If `j/ell->0`, then `b_max~(27/4)j ell^2` and `epsilon_min=log[4/(27 j ell^2)]+o(1)`.
* If `j/ell->r0` in (0,1/6), then `b_max~(27/4)r0(1-2r0)^2 ell^3`.
* If `liminf j/ell>=1/6`, then `b_max~ell^3/2`: the first-norm budget alone controls the leading value.

At r=1/6 the formulas meet continuously. The last conclusion includes r->infinity. A relative o(1) as ell/sqrt(j)->0 does not supply a uniform finite-error bound.

## 3. Optimizing the all-law scalar lower bound

For 0<r<1/6 set

    kappa=2r/(1-6r),
    F(r)=(r+kappa)^3/[kappa^2(1+2kappa)].                               (4)

The latter identity is exact. For ANY feasible law, `J+kappa L<=j+kappa ell`. The imported supercritical lower theorem says

    inf_(full-private)(J+kappa L)
       =[b kappa^2(1+2kappa)]^(1/3)[1+o(1)]                              (5)

whenever `kappa/b^(1/4)->infinity`, allowing varying kappa. To check this for arbitrary near-supremizing feasible b, use the finite J-only bound `b=O(j^2)`. If r stays in a compact subset of (0,1/6), kappa is bounded away from 0 and b->0. If r->0, then

    kappa/b^(1/4) >= constant * (j/ell)/sqrt(j)
                    =constant * sqrt(j)/ell ->infinity.                   (6)

The same applies along any subsequence r->r0<1/6, r0>=0. Thus (5) gives the RELATIVE upper bound `b_max<=ell^3 F(r)[1+o(1)]` even as r->0. Algebraically, (4)'s kappa is the unique stationary minimizer of `(r+kappa)^3/[kappa^2(1+2kappa)]` for r<1/6.

When r->1/6 from below, (5) with divergent kappa is unnecessary: the imported pure first-norm bound directly gives `b_max<=ell^3/(2-3ell)~ell^3/2`. The same upper bound works for r>=1/6.

## 4. Matching actual private mechanisms, not hypothetical points

First suppose a subsequence satisfies r->r0 with 0<=r0<1/6. Fix delta in (0,1) and take the ACTUAL full-D shell construction from the supercritical import at

    b=(1-delta)^3 ell^3 F(r),
    kappa=2r/(1-6r),
    A=[b(1+2kappa)/kappa]^(1/3)
      =(1-delta)(3/2)(1-2r)ell.                                         (7)

By (1), its `kappa/b^(1/4)->infinity`; this also holds if r->0. Its mixed cost is first-order optimal, so the pinned allocation import gives, uniformly along this sequence,

    J/[kappa A] = 1/[3(1+2kappa)]+o(1),
    L/A = 2/3+2kappa/[3(1+2kappa)]+o(1).                               (8)

For r->r0<1/6 the first displayed target is bounded away from 0, including r0=0. Substituting (7) gives RELATIVE estimates

    J=(1-delta)j[1+o(1)],     L=(1-delta)ell[1+o(1)].                    (9)

The laws therefore meet BOTH actual budgets for all sufficiently small j, establishing the matching relative lower bound after delta->0.

For r->1/6 or liminf r>=1/6, instead use the exact diamond shell with core radius `a=(1-delta)ell` and `b=a^3/2`. Its nested sets are `(k+a)D`. The k=0 and k=1 exact D moments show

    L=a[1+o(1)],     J=(a/6)[1+o(1)].                                    (10)

Indeed its denominator is `2a^2[1+o(1)]`; the first-norm numerator is `2a^3[1+o(1)]`, and the squared numerator is `(a^3/3)[1+o(1)]`, with higher shells negligible. Fixed delta gives strict budget slack even when r tends to 1/6 from below. Letting delta->0 proves the ell^3/2 lower bound. Subsequence compactness of r in [0,infinity] covers an arbitrary oscillating r sequence, with the r->0 case handled relatively as above.

## 5. Completion of all limiting ratio regimes

If ell/sqrt(j)->lambda in (0,infinity), the first pinned import gives `b_max~z_*(lambda)j^2`. If ell/sqrt(j)->infinity, the J-only finite bound and actual theta=0 shell give `b_max~(3pi/4)j^2`. Together with (3), these cover every sequence with a limiting ell/sqrt(j) in the extended interval [0,infinity]; arbitrary nonconvergent sequences can be analyzed on their convergent subsequences. The fixed-lambda z_* uses the exact scalar root given in the pinned 376f candidate.

## 6. Exact checks and claim limits

The Python eval kernel used `fractions.Fraction` to check selected formula (2)–(4) coefficients:

```text
r=1/24: F=121/512, kappa=1/9
r=1/12: F=25/64,   kappa=1/3
r=1/9:  F=49/108,  kappa=2/3
r=1/6:  F=1/2,     kappa diverges
```

These are finite algebra checks only. The all-law inequalities, relative r->0 uniformity, actual shell matching, and the r=1/6 boundary are written arguments dependent on the four pinned, unreviewed candidates. None has been independently reviewed, formally checked, novelty-cleared or parent-adopted.
