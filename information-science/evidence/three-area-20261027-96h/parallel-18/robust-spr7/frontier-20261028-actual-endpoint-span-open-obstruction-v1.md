# An open family requiring more than the real endpoint span

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** An explicit strictly Hurwitz-stable, full-dimensional septic interval box has a common SPR numerator, but **no** common numerator in the real linear span of its four actual parity endpoints—even when the four linear-combination coefficients may have arbitrary signs. This obstruction persists on a nonempty 14-dimensional endpoint neighborhood. It is not a negative answer to the unrestricted synthesis problem.

## Exact box, span and common numerator

Let the seven ascending interval endpoints be
\[
\begin{aligned}
\ell&=(99431/9500,\ 2409/50,\ 98801/3800,\ 6101/100,\ 10989/1000,\ 1501/100,\ 42817/42750),\\
u&=(151469/9500,\ 3291/50,\ 98899/3800,\ 6199/100,\ 98999/9000,\ 1599/100,\ 5487/4750),
\end{aligned}
\]
with independent variation and monic leading coefficient. For its actual even and odd parity endpoints define the real four-generator space
\[
\mathcal L_K=\operatorname{span}_{\mathbb R}
\{E_-(-s^2),\ E_+(-s^2),\ sO_-(-s^2),\ sO_+(-s^2)\}.
\]
All four parity-corner polynomials belong to this span, as do arbitrary independent real scalings and mixtures of the even and odd endpoints.

Nevertheless the explicit monic numerator with ascending coefficients
\[
(b_0,\ldots,b_7)=\left(1,\frac{3859}{5},\frac{19153}{10},\frac{6981}{10},1072,119,116,1\right)
\]
is common SPR for the whole box. The independent replay checked all 28 strict corner Hurwitz determinants and 168 strict compactified Bernstein coefficients, giving the uniform pairing bound
\[
P_{a,b}(t)/(1+t)^7\ge
\delta=\frac{291156110641}{286890393600000}>0.
\]
Kharitonov's theorem and affine corner minimization extend this to all denominators and all frequencies.

## Five positive atoms annihilate the entire real span

Number the actual parity corners \((E_-,O_-),(E_-,O_+),(E_+,O_-),(E_+,O_+)\) by 0–3. The following five actual atoms have positive integer weights:
\[
\begin{array}{c|c|r}
\text{corner}&t=\omega^2&\text{weight}\\\hline
2&6/5&53229390749948868643605555179\\
3&9/5&77608046939781933056995507005\\
1&14/5&22249893974058422128108604139\\
2&39/5&2154205808314384545779880704\\
2&41/5&2243968018316626707171891
\end{array}
\]
Let \(F(v)\) be the weighted sum of their pairings. Independent direct monomial accumulation gives **exactly**
\[
F(E_-(-s^2))=F(E_+(-s^2))=F(sO_-(-s^2))=F(sO_+(-s^2))=0.
\]
Thus \(F(v)=0\) for every \(v\in\mathcal L_K\). A common SPR numerator would have all five weighted pairings strictly positive, a contradiction. This zero statement is only on the four-dimensional endpoint space; in fact the explicit unrestricted numerator satisfies
\[
F(b)=\frac{139354709682066710648644001554480686366}{1484375}>0.
\]
Accordingly, the five atoms are **not** a negative-coordinate certificate against all numerators.

## Explicit open persistence

For each atom \(i\) and generator \(k\), set \(R_{ki}=P_{a_i,g_k}(t_i)\). The independent replay checked that all five signed cofactors
\[
q_i=(-1)^i\det R_{\widehat{i}},\qquad i=0,\ldots,4,
\]
are strictly positive and proportional to the integer weights. Their exact minimum is
\[
q_{\min}=\frac{1342782446706907994581061556405348}
{19962317310273647308349609375}>0.
\]
Perturb all 14 interval endpoints independently by at most \(\varepsilon=10^{-52}\). Use the corresponding perturbed corners and parity generators at the same five frequencies. Endpoint coefficients remain below 100 and all \(t_i<9\). A monomial expansion gives the conservative entry and perturbation bounds
\[
|R_{ki}|<10^{14},\quad |\Delta R_{ki}|<10^{12}\varepsilon,
\quad |\Delta q_i|<10^{56}\varepsilon<q_{\min}/2.
\]
The determinant estimate follows by telescoping the four factors in each of 24 determinant terms. Every \(q_i'\) remains positive, and the cofactor identity gives \(R'q'=0\). The corresponding five **actual perturbed corners** therefore still annihilate the entire real endpoint span with positive weights.

The checker also verifies positive interval widths and \(14\varepsilon\sum|b_j|\le\delta\), with \(\sum|b_j|=23471/5\). Project any perturbed denominator coefficientwise into the anchor box. Its normalized pairing with the fixed \(b\) changes by at most \(7\varepsilon\sum|b_j|\le\delta/2\), including along the connecting segment. Positive pairing excludes imaginary-axis crossings, so the perturbed box remains strictly Hurwitz and has the same common numerator. The real-span obstruction and unrestricted existence thus both persist on a full 14-dimensional open endpoint neighborhood.

Frozen box, exact annihilator, numerator and leaves: `frontier-20261028-actual-endpoint-span-obstruction-frozen-v1.json`, SHA-256 `95d943653a8ceca71d99950a326a4fe7a3fcd2fac0471c746de82570daab83fb`. Open bounds: `frontier-20261028-actual-endpoint-span-open-frozen-v1.json`, SHA-256 `c3a98e16130afeb75d6963a6487cbebc4e21e58d8b4f8f261b814157b1e9bd1e`. Independent checker `frontier-20261028-actual-endpoint-span-open-independent-kernel-v1.py`, SHA-256 `f84a60c8260dd9a13de5616b9dcd14e50cef33c30584b074bef66a086ac12cc9`; receipt `frontier-20261028-actual-endpoint-span-open-independent-result-v1.json`, SHA-256 `4a9dd981c240b1b3a44f374e91bbc459258a801de4fbc8542378c93aa4f666d9`.

The finite identities use exact integers and `fractions.Fraction` on one Python Eval host. Kharitonov, affine minimization, determinant continuity and homotopy are written imports or deductions. No formal proof, cross-vendor review, novelty clearance, arbitrary-box theorem, or all-numerator negative certificate is asserted.
