# P-type ILC with arbitrary bounded initial errors

**Book problem:** 相对阶不小于 1 的 P 型迭代学习控制系统 — Sun Mingxuan, *10000 Selected Problems in Sciences: Information Science*, Science Press (2011), **book pp. 712–715 / PDF pp. 733–736**.

**Status: OPEN — evidence-limited, with certified partial results; not fully solved in this attempt.**

**Status date:** 2026-10-14, America/Los_Angeles. The inspected literature establishes substantial progress with D/PD-type, adaptive, initial-state-learning, fractional, discrete-time, and prescribed-tail formulations. It does not furnish a verified solution of the full P-type question under the quantifiers below. This is **not a claim that no such paper exists**: several recent primary texts remain inaccessible, explicitly including a 2026 high-order/MIMO paper. No novelty claim is made.

The continuation strengthens the negative result from one constant-gain law to **every stationary, constant-coefficient, finite-dimensional linear P-local error learner**, for every integer relative degree. This includes fixed forgetting, momentum and finite-history modifications, but not time/iteration-varying, nonlinear or anticipatory learners. A separate compact-inverse theorem identifies a sharp input-reconstruction stability boundary without misrepresenting it as output impossibility. The earlier finite-dimensional full-state positive benchmark and its evidence are preserved. **The broader original design problem is not solved.**

## 1. Exact book statement and faithful formalization

The four authoritative page images are under [`sources/book/`](sources/book/). They were read directly, not inferred from the garbled PDF text layer. The book's continuous-time repetitive system is

\[
\dot x_i(t)=f(x_i(t),t)+B(x_i(t),t)u_i(t)+\eta_i(t),\qquad
 y_i(t)=g(x_i(t),t)+\xi_i(t),
\]

\[
 u_{i+1}(t)=u_i(t)+L e_i(t),\qquad e_i(t)=y_d(t)-y_i(t),
 \quad t\in[0,T],\quad i=0,1,\ldots .
\]

Here `x_i∈R^n`, `u_i∈R^p`, `y_i∈R^m`, and `L∈R^{p×m}`. The book calls the input dimension `r`; we use `q` for relative degree to avoid ambiguity. There is no direct input-output feedthrough. Initial conditions are uncontrolled. In particular,

\[
u_i(0)=u_0(0)+L\sum_{j=0}^{i-1}e_j(0).
\]

The entry asks how to make P-type ILC **robustly convergent under arbitrary bounded initial conditions**, after explaining why accumulating initial errors compromise the simple law. Its preceding fixed-initial-error, exact-tracking-on-a-prespecified-interval result concerns **D-type** learning.

### Plant, uncertainty, and norm

A precise ordinary-ODE reading assumes sufficient smoothness, local Lipschitz continuity in state, forward existence over the finite trial, a feasible nominal reference `(x_d,u_d,y_d)`, and an appropriate uniformly full-row-rank decoupling matrix. These are explicit feasibility conditions, not claims that the book stated each one.

For a SISO output let `D_f h=∂_t h+∂_x h f`. Nominal relative degree `q>=1` means

\[
\partial_x(D_f^j g)B=0\;(0\le j<q-1),\qquad
 \partial_x(D_f^{q-1}g)B\ne0.
\]

For MIMO plants use a constant vector relative degree and the associated full-row-rank decoupling matrix with a bounded right inverse. At degree one it is `g_x B`, or `CB` in the linear case. At degree two or higher `g_x B=0`; a degree-one condition involving `||I-CBL||<1` cannot simply be reused.

The uncertainty model is

\[
\sup_i\|x_i(0)-x_d(0)\|_\infty\le\epsilon_0,\quad
\sup_i\|\eta_i\|_\infty\le\epsilon_\eta,\quad
\sup_i\|\xi_i\|_\infty\le\epsilon_\xi.
\]

Trial dependence is arbitrary: bounded does **not** mean fixed, convergent, zero mean, independent, or averaging to zero. The present theorems take disturbances continuous within a trial. The broader bounded-measurable formulation uses Carathéodory solutions and essential-sup norms and is not silently substituted for the continuous one.

The requested robustness property is bounded error over all trials and

\[
\limsup_{i\to\infty}\|e_i\|_\infty
 \le c_0\epsilon_0+c_\eta\epsilon_\eta+c_\xi\epsilon_\xi,
\]

with constants independent of the initial-error/disturbance sequence and trial index, and **zero tracking error as iteration tends to infinity when all bounds are zero**. A fixed weighted norm `||e||λ=sup exp(-λt)|e(t)|` is equivalent on `[0,T]`; changing to it does not remove divergence. The physical-output error differs from the measured error by at most `εξ`.

