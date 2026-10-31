# Two atoms rule out every midpoint-parity rescaling

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** For the explicit strictly stable box in `frontier-20261029-six-dimensional-endpoint-derivatives-open-obstruction-v1.md`, let its monic midpoint be \(m(s)=E_m(-s^2)+sO_m(-s^2)\). No numerator of the form
\[
\beta(s)=xE_m(-s^2)+y\,sO_m(-s^2),\qquad x>0,\ y\in\mathbb R,
\]
can be common SPR. This excludes **every** positive relative parity gain, not only one chosen gain; the already verified different unrestricted numerator still works.

Use the actual corner \(a_{--}\) at \(t=55/9\) with weight \(3101004199710441\), and the actual corner \(a_{+-}\) at \(t=17/15\) with weight \(22320471051484375\). For their weighted pairing sum \(F\), independent direct monomial calculation gives
\[
F(E_m(-s^2))=-\frac{21369791987759672418908024156}{333073265625}<0,
\qquad F(sO_m(-s^2))=0.
\]
Hence \(F(\beta)<0\) for every \(x>0\) and every real \(y\), whereas common SPR would make both positive-weight pairings strictly positive. The explicit unrestricted numerator \(b\) from the cited packet instead has
\[
F(b)=\frac{18459694655539849450310225849582273}{4667059995637500}>0.
\]
Thus this two-atom certificate is a genuine obstruction to the midpoint-parity scaling construction, not a negative-coordinate certificate against arbitrary numerators. (For monic common SPR, \(x>0\) follows from \(\beta(0)>0\) and \(E_m(0)>0\).)

Frozen exact atoms and values: `frontier-20261029-midpoint-parity-scaling-frozen-v1.json`, SHA-256 `5ad79a97bd9568a80cadfc9eb46a46ef99cc12b776154cc09694454c9cde7ef6`. Independent checker `frontier-20261029-midpoint-parity-scaling-independent-kernel-v1.py`, SHA-256 `11c5a5c2240c7e855335912c5c3ac3a52c682bb46ebcd10007b234fcceb8806e`; receipt `frontier-20261029-midpoint-parity-scaling-independent-result-v1.json`, SHA-256 `98aa4ea1391a01372ca3254a01ccefa7050be88c8571806ba9a073b57365352f`. The checker also replays all 28 strict Hurwitz minors and 256 strict positive pairing coefficients for the known good numerator.

Finite arithmetic is exact integer/`fractions.Fraction` work on one Python Eval host. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or unrestricted negative certificate is claimed.
