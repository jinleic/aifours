# 大种群随机多自主体系统的自适应动态博弈

Status date: **2026-10-14 (PT)**. Book-level outcome: **PARTIAL — no full resolution established**. FRONTIER state: **PROOF-OBLIGATION** for the broad unknown-local-and-global-matrix problem; **NOVELTY-UNCLEAR** for the conditional result below.

**Bottom line.** Li–Zhang (2013) answers all four questions for a scalar model with **known local dynamics**, not the printed unknown-A/unknown-B model. This package supplies a complete classical matrix-valued theorem with **all three matrices unknown**, but only for an explicit robustly stable, fully actuated, homogeneous subclass with sparse prearranged common/private excitation. It must not be counted as a full solution of the book chapter.

## Source

* 《10000个科学难题·信息科学卷》, Science Press, 2011; article by **李韬**, 中国科学院数学与系统科学研究院.
* Book pp.635–637 = PDF pp.656–658. Source PDF: `/Users/jinleic/Documents/中文pdf/10000个科学难题·信息科学卷(10000个科学难题信息科学编委会).pdf`.
* SHA256: `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db` (recomputed in the render receipt).
* Formula/author/reference images read: [635](sources/book-0656.png), [636](sources/book-0657.png), [637](sources/book-0658.png), newly rendered at 150 dpi. [Render receipt](evidence/book-render-command.json).
* The malformed PDF text layer was used only to locate prose; the equations and the quotation below were checked against the page image.

## Problem

### Verbatim Chinese questions and model

The displayed equations on p.636 are

\[
 x_i(t+1)=Ax_i(t)+Bu_i(t)+\Lambda\frac1N\sum_{j=1}^{N}x_j(t)+\omega_i(t),
 \qquad i=1,2,\ldots,N,
\]
\[
 J_i=\limsup_{n\to\infty}\frac1n\sum_{t=0}^{n}
 \left\|x_i(t+1)-\Phi\!\left(t,\frac1N\sum_{j=1}^{N}x_j(t)\right)\right\|^2.
\]

> 式中，\(x_i\) 是第 \(i\) 个自主体的状态；\(u_i\) 是第 \(i\) 个自主体的控制输入；\(\omega_i\) 是随机噪声；\(A、B、\Lambda\) 是未知参数矩阵，其中，\(A\) 和 \(B\) 是局部参数，\(\Lambda\) 是全局参数；\(N^{-1}\sum_{j=1}^{N}x_j(t)\) 是种群平均状态。注意，这里其他个体的状态对于第 \(i\) 个自主体是未知的，不能用于 \(u_i\) 的设计。

> 式中，\(\Phi\) 是某种可测函数。在这类自适应博弈中，实际上存在两个估计过程：一个是对未知种群平均状态的估计过程；另一个是对未知参数的辨识过程。由于自主体的动力学方程中存在未知参数（全局参数 \(\Lambda\)）和未知状态（种群平均状态）的乘积，如果采用传统的辨识方法，回归向量中将出现种群平均状态，而我们知道种群平均状态不能用来构造每个个体的辨识器。如果采用种群平均状态的估计代替种群平均状态构造辨识器，将导致两个估计过程的非线性耦合，再加上分散式信息架构，使得这类自适应博弈系统与传统的单个体自适应控制[10]有着本质的区别。对这类自适应博弈系统，有许多基本问题有待研究，包括分散估计器、分散辨识器和分布式控制器的设计问题及闭环系统分析问题。具体地，能否保证闭环系统的稳定性，如果可以，能否保证闭环系统自主体的状态上界与个体数 \(N\) 无关；能否保证对种群平均状态的估计在某种度量意义下的一致性，能否给出误差收敛速度；能否保证分散辨识的一致性，能否给出误差收敛速度；能否保证分散式控制律在 Nash 均衡意义下的渐近最优性并给出不同个体的指标随个体数增加收敛到最优的速度。这些问题在现有的适应控制和大系统分散控制的框架下都没有现成的答案。

Line breaks and mathematical typesetting are normalized; Chinese wording is retained.

**Translation.** A,B are unknown local parameter matrices and Lambda is an unknown global parameter. Other agents' states are unavailable to agent i and cannot be used in its control. The two learning processes estimate the unobserved population mean and identify the unknown parameters. Since an unknown parameter multiplies the unknown mean, replacing the mean in a regressor by its estimate couples the learning processes nonlinearly. The questions are: (Q1) can closed-loop stability, with a bound independent of N, be guaranteed; (Q2) can the mean estimate be consistent in an appropriate metric, with a rate; (Q3) can decentralized parameter identification be consistent, with a rate; (Q4) can decentralized control be asymptotically optimal in the Nash sense, with a rate of convergence of costs to the optimum as N grows?

