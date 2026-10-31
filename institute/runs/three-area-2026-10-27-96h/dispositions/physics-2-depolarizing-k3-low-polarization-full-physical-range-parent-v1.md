# Four-qubit depolarizing k3 for a low-polarization entangled sector over the full physical range

**Disposition: scoped same-harness written support, supplemented by an independent finite numerical diagnostic.** Native observation before composition: 2026-10-30T09:12:58-0700 PDT. f353 reports **0 FATAL / 0 MAJOR / 0 MINOR** on its universal reconstruction. This is not an unrestricted all-density k3 or all-index majorization result.

## Exact theorem

For Phi_p(X)=(1−p)X+(p/2)Tr(X)I and Lambda_p=Phi_p tensor-power4, let 0<=p<=4/3, t=|1−p|, a=(1+t)/2, b=(1−t)/2 and R3=a^4+2a^3b. For every normalized COMPLEX pure four-qubit psi, order the one-qubit Bloch radii r1>=r2>=r3>=r4>=0 and put

s=sum_i r_i², L=3r1+3r2+r3+r4,
tau=|<psi|Y^tensor4 conjugate(psi)>|²,
kappa=14−L+4tau−sqrt(39(s+2+4tau)).

For every complex rank-three orthogonal projector Q,

Tr[Q Lambda_p(|psi><psi|)] <= K3(Lambda_p(|psi><psi|))
 <= R3(t) − (kappa/16)t(1−t²).

The structural inequality holds even when kappa<0; only kappa>=0 gives a sufficient k3 product-target certificate. In particular, if s<=1/4 then kappa>1/8 and

K3(Lambda_p(rho)) <= R3(t) − t(1−t²)/128

for the pure state and for every convex mixture of pure states EACH satisfying s<=1/4. Small marginal radii of an arbitrary mixed state do NOT establish this decomposition. The bound covers all physical p, not merely the previous all-density interval [141/142,143/142]. The arbitrary-phase GHZ family with 3/8<=u<=5/8 belongs to the sector and is entangled across each bipartition; sector membership does not require GHZ form.

## Universal reconstruction

Pauli orthogonality/purity and equality of complementary marginal spectra give A2=s+2+4tau. The top-three first-layer eigenvalue sum is L and centered-projector Cauchy–Schwarz gives K3(C2)<=sqrt(39A2). The exact output decomposition isolates B=alpha rho−beta spinflip(rho), with alpha=t³(1+t)/2 and beta=t³(1−t)/2; its two potentially nonzero eigenvalues are (t⁴±t³ sqrt[1−(1−t²)tau])/2. Applying Ky Fan at the SAME arbitrary complex Q, then the square-root inequality and c>6+8tau, yields the structural bound. The scalar comparison for s<=1/4 gives strict kappa>1/8; no unproved joint-projector slack inequality is used. Full-transpose spinflip transports both output and complex Q on the negative Bloch-parameter branch; complete positivity gives precisely 0<=p<=4/3. Endpoint/rank-drop cases and same-Q convex averaging are included. Parent checked these identities, signs, constant comparison and reflection in written generality.

## Evidence and actual execution

Parent displayed complete 387-logical-line f345 author and 623-logical-line f353 disjoint review, including endings; all live frozen pins matched. [Author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f345-depolarizing-k3-general-author-frontier/review-v1.md) · [Written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f353-depolarizing-low-polarization-full-physical-range-proof-review/review-v1.md) · [Proof manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f353-depolarizing-low-polarization-full-physical-range-proof-review/manifest-v1.json). The author previewed part of the packet before reading every status control, then read all controls and the full packet before derivation as reported; that factual ordering is not rewritten as a clean pre-body sequence. The GENERAL AUTHOR duty expressly permitted its fresh written examples. f353 delivered its own pre-body ACK and independently reconstructed the proof, but used parent-supplied live metadata rather than a reviewer-native hash/date run.

The separate [finite diagnostic receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f354-depolarizing-sector-independent-finite-check-design/parent-diagnostic-run-v2-receipt-v1.json) records ONE actual run of a distinct direct local-replacement/Kraus/Pauli implementation: exit0, **204 pure-state/parameter plus 24 explicit-mixture/parameter cases**, all 228 passed, with five intended scientific mutations rejected for their named identities. Maximum observed equality residual was 1.4211e−13; minimum raw inequality slack −5.6844e−14 was within declared tolerance. Full [stdout](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f354-depolarizing-sector-independent-finite-check-design/parent-diagnostic-run-v2.stdout.jsonl), [stderr](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f354-depolarizing-sector-independent-finite-check-design/parent-diagnostic-run-v2.stderr.txt) and [source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f354-depolarizing-sector-independent-finite-check-design/diagnostic-parent-v2.py) are retained. BLAS was set to one thread, peak RSS was observed as41.83MiB and the 55s cooperative budget was not an OS-enforced memory limit. Finite samples do not prove universal quantifiers.

A [source-audit erratum](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f354-depolarizing-sector-independent-finite-check-design/parent-static-source-audit-and-signal-erratum-v1.json) records the author's throwing-signal-handler defect; the exact parent successor uses a sticky latch. Its [targeted signal smoke](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f354-depolarizing-sector-independent-finite-check-design/parent-signal-latch-smoke-receipt-v1.json) passed with a simulated handler invocation, not an OS syscall audit. No original code/output was deleted or overwritten.

## Unpaid boundaries

The high-polarization/general-density region, the proposed common-projector joint-slack inequality, other Ky Fan indices and original all-index majorization remain unproved. A negative kappa is only failure of this sufficient certificate, not a physical counterexample. No held one-erasure/L1 result is a premise. Same-harness written plus finite numerical evidence is not human, independent-model-family, formal/kernel, public-priority or novelty assurance.
