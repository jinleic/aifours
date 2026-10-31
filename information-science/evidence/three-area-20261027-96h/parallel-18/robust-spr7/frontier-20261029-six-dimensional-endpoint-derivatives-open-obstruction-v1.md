# An open six-dimensional real-span obstruction

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** An explicit strictly stable, full-dimensional septic interval box has a common SPR numerator, but **no** common numerator in the real span of its four parity endpoint polynomials and the first two derivatives of its midpoint. A seven-atom exact annihilator proves the obstruction, which persists on a nonempty 14-dimensional endpoint neighborhood. It is not an unrestricted negative certificate.

## Explicit box and unrestricted common numerator

Start with the boundary lower and upper coefficient vectors
\[
\ell=\left(\tfrac{989}{95},48,26,61,\tfrac{989}{90},15,1\right),\qquad
u=\left(16,66,\tfrac{989}{38},62,11,16,\tfrac{989}{855}\right),
\]
and let \(K\) be their midpoint-centered independent radial subbox at \(\rho=9999/10000\), with leading coefficient one. Let \(m\) be its monic coefficientwise midpoint and define
\[
\mathcal V_K=\operatorname{span}_{\mathbb R}\{
E_-(-s^2),E_+(-s^2),sO_-(-s^2),sO_+(-s^2),Dm,D^2m\}.
\]
The six coefficients in this span may have **arbitrary real signs**. The following monic numerator works for every member of \(K\):
\[
(b_0,\ldots,b_7)=\left(1,\frac{31123600610695}{40325878296},
\frac{6436183131383}{3360489858},\frac{18768571613959}{26883918864},
\frac{3602387101783}{3360489858},\frac{9596376720775}{80651756592},116,1\right).
\]
Independent exact replay checked 28 strictly positive Hurwitz determinants of the four actual parity corners and 256 strictly positive compactified Bernstein coefficients, giving the anchor margin
\[
P_{a,b}(t)/(1+t)^7\ge
\delta=\frac{476577671648361296780522437607}
{49468096905512397009349817401344000}>0.
\]
Kharitonov's theorem and affine corner minimization extend the result to every denominator and every frequency.

## Seven-atom annihilator

Number actual parity corners 0–3 by \((--),(-+),(+-),(++)\). The seven positive integer-weight atoms are:
\[
\begin{array}{c|c|r}
\text{corner}&t=\omega^2&\text{weight}\\\hline
2&51/50&2945091079401542776765947896543242936532868198393409717484733950001468790867724417468750\\
3&101/50&2240028097667073582988306303520732115390385542006260093727855727198985673025125735093750\\
1&149/50&567550808192629679519955973261157768242014910367774268145342419064456713164024840250000\\
1&151/50&5161085400848713880472506125901567940392046351376498204364276117352770526106316907703125\\
0&301/50&2106439688639964922554087470145892119432885212853643932633502600363237183414787610093750\\
2&399/50&111619654358902570059546981199189939979733609456913573841430345020719630039205767984375\\
0&5&63636877624055365942325237781850392573964934827558462521021804503709887776144378004016
\end{array}
\]
Their weighted pairing sum is **exactly zero on all six generators**. Thus it is zero on their entire real span, while a common SPR numerator would make all seven summands strictly positive. No numerator in \(\mathcal V_K\) can work. The unrestricted positive numerator above works, so the annihilator is not a zero or negative certificate against all eight monomial directions.

## Explicit open persistence

Perturb each of the 14 interval endpoints independently by at most \(\varepsilon=10^{-92}\), retain monicity, and recompute the four parity generators and the first two derivatives of the **new** midpoint. In the \(6\times7\) atom/generator pairing matrix, all seven signed cofactors are positive and proportional to the displayed weights. Their minimum is
\[
q_{\min}=\frac{2299864226065988248080549612712477701407184679709781937644630879902920019608752141596145032709}
{225199892156524583697319030761718750000000000000000000000000000000000000000000000000000}>0.
\]
The independent replay verifies that all endpoints stay below 100 and all selected frequencies are below 9. Endpoint-generator coefficients stay below 100; first and second midpoint derivative coefficients stay below 5000. A direct parity-compatible monomial estimate gives pairing entries below \(10^{16}\) and entry perturbations below \(10^{14}\varepsilon\). Telescoping six factors in each of \(6!\) determinant terms gives
\[
|\Delta q_i|<6!\cdot6\cdot(10^{16})^5(10^{14})\varepsilon
<10^{98}\varepsilon<q_{\min}/2.
\]
Every perturbed cofactor stays positive and the cofactor identity annihilates all six new generators. The checker also verifies \(14\varepsilon\sum|b_j|\le\delta\) and positive interval widths. The same fixed \(b\) retains a positive compactified pairing along each straight path to the anchor box; no imaginary-axis crossing occurs and homotopy preserves strict stability. Thus the six-dimensional real-span obstruction and unrestricted existence both persist on the whole endpoint neighborhood.

Frozen exact endpoints, seven weights and positive-frequency leaves: `frontier-20261029-six-dimensional-endpoint-derivatives-frozen-v1.json`, SHA-256 `93aaebc291516b3d4ff81b4cf7b1435ad3d4b3440f9ff38fb1f2ba1438971a0c`. Open bounds: `frontier-20261029-six-dimensional-endpoint-derivatives-open-frozen-v1.json`, SHA-256 `22a95b0643672af140b6b1c824790d9d715d20658c2e17acac8e82c2ccbce71d`. Independent checker `frontier-20261029-six-dimensional-endpoint-derivatives-open-independent-kernel-v1.py`, SHA-256 `2387496f7f0b4d7f200ea47a3047532f335f5fd0a829bb776ff68374805b5b8b`; receipt `frontier-20261029-six-dimensional-endpoint-derivatives-open-independent-result-v1.json`, SHA-256 `07a20ca61d2f95e5683e24d5b1132932cc2bd19ac4fb606c55c48f458e97c066`.

Finite checks used exact integers and `fractions.Fraction` on one Python Eval host. Kharitonov, cofactor continuity, affine corner minimization and homotopy are written imports or deductions. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or all-numerator negative certificate is claimed.
