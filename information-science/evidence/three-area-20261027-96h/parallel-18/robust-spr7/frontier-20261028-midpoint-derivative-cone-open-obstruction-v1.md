# A robust obstruction to all positive midpoint-derivative constructions

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** For an explicit strictly stable septic interval box, **no nonzero nonnegative linear combination of its midpoint polynomial and its seven formal derivatives** is a common SPR numerator, even though a different common numerator exists. The obstruction holds throughout a nonempty 14-dimensional endpoint neighborhood, with each perturbed box using its *own* midpoint. It rules out a concrete and fairly broad positive-operator strategy, not unrestricted common SPR.

## Four-atom certificate

Use the independently stable box \(K\) and the explicit unrestricted common numerator in `frontier-20261028-sturm-band-anisotropic-box-synthesis-v1.md`. Let \(m\) be the monic coefficientwise midpoint and \(D=d/ds\). The four actual atom combinations are
\[
\begin{array}{c|c|r}
\text{denominator corner}&t=\omega^2&\text{positive weight}\\\hline
a_{--}&147/4&10000000000\\
a_{-+}&428/3&25600000000\\
a_{+-}&196/3&19900000000\\
a_{+-}&32768/3&93
\end{array}
\]
Let \(F(b)\) be their weighted sum of \(P_{a,b}(t)\). Exact monomial accumulation gives
\[
F(m^{(k)})<0\qquad(k=0,1,\ldots,7).
\]
All eight exact rational values are pinned in the frozen data. Hence for every nonzero vector \(c_k\ge0\),
\[
F\!\left(\sum_{k=0}^{7}c_k m^{(k)}\right)<0.
\]
A common SPR numerator would instead make each positive-weight atom strictly positive. Therefore no numerator in this cone works; in particular no \(m(s+h)\), \(h\ge0\), and no \(\prod_i(I+h_iD)m\), \(h_i\ge0\), works. This is a statement about the **midpoint of this box**, not about all possible base polynomials or all differential operators.

The anchor box's independently certified unrestricted numerator has
\[
F(b)=\frac{217577215195744579746232769975466874705989091}
{1528823808000000}>0.
\]
The negative sums are in the derivative-generator basis; they are **not** claimed to be negative in the original monomial coefficient basis. Thus there is no contradiction with that positive result and no unrestricted negative certificate.

## Persistence for perturbed midpoints

Perturb all 14 endpoints independently by at most \(\varepsilon=10^{-14}\). The separately pinned neighborhood theorem `frontier-20261028-sturm-band-no-family-open-neighborhood-v1.md` proves every resulting box remains strictly stable and shares the anchor's fixed unrestricted numerator. Let \(m'\) be the *new* box midpoint and use the four corresponding actual parity corners at the same weights and frequencies.

Both each corner coefficient and each midpoint coefficient move by at most \(\varepsilon\); the monic leading coefficients do not move. For each \(k\), a direct bilinear monomial expansion gives
\[
|F_{K'}(D^km')-F_K(D^km)|\le\varepsilon A_k,
\]
where, with \((j)_k=j!/(j-k)!\) and \(H_\ell=h_\ell+1\) for \(\ell\le6\), \(H_7=1\),
\[
A_k=\sum_iw_i\!\left[
\sum_{\ell=0}^{6}\sum_{j=k}^{7}
\mathbf1_{\ell+j-k\,\mathrm{even}}(j)_k|m_j|t_i^{(\ell+j-k)/2}
+\sum_{\ell=0}^{7}\sum_{j=k}^{6}
\mathbf1_{\ell+j-k\,\mathrm{even}}(j)_kH_\ell t_i^{(\ell+j-k)/2}
\right].
\]
The independent arithmetic replay verifies \(2\varepsilon A_k\le-F_K(D^km)\) for all eight \(k\). Thus every perturbed derivative-generator sum remains strictly negative, and the same finite certificate excludes its entire nonnegative midpoint-derivative cone. The endpoint neighborhood and its fixed positive numerator are as in the cited theorem, not a new unrestricted counterexample.

Anchor support, weights and eight exact negative values: `frontier-20261028-midpoint-derivative-cone-obstruction-frozen-v1.json`, SHA-256 `016e97ece7973285b69ba9275e87580e7b23f6fd0816e120b3dd854470f86c22`. Robust bounds: `frontier-20261028-midpoint-derivative-cone-open-frozen-v1.json`, SHA-256 `66ff7a206699e75007704ee6b36a520489d66542d1c0c43478e38b8bfb8931d8`. Independent checker `frontier-20261028-midpoint-derivative-cone-open-independent-kernel-v1.py`, SHA-256 `0c056f5bdbd3bd0c72cf990d988beea47aa593cda20cc7d85e06098894ed639a`; receipt `frontier-20261028-midpoint-derivative-cone-open-independent-result-v1.json`, SHA-256 `7e29ebd753239a59ae0749828a74334792f53ee5e5daaa7d6c2ca9bbb8838819`.

The finite arithmetic used integers and `fractions.Fraction` on one Python Eval host; perturbation and cone deductions are written mathematics. No formal verification, cross-vendor review, novelty clearance, universal positive conclusion, or unrestricted negative certificate is asserted.
