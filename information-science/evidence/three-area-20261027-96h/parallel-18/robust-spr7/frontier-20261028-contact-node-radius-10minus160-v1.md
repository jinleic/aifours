# A simpler explicit contact-node continuation radius

**Status: WRITTEN bound from the frozen tensor certificate; author candidate, not parent adoption.** This additive refinement replaces the much smaller tower-form radius in `frontier-20261028-contact-node-explicit-radius-addendum-v1.md` by the still very conservative but explicitly ordinary rational radius
\[
\boxed{\varepsilon=10^{-160}.}
\]
For every \(w\in[8,8+10^{-160}]\), the full moving admissible \((u,\lambda,v)\) domain and every radial \(0\le\rho<1\) have the gain-1000 common numerator described in `frontier-20261028-five-contact-node-continuation-v1.md`, with the same unnormalized ratio bound \((1-\rho)m/(2\cdot1000^2)\). This is a structured-family result, not an unrestricted septic verdict.

## Coarse derivative bound

The fixed-node certificate has minimum tensor coefficient
\[
m=267982001098326204748922880/1655595487>1.
\]
For a fixed branch and normalized parameters \(x,z,y\in[0,1]\), use the rational parameterization, cleared Cramer numerator, fixed compact-frequency leaves and degree-\((6,3,3)\) Bernstein interpolation of the continuation packet. On \(w\in[8,9]\), the following uniform **absolute** bounds hold for values and first \(w\)-derivatives:

| Quantity | Value bound | Derivative bound |
|---|---:|---:|
| Each boundary cubic coefficient | \(5\cdot10^3\) | \(2\cdot10^4\) |
| Each contact tangent-row entry | \(10^{11}\) | \(10^{12}\) |
| Each entry of a Cramer matrix or its replaced column, including gain 1000 | \(10^{15}\) | \(10^{16}\) |
| Each corresponding \(5\times5\) determinant, by its 120-term Leibniz formula | \(10^{78}\) | \(10^{79}\) |
| Each cleared numerator coefficient, including \(b_6=1000b_7\) | \(10^{90}\) | \(10^{92}\) |
| Each boundary/center pairing coefficient before contact division | \(10^{95}\) | \(10^{97}\) |

For example, \(|u'|<1\), \(|\lambda'|<5\), \(|v'|<2\), roots and \(v\) are below 13, and \(0<\lambda<2\). The clearing denominator satisfies \(|d|<270\), \(|d'|<1000\), so \(|d^3|<10^8\), \(|(d^3)'|<10^9\). A tangent row contains at most an endpoint derivative times \(t^4\), with \(t\le9\); the table follows by product differentiation and elementary overbounds.

There are at most four synthetic divisions by monic contact factors. For a root and its derivative bounded by 9 and 1, respectively, each division increases the combined coefficient/derivative bound by less than \(10^9\); hence each residual-coefficient derivative is below \(10^{133}\). Frequency compactification followed by a fixed de Casteljau leaf is a convex linear combination of the residual coefficients divided by binomial coefficients, so it does not increase that bound. The exact inverse Bernstein interpolation row-norm bounds in the preceding packet are \(2231/25<90\) for degree 6 and \(17/3<6\) for degree 3. Their product is below \(10^4\), so every parameter tensor Bernstein coefficient has
\[
|f'(w)|<10^{137}<10^{150}\qquad(8\le w\le9).
\]
The mean-value theorem now gives \(|f(w)-f(8)|<10^{-10}<1/2\) for \(8\le w\le8+10^{-160}\). Since each fixed-node coefficient is at least \(m>1\), all remain above \(m/2\). This proves the claimed radius and ratio bound exactly as in the continuation packet. It does **not** certify the separate diagnostic displacement \(10^{-6}\).

The fixed-node exact certificate and independent replay remain those pinned in the continuation packet. These derivative estimates are conservative written mathematics, not a machine-checked universal bound, formal proof, cross-vendor review, novelty claim, or general septic solution.
