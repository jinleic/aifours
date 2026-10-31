# A stable reciprocal-derivative family can have an unstable interval hull

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This is a precise obstruction to applying a monic sextic **interval-box** theorem to a correlated transformed family by taking its naive coordinatewise hull. It is not an SPR counterexample.

For a monic Hurwitz septic \(p(s)=\sum_{j=0}^7a_js^j\), the reciprocal-derivative operator
\[
V p=7p-sp'=\sum_{j=0}^6(7-j)a_js^j
\]
is a Hurwitz sextic: it is the reciprocal of the derivative of the reciprocal septic. Its leading coefficient is \(a_6>0\), so the monic normalized transform is
\[
q_j=\frac{(7-j)a_j}{a_6}\quad(j=0,\ldots,5),\qquad q_6=1.
\]
If the septic coefficients vary independently in positive intervals \([\ell_j,u_j]\), the coordinatewise interval hull of the normalized images has bounds
\[
q_j\in\left[\frac{(7-j)\ell_j}{u_6},\frac{(7-j)u_j}{\ell_6}\right].
\]
The common denominator \(a_6\) makes the actual image correlated; all hull corners need not be attainable.

Take the previously certified five-contact box at \(\rho=3/4\). It is all-member Hurwitz and has the explicit common septic numerator in `frontier-20261028-five-contact-all-eligible-scales-v1.md`. Nevertheless, the actual parity corner \((E_-,O_+)\) of the **normalized sextic interval hull** is the polynomial with ascending coefficients
\[
\left(\frac{531909}{7778},\frac{1308150}{3487},\frac{1779975}{13948},
\frac{836190}{3889},\frac{451041}{15556},\frac{108585}{3487},1\right),
\]
and its fourth leading Hurwitz determinant is exactly
\[
-\frac{3359511916883446081860294075}{35776978374150430625296}<0.
\]
Thus the normalized rectangular hull is not robustly Hurwitz, even though **every actual normalized transform** is Hurwitz.

The offending hull corner is not an actual image: attaining its minimal \(q_0\) requires \(a_0=\ell_0\) and \(a_6=u_6\), while attaining its maximal \(q_2\) requires \(a_2=u_2\) and \(a_6=\ell_6\). The original box has \(\ell_6<u_6\), so those requirements conflict. Therefore neither the unstable hull corner nor its failure may be treated as an actual transformed denominator or as a negative certificate.

Frozen original and hull endpoints, corner polynomial and determinant: `frontier-20261028-reciprocal-derivative-interval-hull-frozen-v1.json`, SHA-256 `ff50db82bd86d6fecfd28caf4ef6e7dc8d30f60cdacf5ccdd73a8d3c0f4358d3`. Standalone replay `frontier-20261028-reciprocal-derivative-hull-independent-kernel-v1.py`, SHA-256 `1109474b560333698c7f2f55392e893b3f533a9828d5a7f1f53751477d2b0345`, reconstructs the original box and hull, checks all 28 original corner Hurwitz minors, the negative hull minor, the shared-denominator endpoint conflict and a positive actual-center control. Receipt `frontier-20261028-reciprocal-derivative-hull-independent-result-v1.json` has SHA-256 `5c42340c5c9685b2ec7252afb8f4658521857e624ae5f952e0a7bc61cce8af98`. The negative minor was also matched by integer Bareiss in the producing Eval kernel.

The conclusion that every actual transform is Hurwitz uses the written reciprocal/Gauss–Lucas argument; all-member stability of the original box is from its separately replayed five-contact certificate. Exact finite arithmetic used one Python Eval host. No formal verification, cross-vendor review, novelty clearance or unrestricted septic verdict is claimed.
