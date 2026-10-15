No fatal or major mathematical error found. The substantive proofs survive scrutiny. Two minor formulation corrections are warranted.

1. **Minor — the Fourier integral does not define the transform on all \(L^2\).**  
   **Location:** [proof.md, lines 7–13](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:7).  
   **Evidence:** The stated domain includes finite-energy signals outside \(L^1\). For example, \(s(t)=(1+t^2)^{-1/2}\) belongs to \(L^2\), but the displayed integral diverges at \(\omega=0\). Subsequent arguments correctly use Plancherel, so this does not invalidate them.  
   **Correction:** State that the integral defines the transform on \(L^1\cap L^2\), extended unitarily to \(L^2\).

2. **Minor — the product rule’s conditional-mean statement needs a moment qualification.**  
   **Location:** [proof.md, line 30](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:30).  
   **Evidence:** Theorem 1 covers every nonzero \(L^2\) signal. For the preceding example, the time marginal is proportional to \((1+t^2)^{-1}\), whose ordinary mean is undefined. Thus the product rule need not have both ordinary conditional means. The regularity assumptions elsewhere correctly supply the required moments.  
   **Correction:** Write “whenever the respective marginal has finite first moment, the product rule’s conditional mean equals its unconditional mean.”

The requested substantive checks give the following results:

- **Normalization, baseline existence, covariance and support — correct.**  
  [Conventions and Theorem 1](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:7) match the book’s equations (1)–(5): \(S_{\mathrm{book}}=\sqrt{2\pi}S\), hence \(p=P/(2\pi E)\). The product requires \(E^2\) in its normalized denominator. Both shift formulas and reciprocal scaling are correct; the scaling map has determinant one. Strong support follows from nonnegativity and the marginals in precisely the stated measure/a.e. sense.

- **Finite-energy analytic negative-IF witness — correct.**  
  [Theorem 2](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:36) has the claimed regularity and spectral bands. Direct calculation gives
  \[
  |e^{it}-\tfrac34e^{2it}|^2=\frac{25-24\cos t}{16},
  \qquad
  \operatorname{Im}(\bar q q')
  =h^2\frac{34-36\cos t}{16}.
  \]
  Thus \(f_q(0)=-2\), with negative IF on a positive-energy interval. Every proposed coupling has \(W\ge3/4\), making its conditional mean at least \(3/4\). This is a measure-level contradiction and therefore excludes densities. The Schwartz variant also works.

- **Explicit \(L=129\) analytic GD certificate — every bound checks.**  
  [Theorem 3](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:64) preserves analyticity because
  \(S_L(\omega)=\chi(\omega)q(\omega-L)\). Its asserted Sobolev and weighted-\(L^2\) properties hold. On the selected interval,
  \[
  \frac{36(127/128)-34}{16}=\frac{55}{512},
  \qquad
  h^2\ge1-\frac4{24576}=\frac{6143}{6144}>\frac12,
  \]
  giving \(55/4096\). Differentiation gives the valid, conservative bounds
  \[
  |q'|\le188/z^2+224/|z|^3\le300/z^2,
  \qquad |d'|\le(300+\tfrac32\,112)/z^2=468/z^2.
  \]
  The error occupies one tail, so the denominator \(3D^3\) is correct. Consequently
  \[
  \|d\|_2\|d'\|_2
  \le\frac{112\cdot468}{3\cdot128^3}
  =\frac{273}{32768}
  <\frac{440}{32768}
  =\frac{55}{4096}.
  \]
  Fourier inversion reflects the original bands into negative time; translation only modulates. The positive-time leakage estimate and Jensen contradiction are valid.

- **Strassen lifting and the density distinction — correct.**  
  [Theorem 4](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:110) uses the finite-first-moment theorem actually stated in the [provided primary text](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/sources/leskela-vihola-2014.txt:47). The kernel \(K(f(t),d\omega)\) is measurable, preserves both marginals, and pulls the exceptional \(\alpha\)-null set back to a \(\mu\)-null set. Integrability follows from \(\nu\); no moment of \(T\) is needed. The uniform-diagonal example correctly demonstrates that convex order does not ensure a joint density.

- **Fourier cross-moment/covariance identity — correct, including the sign.**  
  [Theorem 5](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:135) correctly obtains
  \[
  \langle ts,s'\rangle
  =\langle iS',i\omega S\rangle
  =\int\omega\overline{S'}S.
  \]
  Its imaginary part is \(-\operatorname{Im}\int\omega\bar S S'\), agreeing with GD. The hypotheses control every product by Cauchy–Schwarz. Subtracting the means gives the centered identity.

- **Both two-regression counterexamples — correct.**  
  [Theorem 6](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:155) satisfies both convex orders and the matching cross moment. Adding the three displayed constraints gives exactly
  \(p_{23}+2p_{31}=-1/24\). For the continuous version, each replacement error is at most \(\varepsilon/3\), giving
  \[
  -1/24+2(1/32)/3=-1/48.
  \]
  Symmetric smooth bump densities preserve the argument; bounded smooth extensions of the regressions exist across the gaps. These are valid abstract counterexamples. They provide no Fourier-realizable counterexample, as the text explicitly acknowledges.

- **Wigner proof — correct.**  
  [Theorem 7](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:199) has the correct \(1/(2\pi E)\) normalization and both marginal constants. The frequency moment is \(-iA_t'(0)/E\). The sign-sensitive duality is
  \(w_s(t,\omega)=w_S(\omega,-t)\), yielding the stated negative spectral-phase derivative. Schwartz regularity justifies the operations. Signed moments are correctly distinguished from probability conditional expectations.

- **Quadratic-rule impossibility — correct.**  
  [Theorem 8](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:217) eliminates cross terms separately on the two time regions using positive-form Cauchy–Schwarz. Polarization supplies additivity for arbitrary joint sets. Frequency marginals then contradict the strictly positive interference term near zero. The proof covers the explicitly defined Hermitian quadratic class on all complex \(L^2\); it does not establish an analytic-only quadratic theorem.

The source interpretation and historical boundary are sound. The [Chinese page 453](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/sources/pdfpage-0474.png) names IF/GD as useful Wigner properties without defining “clear physical meaning” by them, and expressly rejects the product baseline. The README preserves that distinction. The negative-IF obstruction is explicitly present in the [provided 1994 primary text](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/sources/loughlin-pitton-atlas-1994.txt:266). **Novelty clearance remains incomplete**, especially for the explicit GD and regression certificates; that is not a mathematical error. The existing novelty disclaimers should remain.

These are classical written proofs. No Lean certification is supplied; its absence is not an error.

**Verdict:** Universal density existence for M, optionally COV/SUP, is settled positively. Universal M+IF and M+GD are settled negatively on the stated regular analytic classes; adding both regressions cannot help. Universal positive Hermitian quadratic rules on all complex \(L^2\) are excluded. Signed Wigner identities are established on Schwartz signals. One-regression existence is completely characterized for joint measures under the stated moment hypotheses. General per-signal density existence and the Fourier-realizable two-regression classification remain unresolved here. **The unrestricted Chinese book question is not solved.**