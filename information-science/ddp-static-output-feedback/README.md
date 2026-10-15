# Disturbance decoupling by static output feedback

**Book:** 静态输出反馈下的干扰解耦, Chen Benmei (陈本美), *10000 Selected Problems in Sciences: Information Science*, Science Press, 2011, printed pp. **631-632**, PDF pp. **652-653**. [Authoritative images](sources/book/).

**Status as of 2026-10-14 (America/Los_Angeles): PARTIALLY-SOLVED, evidence-limited. The original general synthesis question is not solved by this project.**

The important status correction is that **rational-input per-instance algebraic decision was already available before the book**: Chen et al. (2000), printed p. **1722**, explicitly describes QEPCAD for the residual non-invertible case and Groebner bases plus QEPCAD for **both** variants. Its equation **(A.7)** already uses finite Markov parameters. We reproduce that route, rather than claim to have solved a new open problem. A September 2026 preprint establishes unrestricted SOF stabilization as strongly NP-hard; a direct reduction transfers that barrier to internally stable DDP. **Neither decidability nor hardness is a full solution to the book's intended scientific synthesis problem.**

The literature audit did not establish a general structural-synthesis resolution beyond such implicit algebraic descriptions. This is not a proof that no such publication exists. Full sources, limitations, and unresolved retrievals are in [references.md](sources/references.md).