### Formal readings and all modelling choices

The article gives a research program, not one fully quantified conjecture. It specifies neither stabilizability, noise laws, excitation, control dimensions, meaning of stability, order of limits, nor a precise Nash null-set convention. These cannot be supplied silently.

| Reading | Explicit interpretation and justification | What it does NOT license |
|---|---|---|
| R0: unrestricted literal class | Arbitrary matrices, unspecified noise, any measurable Phi; ask for one universal affirmative answer. The words alone do not exclude B=0 or unbounded targets. | This reading is false, by proof.md C1–C5. Those elementary counterexamples expose missing assumptions; they do not solve the intended adaptive-control research program. |
| R1: known-parameter comparison | Fix the same tracking cost, stable mean coupling, suitable noise and bounded/finite-energy reference, but give local dynamics and coupling to controllers. This isolates the mean-estimation issue and is the pre-book baseline. | Not adaptive identification. P1 already supplies this type of theorem; a new oracle calculation cannot be counted as solving Q3. |
| R2: the exact 2013 restricted adaptive model | Scalar state/input, known measurable local g_i, known unit input gain, unknown scalar \(|\alpha|<1\), P3 A1–A4, Lipschitz Phi for Nash, A5 for identification. Appropriate because it repeats the book's four questions and cost almost verbatim. | Unknown A and B, matrix Lambda, fixed-N exact parameter consistency, or arbitrary measurable targets. |
| R3: matrix subclass proved here | Common unknown d-by-d A,B,Lambda; N>=2; \(\|A\|\le a,\|B-I\|\le b<1,\|\Lambda\|\le\ell\), \(2a/(1-b)+\ell<1\); bounded independent iid zero-mean noise and bounded initial states; known bounded f-orbit and uniformly Lipschitz Phi; sparse common/private pilot randomness. | General stabilizable or underactuated plants, heterogeneous A_i/B_i, unbounded-noise pointwise bounds, or a strict prohibition on common design randomness. These are substantive restrictions, not innocuous normalizations. |
| R4: broad conventional adaptive reading | Add meaningful stabilizability, regularity, finite-noise moments and identifiability assumptions, but seek unknown local AND global matrices under strictly local state observations, beyond R3. This is the unresolved scientific design objective. | There is no canonical “minimal assumption” theorem stated in the book. This package does not certify the entire class open, nor a sharp necessary-and-sufficient characterization. |

Specific conventions for R3 are fixed in [proof.md §1](proof.md): square fully actuated controls are a restriction; matrices are common because the display has A,B rather than A_i,B_i (the heterogeneous interpretation remains separately unresolved); current local states are observed exactly; extra randomness is explicit and never contains others' state data; f is deterministic and known from Phi, not inferred from the unknown matrices. Noise is shifted from omega_i(t) to w_i(t+1) only to express nonanticipation. Stability is proved in a stronger pointwise bounded sense because noise is bounded. The cost remains sample-path limsup, **not** replaced by expected cost. Nash comparison uses policywise almost-sure inequalities / the essential infimum, not an unjustified common null set over every possible policy.

### What “consistency” means

1. **Fixed N, current-mean recovery:** generally impossible with persistent private noise. C5 gives a conditional variance lower bound `(N-1)sigma^2/N^2` even in a decoupled scalar model. A deterministic proxy need not converge pointwise in time to the true mean.
2. **Population-limit mean consistency:** the relevant metric is first the infinite-time average squared error, then N grows. P3 bounds it by `sigma^2/[N(1-alpha^2)]`; R3 obtains exactly `tr(S)/N`. Root-mean-square error is order N^-1/2, not N^-1.
3. **Fixed-N parameter consistency:** not ruled out by hidden mean fluctuations. R3's two distinct pilot instruments yield unbiased finite-N Markov moments and consistently identify all matrices for N>=2. P3's Theorem 3 instead bounds the fixed-N limsup error by a population-dependent floor; that theorem does not assert its floor is unavoidable.
4. **Joint limits:** R3's all-agent epoch bound contains `sqrt(log(N k^2/delta)/m_k)`. It supports a chosen diagonal only when this ratio tends to zero. A fixed-N asymptotic statement does not automatically give uniformity over every N(t).
5. **Calibration times:** common probes have zero time density but need not have small population mean at the individual calibration times. R3 makes no uniform-in-time pointwise mean-consistency claim and does not exchange the T and N limits.

