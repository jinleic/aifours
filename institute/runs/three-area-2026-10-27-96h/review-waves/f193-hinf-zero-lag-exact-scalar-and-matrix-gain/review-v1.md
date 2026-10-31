# f193 independent same-harness review: zero-lag scalar and matrix gain

Native observation before writing: `2026-10-29T09:51:28-0700 PDT`, from `/bin/date`. This is an observation, not a claimed file-creation time. The review is of the fixed zero-initial-state given law, on the canonical filtration, with one scalar Brownian driver; it is not controller synthesis.

## Verdicts and outstanding findings

Severity key: **F** = fatal counterexample/invalid central claim; **M** = major proof defect; **m** = minor scope/wording defect; **INCONCLUSIVE** = a specified step not resolved here. Counts below concern the frozen written source, not parent adoption. The reviewer reconstruction below supplies the explicit repair for M1; it is **not** an edit to the frozen candidate or a parent disposition.

| Claim | F / M / m | Reviewer conclusion |
|---|---:|---|
| Scalar radial inequality, exact root and finite-vector martingale bound | 0 / 0 / 0 | Reconstructed below, including interface, origin, all dimensions and localization; rational root bracket independently certified. |
| Scalar literal E2 and E1 gain `r sqrt(T)` | 0 / 0 / 0 | Reconstructed from the upper bound and bounded stopping-input family. The E1 truncation in the scalar source is pointwise. |
| Matrix E2 weighted inequality and exact gain `r c_T` | 0 / 0 / 0 | Reconstructed for arbitrary finite real matrices and ranks with one Brownian driver; burst limit has the correct order. |
| Matrix E1 weighted inequality and equality of E1/E2 gains | 0 / **1** / 0 | The author proof's full-path-norm truncation at matrix LF 79 need not be progressive. M1 below gives an explicit counterexample to that proof step and an independently reconstructed progressive replacement. With that replacement, the E1 conclusion follows; do not adopt the original proof verbatim. |
| Every nonzero input; strict endpoint for `c_T>0` | 0 / 0 / 0 | Correct for E2, and for E1 after M1's repair. The weighted clock is strictly smaller than `c_T^2 ||w||^2` on every nonzero input path; no maximizer exists. |
| RMS `sqrt(T)` / `c_T` | 0 / 0 / 0 | Ito isometry plus deterministic pulses proves these E2 RMS gains; strictness at the positive threshold is also pointwise. |
| Zero-output branch and feasibility at `c_T=0` | 0 / 0 / **1** | Output and both gains vanish. For a nonempty nonzero-input class, strict feasibility is exactly `gamma>0`, not `gamma>=0`. m1 records the unstated positive-input-dimension convention. |
| General controller synthesis, multi-Brownian law, novelty, priority | — | **INCONCLUSIVE / outside this frozen fixed-law scope**, not claimed proved here. |

No F finding was found within the given-law theorem under the stated imports. M1 remains a real defect in the *frozen matrix proof*, even though this review supplies a mathematically explicit repair. All supported conclusions are written-math reconstructions, not a formal/kernel, human, independent-model-family, cross-family, novelty, or parent-acceptance gate.

### M1 — nonprogressive full-path truncation in the matrix E1 proof

At matrix LF 79 the proposed truncation is `w_n = w 1(||w|| <= n)`, while `||w||` in this packet is the `L2[0,T]` **path norm**. This multiplier can reveal the future, so the claimed E2 inputs and their stochastic integrals need not be admissible. For a concrete canonical Brownian example, take `T=1`, scalar `w_t=1` for `t<1/2`, and `w_t=1+2 1{W_{1/2}>0}` for `t>=1/2`. This is bounded, progressive, and has squared path norm `1` on `{W_{1/2}<=0}` and `5` on `{W_{1/2}>0}`. At `n=2` the proposed truncated value for every `t<1/2` is `1{W_{1/2}<=0}`, which is not `F_t`-measurable: its conditional probability given `F_t` lies strictly between 0 and 1. The finite-filtration negative control independently displays the same adaptedness failure; the Brownian counterexample is the actual written argument.

**Explicit repair.** Use `w^(n)_t = w_t 1{|w_t| <= n}`, with Euclidean vector norm at time `t`, or an adapted energy-stopping truncation. These are progressive, bounded and E2. Since the input has finite path energy almost surely, `||w^(n)-w||_L2 -> 0` pathwise and is dominated by `||w||_L2`; hence its expectation tends to zero. The already-proved E2 bound applied to differences gives Cauchy convergence in `L1(Omega;L2[0,T])`. Moreover

