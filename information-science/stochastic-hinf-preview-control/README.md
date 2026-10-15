# Stochastic H∞ preview control (随机系统 H∞ 预演控制)

Book: 《10000个科学难题·信息科学卷》 (Science Press, 2011), pp. 674–676 (PDF pp. 695–697), problem by
张焕水 (Zhang Huanshui) and 王宏霞 (Wang Hongxia). Page images: [`sources/book/`](sources/book/).
Work done 2026-10-14 (PT).

## 1. The problem as printed

The system is

    dx(t) = [A x(t) + B u(t) + C w(t−h)] dt + [A0 x(t) + B0 u(t)] dW(t),    z(t) = D0 x(t) + D1 u(t),

where W is a Brownian motion and h ≥ 0 is the preview length. For a given γ > 0, find a full-information
controller u(t) = F(x(t), w(s) | t−h ≤ s ≤ t) such that

    E‖z‖_{L2[a,b]} / E‖w‖_{L2[a,b−h]} < γ,    with ‖f‖_{L2[a,b]} := (∫_a^b f(t)ᵀf(t) dt)^{1/2}.

Both the finite horizon (a, b bounded) and the infinite horizon (b → ∞) are asked for. The book asks
for necessary and sufficient (N&S) solvability conditions and the controller.

It names three obstacles in the stochastic case:

1. Kalman-filter/LQR duality fails.
2. Non-homogeneous forward–backward stochastic equations are hard to homogenize.
3. The generalized Riccati equation has no Hamiltonian stable-subspace correspondence.

## 2. Formalization, and what "fully solved" means

