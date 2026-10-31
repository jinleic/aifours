# Every common numerator needs an arbitrarily faster root

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel leading-degree replay; not parent adoption.** On the explicitly solvable full-width stable septic family \(K_R\), \(R\ge5000\), from `frontier-20261029-unbounded-b6-strong-lower-v1.md` (SHA-256 `b0cba7cf3305cfb375b1f3eee9739ae8f335a23d2fc9b4f47fb7b0a2ba6206f3`), **every** common numerator has at least one root \(\xi\) with
\[
\boxed{\operatorname{Re}\xi<-R^2/80.}
\]
In contrast, **every** root \(\zeta\) of **every** denominator in the same box satisfies
\[
\operatorname{Re}\zeta>-1001/1000.
\]
Thus no universal fixed strip in the left half-plane, and no fixed multiple of the denominators' damping range, can contain all roots of a valid common numerator. The box is not a counterexample: an explicit numerator is already supplied.

## Written deduction

Normalize the common numerator to monic. It is Hurwitz by the positive-real segment homotopy. If its seven roots have real parts \(-\alpha_j\), then every \(\alpha_j>0\) and Vieta gives
\[
\sum_{j=1}^7\alpha_j=b_6>\frac7{80}R^2.
\]
Some \(\alpha_j\) is therefore greater than \(R^2/80\); it need not be real, and no such claim is made for an arbitrary numerator. For each monic Hurwitz denominator, Vieta likewise gives \(\sum_j-\operatorname{Re}\zeta_j=a_6<1001/1000\), so every one of its roots lies strictly to the right of \(-1001/1000\).

## The explicit numerator has exactly one escaping root

For the determinant-constructed common numerator \(b_R\) from the source, the independently replayed Laurent degrees give coefficient growth exponents
\[
(b_{R,0},\ldots,b_{R,7})=O(R^2,R^3,R^4,R^3,R^4,R^2,R^2,1).
\]
The exact degree-six coefficient asymptote is \(b_{R,6}/R^2\to1317/8425\). Hence the monic scaled polynomials converge coefficientwise:
\[
R^{-14}b_R(R^2z)\longrightarrow z^7+\frac{1317}{8425}z^6
=z^6\left(z+\frac{1317}{8425}\right).
\]
By continuity of polynomial roots, one scaled root tends to the simple negative root \(-1317/8425\), while the other six tend to zero. The single root near that simple real limit must itself be real for sufficiently large \(R\), since otherwise its conjugate would be a second nearby root. It is negative because \(b_R\) is Hurwitz. Thus this explicit construction has precisely one root of order \(R^2\), asymptotic to \(-(1317/8425)R^2\); the others are \(o(R^2)\). This sharpness statement is for the **displayed construction**, not a uniqueness or root-count theorem for every common numerator.

The exact exponent and limiting-coefficient replay `frontier-20261029-unbounded-fast-root-independent-kernel-v1.py` has SHA-256 `91deb4fb1d4c0af38a0b4855347aecdc9de339bfbeb14c16d6d4c4a7ad647ccc`; receipt `frontier-20261029-unbounded-fast-root-independent-result-v1.json` has SHA-256 `3507e122aebd0cb945ab2c7cc3e4f284456b67b725997104740013f60cf5cf1a`. It imports the preceding independently replayed exact symbolic coefficient tables. Vieta, root continuity and the root-count inference are written mathematics. No formal proof, cross-vendor review, novelty clearance or unrestricted original-box verdict is asserted.