`x^(n)_t - x_t = exp(Pt) integral_0^t exp(-Ps) B (w^(n)_s-w_s) dW_s`.

The bracket is bounded by a deterministic constant times `||w^(n)-w||_L2^2`, which tends to zero in probability. Stochastic-integral continuity after localization therefore gives uniform convergence in probability of the actual state/output paths, identifying the Banach-space limit with the actual local solution. The weighted seminorm obeys the triangle inequality and is bounded by `c_T ||w||`, so its expectation passes to the same limit. This proves (0.3) for every E1 input, including `c_T=0`. Denominators of nonzero inputs converge to a positive value; E1 ratios are thus limits of admissible E2 ratios. M1 must be disposed of explicitly rather than silently interpreting a path norm as an instantaneous norm.

### m1 — dimension convention

As usual, the claims are read for positive finite state/input/output dimensions, in particular `m>=1`. If a zero-dimensional input space were included literally, `lambda_max` of the `0 x 0` input Gramian would need a convention and the universal strict criterion would be vacuous for every `gamma` because no nonzero inputs exist. The text should state the convention; arbitrary *ranks*, including zero, are otherwise covered.

## Source order, identities, and coverage

The first scientific source body was the manifest, followed by the three inputs in its prescribed order. Before the manifest, mandatory memory/skill text and directory **metadata** were read; the run-root directory listing exposed file names, not held/f161/f162 payload. No unlisted scientific document, sibling review, author, linked disposition, or external source was opened. After all three complete input bodies had been displayed, selected already-read lines were re-opened solely to anchor M1 and the proof references. No source-order content deviation is asserted.

| Ordered item | Full SHA-256 | Bytes | LF | Actual raw coverage |
|---|---|---:|---:|---|
| `manifest-v1.json` | `5c7d247b81888b73cb12cb3a18d4bfc3b467b995f9188de3cfa95d2a3f94fc47` | manifest pin matched | — | Complete, first scientific body |
| Scalar `frontier-20261029-zero-lag-exact-literal-gain-and-strict-endpoint-v2.txt` | `dc15fd4153e34c28e91dcc557bc8f2e96c37a8fde08fd828e6ab792f70e38845` | 14209 | 165 | Sequential raw windows 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–165, through ending |
| Matrix `frontier-20261029-zero-lag-matrix-gramian-exact-gain-addendum-v1.txt` | `c883bad8e35f4735ef6844a963a7b42cb4137bbb331ddc7c0e72143e7929032b` | 13428 | 137 | Sequential raw windows 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–137, through ending |
| Author `frontier-20261029-zero-lag-profile-and-root-check.py` | `556934892fe7d1d709f232a62285cd0d21e0f39eea93ecf3bc2e6cdd1379cce5` | 5142 | 157 | Sequential raw windows 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–157, through ending |

All input bytes, SHA-256s, LF counts and final LF were independently checked against the manifest before mathematical assessment; the small raw windows were actually displayed without elision. The checker was read and hashed only, never executed or imported. Its obsolete degree-six upper profile is not used. Neither f186 nor any older bracket theorem is a premise.

## Reconstruction: special function and Bellman profile

Let `g(y)=exp(y^2/2)-y integral_0^y exp(s^2/2) ds`. Direct differentiation gives `g'(y)=-integral_0^y exp(s^2/2)ds`, `g''(y)=-exp(y^2/2)`, and `g''-y g'+g=0`. Thus `g` is strictly concave and strictly decreasing on `(0,infinity)`, with `g(0)=1`, `g(1)>0` and `g(y)<=1-y^2/2`; its positive root `r` exists uniquely and satisfies `r>1`. Termwise integration yields

`g(y)=1-sum_{k>=1} y^(2k)/(2^k k! (2k-1))`.

For `alpha=integral_0^r exp(s^2/2)ds`, the root equation gives `exp(r^2/2)=r alpha`. Define `f=-g/alpha` on `[0,r]` and `f(rho)=rho-r` beyond `r`. On the inner branch,

`f'=alpha^(-1) integral_0^rho exp(s^2/2)ds`, `f''=exp(rho^2/2)/alpha`, and `f-rho f'=-exp(rho^2/2)/alpha`.

At `rho=r`, the two values and first derivatives coincide, with `f(r)=0`, `f'(r)=1`; at zero, the even analytic branch has `f'(0)=0`. The function is convex, `0<=f'<=1`, and its tangent at `r` gives the essential majorization `f(rho)>=rho-r` everywhere.

For `a>0`, put `F(m,a)=sqrt(a) f(|m|/sqrt(a))`, `rho=|m|/sqrt(a)`. Then

