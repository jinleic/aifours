**Mathematical claims: correct. Novelty: novelty not established.** I found no counterexample to C1–C5 under their stated hypotheses. The remaining fixes concern attribution and evidence presentation.

I reviewed the requested files without running `code/verify.py`. `STATUS.md` was absent when checked; that is not a correctness finding.

1. **The novelty comparison needs an additional mathematical baseline.**  
   [RESULTS.md:79](/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/RESULTS.md:79), particularly the higher-dimensional argument at lines 150–158.

   Beyond standard [Ruskai–Szarek–Werner qubit-channel geometry](https://arxiv.org/abs/quant-ph/0101003), known joint numerical-range convexity supplies the dimension ≥3 exclusion directly. For \(H_j=\Psi^*(\sigma_j)\), pure-input Bloch vectors form
   \[
   \{(\langle f,H_1f\rangle,\langle f,H_2f\rangle,\langle f,H_3f\rangle):\|f\|=1\}.
   \]
   This set is convex when the complex input dimension is ≥3, as stated in the primary research paper [*Joint matricial range and joint congruence*](https://faculty.sites.iastate.edu/ytpoon/files/inline-files/AOT_1.pdf). **My inference:** a convex set contained in a sphere of fixed radius must be a singleton, giving replacement.

   **Correction:** add this prior-art connection. It substantially weakens a novelty argument based on the dimensional exclusion, although the bounded searches did not locate a source explicitly stating the entire optical classification.

2. **The promised execution history is missing from the reviewed snapshot.**  
   [RESULTS.md:267](/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/RESULTS.md:267) ends with a placeholder. The two earlier failures described in the assignment are not recorded there.

   **Correction:** disclose the symbolic eigenvalue-dictionary comparison failure, its replacement by characteristic-polynomial identities, and the near-dark normalized-ratio failure followed by conditioning control. The successful [verification output](/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/results/verification.json:91) transparently records 21 degree samples versus 33 matrix samples in the focused cases.

   Also reword [code/verify.py:91](/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/code/verify.py:91): averaging two opposite outputs certifies a **mixture witness**, not the three-dimensional pure-input exclusion.

   The propagation representations are meaningfully independent algorithms: source-CSD double contraction versus covariance-factorized Jones fields propagated by FFT. They share the source and paraxial model. Their agreement checks implementations and sampled propagation, not universal claims or continuum error bounds.

3. **C2’s classification, including the disputed dimensional exclusion, passes.**  
   [RESULTS.md:95](/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/RESULTS.md:95), lines 95–158.

   The Choi convention is consistent with the physical contraction:
   \[
   J(f)=\sum_{ab}f_af_b^*\Gamma_{ab},\qquad
   T_{ab}=\operatorname{tr}\Gamma_{ba}.
   \]
   The transpose in the latter identity matters. The source factorization \(\Gamma_{ab}=T_{ba}C\) is consequently correct.

   For singular \(T\), zero trace of a positive output forces every Kraus operator to annihilate \(\ker T\); mixed terms involving that kernel vanish. Whitening on the support is therefore legitimate. A small standalone calculation independently checked the complex conventions and null mixed terms for both exceptional branches with rank-deficient \(T\).

   The higher-dimensional proof has no missing step: the compression on \(V=\operatorname{span}(e_2,e_3)\) is constant. Every subsequent nonconstant compression on \(\operatorname{span}(e_1,w)\) forces
   \[
   |\langle e_1,B_xw\rangle|=1.
   \]
   A complex linear functional on the two-dimensional complex space \(V\) has a nonzero kernel, contradicting this requirement.

   The boundaries also pass: \(p=0\) gives replacement; \(p=1\) is permitted for B; \(p=1/3\) is permitted for C with Choi eigenvalues \(2/3,2/3,2/3,0\). Trace-support dimension one gives only replacement; dimension zero and zero-intensity probes are correctly excluded. **No mathematical correction is needed.**

4. **C3 is correct; preserve the whitening convention when quoting its mixture formula.**  
   [RESULTS.md:168](/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/RESULTS.md:168), lines 168–190.

   Equal mixtures of distinct Bloch vectors of length \(p>0\) have smaller length. Hence constant degree for every PSD response forces replacement. The \(p=0\) case follows directly by linearity.

   The displayed \(P[\Psi(R)]=pP(R)\) is correct for the **whitened** response. For an original modal response \(R\), use
   \[
   S=T^{1/2}RT^{1/2},\qquad P[\Phi(R)]=pP(S).
   \]
   For example, \(T=\operatorname{diag}(4,1)\), \(R=I/2\), and \(p=1/2\) yield output degree \(3/10\), although \(P(R)=0\).

   **Clarification:** retain this distinction in summaries. The manuscript’s formula already uses \(\Psi\) correctly. Its source–medium independence assumption and restriction to arbitrary mathematical mixtures are also explicit; necessity for a particular turbulence model does not follow.

5. **C1 and C5 have the necessary quantifier boundaries.**  
   [RESULTS.md:51](/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/RESULTS.md:51) and [RESULTS.md:235](/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/RESULTS.md:235).

   C1’s two-dimensional Fourier scaling correctly cancels the \(k^2\) Fraunhofer prefactor. Necessity uses every transverse angular coordinate and Fourier inversion under the stated integrability assumptions. It cannot be transferred to a bounded physical hemisphere or the complete source kernel.

   C5 correctly requires the same achromatic input vector across frequencies. Equality of all quadratic forms gives \(T_\omega=B(\omega)T\), including singular support. With chromatic physical probes, \(f(x,\omega)^\dagger Tf(x,\omega)\) must additionally separate. Constancy in frequency of the degree is a separate condition.

   **No correction is needed.** The baseline distinction is supported by [Wolf’s abstract](https://opg.optica.org/ol/abstract.cfm?uri=ol-32-23-3400), which states sufficiency for source-plane/far-zone degree equality. The Zhao full-text link was inaccessible during the bounded checks.

6. **C4’s sources are positive, finite-energy counterexamples to the stated implications.**  
   [RESULTS.md:198](/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/RESULTS.md:198), lines 198–229.

   The kernels are sums of nonnegative covariance outer products. Their spatial norms are
   \[
   \|u_0\|_2^2=\pi w^2,\qquad \|u_a(\cdot;k)\|_2^2=\pi/a^2.
   \]
   Thus an integrable nonnegative spectrum gives finite integrated power.

   The first source has constant local degree \(1/2\), while its far-zone trace \(B(k)k^2e^{-w^2k^2|s|^2}\) is nonseparable. The second has separable far-zone trace and local degree changing from \(0\) to \(1/3\) at the stated angular radius. Both witnesses apply to the same far-zone observation set.

   Local and spatially averaged polarization remain distinct: the second source’s spatially integrated degree is \(3/5\), despite its varying local degree. The rational on-axis spectrum example additionally demonstrates source-plane spectral change; it is not being substituted for the far-zone separability argument. **No correction is needed.**

Strongest defensible claim wording:

> **PARTIAL.** Under the stated integrability assumptions in the ideal full-plane paraxial far-zone model, normalized-spectrum invariance is equivalent to \(G(v;k)=B(k)g(kv)\). For finite-mode positive sources, constant local two-component spectral degree under every deterministic scalar probe admits exactly replacement and the stated trace-whitened two-mode branches; invariance under every independent incoherent probe mixture forces replacement. The two invariants are logically independent. These results do not classify unrestricted free-space or Maxwell propagation, and novelty is not established.