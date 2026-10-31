# One common numerator despite a non-Hurwitz interval hull

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** Two explicit independent septic coefficient boxes and their ordinary convex hull share one strictly positive-real numerator. Their *coefficientwise independent interval hull*, however, contains a non-Hurwitz polynomial. Thus replacing a stable nonrectangular family by its independent coefficient hull can invalidate stability even when the original family already has a common numerator. This is an obstruction to that enclosure proof strategy, not an unrestricted negative certificate.

## Exact boxes and common numerator

For monic \(a(s)=s^7+\sum_{j=0}^6a_js^j\), the two boxes independently use the following intervals:
\[
\begin{array}{c|cc|cc}
j&\ell^{(1)}_j&u^{(1)}_j&\ell^{(2)}_j&u^{(2)}_j\\\hline
0&1041/100&15997/1000&5207/500&16019/1000\\
1&48009/1000&65991/1000&4783/100&65991/1000\\
2&26001/1000&13013/500&26003/1000&13013/500\\
3&61001/1000&61999/1000&61001/1000&61899/1000\\
4&10989/1000&10999/1000&10989/1000&5499/500\\
5&15001/1000&15999/1000&1884/125&15999/1000\\
6&1001/1000&289/250&127/125&289/250
\end{array}
\]
Every interval has positive width. Their shared monic numerator has ascending coefficients
\[
(b_0,\ldots,b_7)=
\left(\frac6{25},\frac{6359}{100},\frac{5667}{50},\frac{6739}{100},
\frac{3033}{50},\frac{1683}{100},\frac{25}{4},1\right).
\]
An independent exact replay verified all **56** positive leading Hurwitz determinants of the eight actual parity corners and **448** positive compactified Bernstein coefficients covering all frequencies. For every denominator \(a\) in either box,
\[
\frac{P_{a,b}(t)}{(1+t)^7}\ge
\delta=\frac{158791179496067}{7388718138654720000}>0.
\]
Kharitonov's theorem supplies all-member stability, and affine corner minimization supplies the pairing bound. With \(S=199189/1000\), this gives the explicit bound \(\operatorname{Re}(b(i\omega)/a(i\omega))\ge\delta/S^2>0\).

The ordinary convex hull of the union also has the same numerator: the pairing is affine in \(a\), so the bound survives convex combinations. Its denominators are Hurwitz by homotopy from a stable box member, because a positive pairing excludes imaginary-axis zeros along the path.

## The larger independent interval hull fails

Take each lower coefficient to be the minimum of the two lowers and each upper coefficient to be the maximum of the two uppers. This independent interval hull contains the monic polynomial with ascending coefficients
\[
\left(\frac{1041}{100},\frac{4783}{100},\frac{13013}{500},
\frac{61999}{1000},\frac{10989}{1000},\frac{15001}{1000},\frac{289}{250},1\right).
\]
Its sixth leading Hurwitz determinant is
\[
\Delta_6=-\frac{1030368095142003531}{25000000000000000}<0,
\]
so it is not strictly Hurwitz. This mixed hull corner need not lie in the ordinary convex hull of the original two boxes; the two hull operations are not interchangeable.

Frozen endpoints, common numerator, frequency leaves and hull corner: `frontier-20261028-two-box-shared-numerator-unstable-hull-frozen-v1.json`, SHA-256 `975116cd772e0bc86123d1f647fd56d8a19b15a11fca657e245c41d0a2769574`. Independent checker `frontier-20261028-two-box-shared-numerator-unstable-hull-independent-kernel-v1.py`, SHA-256 `08e643e7a5c69285fff61f880966c9da4cedbc420a6900786eef4f66c985fd11`; receipt `frontier-20261028-two-box-shared-numerator-unstable-hull-independent-result-v1.json`, SHA-256 `cee211c73764d5ff3fadb37b40ddedbd49837bc0e3100eca5752f7c62168a13f`.

The finite checks use exact integers and `fractions.Fraction` on one Python Eval host. Kharitonov, affine minimization and homotopy are written imports or deductions; no formal proof, cross-vendor review, novelty clearance, universal positive claim, or all-numerator negative certificate is asserted.
