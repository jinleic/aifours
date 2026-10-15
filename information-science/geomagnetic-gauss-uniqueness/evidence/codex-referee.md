I found **no FATAL mathematical error in Theorems 1–10 under their stated models**. The R1–R4 conclusions survive the audit. There is one MAJOR status claim and two MINOR formulation defects. The book-level conclusion is defensible only with its exact-data qualifications retained.

I read `proof.md` in full, the README and reference ledger, both Chinese pages, and the relevant collected primary texts and formula images. No project code, tests, or numerical checks were run.

1. **MAJOR — “Not resolved here” does not establish mathematical openness.**  
   Location: [README.md:64](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/README.md:64).

   The combined **“OPEN”** label for classification, optimal noisy inference, and physical-current inversion is unsupported. These are different questions, and the latter two lack sufficiently specified mathematical formulations.

   Unrestricted current uniqueness is demonstrably false: choose a nonzero smooth solenoidal field \(B_0=\nabla\times A\) supported inside \(K\), and set \(J=\mu_0^{-1}\nabla\times B_0\). These nonzero currents produce zero exterior field and hence zero exterior Gauss coefficients. That uniqueness question is not open. The defensible status for the bundled row is **“NOT ADDRESSED / not adjudicated.”** This does not undermine R1–R4.

2. **MINOR — The finite-sampling theorem overstates its measurement-domain quantifier.**  
   Location: [proof.md:189–191](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:189).

   “Any locations \(x_j\ne0\)” is sufficient for evaluating the constructed finite multipoles. It is insufficient for the subsequent assertion about **any admissible \(V\)**: such a candidate is only guaranteed to exist on \(\Omega\). A sample could lie inside \(K\), or outside \(O\), where that candidate is undefined or singular.

   Require \(x_j\in\Omega\) for the perturbation assertion. The intended surface-sampling R3 is unaffected. The dimension calculation \(N(N+2)>3M\), rank-nullity argument, and proof that a nonzero kernel potential has a nonzero field are correct.

3. **MINOR — Conversion to conventional Gauss coefficients needs a basis convention.**  
   Location: [proof.md:17–21](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:17).

   The moment formulas correctly determine \(A,C\) in **any specified orthonormal real spherical-harmonic basis**. Conventional \(g,h,q,s\), however, are individual normalization/radius rescalings only if that basis is the corresponding conventional real cosine/sine basis.

   For example, replacing degree-one \(Y_x,Y_y\) by \((Y_x\pm Y_y)/\sqrt2\) mixes the conventional coefficients. Specify the basis, or allow a fixed invertible basis transformation. Uniqueness is unaffected.

4. **NOTE — The book interpretation is faithful, but conditional.**  
   Locations: [book p.880](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/sources/page-0901.png), [book p.881](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/sources/page-0902.png), [README.md:38–52](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/README.md:38).

   The images explicitly show both internal and external radial powers and ask about tangential plus vertical observations. R1 therefore does **not** silently discard external sources.

   The book does not spell out your topology, source clearance, or noiseless continuum contract. Those are declared modeling hypotheses, not quotations. Under them, ordinary Cauchy uniqueness answers the proposed fourth-boundary-condition question.

   The book also explicitly discusses finite measurements, approximate least squares, and truncated representations. An exactly finite underlying field is stronger than approximating an infinite field by a truncation. Your R4finite distinction correctly preserves this difference. I found no substantive book-level reinterpretation error, provided the qualifications in the [final verdict](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/README.md:117) remain.

5. **NOTE — Connectedness, single-valuedness, and gauge hypotheses are sufficient.**  
   Location: [proof.md:7–21](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:7).

   Connected \(S\) gives one trace constant. Connected \(\Omega\), \(O\), and \(\mathbb R^3\setminus K\) support the respective continuation conclusions. Global scalar potentials remove the period obstruction on positive-genus surfaces; curl-free alone would not suffice.

   The \(O(r^{-1})\) condition fixes the internal constant. Shifting the recovered trace shifts only the external potential. Zero flux correctly removes the internal monopole. No unjustified genus-zero reduction occurs.

6. **NOTE — Green signs, coefficient moments, and spherical separation check out.**  
   Locations: [proof.md:29–75](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:29).

   With \(-\Delta G=\delta\), the displayed operator satisfies
   \[
   H_{V_e}=V_e\text{ inside},\quad H_{V_e}=0\text{ outside},
   \]
   \[
   H_{V_i}=0\text{ inside},\quad H_{V_i}=-V_i\text{ outside}.
   \]
   The exterior inner-boundary normal is indeed \(-n\); the infinity term vanishes with the stated derivative estimate.

   For \(d\omega\)-orthonormal harmonics, the Newton expansion coefficient is \(1/(2n+1)\). Both moment signs and normalizations are correct. Strict radial separation justifies differentiated kernel-series integration. The general-surface argument does not assume a common spherical convergence shell.

   The spherical system and its determinant \(-(2n+1)\) are correct.

7. **NOTE — The continuity claims use the correct norms and degree weights.**  
   Location: [proof.md:83–113](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:83).

   Surface Poincaré and Cauchy–Schwarz establish the finite-coefficient Lipschitz bounds. In Eq. (9), expansion of
   \[
   |(n+1)I-nE|^2+n(n+1)|I+E|^2
   \]
   gives exactly the stated weights and cancels the cross term.

   The continuation exponents \(n+1\) internally and \(n\) externally are correct for physical surface-area \(L^2(S_r)\), including its radius factor. The general-surface infinite coefficient bound is correctly restricted to the specified \(R_+,R_-\) weights.

   Eq. (9) requires the zero-monopole convention. Extending it to the optional monopole variant would require an additional \(|\delta I_{00}|^2\) term; \(V_i=1/r\) immediately demonstrates this.

