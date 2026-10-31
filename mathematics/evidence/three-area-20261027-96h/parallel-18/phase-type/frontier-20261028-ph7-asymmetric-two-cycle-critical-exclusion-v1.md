# Exact exclusion at z=8/9 for the four-equal-plus-one, two-equal two-cycle family

**NEW EXACT WRITTEN + TWO IMPLEMENTATION CHECKED SUBCASE; independent peer review/novelty clearance pending.** MathResearch96h-2, original math-1. This is an ACTUAL critical-ratio obstruction, but only for the explicitly stated family; it does NOT exclude unrestricted PH7 at8/9 or establish minimum8.

## 1. The excluded family

Consider any real seven-by-seven matrix whose off-diagonal graph is the directed theta shape `(k,l,m)=(4,1,3)`: a directed five-cycle and a directed seven-cycle sharing a directed path of four edges, with exactly those eight edges. Suppose that of the FIVE common cycle vertices, FOUR diagonal entries are `-U` and the fifth is an arbitrary `-W`; at the TWO vertices outside the short cycle, both diagonal entries are `-V`. Edge weights may be arbitrary positive values, and input/exit vectors arbitrary; the proof even allows the two cycle products and U,V,W to be arbitrary real numbers.

**Theorem.** No such matrix can have a characteristic polynomial divisible by

    D(y)=y[(y+1)^2+8/9]^2.                          (D)

Thus this family cannot represent the target at z=8/9, regardless of probability normalization, hidden roots or input/exit choice. In particular it contains the earlier exact v4 PH7 graph at its lower algebraic endpoint, while allowing the fifth common diagonal to vary independently; that earlier endpoint is below8/9 and is not contradicted.

No restriction to four equal common diagonals or to equal two outer diagonals is known to hold for an arbitrary PH7 representation, even for this eight-edge topology. The other 13 eight-edge shapes and ALL graphs with nine or more edges remain outside the theorem.

## 2. Exact coefficient conditions

The only nontrivial directed cycles share vertices. The permutation determinant expansion therefore gives the actual characteristic polynomial

    P(y)=(y+W)(y+U)^4(y+V)^2 - D1(y+V)^2 - D3,     (P)

where D1,D3 are the two cycle-edge products (including any positive diagonal-similarity scaling). This determinant formula is independent of the order of the five common vertices. If D divides P, the monic hidden quadratic has the uniquely forced coefficients

    p=4U+W+2V-4,
    q=6U^2+8UV+V^2+4UW+2VW-4p-70/9.

Equivalently, as a fully expanded expression,

    q=6U^2+8UV+4UW-16U+V^2+2VW-8V-4W+74/9.

Let

    R(y)=(y+W)(y+U)^4(y+V)^2 - D(y)(y^2+p y+q),
    E4=[y^4]R,  E3=[y^3]R,
    E1=[y]R-2V[y^2]R.                              (E)

The shorter-cycle term has degree2, and the longer-cycle term degree0. Coefficient matching thus forces `E4=E3=0`; the y² coefficient forces `D1=[y²]R`, and the y coefficient then forces `E1=0`. These implications use no division and remain valid for all degeneracies or zero feedbacks.

## 3. Eliminate W and V without a sign or denominator assumption

Each E in(E) is LINEAR in W. Write `E_j=A_j(U,V)W+B_j(U,V)` for j=4,3,1, and form

    F=A4 B3-A3 B4,
    H=A4 B1-A1 B4.                                 (ELIM)

If all three E_j vanish then F=H=0, EVEN if A4=0. Thus a common real V would force the Sylvester resultant `Res_V(F,H)` to vanish. The exact rational computation proves

    Res_V(F,H)=C P2(U)^3 P6a(U) P6b(U) P24(U),   C!=0,

    P2=9U^2-18U+17,
    P6a=18225U^6-87480U^5+190026U^4-239598U^3
          +186102U^2-84456U+17629,
    P6b=72900U^6-145800U^5+145800U^4-113400U^3
          +68085U^2-26010U+4913,
    C=-512/109418989131512359209.

The complete literal P24 coefficient list is in the pinned JSON certificate below. Exact Fraction Sturm chains show NO factor has any real root:

    factor       degree  variations(-infinity)  variations(+infinity)
    P2              2              1                      1
    P6a             6              3                      3
    P6b             6              3                      3
    P24            24             12                     12.

The difference in each row is0, so the resultant is nonzero for EVERY real U. Consequently no real U,V,W can satisfy(E), and no P of the stated graph can contain the repeated target pair plus0. This proves the theorem. □

## 4. Two exact, materially different checks

First run, `frontier-20261028-ph7-asymmetric-cycle-89-resultant-check.py`, **90LF/3873B**, SHA256 `a1c994f0588d019c9a4df56c9809d9d3de924660bfc1116da1002b0eddd39704`:

    SymPy 1.14.0 plus independent Fraction Sturm PASS: four resultant factors have no real roots
    degrees/multiplicities: [(2,3),(6,1),(6,1),(24,1)]

It extracts all coefficient equations, verifies the two no-division eliminant identities, constructs the 9-by9 Sylvester matrix, checks its determinant equals the resultant, checks the literal factorization, and computes sign-normalized Sturm sequences with custom Python `Fraction` arithmetic.

The exact certificate `frontier-20261028-ph7-asymmetric-cycle-89-resultant-certificate.json`, **57LF/3173B**, SHA256 `358b8628a4c2c45447d22046634f2a9c1a59af05f5e5c4a35dc7da6851ef2d77`, records both full eliminants, all four factors including P24, the constant and the Sturm counts.

A second, independently written **standard-library-only** replay `frontier-20261028-ph7-asymmetric-cycle-89-fraction-replay.py`, **121LF/4591B**, SHA256 `929fad847ef3396e457d2fcf973bc67942c441f613fb87797bd312734d2a03f7`, was then executed:

    Independent stdlib Fraction replay PASS: 55 Sylvester evaluations establish degree<=54 identity; four Sturm root counts zero
    variations (-inf,+inf): [(1,1),(3,3),(3,3),(12,12)]

It derives(E)/(ELIM) directly using its OWN rational polynomial operations, constructs F and H as polynomials in V by exact Newton interpolation, computes each 9-by9 Sylvester determinant by independent rational Gaussian elimination, parses the printed factor polynomials without `eval`, and redoes Fraction Sturm division. The resultant has U-degree at most `5*6+4*6=54` because F has V-degree<=4 and U-degree<=6, and H has V-degree<=5 and U-degree<=6. Agreement at 55 distinct integer U values therefore proves the entire exact factorization polynomial identity, not a numerical sample. The independent replay still consumes the factor certificate and is not a human or cross-vendor proof; its arithmetic and degree bound are transparent for another reviewer.

## 5. Boundaries

This proof is an exact exclusion of a strictly enlarged equal-rate two-cycle subfamily AT the original critical z=8/9. It gives no claim about ratios near8/9, fully nonuniform diagonals, balanced/full A-or-B fibers, all eight-edge graphs, or nine-edge graphs. A resultant-zero converse is never assumed, and there is no numerical optimizer premise. No parent adoption, Lean/kernel proof, novelty conclusion, old source revision, or historic process cure is claimed.

END — the stated four-equal-plus-one/two-equal two-cycle family is rigorously impossible at z=8/9; the unrestricted problem remains open.
