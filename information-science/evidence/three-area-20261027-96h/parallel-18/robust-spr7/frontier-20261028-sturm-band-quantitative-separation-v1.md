# Uniform separation from the denominator family

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** In the explicit 14-dimensional endpoint neighborhood of `frontier-20261028-sturm-band-no-family-open-neighborhood-v1.md`, every box \(K'\) has a common unrestricted monic septic SPR numerator. Yet **every** such common monic numerator \(b\) must satisfy the quantitative coefficient bound
\[
\operatorname{dist}_\infty\bigl((b_0,\ldots,b_6),K'\bigr)>\frac{23}{100}.
\]
The distance is the usual \(\ell_\infty\) distance to the seven-dimensional coefficient rectangle; both numerator and denominator leading coefficients are one. The assertion is not scale-invariant without that normalization. This is an obstruction to choosing a numerator from, or even uniformly close to, the denominator family—not an unrestricted negative certificate.

## Proof

Use the anchor's three actual atoms, their positive weights, and the combined numerator coefficient vector \(C\), as well as the anchor full-box obstruction margin \(M>0\) in the preceding packet. Put
\[
T=\sum_{j=0}^6|C_j|
=\frac{501620365339001532623335013817068376456912736539642454974155269}
{662100037129581926400000000000000000},\qquad d=\frac{23}{100}.
\]
The maximum of the atom sum over the monic box obtained by enlarging each anchor interval by \(d\) on both sides is exactly \(-M+dT=-M_d\), with
\[
M_d=\frac{5456788847633163642779403540089571027172812503238924707044637426684331943913}
{12981592480036971812065388789760000000000000000000000}>0.
\]
Thus no numerator at distance at most \(d\) from the anchor box can have all three atom pairings strictly positive.

For an endpoint perturbation \(K'\) of radius \(\varepsilon=10^{-14}\), use its corresponding three actual corners. The monomial coefficient perturbation bounds \(A_j\) are those in the neighborhood theorem. Any monic \(b'\) within distance \(d\) of \(K'\) is within coefficient distance \(\varepsilon\) of some monic \(b\) in the anchor's \(d\)-expanded box, and satisfies \(|b'_j|\le h_j+d+1\). Therefore the perturbed atom sum is at most
\[
-M_d+\varepsilon L_d,\quad
L_d=T+\sum_{j=0}^6 A_j(h_j+d+1)+A_7
=\frac{58736528639626517421147336955524305698542223563868974610294661351}
{4634700259907073484800000000000000000}.
\]
Exact arithmetic gives \(2\varepsilon L_d\le M_d\), so this sum is strictly negative. A common SPR numerator would instead make each of the three positive-weight pairings strictly positive. Contradiction. The cited neighborhood theorem independently supplies stability and an unrestricted common numerator for every \(K'\).

Frozen constants and source pins: `frontier-20261028-sturm-band-quantitative-separation-frozen-v1.json`, SHA-256 `d711a682c7a58f27a43b8d9e5c911c1cf15fceca2b77330761cd7e475a68d0e3`. Independent arithmetic checker `frontier-20261028-sturm-band-quantitative-separation-independent-kernel-v1.py`, SHA-256 `c60d11bebc48ba124d258f183c3592d93f1e7d70937baf3fee7a4a302730c30f`; receipt `frontier-20261028-sturm-band-quantitative-separation-independent-result-v1.json`, SHA-256 `e924839e91e0b8f6eb4886d9adce64f19d537e6a191e4f28f55e4c9e5efa5f77`. The neighborhood theorem is SHA-256 `1169da41e41d2b862df67aab8c80b4cfd04b75e07e6eeed8ff18a9db9c174bbc`.

Finite inequalities were recomputed with exact integers and `fractions.Fraction` on one Python Eval host; the projection and perturbation estimates are written mathematics. The result is not formal, cross-vendor, novelty-cleared, or a verdict for arbitrary boxes.
