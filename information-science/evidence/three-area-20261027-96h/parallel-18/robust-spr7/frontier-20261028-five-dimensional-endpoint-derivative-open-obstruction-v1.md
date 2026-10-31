# Five-dimensional real-span obstruction, explicit and generic

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** There is an explicit full-dimensional strictly stable septic box with a common unrestricted SPR numerator, but no common numerator in the **real span of its four parity endpoint polynomials and the derivative of its midpoint**. The obstruction persists in an explicit 14-dimensional endpoint neighborhood. Moreover it is generic near the boundary of the nine-parameter five-contact family. This is a restricted-construction obstruction, not an unrestricted counterexample.

## An actual stable box and a six-atom annihilator

For ascending nonleading coefficients \(a_0,\ldots,a_6\), independently use
\[
\begin{aligned}
\ell&=(198331/19000,\ 4809/100,\ 197601/7600,\ 12201/200,\ 197801/18000,\ 3001/200,\ 85567/85500),\\
u&=(303469/19000,\ 6591/100,\ 197799/7600,\ 12399/200,\ 197999/18000,\ 3199/200,\ 98833/85500),
\end{aligned}
\]
with leading coefficient one. Let \(m\) be its coefficientwise midpoint and
\[
\mathcal V_K=\operatorname{span}_{\mathbb R}\{
E_-(-s^2),E_+(-s^2),sO_-(-s^2),sO_+(-s^2),Dm\}.
\]
All five coefficients in this span are arbitrary real numbers. The box is strictly stable and the monic numerator
\[
(b_0,\ldots,b_7)=\left(1,\frac{3859}{5},\frac{19153}{10},\frac{6981}{10},1072,119,116,1\right)
\]
works for every member. Independent replay checked 28 strict corner Hurwitz minors and 184 positive compactified Bernstein coefficients, with uniform pairing margin
\[
\delta=\frac{17352797961017653}{13161154184478720000}>0.
\]
Kharitonov's theorem and affine corner minimization give all-member stability and positivity.

Number the four actual parity corners 0–3 in \((--),(-+),(+-),(++)\) order. Six actual atoms with positive integer weights are
\[
\begin{array}{c|c|r}
\text{corner}&t=\omega^2&\text{weight}\\\hline
2&4/5&103907856754649655541812570855556029506\\
2&6/5&1250897184611018995554209166557438637561\\
3&9/5&54870341682280569006482635597026935700\\
1&16/5&410628583004308994118622393030855450446\\
0&31/5&79962770209036082935224445538843112265\\
2&39/5&22254053939289091182578874540955270119
\end{array}
\]
Their weighted pairing sum is **exactly zero on each of the five generators**, by independent direct monomial accumulation. Any common SPR numerator would instead make all six positive-weight summands strictly positive. Therefore no nonzero \(b\in\mathcal V_K\) works, including every \(m+hDm\) with arbitrary real \(h\). The displayed unrestricted numerator has strictly positive atom sum
\[
\frac{1284385498855749229429212064724012468467133085351}{1187500}>0.
\]
The six-atom zero is only a five-generator-space annihilator, **not** an all-numerator negative or zero certificate.

## Persistence on an explicit endpoint neighborhood

