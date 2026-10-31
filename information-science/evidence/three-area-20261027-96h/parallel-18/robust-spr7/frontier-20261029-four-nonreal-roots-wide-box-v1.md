# A wider full-dimensional nonreal-root obstruction box

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** The explicit example in `frontier-20261029-common-numerator-nonreal-root-obstruction-v1.md` can be enlarged substantially. Let
\[
a(s)=(s+1)\left((s+\tfrac1{100})^2+1\right)^3,
\]
and let each of its seven nonleading coefficients independently vary by \(1/500000\), retaining a monic leading coefficient. This full-width box is strictly Hurwitz and has \(a\) as a common SPR numerator. Since it contains \(a\), the written phase theorem in the cited packet still proves that **every** common numerator has at least two nonreal conjugate root pairs, even if cancellation is allowed in individual transfer fractions.

An independent exact replay checked all **28** strict corner Hurwitz determinants and **296** strict compactified Bernstein coefficients for \(a\)'s pairing with the four actual corners. Its uniform compactified margin is
\[
\delta=\frac{452611106080221}{14336000000000000000000000000}>0.
\]
Kharitonov's theorem and affine corner minimization extend this to every member and every real frequency. With \(S=8243639180601/500000000000\), one obtains the explicit positive ratio bound \(\operatorname{Re}(a(i\omega)/p(i\omega))\ge\delta/S^2\).

Frozen endpoints, margin and frequency leaves: `frontier-20261029-four-nonreal-roots-wide-box-frozen-v1.json`, SHA-256 `8d7499212660f2cd5135b38ee1125defea80f2551fc655dcb7bf666da97388ff`. Independent checker `frontier-20261029-four-nonreal-roots-wide-box-independent-kernel-v1.py`, SHA-256 `4171ecfeba7e00804b31d3c2cdf4a55642295c29f035bfbdd6a1b8f6b66182f2`; receipt `frontier-20261029-four-nonreal-roots-wide-box-independent-result-v1.json`, SHA-256 `110beafb3e77a156cb565b6fb945a0439c49be7d589f64771c2916e5195417af`. The phase theorem is SHA-256 `3e6728c4b9fca39892d8b4cc10516b98fac5539c1115d2cfd67777519e470ee7`.

Finite arithmetic is exact integer/`fractions.Fraction` work on one Python Eval host; the phase theorem is a named written import. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or unrestricted negative certificate is claimed.
