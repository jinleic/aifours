# Every box in the family has an unbounded monic solution ray

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel all-parameter symbolic replay; not parent adoption.** For every real \(R\ge100\) and every interior radial factor \(0<\rho<1\) of the five-contact boundary in `frontier-20261029-unbounded-common-numerator-b6-obstruction-v1.md` (SHA-256 `71896c927bafabc2098ab283bc6108a7b259bda028dc58c948cffb637106f8c7`), there is an explicitly defined monic degree-six polynomial \(c_R\) such that
\[
b_{R,\tau}=b_R+\tau c_R,\qquad \tau\ge0,
\]
is a common **monic degree-seven** SPR numerator for the entire box. Here \(b_R\) is the predecessor's explicit common numerator. In particular \((b_{R,\tau})_6=(b_R)_6+\tau\), so the monic solution set is unbounded for **each** such box. In fact every one of its seven nonleading coefficients tends to \(+\infty\) along this ray, since \(c_0,\ldots,c_6>0\).

This combines with the predecessor's result: on its near-boundary boxes, \(b_6\) is bounded strictly **below** by order \(R^2\) for every common numerator, but the feasible monic coefficient \(b_6\) has no upper bound. Monic normalization does not make the feasible solution set compact. The degree-six direction is **not** called SPR under the equal-degree definition: only the resulting degree-seven ray members are.

## Construction of the degree-six direction

Use the same boundary corners, five contact pairs and tangent rows \(T_{ij}\) as the predecessor. Let
\[
A_6=(T_{ij})_{i=1}^5{}_{j=1}^5,\quad D_6=-\det A_6,\quad
c_0^\partial=E_+(0)/2,\quad c_6^\partial=1,\quad c_7^\partial=0,
\]
and let \(h_i=-(T_{i0}c_0^\partial+T_{i6})\). For \(j=1,\ldots,5\), define
\[
c_j^\partial=-\frac{\det A_6[j\leftarrow h]}{D_6}.
\]
The exact replay proves \(D_6>0\), \(c_0^\partial,\ldots,c_6^\partial>0\), and all five tangent identities. Set \(c_R=c^\partial\).

For each boundary corner the pairing with \(c_R\) is the square of the same contact factor(s) listed in the predecessor times a strictly positive residual. The four residual degrees are \(4,4,2,4\). The checker proves positivity over the full half-line as follows:

* Corner 0: \(p_0,p_2,p_3,p_4>0\) and \(4p_0p_2-p_1^2>0\), so the quadratic \(p_0+p_1t+p_2t^2\) is positive.
* Corner 1: all five residual coefficients are positive.
* Corner 2: all three residual coefficients are positive.
* Corner 3: write its quartic as \(p_0+t h(t)\), divide \(h\) twice by \(t-L\), and obtain
  \(h(t)=(t-L)^2(Q_0+Q_1t)+v(t-L)+h(L)\). The replay proves \(p_0,Q_0,Q_1>0\) and \(4Q_0h(L)-v^2>0\), so completing the square gives \(h(t)>0\) for all \(t\ge0\).

The ten contact divisions are exact. Boundary pairings are nonnegative and at each finite \(t\) at least three corners give strictly positive pairings. Their midpoint is strictly positive; radial interpolation therefore makes every actual corner pairing strictly positive for \(\rho<1\), and affine minimization covers the whole independent box. The same reasoning gives a strictly positive limit when the pairing is divided by \((1+t)^6\). Thus adding \(\tau c_R\) preserves all finite-frequency pairings, while the normalized degree-seven infinity gain remains 1.

For each fixed \(R\) and \(0<\rho<1\), the degree-six and degree-seven compactified pairings both have positive margins. Endpoint clipping and homotopy as in `frontier-20261029-unbounded-b6-open-neighborhood-addendum-v1.md` therefore give a nonempty 14-endpoint open neighborhood on which the **same entire ray** remains common and all boxes stay Hurwitz. No radius uniform in \(R\) or \(\rho\) is claimed.

## Evidence and scope

Exact sign arrays `frontier-20261029-unbounded-solution-ray-frozen-v1.json`, SHA-256 `e7d99fe3ca90cfb0d2f31d86b5942c0c071b976ccd9c315ebc245689bb276039`. Checker `frontier-20261029-unbounded-solution-ray-independent-kernel-v1.py`, SHA-256 `9deff54bef11c750d0310e6f1b46d94ab5dd8a5f7c6306c88f760454b85685af`, reconstructs the determinants, five tangent identities and ten exact divisions, and checks all **627** shifted Laurent coefficients strictly positive for every real \(R\ge100\). Receipt `frontier-20261029-unbounded-solution-ray-independent-result-v1.json`, SHA-256 `1a73fa85ee3b6b4c25bc24f004b6b45e043d90cd0aedac24c192d3f28c845145`. Exact arithmetic is `fractions.Fraction` on one Python Eval host; compactness, half-line inequalities and homotopy are written deductions. No formal proof, cross-vendor review, novelty clearance, all-negative certificate or arbitrary-box verdict is claimed.
