# A two-member phase certificate for unavoidable nonreal numerator roots

**Status: WRITTEN; author candidate, not parent adoption.** The following is a general analytic obstruction for any compact family of real monic Hurwitz polynomials of fixed degree. It does not assume interval structure and is not equivalent to a finite atom count.

Let \(K\) be a nonempty family of real monic Hurwitz polynomials of degree \(n\). Fix actual members \(p,q\in K\), positive frequencies \(0<\omega_1<\omega_2\), and an integer \(0\le k\le\lfloor n/2\rfloor\). Let each \(\theta_f(\omega)=\arg f(i\omega)\) be the continuous unwrapped phase starting at zero at \(\omega=0\), and write
\[
r=\omega_2/\omega_1,\qquad
M(n,k,r)=\frac n2\log r+k\max(\pi-\log r,0).
\]
If
\[
\boxed{\quad\theta_p(\omega_2)-\theta_q(\omega_1)
>\pi+M(n,k,r),\quad}
\]
then every common exact-degree-\(n\) real SPR numerator for \(K\) has at least \(k+1\) nonreal conjugate root pairs, counted with multiplicity. This remains true with literal numerator/denominator factor cancellation; it says nothing about the roots of a reduced transfer function. Choosing \(p=q\) recovers the resonance obstruction in `frontier-20261029-common-numerator-nonreal-root-obstruction-v1.md`. For an independent interval box, the two members may be actual parity corners or any other actual members; no artificial endpoint hull is used.

**Proof.** Suppose \(b\) is common SPR. Its leading coefficient is positive from the high-frequency ratio. The straight segment from any monic \(p\in K\) to its monic normalization has positive real ratio to \(p\) on the imaginary axis, hence no imaginary-axis crossing, so \(b\) is Hurwitz. Its continuous phase difference with every \(p\in K\) starts at zero and stays in \((-\pi/2,\pi/2)\). Therefore
\[
\theta_b(\omega_2)-\theta_b(\omega_1)
>\theta_p(\omega_2)-\theta_q(\omega_1)-\pi.
\]
If \(b\) has \(j\le k\) conjugate pairs, each pair contributes phase increase less than \(\pi\). Each of the remaining \(n-2j\) negative real roots contributes at most \(\tfrac12\log r\), because its logarithmic-frequency phase derivative is \(\omega a/(a^2+\omega^2)\le1/2\). Hence
\[
\Delta\theta_b<j\pi+\frac{n-2j}{2}\log r
\le\frac n2\log r+k\max(\pi-\log r,0)=M(n,k,r),
\]
contradicting the displayed hypothesis. ∎

The inequality is a **sufficient certificate** for a root-count lower bound, not a necessary condition or a full synthesis criterion. Phase bounds can be proved using exact rational signs and elementary arctangent bounds rather than floating point; the cited septic example gives such an independently replayed instance and also supplies an unrestricted common numerator. The proof uses classical factorization, phase continuity and elementary inequalities only. No machine check of this general theorem, formal proof, cross-vendor review, novelty clearance, or universal arbitrary-box conclusion is claimed.
