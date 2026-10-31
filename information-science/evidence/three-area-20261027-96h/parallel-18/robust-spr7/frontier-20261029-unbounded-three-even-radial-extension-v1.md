# The three forced escapes hold on entire near-boundary radial rays

**Status: WRITTEN corollary, not parent adoption.** Retain the five-contact boundary and determinant numerator \(b_R\) from `frontier-20261029-unbounded-common-numerator-b6-obstruction-v1.md` (SHA-256 `71896c927bafabc2098ab283bc6108a7b259bda028dc58c948cffb637106f8c7`). For every real \(R\ge1000\) and every
\[
1-R^{-4}\le\rho<1,
\]
let \(K_{R,\rho}\) be the corresponding midpoint-centered radial interval box. Then all seven widths are positive, every denominator is Hurwitz, and the **same** explicit monic \(b_R\) is common SPR. Moreover every common monic numerator obeys simultaneously
\[
b_2>R^4/65,\qquad b_4>R^4/100,\qquad b_6>R^2/20.
\]
For \(R\ge5000\), the last bound strengthens to \(b_6>7R^2/80\).

The source's alternating-marker argument and boundary residual factorization already establish stability and strict positivity of \(b_R\) for **every** \(0\le\rho<1\). Meanwhile \(K_{R,1-R^{-4}}\subseteq K_{R,\rho}\), so any common numerator for the larger box must work on the smaller one; the separately pinned positive-atom certificates therefore impose all three necessary bounds. Their denominator atoms are actual members of the larger box, although they need not be its corners. If corner-only atoms are desired, a smaller radial corner is a convex combination of the larger box's midpoint and corresponding corner, and that midpoint is the average of the four larger parity corners; pairing linearity replaces each smaller-corner atom by up to four actual larger-corner atoms with nonnegative weights.

The boundary case \(\rho=1\) is excluded: it contains imaginary-axis contact roots. These are written nesting, affine-pairing and sign arguments based on the pinned exact all-parameter checks. They do not prove an arbitrary-box result, a strict negative-coordinate certificate, formal verification, cross-vendor review, or novelty.