**Continuation result:** for **exactly two control inputs and two measured outputs (m=p=2)**, arbitrary state order and arbitrary remaining channel/feedthrough dimensions, we now give a complete **unstabilized** synthesis: plant-derived linear equations followed by classification of **one real quadric**, returning every gain with explicit parameter domains. This is an elementary corollary of classical Grassmannian/determinantal-assignment machinery, **likely routine and not novelty-certified**. It is additional to the old unknown-V test, but **not a full book resolution**. The general stable selection problem remains. See [Section 7](#7-continuation-complete-unstabilized-synthesis-for-mp2).

## 1. Exact problem and quantifiers

For arbitrary fixed, finite-dimensional real matrices of compatible sizes, with D11=0,

\[
\dot x=Ax+Bu+Ew,\qquad y=C_1x+D_1w,\qquad
z=C_2x+D_2u+D_{22}w,
\]

find **one real constant matrix K** with u=Ky such that, for zero initial state, the rational transfer matrix

\[
(C_2+D_2KC_1)(sI-A-BKC_1)^{-1}(E+BKD_1)
+D_{22}+D_2KD_1\equiv0.
\]

The internally stable variant additionally requires **every eigenvalue of A+BKC1 to have strictly negative real part**, including modes hidden from the transfer matrix. Approximate attenuation, cancellation at finitely many frequencies, dynamic compensation, state feedback, discrete time, and behavioral interconnection with a different controller class do not substitute for this question.

The two plant channels are Sigma_P=(A,B,C2,D2) and Sigma_Q=(A,E,C1,D1). The printed book line defining Sigma_Q appears to use **B**, an apparent typo: equation (1), the dimensions, and Chen et al. (2000), p.1717, use **E**. Both staged images were read before transcribing this statement. We adopt the book's D11=0 model, without claiming that every nonzero-D11 algebraic loop can be ignored.

### What would count as fully solved here?

A full scientific resolution would supply a constructive, independently checked characterization/synthesis procedure for **all** book plants, retaining all direct-feedthrough terms, and address **both** stability variants; it would specify how admissible controllers are obtained and how infeasibility is certified. A result merely quantifying over an unknown K or V, restating polynomial feasibility, enumerating small examples, or proving a complexity barrier is partial evidence, not that deliverable.

There is an unavoidable interpretation issue: the book does not impose a polynomial-time requirement or formally specify the allowable form of a structural characterization. We therefore do **not** manufacture a polynomial-time conjecture. The concrete missing deliverable in this attack is a plant-invariant, constructive selection/parameterization of the admissible subspaces and gains, beyond the already-known QE restatement. For stable DDP, selecting a Hurwitz gain from those families is a further essential step.

The mathematical identities below hold for arbitrary real coefficients. **Effective exact algorithm and bit-complexity claims are restricted to explicitly encoded rational matrices**; arbitrary real numbers with no finite representation are not algorithm inputs.

## 2. Verified SOTA and boundaries

| Result | Hypotheses / actual scope | Primary source and verification |
|---|---|---|
| Linear-equation characterization of all gains in invertible-channel classes | Sigma_P left invertible or Sigma_Q right invertible; extension when iterative reduced systems become invertible | [Chen et al., 2000](https://doi.org/10.1016/S0005-1098(00)00090-X), Corollaries 5-6, Theorems 4 and 7. Full [paper](sources/papers/chen-2000.pdf) fetched. |
| Exact finite-step algebraic decision for the remaining general case | Real feasibility of polynomial constraints; includes both DDPCM and DDPCMS, not an efficient geometric characterization | Same paper, **p.1722** and Appendix A **(A.7)**. Directly verified. This is decisive prior art against a novelty claim for our algorithm. |
| Static-feedback subspace conditions for uncertain switched plants | No book-style feedthrough; mode-dependent gains. Fixed B or C across vertices gives sufficient conditions; both fixed gives an N&S condition | [Otsuka, Conte, Perdon, 2015](https://doi.org/10.17654/FJDSJun2015_099_124), Lemma 2.7, Theorem 3.2, Corollary 3.3. Full primary paper checked. |
| Behavioral DDP characterization for nonregular DAEs | K1 x+K2 u=0 may not solve for u; different controller/trajectory notion | [Berger, 2017](https://doi.org/10.1016/j.automatica.2017.01.012). Full author preprint checked; **not** a solution for u=Ky. |
| Minimal-actuator output-feedback DDP in coupled oscillator networks | Linearization around stable synchronization, specified network structure | [Lebon, Lindberg, Altafini, 2026](https://arxiv.org/abs/2604.14977v2). Primary abstract checked; not a general arbitrary-plant result. |
| BMI/DC performance optimization preserving DD | **State feedback**, precomputed V, feasible initialization, local stationary-point scope | [Ma and Li, 2026](https://arxiv.org/abs/2603.20438v3), Sections III/V. Full text scope checked; not general static measurement-feedback feasibility. |
| Strong NP-hardness of unrestricted SOF stabilization | Continuous time, even one measured output, unrestricted real gain; integer data | [Ahmadi et al., 2026](https://arxiv.org/abs/2609.20636v2), Theorem 1. Full primary text fetched. **Recent preprint; source-relative lower bound**, not an independent replay of its proof. |
| Older hardness result | Gain intervals, simultaneous or decentralized restrictions | [Blondel and Tsitsiklis, 1997](https://www.mit.edu/~jnt/Papers/J067-97-vb-contr.pdf), pp.2119-2120. Full text checked; **not** unrestricted SOF hardness. |
| Exact real-algebraic algorithms and complexity | Rational polynomial equalities/inequalities, including strict inequalities | [Basu, 2014](https://arxiv.org/abs/1409.1534v1), Theorem 2.4 and Section 2.2. Full primary survey checked. |

The Hamano-Furuta, Schumacher (C,A,B)-pair, Otsuka 2000 and van der Woude generic-structured-system leads are documented separately with explicit **[UNVERIFIED full theorem text]** where only metadata or secondary attribution was accessible. We do not silently promote generic almost-all results, dynamic compensators, or state-feedback results into exact decisions for every book plant.

## 3. Attack and established results

Full derivations: [work/characterization.md](work/characterization.md).

Write M=A+BKC1, G=E+BKD1, F=C2+D2KC1 and J=D22+D2KD1.

1. **Finite exact criterion — Certification / Reproduction, not Discovery.**
   \[
   T(s)\equiv0\iff J=0,\quad FM^jG=0\quad(0\le j<n).
   \]
   Cayley-Hamilton proves sufficiency; expansion at infinity proves necessity. No controllability, observability or invertibility assumption is needed. This is already used in Chen 2000.

2. **Both variants in existential real algebra — Certification.** Introduce X0=G, X_(j+1)=M X_j, F X_j=0. The stable variant adds symmetric P, lower-triangular L, P=LL^T, positive diagonal of L, and M^T P+PM=-I. This gives degree-two, polynomial-size encodings: **mp+n²q** variables without stability and **mp+n²q+n(n+1)** with stability. Consequently both belong to exists-R and are decidable by known exact real-algebraic procedures. A conservative CAD bound is (sd)^(2^O(v)) arithmetic operations, with a separate coarse doubly exponential bit bound in total dense input length. This is not a new scientific solution or a claim of practical scalability.

3. **All feedthrough terms for a fixed V — Certification.** Let T span V and ker N=V. Define
   \[
   H=\begin{bmatrix}NB\\D_2\end{bmatrix},\quad
   R=[C_1T\ D_1],\quad
   Q=\begin{bmatrix}NAT&NE\\C_2T&D_{22}\end{bmatrix}.
   \]
   A single compatible gain exists exactly when **HKR=-Q** is solvable, equivalently **ker R subset ker Q** and **im Q subset im H**. The resulting gains form an affine space obtained by solving this linear system. This jointly enforces disturbance containment, invariance, output annihilation and feedthrough cancellation. Separate tests with different gains can be false positives. **The unresolved step is finding the appropriate V in general**, not solving this fixed-V linear equation.

4. **Correct invariance lemma and a failed lattice route — Certification.** A fixed V has a static output-feedback invariance friend iff AV subset V+im B and A(V intersect ker C1) subset V. This is only an invariance theorem, not the full DDP criterion. In the explicit three-state example of manuscript Section 7, span(e1) and span(e2) separately have friends, but their sum does not. Thus the candidate family inside a prescribed output kernel can lack a greatest element. This blocks the naive supremal-subspace iteration; it does not rule out every structural approach.

5. **Stable-case hardness transfer — Certification of reduction; source-relative inherited theorem.** Set E=C2=D1=D2=D22=0 in any SOF stabilization instance. Transfer decoupling then holds for every K, while internal stability is exactly the original SOF task. The 2026 strong NP-hardness result therefore transfers. The construction provides **no** hardness for DDP without stability and does not imply that concise characterizations are impossible.

6. **Noninvertible two-branch example — finite Certification.** One tested three-state plant has m=p=2, q=r=1, so neither original channel can have the required left/right inverse. For K=[[a,b],[c,d]], its exact constraints reduce to b=0 and (1+a)(1+d)=0; internal stability additionally requires c<2. The stored symbolic equations and a gain witness are in `verification.json`, case `noninvertible-two-branches`. This tests the full algorithm outside the **original** invertible-channel classes, but does not assert that the plant escapes every possible Chen reduced-system class.

**First-pass novelty status:** no new general theorem, priority, AI advantage, or full scientific resolution was claimed. The useful outcome was an independently reviewed exact reference formulation, corrected prior-art/status boundary, and explicit identification of the unsuccessful geometric shortcut. The continuation below adds a complete restricted synthesis corollary and sharper obstruction examples, without claiming publication novelty.

## 4. Reproducible verification

[Exact output and witnesses](evidence/verification.json), [initial timeout retained](evidence/initial-verification-timeout.json).

- **6,561 exhaustive scalar plants**, all eight scalar coefficients in {-1,0,1}; two variant decisions per plant, compared with an independent analytic union-of-affine-root-sets oracle and the two possible scalar subspaces.
- **2,583** admit DDP; **997** admit internally stable DDP. These counts refer only to this finite coefficient box.
- **32 deterministic random small plants** and **7 adversarial plants**: Markov recursion versus independently constructed adjugate/determinant transfer numerators. A nonlinear-real XOR check is UNSAT for every pair, so the equivalence is checked for **all real gains** on each fixed plant, not just sampled gains.
- **256 fixed-subspace checks**: two rank conditions versus the original four linear gain constraints, including V=0 and V=R^n.
- Stability checks use exact Hurwitz determinants and Lyapunov equations. One alternate Lyapunov search (`random-12`) timed out at 30 seconds; retry with mathematically redundant Hurwitz inequalities completed exactly. It is labeled **joint-certificate evidence**, not an independent stability decision for that case. The initial failed run remains preserved; timeout was never interpreted as infeasibility.
- Seven named examples additionally exercise the degree-two lifted encoding. Negative controls detect omission of the last Markov parameter, omission of direct feedthrough, hidden unstable modes, strict-stability boundary, incompatible common gains, and real-versus-complex feasibility.
- No floating-point decision, gain grid as a universal feasibility test, machine-checked proof kernel, independent solver audit, or worst-case runtime experiment is claimed. Both algebraic encodings use the same Z3 backend; the independent scalar oracle and matrix constructions address modeling errors, not every possible solver defect.

Observed environment: **Python 3.12.12**, SymPy **1.14.0**, Z3 **4.16.0**, mpmath **1.3.0**. `uv venv` selected the available Python 3.12 interpreter; no Python-3.14-only behavior is assumed. The corrected full run completed in **48.136 seconds**. This is a run record, not a speed comparison.

```sh
# From /Users/jinleic/repos/aifours/information-science/ddp-static-output-feedback
# Rebuild environment if absent; do not overwrite an existing environment:
uv venv --python 3.12 /Users/jinleic/jinleic-workspace/scratch/ai4s-ddp-static-output-feedback/venv
uv pip install --python /Users/jinleic/jinleic-workspace/scratch/ai4s-ddp-static-output-feedback/venv/bin/python -r work/requirements.txt
/Users/jinleic/jinleic-workspace/scratch/ai4s-ddp-static-output-feedback/venv/bin/python work/verify.py
```

`work/ddp_exact.py` exposes rational `Plant`, Markov/direct/lifted encodings, `decide`, and fixed-subspace tests. With no timeout, `decide` submits exact QF_NRA; a configured timeout yields an explicit error, never a false UNSAT. Saved `evidence/*.smt2` are replayable individual queries. Solver witnesses use exact SMT-LIB numerals/root expressions; a gain entry absent from the expression set is unconstrained, not an approximate missing value.

## 5. Independent hostile referee

**Codex gpt-6.1-sol, reasoning effort max**, read-only, reviewed the central manuscript independently. Verdict: **correct-with-fixes**, with no mathematical counterexample to the seven central claims. Its two corrections were applied: separate arithmetic from bit complexity; fix theorem numbering and distinguish our reduction from the external hardness theorem. See [prompt](evidence/codex-referee-prompt.md), [reply](evidence/codex-referee-reply.md), [reviewed snapshot](evidence/characterization-reviewed.md), and [resolution](evidence/referee-resolution.md).

The referee did not audit all source proofs or execute the verification suite. The completed 2000 full-paper comparison, obtained during the review, strengthens the explicit non-novelty conclusion rather than changing a theorem. No broader independent-model web audit was requested or counted.

## 6. First-pass blocker and next actions (superseded in the m=p=2 unstabilized class)

**Blocker:** the joint existence/search over disturbance-containing, output-null subspaces V that admit one common K, with no guaranteed greatest candidate, and—when required—the Hurwitz restriction on the compatible gain families. The current two-rank test is conditional on V; the global lifted encoding simply delegates that nonconvex choice to known real algebra. This does not close the original synthesis question.

1. **Resolve the intended structural deliverable against the exact prior art**, especially Chen 2000's p.1722 distinction between finite computation and interpretable conditions, before labeling any next theorem a solution. Fetch the remaining original generic/invariant-pair papers if a proposed theorem depends on them. The book does not authorize replacing this with a polynomial-time requirement.
2. **Seek a genuinely additional structural selection principle**, e.g. a finite plant-derived family of admissible subspaces with a completeness proof that retains all D terms; reject approaches relying on closure under sums without proof. The current lattice example is an immediate falsification test. No such principle is established here.
3. **If studying complexity instead, state it as a different partial target.** The stable variant has a source-relative strong NP-hardness lower bound and both variants lie in exists-R; the present work gives no matching classification for the unstabilized variant. More small random plants cannot establish that classification.

**Stop decision:** the attempted general algebraic route has no novelty headroom, and further brute-force small-instance computation cannot supply the missing structural selection theorem. No process remains running, no large computational campaign was launched, and no full-solution claim is made.

## 7. Continuation: complete unstabilized synthesis for m=p=2

Full proof: [work/continuation-structural.md](work/continuation-structural.md). Implementation: [work/grassmannian.py](work/grassmannian.py). Separate evidence: [evidence/continuation/](evidence/continuation/).

### What advanced

1. **Plant-derived graph geometry, all port counts.** Use the maximal minors of `Q(K)=[I_p;K]`, with top minor normalized to 1. A bordered Cauchy-Binet construction expresses **every full-feedthrough transfer numerator and the entire state characteristic polynomial linearly in these minors**. The proof covers every finite real K, singular K, nonminimal plants and noninvertible channels. No unknown state subspace V remains. For general m,p this is a **classical exact reformulation**, not a new solution to decomposable-point selection.
2. **Closed synthesis for m=p=2, without stability.** There are six minors `(1,b,d,-a,-c,t)` and exactly one relation `t=ad-bc`. Linear elimination of the plant equations leaves a single quadratic equation in at most five real parameters. Rational congruence diagonalization, completing squares and an inertia/sign classification handle every case, including null-linear directions, singular forms, inconsistent affine sections and zero-dimensional solutions. All gains are recovered by one polynomial chart or two square-root charts with explicit nonnegative domains. The implementation uses **no QE/nonlinear solver** for this synthesis; its independent negative checks may use the existing exact backend.
3. **A genuine residual noninvertible curve.** The two-state plant in proof (13) has **all** gains `K(a)=[[a,-2a^2],[0,-a]]`, and stable gains exactly `-1<a<1`. Its **only** admissible state subspace is `span([a,1]^T)`. Thus no finite list of fixed V's, nor finite union of affine gain families, can cover all gains even of this one plant. The proof explicitly matches Chen (7), (11), (15)-(21), (29): the reduction preserves both states and the dual is a coordinate-swapped copy. This does not rule out finite nonlinear charts or finding a single witness.
4. **Exact nonlinear infeasibility certificate.** A four-state plant has a nonempty lifted linear section, but its remaining graph relation is `a^2+1=0`. It has no real gain, while `a=i` gives an exact complex gain. Dropping decomposability or accepting complex solutions would be false positives.
5. **Strict internal stability retained, not solved generally.** The graph map returns the full characteristic polynomial; strict Hurwitz determinants characterize the stable subset without discarding hidden modes. Appending the fully disconnected hidden mode specified in the proof at `h=0` or `h=1` leaves zero transfer but destroys internal stability. Selecting stable members of arbitrary gain families remains a nonlinear obstruction, including for m=p=2 at arbitrary order.

**Elementary affine corollary:** if **min(m,p)=1** (one control input or one measured output), the normalized maximal minors of `[I_p;K]` are exactly 1 and signed entries of K, so there are **no Plucker relations**. The full unstabilized DDP gain set is therefore an affine subspace, possibly empty, explicitly obtained from `L delta=0` and the normalization by rational linear algebra, for every state order and arbitrary remaining feedthrough/channel dimensions. See Corollary A1 in the proof. Novelty is unclear; this is an elementary classical-framework corollary. Stable synthesis still requires strict Hurwitz selection over that affine family; the one-measurement case includes the source-relative strongly NP-hard SOF stabilization problem already cited above.

### Prior work and independent review

Chen 2000 p.1722 already supplies general algebraic decision. Gorla-Rosenthal's equations (14)-(15) and **Karcanias-Leventides 2016, Sections 2 and 7**, establish the linear-plus-Grassmannian framework. The latter full accepted manuscript was retrieved after the referee identified the omitted comparison; its nonlinear optimization iteration is not a universal exact infeasibility certificate. The closed m=p=2 result here is an **elementary framework corollary, likely routine**, not a new general method. [Primary-source comparison](sources/references.md#continuation-controller-graph-geometry).

**Claude Opus 5.5 / max**, the other-vendor CLI selected by the current registry, independently hand-checked the complete supplied mathematics with no tools or further delegation. It conditionally accepted the restricted corollary and both exact examples, while rejecting any full-book/new-general-method interpretation. Substantive corrections were applied: the hidden-mode append statement now specifies all necessary disconnections; ambiguous “two-port” wording is replaced by m=p=2; graph-map indexing and arithmetic scope are explicit; the Chen reduction is derived with source equation numbers; and novelty is downgraded after the primary-source comparison. The expanded postreview Chen source-map derivation was not independently rereviewed. See [review disposition](evidence/continuation/referee-resolution.json), [exact invocation](evidence/continuation/claude-review-receipt.json), [input snapshot](evidence/continuation/claude-review-prompt.txt), and [raw output](evidence/continuation/claude-review-output.json).

### Checks actually run

One bounded decisive run completed **PASS in 2.176 s**:

- **5 fixed symbolic-gain fixtures**, including dense nonzero feedthrough, rectangular gain dimensions, the continuum family and real-infeasible plant: determinant-minor maps versus independently constructed adjugate numerators and full characteristic polynomials, as identities for all gains.
- **12 exact quadratic-classification boundary cases**, plus complete all-gain and unique-gain synthesis cases with affine dimensions 5 and 0.
- The existing no-greatest-subspace example was checked first: **true, true, false** for the two lines and their sum.
- Exact gain witnesses, explicit real infeasibility, strict stability endpoints and appended hidden modes **-1, 0, +1**.
- Separately, the parent replayed Theorem A with an independent exact `Fraction` implementation on **32 rational plant/gain/frequency instances across eight port shapes**, including rectangular gains and all feedthrough terms: full characteristic and numerator identities, plus inverse-chart signs, passed. This is finite independent evidence, not a universal proof: [parent receipt](../evidence/information-science-push-20261014/ddp-plucker-identity.json).

No old random/exhaustive sweep, large campaign, numerical tolerance decision, kernel-checked proof or general stable-synthesis success is claimed. The reviewer did not run code or independently read the sources. The verifier pins the prerevision mathematical snapshot; [the disposition](evidence/continuation/referee-resolution.json) separately binds the corrected text and explains that no implementation changed afterward.

```sh
# From information-science/ddp-static-output-feedback; reuse the existing environment.
/Users/jinleic/jinleic-workspace/scratch/ai4s-ddp-static-output-feedback/venv/bin/python work/verify_continuation.py
```

The library entry point `synthesize_two_port(plant)` is specifically restricted to **m=p=2** and returns complete gain charts, an exact witness, or a linear/inertia infeasibility certificate. Its name does not denote all generalized “two-port” plants. `coefficient_maps(plant)` supports arbitrary m,p but does not claim closed general selection.

**Remaining blocker / stop decision:** for m,p>=2 other than m=p=2, selecting real points satisfying several Plucker relations remains; for stable synthesis, strict Hurwitz-region nonemptiness remains even in the affine or one-quadric classes. The established determinant framework and more small-plant trials cannot by themselves remove these obligations. Continue only with a genuinely additional real-selection/stability theorem, not another encoding or sweep. **Original-resolution verdict: PARTIAL, not NEW full solution; only the pre-existing algebraic-decision component is SOLVED-BY-PRIOR-WORK.**
