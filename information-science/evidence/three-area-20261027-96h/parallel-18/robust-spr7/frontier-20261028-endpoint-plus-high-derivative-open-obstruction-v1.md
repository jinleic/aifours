# A necessary negative high-derivative coordinate in a full basis

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** For the explicit strictly stable septic box in `frontier-20261028-actual-endpoint-span-open-obstruction-v1.md`, a common unrestricted SPR numerator exists. Nevertheless, in a natural **full eight-dimensional real polynomial basis**, every common numerator must have at least one negative coefficient among four specified high-derivative coordinates. The same statement holds for every box in an explicit 14-dimensional endpoint neighborhood. It is not an unrestricted negative certificate.

## Exact full-basis constraint

Let \(E_\pm,O_\pm\) be the box's actual parity endpoints and \(m\) its coefficientwise midpoint. Define
\[
(g_0,g_1,g_2,g_3)=
(E_-(-s^2),E_+(-s^2),sO_-(-s^2),sO_+(-s^2)),\qquad
(g_4,g_5,g_6,g_7)=(D^4m,D^5m,D^6m,D^7m).
\]
With columns in this order and rows in ascending monomial degree, their exact determinant is
\[
\det[g_0,\ldots,g_7]=-\frac{8512126955071488}{95}\ne0.
\]
Thus every real polynomial of degree at most seven has a unique expansion \(b=\sum_{j=0}^7c_jg_j\).

Using the four actual parity corners numbered \(0,1,2,3\), take the five positive atoms
\[
\begin{array}{c|c|r}
\text{corner}&t=\omega^2&\text{weight}\\\hline
2&6/5&6489599575259351312759922736\\
3&9/5&2239668552714918255310458300\\
1&16/5&1181158527964117600475514036\\
0&31/5&314522287615651130850761745\\
2&39/5&152749742315033516221773855
\end{array}
\]
and write \(F\) for their weighted pairing sum. Independent exact monomial accumulation gives
\[
F(g_0)=F(g_1)=F(g_2)=F(g_3)=0,\qquad
F(g_k)<0\quad(k=4,5,6,7).
\]
If \(b\) is common SPR, its five positive-weight pairings imply \(F(b)>0\); hence at least one of \(c_4,c_5,c_6,c_7\) is strictly negative. Equivalently, no numerator in
\[
\operatorname{span}_{\mathbb R}\{g_0,g_1,g_2,g_3\}
+\operatorname{cone}\{g_4,g_5,g_6,g_7\}
\]
can work. The four endpoint coefficients are unrestricted real numbers; the cone restriction is only on the four high-derivative coordinates. The explicit good numerator in the preceding packet is outside that cone and satisfies
\[
F(b)=\frac{24550117499844251383140814896678343743}{2968750}>0.
\]
In particular the signs above are basis-coordinate signs, not an all-negative monomial-coordinate certificate.

## Explicit 14-endpoint neighborhood

Perturb each endpoint independently by at most \(\varepsilon=10^{-64}\), retaining monicity. Recompute the parity endpoint generators \(g'_0,\ldots,g'_3\) and the **new midpoint's** derivatives \(g'_4,\ldots,g'_7\). Use the corresponding five actual perturbed corners at the same frequencies.

For the \(4\times5\) endpoint-pairing matrix \(R\), its five signed cofactors \(q_i=(-1)^i\det R_{\widehat i}\) are strictly positive, with minimum
\[
q_{\min}=\frac{2132998634896897626712439976089040957}
{199623173102736473083496093750}>0.
\]
They are proportional to the listed integer weights. The independent exact checker verified that all four cofactor-weighted high-derivative sums are strictly negative; their smallest absolute margin is
\[
T_{\min}=\frac{45780027618029712318911405891762281134027279936}
{29631564757437445223331451416015625}>0.
\]

The following deliberately conservative uniform bounds hold for every permitted perturbation: endpoint-pairing entries are below \(10^{14}\) and move by at most \(10^{12}\varepsilon\); cofactors are below \(10^{58}\) and move by at most \(10^{56}\varepsilon\); high-derivative pairing entries are below \(10^{18}\) and move by at most \(10^{16}\varepsilon\). They follow from coefficient bounds below 100, \(t<9\), at most 64 parity-compatible monomials, and \((j)_k\le7!=5040\). Telescoping determinant terms and the five cofactor-weighted terms yields
\[
|\Delta q_i|<10^{56}\varepsilon,\qquad
|\Delta F_{q}(g'_k)|<10^{75}\varepsilon\quad(k=4,5,6,7).
\]
The replay checks \(2\cdot10^{56}\varepsilon<q_{\min}\) and \(2\cdot10^{75}\varepsilon<T_{\min}\), so all cofactor weights remain positive and all four derivative sums remain negative. The cofactor identity preserves \(R'q'=0\).

The full basis determinant changes by less than \(10^{52}\varepsilon\), using the \(8!\) determinant expansion, basis-entry bound \(10^6\), and entry perturbation bound \(10^4\varepsilon\); the checker verifies that this is less than half its nonzero anchor absolute value. Hence the perturbed basis remains a basis, and the same necessary negative-coordinate conclusion holds for **every** common numerator of \(K'\). The checker also verifies positive interval widths and \(14\varepsilon\sum|b_j|\le\delta\) for the fixed good numerator from the preceding packet. The normalized pairing therefore remains positive along the straight path to each perturbed denominator, giving strict stability by homotopy and preserving the same unrestricted common numerator.

Frozen anchor support, basis and exact signs: `frontier-20261028-endpoint-plus-high-derivative-frozen-v1.json`, SHA-256 `3b7436f72f4909f8f4a41638c123030463cb52f19172ef6952136fc8e14ccf36`. Open bounds: `frontier-20261028-endpoint-plus-high-derivative-open-frozen-v1.json`, SHA-256 `72e9b13854b0c19690b67af03ad194e57768ed7fc2bb3807149c138216279217`. Independent checker `frontier-20261028-endpoint-plus-high-derivative-open-independent-kernel-v1.py`, SHA-256 `96905b1fbd686c045bef940ddbe67e0d82d23eac310d60718a4b4b4ab363f1c8`; receipt `frontier-20261028-endpoint-plus-high-derivative-open-independent-result-v1.json`, SHA-256 `07a3152673b92ef6d06b478bb4d35e3d3450006a52f48192eb33bc055d946cb5`.

The finite checks use exact integers and `fractions.Fraction` on one Python Eval host. Basis, cofactor, perturbation and homotopy conclusions are written mathematics; no formal proof, cross-vendor review, novelty clearance, universal arbitrary-box conclusion, or all-numerator negative certificate is claimed.
