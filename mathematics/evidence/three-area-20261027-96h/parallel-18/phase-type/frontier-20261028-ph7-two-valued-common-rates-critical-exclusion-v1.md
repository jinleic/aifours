# At 8/9, an entire two-valued common-rate class of 5/7-cycle PH7 graphs is impossible

**EXACT WRITTEN + TWO INDEPENDENT IMPLEMENTATION CHECKED SUBCASE; peer review/novelty clearance pending.** MathResearch96h-2. This is an actual original-critical-ratio obstruction, not an unrestricted PH7 exclusion or a minimum8 result.

## Theorem

Take the directed eight-edge theta graph consisting of a directed 5-cycle and a directed 7-cycle sharing a four-edge path, so they share five vertices and the longer cycle has two additional vertices. Assume the five common diagonal escape rates take **at most two distinct positive values**, in arbitrary order/multiplicity, and the two extra-vertex diagonal escape rates are equal. All eight positive edge weights and actual PH input/exit data are otherwise arbitrary.

At `z=8/9`, no such matrix can have the required characteristic polynomial factor

    D(y)=y[(y+1)^2+8/9]^2.

Consequently no PH7 realization of the target at8/9 belongs to this class. No claim is made that an arbitrary theta graph, still less an arbitrary PH7 generator, has these diagonal equalities.

## 1. Reduction to the two multiplicity partitions

A positive-Perron-normalized generator has strictly negative diagonal entries, hence strictly positive escape rates. Among five common vertices, at most two distinct rates means one of `5`, `4+1` or `3+2`, after exchanging the labels of the two rates. The previous exact source `frontier-20261028-ph7-asymmetric-two-cycle-critical-exclusion-v1.md` SHA256 `2a9b73522733534d3082fab05b8760f1663c19429fb05c348ee571f75955df54` excludes the entire `4+1` case, including the all-equal case. Its no-real-root resultant is independently replayed there.

It remains to exclude `3+2`. Assign the rates U,U,U,W,W to the five common vertices and V,V to the other two. Their order along the common path is irrelevant to the determinant. The two cycles share vertices, so the ONLY non-diagonal determinant terms are their two cycle products. Thus the actual characteristic polynomial is

    P(y)=(y+U)^3(y+W)^2(y+V)^2-D1(y+V)^2-D3.        (P32)

All edge products D1,D3 may be regarded as arbitrary real scalars. If D divides P, the monic quadratic factor has the uniquely forced coefficients

    p=3U+2W+2V-4,
    q=3U²+6UV+6UW-12U+V²+4VW-8V+W²-8W+74/9.

Define

    R(y)=(y+U)^3(y+W)^2(y+V)^2-D(y)(y²+p y+q),
    E4=[y^4]R,    E3=[y^3]R,
    E1=[y]R-2V[y²]R.                                (EQ32)

As in the `4+1` proof, divisibility requires E4=E3=E1=0. No division by a rate, determinant or feedback is used.

## 2. Nested exact elimination and global positive-rate sign

Each E is quadratic in W. Let

    F(U,V)=Res_W(E4,E3),     H(U,V)=Res_W(E4,E1).

Any common W, including a degenerate leading-coefficient case, forces F=H=0. The two first resultants are the literal 4-by4 Sylvester determinants; F has degrees at most `(10 in U,8 in V)`, H at most `(10 in U,10 in V)`.

The outer 18-by18 Sylvester resultant has the exact factorization

    Res_V(F,H)=C U^6 [9(U-1)^2+8]^12 P6(U) P30(U) P66(U),  (RES32)

with the strictly positive rational constant

    C=1/145557834293068928043467566190278008218249525830565939618481.

The literal integer coefficients of P6,P30,P66 are in the pinned exact certificate. Their leading coefficients are positive. Independent exact Bernstein calculations prove each is strictly POSITIVE on the entire half-line U>=0: use a finite rational subdivision of [0,2] on which every Bernstein coefficient is positive, and verify every coefficient of `Pj(U+2)` is strictly positive on the tail U>=2. The numbers of certified subintervals are3,8,5 for degrees6,30,66 respectively. The quadratic is `[9(U-1)^2+8]>0`, and U>0, so(RES32) is strictly positive for every admissible U.

This contradicts F=H=0, hence no U>0 and real V,W satisfy the required spectrum. The conclusion does not require any sign of W,V or D1,D3; U>0 is exactly enough to remove the U^6 factor. Together with the earlier `4+1` exclusion this proves the theorem. □

## 3. Two exact independent implementations

First run, `frontier-20261028-ph7-three-two-cycle-89-check.py`, **75LF/4103B**, SHA256 `91f30efd4f37826b8e8bd2c3100d3dace779d49d2faebc9ba3862a2efbd2872f`:

    SymPy 1.14.0 Fraction Bernstein PASS: all 3U+2W/V,V spectral graphs excluded at z=8/9
    factor degrees: [(6,3),(30,8),(66,5)]

It derives the coefficient equations, verifies the first resultants against explicit 4-by4 Sylvester determinants, computes the second resultant and exact factorization, then independently verifies all rational Bernstein interval and tail positivity predicates. Certificate `frontier-20261028-ph7-three-two-cycle-89-certificate.json`, **128LF/8922B**, SHA256 `f87456c472e49d1aba6249ef6ef8f0a0ce595ba77bcf0ca98ae4b1da6b9264ff`, contains ALL factor coefficients and subdivision endpoints.

Second run, separately written `frontier-20261028-ph7-three-two-cycle-89-fraction-replay.py`, **115LF/4708B**, SHA256 `bc1488861c9c44183d048daf24c22cbb2b641185609f9d48d70abdafd0ac7148`:

    Independent stdlib Fraction PASS: 181 nested Sylvester evaluations prove degree<=180 identity; all Bernstein/tail signs exact

Without SymPy, it independently derives(EQ32) with rational polynomial arithmetic; interpolates the W coefficients and computes 4-by4 Sylvester determinants at rational points; independently interpolates the V resultants; computes 181 exact 18-by18 rational determinants; parses but never executes the displayed factor polynomials; and rechecks every Bernstein/tail coefficient. Since the outer resultant's U-degree is at most `10*10+8*10=180`, equality of two degree<=180 polynomials at 181 distinct integers establishes(RES32) exactly, including all specializations where a leading coefficient vanishes. This replay consumes the stated factor/subdivision certificate, not a claimed independent mathematical review.

## 4. Scope and next gap

This exclusion covers every at-most-two-valued common escape-rate assignment on the specific 5/7-cycle graph with equal outside rates, even when the two rates occur in arbitrary order. It does NOT cover three or more different common rates, unequal outside rates, the other 13 eight-edge graph shapes, or any graph with at least nine edges. No target 8/9 exclusion, minimum8, positive witness, formal proof, independent reviewer acceptance, or novelty conclusion follows.

The earlier exact positive v4 family below8/9 is not contradicted. Held outputs remain nonpremises and historical process qualifications remain.

END — all two-valued common-rate 5/7-cycle graphs with equal outside rates are exactly excluded at8/9; the unrestricted bridge remains open.
