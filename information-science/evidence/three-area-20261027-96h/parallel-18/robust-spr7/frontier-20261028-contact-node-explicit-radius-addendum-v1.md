# An explicit conservative contact-node continuation radius

**Status: WRITTEN bound from the frozen exact tensor certificate; author candidate, not parent adoption.** This additive result strengthens `frontier-20261028-five-contact-node-continuation-v1.md`, which proved a positive radius existed but did not quantify it. The bound below is deliberately enormous in exponent and is not claimed useful numerically.

Let
\[
H=10^{12},\qquad N=10^9,\qquad
M=(2H)^{2^N},\qquad \varepsilon_0=M^{-2}.
\]
Then the conclusion of the continuation theorem holds for every
\[
8\le w\le8+\varepsilon_0.
\]
This is an explicit positive rational number, specified symbolically; the enormous integer is not expanded or computed. In particular the common unnormalized Cramer numerator with gain 1000 works for every admissible shape and every \(0\le\rho<1\) in that interval, with the same \((1-\rho)m/(2\cdot1000^2)\) lower bound from the preceding packet.

## Bound on the coefficient functions

Fix either rational \(u\)-branch, one of the 110 compact-frequency leaf/numerator polynomials, and one of its degree-\((6,3,3)\) parameter Bernstein coefficients \(f(w)\). The fixed-node independent replay gives \(f(8)\ge m>1\), uniformly over all 24,640 coefficients in the two branches.

On \(w\in[8,9]\), normalize each admissible branch by parameters \(x,z,y\in[0,1]\), as in the preceding packet. The following deliberately loose bounds hold uniformly for the values **and first \(w\)-derivatives** of the primitive functions:

- \(0<u<1\), \(|u'|<1\), \(|\lambda|<2\), \(|\lambda'|<5\), \(|v|<13\), \(|v'|<2\).
- Both clearing factors \(d\) are positive, at least 1, and satisfy \(|d|,|d'|<1000\).
- The fixed inverse Bernstein interpolation matrices of degrees 6 and 3 have maximum absolute entries 30 and 3, respectively; their maximum row \(\ell^1\)-norms are \(2231/25\) and \(17/3\). Frequency-leaf endpoints have denominators at most 8. In particular all fixed rational constants used below have value and derivative norm below \(H\).

The first two bounds follow by differentiating the explicit rational formulas: their variable denominators are at least 1 on \([8,9]\). The interpolation constants were computed exactly in `frontier-20261028-contact-node-continuation-interpolation-bounds-v1.json`, SHA-256 `c9875f83da45168b5cbaf2c79fe0e09022ade668cdf8d739e8df72f93a984d13`.

Define an evaluation of \(f(w)\) using only additions, multiplications and divisions by those positive parameter denominators or fixed nonzero constants. Use the Leibniz formula for each \(5\times5\) Cramer determinant—**not** Gaussian pivot division—and synthetic division by the monic contact factors. A direct overcount gives fewer than \(10^5\) scalar arithmetic operations per parameter sample: six determinants have 120 terms each; the five pairing polynomials, contact divisions and fixed frequency-leaf transformations are smaller. One parameter Bernstein coefficient uses 112 samples plus a fixed tensor interpolation, so fewer than \(10^9=N\) scalar operations suffice even when everything is recomputed separately. This is a coarse written circuit bound, not a claim that the software executed a billion operations.

For a scalar function and derivative both bounded in absolute value by \(B\ge H\), one such addition, multiplication, or division by a denominator of absolute value at least 1 is bounded by \(2B^2\); fixed smaller denominators are absorbed into the constant bound \(H\). Induction from \(B_0=H\) gives
\[
B_N\le\tfrac12(2H)^{2^N}<M.
\]
Thus \(|f'(w)|<M\) throughout \([8,9]\), uniformly over both branches and all coefficient indices. By the mean-value theorem, for \(w\in[8,8+M^{-2}]\),
\[
f(w)>m-M\varepsilon_0=m-M^{-1}>m/2.
\]
Every numerator, boundary-residual and center-leaf Bernstein coefficient therefore remains strictly positive, and the stability and radial-box argument in the preceding packet applies. The diagnostic at \(w=8000001/1000000\) remains only a diagnostic; this proof does not claim that its much larger displacement lies within \(\varepsilon_0\).

This is a deliberately conservative written bound built from the exact fixed-node tensor certificate, explicit rational parameterization, and the stated circuit overcount. The derivative bound and continuation are not machine-checked universal quantifications, formal verification, a cross-vendor review, novelty clearance, or an unrestricted septic verdict.
