# An exact positive direction and the full feasible b6 interval

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel all-parameter symbolic replay; not parent adoption.** The auxiliary degree-six polynomial \(d_R\) in `frontier-20261029-improved-common-numerator-b6-bracket-v1.md` (SHA-256 `2bbe8cb950b27870cfceac1f11683eaee1f920ddd71c683c2b5883c56412f58b`), previously not asserted to be a positive direction, **is** such a direction for every \(R\ge100\) and every interior radial factor \(0<\rho<1\). It has
\[
d_0=d_6=1,\quad d_7=0,\quad d_1,\ldots,d_5>0,
\]
and its pairing with every actual denominator is strictly positive at every finite frequency, with a positive limit after division by \((1+t)^6\). Under the original equal-degree definition, \(d_R/a\) itself is **not** called SPR.

For \(R\ge500\), the predecessor's improved common monic numerator therefore generates the entire feasible ray
\[
b_R^*+\tau d_R,\qquad \tau\ge0.
\]
The resulting polynomials remain monic degree seven and common SPR; their \(b_6\) values are exactly \((b_R^*)_6+\tau\). In particular every \(b_6\ge(b_R^*)_6\) is achieved by an explicit common numerator, and all seven nonleading coefficients diverge along the ray.

## Exact shape of the one-coordinate projection

For any fixed compact stable box in this family, let \(m_6\) be the infimum of \(b_6\) over common monic numerators. The set of **all** achievable \(b_6\) values is precisely
\[
\boxed{(m_6,\infty).}
\]
To see this, the set is nonempty and \(m_6\ge0\) because common numerators are Hurwitz. For any \(x>m_6\), the definition of infimum supplies a common numerator with \(b_6<x\); adding \((x-b_6)d_R\) gives a common numerator with exactly \(b_6=x\). The endpoint cannot be attained: any monic common numerator has a uniform positive compactified pairing margin over the compact box and frequency interval. A sufficiently small negative perturbation of its \(s^6\) coefficient preserves the margin and hence common SPR, contradicting minimality. Thus there is no minimizing numerator, even though every larger value is attainable. For the near-boundary family, the pinned lower and improved upper bounds give a nonvacuous explicit bracket for \(m_6\); its exact value remains open.

## Exact proof of the positive direction

The independent symbolic checker reconstructs the same tangent Cramer system as the predecessor, now with \(d_0=d_6=1\). The five tangent identities and ten contact-square divisions are exact. At boundary corners 0, 1 and 2 every residual coefficient is strictly positive. At corner 3, write the quartic residual as \(p_0+t h(t)\), and divide the cubic \(h\) twice at \(L=R^2/5\):
\[
h(t)=(t-L)^2(Q_0+Q_1t)+v(t-L)+h(L).
\]
The replay proves \(p_0,Q_0,Q_1>0\) and \(4Q_0h(L)-v^2>0\), so \(h(t)>0\) by completing the square. Boundary pairings are nonnegative and at every finite \(t\) at least three are strictly positive; the midpoint and every radial corner with \(\rho<1\) are strictly positive. The degree-six normalized infinity limit is positive as well. Affine minimization extends the pairing to the entire box.

The frozen `frontier-20261029-unit-endpoint-direction-frozen-v1.json`, SHA-256 `7e28c59115a6d224818d441b54cce32201a7895d6c8105601360be8408088254`, records **600** strictly positive shifted Laurent coefficients in 26 sign polynomials. Independent checker `frontier-20261029-unit-endpoint-direction-independent-kernel-v1.py`, SHA-256 `8c76145ad0c98960863b61ae7e1dfcc49fd35a89b951792fe473b2ba3aaaf8cf`, reconstructs them, the five tangencies and all ten divisions; receipt `frontier-20261029-unit-endpoint-direction-independent-result-v1.json`, SHA-256 `afe0ef06f9ce4e1f74ec63d0f8972c60478bc2ed705406953149c81031476716`.

Arithmetic uses exact `fractions.Fraction` on one Python Eval host. The open-margin, infimum and affine-pairing arguments are written mathematics. No exact value of \(m_6\), formal proof, cross-vendor review, novelty clearance, or original arbitrary-box verdict is asserted.
