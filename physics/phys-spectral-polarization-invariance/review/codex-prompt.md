# Independent hostile referee: spectral/polarization invariance

Today is 2026-10-14. Review a bounded proposed contribution to the 2009 book problem by Zhao Daomu, “Spectrum invariance and polarization invariance in light propagation.” The assignment is NOT to prove the entire open-ended physical problem. We explicitly mark the result PARTIAL and novelty unclear.

## Permissions

Read only files inside `/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/`. Do not read workspace instructions, private material, credentials or files outside this folder. Do not delegate. Do not write or edit files, run network/account actions, install software, or launch a compute campaign. You may use public web search for up to six high-impact primary-source citation/novelty spot-checks. Do not run `code/verify.py`, because it writes its output. You may reason independently or execute small standalone, write-free algebra calculations. Final answer only; the caller captures it.

## Read set

- `RESULTS.md`: exact definitions, theorem C1, full classification C2, convex-mixture theorem C3, analytic counterexamples C4, achromatic joint criterion C5.
- `code/verify.py`: numerical/identity verifier.
- `results/verification.json`: actual successful execution output.
- `README.md`: scope language.
- `source/problem.zh.txt`: original book excerpt.
- `STATUS.md`, if it exists when you read: literature evidence map (being completed separately; do not delay or assume an absent file is a correctness error).

## Central claims to falsify

1. Paraxial full-angular-plane far-zone spectral invariance iff midpoint-integrated trace correlation has scaling `G(v;k)=B(k)g(kv)`. Fixed distance, two transverse dimensions, all transverse angular coordinates, integrability assumptions. Not full Maxwell / bounded physical hemisphere.
2. For a finite-mode PSD source covariance with 2 transverse polarization components, scalar probe `f` gives `Phi(ff*)`, a completely positive map. Trace-whitening makes it trace preserving on support of `T=Phi*(I)`. If local degree `P` is constant `p` for every pure spatial input / every deterministic scalar probe, the whitened map is either:
   - replacement `X -> tr(X) C`, any input support dimension;
   - support dimension 2 only: `p U X U* + (1-p)tr(X)I/2`, `0<=p<=1`;
   - support dimension 2 only: `p U X^T U* + (1-p)tr(X)I/2`, `0<=p<=1/3`.
   The proof excludes dimension >=3 using two-dimensional compressions and a complex linear functional on a two-dimensional orthogonal complement. Please examine this exclusion especially critically, as well as Choi/conjugation conventions and singular trace support.
3. Constant degree under every PSD modal response (arbitrary incoherent scalar-probe mixtures) iff replacement/factorization. Nonreplacement two-mode branches have ensemble `P_out=p P(R)`; deterministic invariance alone does not imply ensemble invariance.
4. Valid finite-energy positive source counterexamples show neither far-zone normalized-spectrum invariance nor constant polarization degree implies the other. All-distance and source-plane equality are carefully distinguished.
5. The simultaneous all-probe spectral condition `T_omega=B(omega)T` requires the same achromatic probe at all frequencies; physical chromatic propagation requires a further scalar separation condition.

## Existing evidence / checks

The successful verifier reports exact symbolic characteristic-polynomial and determinant identities; rational spectral weights `5/13,8/13`; `P=1/3` far-field counterexample; independent source-CSD Fresnel double integrals versus coherent-Jones-mode FFT for both exceptional families; scalar ABCD lens+free propagation; finite binary scalar phase-screen averaging; analytic Gaussian Schell-model controls with unequal correlation-width negative controls. The focused-beam numeric degree comparison excludes intensities below 1e-6 of sampled peak; all coherency-matrix samples remain checked. This is conditioning control, not a proof. There was an earlier failed dictionary eigenvalue-multiplicity comparison in SymPy and a failed near-dark normalized ratio; these are being disclosed in RESULTS execution history. No priority or continuum floating-point error-bound claim is made.

## Baseline sources

- Wolf, Optics Letters 32, 3400 (2007), DOI 10.1364/OL.32.003400, primary abstract explicitly says sufficiency and far zone, not unrestricted necessity: https://opg.optica.org/ol/abstract.cfm?uri=ol-32-23-3400
- Zhao et al., Optics Express 17, 17888 (2009), DOI 10.1364/OE.17.017888: equal three correlation widths and equal x/y source radii suffice for polarization-state preservation. https://opg.optica.org/services/open_md.cfm?uri=oe-17-20-17888
- Ruskai, Szarek, Werner, “An Analysis of Completely-Positive Trace-Preserving Maps on 2x2 Matrices,” arXiv:quant-ph/0101003. This supplies standard Bloch-affine/Choi geometry; the exact all-input-dimension constant-purity classification may be prior art and is NOT claimed new.
- Tao et al., arXiv:2302.12394, reports simulated DOP changes 1e-13 to 1e-6; its title is not treated as an exact universal invariance theorem.

## Requested final report

Give `correct / correct-with-fixes / incorrect` for mathematical claims, and separately `novelty not established / prior art located / potentially distinct` for novelty. List numbered findings, highest severity first, with precise file locations, counterexample or missing step, and a concrete correction. Verify hypotheses, quantifiers, edge cases p=0, p=1, p=1/3, zero intensity, rank-deficient T, actual positivity of sources, independence of numerical representations, and the difference between local and spatially averaged polarization. Do not invent a flaw merely to be critical. Do not treat numeric agreement as proof. End with the strongest defensible claim wording. Keep the final report focused and finite.
