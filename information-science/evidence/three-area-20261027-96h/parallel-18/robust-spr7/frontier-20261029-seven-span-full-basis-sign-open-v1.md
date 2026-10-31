# A forced negative coefficient in a full eight-dimensional basis

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** In the explicit stable box of `frontier-20261029-seven-dimensional-span-obstruction-open-v1.md`, every common SPR numerator has a **strictly negative coefficient on \(D^4m\)** in a full basis consisting of the four parity endpoints and the first four midpoint derivatives. The statement persists on an explicit 14-dimensional endpoint neighborhood. A different unrestricted common numerator exists throughout; no global negative certificate is claimed.

Let the four actual parity endpoint generators be \(g_0,\ldots,g_3\), and let \(m\) be the monic coefficient midpoint. The eight polynomials
\[
(g_0,g_1,g_2,g_3,Dm,D^2m,D^3m,D^4m)
\]
form a basis of the real degree-at-most-seven polynomial space: their exact coefficient-matrix determinant is
\[
-\frac{20402691558685462688650499072600057407876412402245776546821283}
{1000000000000000000000000000000000000}\ne0.
\]
The eight positive actual atoms in the companion packet define \(F\), which annihilates the first seven generators exactly. The independent replay verifies \(F(D^4m)<0\). Thus the unique expansion
\[
b=\sum_{j=0}^3c_jg_j+c_4Dm+c_5D^2m+c_6D^3m+c_7D^4m
\]
of a common SPR numerator must satisfy \(F(b)=c_7F(D^4m)>0\), hence \(c_7<0\). This is a basis-coordinate necessity; \(F\) is not an all-negative monomial-coordinate certificate.

Perturb all 14 endpoints by at most \(\varepsilon=10^{-425}\). This is inside the companion's \(10^{-370}\) stable neighborhood. Recompute all generators from each perturbed box. The positive cofactor weights of the seven-generator atom matrix remain positive, and their weighted \(D^4m\) sum remains strictly negative: the checker verifies cofactor changes \(<10^{367}\varepsilon\), cofactor magnitudes \(<10^{375}\), derivative-row magnitudes \(<10^{53}\), derivative-row changes \(<10^{44}\varepsilon\), and total weighted-sum change \(<10^{422}\varepsilon\), smaller than half the exact anchor margin. The eight-basis determinant changes by less than \(10^{102}\varepsilon\), below half its nonzero anchor magnitude. Thus the moving basis and forced sign survive. The companion theorem separately supplies the same fixed unrestricted common numerator for every perturbed box.

Frozen sign and determinant: `frontier-20261029-seven-span-full-basis-sign-frozen-v1.json`, SHA-256 `2850b3c4a82dfe7d0d4ab367d3e1e983328747499f7aa9a9ab58b67f7021906d`. Frozen open bounds: `frontier-20261029-seven-span-full-basis-sign-open-frozen-v1.json`, SHA-256 `25ae65e5d7952f86f52002755051166fa6ec50d7669cacd95fd234cfc69e3442`. Independent checker `frontier-20261029-seven-span-full-basis-sign-open-independent-kernel-v1.py`, SHA-256 `e9e092f16bfc783fff09d96dfed7092b22ba5af9cb366a0878a7cfa7b2c5eca1`; receipt `frontier-20261029-seven-span-full-basis-sign-open-independent-result-v1.json`, SHA-256 `66ef2f6ef4c986117d5bf1035e0a48c3bd7365c8b267c0b30eb19fb9478f0206`.

All finite calculations use exact integers and `fractions.Fraction` on one Python Eval host; basis, cofactor and perturbation deductions are written mathematics. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or unrestricted negative certificate is claimed.