## Status as of 2026-10-14

| Book question | Prior work: exact coverage | Result supplied here | Verdict for broader all-unknown class |
|---|---|---|---|
| Q1 stability and N-independent bound | SOLVED-BY-PRIOR-WORK on R2: almost-sure uniform long-run-L2 stability, P3 Theorem 2(ii). | T1: explicit deterministic bound X on every state for all times/N, on R3 only. | **PARTIAL / OPEN-BLOCKED beyond stated assumptions**; R0 universally false. |
| Q2 mean consistency and rate | SOLVED-BY-PRIOR-WORK on R2: long-run squared error O(1/N), P3 Theorem 2(i). | T3: exact long-run squared error tr(S)/N; RMS O(N^-1/2). | **PARTIAL**; fixed-N exact-current-mean reading is false in general. |
| Q3 decentralized identification and rate | SOLVED-BY-PRIOR-WORK on R2 with A5: limsup squared coupling error O(1/N), P3 Theorem 3; A/B are known there. | T2: all unknown matrices consistent for each fixed N>=2, explicit simultaneous concentration; physical-time error O(t^-1/4 sqrt(log log t)) a.s. for fixed N. | **PARTIAL / OPEN-BLOCKED beyond R3**. No verified general joint-unknown result located. |
| Q4 Nash optimality and N rate | SOLVED-BY-PRIOR-WORK on R2 with Lipschitz Phi: cost gap O(1/N), P3 Theorem 2(iii). | T4: epsilon_N <= (ell+L)^2 tr(S)/N on R3, even versus globally informed causal unilateral deviations in the stated random-cost convention. | **PARTIAL / OPEN-BLOCKED beyond R3**; arbitrary targets can conflict with stability. |

Dated search log: [machine-readable queries/access attempts](evidence/search-log.json) and [source-by-source reading notes](sources/references.md). The strongest negative prior-art evidence is P3 p.505 explicitly listing simultaneous unknown local/global parameters as future work. The searches extend beyond that date to 2026, but P6/P7 full-text gaps mean “no full resolution located” is the defensible statement, **not certified openness**.

## State of the art

