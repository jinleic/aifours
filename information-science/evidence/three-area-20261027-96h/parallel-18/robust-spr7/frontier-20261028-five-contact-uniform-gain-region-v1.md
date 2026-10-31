# A uniform-gain construction on a three-parameter five-contact family

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This proves an explicit continuous family of full-width septic boxes has common numerators all the way to its five-contact stability boundary. It does not claim that the sufficient criterion holds for all five-contact shapes or for arbitrary boxes.

## Boundary family

Let
\[
\lambda\in[2313/2000,1157/1000],\qquad v\in[21/2,11],
\]
and define the four boundary parity endpoints by
\[
\begin{aligned}
E_-&=-\lambda(t-1/2)(t-3)(t-6),&E_+&=-(t-1)(t-2)(t-8),\\
O_-&=-(t-1)(t-6)(t-8),&O_+&=-(t-2)(t-3)(t-v).
\end{aligned}
\]
They determine the independent monic septic endpoint intervals through the parity coefficients. All seven lower endpoints and widths are positive for every parameter in the rectangle: the relevant coefficients are affine in \(\lambda\) or \(v\), and all four parameter-corner checks are strict. Let \(K_{\lambda,v,\rho}\) be the radial subbox with the same midpoint and widths scaled by \(0\le\rho<1\).

At the five markers \(1,2,3,6,8\), the boundary actual corners have contacts \((2,1),(3,2),(1,3),(0,6),(2,8)\). For \(\rho<1\), the parity sign sequence is \((+,+),(-,+),(-,-),(+,-),(+,+),(-,+),(-,-)\) at \(0,1,2,3,6,8,\infty\). Thus all even and odd roots lie in alternating disjoint intervals, and every denominator is strictly Hurwitz. At \(\rho=1\) the displayed contacts are imaginary-axis roots; every larger nested box is ineligible.

## Exact numerator with one gain for the whole rectangle

Use the contact derivative row
\[
d_{ij}=\begin{cases}
E_i'(t_i)(-t_i)^{j/2},&j\text{ even},\\
t_iO_i'(t_i)(-t_i)^{(j-1)/2},&j\text{ odd},
\end{cases}
\]
where \((E_i,O_i)\) denotes the actual corner at contact \(t_i\). Form the \(5\times5\) matrix \(M=(d_{ij})_{j=1}^{5}\), its determinant \(D\), and
\[
r_i=-d_{i0}-1000d_{i6}-d_{i7}.
\]
Let \(M_j\) replace column \(j\) by \(r\). The numerator is the **scaled Cramer vector**
\[
\widetilde b_{\lambda,v,0}=\widetilde b_{\lambda,v,7}=-D,\quad
\widetilde b_{\lambda,v,6}=-1000D,\quad
\widetilde b_{\lambda,v,j}=-\det M_j\ (1\le j\le5).
\]
All eight coefficients are strictly positive on the entire parameter rectangle, so \(-D>0\); division by \(-D\) makes the numerator monic. The gain \(b_6/b_7=1000\) is the **same for every shape**, but the other numerator coefficients depend on \((\lambda,v)\).

Each actual boundary pairing has its contact-square factors; after removing them the residual is strictly positive on the whole half-line. The midpoint pairing is also strictly positive. Consequently \(\widetilde b_{\lambda,v}\) is a common numerator for **every** \(K_{\lambda,v,\rho}\), and no nonzero nonnegative atom combination for any of those boxes can have all coefficient sums nonpositive.

More precisely, the exact bivariate certificate proves the midpoint compactified pairing is at least
\[
m=1437153684857541/40000>0
\]
for the displayed **unnormalized** Cramer vector, uniformly over the rectangle and \(t\ge0\). The maximal \(1+\sum_j u_j\) over the rectangle is \(398379/2000\). Boundary-to-center linearity therefore yields
\[
\operatorname{Re}\frac{\widetilde b_{\lambda,v}(i\omega)}{a(i\omega)}
\ge(1-\rho)\frac{15968374276194900}{17633980849}>0.
\]
The bound is for the unnormalized vector and is not claimed sharp.

## Certificate mechanics and evidence

Every entry of \(M\) is affine in at most the relevant boundary parameter. Cramer's determinants for the numerator have degree at most two in each of \(\lambda,v\), and boundary/center pairing coefficients have degree at most three in each. The contact factors are exact polynomial identities by Cramer's tangent equations. Frequency compactification and Bernstein conversion are linear, so each frequency-leaf coefficient has the same bidegree bound.

The four boundary residuals use 3, 4, 1, 4 compact-frequency leaves; the center uses 4. Together with the eight numerator coefficients they give 110 bivariate parameter polynomials. Every one of their 1,760 degree-\((3,3)\) Bernstein coefficients on the rectangle is strictly positive. Thus the conclusion is a continuum statement, not an interpolation heuristic or a finite sample assertion.

Frozen exact rectangle, gain, partitions, degree bounds and constants: `frontier-20261028-five-contact-uniform-gain-region-frozen-v1.json`, SHA-256 `a27225c9497833060eb442f8435aa61eae12ddf155e7ee4c4ad8308c0cda0f71`. Independent standalone checker `frontier-20261028-five-contact-uniform-gain-region-independent-kernel-v1.py`, SHA-256 `663f7979559c2c9578541e515a278fa76b3eccbe31c47b0271cc2276e29acb8b`, reconstructs boundary widths at all four parameter corners, uses integer Bareiss for all Cramer determinants, uses de Casteljau subdivision in frequency and a separate Vandermonde/power-to-Bernstein parameter conversion, checks all 1,760 strict signs and the ratio constant. Receipt `frontier-20261028-five-contact-uniform-gain-region-independent-result-v1.json` has SHA-256 `acad851a7ffe3bc666ee0127dd92b02b25d90c955593b3f2ed8d7ef7bd0707bc`.

The finite identities use exact integers and `fractions.Fraction` on one Python Eval host; the polynomial-degree, stability and boundary-to-interior conclusions are written arguments. No formal verification, cross-vendor review, novelty clearance or unrestricted septic verdict is claimed.
