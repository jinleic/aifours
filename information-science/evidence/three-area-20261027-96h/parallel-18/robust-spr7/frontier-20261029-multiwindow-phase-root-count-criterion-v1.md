# A multiwindow phase certificate for unavoidable nonreal roots

**Status: WRITTEN; author candidate, not parent adoption.** The following is a genuinely multiwindow extension of `frontier-20261029-cross-member-phase-root-count-criterion-v1.md`. It applies to any nonempty family \(K\) of real monic Hurwitz polynomials of fixed degree \(n\), not necessarily a convex or interval family.

Choose ordered nonoverlapping positive-frequency windows \([u_i,v_i]\), \(i=1,\ldots,N\), and actual members \(p_i,q_i\in K\). Let \(\theta_f\) be each continuous phase starting at zero, and put
\[
L=\sum_{i=1}^N\log(v_i/u_i),\qquad
M=\frac n2L+k\max(\pi-L,0),\qquad
0\le k\le\lfloor n/2\rfloor.
\]
If
\[
\boxed{\quad\sum_{i=1}^N
\bigl[\theta_{p_i}(v_i)-\theta_{q_i}(u_i)\bigr]>N\pi+M,\quad}
\]
then every common exact-degree-\(n\) real SPR numerator has at least \(k+1\) nonreal conjugate root pairs, counted with multiplicity. The statement concerns the literal numerator polynomial and remains valid under cancellation.

**Proof.** For a common numerator \(b\), the continuous SPR phase differences lie strictly in \((-\pi/2,\pi/2)\). Summing their endpoint bounds gives
\[
\sum_i[\theta_b(v_i)-\theta_b(u_i)]
>\sum_i[\theta_{p_i}(v_i)-\theta_{q_i}(u_i)]-N\pi.
\]
If \(b\) has \(j\le k\) nonreal conjugate pairs, the phase of each pair is strictly increasing from zero to \(\pi\), so its total rise on the **disjoint** windows is less than \(\pi\), not \(N\pi\). Each of the remaining \(n-2j\) real-negative-root factors has logarithmic-frequency phase derivative at most \(1/2\), so its summed rise is at most \(L/2\). Therefore
\[
\sum_i[\theta_b(v_i)-\theta_b(u_i)]
<j\pi+\frac{n-2j}{2}L
\le\frac n2L+k\max(\pi-L,0)=M,
\]
a contradiction. If there are no nonreal pairs, the corresponding real-root bound is non-strict, but the strict lower bound is still enough. ∎

For a convex stable family, the separate `frontier-20261029-stable-family-phase-packing-obstruction-v1.md` constrains how large such multimeasurements can be; neither criterion establishes that an arbitrary interval box satisfies the hypothesis. The result is sufficient, not necessary, and it does not preclude an unrestricted common numerator. No finite example beyond the one-window instances is claimed here. The argument is written mathematics, not formal verification, cross-vendor review, novelty clearance, or an arbitrary-box verdict.
