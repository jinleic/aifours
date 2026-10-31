# Exact uniform-gain synthesis for a full interval of contact-node ratios

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This strengthens the preceding tiny-radius node-continuation results to the entire interval \(8\le w\le9\), with **all** coefficient-admissible shape parameters and all radial scales below the stability boundary. It does not solve arbitrary septic interval boxes.

## Family and result

Take five contact nodes \(1,2,3,6,w\), where \(8\le w\le9\), and define
\[
\begin{aligned}
E_-&=-\lambda(t-u)(t-3)(t-6),& E_+&=-(t-1)(t-2)(t-w),\\
O_-&=-(t-1)(t-6)(t-w),& O_+&=-(t-2)(t-3)(t-v).
\end{aligned}
\]
The exact nonnegative-width domain is
\[
\begin{gathered}
u_{\min}(w)=\frac{9w-36}{6w+25}\le u\le
u_{\max}(w)=\frac{w}{w+1},\qquad
w+2\le v\le\frac{7w}{5},\\
\frac{2+3w}{9u+18}\le\lambda\le
\begin{cases}
(w+3)/(u+9),&u\le9w/(8w+27),\\
w/(9u),&u\ge9w/(8w+27).
\end{cases}
\end{gathered}
\]
This follows by coefficientwise nonnegativity of \(E_+-E_-\) and \(O_+-O_-\), as derived in the node-continuation packet. Some widths may vanish on the domain boundary; all lower coefficients remain positive.

For every allowed \((w,u,\lambda,v)\), form the independent monic septic boundary box and its midpoint-centered radial subboxes \(K_\rho\). Every member is strictly Hurwitz for \(0\le\rho<1\); at \(\rho=1\), actual corners have imaginary-axis roots at all five contact values. A single exact-degree-seven numerator for each shape works on **all** \(K_\rho\), \(\rho<1\), with the same dimensionless gain \(b_6/b_7=1000\). The coefficients vary with the shape, not with \(\rho\).

The numerator is the tangent-equation Cramer vector from the preceding full-root-domain theorem, with the last contact replaced by \(w\). Parameterize each admissible \(u\)-branch by \(x\in[0,1]\), its \(\lambda\)-interval by \(z\in[0,1]\), and its \(v\)-interval by \(y\in[0,1]\). Let
\[
d=(9u+18)\begin{cases}u+9,&\text{branch 1},\\9u,&\text{branch 2},\end{cases}
\quad
Q(w)=\begin{cases}(6w+25)(8w+27),&\text{branch 1},\\(8w+27)(w+1),&\text{branch 2}.\end{cases}
\]
If \(D\) and \(D_j\) are the tangent and replaced-column determinants with \(b_0=b_7=1,b_6=1000\), use the **unnormalized** positive polynomial vector
\[
\widehat b_0=\widehat b_7=-D\,d^3Q(w)^6,\quad
\widehat b_6=-1000D\,d^3Q(w)^6,\quad
\widehat b_j=-D_jd^3Q(w)^6\ (1\le j\le5).
\]
Its leading coefficient is strictly positive and may be divided out for a monic numerator. The exact certificate proves every boundary corner pairing nonnegative, with only its contact-square zeros, and the midpoint pairing strictly positive throughout the entire shape domain.

For this unnormalized vector, the uniform midpoint compactified margin is at least
\[
m=48848901567473582766244507224637440>0.
\]
The sum of upper coefficient bounds plus the monic term is below 250, giving for every eligible member
\[
\operatorname{Re}\frac{\widehat b(i\omega)}{a(i\omega)}\ge
(1-\rho)\frac{2442445078373679138312225361231872}{3125}>0.
\]
This large value reflects the deliberately unnormalized Cramer scaling. Since \(\widehat b\) has positive coefficients, no finite nonzero nonnegative atom combination for any box in this family can have all coefficient sums nonpositive.

