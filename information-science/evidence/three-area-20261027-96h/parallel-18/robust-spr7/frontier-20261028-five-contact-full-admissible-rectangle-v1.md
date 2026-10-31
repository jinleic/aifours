# The full admissible parameter rectangle for the fixed five-contact pattern

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This is an additive strengthening of `frontier-20261028-five-contact-uniform-gain-region-v1.md`: the **same gain 1000 and the same Cramer construction** work on the entire coefficient-admissible \((\lambda,v)\) rectangle for these fixed nodes, not merely the smaller rectangle previously certified. It is still a fixed-node family, not a theorem for all septic interval boxes.

Keep \(u=1/2\), contact nodes \(1,2,3,6,8\), and boundary endpoints
\[
\begin{aligned}
E_-&=-\lambda(t-1/2)(t-3)(t-6),&E_+&=-(t-1)(t-2)(t-8),\\
O_-&=-(t-1)(t-6)(t-8),&O_+&=-(t-2)(t-3)(t-v).
\end{aligned}
\]
The exact conditions for all seven independent interval widths to be nonnegative are
\[
\boxed{\ 52/45\le\lambda\le22/19,\qquad 10\le v\le56/5\ }.
\]
Indeed, the coefficients of \(E_+-E_-\) are
\[
16-9\lambda,\quad(45/2)\lambda-26,\quad 11-(19/2)\lambda,\quad\lambda-1,
\]
and those of \(O_+-O_-\) are \(6v-48,56-5v,v-10\). The displayed rectangle is precisely their simultaneous nonnegativity region. Lower endpoints remain positive. At rectangle edges some widths vanish, which is allowed; for interior \((\lambda,v)\) and \(\rho>0\), all seven widths are positive.

For every point of this **closed** parameter rectangle and every radial scale \(0\le\rho<1\), the corresponding septic box is all-member strictly Hurwitz and has one common degree-seven SPR numerator given by the Cramer formula in the previous packet with fixed \(b_6/b_7=1000\). The numerator depends on \((\lambda,v)\), not on \(\rho\). In the scaled notation of that packet, its eight coefficients, all boundary pairing residuals and the midpoint pairing satisfy 1,760 strict bivariate Bernstein inequalities on the full rectangle. Their common minimum is
\[
m=33547441536>0.
\]
The four boundary residuals use 3, 4, 1, 4 frequency leaves, and the midpoint pairing uses 4. The maximal \(1+\sum_j u_j\) over the full rectangle is \(19058/95\). Thus the unnormalized scaled Cramer numerator satisfies the uniform bound
\[
\operatorname{Re}\frac{\widetilde b_{\lambda,v}(i\omega)}{a(i\omega)}
\ge(1-\rho)\frac{75691414965600}{90801841}>0.
\]
As before, normalizing by the strictly positive leading coefficient yields a monic numerator. The expression above is for the unnormalized one.

The stability proof remains the five-marker sign-band argument. Although some individual widths vanish on rectangle edges, the constant differences of both endpoint parity polynomials remain strictly positive, so their five contact sign separations persist for every \(\rho<1\). At \(\rho=1\) the actual boundary corners contain the stated imaginary roots, and every larger radial box contains them. Pairing is affine in the box coefficients, so nonnegative boundary residuals and the strict center margin give the bound for all members. No nonpositive-coordinate finite atom certificate can therefore exist for any box in this family.

## Exact replay

Frozen full rectangle, fixed gain, partitions and constants: `frontier-20261028-five-contact-full-rectangle-uniform-gain-frozen-v1.json`, SHA-256 `922d6c3e463d2ae99bab3c8ae8b0f5041cd86519a6d813c277cef1cc207a5b4b`. Standalone independent replay `frontier-20261028-five-contact-full-rectangle-uniform-gain-independent-kernel-v1.py`, SHA-256 `7e05217e9d1533f4af276fb541c5ff0c8dfa0ca8165c8c0e17034c94813747f3`, independently permits zero widths at the parameter edges, reconstructs the Cramer determinants by integer Bareiss, replays frequency leaves by de Casteljau subdivision and parameter coefficients via a separate Vandermonde/power conversion, checks all 1,760 strict signs and the ratio constant. Receipt `frontier-20261028-five-contact-full-rectangle-uniform-gain-independent-result-v1.json` has SHA-256 `1dc1bd48465369f2994cf65a231bc3443512c74d18f5868160687dca14850d7d`.

The exact proof covers the full admissible rectangle for the **specified roots and \(u\)** only. The high-gain criterion for other root patterns remains conditional on its residual positivity hypotheses; the 436-design screen is not a universal proof. Machine calculations use exact integers and `fractions.Fraction` on one Python Eval host; the degree, stability, and convexity steps are written arguments, not formal or cross-vendor verification.