A nonzero output error at `t=0` cannot be removed by a strictly proper controller during that same trial. Accordingly, exact tracking despite persistent nonzero initial errors can at most be an additional **tail-interval** objective; it is not full-interval zero tracking. The whole-interval robustness bound above properly allows an initial-error floor.

### What counts as fully solved

A full solution must resolve the original P-type design question, not merely one implementation. It would need a precisely specified faithful P-type controller, a complete independently checked proof covering its stated general nonlinear class and **both degree one and higher relative degrees**, arbitrary bounded uncontrolled trial starts and disturbances, the whole-interval robustness property, nominal zero-error convergence, and a reproduction/verification package. Alternatively, an impossibility result would have to cover the genuinely admissible design class, not just the single displayed constant-gain law.

Controller-class boundaries are explicit:

* **P0:** exactly `u_{i+1}(t)=u_i(t)+L e_i(t)` with constant `L`.
* **Potential P-type modifications:** pointwise/time-varying gains, forgetting, dead zones, finite histories, initial-error corrections, or specifically declared filters/anticipation. The continuation rules out only the stationary constant-coefficient linear finite-memory subclass, not every modification.
* **Not silently allowed:** differentiating measured error, using an exact inverse disguised as proportional learning, controlling an initial state described as uncontrolled, or replacing the plant by a discrete-time problem.
* **The positive benchmark here:** nonlocal integral processing of error values plus known full-state feedback, with a finite-dimensional realizable target. This is a disclosed relaxation, not a general model-light, output-only P-type solution.

## 2. Current status and assumption-aware SOTA

Full citations, primary links, source snapshots, and access limitations are in [`sources/references.md`](sources/references.md). “Verified” below distinguishes an inspected full text from an author/publisher abstract; neither automatically means its entire proof was independently certified.

