# An explicit stable box defeats the seven-dimensional endpoint-derivative span

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** An explicit full-dimensional strictly Hurwitz septic interval box has an unrestricted common SPR numerator, but **no** common numerator in the real span of its four parity endpoint polynomials and the first **three** derivatives of its midpoint. An exact eight-atom annihilator excludes this entire seven-dimensional space, not just nonnegative combinations. The obstruction persists throughout a nonempty 14-dimensional endpoint neighborhood. This disproves the proposed seven-generator construction as a general route, but it is **not** an all-numerator negative certificate.

## The box and an unrestricted common numerator

Take five contact nodes
\[
(t_1,t_2,t_3,t_4,t_5)=\left(1,\frac32,100,101,2000\right),
\qquad u=\frac1{20},\quad v=2001,\quad \lambda=\frac{1001}{1000},
\]
and define the boundary parity endpoint cubics
\[
\begin{aligned}
E_-&=-\lambda(t-u)(t-100)(t-101),& E_+&=-(t-1)(t-\tfrac32)(t-2000),\\
O_-&=-(t-1)(t-101)(t-2000),& O_+&=-(t-\tfrac32)(t-100)(t-2001).
\end{aligned}
\]
They determine seven positive-width independent coefficient intervals. Let \(K\) be their midpoint-centered radial subbox at \(\rho=1-10^{-8}\), with leading coefficient one. The exact endpoints are pinned below. All 28 leading Hurwitz determinants of the four actual parity corners were independently checked strictly positive, so classical Kharitonov implies every member is strictly Hurwitz.

The following exact numerator is common SPR for the whole box:
\[
\begin{aligned}
(b_0,\ldots,b_7)=\biggl(&1,
\frac{2468423172985451768983127790933083}{7144455521819770790651676000},
\frac{1029507250507655223177021922509023}{59537129348498089922097300},\\
&\frac{110036243543554578505187531855699}{396914195656653932813982000},
\frac{184354521847628722242710239399423}{59537129348498089922097300},\\
&\frac{19463704954933091897679267922717}{7144455521819770790651676000},
4000,\frac1{2000}\biggr).
\end{aligned}
\]
Its degree is exactly seven; it may be divided by \(b_7>0\) to be monic. The independent checker verified **672** strictly positive compactified Bernstein coefficients across the four actual corner pairings. Affine minimization extends the proof to all members and all real frequencies. An explicit exact compactified margin is recorded in the frozen data.

## Eight positive atoms annihilate all seven generators

Let \(m\) be \(K\)'s monic midpoint, and set
\[
\mathcal V_K=\operatorname{span}_{\mathbb R}\{
E_-(-s^2),E_+(-s^2),sO_-(-s^2),sO_+(-s^2),Dm,D^2m,D^3m\}.
\]
The parity endpoints here are those of the **actual radial box**, not merely the boundary polynomials above. Number its actual parity corners 0–3 by \((--),(-+),(+-),(++)\). The eight positive-weight atoms have corner/squared-frequency pairs
\[
(2,999/1000),\ (3,2997/2000),\ (3,3003/2000),\ (1,1001/10),\
(0,100899/1000),\ (2,1998),\ (0,1/3),\ (0,4093/3).
\]
Their exact positive integer weights are large and are given in full in the frozen JSON. Independent direct monomial accumulation checks that their weighted pairing sum is **exactly zero on each of the seven generators**. A common SPR numerator would make all eight actual weighted pairings strictly positive. Thus no element of \(\mathcal V_K\), with **arbitrary real generator coefficients**, is a common numerator.

The eight signed \(7\times7\) cofactors of the atom/generator matrix are all strictly positive after the stated common orientation and proportional to those weights. In particular the generator space has dimension seven. The full atom sum has mixed monomial-coordinate signs, so it is not a strict negative-coordinate certificate against all numerators; the explicit numerator above proves unrestricted synthesis for this box.

## Persistence on an explicit open family

Perturb all 14 endpoints independently by at most \(\varepsilon=10^{-370}\), retain monicity, and form each new box's **own** four parity endpoints and midpoint derivatives. Coefficient widths remain positive. The corresponding eight actual corners/frequencies yield a perturbed \(7\times8\) pairing matrix whose cofactor vector remains positive: all denominator coefficients are below \(10^{10}\), all generator coefficients below \(10^{13}\), and all atom squared frequencies below \(10^4\). Direct monomial expansion bounds each matrix entry by \(10^{53}\) and its change by \(10^{44}\varepsilon\). Telescoping seven factors in each determinant gives
\[
|\Delta q_i|<7!\,7\,(10^{53})^6 10^{44}\varepsilon
<10^{367}\varepsilon<q_{\min}/2,
\]
where the exact positive \(q_{\min}\) and numerical checks are frozen. The cofactor identity continues to annihilate the new seven-generator matrix with strictly positive weights.

The same unrestricted \(b\) remains common for every perturbed box: the checker verifies \(14\varepsilon\sum|b_j|\le\delta\), where \(\delta\) is the anchor compactified pairing margin. Projection to the anchor and the straight coefficient path preserve a positive pairing and exclude imaginary-axis roots; homotopy gives strict stability. Consequently the span obstruction is not an isolated or degenerate example.

## Evidence and limits

Frozen exact endpoints, eight integer weights, seven generator sums, numerator and leaves: `frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json`, SHA-256 `3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293`. Open bounds: `frontier-20261029-seven-dimensional-span-obstruction-open-frozen-v1.json`, SHA-256 `5c9ef2bce336f60220d93b5e6a9720be4ca0a7971b1e7f96bdf44e9cf4014f11`. Independent checker `frontier-20261029-seven-dimensional-span-obstruction-open-independent-kernel-v1.py`, SHA-256 `f42e25296cc32a3863e003a592c8cbfd22651dffabe5080c369869e006b28671`; receipt `frontier-20261029-seven-dimensional-span-obstruction-open-independent-result-v1.json`, SHA-256 `42d6dfbb4dd6752d5f3814c70facb4f3526decfb29c5b29a9b3f8cdb95a9613f`. The receipt records the corrected JSON-key mismatch; the independently pinned 7+1 checker subsequently ran the corrected full source.

All finite arithmetic uses exact integers and `fractions.Fraction` on one Python Eval host. Kharitonov, affine minimization, cofactor continuity and homotopy are written imports or deductions. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or all-numerator negative certificate is claimed.
