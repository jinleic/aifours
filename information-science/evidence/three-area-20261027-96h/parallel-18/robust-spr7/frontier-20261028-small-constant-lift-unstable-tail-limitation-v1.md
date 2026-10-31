# The stable-tail condition is not automatic for stable septic boxes

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This is a precise limitation of the small-constant lifting theorem, not a counterexample to common septic SPR synthesis.

Consider the explicitly Hurwitz septic
\[
p_*(s)=(s+1)\prod_{v\in\{4,5,6\}}((s+1)^2+v^2),
\]
with ascending coefficients
\[
(16354,20420,6419,2681,420,98,7,1).
\]
Its monic sextic tail \(q_*(s)=(p_*(s)-p_*(0))/s\) has ascending coefficients
\[
(20420,6419,2681,420,98,7,1).
\]
The fifth leading Hurwitz determinant of \(q_*\) is exactly \(-1933582924\), independently computed by rational Gaussian elimination and integer Bareiss. Hence \(q_*\) is not Hurwitz, although \(p_*\) is strictly Hurwitz by its displayed factorization.

This is not just a degenerate singleton. Form a monic septic interval box by varying each of the seven lower coefficients of \(p_*\) independently by \(\pm10^{-9}\). Every width is positive. The whole box is strictly Hurwitz and has the common numerator \(b=p_*\). Indeed, exact rational Bernstein leaves give
\[
\frac{|p_*(i\sqrt t)|^2}{(1+t)^7}\ge \frac{20885}{3670016},\qquad
\sum_{j=0}^7|p_{*,j}|=46400.
\]
The compact perturbation theorem therefore gives the strict box pairing bound
\[
\frac{P_{a,b}(t)}{(1+t)^7}\ge
\frac{20885}{3670016}-7\cdot10^{-9}\cdot46400
=\frac{1538513969}{286720000000}>0.
\]
The same bound on the straight homotopy to the center prevents imaginary-axis crossings and proves every denominator Hurwitz. With \(S=1+\sum u_j\), the resulting ratio lower bound is
\[
\operatorname{Re}\frac{b(i\omega)}{a(i\omega)}\ge
\frac{75122752392578125}{30141440000009094400000000686}>0.
\]
Because the central \(q_*\) belongs to the set of tail polynomials, this full-width stable septic box has a tail family that is **not** robustly Hurwitz. The small-constant lift cannot be applied merely by asserting the tail-stability hypothesis; a separate certificate would be required. Nothing here shows every tail in the box unstable, nor does it show an SPR obstruction.

Frozen factorization, tail minors, endpoints, center and corner Bernstein leaves and bounds: `frontier-20261028-hurwitz-septic-unstable-tail-frozen-v1.json`, SHA-256 `0c275cf02ae54a1f24185ff4bc3b6732903a06160fc5dee53492d9a7692dfd7c`. Standalone checker `frontier-20261028-hurwitz-septic-unstable-tail-independent-kernel-v1.py`, SHA-256 `63d9fb27b4658945a59c4b0bc78acdf2d47e303f16114a71685d2fa5a6f2d587`, reconstructs the stable factorization, all tail Hurwitz minors, all 28 box-corner minors, the six-leaf center proof, four six-leaf corner proofs, and the quantitative perturbation/ratio bounds. Its stable-tail positive control passed. Receipt `frontier-20261028-hurwitz-septic-unstable-tail-independent-result-v1.json`, SHA-256 `52317706fd988dcd97e4ae7ffd5035e28cc364361446a2ec484e849f01c33b32`.

The first producer invocation stopped on a helper-arity `TypeError`; the missing explicit corner helper was added and execution resumed at that failed step. The displayed candidate was subsequently replayed from frozen bytes by the standalone checker. This is same-host exact rational arithmetic and written homotopy reasoning, not formal, cross-vendor or novelty-verified evidence.
