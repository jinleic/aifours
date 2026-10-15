**Theorem 10 is proved as stated, conditional only on correct execution of the audited checker against certificate entry 0.** I found no fatal or major defect. Two minor defects concern exposition and numerical reporting.

1. **Minor — a real root alone does not establish the strict lower bound \(3<\sup|f|\).**  
   At [proof.md:352](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:352), rejecting cap \(3\) because a real root exists establishes \(\sup|f|\ge3\); tangency could give equality. The [checker’s rejection path](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/work/verify_fourier_obstruction.py:187) does not establish a sign crossing.

   Fix: give the exact witness
   \[
   f(9/5)=3+\frac{608217}{91147261}>3.
   \]
   This concerns an auxiliary diagnostic. The theorem’s upper bound \(3.01\) is sound.

2. **Minor — the quoted numerical enclosure is rounded inward.**  
   [proof.md:392](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:392) and [README.md:113](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/README.md:113) quote radius \(4\cdot10^{-74}\), whereas the [saved Arb output](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/evidence/fourier-obstruction-verification.json:1537) prints \(4.01\cdot10^{-74}\).

   Fix: reproduce the saved enclosure exactly, or round outward. Negativity is unaffected.

The load-bearing checks are sound:

- **Fourier invariance, normalization and regressions.** Under the stated convention,
  \[
  \mathcal F[t^nG]=(-i)^n\mathrm{He}_nG,\qquad
  4\mathrm{He}_4+12\mathrm{He}_2+3=p.
  \]
  Thus \(S=s\), with the correct eigenvalue signs. Equivalently, \(h_4=Gp/(2\sqrt6)\), verifying the Hermite coefficient. Expanding
  \[
  p^2=16t^8-96t^6+168t^4-72t^2+9
  \]
  gives Gaussian expectation \(24\), hence \(E=55/49\) and the stated \(\rho\). A common nonzero scalar does not affect normalized marginals or phase derivatives. The positive real factor in \(1+ip/14\) excludes zeros. Direct differentiation gives
  \[
  f=\frac{14p'}{196+p^2},\qquad g=-f.
  \]
  Finally,
  \[
  \int tf\,d\mu=\frac{14}{220}(16\cdot\tfrac34-24\cdot\tfrac12)=0,
  \]
  and the GD expression is its negative, also zero.

- **All-real-strike convex order.** The symmetry reduction and negative-strike identity are correct, including the factors of two. The cap polynomials have positive leading coefficients; absence of real roots therefore establishes their strict positivity. On every grid interval, monotonicity gives the claimed sandwich in the correct direction. Strikes beyond \(3.01\) have \(C_f=0<C_T\), since \(\rho\) is positive everywhere. Consequently the proof covers every real strike and gives a strictly positive potential gap at every finite threshold.

- **Root and integration code.** In the [checker](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/work/verify_fourier_obstruction.py:87), `sturm_count` uses the correct signed remainder sequence and endpoint variations. `positive_simple_roots` requires simple, separated positive root balls and matches their count against Sturm. `sign_intervals` samples exact rationals between certified bounds and uses the leading coefficient beyond the last root. The moment recursions have the correct boundary signs, including negative endpoints. `call_signal` computes
  \[
  \frac2{220\sqrt\pi}\int_0^\infty
  \bigl[(\mathrm{CUR}-k\mathrm{RHO})_+
       +(-\mathrm{CUR}-k\mathrm{RHO})_+\bigr]e^{-t^2}\,dt,
  \]
  and `call_time` computes the stated absolute call. The special \(k=0\) branch correctly avoids a root at zero. Splitting at \(t=\sqrt{3/2}\) verifies
  \[
  \mathbb E|f(T)|=\frac{7(16e^{-3/2}+4)}{55\sqrt\pi}.
  \]

- **Full-plane dual certificate.** [Lemma 10.1](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/proof.md:377) is valid: each interior expression is affine, and the exact corner check covers all \(4096\) corners. The three exterior cases follow from the stated maxima. Endpoint choices are harmless with consistent cell assignments; moreover, both marginals give endpoints zero mass. Bounded \(h,k\), linear growth of \(a,b\), and finite first moments justify integrability and conditioning. The [implementation](/Users/jinleic/jinleic-workspace/ai4s/positive-tfd-marginals/work/verify_fourier_obstruction.py:237) includes precisely
  \[
  \sum_i[(a_i+b_i)\mu(C_i)+(h_i-k_i)\!\int_{C_i}J]
  +(A^-+B^-)\mu(|t|>4)+(H+K)\!\int_{|t|>4}|t|\,d\mu.
  \]
  No tail term or regression sign is missing.

- **Chirps and mutations.** The chirp laws have variances \(1/2\) and \((1+\beta^2)/2\), with regressions \(\beta t\) and \(\beta\omega/(1+\beta^2)\). The Gaussian cell and tail formulas implement these correctly. Controls and mutations impose additional checks; they do not replace or weaken either decisive certificate. The floating-point sanity calculation is not load-bearing.

- **Theorem 9 and prior art.** Strict positivity makes the contact set empty, so both separate density-existence applications are justified. The locally supplied BNT and Nutz–Wiesel texts support the stated attribution, including the distinction between dominating an absolutely continuous measure and being absolutely continuous. The cited range-obstruction results do not establish this example’s two-sided obstruction. The package appropriately leaves novelty unestablished; this static audit does not independently validate an exhaustive literature search.

I performed static inspection only and did not run the checker.