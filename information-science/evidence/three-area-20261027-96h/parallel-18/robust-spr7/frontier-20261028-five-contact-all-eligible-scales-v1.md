# Exact SPR synthesis up to five simultaneous stability contacts

**Status: WRITTEN-checked-in-kernel; author candidate, not a parent adoption.** This resolves one explicit, highly constrained family, not the original unrestricted septic synthesis decision. It supplies an all-frequency obstruction to negative atom certificates for every eligible box in this family.

## The box family and five boundary contacts

Set the ascending lower and upper coefficient vectors

\[
\ell=\left(\frac{989}{95},48,26,61,\frac{989}{90},15,1\right),\qquad
u=\left(16,66,\frac{989}{38},62,11,16,\frac{989}{855}\right),
\]
with leading coefficient one. Let \(c=(\ell+u)/2\), and for \(\rho\ge0\) let \(K_\rho\) be the independent monic box \(a_j\in[c_j-\rho(u_j-\ell_j)/2,c_j+\rho(u_j-\ell_j)/2]\).

At \(\rho=1\), its actual parity extremal cubics are exactly

\[
\begin{aligned}
E_-&=-\frac{989}{855}(t-\tfrac12)(t-3)(t-6),&
E_+&=-(t-1)(t-2)(t-8),\\
O_-&=-(t-1)(t-6)(t-8),&
O_+&=-(t-2)(t-3)(t-11).
\end{aligned}
\]

The four actual corners, ordered \((E_-,O_-),(E_-,O_+),(E_+,O_-),(E_+,O_+)\), have five boundary imaginary-axis contacts at \((\text{corner},t)=(2,1),(3,2),(1,3),(0,6),(2,8)\).

**Exact stability classification.** Every polynomial in \(K_\rho\) is strictly Hurwitz for every \(0\le\rho<1\); no \(K_\rho\) with \(\rho\ge1\) is all-member strictly Hurwitz. Indeed, at \(t=1,2,3,6,8\) the center signs of \((E,O)\) are respectively \((-,+),(-,-),(+,-),(+,+),(-,+)\), and at the corresponding boundary contacts one extremal \(E\) and one extremal \(O\) vanish. For every smaller scale these signs hold strictly for every member; at \(t=0\) both signs are positive and at infinity both leading signs are negative. Consequently the three \(E\)-roots lie in \((0,1),(2,3),(6,8)\), and the three \(O\)-roots lie in \((1,2),(3,6),(8,\infty)\), with no common root. The box is connected to the center, whose positive rational Routh column is independently checked, so no root can cross the imaginary axis. Larger boxes contain the displayed boundary polynomial(s).

## One numerator for all eligible scales

The following **single** monic numerator works for every \(0\le\rho<1\), every \(a\in K_\rho\), and every real frequency:

\[
(b_0,\ldots,b_7)=\left(1,\frac{31123600610695}{40325878296},
\frac{6436183131383}{3360489858},
\frac{18768571613959}{26883918864},
\frac{3602387101783}{3360489858},
\frac{9596376720775}{80651756592},116,1\right).
\]

Let \(P_{a,b}(t)=\operatorname{Re}[b(i\sqrt t)a(-i\sqrt t)]\). At the singular boundary, exact polynomial identities and strictly positive half-line residuals give

\[
P_0=(t-6)^2q_0,\quad P_1=(t-3)^2q_1,\quad
P_2=(t-1)^2(t-8)^2q_2,\quad P_3=(t-2)^2q_3.
\]

The residual degrees are 5, 5, 3, 5, and complete rational Bernstein leaves certify each residual strictly positive on \([0,\infty)\). Their counts are 2, 3, 1, 3. The center pairing has a four-leaf certificate

\[
\frac{P_{c,b}(t)}{(1+t)^7}\ge
\delta=\frac{4820956225828025777}{28119357526470819840}>0.
\]

An actual corner at scale \(\rho\) is \((1-\rho)c+\rho a_{\mathrm{corner},1}\); pairing is affine in the denominator. For any frequency, the minimum over the independent box is the minimum over its four actual parity corners. Hence \(P_{a,b}(t)/(1+t)^7\ge(1-\rho)\delta\). Since \(S_1=1+\sum_j u_j=340603/1710\), every eligible member satisfies the explicit uniform bound

\[
\operatorname{Re}\frac{b(i\omega)}{a(i\omega)}\ge(1-\rho)
\frac{1373972524360987346445}{317947175036223363645177856}>0.
\]

As a consequence, no finite nonzero nonnegative combination of actual-corner finite-frequency functionals and the infinity functional can have all eight coefficient sums nonpositive for any of these boxes: its dot product with the displayed positive vector \(b\) would otherwise be both positive and nonpositive. This is a genuine all-frequency restriction **only on this family**.

## Evidence and limits

- Frozen exact boundary root factorizations, endpoint vectors, five marker intervals, numerator, pairing factorizations, all Bernstein leaves and margins: `frontier-20261028-five-contact-uniform-numerator-frozen-v1.json`, SHA-256 `ca236e378ba9e5d9d8686dfe5e7cbc718799edfd59ff6a21bd51104fe7723c45`.
- Independent standalone checker `frontier-20261028-five-contact-independent-replay-kernel-v1.py`, SHA-256 `2821a22b1ad11f7b617e13086f706b137543b911a127066be7fff2710cc2761b`. It rebuilds all four root factorizations, five contacts and center signs, exact center Routh column, all 28 corner Hurwitz minors at \(\rho=999/1000\), four boundary square factorizations, every Bernstein coefficient, center margin and ratio. Corrupted leaf and factor controls were rejected. Receipt `frontier-20261028-five-contact-independent-replay-result-v1.json`, SHA-256 `4fbafafd696f5c6e40eb4b60c26b5c074691278bfc377b04a5abae6defe69a2b`.
- The five-contact candidate was constructed from rational parity-root data and solved by exact limiting-tangent and Bernstein calculations. Search trajectories, including nondecisive physical-grid searches on four designs, are recorded in `frontier-20261028-five-contact-search-results-v1.json`, SHA-256 `495d6d20a2c02159cbab28d23ec57a4f6e9a7b46428f198df32a877b0af4545c`. A positive grid dual alone was not used as a full-halfline proof.

All machine arithmetic used integers and `fractions.Fraction` in one Python Eval host. The written proof imports elementary polynomial signs, root continuity, interval linearity, and Bernstein positivity. It is not formal verification, cross-vendor review, novelty clearance, or a general positive/negative verdict.
