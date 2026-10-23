DISPOSITION **INCONCLUSIVE**

All seven supplied SHA-256 hashes match. No false mathematical bound was demonstrated. One missing mathematical interface prevents completing the requested predicate-to-proof audit.

**FATAL: none found.**

1. **MAJOR — SWC’s certified inequalities lack their mathematical definitions in this snapshot.**  
   **SOURCE01:LF38–46; SOURCE03:LF249; SOURCE00:LF226–236.**

   SOURCE01 imports \(X_m,U_m,\Psi,I_g\) and their tail definitions from spec v1, which is absent. SOURCE03 certifies
   \[
   \Psi_N+\mathrm{tail}\Psi<0,\qquad I_{g,N}-\mathrm{tail}I_g>0.
   \]
   Without the missing definitions, those inequalities cannot independently be connected to the RADIAL condition required by Lemma D. Accepting the leaf inequalities does not supply that connection.

   **Concrete repair:** include the relevant v1 definitions, or inline an explicit interface. For example, with the analytic branch \(g=\log W\), \(g(0)=0\), define
   \[
   I_g=\frac{\Im g}{\omega},\qquad
   \Psi=\frac{\Re g+\delta I_g}{\delta^2+\omega^2},
   \]
   and establish
   \[
   I_g\ge I_{g,N}-\mathrm{tail}I_g,\qquad
   \Psi\le\Psi_N+\mathrm{tail}\Psi.
   \]
   Then \(\alpha=\omega I_g>0\) is an argument of \(W\), and
   \[
   \log|W|+\frac{\delta}{\omega}\alpha
   =(\delta^2+\omega^2)\Psi<0,
   \]
   exactly yielding RADIAL. If the implementation uses another normalization, state its positive conversion factor.

   This is a missing **mathematical interface**, separate from the closed manifest gap. It does not show that SWC or its replay is wrong.

2. **MINOR — “real span” of the complex exponentials is technically incorrect.**  
   **SOURCE00:LF124–130.**

   The explicit displayed definition of \(K\) is correct and includes the sine component. Literally taking real coefficients on the two complex exponentials, then requiring real-valued functions, loses that component.

   **Concrete repair:** replace the explanatory span with
   \[
   \operatorname{span}_{\mathbb R}
   \{e^{-t},\,e^{-(1+\delta)t}\cos\omega t,\,
   e^{-(1+\delta)t}\sin\omega t\}.
   \]
   Keep the displayed definition unchanged.

**Audited versus imported**

- **Audited — class and reductions interfaces.** The stated L1–L6 contracts cover unrestricted real ME representations, lower orders and repeated real poles. After cancellation of invisible modes, integrability forces the effective poles to decay; a nonnegative oscillatory density requires a real pole whose damping is no greater than the pair’s. Equal damping gives D1, strict dominance gives D2. Thus the case split imposes no phase-type sign restriction. Finite second moments add no restriction to these finite, integrable exponential-polynomial densities.

- **Audited — Lemma D.** Both arguments for \(a\ge0\) are valid. For \(y>0\),
  \[
  \kappa y^2-2y+2
  =\kappa(y-1/\kappa)^2+2-1/\kappa>0.
  \]
  Taking \(q_\theta(t)=t^2-2\theta t+\kappa\theta^2\), the integration identity is correct. Nonnegativity for every finite \(\theta>0\) gives \(m_0m_2/m_1^2\ge1/\kappa=1+T\). The finite coefficients and times may depend on \(\theta\); no uniform choice is needed.

- **Audited — RADIAL/SMALL/TRIANGLE and zeros.** RADIAL gives one orbit point at \(t=\alpha/\omega\), with coefficient \(|W|e^{\delta\alpha/\omega}\le1\). SMALL reduces to RADIAL by choosing an argument in \([0,2\pi)\). TRIANGLE is already a finite representation. For \(W=0\), take all coefficients zero. The unused weight is justified by \(a\ge0\); no closure of a hull is needed.

- **Audited — Lemma M and derivative factors.** With \(a_k=1-\Re(c\zeta^{k+1})\),
  \[
  \partial_r a_k=-\Re\!\left[
  c\zeta^{k+1}\left(\phi-\frac{i}{1-ir}-(k+1)\omega\zeta\right)\right],
  \]
  and
  \[
  S'=\frac{2}{a_1^3}
  \big[(a_0'a_2+a_0a_2')a_1-2a_0a_2a_1'\big].
  \]
  These have the correct signs and factors. Decreasing \(\theta_1\) keeps the fixed-\((\omega,\phi)\) path feasible. Its density stays nonzero, so \(a_1>0\). The \(r_*\) continuation argument is sound. Strictness for \(r_0>0\) comes from a positive-length subinterval; only a non-strict bound is needed at \(r=0\).

- **Audited — coverage and SKIPs.** The stated domains cover every finite positive D2 parameter. The \(d,\beta,\nu,\chi,\rho_t\) transformations cover both unbounded tails. The P phase ceiling exceeds \(2\pi\); finite test centres correspond exactly to \(0<s<1\). Padding faces require no pole interpretation. G SKIPs lie inside P. LD2 SKIPs exclude its physical domain; applicable larger-\(s\) points belong to LD1. Boundary overlaps introduce no hole. The LD small-\(\beta\) argument and replacement of \(1-d\) by \(1\) are conservative on physical points.

- **Audited — assembly, strictness and attainment interfaces.** The exact rational upper example separates \(v_{\cos}\) from \(T\) and \(\Delta_3\); no rounded decimal minimum is used. Fixed-cone attainment makes strict bounds on every extreme ray sufficient for strictness throughout each D2 cone. No uniform gap over all D2 cones is asserted or needed. D1 attainment follows from the imported uniform tails and compact phase/frequency minimization. These conclusions remain conditional on completing finding 1.

- **Imported as instructed:** all certificate-leaf inequalities and reported tilings, parent reduction results L1–L6, arithmetic correctness and completed pin closure. I did not replay computations or inspect material outside the snapshot. The SWC normalized-predicate definitions were neither supplied nor independently verified.