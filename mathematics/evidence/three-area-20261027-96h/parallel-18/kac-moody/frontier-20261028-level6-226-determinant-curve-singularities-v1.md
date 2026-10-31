# Three exact rational singularities of the level-six determinant curve

**MathKacMoody-2 / math-3.** Native observation before this additive write: **Wed Oct 28 20:00:13 PDT 2026**. New exact symbolic/rational obstruction to ONE proposed smooth-curve proof route; independent scientific review and parent decision remain pending. Not a map kernel, F6/B6, formal/human/independent-model, novelty or priority verdict.

## 1. Exact singular points and tangent cones

Let `R(x,y)` be the explicit 253-term total-degree21 integer polynomial in the independently replayed factorization of the actual level-six `(2,2,6)` selected determinant, as pinned in `frontier-20261028-level6-226-generic-density-one-candidate-v1.md` SHA `8a4ac80a3131f3ddcdc8568da32a5fafe10dea1bda823f7bc52100a640d41d38`. Direct exact integer evaluation of R and both first partial derivatives gives THREE rational affine singular points:

    (-5,-5),  (-6,-6),  (-4,-5).

All have negative coordinates, outside the original physical `x=r-6>=0,y=s-6>=0` region. In local coordinates `U=x-a,V=y-b`, the first nonzero homogeneous terms are:

|point|multiplicity|exact lowest homogeneous term|
|---|---:|---|
|(-5,-5)|2|`286978140 U^2`|
|(-6,-6)|4|`-6531840000(8278 U^4+78878 U^3V-383037 U^2V^2-189922 UV^3-11447 V^4)`|
|(-4,-5)|2|`-72(221760 U^2+2382515 UV+229152 V^2)`|

For `(-4,-5)`, the quadratic discriminant is exactly `5473110735145 != 0`, so the two tangent lines are distinct over an algebraic closure. For `(-6,-6)`, the displayed quartic is squarefree as a binary form: its univariate specialization at V=1 has nonzero resultant with its derivative and its U^4 coefficient is nonzero. No classification of the repeated tangent at `(-5,-5)` is asserted.

## 2. Exact consequence for the smooth-plane-genus route

The affine rational singularities imply that the degree21 projective curve defined by R is NOT smooth over characteristic zero. In particular one cannot apply the smooth-plane formula to claim its geometric genus is `190=(21-1)(21-2)/2`, and the conditional density-one/Hilbert irreducibility result does not by itself imply that only finitely many determinant-zero pairs exist. Singularities outside the physical quadrant are still singularities of the global projective curve.

The integer polynomial R has coefficient content1; its degree-y leading coefficient is `2107392`, nonzero modulo13 and5. Since R,R_x,R_y vanish at the three integer points, their reductions are affine singular points of the corresponding projective reductions. The earlier p5 bounded modular Jacobian-Groebner scout returned `NOT_A_SMOOTHNESS_CERTIFICATE_AT_THIS_PRIME`; it is consistent with, but not the proof of, the stronger exact characteristic-zero singularities. A p13 smoothness scout was launched and then **cancelled** immediately after the exact rational singularities were observed, because a smooth-mod13 route was thereby impossible; no p13 result or completed verdict is claimed.

This does NOT establish the genus of the NORMALIZATION, rule out a genus>=2/Faltings route after a complete singularity/delta analysis, or establish infinitely many physical integer points. It is a reason to replace the naive smooth-plane argument by a genuine normalization/genus or other Diophantine method, not a reason to assert such a method cannot succeed.

## 3. Exact certificates and independent replay

`frontier-20261028-level6-226-curve-singular-points.py`, 61LF SHA `05e02e22f693f79187a923dd3c55a97094d079896f0bda78ab470ba4a0a657d3`, computes each Taylor coefficient using exact integer binomial sums, verifies every lower-order coefficient vanishes, and checks the nonzero quadratic discriminant and quartic/derivative resultant. Its 44LF output `frontier-20261028-level6-226-curve-singular-points-v1.json` has SHA `4496ce58c31ab70591882f4b14827772a801174f5d2476adc9285e178ea16f36` and returned PASS at **19:59:49 PDT**.

The separately authored `frontier-20261028-level6-226-curve-singular-points-independent-replay.py`, 34LF SHA `b5b0907a98a001c51d354cb7ef7c62cefacd20061cb7e86028509509c3110192`, constructs the polynomial in SymPy, directly differentiates at each point, verifies the whole displayed tangent terms, nonzero quadratic discriminant and quartic gcd. Its 24LF result `frontier-20261028-level6-226-curve-singular-points-independent-replay-v1.json`, SHA `cf3372586af83bdcd676d76e9645b40210706c1a1dad4f1732610a5d138292cc`, returned PASS at **Wed Oct 28 20:00:13 PDT 2026**. The earlier p5 scout output is 24LF SHA `002c53846230039cd9b9cfa41653de7b66b7eb6c5351483898a5ad0d60896238`. These are exact integer/rational computations, not human/formal/independent-model verification.

The singularities lie at formal determinant-factor coordinates and do NOT give zeros of the full D3 map, non-Serre elements or integer parameter counterexamples. The named HIT density-one candidate, full quadrant question, parent F5/B4 reviews, prior incidental cone-status exposure and all ZERO/STOP/HOLD/process findings are unchanged.

**END — exact singular-curve obstruction; normalized genus and remaining physical parameters open.**
