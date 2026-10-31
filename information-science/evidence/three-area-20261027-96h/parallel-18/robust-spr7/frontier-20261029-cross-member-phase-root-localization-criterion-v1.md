# A cross-member certificate localizing common-numerator roots

**Status: WRITTEN; author candidate, not parent adoption.** This extends `frontier-20261029-cross-member-phase-root-count-criterion-v1.md` from a count of nonreal pairs to an explicit geometric region.

Let \(K\) be a nonempty family of real monic Hurwitz polynomials of degree \(n\), let \(p,q\in K\) be actual members, and take \(0<\omega_1<\omega_2\), \(0<R<\omega_1\), \(0\le k\le\lfloor n/2\rfloor\). Put \(\Delta=\omega_2-\omega_1\), and let \(\theta_f\) be the continuously unwrapped phase of \(f(i\omega)\), starting at zero. Define
\[
M_{\rm loc}=\frac{n\Delta}{R}
+k\max\!\left(\pi-\frac{2\Delta}{R},0\right).
\]
If
\[
\boxed{\quad\theta_p(\omega_2)-\theta_q(\omega_1)>\pi+M_{\rm loc},\quad}
\]
then **every** common exact-degree-\(n\) real SPR numerator has at least \(k+1\) upper-half-plane roots, counted with multiplicity, within distance \(R\) of the segment \(i[\omega_1,\omega_2]\). Their conjugates give at least \(k+1\) lower-half-plane roots near the reflected segment. These are roots of the literal numerator, regardless of possible transfer-function cancellation.

**Proof.** Common SPR makes the numerator Hurwitz and yields
\(\Delta\theta_b>\theta_p(\omega_2)-\theta_q(\omega_1)-\pi\), as in the root-count criterion. If only \(j\le k\) upper roots lie within the segment neighborhood, \(R<\omega_1\) guarantees that neither real nor lower-half-plane roots lie there. Group those \(j\) upper roots with their conjugates; each pair's phase increment is less than \(\pi\). For each remaining root \(r=-a+i\beta\),
\[
\frac{d}{d\omega}\arg(i\omega-r)=\frac{a}{a^2+(\omega-\beta)^2}\le\frac1R,
\]
so the remaining \(n-2j\) roots contribute at most \((n-2j)\Delta/R\). Maximizing over \(0\le j\le k\) yields \(\Delta\theta_b<M_{\rm loc}\), contradicting the hypothesis. ∎

The explicit septic localization with \(p=q\), \(\omega_1=9/10\), \(\omega_2=11/10\), \(R=197/500\), \(k=1\), is independently supported in `frontier-20261029-resonant-root-localization-v1.md`. The criterion is sufficient, not necessary, and does not certify or refute unrestricted synthesis. The general proof is written mathematics; no formal verification, cross-vendor review, novelty clearance or arbitrary-box verdict is claimed.