`2 sqrt(a) F_a=f-rho f'`, `|grad_m F|=f'<=1`,

and the `m`-Hessian has radial eigenvalue `f''/sqrt(a)` and, in dimension at least two, tangential eigenvalue `f'/(rho sqrt(a))`. The latter is no greater than the former inside the sphere because the average of the increasing exponential over `[0,rho]` is no greater than its endpoint; at zero the common limit applies. Thus inside `rho<r`, `2F_a+lambda_max(D_m^2F)=0`. Outside, the radial eigenvalue is zero, the largest tangential eigenvalue is at most `1/(rho sqrt(a))`, and

`2F_a+lambda_max <= (-r+1/rho)/sqrt(a)<0`

because `rho>=r>1`; in dimension one the outer Hessian is zero. These cover every finite dimension. At the joining sphere the first `m` and `a` derivatives match, even though the radial second derivative jumps from `r/sqrt(a)` to zero. The origin is smooth for `a>0`; there is no surface delta from the join.

For the concavity question, the displayed `F` is convex, not concave: in addition to its nonnegative tangential Hessian, the radial/`a` block has

`F_aa=[rho^2 f''-(f-rho f')]/(4 a^(3/2))`, `F_ma=-(rho f''/(2a)) e`,

whose determinant is `-f''(f-rho f')/(4a^2)>=0`; on the outer branch `f''=0` and `F_aa=r/(4a^(3/2))>0`. Matching first derivatives preserve convexity across the interface. Equivalently `-F` is jointly concave and lies below `r sqrt(a)-|m|`; no unproved contrary concavity condition is needed. Also `|m|-r sqrt(a)<=F(m,a)<=|m|` and `F(m,0)=|m|` by continuous extension.

## Finite-vector Ito, sampled outputs, and E1 identification

For any progressive `q` in `R^d` with `E integral |q|^2<infinity`, one Brownian motion, `M_t=integral_0^t q_s dW_s`, `A_t=integral_0^t |q_s|^2 ds`, apply Ito to `F(M_t,A_t+epsilon)`. Its drift is

`F_a |q|^2 + (1/2) q^T D_m^2F q <= (|q|^2/2)(2F_a+lambda_max)<=0`.

The martingale integrand is bounded by `|q|`. For a rigorous join treatment, convolve `F` in `(m,a)` with a nonnegative mollifier supported within `a>0`; the distributional inequalities `F_a+(1/2)e^T D_m^2F e<=0` hold for every constant unit `e` and survive positive convolution. Apply ordinary Ito with localization, then let the mollifier shrink. Matched first derivatives rule out a surface measure; the gradient bound gives an L2 martingale. Linear growth, `E sup|M|<infinity`, and `E sqrt(A+epsilon)<infinity` justify localization/expectation. Majorization and `F(0,epsilon)=-sqrt(epsilon)/alpha`, followed by `epsilon downarrow 0`, give

`E|M_T| <= r E sqrt(A_T)`.

This covers random progressive vector directions, not just deterministic `q` times a scalar.

For matrix output samples `t_j=jT/N`, define the terminal martingale integrand blocks

`q_j^N(s)=sqrt(T/N) 1{s<t_j} C exp(P(t_j-s)) B w_s`.

Its terminal vector is `sqrt(T/N)(z_t1,...,z_tN)`; **the process `z_t` itself is not asserted to be a martingale**. Its clock is `integral w_s^T G_N(s)w_s ds`, where `G_N` is the finite Riemann sum in matrix LF 71. The deterministic kernels are uniformly bounded and `G_N(s)->G(T-s)` for almost every `s`. Pathwise dominated convergence and the integrable bound `sqrt(A_N)<=K ||w||` yield convergence of the expected clock norms. Continuity of the actual output gives a.s. convergence of the output Riemann sums, and Fatou yields

`E||z|| <= r E sqrt(integral_0^T w_s^T G(T-s) w_s ds)`.

This is first an E2 statement. The scalar sampled-martingale argument is the special case `P=0`, `B=C=1`, with clock `integral_0^T (T-s)w_s^2 ds`. Pointwise truncation gives the scalar E1 result; for matrix E1 use M1's explicit repair. No Hilbert-space Ito formula or unproved stochastic Fubini interchange is needed.

## Lower bound: stopping and physical burst

For each `0<b<r`, set `U(x,t)=sqrt(t)g(x/sqrt(t))`; the ODE gives `U_t+(1/2)U_xx=0`. Let `tau_b=inf{u>=0: |beta_u|=b sqrt(1+u)}`. Before the stopped boundary, `g(b)<=g(beta_u/sqrt(1+u))<=1`. Ito and bounded stopping at `tau_b wedge N` give

