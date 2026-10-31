# A rigorous local variation of a five-contact node ratio

**Status: WRITTEN continuation theorem from the independently replayed fixed-node tensor certificate; author candidate, not parent adoption.** This proves the construction persists on a nonempty open range of contact-node ratios. It does not give a numerical lower bound for that range and does not resolve arbitrary septic boxes.

## Statement

Replace the last contact node 8 in the preceding full-domain theorem by \(w\). There exists a real \(\varepsilon_*>0\) such that for every \(w\in[8,8+\varepsilon_*]\), **every** coefficient-admissible shape in the family
\[
\begin{aligned}
E_-&=-\lambda(t-u)(t-3)(t-6),& E_+&=-(t-1)(t-2)(t-w),\\
O_-&=-(t-1)(t-6)(t-w),& O_+&=-(t-2)(t-3)(t-v)
\end{aligned}
\]
has a common exact-degree-seven SPR numerator on every radial subbox \(0\le\rho<1\). The dimensionless gain \(b_6/b_7=1000\) is the same throughout. The numerator coefficients depend on the shape, but not on \(\rho\).

More precisely, the **entire** nonnegative-width domain for \(8\le w\le9\) is
\[
\begin{gathered}
u_{\min}(w)=\frac{9w-36}{6w+25}\le u\le
u_{\max}(w)=\frac{w}{w+1},\qquad
w+2\le v\le\frac{7w}{5},\\
L(u,w)=\frac{2+3w}{9u+18}\le\lambda\le H(u,w),\\
H(u,w)=\begin{cases}
(w+3)/(u+9),&u\le u_s(w):=9w/(8w+27),\\
w/(9u),&u\ge u_s(w).
\end{cases}
\end{gathered}
\]
Zero widths at parameter-boundary points are permitted. For the sufficiently small range of \(w\) in the statement, the scaled Cramer construction from the fixed-node theorem works for this whole domain, with a uniform ratio lower bound
\[
\operatorname{Re}[\widetilde b(i\omega)/a(i\omega)]\ge
(1-\rho)\frac{418721876716134694920192}{5173735896875}>0.
\]
The bound is for the unnormalized, denominator-cleared Cramer vector; monic normalization changes it by a positive factor.

## Proof

The even endpoint-width coefficients are
\[
2w-18\lambda u,\quad \lambda(9u+18)-(2+3w),\quad
w+3-\lambda(u+9),\quad\lambda-1,
\]
and the odd widths are \(6(v-w),7w-5v,v-w-2\). For \(w\in[8,9]\), their simultaneous nonnegativity is exactly the stated domain. The upper branches cross at \(u_s\); the feasibility bounds are \(u_{\min}\) and \(u_{\max}\). In particular,
\[
u_s-u_{\min}=\frac{18(18-w)(w+3)}{(8w+27)(6w+25)}>0,
\quad
u_{\max}-u_s=\frac{w(18-w)}{(w+1)(8w+27)}>0.
\]
All lower coefficients are positive, \(0<u<1<2<3<6<w<v\), and neither parity endpoint difference vanishes identically. The five marker sign pattern therefore gives disjoint interlacing root bands for every radial box with \(\rho<1\), including width-degenerate domain edges. Every denominator is strictly Hurwitz; the boundary has the five stated imaginary contacts.

Parameterize each of the two \(u\)-branches by \(x\in[0,1]\), its \(\lambda\)-interval by \(z\in[0,1]\), and its \(v\)-interval by \(y\in[0,1]\), using affine interpolation of the displayed endpoints. Let \(d=(9u+18)(u+9)\) on the first branch and \(d=(9u+18)(9u)\) on the second. The same five tangent equations, gain 1000 and scaled Cramer vector \(\widetilde b=-d^3\) times the corresponding determinants apply, now with last contact \(w\).

For every fixed \(w\in[8,9]\), the eight numerator coefficients, boundary residual leaf coefficients and center pairing leaf coefficients are polynomials of degree at most \((6,3,3)\) in \((x,z,y)\). The bound follows exactly as in the fixed-node packet: only two tangent rows involve \(E_-\), only two involve \(O_+\), and the single possible \(1/d\) in a denominator pairing is canceled by a built-in \(d\) factor. Division by the monic contact factors \((t-t_i)^2\), including \((t-w)^2\), is polynomial in \(w\) and does not increase those three parameter degrees.

At \(w=8\), the frozen certificate in the preceding theorem checks all **24,640** tensor Bernstein coefficients strictly positive, with common lower bound
\[
m=267982001098326204748922880/1655595487.
\]
For fixed parameter degrees and fixed compact-frequency leaves, each of these finitely many tensor coefficients is a continuous rational function of \(w\) near 8: all parameterization denominators are strictly positive. Hence there is some \(\varepsilon_*>0\) for which every coefficient in both branches stays above \(m/2\) on \([8,8+\varepsilon_*]\). This simultaneously proves positive numerator coefficients, nonnegative boundary pairings with exact contact factors, and a center compactified pairing of at least \(m/2\), for all shapes in the moving admissible domain. Affine pairing over the radial box completes the synthesis proof.

A simple uniform bound \(S\le1000\) for \(1+\sum_j u_j\) holds for \(w\in[8,9]\): the upper coefficients are bounded by \(18,76,54,69,12,18,2\), and one adds the monic term. Here \(\lambda<2\) follows from the displayed upper branch bounds. Therefore \((m/2)/1000^2\) is the stated ratio constant. The existence of \(\varepsilon_*\) is a complete continuity conclusion but is **not an explicit numerical radius**.

## Evidence and diagnostic

The fixed-node tensor certificate and its independent replay are `frontier-20261028-five-contact-full-u-branches-frozen-v1.json`, SHA-256 `64902389e1915aec3218a28ada0e0d9ff791f12ecbcecf0468f44fe144aac81c`, and `frontier-20261028-five-contact-full-u-branches-independent-result-v1.json`, SHA-256 `15efc62481476d5c5bfe41b4f3c07ebc773703fef296ef84ee485b32241ba46c`. The ratio constant is exactly \(m/(2\cdot1000^2)\).

As a **diagnostic only**, exact Cramer/Bernstein calculations at the 16 parameter vertices for \(w=8000001/1000000\) were all positive; `frontier-20261028-contact-node-variation-samples-result-v1.json` has SHA-256 `ce9e620306872ff1ebe41081c993bf87fc1c8a7a3c1d79f42022b9135284e500`. Those finite samples do not establish that \(10^{-6}\) is a valid choice of \(\varepsilon_*\), and the theorem does not assert that they do.

The continuation, admissibility, degree and stability arguments are written mathematics; the tensor and diagnostic arithmetic used exact integers/`fractions.Fraction` in one Eval host. This is not formal verification, cross-vendor review, novelty clearance, or an unrestricted septic verdict.
