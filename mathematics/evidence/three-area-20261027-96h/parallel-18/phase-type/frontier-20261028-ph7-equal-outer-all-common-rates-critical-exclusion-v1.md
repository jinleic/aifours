# PH7 at 8/9: complete exclusion of the 5/7-cycle graph with equal outside rates

**NEW EXACT WRITTEN + INDEPENDENT IMPLEMENTATION CHECKED TOPOLOGICAL SUBCASE. Independent peer review, parent adoption, formal proof and novelty clearance pending.** MathResearch96h-2, original math-1. This is an exact critical-ratio exclusion with **all five common rates unrestricted**, not an unrestricted PH7 solution.

## 1. The theorem and its exact scope

Consider the directed 8-edge theta graph with a directed 5-cycle and 7-cycle sharing a 4-edge path. Its five common vertices have arbitrary positive diagonal escape rates `u1,...,u5` in any order; its two extra vertices have the SAME positive diagonal escape rate V. All eight edge weights and all input/exit vectors are otherwise arbitrary. At

    z=b²/(a-c)²=8/9,

NO such matrix can have characteristic factor

    D(y)=y[(y+1)^2+8/9]^2.                          (D)

Consequently this entire graph/rate family cannot realize the original PH target at8/9. The proof imposes no equalities on the five common rates, no hidden-root type, and no diagonalizability assumption. It uses the common-rate polynomial's necessary real-rootedness; it does NOT prove that arbitrary PH7 generators have equal outer rates, this theta graph, or eight edges.

The previously exact `frontier-20261028-ph7-two-valued-common-rates-critical-exclusion-v1.md`, SHA256 `3daac4b259227270fd27f588d8b1706a4861f95b5a4373f5afe95b81e5557685`, covers the degenerate case in which the five common rates take at most two distinct values. Its cited 4+1/3+2 resultant proofs and independent Fraction replays are an explicit dependency, not silently subsumed by a strict inequality.

## 2. Reduce FIVE arbitrary rates to two aggregate variables

Let `s_j` be the elementary symmetric functions of `u1,...,u5`, and write `s=s1`. The actual determinant permutation expansion has just its diagonal product and the two overlapping cycle terms:

    P(y)=A(y)(y+V)^2-D1(y+V)^2-D3,
    A(y)=y^5+s y^4+s2 y^3+s3 y^2+s4 y+s5.

D1,D3 are positive products of the actual edges. If D divides P, its monic hidden quadratic is `Q=y²+p y+q` with

    p=s+2V-4,
    q=s2+2V s+V²-4p-70/9.

Write `T_j=[y^j](D Q)`. The y4 and y3 equations determine

    s3=T4-2V s2-V² s,
    s4=T3-2V s3-V² s2.                             (COEF)

The y2 equation fixes D1. The y1 equation, with that D1 substituted, is

    (9V²-18V+17) * [324sV³-1944sV²+1944sV-612s
      +(405V²-486V+153)s2-1296V³+4626V²-3996V+1258] = 0.

The first factor is `9(V-1)²+8>0`. Also

    d=45V²-54V+17=45(V-3/5)²+4/5>0.

Therefore the second factor uniquely determines s2. Let `A2=9d s2`, `A3=9d s3`, `A4=81d s4`. They are explicit INTEGER polynomials linear in s, given in the pinned checker/certificate; for example

    A2=-2[(162V³-972V²+972V-306)s
           -648V³+2313V²-1998V+629].

The constant-coefficient equation gives, with no input/exit assumption,

    D3/V² = T2-2V s4-V² s3
          = (s-4)[9(V-1)²+8]^3/(81d).                (LONG)

Since the actual long-cycle product and V are positive, (LONG) forces `s>4`.

## 3. Strict Newton and Hankel conditions for the remaining cases

For five positive rates, s2,s3,s4 are positive. If at least three distinct rates occur, the ordinary strict Newton inequality and Vandermonde Gram matrix give

    s3² > 2 s2 s4,                                    (NEWTON)
    det [[5,p1,p2],[p1,p2,p3],[p2,p3,p4]] > 0,      (HANKEL)

where `p_k=sum_i u_i^k`, `p1=s`. (NEWTON) is strict for non-equal positive rates; the Hankel matrix is a Gram matrix of the vectors `(1,u_i,u_i²)` and is positive definite precisely when at least three distinct rates occur. If there are at most two distinct rates, the explicitly named previous exact theorem handles the case.

Use Newton identities to define

    p2=s²-2s2,
    p3=s³-3s s2+3s3,
    p4=s^4-4s²s2+2s2²+4s s3-4s4.

After clearing the strictly positive denominators, (NEWTON) is `N=9 A3²-2 A2 A4>0`. Define `D0=9d`, `P2=D0 p2`, `P3=D0 p3`, `P4=D0² p4`; then (HANKEL) is equivalent to `H>0`, with the explicit polynomial

    H=5P2 P4-5D0 P3²-s²D0 P4+2s D0 P2 P3-P2³.