F1–F8 below describe the **mean-square attempt and its corrected assumptions**, not every result now
in this directory. The [literal-norm continuation](#5a-literal-norm-continuation)
keeps the printed expectation-of-pathwise-norm criterion and separately states
its disturbance and controller information.

Full details are in [`work/theory.md` §0](work/theory.md). Each choice is labelled as an
interpretation (I), a restriction (R) or a substantive replacement (S):

* **F1 (S)**: the norms are mean-square: ‖z‖² = E∫|z|², ‖w‖² = E∫|w|².
  * The printed ratio E[(∫|z|²)^{1/2}] / E[(∫|w|²)^{1/2}] is a different, non-Hilbert, L¹(Ω; L²)
    criterion. **Its general N&S synthesis problem remains unsolved here.**
  * Reasons for the replacement: the book itself (p. 676) ties the problem to a generalized Riccati
    equation, which characterizes the mean-square norm. The proposers' own 2014 paper on this model
    uses E‖z‖²/E‖v‖² < γ² (its eq. (4); full text read).
* **F2 (I)**: disturbances w are square-integrable processes adapted to the Brownian filtration. The
  variant "sup over deterministic w only" is not covered. w = 0 outside the counted window
  [a, b−h].
* **F3 (I)**: x(a) = 0.
* **F4 (I)**: controllers are strongly well-posed nonanticipative path functionals, event-local,
  and square-integrable for every disturbance. Necessity even allows full past Brownian information;
  sufficiency supplies a controller of the book's form.
* **F5 (I)**: "< γ" means induced norm < γ with a uniform margin. Requiring it only per input
  changes the answer at most at the single point γ = γ_opt.
* **F6 (R)**: D1ᵀD1 ⪰ r0 I > 0 uniformly, with bounded data. The book's constant matrices with full
  column rank D1 satisfy this; the singular case D1ᵀD1 ⊁ 0 is not covered.
* **F7 (I)**: the infinite horizon additionally requires internal mean-square stability.
* **F8 (R)**: infinite-horizon mean-square stabilizability and detectability are required
  **after** the feedback substitution in (A1); original-data detectability need not survive that substitution.

**"Fully solved"** means:

* For the finite horizon: an N&S condition, with both directions proved, for the existence of an
  admissible controller with sup ‖z‖/‖w‖ < γ, plus an explicit controller.
* For the infinite horizon: the same, under the standard stabilizability and detectability
  hypotheses.
* For both: independent verification (an independent-model referee and an independent numerical
  representation).

The finite-horizon characterization uses F1–F6; the infinite-horizon argument uses F1–F8 and (A1)–(A3).

## 3. Status verdict (literature, 2026-10-14): **PARTIALLY-SOLVED**

| Evidence (checked 2026-10-14) | What it settles |
|---|---|
| Wang, Zhang, Chen, Yu, J. Harbin Inst. Technol. 46(7):101–106, 2014, doi:10.11918/j.issn.0367-6234.2014.07.017. Full text read. | Continuous-time Itô, **B0 = 0 only**, finite horizon. A **sufficient** condition: if a coupled ODE/PDE system (P, α, β) has a bounded solution, the problem is solvable. No necessity, no infinite horizon, no closed-form kernels. |
| Wang, Fu, Zhang, SIAM J. Control Optim. 58(1):215–242, 2020, doi:10.1137/18M1232942. The [author's submitted manuscript](https://www.eng.newcastle.edu.au/~mf140/home/Papers/SICON_2020.pdf) was retrieved and read during this continuation; the published PDF remains unavailable. | **Discrete-time, finite-horizon, mean-square** disturbance-preview control. Equation (2.1) is a difference equation, (2.4) uses the finite window [0,N], and Theorem 4.3 gives an N&S inertia condition and controller. This time model is now confirmed from the manuscript, not inferred from MSC codes. |
| Crossref, OpenAlex (all 14 citing works of the SIAM paper), the zbMATH API, the arXiv API, and English/Chinese web search | No continuous-time N&S result found. An empty search is not proof of absence. |

## 4. State of the art

| Result | Hypotheses | Source | Verified? |
|---|---|---|---|
| Deterministic H∞ preview control: N&S via ARE or operator methods | A0 = B0 = 0 | Tadmor–Mirkin, IEEE TAC 50(1), 2005; Kojima–Ishijima, IEEE TAC 51(12), 2006; Zhang–Duan–Xie 2005/06 (book refs [6]–[9]) | Cited by the book; primary pages not fetched [UNVERIFIED] |
| Stochastic H∞, no preview (h = 0): generalized Riccati characterization | Mean-square norm | Hinrichsen–Pritchard, SIAM J. Control Optim. 36(5), 1998 | Landing page only [UNVERIFIED content]. Our Theorem 1 contains this case and our code reproduces it (§5) |
| Continuous-time stochastic H∞ preview, sufficient condition | B0 = 0, finite horizon | Wang–Zhang–Chen–Yu 2014 | Full text read. Observation [INFERENCE from its eqs. (4), (21), (31)]: its eq. (31) keeps a γ⁻²PCCᵀP term on (T−h, T]. Under its own model, eq. (4) counts v only on [0, T−h], and v decided at t reaches the plant at t+h, so no maximization over disturbances arises on (T−h, T] and no γ-term should appear there. The discrepancy was noted, not pursued. |
| Discrete-time stochastic H∞ preview, N&S | Discrete time, finite horizon, mean-square norm | Wang–Fu–Zhang 2020 | Author manuscript read: (2.1), (2.4), Theorem 4.3; published version not retrieved |
| Stochastic H∞ *tracking* with *reference* preview | Reference given; preview in an H2 sense (zbMATH review of the 2020 paper) | Gershon et al., IEEE TAC 49(11), 2004; Gershon et al., IJRNC 2004, 2014 | Abstracts only. A different problem |
| Stochastic LQ (not H∞) with input delay / preview | — | Zhang–Xu 2017; Wang–Zhang–Xie 2021; Liu–Lessard–Seiler arXiv:2412.06662 | Abstracts |

Full citations, with what was actually fetched: [`sources/references.md`](sources/references.md).

## 5. What this attempt established

### Theorem 1: finite horizon, N&S

Proof in [`work/theory.md`](work/theory.md) §§1–3.

For symmetric P define:

* R̂ = D1ᵀD1 + B0ᵀPB0, S = B0ᵀPA0 + D1ᵀD0, L = BᵀP + S
* Ã = A − BR̂⁻¹S, Q̃ = A0ᵀPA0 + D0ᵀD0 − SᵀR̂⁻¹S
* H0(P) = [[Ã, −BR̂⁻¹Bᵀ], [−Q̃, −Ãᵀ]]

Here H0 is the Hamiltonian of an LQ problem whose weights carry the Itô corrections. Let Φ(t, s) be
the transition matrix of r ↦ H0(P(r)) over the preview window. The problem is solvable **iff** the
n×n *advanced generalized Riccati equation*

    −Ṗ = AᵀP + PA + A0ᵀPA0 + D0ᵀD0 − LᵀR̂⁻¹L + γ⁻² k kᵀ,   P(b) = 0,
    k(t) = [P(t), −I] Φ(t, t+h) [C; 0]   (k = 0 for t > b−h)

has a solution on [a, b]. It is a backward functional ODE whose right side at t uses P on
[t, t+h].

When it does, P ⪰ 0, and the following controller has exactly the book's form and achieves
sup ‖z‖/‖w‖ < γ:

    u*(t) = −R̂⁻¹ [ L x(t) + Bᵀ ∫_t^{min(t+h,b)} K(t, s) w(s−h) ds ],    K(t, s) = [P(t), −I] Φ(t, s) [C; 0].

The worst-case disturbance is w*(t) = γ⁻²[k(t)ᵀx(t) + ∫ k(t)ᵀΦ11(t, s)C w(s−h) ds]. For every
controller u and disturbance w,

    J(u, w) = E∫|R̂^{1/2}(u − u*)|² − γ²E∫|w − w*|².

Special cases:

* h = 0 gives the classical stochastic H∞ generalized Riccati equation.
* In the deterministic case the equation is a standard Riccati equation of
  H_eff = e^{−H0h} H_γ e^{H0h}.

How the three obstacles are handled:

1. Duality is not used. The conditional means of state and costate solve a *deterministic* Hamiltonian
   system whose coefficients carry the Itô terms through P.
2. The forward–backward system is decoupled by explicit kernels K and M, given by the window
   transition matrix.
3. There is no fixed Hamiltonian. The Hamiltonian over the window is frozen at the true P(s), which
   makes the Riccati equation non-local in time.

Necessity:

* No sign or linearity assumption on the controller is needed.
* The proof first transfers uniform concavity of the lower value to every subinterval, using a
  plant-only shift trick (Lemma 6).
* That gives a uniform bound 0 ⪯ P(t) ⪯ c_* I, so P cannot escape (Lemmas 7–8).

### Theorem 2: infinite horizon, N&S

[`work/theory.md` §5](work/theory.md) assumes F1–F8 and mean-square stabilizability/detectability
of the transformed data in (A1)–(A3). Modulo the cited standard facts, the problem is solvable **iff**

    0 = AᵀP + PA + A0ᵀPA0 + D0ᵀD0 − LᵀR̂⁻¹L + γ⁻²kkᵀ,   k = [P, −I]e^{−H0(P)h}[C; 0]

has a solution P ⪰ 0 that satisfies two conditions:

* (T1) A_P := A − BR̂⁻¹L + γ⁻²(e^{H0h})22ᵀ C kᵀ is Hurwitz. These are the mean dynamics, the
  restriction of e^{−H0h}H_γe^{H0h} to graph(P).
* (T2) under (T1), the well-defined positive renewal map 𝒯_P(Σ)=∫_0^∞ΓσΨ(τ)ΣΨ(τ)ᵀΓσᵀdτ
  has spectral radius below one. It describes second-moment dynamics.

That P equals lim_{T→∞} P_T, is unique, and gives the stationary controller. For h = 0, (T1)–(T2)
reduce to the standard mean-square-stable worst-case loop.

Status: a detailed independently challenged argument, conditional on cited standard facts:
strong SFDE well-posedness/continuous dependence, positive renewal theory, PSD-cone
Perron–Frobenius/Krein–Rutman, and the L²-to-exponential mean-square stability implication.

### Numerical verification

Raw outputs are in [`evidence/numerics.json`](evidence/numerics.json) and the other JSON files in
[`evidence/`](evidence/). The independent check is an Euler discretization with the previewed
disturbances in a shift register (an augmented state of dimension n + Nm), solved by the textbook
discrete-time min-max dynamic programme. It shares only the plant data with the continuous solver.

Examples:

* ex1: scalar plant, A = 1, B = 1, C = 1, A0 = 0.5, B0 = 0.4, z = [x; u].
* ex2: two states, B0 ≠ 0, D1ᵀD0 ≠ 0.
* ex3: as ex2, with two disturbance channels.

Finite horizon [0, 3]: γ* extrapolated to dt → 0 (continuous / discrete):

| Example | h = 0 (classical GRDE in parentheses) | h = 0.5 | h = 1 |
|---|---|---|---|
| ex1 | 1.46459 / 1.46457 (1.46459) | 1.02827 / 1.02824 | 0.76553 / 0.76550 |
| ex2 | 0.94792 / 0.94789 (0.94791) | 0.82233 / 0.82232 | 0.79376 / 0.79375 |
| ex3 | — | 0.94998 / 0.94997 | — |

Relative disagreement is ≤ 3.7·10⁻⁵ everywhere. Below γ*, the escape time of the continuous
equation matches the first failing stage of the discrete game to within 0.01–0.08 (dt = 0.01).

Other checks:

* **The bound flips at γ\*.** The continuous controller u*, designed at 1.002–1.2·γ*, was
  discretized, and its exact discrete closed-loop gain computed by a max-only dynamic programme.
  * The gain is always ≥ the discrete optimum (necessity) and approaches it as the design γ ↓ γ*.
    For ex1 the optimum is 1.02620 and the gain is 1.02634 at 1.002·γ*. For ex2 the optimum is
    0.82601 and the gain is 0.82623.
  * Gain/design ratios are below 1 for every design ≥ 1.01γ*.
  * One case exceeds 1: ex2 at 1.002γ*, ratio 1.0029. There the design margin (0.2%) is smaller
    than the dt = 0.01 discretization error (0.46%).
* **Near-worst-case disturbance (Monte Carlo, 40 000 paths).** The disturbance is an impulse at the
  critical stage followed by the maximizing feedback. Against the controller designed at 1.01γ* it
  gives these ratios:
  * ex1: 1.025 ± 0.011, against an exact 1.0266.
  * ex2: 0.8276 ± 0.0007, against an exact 0.8275.
  * For contrast: white noise gives 0.10 and 0.09; a sine gives 0.67.
* **Lemma identities**
  ([`evidence/identities.json`](evidence/identities.json)):
  * The finite-difference relative error of the kernel equation (K2) is ≤ 3.3·10⁻⁶.
  * The boundary identity (M0) holds to 2·10⁻¹⁰.
  * The saddle-point cost J(u*, w*) from x0, by Monte Carlo, converges to x0ᵀP(0)x0 = 0.80321 at
    first order in dt. The bias is 0.0119, 0.0055 and 0.0020 at dt = 0.005, 0.0025 and 0.00125.
* **Infinite horizon, ex1.**
  * Exact at h = 0, from the closed-form scalar stationary equation with mean-square stability of
    the worst-case loop: γ*_∞ = 1.72152.
  * Brackets for h > 0: γ*_∞(0.5) ∈ [1.31684, 1.31904] and γ*_∞(1) ≤ 1.11687.
    * The upper ends are time-budget-limited estimates: P_T converged within T ≤ 400 at that γ.
      They are not exact thresholds; at h = 0 the same procedure gives 1.72167 against the exact
      1.72152.
    * The lower end is the T = 40 finite-horizon threshold (continuous, dt-converged). It lies
      below γ*_∞ as it must, and the discrete game reproduces it: Richardson gives 1.316842 against
      1.316841, and 1.719835 against 1.719835 at h = 0
      ([`evidence/long_horizon_T40.json`](evidence/long_horizon_T40.json)).
  * Just above the estimates (1.0005×): ρ(𝒯) = 0.90 / 0.89 / 0.82 while A_P stays Hurwitz (max Re
    −0.62 / −0.47 / −0.26). **The infinite-horizon threshold is a second-moment (T2) phenomenon,
    invisible to any Hamiltonian/mean analysis**, which is consistent with the book's third obstacle.
* **Lemma 9 with a nonzero initial window**
  ([`work/check_lemma9.py`](work/check_lemma9.py),
  [`evidence/lemma9_check.json`](evidence/lemma9_check.json)).
  * Setup: ex1, h = 0.5, γ = 1.332, ρ(𝒯) = 0.63; x0 = 1 and committed window v_0 = 1. Euler–Maruyama
    with 200 000 paths at dt = 0.0025 and 100 000 paths at dt = 0.00125.
  * The predicted endpoint ȳ(h) lies in 𝒮 = e^{H0h}·graph(P) to 9·10⁻⁸.
  * The simulated mean of x matches the theory mean (H0-flow, then the A_P-flow inside 𝒮) at
    s = 0.25 … 8; at s = 8 it is 0.00219 / 0.00232 against 0.00224.
  * E x² and E σ² match the renewal-equation prediction within about 0.5–3 Monte Carlo standard
    errors. At s = 4, dt = 0.00125 gives E σ² = 0.322 ± 0.051 against 0.321. The SEs are only
    approximate because the late-time distributions are heavy-tailed.
  * There is no systematic dt trend.
* **Deterministic consistency.**
  * The advanced equation matches the H_eff Riccati equation to 2·10⁻⁷.
  * For ex2 with A0 = B0 = 0, γ*_∞(h) = 1.31998, 1.31997, 1.31986, 1.31963, 1.31937 for
    h = 0, 0.5, 1, 2, 4. It decreases toward the classical non-causal bound 1.31870, computed
    independently by a frequency sweep
    ([`evidence/deterministic_limit.json`](evidence/deterministic_limit.json)).

### Evidence labels

| Claim | Label |
|---|---|
| Theorem 1 (finite-horizon N&S, explicit controller, finite-dimensional reduction) | **Discovery (candidate)**. Correctness rests on a written proof, an independent-model referee (correct-with-fixes; fixes applied) and an independent numerical representation. No human or formal verification. |
| Theorem 2 (infinite-horizon N&S with T1–T2) | **Discovery (candidate)**: a detailed argument conditional on cited standard facts and transformed-data assumptions (A2)–(A3). Codex and the independent Claude continuation review accepted the scoped argument with corrections; no human or formal verification. |
| h = 0 and deterministic reductions | **Reproduction** of known structures (classical GRDE; preview Hamiltonian transport) |
| All numbers in §5 | **Empirical evidence** for the stated examples only |
| Novelty | **NOVELTY-UNCLEAR.** No prior continuous-time N&S result was found. The 2020 author manuscript now confirms a discrete-time finite-horizon result; Chinese-venue coverage and other primary-source retrievals remain incomplete. Priority is not established. |

Word audit: "proved" refers to the arguments in `work/theory.md` as refereed. No result here is
machine-checked. No "first" claim is made.

## 5A. Literal-norm continuation

Full proofs: [`work/literal_continuation.md`](work/literal_continuation.md).
Unlike Theorems 1–2 above, the following results use the **printed norm exactly**.

### Constant-matrix finite-horizon separation (Theorem L2)

For h = 1, output horizon [0,5], counted disturbance horizon [0,4], take

    dx = (-x + u + w(t−1)) dt + 2x dW,    z = (x, 100u),    x(0) = 0.

The control is effective (B = 1), D1ᵀD1 = 10000, and the plant is mean-square
stabilizable. There is no singular-control or uncontrollable-state loophole.

* **Literal problem:** the explicit controller **u = 0** has induced gain
  at most `2 sqrt((e²−1)/2)/(1−e⁻¹) < 6`, uniformly over **all adapted**
  disturbances, not merely the deterministic ones tested in a simulation.
  The bound even allows finite E‖w‖ with infinite E‖w‖².
* **Mean-square substitute:** **every** admissible controller has gain > 14.
  This includes nonlinear controls adapted to the full Brownian **past**,
  all preview pre-action, and the smaller information class printed in the book.
  One deterministic unit pulse, linear superposition of its state response
  with the control response, and a Hilbert-space convolution bound prove this.
* Therefore gamma = 6 is **solvable for the literal problem and impossible
  for the substitute**, for either the deterministic or adapted disturbance
  interpretation. This separates controller existence, not just ratios for
  a single controller/input pair. It disproves any general transfer of
  mean-square **necessity** to the book's finite-horizon norm.

**Control-dependent noise is covered too (Corollary L2b):** replace `2x dW`
by `(2x+u) dW` and take `z=(x,10000u)`. The literal controller u=0 still has
gain <6, whereas every adapted controller's mean-square gain is >17.
This follows from the control-only moment bound
`(E y²)' ≤ 3E y² + 10E u²`, not from sampling. Here B0=1 as well as B=C=1.

The key estimate is conditional stochastic convolution: for a < 0,
`dx = (a x + w(t−h))dt + sigma x dW`, a geometric time-block bound on the
expected L2 norm of the stochastic exponential gives a uniform finite-horizon
mixed-norm bound, even when `2a + sigma² > 0`. Future increments are independent
of each adapted input value. The proof never replaces its denominator by RMS.

For deterministic inputs, a mean-square performance bound always implies the
same literal bound by Jensen, because the input denominator is nonrandom.
That argument does **not** compare the two induced gains over adapted random
inputs. Any conclusion specifically about failure of the old Riccati condition
is conditional on the old mean-square sufficiency theorem; the norm-solvability
separation above is self-contained and does not use that theorem.

### Complete N&S benchmark, explicitly time-gated (Theorem L3)

A separately labelled scalar system accumulates w on [0,1], evolves by
`dx = x dW` on [1,2], accumulates w again on [2,3], then holds its state on [3,4].
Its output is `z = (d(t)x + u, u)`, with d = 1 on [3,4] and zero elsewhere.
This is **time-varying, not the printed constant-matrix general problem**.
It has no state actuation or preview: its synthesis is pointwise output
minimization by time-varying memoryless feedback, not a new dynamic preview law.

For both deterministic and adapted disturbances, its exact optimal literal
gain is **1**, achieved by **u = −d(t)x/2**. Thus strict solvability is exactly
**gamma > 1**. Both directions hold against arbitrary nonlinear controllers.
For comparison, its adapted-input mean-square optimum is `sqrt((1+e)/2)`;
the deterministic-input mean-square optimum is the different expression
`sqrt((e+1+sqrt((e−1)²+4))/4)`. All three are proved explicitly.

### Scope and evidence

These are **finite-horizon partial results**. They do not settle general
constant-matrix literal N&S synthesis or either general infinite-horizon
interpretation. In particular u = 0 in L2 is not internally mean-square stable
on the infinite horizon. No infinite-horizon conclusion is inferred from it.
The new bounded verifier is
[`work/check_literal_continuation.py`](work/check_literal_continuation.py);
it uses exact rational inequalities and independent moment ODE/quadrature
representations, not Monte Carlo. New continuation evidence is kept separately
under [`evidence/literal-continuation-20261014/`](evidence/literal-continuation-20261014/).

The decisive verifier was run once after stabilizing the result and **passed**:
[`verification.json`](evidence/literal-continuation-20261014/verification.json).
Exact rational arithmetic certifies the strict bounds <6, >14 and >17.
Decimal diagnostics are 5.6550107285, 14.8897698250 and 17.6055112251 respectively.
Six independent moment-ODE comparisons have maximum scaled error
5.64×10⁻¹²; 32- and 64-node Gaussian quadrature reproduce the three distinct
gated gains. These numerical comparisons support the identities, not the
universal input/controller quantifiers in the written proofs. No Brownian
Monte Carlo paths were used.

**Independent other-vendor proof review:** two isolated, no-tools Claude
Opus 5.5/max calls reviewed the pinned mathematics only. The L1/L2/L3 review
returned **correct-with-fixes**, with no load-bearing mathematical defect;
the focused B0≠0 corollary review returned **correct**. Minor fixes were
applied: in-text rational certificates, conditional Riccati attribution,
nonanticipative/full-past information, one-plant benchmark scope, and explicit
Itô admissibility plus localization. Original commands, inputs, model identities
and outputs are retained. See
[`review-resolution.json`](evidence/literal-continuation-20261014/review-resolution.json)
for all 17 findings and dispositions. The final exposition/localization edits
were not submitted for an additional model re-review; the verifier's plant,
gain bounds and computations were unchanged.

Novelty is unestablished; no Lean/kernel verification is claimed.

## 6. Independent-model referee (Codex gpt-6.1-sol, max effort)

**Round 1** ([prompt](evidence/codex-referee-prompt.md), [reply](evidence/codex-referee-reply.md)):

* **Theorem 1.** "Correct-with-fixes" under uniform positivity of D1ᵀD1. The referee independently
  re-derived the kernel equations (K2, M0, M1) and the γ-term, all matching, and found no
  information-structure error in the necessity lemmas.
* **Theorem 2.** "Plausible and repairable, not proved".
* **Objections.**
  * One fatal-as-stated: a counterexample with D1(t) → 0 at an interior time.
  * Three minor: circular P ⪰ 0, the martingale integrability step, and disturbance values after
    b − h.
  * Four major: F1 fidelity, a nonlinear comparison controller in Theorem 2, the informal
    input–output bound, and V ⪰ 0 / transversality.
* **Resolution.** All eight were checked by hand and accepted. Each fix and its location is listed
  in [`work/theory.md` §7](work/theory.md).

**Round 2**, on the revised text ([prompt](evidence/codex-referee2-prompt.md),
[reply](evidence/codex-referee2-reply.md)):

* **Objections 1–8.** 1–6 and 8 resolved. 7 partly resolved: the block argument was empty for
  h = 0; it is now fixed with block length 1.
* **Theorem 1.** "Correct under revised F6. No remaining substantive mathematical error found."
* **Theorem 2.** "The main N&S argument now works, modulo legitimate standard facts". Two minor
  corrections were applied: the h = 0 block length, and the renewal forcing for random initial
  windows.
* **Numerics.** "Consistent as approximation evidence; overstated as certification". Two points:
  * The infinite-horizon brackets were time-budget limited. They are now reported as such, with the
    exact h = 0 value.
  * One discretized design at 1.002γ* exceeded its target because of discretization (§5).
* **Lemma 9 with a nonzero initial window**, untested in round 1, now has a direct check (§5,
  addendum).
* Round 3 was not run.

**Independent Claude continuation review:** the completed no-tools `claude-opus-5-5`/max
review returned **correct-with-fixes** for both mean-square theorems, with Theorem 2 conditional
on cited standard facts. The parent added the missing zero-input localization lemma, made
strong event-local admissibility explicit, imposed detectability on the transformed data,
and corrected the terminal-window Hamiltonian qualifier. This does not upgrade the
mean-square substitute into a solution of the printed problem. Findings and parent dispositions:
[`../../evidence/information-science-push-20261014/meansquare-referee-findings.json`](../evidence/information-science-push-20261014/meansquare-referee-findings.json),
[`review-resolution`](../evidence/information-science-push-20261014/meansquare-referee-resolution.json).

## 7. Exact remaining blockers

1. **General literal N&S synthesis, separately for finite and infinite horizons.**
   Theorem L2 now proves that the literal and mean-square solvability thresholds
   can differ even for constant matrices, nonzero control and all adapted inputs.
   Theorem L3 solves one explicitly time-gated benchmark plant exactly, not the general
   book problem. A general result still needs both directions and an actual
   admissible controller; writing a Bellman optimum implicitly is insufficient.
   * The old 17-family Monte Carlo probe remains historical empirical evidence
     in [`evidence/literal_probe.json`](evidence/literal_probe.json).
   * Its inference that the mean-square controller was necessarily sufficient
     for the random-input printed criterion is **withdrawn**: Jensen changes
     both numerator and denominator, and proves no such ratio comparison.
     The new L2 separation refutes necessity, not sufficiency.
   * Deterministic and adapted suprema must remain distinct. Infinite-horizon
     repetition arguments require justified resets/forgetting and controller
     information; they cannot be transferred to arbitrary nonlinear controllers.
2. **Novelty and priority.** The retrieved Wang–Fu–Zhang author manuscript settles its
   discrete-time scope, not priority for a continuous-time result. The published version,
   Chinese-venue coverage, other inaccessible leads and human expert proof review remain outstanding.
3. **Infinite horizon.** The cited standard facts (SFDE continuous dependence, the operator-valued
   positive renewal theorem, Krein–Rutman for the converse of Lemma 9) should be written out in this
   setting.
4. **Variants not covered by the general mean-square theorems.**
   Deterministic-only disturbances; singular D1ᵀD1; output feedback (not asked
   by the book). The scoped literal examples do not remove these general gaps.

## 8. Ranked next actions

1. Seek a literal mixed-norm N&S characterization for a regular constant-matrix
   class, with both deterministic and adapted interpretations explicit. The
   exact finite-horizon separation rules out simply reusing the quadratic game.
2. Independently justify any infinite-horizon bridge: block independence,
   positivity or reset/forgetting, and controller memory are real obligations.
3. Write out the three cited facts for the **mean-square** Theorem 2 (blocker 3);
   this would not by itself settle the literal problem.
4. Extend the primary-source comparison beyond the now-read SIAM 2020 author manuscript
   and seek human expert proof review. External contact requires the owner's authorization.

## 9. Reproduction

The new continuation command starts at the repository root and reuses the existing environment.

```zsh
# new literal continuation; reuse the existing environment, no Monte Carlo
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
  /Users/jinleic/jinleic-workspace/scratch/ai4s-stochastic-hinf-preview-control/venv/bin/python \
  information-science/stochastic-hinf-preview-control/work/check_literal_continuation.py \
  information-science/stochastic-hinf-preview-control/evidence/literal-continuation-20261014/verification.json

```

The historical mean-square commands below instead start in
`information-science/stochastic-hinf-preview-control/`; they are preserved for reproducing
the earlier evidence, not rerun as part of this continuation.

```zsh
# historical mean-square numerical campaigns, from the target directory
# environment (about 100 MB, outside Git)
uv venv /Users/jinleic/jinleic-workspace/scratch/ai4s-stochastic-hinf-preview-control/venv --python 3.14
uv pip install --python /Users/jinleic/jinleic-workspace/scratch/ai4s-stochastic-hinf-preview-control/venv/bin/python -r work/requirements.txt
PY=/Users/jinleic/jinleic-workspace/scratch/ai4s-stochastic-hinf-preview-control/venv/bin/python
cd work
OMP_NUM_THREADS=4 PYTHONPATH=. $PY run_evidence.py ../evidence/numerics.json > ../evidence/numerics.log   # about 8 min (E1–E6)
PYTHONPATH=. $PY check_identities.py ../evidence/identities.json                                        # about 30 s
OMP_NUM_THREADS=1 PYTHONPATH=. $PY check_deterministic_limit.py ../evidence/deterministic_limit.json      # about 15 min
OMP_NUM_THREADS=4 PYTHONPATH=. $PY check_long_horizon.py                                                 # about 2 min
OMP_NUM_THREADS=4 PYTHONPATH=. $PY probe_literal_ratio.py ../evidence/literal_probe.json               # about 20 s, exploratory
OMP_NUM_THREADS=4 PYTHONPATH=. $PY check_lemma9.py ../evidence/lemma9_check.json                        # about 3 min
```

The Monte Carlo seeds are fixed in the scripts. Versions: Python 3.14.3, numpy 2.5.4, scipy 1.18.1,
macOS arm64.

## 10. Files

* [`work/theory.md`](work/theory.md): formalization, theorems, proofs, referee record.
* [`work/literal_continuation.md`](work/literal_continuation.md): literal mixed-norm
  convolution estimate, constant-matrix controller-solvability separation,
  and a fully characterized, separately scoped time-gated benchmark.
* [`work/check_literal_continuation.py`](work/check_literal_continuation.py):
  exact rational separation certificate and independent moment/quadrature checks.
* [`work/shp.py`](work/shp.py): both solvers. The continuous one is the advanced GRDE plus the
  infinite-horizon tests; the discrete one is the augmented game plus the closed-loop gain and
  Monte Carlo.
* `work/run_evidence.py`, `check_identities.py`, `check_deterministic_limit.py`,
  `check_long_horizon.py`, `check_lemma9.py`: fixed-parameter experiments.
* `work/probe_literal_ratio.py`: an exploratory probe of the printed L¹ criterion.
* [`evidence/`](evidence/): JSON outputs and logs; Codex prompts and replies; the literature-scout
  report.
* [`sources/`](sources/): book page images and `references.md`. The 2014 paper's PDF is
  third-party and kept outside Git, at
  `/Users/jinleic/jinleic-workspace/scratch/ai4s-stochastic-hinf-preview-control/hit2014.pdf` (sha256 38cbe352…d793).