Perturb all 14 endpoints independently by at most \(\varepsilon=10^{-68}\), and in each new box form its own four endpoint generators and its own midpoint derivative. Let \(R\) be the \(5\times6\) matrix of the six atom pairings with the five generators. With the stated atom order, all signed cofactors \(q_i=(-1)^{i+1}\det R_{\widehat i}\) are strictly positive and proportional to the listed weights. Their minimum is
\[
q_{\min}=\frac{448466809016575544173147749193823993849991021789}
{75856805779039859771728515625000000000}>0.
\]
Endpoint coefficients stay below 100, first-derivative generator coefficients below 1000, and all atom frequencies satisfy \(t<9\). Direct monomial estimates bound each entry by \(10^{15}\) and its perturbation by \(10^{13}\varepsilon\). Telescoping the five factors in each determinant term gives
\[
|\Delta q_i|<5!\cdot5\cdot(10^{15})^4\cdot10^{13}\varepsilon
<10^{76}\varepsilon<q_{\min}/2.
\]
Thus the perturbed cofactors remain positive and annihilate the perturbed five-generator matrix by the cofactor identity. The fixed good numerator remains common: its anchor compactified margin \(\delta\) satisfies \(14\varepsilon\sum|b_j|\le\delta\), and the straight projection path to the anchor excludes imaginary-axis zeros. Interval widths stay positive; homotopy gives strict stability. The no-span and unrestricted-existence statements therefore hold throughout this open endpoint neighborhood.

## Generic five-contact boundary theorem

For the nine-parameter feasible five-contact family of `frontier-20261028-generic-five-contact-span-rigidity-v1.md`, form the five actual boundary contact tangent rows and add the boundary midpoint derivative to the four endpoint generators. At the explicit feasible shape \((t_1,\ldots,t_5)=(1,2,3,6,8)\), \(u=1/2,v=11,\alpha=1,\beta=989/855\), the full \(5\times5\) tangent determinant is
\[
-\frac{18174831701965702400}{20577}\ne0.
\]
It is a polynomial in the nine shape parameters. Thus it is nonzero on an open dense subset of the strictly feasible parameter set. For any such shape, the compactness argument in the cited four-dimensional theorem applies verbatim with five generators: if common numerators in these spans existed arbitrarily near the boundary, normalize their coefficient norm, pass to a nonzero limiting span numerator, and use five boundary nonnegative-pairing tangencies. The invertible tangent matrix forces the limit to vanish, a contradiction. Hence every sufficiently near-boundary radial stable box for a generic shape has no common numerator in its real endpoint-plus-midpoint-derivative span. No claim is made here that an unrestricted common numerator exists for every generic shape.

## Evidence

Anchor six-atom data and exact leaves: `frontier-20261028-five-dimensional-endpoint-derivative-span-frozen-v1.json`, SHA-256 `0345ecd235b7361d2ba7e52067a0c317f9da8473fe019bf448f5fef2b7fef12b`. Open bounds: `frontier-20261028-five-dimensional-endpoint-derivative-open-frozen-v1.json`, SHA-256 `71336558fd0cf32a16c178a6a0b6b6a01bb5ff77799c8418ebcb574a295d2583`. Independent open checker `frontier-20261028-five-dimensional-endpoint-derivative-open-independent-kernel-v1.py`, SHA-256 `0acf59f11260d39ecff846bd16a99fa5977e78f0aa32cc84b89cff326c477b5e`; receipt `frontier-20261028-five-dimensional-endpoint-derivative-open-independent-result-v1.json`, SHA-256 `23090f096f95d26b2137c3ecc82992e0af9931b188d5c883a34814854fb454ad`. The receipt discloses the corrected common cofactor orientation in the first anchor-only replay; the final open checker ran cleanly.

Generic tangent determinant input: `frontier-20261028-generic-five-dimensional-boundary-frozen-v1.json`, SHA-256 `8d6b3603c9bd42ea02867e64714f1ee1099fa8202407c8607eafd270c2b221ed`. Independent checker `frontier-20261028-generic-five-dimensional-boundary-independent-kernel-v1.py`, SHA-256 `628783099fd19187b65b376c613d5cfe553b4fbd2255c0b31b6d7a782fdd10c7`; receipt `frontier-20261028-generic-five-dimensional-boundary-independent-result-v1.json`, SHA-256 `19f9c6f64bbfd65db5e1ec5c7c1d6a2e4c90451147b90b70743a4d825d512fdb`.

Finite identities use exact integers and `fractions.Fraction` on one Python Eval host. Kharitonov, cofactor continuity, genericity and compactness are written imports or deductions. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or unrestricted negative certificate is claimed.
