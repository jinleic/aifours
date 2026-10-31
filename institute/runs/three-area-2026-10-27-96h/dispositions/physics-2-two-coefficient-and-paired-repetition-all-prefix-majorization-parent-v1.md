# Four-qubit depolarizing channel: constructive full majorization on two explicit sectors

**Disposition: scoped same-harness written support, with independent finite physical-channel corroboration.** Native observation before composition: 2026-10-30T10:21:28-0700 PDT. Disjoint f372/f373 reviews each report **0 FATAL / 0 MAJOR / 0 MINOR**. Unrestricted four-qubit k3 and unrestricted all-index majorization remain open.

## State classes and all physical parameters

Let Phi_p(X)=(1−p)X+(p/2)Tr(X)I, Lambda_p=Phi_p tensor4, 0<=p<=4/3, t=|1−p|, a=(1+t)/2, b=(1−t)/2, and D_t=diag(a,b) tensor4.

Let C be the finite convex hull of:

- **Class A:** pure states with at most two nonzero coefficients in ONE physical local orthonormal product basis. This is not every sum of two nonorthogonal product vectors.
- **Class B:** arbitrary complex logical two-qubit density operators encoded into span{00,11} tensor span{00,11}, with arbitrary physical local bases and any pairing of the four physical qubits.

Bases, pairings and decomposition choices may differ between mixture components. For every rho in C and every physical p, there is a finite ensemble, depending on rho,p but NOT on the consuming projector, such that

Lambda_p(rho)=sum_j w_j U_j D_t U_j†, w_j>=0, sum_jw_j=1.

Therefore Tr(Q Lambda_p(rho))<=K_k(D_t) for EVERY complex orthogonal rank-k projector Q and EVERY k=1,...,16. This is full output majorization on C, not an input-independent postprocessing channel or an unrestricted theorem.

## Constructive mechanisms

For Class A, reduce the two basis strings to an m-qubit cat plus4−m pure spectators, m=1,...,4. The actual output has complement-pair diagonal blocks and one complex endpoint2x2block. With delta=a^m−b^m, the endpoint half-gap h satisfies2h<=delta because delta>=t^m. A complex diagonalizer followed by a convex swap reproduces that block; independent block swaps and spectator tensoring give a finite whole-space unitary ensemble (at most256 choices for m=4). t=0, t=1, zero populations and tied eigenvalues are handled explicitly.

For Class B, the physical encoded-pair channel is exactly

E block: h F(X); O block: ell Tr(X)I2,
h=(1+t²)/2, ell=(1−t²)/4, gamma=t/h,
F=dephase_t composed with depolarize_gamma.

The independent logical-two-qubit Schmidt calculation gives the needed finite product-reference ensemble before random-unitary dephasing. The EE/EO/OE/OO blocks have matching actual/reference traces h²,2h ell,2h ell,4ell². Product probabilities and direct sums of their unitaries assemble the full ensemble without dividing by zero block traces. This applies to arbitrary correlated logical densities, not only logical products. Logical dephasing is not assumed covariant under arbitrary logical rotations.

Local physical covariance, qubit permutations and finite convex averaging preserve the claim. The physical negative branch uses full transpose/spin flip W=Y tensor4: Lambda_(1+t)(rho)=W Lambda_(1−t)(rho)^T W, with the consuming projector transported to WQ^TW. The reference orbit transports by U -> W conjugate(U); partial transpose is not substituted.

The classes cover all GHZ populations/phases, pure-spectator cats, complex X densities, row-diagonally-dominant densities in a local product basis, every state separable across any fixed2|2cut, and mixtures across those balanced cuts. They do NOT cover all1|3-separable or all biseparable states by this proof. Adding Class B strictly enlarges the Class A hull: a supplied pure product of two entangled pairs has Schmidt rank4 across a crossed cut, while every Class A vector has rank<=2 there.

## Same-projector consequence and evidence

With rho=(I+C1+C2+C3+C4)/16, tilde(rho)=Wrho^TW and B=t³((1+t)rho−(1−t)tilde(rho))/2, the positive-branch identity gives, for the SAME complex rank3 projector Q,

16Tr(QB)+(t−t³)Tr(QC1)+(t²−t4)Tr(QC2)<=8t+6t²+2t4.

Here t4 denotes t^4. The negative branch uses the reflected Q. No sum of separately attained layer maxima or unrestricted joint-slack premise is assumed. Prior low-polarization, regional and selected-prefix results retain their exact scopes, including the mandatory Class H moment/spin-flip erratum; this theorem does not subsume every old sector.

[Author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f363-depolarizing-common-projector-slack-frontier/review-v1.md) · [Class A review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f372-depolarizing-two-coefficient-unitary-orbit-proof-review/review-v1.md) · [Class B review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f373-depolarizing-paired-repetition-full-majorization-proof-review/review-v1.md). Parent displayed the full691-line author and961/775-line review/process bodies, reconstructed endpoint ensembles, physical encoded blocks, finite assembly, projector/reflection and exact examples, and checked all frozen input pins. f372 metadata was parent-supplied; f373 additionally reports three actual native metadata clock commands, not scientific execution.

[Independent f374 report/source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f374-depolarizing-orbit-sector-independent-finite-check/review-v1.md) · [Diagnostic](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f374-depolarizing-orbit-sector-independent-finite-check/diagnostic-v1.py) · [Actual parent run](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f374-depolarizing-orbit-sector-independent-finite-check/parent-diagnostic-run-v1-receipt.json): one run, exit0/PASS/complete,51physical states across9physical parameters=459cases, all16prefixes=7344actual-output comparisons,16literal Class A ensemble reconstructions, two exact-source examples and5 intended scientific mutations rejected while preserving their physical prerequisites. Direct replacement and separately implemented Pauli-Kraus channels agree. Parent elapsed1.477057875s, measured peakRSS42,958,848bytes, signal latch0; single-threaded BLAS was requested, not independently measured. Complete stdout is retained. Floating-point tolerance2e−10, mutation threshold1e−7; this is finite corroboration, not a continuum proof. The sticky-latch self-check invokes the handler directly, not an OS signal audit.

No human, independent-model-family, formal/kernel, original-source authenticity or novelty assurance is asserted. The unrestricted high-polarization/all-density k3 and all-index target remain unpaid; no whole-target closure or original-owner recovery follows.
