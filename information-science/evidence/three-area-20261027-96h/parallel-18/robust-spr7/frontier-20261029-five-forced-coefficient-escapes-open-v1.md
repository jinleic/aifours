# A fifth numerator coefficient must exceed the denominator interval

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel independent exact replay; not parent adoption.** This strengthens `frontier-20261029-four-forced-coefficient-escapes-open-v1.md` (SHA-256 `9dea60cbbc82ef37ee3fb2bba3501dac2581f7fdbd6d472a63d45508e5e8df76`). On the same actual full-width stable septic box, which has a separately certified unrestricted common numerator, every common monic numerator must obey
\[
\boxed{b_2>11000,\quad b_3>211000,\quad b_4>1000000,\quad b_5>2150,\quad b_6>909.}
\]
Thus **five** distinct numerator coefficients \(b_2,\ldots,b_6\) must strictly exceed their own original denominator upper endpoints; no coefficient is fixed or restricted in advance. In particular the new upper endpoint is \(\overline a_2=40480640097626799/4000000000000<11000\).

## Independent sixth-atom certificate

A different set of six actual positive-frequency corner atoms, with the explicit positive integer weights in `frontier-20261029-fifth-forced-coefficient-escape-frozen-v1.json`, has aggregate monomial vector
\[
C=(C_0,0,C_2,0,C_4,0,0,-11000C_2),\qquad C_0<0,\ C_2>0,\ C_4<0.
\]
Every common numerator is Hurwitz with strictly positive coefficients by the homotopy argument in the predecessor. Strict positivity of its six atom pairings therefore gives
\[
0<C\cdot b\le C_2(b_2-11000b_7),
\]
so \(b_2>11000b_7\). The numerical certificate is a necessary positive-coordinate bound, not an all-negative vector. Together with the four independently frozen prior certificates it yields the displayed five simultaneous bounds.

## Explicit open persistence

In the same 14-endpoint radius \(10^{-10000}\), use these six fixed corner/frequency pairs. Keep two positive nonpivot weights fixed and solve four nonzero-pivot Cramer equations to keep \(C_1=C_3=C_5=C_6=0\). The independent replay verifies the zero-row rank 4, positivity of all four anchor pivot weights, strict negativity of \(C_0,C_4\), and strict slack \(C_7+10500C_2<0\). The common denominator of the anchor rows is less than \(10^{48}\), and every relevant Cramer or augmented matrix has dimension at most 5. Its entries and changes are bounded by \(10^{251}\) and \(10^{241}\epsilon\), respectively, using the same argument as in the predecessor, now with all squared frequencies below 3000. The exact replay checks
\[
6!\,6\,10^{251\cdot5+241}\epsilon<\tfrac12D^{-6}.
\]
All required signs and weights therefore persist, proving \(b_2>10500b_7\) for every perturbed box. This is still strictly above every perturbed \(\overline a_2\). The four predecessor bounds persist with their recorded weakened thresholds on the same neighborhood, which is contained in the independently certified stable, common-numerator neighborhood. Consequently all five coefficient escapes hold for every box there.

Frozen atoms: `frontier-20261029-fifth-forced-coefficient-escape-frozen-v1.json`, SHA-256 `d680463d33272b2a25b7bb74ad74ae2682a79eb97d04c7bd5a01b3a4e1fad313`. Open parameters `frontier-20261029-fifth-forced-coefficient-escape-open-frozen-v1.json`, SHA-256 `ebfb49a7aea63a0975978bdb018d467f7e7204e430e051ec1c7cfaa79172aa9a`; independent signed-monomial/Cramer replay `frontier-20261029-fifth-forced-coefficient-escape-open-independent-kernel-v1.py`, SHA-256 `d1113ae714b8d58709d00ca89e4d1e93bcb56fe1839148d36858584425ae03de`; receipt `frontier-20261029-fifth-forced-coefficient-escape-independent-result-v1.json`, SHA-256 `e7956f88950553e45cad73494236de1ab53c65dc04719d776a528031f95946ce`.

Finite computations use exact integers/`fractions.Fraction` in one Python Eval host; the stability, Hurwitz-coefficient, homotopy and determinant arguments are written mathematics. No formal proof, cross-vendor review, novelty clearance, all-negative-coordinate certificate or universal original-box verdict is asserted.
