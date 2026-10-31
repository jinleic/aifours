# The norm-gap criterion is strictly conservative

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** The sufficient condition \(V-H>0\) in `frontier-20261029-norm-gap-heterogeneous-synthesis-v1.md` is not necessary even for the **same center numerator**.

Use the explicit full-width box `frontier-20261029-ultrawide-box-08-frozen-v1.json`, SHA-256 `5f0098d290a9cd9e86e01b90d6faaf453b48a8186d61a1bc1957f79d93383e79`. Let \(m\) be its coefficient midpoint and \(r_j\) its half-widths, and form \(V=E_m^2+tO_m^2\), \(H=A_r^2+tB_r^2\) as in that theorem. An independent exact replay checked all **28** strict corner Hurwitz minors and **808** strictly positive compactified pairing coefficients for \(m\), proving \(m\) is common SPR. Yet at the rational squared frequency \(t=246723\),
\[
V(t)-H(t)=-\frac{50224407658631942894486063294295800477161207709025095173}
{21474836480000000000000000}<0.
\]
The Cauchy norm-gap test therefore fails even though actual four-corner pairings are strictly positive for the same numerator. This is not an unrestricted negative certificate; it explains why the sufficient theorem cannot be used as a decision procedure.

Frozen midpoint, radii, negative witness and leaves: `frontier-20261029-norm-gap-conservative-example-frozen-v1.json`, SHA-256 `d757dcccd39947165ad495a81e83577c5360d72aba1123284e476fd0749f8e2d`. Independent checker `frontier-20261029-norm-gap-conservative-example-independent-kernel-v1.py`, SHA-256 `809d6fa82a7762521b40e24c203a7465f9cfa98660ff5655c6d757ad22d79549`; receipt `frontier-20261029-norm-gap-conservative-example-independent-result-v1.json`, SHA-256 `f06a6d4941fcf24eeb8326465c9c08c369e69143444440f99fbc5fe737343d47`.

All finite arithmetic uses exact integers and `fractions.Fraction` on one Python Eval host. Kharitonov and affine corner minimization are written imports. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict or all-numerator negative certificate is claimed.
