# Exact CP cone accepted by the free-marginal PPT SDP for k>=2

**Disposition: same-harness written support for the exact written SDP characterization, supplemented by one independently constructed exact finite control.** Native observation before composition: 2026-10-30T09:59:08-0700 PDT. f368 reports **0 FATAL / 0 MAJOR / 0 MINOR**. This is a limitation of one detector-certification route, not a4x4PPT/SN3 witness or global no-go, and priority is unresolved.

## Literal source scope and theorem

In [vom Ende–Khatri–Denisov, arXiv:2508.21348v2 §3.3 Eq.(6)](https://arxiv.org/html/2508.21348v2#S3.SS3), BOTH marginals are independently FREE density variables. Thus the feasible P are precisely trace-one PPT operators on (C^d tensor C^k)|(C^d tensor C^k); there are no extra fixed-marginal/separability/extension constraints. Use its UNNORMALIZED Choi convention. For every Hermiticity-preserving complex-linear Phi and k>=2,

F_k(Phi)>=0  IFF  C(Phi)>=0  IFF  Phi is COMPLETELY POSITIVE.

Moreover F_k=0 in the CP case and F_k<0 otherwise. The paper-relevant domain2<=k<=d is included; the displayed algebraic SDP also defines the same characterization for anyd>=1 and integerk>=2. No claim is made fork1.

## Universal proof

Let D_k be the normalized maximally entangled ancilla projector. Regrouping from AaBb to ABab gives C(Phi tensor id_k)=k C(Phi) tensorD_k, while the physical PPT transpose remains on BOTH A and a. For a negative Choi eigenpair (psi,lambda), ||psi||=1, define

Ppsi=[psi] tensorD_k + I_(d²) tensor(I_(k²)−D_k),
Z=TrPpsi=1+d²(k²−1).

Ppsi is PSD. With ancilla swapV and Pi±=(I±V)/2, its physical partial transpose is

([psi]^Gamma_A+(k−1)I)/k tensorPi+
 + (−[psi]^Gamma_A+(k+1)I)/k tensorPi−.

Schmidt decomposition of arbitrary COMPLEXpsi bounds its pure-projector PT spectrum between−1/2 and1, so this is PSD fork>=2. Its normalization has genuine density marginals, hence is feasible in precisely the free-marginal Eq6. Its objective is exactlyk lambda/Z<0. This is a feasible upper bound on F, not generally its minimum value. Conversely CP makes the objective nonnegative for every feasibleP; the separately feasible PPT density proportional toI tensor(I−D_k) has objective0, proving the stated CP value. Parent checked the tensor regrouping, transpose factors, normalization, complex Schmidt spectrum, objective and zero-witness argument in writing.

## Exact finite corroboration and limits

The parent independently constructed a selected d4,k2 check for Phi(X)=Tr(X)I4−X/2, one HALF of the author's supplied scaling. The map is2-positive by the written rank-two trace/nuclear-norm inequality and is notCP. Exact integer-scaled PSD projector identities and physical partial transpose give a feasible8x8 state of trace1 with objective−2/49 (the author's twice-scaled map has−4/49). The run exited0 and rejected three intended mutations: transpose onlyA instead ofAa, omit the PPT filler, and change the map scaling. [Run receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f362-ppt44-actual-witness-or-global-obstruction-frontier/parent-equation6-reduction-map-exact-v1-receipt.json) · [Code](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f362-ppt44-actual-witness-or-global-obstruction-frontier/parent-equation6-reduction-map-exact-v1.py) · [Exact output](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f362-ppt44-actual-witness-or-global-obstruction-frontier/parent-equation6-reduction-map-exact-v1.stdout.json). This selected control does not prove the generic theorem, cannot be called a4x4 target witness and does not independently prove the universal2-positivity criterion; that part is written mathematics.

The primary paper's implication F>=0 impliesk-positive remains CORRECT. The characterization shows that this particular sufficient test accepts onlyCP fork>=2; it does not refute the paper's theorem or rule out higher hierarchies, fixed marginals, extra constraints or different certificates. No author contact, external publication or exhaustive literature/novelty claim was made.

Parent displayed full502-line f362 source and complete434-line f368 written review, exact Eq5–8 snapshot and primary-definition passages; all frozen pins match. [Author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f362-ppt44-actual-witness-or-global-obstruction-frontier/review-v1.md) · [Review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f368-ppt-k-positive-free-marginal-sdp-collapse-proof-review/review-v1.md) · [Manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f368-ppt-k-positive-free-marginal-sdp-collapse-proof-review/manifest-v1.json). The reviewer independently consulted only the named publicv2 Choi/Proposition1 and Eq6 sections after its full packet; it did not inspect ancillarycode or sibling finite results. Hash/time metadata was parent-supplied, not reviewer-executed. Same-harness written plus finite exact evidence is not human, independent-model-family, formal/kernel, novelty or original-target acceptance.