8. **NOTE — Radial versus normal measurements are handled correctly.**  
   Location: [proof.md:119–129](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:119).

   Eq. (12) and the radial-graph normal formula are correct. For general closed \(S\), a maximum-radius point supplies a transverse open patch, which suffices for uniqueness. The argument correctly avoids claiming a global bounded division where \(n\cdot e_r\) vanishes. Geocentric horizontal components plus the radial component already determine the vector.

9. **NOTE — Patch uniqueness uses valid Cauchy continuation, not invalid surface analyticity reasoning.**  
   Location: [proof.md:133–149](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:133).

   The zero-extension integration-by-parts argument removes both interface distributions because both Cauchy traces vanish. Weyl’s lemma and analytic continuation then apply. A \(C^2\) observation surface is sufficient.

   Tangential integration supplies the constant on a connected subpatch, and the normal component supplies the second trace. Thus Theorem 6 is valid. The separate analytic-sphere assertion about internal potential or radial traces also holds under the collar assumption.

10. **NOTE — The explicit Kelvin instability sequence is valid.**  
    Location: [proof.md:151–181](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:151).

    The complex direction \((i,0,1)\) has bilinear square zero, so the polynomial is harmonic. Removing its constant term removes the Kelvin monopole; all remaining terms are internal degrees \(1,\ldots,N\), singular only at the fixed origin.

    The bound \(|t|^2\le1-\varepsilon/2\), gradient formula, and exponential decay after any fixed number of tangential derivatives check out. At the north pole, \(t=1\) and \(\partial_rt=-1/2\), giving exactly the stated field magnitude.

    The unobserved-cap hypothesis is essential. For a dense open patch, the supremum norm of a continuous field equals its whole-sphere supremum norm, so the same instability assertion would fail. The draft explicitly excludes that overclaim.

11. **NOTE — The finite scalar theorem covers nongeneric top harmonics.**  
    Location: [proof.md:203–221](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:203).

    Eq. (17) follows correctly from Euler’s identity. Lower-degree pairs cannot contribute to degree \(p+q\).

    The Fischer decomposition identifies vanishing top harmonic projection with divisibility by \(r^2\). A nonzero harmonic polynomial cannot have that divisor. Since \(x^2+y^2+z^2\) is irreducible and prime over \(\mathbb R\), its divisibility into \(H_pK_q\) would force divisibility into one factor. This proves the needed contradiction for arbitrary nonzero top harmonics.

    No fixed-frame highest-order coefficient assumption survives into this proof. The internal-only and decay restrictions are essential; the external \(x,y\) counterexample correctly demonstrates their necessity.

12. **NOTE — The Backus recurrence and its convergence are proved, not merely formal.**  
    Location: [proof.md:227–250](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:227).

    The Legendre identities yield the displayed \(A_l,B_l\), and cancellation requires exactly
    \[
    a_{l+2}=-A_la_l/B_{l+2}.
    \]
    For example, \(a_3=-7/48\). The two-step ratio limit \(1/3\), polynomial angular growth, and geometric majorant establish compact convergence for \(r>1/\sqrt3\). Interior harmonic estimates justify derivative convergence and cancellation; identities at the poles follow by continuity.

    Normalization agrees with the now-collected [Alberto Eq. 22 image](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/sources/alberto-eq22-4.png). Both \(D\) and \(U\) are nonzero, so the resulting pair is neither equal nor opposite.

    This establishes noninjectivity in the declared class. It does not establish ambiguity for every prescribed smaller source ball, every intensity function, or every infinite field.

13. **NOTE — The core prior-art verdict is supported; original-proof verification remains limited.**  
    Locations: [2010 review:1351–1363](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/sources/sabaka-hulot-olsen-2010.txt:1351), [Alberto:211 onward](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/sources/alberto-oliveira-pais-2004.txt:211), [reference ledger:19–29](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/sources/references.md:19).

    The 2010 chapter explicitly states one-sphere internal/external uniqueness and demonstrably predates the Chinese book. Gauss’s translated §40 states the separation; its two missing printed factors are visible and correctly repaired from the preceding equations.

    Alberto et al. supply an actual primary rederivation, not merely an attribution. Their convergence caveat also supports your refusal to assert a convergent orthogonal partner for every finite field.

    The original Backus 1968/1970/1986 proofs remain unread. BPC contents pages establish section locations only; theorem bodies remain unverified. These limitations do not invalidate the independently checked mathematical arguments.

14. **NOTE — Certification and numerical evidence remain separate.**  
    Locations: [proof.md:3](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:3), [proof.md:260](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/proof.md:260), [README.md:97–103](/Users/jinleic/jinleic-workspace/ai4s/geomagnetic-gauss-uniqueness/README.md:97).

    These are conventional written proofs, **not Lean/kernel-certified results**. Numerical results appeared during the audit; I did not independently reproduce them and used none as a theorem premise.

The final assessment of the formal readings is:

| Reading | Mathematical decision | Fully settled as claimed? |
|---|---|---|
| **R1 / R1-radial** | Exact admissible observations determine the field and source separation, with the stated potential gauge. | **Yes**, within the declared domains and hypotheses. |
| **R2** | Exact open-patch vector data give uniqueness; the specified restricted-patch inverse is unstable. | **Yes**; retain the instability norm and cap qualifications. |
| **R3** | Finite vector samples do not determine an untruncated field. | **Yes**, with the measurement-domain wording corrected. |
| **R4∞** | Intensity is noninjective even modulo global sign. | **Yes**; one convergent counterexample suffices. |
| **R4finite** | Two finite internal expansions with equal intensity differ only by global sign. | **Yes**, including nongeneric coefficients. |
| **R4mixed** | Even finite expansions are noninjective modulo sign. | **Yes**; uniform external fields suffice. |