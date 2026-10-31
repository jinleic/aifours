# Sharper forced numerator-root localization

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** For every box in the explicit 14-endpoint neighborhood of `frontier-20261029-resonant-root-localization-open-v1.md`, every common exact-degree-seven numerator has at least two upper-half-plane roots, counted with multiplicity, at distance less than
\[
\boxed{\frac{91}{500}}
\]
from the imaginary-axis segment \(i[9/10,11/10]\), plus their conjugates. This improves the previously recorded \(197/500\) radius. Every such box is strictly Hurwitz and has a fixed unrestricted common numerator; the localized roots are literal numerator roots, even if cancellation occurs.

Use the conjugate-aware localization criterion in `frontier-20261029-conjugate-aware-root-localization-criterion-v1.md` with \(n=7\), \(k=1\), \(\Delta=1/5\), \(\omega_1=9/10\), and \(R=91/500\). The retained actual denominator \(a\) has phase increment exceeding \(3\pi-3e\), where \(e=796040/3990199\). For no localized upper roots, the refined phase budget is \(3\Delta/R+4\Delta/(2\omega_1)\); for at most one, it is \(\pi+2\Delta/R+3\Delta/(2\omega_1)\). The independent checker verifies both strict rational implications
\[
\begin{aligned}
2\pi_L&>3e+3\Delta/R+4\Delta/(2\omega_1),\\
\pi_L&>3e+2\Delta/R+3\Delta/(2\omega_1),
\end{aligned}
\qquad \pi_L=\frac{281476}{89625}<\pi.
\]
Thus neither case can satisfy the common-SPR phase gap. The root bounds also imply the simpler rectangle
\[
-\frac{91}{500}<\operatorname{Re}z<0,\qquad
\frac{359}{500}<\operatorname{Im}z<\frac{641}{500}
\]
for two upper roots and reflected bounds for their conjugates.

Frozen exact comparisons: `frontier-20261029-resonant-root-localization-sharp-frozen-v1.json`, SHA-256 `a3b737dcc2ac85b2ca14be92c9f447e440f7cf9f2975518e921eab74dbc93d50`. Independent checker `frontier-20261029-resonant-root-localization-sharp-independent-kernel-v1.py`, SHA-256 `f600a36de4d70cc66b29d59868c03ec6c322cad1eb92c6cb7498301c22d6b643`; receipt `frontier-20261029-resonant-root-localization-sharp-independent-result-v1.json`, SHA-256 `a511199ca641a31932b07dd3a71d5238330ca4554ba726bc6b83c7db48a6ff6c`. The general conjugate-aware criterion is SHA-256 `1f3a63233df985092c6578557146c9020f45cef5d66c434e00cb2560f8cd9297`.

Finite inequalities use exact integers and `fractions.Fraction` on one Python Eval host. Phase and rootwise bounds are written mathematics; no formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or unrestricted negative certificate is claimed.
