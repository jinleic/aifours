# Uniform-gain synthesis on the full node interval \(8\le w\le17\)

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This additive theorem strengthens `frontier-20261028-five-contact-node-interval-theorem-v1.md` from \(8\le w\le9\) to the entire much wider interval **\(8\le w\le17\)**. It retains all coefficient-admissible shape parameters and every radial scale below the five-contact stability boundary. It does not cover arbitrary contact-node ratios or arbitrary septic boxes.

For each \(w\in[8,17]\), let
\[
\begin{aligned}
E_-&=-\lambda(t-u)(t-3)(t-6),& E_+&=-(t-1)(t-2)(t-w),\\
O_-&=-(t-1)(t-6)(t-w),& O_+&=-(t-2)(t-3)(t-v),
\end{aligned}
\]
with the **entire** nonnegative-width domain
\[
\begin{gathered}
\frac{9w-36}{6w+25}\le u\le\frac{w}{w+1},\qquad
w+2\le v\le\frac{7w}{5},\\
\frac{2+3w}{9u+18}\le\lambda\le
\begin{cases}(w+3)/(u+9),&u\le9w/(8w+27),\\
w/(9u),&u\ge9w/(8w+27).
\end{cases}
\end{gathered}
\]
The algebraic domain derivation and the two branch parameterizations are unchanged from the preceding packet. Their ordering remains valid because \(w<18\); zero widths at edges are allowed. For every such shape, the corresponding midpoint-centered radial boxes are all-member strictly Hurwitz for \(0\le\rho<1\), and the **same dimensionless gain** \(b_6/b_7=1000\) in the tangent-equation Cramer construction gives a common numerator for all those scales. The other numerator coefficients depend on the shape.

Use exactly the unnormalized vector \(\widehat b\) defined in the preceding \([8,9]\) theorem, including the positive clearing factor \(Q(w)^6\). The independent tensor replay below gives a uniform midpoint compactified pairing lower bound
\[
m=48848901567473582766244507224637440>0.
\]
All four boundary corner pairings are nonnegative after their exact contact-square factors are removed. Hence every eligible member satisfies
\[
\operatorname{Re}\frac{\widehat b(i\omega)}{a(i\omega)}\ge
(1-\rho)\frac{610611269593419784578056340307968}{3125}>0.
\]
This is a conservative bound for the **unnormalized** vector. Normalizing by its strictly positive leading coefficient preserves SPR but rescales the bound. No finite nonpositive-coordinate atom certificate exists for any box in this stated family.

The bound uses \(1+\sum u_j<500\): for \(w\le17\), \(v\le119/5<24\) and both upper-\(\lambda\) branches are below 3. The seven upper coefficients are bounded by \(34,143,81,125,20,29,3\), and the monic term adds one. The five-marker sign-band and homotopy proof is identical to the \([8,9]\) theorem; the first four contact nodes stay fixed and the last remains less than 18.

## Exact wide-interval certificate

The polynomial-degree bound remains \((23,6,3,3)\) in \((w,x,z,y)\), with the same positive denominator clearing; the degree argument is spelled out in the preceding theorem. A single compact-frequency leaf \((7/8,1)\) for the fourth boundary corner was split at \(15/16\); no other leaf was coarsened. The resulting frequency-leaf counts are \(3,4,1,5,4\) for the boundary residuals and midpoint.

Each branch has 116 scalar parameter polynomials and
\[
116\cdot24\cdot7\cdot4\cdot4=311{,}808
\]
strictly positive tensor Bernstein coefficients. The two exact minima are
\[
27983795977368197193399348944373796270080,\qquad
48848901567473582766244507224637440.
\]
The smaller is \(m\). In particular this is a continuum certificate on \([8,17]\), not an interpolation from a few positive slices.

Frozen interval, branch parameterizations, positive scaling, refined leaves and minima: `frontier-20261028-five-contact-wide-node-interval-frozen-v1.json`, SHA-256 `d2e9ebd08c4c5387680c33bc464e35064bf733523fc0512c6e63825a27de0cd4`. Independent standalone replay `frontier-20261028-five-contact-wide-node-interval-independent-kernel-v1.py`, SHA-256 `b68ddf043f671794f2283f9dd28f16d4ba2d7b3cd49ebccef0c5d626730d8ccb`, uses integer Bareiss, dyadic de Casteljau and a separate monomial-Vandermonde/power-to-Bernstein conversion to check all **623,616** strict tensor signs and both minima. Receipt `frontier-20261028-five-contact-wide-node-interval-independent-result-v1.json` has SHA-256 `f14fb45e95dd9488186fdcce25da19c429cb98f9b1d43d961cf9d66bfd0ddbf9`.

The parameter-degree, admissibility, sign-band, coefficient bound and radial-affinity arguments are written mathematics; the finite tensor identities were checked with exact integer/`fractions.Fraction` arithmetic on one Python Eval host. This is not formal or cross-vendor verification, novelty clearance, a universal positive theorem, or an actual negative certificate.