| Work | Hypotheses / mathematical object | Primary link and read status | Relation to the exact target |
|---|---|---|---|
| Li–Zhang, Automatica 2008 | Vector discrete tracking, known g_i and Lambda, rho(Lambda)<1, martingale noise and target-orbit regularity | [Author PDF](https://lsc.amss.ac.cn/~jif/paper/%5BJ57%5D.pdf); model, construction and main theorems read | Known-parameter Q1/Q2/Q4 baseline; no Q3. |
| Li–Zhang, TAC 2008 | Continuous-time cost-coupled linear systems, known parameter information, compact distribution, stabilizable/detectable, mean-field fixed point | [Author PDF](https://lsc.amss.ac.cn/~jif/paper/%5BJ65%5D.pdf); model/assumptions/main results read | Different dynamics/cost; origin of the stochastic Nash convention, not full solution. |
| Li–Zhang, DGA 2013 | Scalar known g_i and B=1, unknown abs(alpha)<1; A1–A4; Lipschitz Phi for Nash; A5 excitation for identification | [Author PDF](https://lsc.amss.ac.cn/~jif/paper/%5BJ93%5D.pdf); main text and proofs read, decisive formulas image-checked | All four answered on R2; explicitly excludes the main unknown-A/B difficulty. |
| Kizilkale–Caines, TAC 2013 | Continuous-time dynamically uncoupled LQG, unknown local parameters/population distribution, RWLS+dither, observations of other agents for distribution learning | [Author preprint](https://arxiv.org/abs/1210.5493); model/information/assumptions/main theorem read | Unknown distribution is not unknown Lambda multiplying hidden mean; information and objective differ. |
| Nourian et al., TAC 2012 | Continuous-time cost-coupled leader/follower LQG, unknown finite-class leader reference, observed leader trajectories, identifiability | [Author PDF](https://people.math.carleton.ca/~mhuang/res/MojTac12.pdf); model, estimator, theorem and controller sections read | Adapts the reference model, not unknown local and global dynamical matrices. |
| Chen–Li–Qiao, online 2024 / MCRF 2025 | Sampled-data continuous-time LQG, unknown dynamical parameters, leader/follower aggregation; abstract's limit is sample step ->0 | [Publisher](https://www.aimsciences.org/article/doi/10.3934/mcrf.2024059); abstract/references read, **full text [UNVERIFIED]** after access failures | Sampling alone does not establish equivalence to fixed-step book dynamics/cost. Full coefficient hypotheses not asserted. |
| Liu–Liu, CCC 2022 | Discrete-time cost-coupled LQ, unknown dynamics and population distribution per indexed abstract | [DOI](https://doi.org/10.23919/CCC55666.2022.9901983); metadata verified, **full text [UNVERIFIED]** | Relevant later lead; not certified as either an exact solution or an exclusion based only on title. |

Details, precise prior constants, read limits and other 2014–2026 leads are in [references.md](sources/references.md). No prior-art item is upgraded from a search summary to a verified theorem.

## Results claims table

| ID | Claim and exact scope | FRONTIER label | Novelty / verification |
|---|---|---|---|
| T1–T4 | Complete decentralized matrix theorem for H1–H4, retaining the book dynamics and original cost; all A,B,Lambda unknown | **Certification; PARTIAL** | Classical proof in [proof.md](proof.md); no Lean/kernel or human-specialist certification; novelty unestablished. |
| P3 comparison | The 2013 result settles the known-local scalar subclass but not the displayed joint-unknown problem | **Certification of source scope** | Direct primary model, hypotheses and conclusion read; not a new mathematical result. |
| C1–C7 | Stabilizability/target/noise/identifiability counterexamples; fixed-N mean floor; exact omitted-mean LS pseudotrue coefficient | **Certification; negative scoped results** | Classical calculations in proof.md §9; standard/routine obstructions, no priority claim. |
| E1 | Sparse calibration implementation with unknown A/B/Lambda; state bound and matrix moment algebra controls exercised | **Empirical evidence** | Frozen protocol, deterministic seeds, pinned NumPy; scalar simulation cannot certify a matrix theorem. |
| E2 | Known-parameter oracle 1/N noise/cost scaling, and proxy-LS bias negative control | **Empirical evidence** | Oracle is explicitly not adaptive; independent numerical negative control agrees with its analytical pseudotrue coefficient. |

### Mechanism, without substituting an easier model

The natural f-proxy LS route is not assumed valid: C7 gives an explicit omitted-mean/endogeneity bias. Instead, during sparse calibration agent i knows its own private pilot and a prearranged common pilot. Its lag-two cross moments identify **different matrices**:

\[
 E[x_i(t+2)c(t)^\top]=(A+\Lambda)B,
 \qquad E[x_i(t+2)v_i(t)^\top]=(A+\Lambda/N)B.
\]

Together with `E[x_i(t+1)v_i(t)^T]=B`, these separate A and Lambda for N>=2 without seeing another state. Projection guarantees safety before learning succeeds. Calibration lengths are order sqrt(time), and their cumulative time density tends to zero. Complete proof of the overlapping-sample concentration, matrix inversion, stability, original cost and deviation lower bound is included; no unproved persistent-excitation hypothesis is hidden in the conclusion.

### Empirical evidence (frozen before execution)

[Protocol](work/protocol.json), [code](work/smoke.py), [results](evidence/smoke/smoke.json), [command receipt](evidence/smoke/command.json). One scalar run per N=4,16,64, each with 12 independent replicates and T=262144; no post-result tuning. A=0.12, B=1.05, Lambda=0.25 are all unknown to the adaptive algorithm; bounded noise is +/-0.5; Phi(z)=1+1.1(z-1), f=1. Every simulated state stayed below the proved bound. The 2-by-2 algebra control tests matrix ordering numerically, not the full matrix dynamics.

| N | Full-time adaptive mean MSE | Full-time original adaptive cost | Preselected exploitation-tail mean MSE | Oracle N×mean MSE |
|---:|---:|---:|---:|---:|
| 4 | 0.120565 | 0.324462 | 0.091062 | 0.266361 |
| 16 | 0.046236 | 0.287681 | 0.023235 | 0.266439 |
| 64 | 0.031561 | 0.278221 | 0.013530 | 0.266726 |

The exact oracle normalized limit is 0.2666667. The adaptive finite-time results remain **above** their infinite-time limits; they do not establish the asymptotic N^-1 law. This distinction is intentional: the parameter estimates have only 362 samples in the last calibration window, and calibration occupies 0.00474548 of all controls. For N=64 the A/B/Lambda RMSEs decrease from (0.152616,0.095898,0.313286) at m=16 to (0.061783,0.052162,0.092636) at m=362. This is qualitatively consistent with learning, not a fitted-rate certificate.

The proxy-LS negative control gives `A_hat=0.0801646` versus the exact pseudotrue `0.08`, while true A=0. It exercises why a naïve “regression noise is a martingale” assertion is false. All empirical results, including the finite-time adaptation error, are preserved.

## Independent review dispositions

The other-vendor **Claude Opus 5.5, effort max**, reviewed the complete embedded proof with no tools, safe mode, no Chrome, no session persistence and stdin `/dev/null`. The final event had `subtype:"success"`, `is_error:false`; its mathematical verdict was **`correct`**, with **seven non-blocking wording/precision findings and no mathematical error found**. This is model review, not human peer review or kernel certification.

Evidence: [full parsed findings](evidence/referee-findings.json), [raw response](evidence/referee-raw.json), [command/model/hash receipt](evidence/referee-command.json), [parse-recovery receipt](evidence/referee-parse-recovery.json), [runner](work/run_referee.py). The model completed successfully; the wrapper initially failed to parse a JSON fence preceded by prose. Only parsing was repaired/replayed from the retained successful event—**no model rerun**. The initial failed wrapper receipt is retained rather than silently overwritten.

| Finding | Disposition | Applied resolution |
|---|---|---|
| F1: C7 called a decentralized certainty-equivalence loop an “oracle” | Accepted | Relabelled it as known-parameter decentralized CE; the globally informed oracle is distinguished. |
| F2: unsupported unbounded-noise extension/correlation wording | Accepted | Restricted the claim to the displayed scalar Gaussian example and supplied its ordinary-SLLN justification; no extension of T1–T4 is claimed. |
| F3: loose “stronger than 2013” comparison | Accepted | Removed it from the proof; the source table retains the exact different hypotheses and identification targets. |
| F4: conditional McDiarmid freezing step implicit | Accepted | Stated freezing of the initial state, uniform supported-block sensitivity, and safety of the counterfactual trajectory. |
| F5: joint independence, causality and cross-N coupling implicit | Accepted | Added the product probability space, joint independence and explicit noise-nonanticipating filtration. |
| F6: undefined/colliding notation and unnamed summable failure sequence | Accepted | Defined theta and the generic empirical matrix; separated moment/error/offset/perturbation symbols; specified epoch failure probability k^-2. |
| F7: stabilizability necessity insufficiently scoped | Accepted | Made the necessity explicitly for stability, not every cost-only Nash requirement. |

The referee checked the matrix moment identities, overlapping-sample concentration constants, epoch endpoints, N=2 inverse constants, safe projection, stable convolution, original random cost, explosive-deviation lower bound and counterexamples. The reviewed proof hash and post-editorial-revision hash differ as recorded in the recovery receipt. The seven refinements do not change the theorem constants or algorithm; the revised wording was not independently re-reviewed.

## Book-level verdict

**No full book-level solution is claimed or counted.** The 2013 paper is not an exact all-unknown solution. R0 permits elementary impossibilities. R3 is a substantive positive matrix subclass, but its robust small-gain set, homogeneous full actuation, bounded noise and common-pilot information pattern do not exhaust the chapter's research class. The remaining broad positive theorem has not been proved here, and the literature search has two explicitly unverified full-text comparisons.

The exact mathematical blocker is a safe, locally implementable identification/control argument for unknown local and global dynamics outside a known jointly robustly stable uncertainty family, while the regressor's mean is unobserved. The additional unresolved interpretations are heterogeneous local dynamics, underactuation and no common design excitation. Claiming minimal assumptions or a universally open general theorem would go beyond the evidence.

## Next steps

1. Obtain an authorized readable copy of CCC2022 and the full MCRF2024/2025 paper to close the identified **prior-art comparison**, without treating access failure as openness. No purchase/contact was authorized or made.
2. For mathematical generalization, first replace H1's uniform small-gain bound by an explicit known decentralized stabilizer/robust uncertainty condition, and prove that calibration remains safe. Arbitrary stabilizability alone is not a supplied constructive argument.
3. Independently audit the heterogeneous-local-matrix and strict-no-common-randomness variants before claiming they follow from the two instrumental moments. They do not follow from the present identities.
4. Seek specialist/human review and priority comparison before presenting the sparse-pilot result as novel. A model referee and numerical smoke are not publication or kernel certification.

### Replay

From this directory, with CPython 3.14.3 and `numpy==2.4.3` available:

```sh
python3 -B work/smoke.py --output /Users/jinleic/jinleic-workspace/scratch/ai4s-adaptive-mean-field-game/parent-replay
```

This replays empirical and numerical-algebra evidence only; the classical proof is a document requiring mathematical review. The output option preserves the worker evidence. The separate `work/run_referee.py` makes a model call and is not part of the smoke replay.