Any common positive frequency scaling \(p(s)\mapsto c^7p(s/c)\), \(c>0\), preserves the ratio and extends the contact nodes to \(c^2(1,2,3,6,w)\). The gain scales by \(c\); 1000 is the unscaled value.

## Why a finite exact tensor check covers all shapes

Write \(u=N_u/Q\), where \(Q\) is the appropriate polynomial above; \(N_u,Q\) have degree at most two in \(w\). For either branch, the rational \(\lambda\) can be written \(Q N_\lambda/(AB)\), with \(A,B\) of degree at most two and \(N_\lambda\) of degree at most three in \(w\). An \(E_-\) coefficient or derivative then has numerator degree at most five over \(AB\). Only two of the five tangent rows involve \(E_-\). After multiplying a tangent or Cramer determinant by \((AB)^2\), its degree in \(w\) is at most 18; multiplication by the remaining \(AB\) in \(d^3Q^6\) makes each \(\widehat b_j\) degree at most 22. Pairing with a boundary or midpoint denominator has degree at most 23 in \(w\).

All contact-square divisions are exact polynomial identities. Division by the moving factor \((t-w)^2\) cannot increase the degree in \(w\): in the polynomial ring, the degree in \(w\) of a nonzero product is the sum of the degrees. Frequency Bernstein conversion is linear. The resulting numerator, four boundary-residual and center-leaf scalar functions therefore have degree at most
\[
(23,6,3,3)\quad\text{in }(w,x,z,y).
\]
For each branch, the 110 scalar functions have \(24\cdot7\cdot4\cdot4=2688\) tensor Bernstein coefficients apiece. **All 295,680 coefficients per branch are strictly positive**, 591,360 in total. Their branch minima are
\[
27983795977368197193399348944373796270080,\qquad
48848901567473582766244507224637440.
\]
The smaller is the displayed \(m\). Bernstein positivity gives nonnegative boundary pairings and a strict midpoint margin throughout the continuum. Coefficientwise affine interpolation from the midpoint and the four actual boundary corners gives the result for every \(\rho<1\).

The stability sign sequence at \(0,1,2,3,6,w,\infty\) is \((+,+),(-,+),(-,-),(+,-),(+,+),(-,+),(-,-)\) for every \(\rho<1\). Nonnegative width coefficients and nonidentical endpoints give strict signs at positive markers even when some widths vanish. The even and odd roots lie in disjoint alternating bands, so no denominator has an imaginary-axis root. The midpoint has the same interlacing and is Hurwitz by the odd-degree Hermite–Biehler criterion; the connected-box homotopy then proves all-member stability.

## Exact evidence and limits

Frozen domains, positive scaling, tensor partitions, degree bounds and minima: `frontier-20261028-five-contact-node-interval-tensor-frozen-v1.json`, SHA-256 `27a53fc2c1b03bc9886b8a26a096edd4b2f1834c5370eaf752b023303c66f0ed`. Independent standalone replay `frontier-20261028-five-contact-node-interval-independent-kernel-v1.py`, SHA-256 `45318617fec457c000cd4c4453f8a1875b773da4aca18a166280841f48531a4e`, uses integer Bareiss determinants, dyadic de Casteljau frequency subdivision, and a separate monomial-Vandermonde/power-to-Bernstein parameter conversion. It independently checks all 591,360 tensor coefficients strictly positive and the two exact minima. Receipt `frontier-20261028-five-contact-node-interval-independent-result-v1.json` has SHA-256 `e39d9ce4869b9d6147d3f2552ed70abe2a2c11008855fc1552046a2b1290f5af`.

This proof covers the entire admissible \((w,u,\lambda,v,\rho)\) domain only for the first four fixed contact nodes \((1,2,3,6)\), up to common positive scaling. It does not establish the claim for arbitrary contact-node ratios, prove a universal positive result, or supply a negative certificate. Parameter-degree, admissibility, root-band and homotopy arguments are written mathematics; the large finite tensor replay used exact integer/`fractions.Fraction` arithmetic on one Python Eval host, not formal or cross-vendor verification.
