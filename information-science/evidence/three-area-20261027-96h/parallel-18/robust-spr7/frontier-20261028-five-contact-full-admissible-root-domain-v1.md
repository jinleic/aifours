# A uniform-gain SPR construction on the full admissible root domain

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This strengthens the preceding fixed-\(u\) result to **all** coefficient-admissible values of \(u,\lambda,v\) for the five fixed contact nodes \(1,2,3,6,8\). It remains a structured family, not a resolution of arbitrary septic interval boxes.

## Exact admissible domain

Let the boundary parity endpoints be
\[
\begin{aligned}
E_-&=-\lambda(t-u)(t-3)(t-6),&E_+&=-(t-1)(t-2)(t-8),\\
O_-&=-(t-1)(t-6)(t-8),&O_+&=-(t-2)(t-3)(t-v),
\end{aligned}
\]
with \(0<u<1\), \(v>8\), \(\lambda>0\). The exact condition that all seven independent coefficient widths be nonnegative is
\[
\frac{36}{73}\le u\le\frac89,\qquad 10\le v\le\frac{56}{5},
\qquad L(u)\le\lambda\le H(u),
\]
where
\[
L(u)=\frac{26}{9u+18},\qquad
H(u)=\begin{cases}
11/(u+9),&u\le72/91,\\
8/(9u),&u\ge72/91.
\end{cases}
\]
To verify this, the even-width coefficients are
\[
16-18\lambda u,\quad \lambda(9u+18)-26,\quad
11-\lambda(u+9),\quad \lambda-1,
\]
and the odd-width coefficients are \(6v-48,56-5v,v-10\). The two possible upper bounds for \(\lambda\) cross at \(72/91\); their intersection with the lower bounds is exactly the stated \(u\)-interval. All lower coefficients remain positive. Some widths vanish at boundary parameter values; zero widths are allowed. The even and odd endpoint differences are not identically zero and are strictly positive at every positive marker.

Let \(K_{u,\lambda,v,\rho}\) be the radial subbox centered at the boundary-box midpoint with \(0\le\rho<1\). The five markers \(1,2,3,6,8\) give alternating even/odd signs, hence disjoint interlacing root bands for every member. Every such box is strictly Hurwitz. At \(\rho=1\) actual corners have imaginary roots at the five markers, so larger nested boxes are not all-member strictly Hurwitz.

## One gain for the entire domain

For each allowed \(u,\lambda,v\), form the same five tangent rows and \(5\times5\) matrix \(M\) described in `frontier-20261028-five-contact-uniform-gain-region-v1.md`, with actual contact corners \((2,1),(3,2),(1,3),(0,6),(2,8)\). Put
\[
r_i=-d_{i0}-1000d_{i6}-d_{i7},\qquad D=\det M,
\]
and let \(M_j\) replace column \(j\) by \(r\). The **same gain** \(b_6/b_7=1000\) works throughout the domain; the other coefficients depend on the shape.

For the exact polynomial certificate, parameterize \(\lambda=(1-z)L(u)+zH(u)\), \(0\le z\le1\), and set
\[
d(u)=\begin{cases}(9u+18)(u+9),&u\le72/91,\\
(9u+18)(9u),&u\ge72/91.\end{cases}
\]
Use the unnormalized vector
\[
\widetilde b_0=\widetilde b_7=-D\,d(u)^3,\quad
\widetilde b_6=-1000D\,d(u)^3,\quad
\widetilde b_j=-\det(M_j)d(u)^3\quad(1\le j\le5).
\]
All eight coefficients are strictly positive over both closed branches, so \(D\ne0\) and the monic vector is obtained by dividing by \(\widetilde b_7\). For every allowed shape, that one numerator works for **every** \(\rho<1\), every denominator in the box, and every real frequency.

