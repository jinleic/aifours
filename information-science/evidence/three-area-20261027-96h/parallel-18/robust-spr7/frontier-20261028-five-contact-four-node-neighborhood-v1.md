# An explicit open neighborhood of four five-contact node ratios

**Status: WRITTEN continuation theorem with exact base constants independently replayed; author candidate, not parent adoption.** Unlike the fixed-node result, this permits four contact-node ratios to vary independently. The explicit radius is deliberately astronomically conservative. The family remains structured and does not cover arbitrary septic boxes.

## Statement

Let
\[
H=10^{12},\quad N=10^9,\quad M=(2H)^{2^N},\quad \epsilon=M^{-2}>0.
\]
Choose
\[
t_1=1,\quad |t_2-2|,|t_3-3|,|t_4-6|,|t_5-8|\le\epsilon,
\]
and independently choose
\[
\frac{501}{1000}\le u\le\frac{509}{1000},\quad
\frac{5779}{5000}\le\lambda\le\frac{2891}{2500},\quad
\frac{101}{10}\le v\le\frac{111}{10}.
\]
Define boundary parity endpoints
\[
\begin{aligned}
E_-&=-\lambda(t-u)(t-t_3)(t-t_4),&E_+&=-(t-t_1)(t-t_2)(t-t_5),\\
O_-&=-(t-t_1)(t-t_4)(t-t_5),&O_+&=-(t-t_2)(t-t_3)(t-v).
\end{aligned}
\]
They define seven positive lower coefficients and **seven strictly positive widths**. For every such choice and every radial scale \(0\le\rho<1\), the resulting monic septic box is all-member Hurwitz and has an explicit common degree-seven SPR numerator. The numerator is the positive scaled Cramer vector from the preceding gain-1000 packet, with the five contacts replaced by these \(t_i\); it depends on the root/shape parameters but not on \(\rho\). Every corresponding finite nonpositive-coordinate atom certificate is excluded.

For the unnormalized Cramer vector, the quantitative ratio bound is
\[
\operatorname{Re}[\widetilde b(i\omega)/a(i\omega)]\ge
(1-\rho)\frac{2614056841543193314947}{156250000000000000}>0.
\]
A common positive rescaling of the frequency variable gives the corresponding open family with arbitrary \(t_1>0\); the gain scales with it.

## Proof

At the unperturbed nodes, the 7040-coefficient trivariate tensor certificate in `frontier-20261028-five-contact-trivariate-gain-frozen-v1.json` covers a larger \((u,\lambda,v)\) rectangle and has strict minimum
\[
m=2614056841543193314947/78125000000>1.
\]
Restricting a Bernstein polynomial to the smaller shape rectangle expresses its new Bernstein coefficients as convex combinations of the old ones, so they remain at least \(m\). Direct exact arithmetic at the eight shape corners gives minimum lower coefficient 1 and minimum width \(9481/2500000\); these minima hold throughout the shape rectangle because the endpoint expressions are multiaffine in \((u,\lambda,v)\).

The contact tangent matrix has at most two rows depending on \(E_-\) and at most two depending on \(O_+\). For **any fixed nearby node vector**, its Cramer determinants and all boundary/center frequency-leaf coefficients have degree at most 3 in each of \(u,\lambda,v\). Contact-square division is exact by the tangent identities and is polynomial in the contact nodes. Thus every parameter Bernstein coefficient is a polynomial function of \((t_2,t_3,t_4,t_5)\).

The same deliberately loose arithmetic-circuit bound used in `frontier-20261028-contact-node-explicit-radius-addendum-v1.md` applies to every one of these coefficient functions and every endpoint/width function: on the node box of radius \(1/10\), all primitive values and first partial derivatives are below \(H\); a pivot-free Leibniz/Cramer evaluation of one tensor coefficient uses fewer than \(N\) additions and multiplications and fixed rational constants. There is no division by the determinant. Thus every partial derivative has absolute value below \(M\). Moving four node coordinates by at most \(\epsilon=M^{-2}\) changes any such quantity by at most \(4/M\), which is smaller than half of each positive base bound above. Hence all seven widths remain strict, all numerator/leaf tensor coefficients remain above \(m/2\), and the determinant cannot vanish.

Because \(\epsilon<1/10\), the root order \(0<u<t_1<t_2<t_3<t_4<t_5<v\) persists. Coefficientwise positivity of both parity endpoint differences makes the five alternating marker signs strict at every \(\rho<1\), so all parity roots remain in disjoint interlacing bands and the whole box is Hurwitz. Each boundary pairing has exact contact-square factors and strictly positive residuals, while the center compactified pairing is at least \(m/2\). Affine pairing over the independent coefficient box gives \(P/(1+t)^7\ge(1-\rho)m/2\).

On the much larger auxiliary node box of radius \(1/10\), the seven upper coefficients are bounded by \(20,80,60,65,12,18,2\), respectively; with the monic term their sum is below 1000. This proves the displayed ratio bound. The bound is not claimed sharp or practically sized, and no numerical expansion of \(M\) is required.

## Evidence and scope

The source trivariate tensor data are hash-bound as `frontier-20261028-five-contact-trivariate-gain-frozen-v1.json`, SHA-256 `e7472e4aff2f02e04e8257724886409cbdc4a3632ebd1cd0fc2e6aa055e05764`; the independent tensor receipt has SHA-256 `008ab0aef65ae08b868eb4632687f5915cdde35ba9d33610ba0a9814f25dfb64`. The new interior shape bounds and symbolic radius are frozen in `frontier-20261028-five-contact-four-node-neighborhood-frozen-v1.json`, SHA-256 `70ad5d5e8530286c301c2f8a7385c45756485c867e59967dcaa1bc1d78d4daf7`. Independent base checker `frontier-20261028-five-contact-four-node-neighborhood-independent-kernel-v1.py`, SHA-256 `043df8dc813053c098ddc0aa5e98020bc4397b7dea350b12f325e9649d863207`, verifies the eight shape-corner bounds, tensor-minimum binding and ratio constant; receipt `frontier-20261028-five-contact-four-node-neighborhood-independent-result-v1.json` has SHA-256 `d35915642eb65a20866a489d4a5f1943858e2fef01225fe108f85c10e2034ed8`.

The multivariate circuit/continuity, root-band and homotopy arguments are written mathematics; the finite base identities are exact rational checks on one Python Eval host. This is not a formal proof, cross-vendor review, novelty clearance, or a verdict for arbitrary septic interval boxes.
