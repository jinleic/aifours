# Two independent exact constraints in the six-span quotient

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** On the explicit strictly stable box of `frontier-20261029-six-span-two-derivative-sign-open-v1.md`, two different positive actual-atom functionals annihilate the same six-dimensional real endpoint-plus-derivative span and impose **linearly independent** strict constraints on every common numerator. An unrestricted common numerator exists; the constraints are not an unrestricted negative certificate.

Use the full basis of that packet and write
\[
b=v+c_3D^3m+c_4D^4m,\qquad
v\in\operatorname{span}_{\mathbb R}\{E_-(-s^2),E_+(-s^2),sO_-(-s^2),sO_+(-s^2),Dm,D^2m\}.
\]
The independent checker reconstructed two seven-atom functionals \(F_\mathrm{lo},F_\mathrm{hi}\), each with strictly positive integer weights at actual box corners and positive finite frequencies. Each annihilates all six generators exactly, and its quotient values
\[
(x_i,y_i)=(F_i(D^3m),F_i(D^4m))
\]
satisfy \(x_i<0,y_i<0\), with
\[
\frac{y_\mathrm{lo}}{x_\mathrm{lo}}<\frac{267}{100}
<\frac{27}{10}<\frac{y_\mathrm{hi}}{x_\mathrm{hi}}.
\]
The determinant of the two quotient vectors is strictly positive, so these are not repeated or rescaled copies of one constraint. Any common SPR numerator must satisfy both
\[
x_\mathrm{lo}c_3+y_\mathrm{lo}c_4>0,\qquad
x_\mathrm{hi}c_3+y_\mathrm{hi}c_4>0.
\]
The coefficient region satisfying both is nonempty—the previously certified common numerator belongs to it. The two constraints therefore strengthen the tested quotient cone but do not close the original synthesis problem.

Both exact supports, all integer weights and quotient coordinates: `frontier-20261029-quotient-two-direction-cone-frozen-v1.json`, SHA-256 `b265082fe04ac8791abacf64d3a1774e3ce1d33b89b95d71b92c71529c4702ee`. Independent direct-monomial checker `frontier-20261029-quotient-two-direction-cone-independent-kernel-v1.py`, SHA-256 `9c6e819008aeb2babe3655e07f8c3ba3db714b36fa68f1f429da310293a1984f`; receipt `frontier-20261029-quotient-two-direction-cone-independent-result-v1.json`, SHA-256 `06429f0bb4678b9708b2318eb30890fdedbb5e448305c6c9a6c2c638b3539e21`. The underlying basis theorem is SHA-256 `33212b419995b82ef68f488c1128e4816e20d79838d86547e5bc9f3e0bf61786`.

Finite arithmetic used exact integers and `fractions.Fraction` on one Python Eval host. The quotient reasoning is written mathematics; no formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or global no-go claim is made.
