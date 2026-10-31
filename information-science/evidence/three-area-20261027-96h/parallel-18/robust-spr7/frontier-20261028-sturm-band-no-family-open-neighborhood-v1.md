# An open family requiring the common numerator to leave the denominator box

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** The obstruction in `frontier-20261028-sturm-band-no-family-numerator-v1.md` is not an isolated degeneracy. Let \(K\) be that packet's explicit strictly stable septic box, with endpoints \((\ell_j,h_j)_{j=0}^6\), and perturb each of its 14 endpoints independently by at most
\[
\varepsilon=10^{-14}.
\]
Every resulting box \(K'\) has seven positive-width intervals, is strictly Hurwitz, and shares the **same explicit unrestricted** common SPR numerator \(b\) from `frontier-20261028-sturm-band-anisotropic-box-synthesis-v1.md`. However, **no monic numerator lying inside its own \(K'\)** can be common SPR for \(K'\). In particular the strict inequalities hold on a nonempty 14-dimensional open endpoint neighborhood. This does not rule out unrestricted numerators and does not settle the original arbitrary-box problem.

## Positive synthesis and stability persist

For the anchor box and its displayed monic numerator, the independent compactified pairing replay gives
\[
\frac{P_{a,b}(t)}{(1+t)^7}\ge\delta>0\quad(a\in K,\ t\ge0),\qquad
\delta=\frac{8935551948234464603794129462286704554333771}
{11909882842232846221218111260111887400960000000},\quad
B=\sum_{j=0}^7|b_j|=\frac{3159232301}{5}.
\]
For each \(a'\in K'\), choose \(a\in K\) with \(|a'_j-a_j|\le\varepsilon\) for \(j\le6\). Monomial expansion and \(t^{(j+k)/2}\le(1+t)^7\) give
\[
\frac{|P_{a',b}(t)-P_{a,b}(t)|}{(1+t)^7}\le7\varepsilon B\le\delta/2.
\]
The same estimate holds on the straight coefficient path from \(a\) to \(a'\). No polynomial on that path has an imaginary-axis zero, because then its pairing would be zero. Since \(a\) is Hurwitz, homotopy makes \(a'\) Hurwitz. Also, if \(S=1+\sum h_j\) for the anchor, then
\[
\operatorname{Re}\frac{b(i\omega)}{a'(i\omega)}\ge
\frac{\delta/2}{(S+7\varepsilon)^2}>0.
\]

## The no-family-numerator certificate persists

Let the three actual anchor atoms, positive weights and combined coefficient vector \(C\) be those of the cited three-atom packet. Their maximum over monic \(b\in K\) is \(-M\), where
\[
M=\frac{2267533640364343317259095319125151909302637034028471098859237860674482800551913}
{12981592480036971812065388789760000000000000000000000}>0.
\]
In \(K'\), use the **corresponding three actual parity corners** at the same frequencies and weights. Write their combined coefficients as \(C'_j\). Since each denominator coefficient moves by at most \(\varepsilon\), the monomial formula gives
\[
|C'_j-C_j|\le\varepsilon A_j,\qquad
A_j=\sum_iw_i\sum_{\substack{0\le k\le6\\j+k\;\mathrm{even}}}t_i^{(j+k)/2}.
\]
For \(b'\in K'\), choose \(b_0\in K\) within \(\varepsilon\) coefficientwise. Using \(|b'_j|\le h_j+1\) and \(b'_7=1\), one obtains
\[
F_{K'}(b')\le F_K(b_0)+\varepsilon L\le-M+\varepsilon L\le-M/2<0,
\]
where
\[
L=\sum_{j=0}^6|C_j|+\sum_{j=0}^6A_j(h_j+1)+A_7
=\frac{25114833953533426472470508729994423827488815938379732095785492579}
{1986300111388745779200000000000000000}.
\]
A numerator common SPR for \(K'\) would have strictly positive pairing on all three positive-weight atoms and therefore \(F_{K'}(b')>0\), impossible. The separately checked conditions \(\varepsilon\le1\), \(4\varepsilon\le\min_j(h_j-\ell_j)\), and \(2\varepsilon\le\min_j\ell_j\) make all perturbed intervals valid and positive. The exact replay checked \(14\varepsilon B\le\delta\) and \(2\varepsilon L\le M\).

Frozen constants and source pins: `frontier-20261028-sturm-band-no-family-open-neighborhood-frozen-v1.json`, SHA-256 `f6b46be8749712e19172764e0ae6274189b3d08daa6d1bf16234e5e421362ca0`. Independent arithmetic checker `frontier-20261028-sturm-band-no-family-open-neighborhood-independent-kernel-v1.py`, SHA-256 `431136914d805381c51362d53c4167b10882b4034eb668b38267e95317290888`; receipt `frontier-20261028-sturm-band-no-family-open-neighborhood-independent-result-v1.json`, SHA-256 `b216fb33c7b09511d62057e685ccb863dcedd85dbbf55a133c667356a76461f5`. The two anchor replays are named imports, not newly asserted cross-vendor results.

The finite bounds were recomputed exactly with integers and `fractions.Fraction` on one Python Eval host. Continuity and homotopy are written deductions. No formal verification, cross-vendor review, novelty clearance, all-numerator negative certificate, or universal positive conclusion is claimed.
