# A sharper conjugate-aware cross-member root-localization certificate

**Status: WRITTEN; author candidate, not parent adoption.** The following improves the sufficient phase-localization test in `frontier-20261029-cross-member-phase-root-localization-criterion-v1.md` by using conjugate symmetry rather than treating all nonlocalized roots identically.

Let \(K\) be a nonempty family of real monic Hurwitz polynomials of fixed degree \(n\), and take actual members \(p,q\in K\), \(0<\omega_1<\omega_2\), \(0<R<\omega_1\), and \(0\le k\le\lfloor n/2\rfloor\). Put \(\Delta=\omega_2-\omega_1\) and
\[
M_{\rm sym}=\max_{0\le j\le k}\left[
 j\pi+\left\lfloor\frac{n-2j}{2}\right\rfloor\frac\Delta R
 +\left\lceil\frac{n-2j}{2}\right\rceil\frac\Delta{2\omega_1}\right].
\]
If the continuously unwrapped phases satisfy
\[
\boxed{\quad\theta_p(\omega_2)-\theta_q(\omega_1)>\pi+M_{\rm sym},\quad}
\]
then every common exact-degree-\(n\) real SPR numerator has at least \(k+1\) upper-half-plane roots, with multiplicity, at distance less than \(R\) from the segment \(i[\omega_1,\omega_2]\), plus their conjugates. This concerns literal numerator roots, even when cancellations occur.

**Proof.** A common numerator \(b\) is Hurwitz, and the SPR phase bounds yield
\(\Delta\theta_b>\theta_p(\omega_2)-\theta_q(\omega_1)-\pi\). Suppose at most \(j\le k\) upper roots lie inside the segment neighborhood. Since \(R<\omega_1\), neither a real nor lower-half-plane root can be in that neighborhood. The \(j\) localized roots and their conjugates give at most \(j\pi\) phase rise. For each remaining upper-half-plane root, distance at least \(R\) gives phase derivative at most \(1/R\). For a lower-half-plane root \(r=-a-i\beta\) with \(a,\beta>0\),
\[
\frac{a}{a^2+(\omega+\beta)^2}\le\frac1{2(\omega+\beta)}\le\frac1{2\omega_1}.
\]
The same \(1/(2\omega_1)\) bound holds for real negative roots. Among the remaining \(n-2j\) roots at most \(\lfloor(n-2j)/2\rfloor\) are upper-half-plane; all others have the latter bound. Integrating and maximizing over \(j\le k\) yields \(\Delta\theta_b\le M_{\rm sym}\), a contradiction. ∎

This is a sufficient test, not an equivalence and not an unrestricted synthesis verdict. The earlier septic localization is a special case with weaker numerical bounds. The proof is written mathematics; no formal verification, cross-vendor review, novelty clearance or arbitrary-box conclusion is claimed.
