# The maximal admissible node interval for the five-contact construction

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This additive theorem strengthens the preceding \([8,17]\) result to the full **\([8,18]\)** interval. In fact, with the first four contact nodes fixed at \((1,2,3,6)\), no coefficient-admissible member of this pattern exists with \(w>18\). The result does not cover arbitrary node ratios or arbitrary septic boxes.

## Exact maximal domain

Use the boundary parity endpoints and the \((u,\lambda,v)\) inequalities in `frontier-20261028-five-contact-wide-node-interval-theorem-v1.md`. For every \(w\ge8\), simultaneous nonnegativity of the independent coefficient widths implies
\[
\frac{9w-36}{6w+25}\le u\le\frac{w}{w+1}.
\]
This interval can be nonempty only when
\[
(w-18)(3w+2)\le0,
\]
so \(w\le18\). Conversely, for every \(8\le w\le18\), the two branches, \(w+2\le v\le7w/5\), and the displayed lower/upper bounds for \(\lambda\) give the entire nonnegative-width domain. At \(w=18\), the \(u\)-interval collapses to \(18/19\) and \(\lambda=19/9\); this is an allowed degenerate coefficient-width edge, not an empty box. Lower coefficients remain positive and the two parity endpoint differences remain nonzero at positive frequencies.

For every admissible shape with \(8\le w\le18\), all midpoint-centered radial boxes \(0\le\rho<1\) are strictly Hurwitz and have a common exact-degree-seven numerator with the same dimensionless gain \(b_6/b_7=1000\). Its remaining coefficients are the explicitly specified Cramer expressions in the \([8,9]\) theorem, using the same positive \(Q(w)^6d^3\) clearing. At \(\rho=1\) actual corners have the five imaginary-axis contacts; larger boxes are ineligible. A common positive frequency scaling gives all contact nodes proportional to \((1,2,3,6,w)\).

For the unnormalized numerator, the exact midpoint compactified pairing is uniformly at least
\[
m=48848901567473582766244507224637440>0,
\]
and all four boundary pairings are nonnegative after their contact-square factors. For every member,
\[
\operatorname{Re}\frac{\widehat b(i\omega)}{a(i\omega)}\ge
(1-\rho)\frac{610611269593419784578056340307968}{3125}>0.
\]
The bound is for the unnormalized vector. It excludes every finite nonzero nonnegative atom combination with all coefficient sums nonpositive for each box in this family, not for unrelated boxes.

The conservative denominator coefficient bound \(1+\sum u_j<500\) remains valid at \(w=18\): \(v\le126/5\), \(\lambda<3\), and the seven upper coefficients are at most \(36,152,81,132,21,31,3\), respectively. The five-marker sign-band argument remains strict at every positive marker even if some coefficient widths vanish.

## Exact tensor replay

The frequency leaves and degree \((23,6,3,3)\) argument are the same as for \([8,17]\). Each parameter branch has 116 scalar functions and 311,808 strictly positive tensor Bernstein coefficients. Independent exact replay checked all **623,616** coefficients on the closed \([8,18]\) interval; the two branch minima remain
\[
27983795977368197193399348944373796270080,\qquad
48848901567473582766244507224637440.
\]
The smaller is \(m\).

Frozen domain, partitions and constants: `frontier-20261028-five-contact-maximal-node-interval-frozen-v1.json`, SHA-256 `46abb1c91770cc14137f317efdfbc16383fa306331efd59e298627d7837cac19`. Standalone independent checker `frontier-20261028-five-contact-maximal-node-interval-independent-kernel-v1.py`, SHA-256 `b6e5b08fabb70801fb1e82c25c5399cacc3680da5c252a9861d2d5fb53a181a8`, uses integer Bareiss, dyadic de Casteljau and a distinct monomial-Vandermonde/power-to-Bernstein conversion. Receipt `frontier-20261028-five-contact-maximal-node-interval-independent-result-v1.json` has SHA-256 `79e1d842cccb78e4b89e2b45fbf5c2ad27ec829928f8c5a07fa3f943e328729e`.

The maximality, parameter-degree, sign-band and radial-affinity arguments are written mathematics; the finite tensor identities were checked with exact integers and `fractions.Fraction` on one Python Eval host. This is not formal or cross-vendor verification, novelty clearance, an arbitrary-box theorem, or a negative certificate.
