# Actual non-invariant four-qubit densities: uniform defect regions and genuine extension

**Disposition: scoped same-harness written support with independently authored exact physical-matrix checks and explicitly NUMERICAL spectral corroboration, parent-run once.** Let \(\widetilde\rho=Y^{\otimes4}\rho^TY^{\otimes4}\), \(\sigma=(\rho+\widetilde\rho)/2\), and \(d=\|\rho-\sigma\|_1=\tfrac12\|\rho-\widetilde\rho\|_1\). For the ACTUAL four-qubit depolarizing channel \(\Phi_p(X)=(1-p)X+(p/2)\operatorname{Tr}(X)I\), every physical \(p\in[0,4/3]\) and all sixteen prefixes satisfy the product-reference majorization in each of these sufficient regions:

\[d^2\le\frac3{13}\quad\text{for ANY mixed density};\qquad \eta=|\langle\psi|\Theta_4\psi\rangle|^2\ge\frac{55}{72}\quad\text{for pure densities}.\]

For pure inputs \(d^2=1-\eta\), so the second bound is \(d^2\le17/72\), slightly larger than the first. Every FINITE convex mixture of pure-region states also satisfies the conclusion by fixed-projector linearity; it need not itself retain the pure rank bound. Threshold equality is included. These are sufficient, not necessary or optimal, regions. **Unrestricted non-invariant four-qubit majorization remains open.**

The reference is \(D_t=\operatorname{diag}((1+t)/2,(1-t)/2)^{\otimes4}\), \(t=|1-p|\). The proof always uses ONE arbitrary physical complex consuming projector Q and the SAME actual density/marginals, not independently optimized incompatible marginal data.

## Actual Pauli coupling and the moment thresholds

For \(R_w=\sum_{\operatorname{wt}P=w}\operatorname{Tr}(\rho P)P\) and \(S_w=\sum_{\operatorname{wt}P=w}\operatorname{Tr}(\rho P)^2\), physical partial traces give

\[H_1=2I+\tfrac12R_1,\quad H_2=\tfrac14(6I+3R_1+R_2),\quad H_3=\tfrac18(4I+3R_1+2R_2+R_3).\]

Spin flip keeps precisely the even weights. Thus \(\Delta=\rho-\sigma=(R_1+R_3)/16\), \(H_2(\rho)-H_2(\sigma)=3R_1/4\), and the odd H3 difference is \((3R_1+R_3)/8\). Each physical singleton Bloch length is at most d by trace-norm contraction; \(S_1\le4d^2\). Since Delta is traceless Hermitian, \(\operatorname{Tr}\Delta^2\le d^2/2\), giving \(S_1+S_3\le8d^2\).

For pure inputs, complementary marginal purities and spin-flip overlap reconstruct the UNRESTRICTED identity \(\operatorname{Tr}H_3^2=8+3S_1+2\eta\). Every invariant pure component has S1=0,eta=1, so the invariant mixed midpoint obeys \(\operatorname{Tr}H_3(\sigma)^2\le10\) by convexity. Orthogonality of even and odd Pauli sectors then proves, for every actual mixed input,

\[\operatorname{Tr}H_3(\rho)^2\le10(1+d^2).\]

H3 is positive, trace8, and at most4I. For pure inputs the ACTUAL Pauli twirl writes it as thirteen rank-one terms, so rank≤13. Cauchy–Schwarz on padded eigenvalue lists gives sufficient H3-majorization moment thresholds160/13 at padded rank16 and445/36 at padded rank13. The corresponding defect thresholds are3/13 and17/72. Rank-deficient cases are included by padding, not division by actual rank minus the prefix. Failure of either sufficient threshold is not a physical counterexample.

## Compatible H2, common Q and the actual channel

The load-bearing [adopted ENTIRE invariant-sector theorem](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-all-mixed-spinflip-invariant-fourqubits-sharp-fourth-prefix-and-channel-parent-v1.md) supplies H2(sigma)=I+H3(sigma), H3(sigma)≤2I, trace8 and SHARP K4(H3(sigma))≤6. This is used ONLY on the actual invariant midpoint sigma, not on arbitrary rho.

The remaining H2 operator is3R1/4. After physical local rotations it is a convex mixture of local-bit-flipped conjugates of \(d(3/4)\sum_iZ_i\). Combining its exact Ky Fan prefixes with the invariant bound proves **H2(rho)≺(6,3×4,1×6,0×5) whenever d≤1/2**. Both new regions have d<1/2. The sharp invariant fourth-prefix6, rather than the trivial8, is essential to the compatible fourth-prefix step.

