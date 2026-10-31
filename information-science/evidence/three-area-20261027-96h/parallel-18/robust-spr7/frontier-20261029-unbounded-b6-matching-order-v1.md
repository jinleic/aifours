# The forced quadratic coefficient growth is attained

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel exact coefficient comparison; not parent adoption.** For the explicit common numerator \(b_R\) and eligible boxes \(K_R\) in `frontier-20261029-unbounded-common-numerator-b6-obstruction-v1.md` (SHA-256 `71896c927bafabc2098ab283bc6108a7b259bda028dc58c948cffb637106f8c7`), every real \(R\ge100\) satisfies
\[
\frac{R^2}{20}<(b_R)_6<\frac{R^2}{5},\qquad
\lim_{R\to\infty}\frac{(b_R)_6}{R^2}=\frac{1317}{8425}.
\]
The lower bound also applies to **every** common monic numerator, by the predecessor's five positive actual-atom certificate. Thus the unavoidable growth is quadratic and the explicit determinant construction attains that order within a factor four, while the denominator coefficient \(a_6\) stays below \(1001/1000\).

For the predecessor's positive Cramer determinant \(D\) and degree-six numerator determinant \(B_6\), \((b_R)_6=B_6/D\). The independently replayed sign data give lowest powers \(R^5\) in \(D\) and \(R^4\) in \(B_6\). After substituting \(R=100+u\) and factoring out the positive \(R^4\), the coefficient arrays of
\[
R^2D-5B_6,\qquad 20B_6-R^2D
\]
each have 23 strictly positive rational coefficients. Hence both inequalities hold for all \(u\ge0\). The exact leading terms are
\[
D(R)\sim\frac{3033}{312500000}R^{24},\qquad
B_6(R)\sim\frac{11853}{7812500000}R^{26},
\]
whose ratio is \(1317/8425\).

The exact comparison coefficients are frozen in `frontier-20261029-unbounded-b6-matching-order-frozen-v1.json`, SHA-256 `6a6df044750d9e3227aa07e16ca226b1636801d7a8c8070f6d916b5a15076c6a`. The independent shifted-array checker `frontier-20261029-unbounded-b6-matching-order-independent-kernel-v1.py`, SHA-256 `821dff027dcfbcbd0f6562921b5925f5c5ef0f26e97edce9e921e009b4fd02cf`, verifies all 46 signs and the exact limit; receipt `frontier-20261029-unbounded-b6-matching-order-independent-result-v1.json`, SHA-256 `46200600c9d37a400549c4811ee7fcb9357f5993ae5141eb15eaa98510c2771b`. It imports the preceding independently reconstructed symbolic sign tables, not a solver. Arithmetic is exact `fractions.Fraction` on one Python Eval host; the asymptotic inference is written mathematics. No formal proof, cross-vendor review, novelty clearance or arbitrary-box verdict is claimed.