`g(b) E sqrt(1+tau_b wedge N) <= E U(beta_(tau_b wedge N),1+tau_b wedge N)=1`.

The stopped integrand is bounded on each finite horizon. Monotone convergence implies `E sqrt(1+tau_b)<=1/g(b)<infinity`, hence `tau_b<infinity` a.s.; dominated convergence even gives equality `g(b) E sqrt(1+tau_b)=1`. Continuity gives `tau_b>0` a.s. and the boundary gives `|beta_tau|=b sqrt(1+tau)`. The integrable domination `|beta_(tau wedge N)|<=b sqrt(1+tau)` and monotone convergence show

`E|beta_(tau wedge N)| / E sqrt(tau wedge N) -> b E sqrt(1+tau)/E sqrt(tau) > b`.

For each *finite* `N` and physical burst duration `epsilon`, use `R=N/epsilon`, `beta_u=sqrt(R)W_(u/R)` on `[0,N]`, `sigma_N=tau_b wedge N`, and the bounded, progressive physical input `v_s=sqrt(R) 1{s<epsilon}1{Rs<tau_b}`. It has squared energy `sigma_N`, and its actual accumulated stochastic input is `beta_sigma_N`. Coupling the changing finite-`N` Brownian paths is only a comparison in law, not an anticipative physical input.

For the scalar law, after the burst the output is constant; the `N->infinity` and then `epsilon->0` lower bound gives at least `b`. Scaling from unit horizon gives at least `b sqrt(T)`. For the matrix law, select any unit top eigenvector `a0` of `G(T)` when `c_T>0` and use `w=a0 v`. Write

`K_s a(t)=1{t>=s} C exp(P(t-s)) B a`, so `||K_s a||^2=a^T G(T-s)a`.

Compare the actual output to `K_0 a0 beta_sigma_N`, which is a random reference path, not a proposed causal state. Ordinary fixed-output-time Ito isometry and Tonelli give

`E||z-K_0 a0 beta_sigma_N||^2 <= omega(epsilon)^2 N`,

where `omega(epsilon)=sup_{s<=epsilon} ||K_s a0-K_0 a0|| ->0`. Indeed the missing interval `[0,s]` contributes `O(s)` to the squared norm and the exponential kernel changes by `O(s)` uniformly on `[s,T]`. For **fixed N**, send `epsilon` down to zero, then `N` to infinity, then `b` up to `r`. The resulting bound is at least `r c_T`; combining with the upper inequality proves the sharp literal gain. In particular, there is no use of an infinite-energy witness, no claim that a finite burst attains the gain, and no interchange requiring `omega(epsilon) sqrt(N)->0` uniformly in `N`.

## Strictness, all ranks, zero mode, and RMS

`G(u)=B^T integral_0^u exp(P^T t) C^T C exp(Pt)dt B` is positive semidefinite and increasing in Loewner order; its maximum eigenvalue at `T` is `c_T^2`. If `c_T>0`, for every `s in (0,T)` and `a!=0`,

`a^T G(T-s)a < c_T^2 |a|^2`.

Otherwise equality would force both top-eigenvector equality for `G(T)` and `C exp(Pt)B a=0` on the nonempty interval `[T-s,T]`. This real-analytic vector function then vanishes identically, giving `a^T G(T)a=0`, contradicting `c_T>0`. This includes invisible directions: their clock is zero, still strictly below the positive bound for nonzero `a`. Every nonzero L2 input path is nonzero on a set of positive time measure, so its weighted clock is strictly less than `c_T^2 ||w||^2`; finite expectations then give strictness for every nonzero E1 input, with M1's repair. The supremum is not attained. Thus for the positive branch the pointwise literal criterion is feasible exactly for `gamma>=r c_T`; a common uniform strict margin requires `gamma>r c_T`.

If `c_T=0`, then `G(T)=0` and `trace G(T)=integral_0^T ||C exp(Pt)B||_F^2 dt=0`. Continuity makes the entire kernel zero on `[0,T]`, hence the actual output is identically zero even for local E1 solutions. With `m>=1`, a nonzero deterministic input exists: the strict criterion is true for `gamma>0` and false for `gamma<=0`.

For E2, Ito isometry and Tonelli yield `E||z||^2=E integral w_s^T G(T-s)w_s ds <= c_T^2 E||w||^2`. A normalized deterministic pulse in a unit top-eigenvector direction satisfies

`(1/epsilon) integral_0^epsilon a0^T G(T-s)a0 ds -> c_T^2`.

