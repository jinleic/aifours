# A computable all-degree interval radius around any stable center

**Status: WRITTEN; author candidate, not parent adoption.** Every real monic Hurwitz polynomial has an explicitly bounded independent coefficient neighborhood on which the center itself is a common SPR numerator. The following radius uses parity geometry and an explicit root-factor lower bound; it is a sufficient local result, not the unrestricted interval-box theorem.

Let \(a\) have degree \(n\), real roots \(-\alpha_i\) and nonreal pairs \(-\gamma_j\pm i\beta_j\), with all \(\alpha_i,\gamma_j>0\). Choose a scale \(c>0\), and put
\[
\mu_c=\prod_i\min\!\left(1,\frac{\alpha_i}{c}\right)
\prod_j\frac{(\gamma_j/c)^2}{1+(\gamma_j/c)^2+(\beta_j/c)^2}>0.
\]
For any \(0\le r<\mu_c\), independently vary the coefficient \(a_j\), \(0\le j<n\), by at most \(r c^{n-j}\), retaining monicity. Every member \(p\) is Hurwitz and \(a/p\) is strictly positive real. With \(B=\sum_{j=0}^n a_jc^{j-n}=a(c)/c^n\),
\[
\operatorname{Re}\frac{a(i\omega)}{p(i\omega)}
\ge\frac{\mu_c(\mu_c-r)}{(B+nr)^2}>0.
\]
The radius is conservative; the preceding real-rooted and sector-damped theorems often give the much stronger threshold \(r<1\).

## Proof

Scale \(s=cz\) and write \(A(z)=c^{-n}a(cz)\). For a real factor \(z+u\), \(|u+i\omega|\ge\min(1,u)\sqrt{1+\omega^2}\). For a conjugate pair \(-u\pm iv\), consider each factor \(u+i(\omega\pm v)\). The positive quadratic form
\[
 u^2+(\omega\pm v)^2-\lambda(1+\omega^2),\qquad
 \lambda=\frac{u^2}{1+u^2+v^2},
\]
is nonnegative: the associated symmetric matrix has nonnegative diagonal and determinant \(u^2-(1+u^2+v^2)\lambda+\lambda^2=\lambda^2\ge0\). Hence each factor has modulus at least \(\sqrt\lambda\sqrt{1+\omega^2}\), and their product at least \(\lambda(1+\omega^2)\). Multiplying all factors gives
\[
|A(i\sqrt t)|\ge\mu_c(1+t)^{n/2}.
\]

The geometric-sum Cauchy–Schwarz lemma in `frontier-20261029-real-rooted-center-uniform-box-theorem-v1.md` gives, for scaled coefficient perturbations of magnitude at most \(r\),
\[
P_{P,A}(t)\ge |A|^2-r|A|(1+t)^{n/2}
\ge\mu_c(\mu_c-r)(1+t)^n>0.
\]
This remains true along the straight coefficient path from \(A\) to \(P\), precluding imaginary-axis roots. The center is Hurwitz, so homotopy proves all members Hurwitz. The coefficient-sum bound \(|P(i\sqrt t)|\le(B+nr)(1+t)^{n/2}\) gives the displayed ratio bound. ∎

The roots need not be rational; the formula is an explicit function of the given stable center's roots. The argument imports elementary root factorization, positive quadratic forms, Cauchy–Schwarz and homotopy. It is written mathematics, not formal or cross-vendor verification, novelty clearance, a universal arbitrary-box verdict, or an unrestricted negative certificate.
