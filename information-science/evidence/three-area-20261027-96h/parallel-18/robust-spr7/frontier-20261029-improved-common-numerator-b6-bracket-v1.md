# A sharper constructive upper bound on the forced numerator coefficient

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel all-parameter exact symbolic replay; not parent adoption.** For every real \(R\ge500\) and \(0\le\rho<1\), the explicit five-contact radial box from `frontier-20261029-unbounded-common-numerator-b6-obstruction-v1.md` (SHA-256 `71896c927bafabc2098ab283bc6108a7b259bda028dc58c948cffb637106f8c7`) has a new common monic numerator \(b_R^*\) satisfying
\[
\boxed{\quad (b_R^*)_6<\frac{20611}{168500}R^2,\qquad
\lim_{R\to\infty}\frac{(b_R^*)_6}{R^2}=\frac{20611}{168500}.\quad}
\]
On the near-boundary boxes \(K_R\), the stronger actual-atom theorem `frontier-20261029-unbounded-b6-strong-lower-v1.md` (SHA-256 `b0cba7cf3305cfb375b1f3eee9739ae8f335a23d2fc9b4f47fb7b0a2ba6206f3`) gives \(b_6>7R^2/80\) for **every** common monic numerator when \(R\ge5000\). Thus this construction is within the uniform factor \(82444/58975<7/5\) of that lower bound. If \(m_6(R)\) is the infimum over all such numerators, the exact asymptotic bracket improves to
\[
\frac8{91}\le\liminf\frac{m_6(R)}{R^2}
\le\limsup\frac{m_6(R)}{R^2}\le\frac{20611}{168500}.
\]
No exact optimal constant or limiting infimum is claimed.

## Explicit determinant construction

Use the predecessor's five boundary contacts and tangent rows \(T\). Let \(b_R\) be its common monic numerator. Define a different degree-six **auxiliary polynomial** \(d_R\) by
\[
d_0=d_6=1,\qquad d_7=0,\qquad
(T_{ij})_{i=1}^5{}_{j=1}^5(d_1,\ldots,d_5)^T=-(T_{i0}+T_{i6})_{i=1}^5.
\]
The coefficient matrix has nonzero determinant for the entire stated range. Set
\[
b_R^*=b_R-\frac{17}{500}R^2d_R.
\]
It is monic of degree seven. The auxiliary \(d_R\) is **not** asserted to be a positive-real direction; subtracting it is justified by the independent full-halfline proof below, not by an unchecked cone argument.

After clearing the two positive Cramer denominators, the five boundary tangent identities and ten contact-factor divisions hold exactly. The residuals for corners 0 and 1 are quintics whose positive \(p_0,p_1,p_2,p_3,p_5\) and strict gap \(4p_3p_5-p_4^2>0\) prove positivity. The corner-2 cubic has positive coefficients. For the remaining quintic write \(p(t)=p_0+t h(t)\), where \(h\) is quartic. Divide twice at \(L=R^2/5\):
\[
h(t)=(t-L)^2(Q_0+Q_1t+Q_2t^2)+v(t-L)+h(L).
\]
The exact proof splits the half-line:

* On \([0,L/2]\), all five degree-four Bernstein coefficients of \(h((L/2)x)\) are strictly positive.
* On \([L/2,\infty)\), the \(Q_j\) are positive. With \(q_{\min}=Q_0+(L/2)Q_1+(L^2/4)Q_2\), one has \(Q(t)\ge q_{\min}>0\) and \(4q_{\min}h(L)-v^2>0\); completing the square yields \(h(t)>0\).

Thus all boundary pairings are nonnegative, with zeros only at their own distinct contact nodes. Their midpoint is strictly positive, and radial interpolation plus affine minimization establishes \(b_R^*\) as a common numerator for every \(\rho<1\). All numerator coefficients are independently checked positive.

The predecessor's \(b_{R,6}/R^2\) is strictly below its own exact asymptotic constant \(1317/8425\) for every \(R\ge100\), proved by a nonnegative shifted-coefficient array with positive constant. Since \((d_R)_6=1\),
\[
(b_R^*)_6=(b_R)_6-\frac{17}{500}R^2
<\left(\frac{1317}{8425}-\frac{17}{500}\right)R^2
=\frac{20611}{168500}R^2.
\]
The corresponding limit is the same exact constant.

## Evidence and scope

Exact symbolic signs and base comparison: `frontier-20261029-improved-common-numerator-frozen-v1.json`, SHA-256 `333d5b76b2bceccfcd6f2a289790ea3ed36e7a572aa55cb47ba278ab938183c9`. Checker `frontier-20261029-improved-common-numerator-independent-kernel-v1.py`, SHA-256 `c8f0d29fc1ff115b713819fafa32c4c9be47dbf61f4fe833339dd91a49ca2673`, reconstructs both determinant systems, five tangencies, ten contact divisions, five interval Bernstein coefficients and **1,640** strictly positive shifted Laurent coefficients for every real \(R\ge500\). Receipt `frontier-20261029-improved-common-numerator-independent-result-v1.json`, SHA-256 `11e8695be398ea43e304cd94b5a6462552d3df3867778c122c9a1eb163bf847d`.

The computations use exact `fractions.Fraction` on one Python Eval host. The positivity split, determinant construction, radial interpolation and asymptotic inference are written mathematics. No formal proof, cross-vendor review, novelty clearance, exact optimum, strict negative-coordinate certificate, or universal original-box verdict is claimed.
