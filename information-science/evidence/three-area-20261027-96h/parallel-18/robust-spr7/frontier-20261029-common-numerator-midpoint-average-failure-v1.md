# A common numerator cannot always be averaged halfway to the midpoint

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** In the explicitly stable septic box of `frontier-20261029-six-dimensional-endpoint-derivatives-open-obstruction-v1.md`, the monic numerator \(b\) displayed there is common SPR, and the monic coefficient midpoint \(m\) is itself a denominator in the box. Nevertheless their average \((b+m)/2\) is **not** common SPR.

At the actual \((E_+,O_-)\) corner \(a_2\) and \(t=\omega^2=101/100\), direct exact monomial accumulation gives
\[
P_{a_2,b+m}(101/100)
=-\frac{14414509265575286138071525621}
{6487362774000000000000000000}<0.
\]
The average's pairing is half this value. Hence the convex set of common numerators, although containing \(b\), need not contain the halfway point toward a particular denominator-family midpoint. This rules out that simple averaging step; it does **not** rule out a different midpoint-mixing weight, a different common numerator, or all common numerators. The box demonstrably has one.

The independent checker also replayed all 28 strict corner Hurwitz minors and all 256 strict Bernstein coefficients for the original \(b\), before evaluating the mixed numerator. Frozen witness `frontier-20261029-common-numerator-midpoint-average-failure-frozen-v1.json`, SHA-256 `4e9779610cef9859e2203b0560d1c632bdf32247b4d056efa36553913ed99f4f`; checker `frontier-20261029-common-numerator-midpoint-average-failure-independent-kernel-v1.py`, SHA-256 `eef254e4dcb19dd0e49f2bd23ca2cc2b069376ea6666b7f42e562ca5ab86e62f`; receipt `frontier-20261029-common-numerator-midpoint-average-failure-independent-result-v1.json`, SHA-256 `ff64f8c4ef24fcfe17b3cf7616f37a104fbb77b3153e79bb393db3a55c4d4224`.

All finite arithmetic uses exact integers and `fractions.Fraction` on one Python Eval host. Kharitonov and affine corner minimization are written imports; no formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or unrestricted negative certificate is claimed.