For positive retention, the actual expansion \(t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I\), b=(1−t)/2, applies to ONE Q. The product-reference marginal layers are coordered by physical Hamming weight, and their weighted sum is EXACTLY Dt, not a larger relaxed comparator. Rank3 and rank4 output gaps are at least \((3-6d)t^2b^2\) and \((5-15d/2)t^2b^2\), respectively, strictly positive for0<t<1 in both regions. All sixteen prefixes and both endpoints are included. Negative retention uses the FULL-transpose transport \(Q\mapsto Y^{\otimes4}Q^TY^{\otimes4}\), valid for arbitrary complex Q, not a partial transpose or real-projector shortcut.

## A universal genuinely entangled addition to the named prior hull

For the literal two-excitation Dicke state D, take ANY unit Theta4-fixed y orthogonal to D, and any0<theta<pi/4 with \(\sin^2(2\theta)\le17/72\). Then \(\psi=\cos\theta D+i\sin\theta y\) has eta=cos²(2theta)∈[55/72,1), so the theorem applies. No independent local normal forms for its real and imaginary parts are assumed.

D’s second Schmidt singular value is at least1/√6 on ALL seven bipartitions. The uniform vector perturbation is2sin(theta/2)≤theta<pi/12<1/3<1/√6, so every such pure state remains genuinely four-party entangled. Its intermediate eta excludes pure invariant and Dicke-orbit states (eta1) and coherent-vacuum–W4 orbit states (eta0); genuine entanglement excludes biseparable states. Positivity of a convex mixture equal to a rank-one density forces every component onto the same ray, so the new family is outside the convex hull of ALL FOUR named prior classes, including their mixed components. This is a strict extension relative to that named hull, NOT a literature-wide novelty claim or assertion that every mixed state/mixture is genuinely entangled.

## Evidence and exact-versus-numerical verification

[Complete f598 author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f598-actual-noninvariant-four-qubit-common-projector-majorization-frontier/review-v1.md) · [f612 defect/moment/H2 written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f612-fourqubit-spinflip-defect-moment-and-physical-h2-written-review/review-v1.md) · [f613 pure-region/common-Q/GME written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f613-fourqubit-defect-pure-stratum-and-outside-hull-common-projector-review/review-v1.md) · [f614 independent physical report/source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f614-fourqubit-defect-region-independent-actual-physical-finite-check/review-v1.md) · [materialized checker](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f614-fourqubit-defect-region-independent-actual-physical-finite-check/independent-fourqubit-defect-physical-v1.py) · [actual parent one-shot receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f614-fourqubit-defect-region-independent-actual-physical-finite-check/parent-independent-finite-run-v1-receipt.json). Parent displayed765/647/477/974 logical author/review/source lines. Both WRITTEN gates report0F/0M/0m at the exact imported invariant interface; neither infers the universal proof from a finite sample.

After full static read and GO, the independent stdlib checker ran ONCE: exit0, empty stderr,7.735s. Exact arithmetic in Q(√15,i) checks actual16×16 states, physical partial traces, Pauli layers, channels, trace-norm identities for the selected inputs and fixed complex-Q expectations. Eleven actual densities at seven physical p values yield77 cases and1232 NUMERICAL prefix comparisons; two densities are explicitly OUTSIDE-REGION diagnostics, so their spectral comparisons are not counted as theorem-region assertions. The enforced scoped subset also includes one already-proved eta0 coherent control. Numerical spectral tolerance2e−9; observed maximum eigenpair Frobenius residual1.3524e−13, orthogonality residual5.108e−15 and off-diagonal row residual9.887e−14. Numerical spectra are NOT exact roots.

The actual pureq15/16 state has eta49/64, d²15/64, lies inside the larger pure region but OUTSIDE the mixed sufficient bound, and has nonzero2eta=49/32, genuinely distinguishing that moment coefficient—unlike the earlier eta0-only family. A complex Dicke perturbation gives correct transported expectation77/972 versus omitted-transpose1193/16524, discrepancy29/4131, checked EXACTLY. Ten intended controls include explicitly limited endpoint/rank/mixture-GME scope guards, not channel counterexamples; the maximally mixed H3 rank16 shows why the pure rank13 argument cannot be applied to every mixed input.

The all-p/universal conclusions rest on the written physical proof. Higher-defect/non-invariant inputs outside these sufficient regions, global four-qubit/all-blocklength majorization, source equivalence, novelty, independent-model-family/human review and a formal kernel remain unpaid. All held episodes and ALL consumers remain NONINPUT; no stopped fragment is reused.
