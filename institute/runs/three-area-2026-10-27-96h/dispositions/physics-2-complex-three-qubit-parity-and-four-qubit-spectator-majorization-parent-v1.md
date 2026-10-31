# Entire complex three-qubit parity sector and four-qubit spectator hull: full physical majorization

**Disposition: scoped same-harness written support with independently authored physical-channel corroboration.** Native observation before composition: 2026-10-30T11:23:19-0700 PDT. f428/f429 reconstruct the theorem without mathematical findings; f429 explicitly reports **0 FATAL / 0 MAJOR / 0 MINOR**. This is not arbitrary three-qubit input, all1|3separable four-qubit input or unrestricted four-qubit majorization.

## Every complex density, every projector and the full physical interval

Let Phi_p(X)=(1−p)X+(p/2)Tr(X)I2, 0<=p<=4/3, t=abs(1−p), a=(1+t)/2,b=(1−t)/2. For EVERY complex three-qubit density rho commuting with Z⊗Z⊗Z, all8 output eigenvalue prefixes obey

K_k(Phi_p^tensor3(rho))<=K_k(diag(a,b)^tensor3), k=1,...,8.

Equivalently every complex orthogonal rank-k projector obeys that trace bound. The same holds in arbitrary physical local bases, equivalently commuting with A1⊗A2⊗A3 for traceless Hermitian one-qubit unitaries Ai. Both positive4×4parity blocks may be arbitrary complex matrices; the fixed-basis density sector has affine dimension31, not just diagonal/X states.

Tensoring ANY such factor with an arbitrary single-qubit density, at any spectator position, gives all16 product-reference prefixes on four qubits. Finite mixtures allow different spectators, bases and factors by component. They can also be adjoined to the independently adopted [A/B hull](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-two-coefficient-and-paired-repetition-all-prefix-majorization-parent-v1.md) and [equal-amplitudeW4 orbit hull](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-symmetric-w4-orbit-all-prefix-majorization-parent-v1.md), since each has the same reference and the SAME fixed consuming projector can be averaged. No new relative-hull separation involving W4 is claimed here.

## Actual physical blocks and coupled deficit proof

For a pure even-parity input in e=(000,011,101,110), coefficients c∈C4, put R=cc†, D=diag(abs(c_i)²), A=(1−t)D+tR and B=(1+t)D−tR. In the e basis and complementary odd basis, ACTUAL channel output blocks are

M_E=ab² I+at A, M_O=a²b I−bt conjugate(B).

The complex conjugation in the complementary block is essential. A>=0,TrA=1; B<=I and has at mostone negative eigenvalue. If alpha=maxeig(A), gamma=max(0,−mineig(B)), delta=bt gamma, then gamma<=max(0,(3t−1)/4)<=a/2 and gamma<=2t(1−max_i abs(c_i)²). Since alpha<=t+(1−t)max_i abs(c_i)², these give delta<=at(1−alpha) and2delta<=abt. The estimates include zero populations and t0/1/1/3.

Write u=a³,d=a²b,c0=ab²,ell=b³. Every block prefix is bounded by the ordered four-vectors (u−delta,c0+delta,c0,c0) and(d+delta,d,d−delta,ell). Their globally ordered union is

(u−delta,d+delta,d,d−delta,c0+delta,c0,c0,ell).

Relative to the ordered product-reference (u,d,d,d,c0,c0,c0,ell), its8 cumulative deficits are(delta,0,0,delta,0,0,0,0). Direct-sum KyFan allocation therefore proves the full8prefix comparison without restricting the projector to a block or independently maximizing incompatible observables. Odd pure states follow by local covariance; spectral decomposition and convexity give every mixed parity state. For p>1, FULL transpose/spin-flip preserves spectra and transports Q to Y^tensorn Q^T Y^tensorn. The two signs from odd n cancel; a partial transpose or stale Q is not valid. Positive tensor-majorization then proves the spectator theorem.

## Nontrivial exact physical example and strict old-hull enlargement

The pure spectator state Omega=|0>⊗(|100>+i|010>+|001>)/sqrt3 is in the new class and outside the ENTIRE earlier A/B hull. Its three-qubit factor has tensor rank3 by its two-qubit Schmidt support's one-product-ray determinant −iv², excluding A. In any pairing, the spectator-containing pair has support |0>⊗C2, whose support-projector spectator marginal is2|0><0|, unlike I2 for any local repetition code, excluding B. Purity excludes decompositions into other positive A/B states. This establishes strictness over A/B alone.

At p1/4 the three-qubit factor has exact ordered spectrum(287,57,49,35,35,21,21,7)/512. A genuinely complex rank3 Q has expectation393/512; the actual four-qubit same-projector value is2751/4096<3087/4096. Its corresponding even parity block has max57/512>49/512 for the product-input even block. Thus separate corresponding-block majorization is FALSE, while full output majorization holds. No blockwise shortcut is imported.

## Evidence and assurance ceiling

[Author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f397-depolarizing-unrestricted-or-three-qubit-bridge-frontier/review-v1.md) · [Complex-block written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f428-depolarizing-complex-parity-sector-block-deficit-written-review/review-v1.md) · [Tensor/separation written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f429-depolarizing-parity-tensor-four-qubit-separation-written-review/review-v1.md) · [Independent finite report](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f430-depolarizing-parity-independent-exact-physical-check/review-v1.md) · [Exact/numerical physical verifier](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f430-depolarizing-parity-independent-exact-physical-check/independent-complex-parity-physical-channel-v1.py) · [Actual parent run](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f430-depolarizing-parity-independent-exact-physical-check/parent-independent-finite-run-v1-receipt.json). Parent displayed all711author,458/566written-review and1147finite-report/source lines, reconstructed all complex blocks, coupled inequalities, ordering, odd-n transpose signs, positive tensor preservation and pair-support separation, and checked frozen pins. The f428 packet did not contain the historical A/B theorem as a standalone source; f429 DID, and parent retains that exact already-adopted import rather than claiming a fresh source-wide proof.

The independent code was parent-run ONCE, exit0. Actual matrix-unit and separate Pauli implementations agree exactly, with Gaussian-rational PSD/trace/projector/observable checks. W3 and spectator spectra and allprefixes are EXACT via complete orthogonal spectral-projector resolutions. The broader96case/1024prefix coverage is NUMERICAL Jacobi at tolerance2e−9, not exact/interval-certified: observed worst excess2.22044604925e−16 and residual8.60382872106e−13. Eight intended-invariant scientific mutations are rejected, including physically valid CPTP factor changes and stale/missing-transpose observable controls. Child execution was NOTRUN. Neither finite scope replaces the universal written theorem.

Cross-parity coherences, arbitrary three-qubit factors, all1|3separable states and unrestricted four-qubit k3/allprefixes remain unpaid. Earlier formally stronger printed source claims cannot be accepted from their inspected [false ancillary proof step](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-public-ancillary-orbit-span-proofstep-obstruction-parent-v1.md); that finding does NOT refute the theorem. A new ancillary repair/tensorization countermodel is still under review. Novelty/priority, original-target closure, human/independent-family and formal/kernel acceptance are not claimed. All genuine held episodes/consumers remain NONINPUT.