| Development | Verified result / hypotheses | Why it does not close this target | Primary source and verification |
|---|---|---|---|
| Initial rectifying action, Li–Chow–Ho–Zhang (2009 baseline) | D-type, right-invertible/estimable `B` on an initial interval; claimed tail residual and zero tail error for exact `B` | Uses error derivatives and state information; not P0 or whole-interval exact tracking. The proof also makes an auxiliary-system extension that is not imported here | [10.1049/iet-cta:20070486](https://www.ee.cityu.edu.hk/~twschow/pubs/papers/50.pdf), **full text** |
| 2-D/averaged PD approach, Meng–Jia–Du (2015) | Publisher-supplied mirrored abstract reports two averaged PD algorithms, one rectified, with Roesser-system analysis | Derivative and averaging assumptions matter; 2-D analysis is not itself a P-type controller. Full hypotheses **[UNVERIFIED]** | [10.1080/00207721.2014.924603](https://doi.org/10.1080/00207721.2014.924603), DOI verified; publisher text blocked |
| Fractional P-type with learned initialization, Liu–Li (2017) | Caputo order `0<α<1`; an explicit initial-state update is required | Changes both plant class and uncontrolled-initial-state assumption. Printed equation (6) has a free-time initialization issue; its theorem is not imported | [10.1186/s13660-017-1302-6](https://pmc.ncbi.nlm.nih.gov/articles/PMC5285440/), **full text** |
| Later Sun error-trajectory/dead-zone work (2018) | Neural adaptive ILC; desired error trajectory starts at the actual error; neighborhood tracking and boundedness | Adaptive/error-trajectory design, not the simple P law; approximation residual is a separate bound | [10.1109/TNNLS.2017.2698507](https://pubmed.ncbi.nlm.nih.gov/28534792/), **primary abstract** |
| Continuous vector relative degree, Wei–Li (2021) | Moving-average **D-type** correction; tail bound proportional to random initial shifts; exact tail tracking for fixed shifts | Derivative controller and tail interval, not a general P-type answer | [10.1002/rnc.5300](https://doi.org/10.1002/rnc.5300), **publisher abstract** |
| High-order nonlinear random shifts, Li et al. (2022) | Adaptive, order-dependent rectification; bounded signals and exact tracking on a preset interval | Adaptive/tail-tracking result; full noisy-output/general P-type theorem not established by the abstract | [10.1016/j.isatra.2022.04.028](https://pubmed.ncbi.nlm.nih.gov/35570151/), **primary abstract** |
| Initial-shift survey (2023) | Separates fixed/arbitrary shifts, PID/2-D methods, time-decaying boundary layers, adaptive attractors, and initial-state learning | Its broad introduction cannot erase the controller-class and interval restrictions in its detailed sections | [10.1016/j.heliyon.2023.e22492](https://pmc.ncbi.nlm.nih.gov/articles/PMC10686873/), **full text** |
| Sun barrier-function learning (2023) | Saturated/barrier adaptive learning; Section IV-A explicitly assumes `x_k(0)=x_d(0)` | Matched initial states; “fractional barrier” is not a fractional plant or arbitrary-shift solution | [arXiv:2306.06646v1](https://arxiv.org/html/2306.06646), **full text, preprint** |
| Initialized fractional systems (2024) | Initialization-shift-dependent robust bounds; noise/nonlinearity considered; initialization learning for perfect tracking | Fractional memory and learned initialization differ from the target | [10.3390/fractalfract8030168](https://doi.org/10.3390/fractalfract8030168), **publisher abstract** |
| Random starts / varying reference and length (2025) | Bounded modified error; zero error when initial state and reference are fixed | Explicitly discrete-time; not a continuous Volterra theorem | [10.1007/s10846-025-02256-x](https://link.springer.com/article/10.1007/s10846-025-02256-x), **publisher abstract** |
| Robust high-degree nonaffine adaptive learning (2026) | Bounded disturbance neighborhood and disturbance-free exact tracking claimed for parameterized, globally Lipschitz discrete systems | Adaptive implicit controller; known bounded initial values; different time model | [arXiv:2602.00968v1](https://arxiv.org/html/2602.00968v1), **full text, preprint** |

**Unresolved primary-source leads:** the 2020 high-order paper [10.1109/ACCESS.2019.2962743](https://doi.org/10.1109/ACCESS.2019.2962743), Sun's 2021 initial-error paper [10.1109/ACCESS.2021.3073458](https://doi.org/10.1109/ACCESS.2021.3073458), the 2024 multi-phase paper [10.1016/j.matcom.2023.09.019](https://doi.org/10.1016/j.matcom.2023.09.019), and the 2026 MIMO/high-order paper [10.1016/j.amc.2026.130028](https://doi.org/10.1016/j.amc.2026.130028) have verified bibliographic records but unverified primary theorem coverage here. The last encountered a CAPTCHA even in a real browser; see [`evidence/publisher-2026-access.txt`](evidence/publisher-2026-access.txt). They are not counted as solutions or dismissed as irrelevant without their hypotheses.

**Decision:** do not mark SOLVED-BY-PRIOR-WORK, and do not promote a failed literature lookup into proof of openness. “OPEN” is this target's conservative, evidence-limited unresolved status. The successful adaptive/prescribed-tail results are real progress under different specifications, not evidence that initial-state difficulties are wholly untouched.

## 3. Attack and analytic results

Complete statements and proofs: [`work/theorems.md`](work/theorems.md).

### A. Volterra obstruction — Certification, scoped

For a strictly proper linear plant, `(Gv)(t)=∫_0^t K(t,s)v(s)ds`. Iterated triangular integration gives `||(GL)^n|| <= (MT)^n/n!`, hence `r(GL)=0` and

\[
\sigma(I-GL)=\{1\}.
\]

Thus the pure-P iteration cannot be a **strict Banach contraction** in the sup norm, any fixed `λ`-norm, or any equivalent norm. This remains true on compatible errors vanishing initially. The nonlinear local derivative has the same obstruction. **Spectral radius one alone does not prove divergence or exclude nongeometric convergence.**

### B. Arbitrarily small bounded starts can yield unbounded output — Certification, partial negative result

For every integer `q>=1`, every nonzero real gain `ell`, and any prescribed `t_*>0`, the `q`-fold integrator with `u_0=y_d=0` and initial state `(a_i,0,...,0)` admits **one** bounded sequence `|a_i|<=ε0` with unbounded `|y_i(t_*)|` across trials.

The impulse generating function is

\[
H_q(z,t)=E_q\!\left(-\frac{\ell t^q z}{1-z}\right),\qquad
E_q(w)=\sum_{k\ge0}\frac{w^k}{(qk)!}.
\]

It cannot extend continuously to `z=1`, so its impulse coefficients are not absolutely summable. The uniform boundedness principle supplies the single infinite bounded initial-error sequence. This is stronger than merely observing `u_i(0)` grow, and does not mistake a different finite worst-case sequence for each horizon for one infinite witness. Zero gain separately fails nominal tracking of a nonzero feasible reference.

This **rules out P0**, not all allowed P-type modifications. It is consistent with the historical warning already in the book; its novelty has not been established.

### C. Explicit robust derivative-free filtered benchmark — Certification, restricted positive result

For a globally defined fully measured normal-form chain, known input gain bounded away from zero, no internal dynamics, and a realizable finite-dimensional desired input, cancel the known last-state drift and write `v_i=φ^T θ_i`, `ψ=J^q φ`, `W=∫ψψ^T`. Then

\[
\theta_{i+1}=\theta_i+\gamma W^{-1}\int_0^T\psi(t)e_i(t)dt,
\qquad 0<\gamma\le1,
\]

uses **error values, not error derivatives**. Its bound is

\[
\|e_i\|_\infty\le(1-\gamma)^i
 \|\psi^T(\theta_d-\theta_0)\|_\infty+(1+\kappa)\delta,
\]

\[
\delta=\epsilon_0\sum_{j=1}^q\frac{T^{j-1}}{(j-1)!}
 +\epsilon_\eta\sum_{j=1}^q\frac{T^j}{j!}+\epsilon_\xi,
\quad
\kappa=\max_t\int_0^T|\psi(t)^TW^{-1}\psi(s)|ds.
\]

Nominal error decays geometrically, and all signals are bounded under the stated global assumptions. The proof covers all `q`, including one and two. **Nonlocal filtering, exact model/state information, and target realizability are essential disclosed restrictions**. If the target lies outside the chosen span, an approximation-residual term remains; no exact-tracking claim is made then. This is a sanity benchmark based on elementary finite-dimensional learning, not a claimed novel full solution.

### D. Every rational finite-memory P-local learner faces the same obstruction — scoped structural theorem

Full proof: [`work/continuation-theorems.md`](work/continuation-theorems.md), Theorem D. The controller class is

\[
u_i(t)=\sum_{j<i}c_{i-1-j}e_j(t),\qquad
C(z)=\sum_{k\ge0}c_kz^k\ \text{real rational and analytic at zero}.
\]

The learner has zero initial memory, constant coefficients across time and trials, and no reference feedforward. It is output-error-only and pointwise in physical time. This covers **all** such fixed finite-dimensional linear memory filters, not just a list of tested gains. For every `q>=1`, nominal zero-error convergence even for the feasible reference `t^q/q!` is incompatible with robustness to arbitrary bounded uncontrolled starts.

The reason is structural: nominal exactness forces `K(z)=zC(z)` to have a pole at `z=1`; the initial-shift response

\[
H_q(z,t)=E_q(-t^qK(z)),\qquad E_q(w)=\sum_{k\ge0}w^k/(qk)!,
\]

then fails continuous extension to the closed unit disk. Its impulse coefficients are not absolutely summable. The uniform boundedness principle supplies **one bounded infinite initial-error sequence** with unbounded output at any prescribed positive time. The proof treats every pole order and relative degree, including the delicate positive-residue simple-pole degree-one case. It also supplies genuinely nonlinear coordinate witnesses without state cancellation by the controller.

Fixed forgetting is analyzed positively as well: `u_{i+1}=rho u_i+ell e_i`, `|rho|<1`, has an explicit full-interval bound for **arbitrary persistent** additive disturbances, but its nominal residual is exactly `(I+[ell/(1-rho)]J^q)^(-1)y_d`, nonzero for any nonzero target. The theorem shows that no other filter in this same stationary finite-dimensional class can remove that tradeoff.

**Excluded from this theorem:** gains depending on time or trial index, nonlinear dead zones/saturation/rectification, nonlocal or anticipatory error processing, general matrix-valued MIMO filter classification, and model/reference feedforward. It is a broader-class impossibility, **not** a universal impossibility for the book's entire admissible design space.

### E. A sharp compact-inverse information boundary, not an output no-go

Theorem E in the same file proves that no sequence of arbitrary reconstruction maps can both satisfy `||R_n(f)||∞<=M||f||∞` with one finite M and achieve `J^q R_n(J^q u)->J^q u` for every continuous input u. Terminal ramps of width h have unit input norm and output norm `h^q/(q+1)!`. A weak-star compactness argument turns consistent uniformly bounded reconstruction into an impossible bounded inverse.

On a restricted input class U, exact inverse stability is equivalent to `||u-v||∞<=M||J^q(u-v)||∞` for all u,v in U. With noise radius delta, pairs whose outputs differ by at most `2 delta` are indistinguishable and force worst-case input error at least half their input separation. This necessity/sufficiency concerns information on feasible data; it does not make exact inversion an admissible P law. **The original property only bounds output error**, so Theorem E alone cannot settle it.

### F. An honest initial-rectified P design succeeds for initial errors, but fails arbitrary noise

The parent's explicit candidate was analyzed rather than dismissed: for the degree-one integrator, take `theta(t)=max(1-t/h,0)` and

\[
u_{i+1}(t)=u_i(t)+\ell[e_i(t)-\theta(t)e_i(0)],\qquad \ell>0.
\]

Full proofs: [`work/rectification-boundary.md`](work/rectification-boundary.md). **Theorem F1** proves, for arbitrary bounded uncontrolled starts but **no process or measurement noise**, a full-interval bound

\[
\|e_i\|_\infty\le\|(I-\ell J)^i y_d\|_\infty+
(1+\ell S)\epsilon_0,\quad
S=\sum_{k\ge0}\|(I-\ell J)^kJ(1-\theta)\|_\infty<\infty.
\]

The nominal term tends to zero for **every feasible continuous input**, with no fixed target basis. A Laguerre–Bessel integral proves a uniform summable `k^(-5/4)` estimate for the rectified forcing, including `t=0`. The controller uses only error values and initial-error subtraction, not derivatives, inversion, state feedback or controlled resets. A nonlinear coordinate version with the **same integrator input-output map** is covered, not general nonlinear dynamics. Fixed starts leave the residual ramp `-theta a` on `[0,h)` and give zero tail error on `[h,T]`. This is **output convergence only**: no uniform input boundedness/convergence is claimed, and the actual worst-case robustness gain necessarily diverges as the layer width h tends to zero.

**Theorem F2 identifies the decisive limitation:** for every continuous theta, every nonzero constant gain and every `q>=1`, this initial-output-subtraction law admits a single bounded continuous measurement-noise sequence producing unbounded physical output, even with zero starts and all noise traces vanishing on a common initial interval. Then `e_i(0)=0`, so the rectifier is inactive; smooth delayed-step approximants recover the nonsummable pure-P impulse response. Thus F1 is a real output-only positive result beyond the earlier full-state finite-basis benchmark, but **cannot be promoted to the original arbitrary-noise/all-degree solution**.

**Theorem F3**, supplied by the independent referee and integrated with its proof, separately shows that the degree-one rectifier also fails arbitrary bounded continuous **process noise**. Its kernel-norm sums diverge by Tonelli and Theorem B. Equivalently, measurement-noise witnesses can be uniformly Lipschitz at degree one; merely adding equicontinuity does not rescue the design. A stronger restriction `xi_i=J^2 g_i`, `sup||g_i||<=M`, does yield an explicit output bound with an M-dependent term, while `J(L∞)` noise can still fail. This is a necessary-versus-sufficient regularity distinction, not a claimed sharp threshold or a solution under arbitrary bounded noise.




## 4. Verification and simulations

Protocol: [`work/verification_protocol.md`](work/verification_protocol.md). Numerical records are **Empirical evidence**, not proofs of infinite convergence. Analytic claims were checked by the independent referee and finite identities by exact rational arithmetic.

### Exact and high-precision checks

* Independent polynomial-integration recursion agrees exactly with the combinatorial impulse formula for `q=1,...,5`, trials `0,...,10`.
* Rational finite worst-case witnesses for `q=1,2`, horizons `8,32,128`, preserve exact numerator/denominator and initial signs in [`evidence/exact-certificates.json`](evidence/exact-certificates.json).
* With `ε0=0.05`, `ell=t_*=1`, horizon 128, exact outputs are approximately **0.3691802371** (`q=1`) and **1.4171343999** (`q=2`): amplification factors **7.38360** and **28.34269**.
* Five 80-digit generating-function checks agree to below `1e-65`. This is a numerical identity check, not a certified error bound for the infinite theorem.
* The degree-one absolute impulse sums at horizons 100, 1,000, 10,000, 100,000 are **6.83848, 12.74266, 23.07261, 41.51062**. Their numerical growth illustrates, but does not establish, the analytic nonsummability.

### Nonlinear random-initial/error trials

The physical plants are

* Degree one: `dot x=0.3 sin(x)+u+η`, `y=x+ξ`.
* Degree two: `dot x1=x2+η1`, `dot x2=0.3 sin(x1)+0.2 sin(x2)+u+η2`, `y=x1+ξ`.

For each, 200 trials on `[0,1]`, seeds `20261014+q`, bounded random initial components, smooth bounded random-phase disturbances, `ε0=0.02`, `εη=0.01`, `εξ=0.005`. P0 uses `ell=1`. The filtered benchmark uses `γ=0.7`, one basis `ψ=t^q`, target `y_d=t^q`, and exact state-feedback cancellation. It therefore has **more model/state information**; no matched-information superiority or optimality claim is made.

Fine-grid results (800 steps; 400-step results also retained):

| Plant and controller | Max sup error over last 50 trials | Proved asymptotic bound for filtered design | Max physical input over all 200 trials |
|---|---:|---:|---:|
| Degree 1, P0 | 0.0749623 | Not guaranteed | 1.54550 |
| Degree 1, filtered | 0.0390532 | 0.0875 | 1.02834 |
| Degree 2, P0 | 1.37653 | Not guaranteed | 83.8778 |
| Degree 2, filtered | 0.0571674 | 0.1600 | 2.09343 |

Half-amplitude filtered disturbances halve the last-50 maxima to **0.0195266** and **0.0285837**. With zero uncertainty the final errors are about **6.0e-15** and **1.2e-14**, numerical zero rather than literal real-number zero. Every sampled filtered error passed the stated finite-iteration bound with `1e-5` discretization allowance. The independent analytic-integral versus physical-RK4 discrepancy is at most **7.86e-13** across all main runs. Coarse/fine filtered error-metric differences are at most **5.48e-6**; the largest P0 difference is **1.49e-4**.

The random degree-one P0 run does **not** visibly diverge in 200 trials. That does not contradict a worst-case arbitrary-sequence theorem. The degree-two large inputs and worsening tracking are finite observations, not an infinity claim.

Full results: [`evidence/verification.json`](evidence/verification.json), [`evidence/simulation-trials.csv`](evidence/simulation-trials.csv).

### Initial-error-only nonlinear divergence-mechanism diagnostic

To isolate initial errors from nominal-target and process-noise effects, a second cheap diagnostic uses the already certified horizon-128 sign sequences, `y_d=0`, and **no process or measurement noise**. It uses nonlinear coordinate versions of the integrators: `g(x)=x+0.2 sin x`, with `g'>=0.8`; degree one has `dot x=u/g'(x)`, and degree two has `dot x1=x2/g'(x1), dot x2=u`, both with output `g(x1)`. Their output equations are exactly `dot y=u` and `ddot y=u`, without cancellation in the P0 controller.

At trial 128 and time one, 800-step physical simulations give:

| Relative degree | P0 output | Exact finite witness | Filtered output | Filtered bound for this zero-target diagnostic |
|---|---:|---:|---:|---:|
| 1 | 0.3691805904 | 0.3691802371 | 0.1209500464 | 0.125 |
| 2 | 1.4171232178 | 1.4171343999 | 0.1333331807 | 0.1333333333 |

Initial output magnitude is only `0.05`; actual initial physical-state values are recorded, with conservative bound `0.0625`. This directly displays initial-error amplification into later-time output on nonlinear plants. It still certifies only a **finite witness**; Theorem B, not the plot-free diagnostic, supplies the infinite statement. The filtered comparator uses the known transformed basis, and remains a different controller class.

Artifacts: [`evidence/nonlinear-witness.json`](evidence/nonlinear-witness.json), [`evidence/nonlinear-witness-trials.csv`](evidence/nonlinear-witness-trials.csv). The diagnostic was added after the main suite, using its already fixed exact witnesses; it was not an adaptive parameter search, and the original results are retained.

### Continuation: finite-memory adversaries and nonlinear counterchecks

The separate bounded continuation suite ran once after its formulas and fixed cases were specified. It passed in **6.24 seconds**, single-threaded, without modifying earlier certificates. Evidence: [`evidence/continuation/verification.json`](evidence/continuation/verification.json).

* **35 exact rational identities:** seven fixed rational learners, degrees `q=1,...,5`, horizons through 12; direct polynomial plant/difference-equation recursion agrees with an independently formed generating series.
* **27 exact finite adversaries:** momentum, double accumulation, and two-error memory; degrees 1–3; horizons 8, 24, 48. At horizon 48, momentum amplifies the initial bound by **26.8098, 23.8359, 11.2166** respectively. Double accumulation gives **52169.4, 2376.58, 140.053**. These are finite sign witnesses, not substitutes for the infinite-sequence proof.
* The same certificates also give **measurement-noise-only** witnesses with zero starts: measured output has the identical transfer and physical output differs by the bounded current noise. This tests persistent deterministic trial noise, not only random trials.
* **12 nonlinear physical counterchecks:** momentum at degree 1–3, 400/800 time steps, both initial-shift-only and measurement-noise-only channels. The degree-one nonlinear endpoint for a `0.05` initial bound is about **0.805709** at trial 24, versus exact **0.805713**; the largest 800-step discrepancy is **4.45e-6**. No state feedback cancellation is used.
* Fixed-forgetting controls at degrees 1–3 reproduce the exact nonzero nominal residual with largest uniform discrepancy **2.46e-7**. Persistent deterministic, biased-in-blocks initial shifts and alternating spatially varying measurement noise obey the proved (conservative) full-interval bounds.
* 100-digit complex-path checks exercise pole orders 1–3 and degrees 1,2,3,5, including the degree-one tangential limit. Exact terminal-ramp checks exercise the compact-inverse obstruction at degrees 1–5. These finite checks do not certify universal analytic limits.
* The separately requested rectifier assay passed once in **2.84 seconds**: **104 exact identities**, six positive checks, and 12 negative checks. The initial-only nonlinear adversary at trial 48 agrees with its exact endpoint within **2.03e-7** on 1024 steps. For `y_d=sin(t)+t^2`, no finite basis is used by the controller; the nominal sup error falls from **1.84147** to **0.0139181** by trial 256. This is an illustration of, not a proof of, convergence.
* Continuous-noise traces zero on `[0,1/4]` defeat the rectifier's initial-value channel. Exact delayed-ramp coefficients and nonlinear degree-1/2/3 runs agree within **2.21e-7** at trial 24; measured endpoints for noise bound `0.05` are **0.197361, 0.227246, 0.126251**. Theorem F2, not these finite magnitudes, establishes infinite-sequence failure. Evidence: [`evidence/continuation/rectification-verification.json`](evidence/continuation/rectification-verification.json).


## 5. Independent hostile review

[`evidence/codex-referee.md`](evidence/codex-referee.md) is the preserved independent `gpt-6.1-sol`, max-effort, read-only review. Its verdicts were **A correct with fixes; B correct; C correct with fixes**. It independently reconstructed the key generating function and checked the all-degree boundary argument and single-sequence quantifier.

All objections were addressed: continuous gains for `C`-space operators, explicit complexification/input-space derivative, explicit zero-gain example and time quantifier, integrable signal regularity, and globally defined coefficients/common compact containment for bounded physical inputs. Detailed resolutions: [`evidence/referee-resolution.md`](evidence/referee-resolution.md). The reviewer did not certify novelty or all cited papers. No Lean/kernel proof or human peer review was performed.

The continuation uses the **other vendor**, `claude-opus-5-5`, max effort, through the authorized CLI with embedded mathematical context, no tools and no further delegation. The [rectification referee](evidence/continuation/rectification-review/claude-referee.txt) judged **F1 and F2 correct as stated** and independently rechecked the required pure-P theorem. Its substantive scope findings were applied: explicit unit-bounded ramps; residual on all of `[0,h)`; no input-stability claim; nonuniform layer-width tradeoff; no general nonlinear inference; and a separate proof for process noise rather than inferring it from measurement noise. The reviewer supplied F3 and the stronger-regularity sufficient bound; the latter includes the current-noise term when reporting measured error. Command, proof snapshot hash, reported model, raw output and final review are preserved under `evidence/continuation/rectification-review/`.

The separate [focused rational-memory referee](evidence/continuation/rational-focused-review/claude-referee.txt), also `claude-opus-5-5`/max, returned **ACCEPT for both D and E, no substantive errors**. It checked a self-contained concise version of those proofs, including the interior-pole continuation, every pole-order/relative-degree case, the tangential simple-pole limit and the weak-star argument. Optional clarifications of connectedness, norm lower semicontinuity and injectivity were integrated. The earlier broad attempt timed out after 1800 seconds with no final reply and **is not counted as review**; its evidence is retained in [`claude-referee-timeout.json`](evidence/continuation/claude-referee-timeout.json). The focused successful retry took 329.63 seconds. The review does not certify novelty, the inaccessible papers, or a general nonlinear/MIMO design.


## 6. Outcome, blocker, and ranked next actions

* **Certification:** written analytic Theorems A–E and F1–F2, with the independent review scopes recorded above; F3 and the stronger-noise-regularity observation were supplied by the rectification referee and integrated with complete proofs. Exact rational finite identities and witnesses are separate evidence, not kernel certification.
* **Empirical evidence:** reproducible nonlinear coordinate counterchecks through degree three, deterministic adversarial starts and measurement noise, fixed-forgetting residuals, the initial-rectified positive law, a nominal non-polynomial tracking example, and independent analytic-versus-physical integrations. F3 is an analytic consequence, not a separate numerical process-noise experiment.
* **Reproduction:** primary-source statements and assumptions were inspected; no claim is made to have reproduced another paper's full controller implementation.
* **Discovery / novelty status:** no established discovery or priority claim. The pure-P failure was already a historical concern, and the filtered construction is elementary. Correctness is separated from novelty.

**Exact remaining scientific blocker:** find an output-error-based P-type robust mechanism outside the excluded stationary constant-coefficient linear finite-memory class **and not merely constant-gain initial-output subtraction**, or prove a correspondingly wider impossibility. Any positive result must cover the broader nonlinear class and arbitrary relative degree, arbitrary bounded uncontrolled starts/noise, a full-interval bound and nominal zero-error convergence, without controlled resets, a realizable finite basis, full-state/model cancellation or error differentiation. Theorems D and F2 close the single-law/finite-memory gap and the initial-subtraction/noise gap. Theorem F1 positively handles initial shifts at degree one but does not close arbitrary-noise or higher-degree tracking.

Ranked next actions by decision value:

1. **Resolve primary-source coverage first:** obtain authorized public/institutional full text for the 2026 MIMO/high-order paper and the 2020/2021 high-order/Sun papers. Audit controller equations, arbitrary-vs-fixed starts, norm, disturbance assumptions, and full-vs-tail interval. A decisive already-solved result would change the status; metadata cannot.
2. **Pin a candidate outside Theorems D and F2:** genuinely time/iteration-varying gains, nonlinear disturbance-aware rectification, or disclosed anticipatory/nonlocal filtering. Merely adding fixed forgetting, momentum, constant-coefficient finite history, or initial-output subtraction cannot satisfy the whole specification. Prove the exact arbitrary-disturbance transfer on integrator chains before generalizing.
3. **Only then lift a surviving mechanism to nonlinear/MIMO plants:** retain decoupling rank, uncontrolled starts, and measurable information; establish well-posedness and common domain bounds instead of assuming them.

Further brute-force tuning within Theorem D's excluded class is not justified: the obstruction is analytic, not a failed gain search. The original problem remains active but unresolved outside that class. The continuation makes a concrete structural advance without promoting it to a full original-class design.

## 7. Reproduction and artifact map

From `/Users/jinleic/repos/aifours/information-science/p-type-ilc-initial-error/`:

```sh
uv venv --python 3.14 /Users/jinleic/jinleic-workspace/scratch/ai4s-p-type-ilc-initial-error/venv
uv pip install --python /Users/jinleic/jinleic-workspace/scratch/ai4s-p-type-ilc-initial-error/venv/bin/python -r work/requirements.txt
/Users/jinleic/jinleic-workspace/scratch/ai4s-p-type-ilc-initial-error/venv/bin/python work/verify.py
/Users/jinleic/jinleic-workspace/scratch/ai4s-p-type-ilc-initial-error/venv/bin/python work/witness_simulation.py
```

The main suite ran with Python **3.14.3**, NumPy **2.4.3**, and mpmath **1.4.1**, one numerical thread; approximately 16.5 seconds for the main suite and 4.6 seconds for the extra diagnostic. The environment is outside the synced target. No heavyweight datasets/builds, Git changes, author contact, or external submissions were used. All launched computations ended; the owned browser tab was released.

The preserved referee can optionally be regenerated with `python3 work/run_referee.py` using the workspace's configured authorized delegate. This is a model invocation, not required for offline numerical reproduction. Prompt, final reply, CLI log, and metadata are saved under `evidence/`.

Key files:

* [`work/theorems.md`](work/theorems.md): full mathematical statements and proofs.
* [`sources/references.md`](sources/references.md): primary-source verification ledger and limitations.
* [`work/verify.py`](work/verify.py), [`work/exact_checks.py`](work/exact_checks.py), [`work/witness_simulation.py`](work/witness_simulation.py): reproducible implementation.
* [`evidence/verification.json`](evidence/verification.json), [`evidence/exact-certificates.json`](evidence/exact-certificates.json), [`evidence/nonlinear-witness.json`](evidence/nonlinear-witness.json): numerical/rational evidence.
* [`evidence/codex-referee.md`](evidence/codex-referee.md), [`evidence/referee-resolution.md`](evidence/referee-resolution.md): independent review and fixes.

Continuation-only reproduction, using the already existing environment:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-p-type-ilc-initial-error/venv/bin/python work/verify_continuation.py
/Users/jinleic/jinleic-workspace/scratch/ai4s-p-type-ilc-initial-error/venv/bin/python work/verify_rectification.py
```

The continuation preserves its own [`work/continuation-theorems.md`](work/continuation-theorems.md), [`work/verify_continuation.py`](work/verify_continuation.py), and [`evidence/continuation/`](evidence/continuation/). Its authorized public-source retries and the metadata-only Elsevier XML success are recorded in [`evidence/continuation/source-access.json`](evidence/continuation/source-access.json); primary theorem coverage remains unresolved, so novelty is not certified.