The exact certificate establishes the uniform midpoint bound
\[
P_{\mathrm{center},\widetilde b}(t)/(1+t)^7\ge
m:=\frac{267982001098326204748922880}{1655595487}>0
\]
for the displayed **unnormalized** vector. Each boundary pairing is nonnegative after its contact-square factors are removed. Since \(1+\sum u_j<207\) throughout the domain,
\[
\operatorname{Re}\frac{\widetilde b(i\omega)}{a(i\omega)}\ge
(1-\rho)\frac{3308419766646002527764480}{875810012623}>0.
\]
This is a conservative bound for the scaled vector; it is not claimed for its monic normalization without rescaling. The same positivity excludes any finite nonpositive-coordinate atom certificate for every box in this family.

## Why the finite tensor check proves the continuum

The tangent matrix has at most two rows involving \(E_-\) and at most two involving \(O_+\). After substituting the rational \(\lambda\)-parameterization, its Cramer determinants times \(d(u)^3\) are polynomial of degree at most \((6,2,2)\) in \((u,z,v)\); multiplication by a boundary parity endpoint gives pairing coefficients of degree at most \((6,3,3)\), with the one possible factor \(1/d(u)\) canceled by the built-in positive \(d(u)\) factor. Contact-square division and frequency Bernstein conversion are linear operations and do not increase those parameter degrees.

For each branch, the eight numerator coefficients, four boundary residual families and center pairing give 110 parameter polynomials over fixed frequency leaves of counts 3, 4, 1, 4, 4. Every one of their \(110\times7\times4\times4=12{,}320\) tensor Bernstein coefficients is strictly positive. The two branch minima are respectively
\[
\frac{49278589881016792591329914880}{151334226289},\qquad
\frac{267982001098326204748922880}{1655595487}.
\]
The smaller is \(m\). Nonnegative Bernstein basis functions then establish all boundary and midpoint inequalities for the entire continuous domain, including admissible edge degeneracies. Affine pairing and the fixed midpoint prove the entire radial family.

The simple bound \(S=207\) is valid because the upper coefficients are bounded by \(16,336/5,31,62,11,81/5,2\): \(v\le56/5\), \(u\le8/9\), and \(\lambda\le73/63\) give \(\lambda(9u+18)<31\). Adding one for the monic term gives a value below 207.

The result also holds after any common positive frequency scaling: for \(c>0\), replace every denominator \(p\) by \(\widehat p(s)=c^7p(s/c)\) and its numerator by \(\widehat b(s)=c^7\widetilde b(s/c)\). The seven coefficient intervals scale independently by \(c^{7-j}\), the five contact values of \(t\) become \(c^2(1,2,3,6,8)\), and \(\widehat b(i\omega)/\widehat p(i\omega)=\widetilde b(i\omega/c)/p(i\omega/c)\). The same ratio bound therefore applies. The gain \(b_6/b_7\) scales by \(c\); 1000 is the unscaled value.

## Frozen evidence and limits

Frozen branch domains, partitions, degree bounds and constants: `frontier-20261028-five-contact-full-u-branches-frozen-v1.json`, SHA-256 `64902389e1915aec3218a28ada0e0d9ff791f12ecbcecf0468f44fe144aac81c`. Independent standalone replay `frontier-20261028-five-contact-full-u-branches-independent-kernel-v1.py`, SHA-256 `4675aacab3739df7c9f8ef6c72a9b6732cf803e8218d3fc17ab2f5a01be612fc`, reconstructs both rational parameterizations and Cramer determinants with integer Bareiss, replays dyadic frequency leaves by de Casteljau and parameter coefficients by a separate Vandermonde/power-to-Bernstein route, and checks all 24,640 strict tensor coefficients and the stated uniform ratio constant. Receipt `frontier-20261028-five-contact-full-u-branches-independent-result-v1.json` has SHA-256 `15efc62481476d5c5bfe41b4f3c07ebc773703fef296ef84ee485b32241ba46c`.

This resolves the entire admissible \((u,\lambda,v,\rho)\) domain for the **specified five contact nodes, up to common positive scaling**. It does not prove the high-gain criterion for arbitrary contact-node ratios, prove an arbitrary-box positive theorem, or produce a negative certificate. The parameter-degree, admissibility, sign-band, scaling and convexity arguments are written mathematics; the finite identities were checked with exact integer/`fractions.Fraction` arithmetic on one Python Eval host, not formally or cross-vendor verified.