For `c_T=0` the same zero-output conclusion applies. Hence RMS gain is `c_T`; the scalar case has `G(u)=u`, so RMS gain is `sqrt(T)`, with pulse squared ratio `T-epsilon/2`. For `c_T>0` the positive weighted-clock gap also implies pointwise RMS strictness at `gamma=c_T`. Neither RMS equality nor its pulse family is substituted for the literal-gain proof.

## Independent finite controls and limits

Both reviewer-authored programs use only exact `Fraction` arithmetic and the standard library; neither imports or runs author code. Each was run once with a 120-second cap, native `/bin/date` before and after, input/script/output hashes and exit receipt. Timeout would be **UNKNOWN**, not negative evidence. Both completed with exit code 0; no floating-point result is used as proof.

1. `reviewer-controls-v1.py`, SHA-256 `d092d1859842cf288f125330e4a11a56ee45c62149fa0b76ad9644594fff453d`; output `reviewer-controls-output-v1.txt`, SHA-256 `d0897ca2e43da6fb228c59492cedec924dec81c712f7b4909b499a09dc280397`; receipt `reviewer-controls-receipt-v1.json`, SHA-256 `59001691c3b822e3eb49d6fbbde3c7021270adad1410e45fc3f1196f2aa3ca18`. Start/end `2026-10-29T09:49:19-0700 PDT`. Direct factorial terms through `k=32` and the exact geometric tail ratio `q=x^2/[2(32+2)]` yield
   - `17484680/10^12 <= g(32673/25000) <= 17484681/10^12`, and
   - `-489403/10^12 <= g(130693/100000) <= -489402/10^12`.
   Consequently the claimed strict rational root enclosure and margins hold. Incorrect lower and upper endpoints, an invalid geometric tail and a supercritical stopping boundary were rejected for their intended reasons. The program also checks exact scalar clocks/pulses, selected matrix Riemann sums, zero/invisible and delayed-mode negatives, and the finite-filtration adaptedness diagnostic.
2. `reviewer-matrix-controls-v1.py`, SHA-256 `41424162dd9c01dc19b56a3193d27c12372674618becfc8e38f5d7cc4e6d0098`; output `reviewer-matrix-controls-output-v1.txt`, SHA-256 `bdf6abdc74170791892c343ec4c1361d229149fde91c6457daa3ea54d91947c7`; receipt `reviewer-matrix-controls-receipt-v1.json`, SHA-256 `01566f7e3a28b84b8a775a5877735731f51193fd4dea16c37f407bde93053800`. Start/end `2026-10-29T09:50:29-0700 PDT`. It constructs explicit matrices and their kernels, not just pre-entered verdicts:
   - nonnormal `P=[[0,1],[0,0]], B=I, C=[1,0]`, `H(t)=[1,t]`, `G(1)=[[1,1/2],[1/2,1/3]]`, top eigenvalue `(4+sqrt(13))/6`, and exact gap determinant `s^4/12` at selected rational `s`;
   - a singular `B` and an invisible input direction with `G(u)=diag(u,0)`; nonzero `B=e1`, `C=e2^T` with identically zero kernel; and `CB=0` but `CPB=1`, `H(t)=t`, `c_T^2=1/3`;
   - a two-input/two-output nonnormal example with `G(1)=[[1,3/2],[3/2,19/3]]`, `c_T^2=(22+sqrt(337))/6`, selected positive gaps, finite output-sampling Gramian errors, pulse limits and burst-kernel error bounds. False identity-Gramian, positive invisible output, zero-threshold and `CB=0`-implies-zero-output assertions are rejected for their intended reasons.

These are finite controls only. They do not replace the universal Hessian, analyticity, localization, stopping or limit arguments above. No claim of a machine-checked stochastic proof follows.

## Imports and residual boundary

Ordinary imports used explicitly: finite-dimensional Ito/isometry and localization; deterministic variation of constants and matrix-exponential analyticity; stochastic-integral continuity in probability from bracket convergence; Brownian scaling and bounded optional stopping; positive mollification and the distributional meaning of matched first derivatives; elementary eigenvalue/radial Hessian identities; finite-dimensional compactness; Tonelli, Fatou, dominated/monotone convergence, Riemann sums and Banach completeness. The root profile, stopping family and matrix extension are reconstructed from the two declared written packets, not accepted from a previous disposition. No book equivalence, lag, controller synthesis, state-multiplicative noise, drift input, direct feedthrough, multi-driver extension, novelty or priority result is established. The exact remaining action for the frozen proof is parent disposition of M1 and m1; any broader acceptance gate is separate.
