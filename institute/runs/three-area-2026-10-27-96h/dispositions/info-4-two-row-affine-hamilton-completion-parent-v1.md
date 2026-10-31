# Parent disposition — info-4-two-row-affine-hamilton-completion-parent

Observed clock before writing: **2026-10-27T19:03:02-0700 PDT**. Same-harness written disposition; not formal/kernel, human, configured-family, executable or novelty acceptance. Independent-model CLI review not performed.

## Main source and review reads

- [Literal actual-row packet](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/written-releases/info-4-actual-rows-packet-v1.md), SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`, 37 LF; Main raw 1–37 (read for w103) through the ending.
- [ENTIRE v8 two-row completion](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/prerequisite-two-row-completion-v8.md), SHA256 `a7414abf523c8d76c26dca66fae4cf25ba255dbe58245167090010fc9ecb1bcb`, 134 LF; Main raw 1–45,46–90,91–134 through the ending.
- [ENTIRE v9 affine Hamilton cuts](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/prerequisite-affine-hamilton-cuts-v9.md), SHA256 `141812a7a8eeebc90c3da035ae1d9b9f3612898d843fa861209ae6e528f55324`, 101 LF; Main raw 1–50,51–101 through the ending.
- [ENTIRE v10 cycle-parity cut duality](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/prerequisite-cycle-parity-cut-duality-v10.md), SHA256 `a10074fff184f4978f19dc1bbda523c1f00b68214284d872497edb09c77f53d7`, 108 LF; Main raw 1–54,55–108 through the ending.
- [ENTIRE w36](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/review-w36-tuscan-two-row-affine-hamilton-v1.md), SHA256 `7591c06909f1375b254035e7e833a93e2b3e4ee9c9d175fbe266cc2859f049c6`, 201 LF; Main raw 1–50,51–100,101–150,151–201 through the ending.
- [w54](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/review-w54-tuscan-cycle-parity-cut-duality-v1.md) (PhysicsAME46-2, second review of v10 alone) was NOT read by Main for this gate; it adds no verdict here and is recorded as subsumed bookkeeping.

Reviewer PhysicsDepol4-2 returned 0F/0M/0m separately for v8, v9 and v10; same-harness/nonblind, with its own physics-2 provenance stop carried. All three predate the later post-v13 selected-graph and pre-ACK real-weight episodes (NONINPUT); timing gives no clean-cognition certificate. The unsupplied v6/v7 references are context only.

## Written-supported completion theory for the last two rows

Let n≥3 and take ANY n−2 actual linear permutation rows with distinct distance-one and distinct distance-two events.

1. **Sentinel equivalence (v8).** An original array is equivalent to a decomposition of the complete loopless digraph on X∪{∞} into n Hamilton cycles whose two-step paths with all three vertices in X have distinct outer pairs (no wraparound events counted).
2. **Residual parametrization.** If the fixed rows have distinct starts and distinct ends (otherwise no extension), the residual digraph D is 2-in/2-out regular; its bipartite double has c even-cycle components, and every proper 2-colouring is χ(e)=τ(e)⊕x_j.
3. **Exact D2 coupling.** For a used outer pair every residual two-step path must be bichromatic; for an unused pair with two paths, both must be bichromatic (they are monochromatic together, in opposite colours); one or zero paths impose nothing. These give affine equations x_j⊕x_k=1⊕τ(e)⊕τ(f), consistent iff every constraint cycle has label sum 0.
4. **Capacity (v8/v9).** Unused pairs split as |Z0|+|Z1|+|Z2|=3n−4 by available-path count; every Z0∪Z2 pair stays missing, so |Z0|+|Z2|≤n, i.e. |Z1|≥2n−4.
5. **Parity (v8/v10).** Both colours Hamilton requires N−c even (N=n+1; at n=11 an even component count), and individually Σ_(l_j even) x_j=b with b fixed by the reference colouring; after pairwise closure this is a possibly higher-arity relation on class bits.
6. **Cuts (v9/v10).** Both covers are Hamilton iff every nonempty proper vertex set has outgoing residual arcs of both colours. For the full affine system Mx=q (D2, two-arc cuts, HP1) assumed consistent, a nonempty cut is bichromatic in EVERY solution iff Mx=q together with the cut's monochromatic equations is inconsistent, iff an F2 dual certificate exists. Consistency plus a certificate for every proper cut gives a completion from ANY solution; inconsistency, an empty cut or a cut forced monochromatic in every solution excludes completion.

## Parent checks and exact gap

Main checked the endpoint count, degree-2 residual and alternating-colour parametrization, the two-path colour complementarity, 3n−4 counting, the component-toggle sign (−1)^(l_j−1), the e-parity of both covers, the cycle-cover Hamiltonicity cut criterion and the F2 Fredholm alternative. These are universal written arguments; no selected partial array, graph, cut or executable check was used.

These are conditional completion criteria for an arbitrary n−2-row partial system; no nine-row input at n=11 is supplied, and no argument forces a negative certificate for every input. T2(11) existence/nonexistence, support classification and novelty remain open. Later selected-graph/real-weight episodes, L1, the global parent source pause, N4 UNKNOWN historical child exit unestablished and auxiliary214 STOP persist. Formal/kernel, executable, human and independent-model CLI review not performed.