Accordingly EVERY remaining candidate must satisfy the SIX strict rational-polynomial inequalities

    s-4>0, V>0, A2>0, A3>0, A4>0, N>0, H>0.        (STRICT)

Here V>0 is the base-coordinate domain; the other six displayed polynomials are the six constraint entries in the certificate. (There are seven strict inequalities including V>0.) The proof below rules out this necessary system; it never presumes that Newton/Hankel are sufficient for five rates.

## 4. Exact complete two-variable sign decomposition

For the six listed polynomials in `(s,V)`, their degrees in s are `1,1,1,1,2,4` and their maximum V-degrees are `0,3,4,5,8,10`. Form ALL leading coefficients in s, discriminants for degrees>1, and pairwise s-resultants: 23 projection polynomials. Their exact rational factorization has 17 distinct nonconstant factors. Exact Sturm counts show that altogether these factors have **25 distinct positive V roots**, isolated in disjoint rational intervals in the certificate.

On the 26 open V intervals between these roots, all six polynomials have fixed degree, their s-roots are simple, and roots of different polynomials cannot cross: all relevant leading coefficients, discriminants and resultants are nonzero there. At one rational V in each interval, exact Sturm sequences isolate EVERY s-root above4. The 26 sections yield 82 open rational sign cells in s; at least one of the six constraints is negative on each cell, as the exact certificate records. Since the required inequalities are STRICT, a solution at an omitted projection root would persist under a small perturbation to a neighboring open V interval; a solution at an s-root is also impossible. Thus(STRICT) is empty on the ENTIRE half-plane `V>0,s>4`.

This covers every case with three or more distinct common rates; the named two-valued theorem covers the remaining cases. Hence the theorem follows. □

## 5. Two exact checks and the actual proof boundary

Primary executable `frontier-20261028-ph7-equal-outer-open-cad-check.py`, **139LF/6504B**, SHA256 `a16e89e7a260d719257a9c9cd4e3484ec5cdb911990b7315eb5a2c1a606b1083`, actually returned

    SymPy 1.14.0 and custom Fraction Sturm PASS: open system empty; 26 projection intervals and 82 sign cells

It verifies the original spectral coefficient elimination, positive-denominator identities, projection factorization, all projection and section Sturm counts, and the literal signs. The full rational certificate `frontier-20261028-ph7-equal-outer-open-cad-certificate.json`, **1424LF/32782B**, SHA256 `ebe39f8329350a7b48cdd75d13263c9fbc6520e53e577272fd8e1d5d0eb90890`, contains every polynomial, factor, isolating interval and sampled sign failure.

Separately written standard-library-only replay `frontier-20261028-ph7-equal-outer-open-cad-fraction-replay.py`, **205LF/9373B**, SHA256 `78a93dee3bca79a4031baf3031d768e20eb0479deb0c4b954639fab8e056105b`, actually returned

    23 projection identities replayed at 61 exact values each
    Independent stdlib Fraction CAD replay PASS: 25 projection roots, 26 base intervals, 82 empty strict-sign cells

It reconstructs the spectral eliminations and all six bivariate polynomials from scratch with sparse rational arithmetic; compares their literal coefficients to the certificate; independently evaluates EVERY Sylvester/discriminant/leading-coefficient factorization at 61 integers. The analytic upper bound on the projection degree is60, so these are exact polynomial identities, not numerical sampling. It then independently recomputes all factor and section Sturm chains and all 82 rational signs. The replay reads the primary certificate's factor/interval tables; it is an independent algorithmic implementation, not a human, cross-vendor, Lean or kernel proof.

The proof's non-machine imports are finite determinant/adjugate algebra, strict Newton inequalities for positive roots, Vandermonde Gram positivity, univariate Sturm theorem, and the elementary root-continuation/delineability argument when leading coefficients, discriminants and pairwise resultants are nonzero. Review must include the degenerate two-valued dependency, coefficient degree bounds, complete projection factorization and strict-boundary reasoning. No computational timeout or floating optimizer is used in this exclusion.

## 6. Remaining original gap

This removes the **whole equal-outer-rate subfamily** of the 5/7-cycle graph at8/9, including fully nonuniform common rates. It does not remove the SAME graph with unequal outer rates, any of the other 13 eight-edge theta/figure-eight shapes, or generators with >=9 transitions. No unrestricted 8/9 feasibility/exclusion, global spectral maximum, minimum8, novelty or independent-review acceptance is claimed. Held outputs remain nonpremises and earlier process findings survive.

END — the 5/7-cycle PH7 graph with equal outside rates is exactly impossible at 8/9, for ALL five positive common rates.
