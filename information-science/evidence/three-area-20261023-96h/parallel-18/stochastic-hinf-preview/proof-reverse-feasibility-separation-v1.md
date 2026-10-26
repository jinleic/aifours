# A reverse feasibility separation under the actual printed criterion

Observed before creation: **2026-10-23T14:27:27-0700** (`/bin/date '+%Y-%m-%dT%H:%M:%S%z'`). Author: InfoHinfPreview, info-3. **CANDIDATE, pending separate reconstruction and parent review.** Written proof only; no scientific execution. This continues the same stochastic preview problem after the bounded SPR review.

## 0. Exact consequential claim

The previous dossier's finite-horizon gamma6 baseline shows **literal feasibility need not imply mean-square feasibility**. It does not decide the converse at the same performance level.

The theorem below supplies the opposite direction, for the book's actual constant-matrix model on the **infinite horizon**, with **strictly positive preview**, **nonzero effective drift control**, **control-dependent diffusion**, **full-rank control penalty**, and an internally mean-square-stable exhibited controller:

> At one exact level `gamma=16386`, the mean-square problem is strictly feasible for every adapted square-integrable disturbance, but **no nonanticipative controller** can satisfy the printed expectation-of-pathwise-L2 criterion.

The impossibility allows all adapted control histories, hence includes all controllers of the book's state/preview-window form and their preview pre-action. The adversarial disturbance is adapted, not deterministic. It is not legal to restrict the disturbance supremum to deterministic signals in applying this theorem.

This is a counterexample to a same-level objective substitution, **not a necessary/sufficient characterization for every plant**, and not a second proof of the old gamma6 separation. Novelty remains UNCLEAR.

## 1. Model, exact parameters and admissibility

On a Brownian filtered probability space with independent future increments, set `x=(f,y)^T` and use

\[
 \begin{aligned}
 df_t&=\kappa[-f_t+w(t-h)]dt,\\
 dy_t&=(-\varepsilon y_t+u_t)dt+(f_t+u_t)dW_t,\\
 z_t&=(y_t,r u_t)^T,\qquad f_0=y_0=0.
 \end{aligned}                                                \tag{1}
\]

The horizon is `[0,infinity)`, negative-time disturbance history is zero, and

\[
 \varepsilon=h=2^{-29}>0,\quad \kappa=2^{28},\quad r=2^{43},
 \quad g=2^{14}=16384,\quad \delta=2^{-11}=1/2048,
 \quad\gamma=g(1+\delta/4)=16386.                              \tag{2}
\]

These are exact rational parameters. No floating-point tuning, simulator search or executable arithmetic was used.

In the notation printed in the book the constant matrices are

\[
 A=\begin{pmatrix}-\kappa&0\\0&-\varepsilon\end{pmatrix},
 \quad B=B_0=\binom01,\quad C=\binom\kappa0,
 \quad A_0=\begin{pmatrix}0&0\\1&0\end{pmatrix},
\]

\[
 D_0=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad D_1=\binom0r.
                                                               \tag{3}
\]

Thus the control genuinely affects the performance state in both drift and diffusion; it is not an unused actuator or a separate irrelevant state. `D1^T D1=r^2>0` and `D1^T D0=0`.

Disturbances range over **all progressively measurable** `w` with `E integral_0^infinity w^2<infinity`. The comparison controller is simply `u=0`, which has the book's information form. In the impossibility direction allow any progressively measurable realized control `u`, even nonlinear/history-dependent and using full Brownian past, provided the closed loop is strongly well posed and `u` is locally pathwise square-integrable so its Itô integral exists. A controller with infinite printed output norm already fails.

Write `Np` as in `proof-v1.md`: `N1(v)=E sqrt(integral |v|^2)` and `N2(v)=sqrt(E integral |v|^2)`. At no point is the printed input denominator replaced by its RMS value.

## 2. Explicit dependency boundary

This proof uses the source-checked **causal transfer theorem A**, including its larger-input localization extension, in

`proof-v1.md`, SHA256 **895a36cdc42565aa7b7b6fd4279a34aba6b3bb7f0c8918d14e49d59b72f5635c**.

That theorem is an application of Geiss–Scheutzow, arXiv:2101.10884v2, [Theorem2.2](https://arxiv.org/html/2101.10884v2#S2.Thmtheorem2), at `p=1/2`: a strongly causal zero-preserving map with mean-square gain at most `M2` has literal gain at most `sqrt(2) M2`. Its actual monotonicity/predictability/stopping-time hypotheses are verified in the pinned manuscript. Theorem A has a separate in-harness peer reconstruction by InfoSPR7, not a formal/human/novelty acceptance; parent review is separate.

No preview Riccati theorem from the 2014 or 2020 papers is imported. The remaining facts below follow directly from Itô isometry, deterministic convolution, Brownian continuity and its Gaussian marginal, integration by parts, elementary squares, Markov's inequality, Fatou and monotone convergence. In particular the stopping-time norm gap is proved here; a sharp BDG constant or an exit-time distribution is not imported.

## 3. Mean-square strict feasibility, including internal stability

Take `u=0`. Let `v_t=w(t-h)` and

\[
 f_t=\int_0^t\kappa e^{-\kappa(t-s)}v_sds,
 \qquad d_t=\int_0^t e^{-\varepsilon(t-s)}f_s\,dW_s.           \tag{4}
\]

Here `d` denotes the uncontrolled performance-state response, not the parameter `delta`. Extend inputs by zero to negative times. Since the scalar kernel `kappa exp(-kappa t)1_(t>=0)` has integral1, Jensen followed by Tonelli proves the **pathwise** contraction

\[
 \int_0^\infty f_t^2dt\le\int_0^\infty v_t^2dt
                         =\int_0^\infty w_t^2dt.             \tag{5}
\]

The delayed signal and its filter are adapted. Itô isometry and Tonelli give

\[
 N_2(d)^2=\mathbb E\int_0^\infty\int_0^t
 e^{-2\varepsilon(t-s)}f_s^2dsdt
 ={1\over2\varepsilon}\mathbb E\int_0^\infty f_s^2ds
 \le g^2 N_2(w)^2,                                         \tag{6}
\]

because `1/sqrt(2 epsilon)=2^14=g`. Thus `u=0` has mean-square induced gain at most16384, **strictly less than gamma16386**, uniformly over every adapted disturbance in the stipulated class.

For `w=0`, the homogeneous system under the same controller has

\[
 d\mathbb E(f_t^2+y_t^2)/dt
 =-(2\kappa-1)\mathbb E f_t^2-2\varepsilon\mathbb E y_t^2
 \le-2\varepsilon\mathbb E(f_t^2+y_t^2),                     \tag{7}
\]

since `2 kappa-1>=2 epsilon`. This proves exponential internal mean-square stability directly, with storage `P=I`; no unobservable unstable mode is hidden.

## 4. A self-contained adapted input with a strict norm gap

Let

\[
 \tau=\inf\{t\ge0:|W_t|=1\},\quad
 w_t=1_{\{t<\tau\}},\quad M_t=W_{t\wedge\tau}.               \tag{8}
\]

The process `w` is an admissible progressively measurable disturbance. The endpoint convention is immaterial. Itô isometry for the bounded stopped Brownian motion gives

`E(t wedge tau)=E M_t^2<=1`.

Monotone convergence implies `E tau<=1`, so `tau` is finite almost surely. Brownian continuity then gives `|W_tau|=1`; dominated convergence of `M_t^2`, bounded by1, proves

\[
 \mathbb E\tau=1,\qquad N_2(w)=1,\qquad N_1(w)=\mathbb E\sqrt\tau.
                                                               \tag{9}
\]

We need a quantitative **strict** gap in the last quantity. If `Z` is standard normal, Brownian continuity gives

\[
 \mathbb P(\tau\le1/2)
 \ge\mathbb P(W_{1/2}\ge1)
 =\mathbb P(Z\ge\sqrt2)
 \ge\int_{3/2}^{2}{e^{-x^2/2}\over\sqrt{2\pi}}dx
 >{1\over54}.                                               \tag{10}
\]

For the last elementary lower bound use `sqrt(2)<3/2`, `e<3` and `pi<4`: on the indicated interval the Gaussian density is at least `e^-2/sqrt(2pi)>1/27`, and the interval length is1/2.

The exact identity

`(1+t)/2-sqrt(t)=(sqrt(t)-1)^2/2`

and `E tau=1` imply

\[
 \mathbb E\sqrt\tau
 =1-\tfrac12\mathbb E(\sqrt\tau-1)^2.
\]

On `tau<=1/2`, `sqrt(tau)<=1/sqrt(2)<3/4`, so the squared deviation exceeds1/16. Therefore

\[
 N_1(w)<1-{1\over1728}<1-{1\over2048}=1-\delta.              \tag{11}
\]

This is where adaptedness matters: the input stops after observing Brownian hitting information. There is no anticipating or deterministic-input replacement.

## 5. Literal output lower anchor for the slow state

First use the **ideal** slow OU response driven by the adapted input directly in diffusion,

\[
 Z_t=\int_0^t e^{-\varepsilon(t-s)}w_s\,dW_s
    =M_t-\varepsilon\int_0^t e^{-\varepsilon(t-s)}M_sds.      \tag{12}
\]

This ideal process is only a comparison quantity; **the actual plant remains(1)** with delayed drift forcing and filtering. The equality follows by integration by parts against the deterministic exponential kernel.

At the finite stopping time `tau`, `|M_tau|=1` and `|M_s|<=1`, hence

\[
 |Z_\tau|\ge1-\varepsilon\tau.                              \tag{13}
\]

After `tau`, its diffusion forcing is zero, so `Z_t=e^(-epsilon(t-tau)) Z_tau`. Consequently on `tau<=R` its full path norm is at least `g(1-epsilon R)`. Choose the exact threshold

\[
 R=2^{14},\qquad \varepsilon R=2^{-15}=\delta/16,
 \qquad1/R=2^{-14}=\delta/8.
\]

Markov's inequality and `E tau=1` give

\[
 N_1(Z)\ge g(1-\varepsilon R)\mathbb P(\tau\le R)
 \ge g(1-\delta/16)(1-\delta/8)
 \ge g(1-\delta/4).                                         \tag{14}
\]

Only a lower bound is required; no claim that this is the exact induced gain is made.

## 6. Explicit positive-preview and low-pass error

For the actual delayed input `v_t=w(t-h)=1_[h,h+tau)(t)`, the two step intervals have symmetric difference of length `2 min(h,tau)`, so **pathwise**

\[
 \int_0^\infty|v_t-w_t|^2dt\le2h.                           \tag{15}
\]

The actual low-pass state `f` is zero before `h`, equals `1-exp(-kappa(t-h))` on `[h,h+tau]`, and equals `(1-exp(-kappa tau))exp(-kappa(t-h-tau))` afterward. Direct integration gives the exact identity

\[
 \int_0^\infty|f_t-v_t|^2dt
 ={1-e^{-\kappa\tau}\over\kappa}\le1/\kappa.                \tag{16}
\]

All processes remain adapted: after the delayed switch, `tau` is already past information. There is no comparison with an input chosen using future noise.

By Minkowski in `L2(Omega x time)`,

\[
 N_2(f-w)\le\kappa^{-1/2}+\sqrt{2h}
           =2^{-14}+2^{-14}=2^{-13}=\delta/4.                 \tag{17}
\]

The actual uncontrolled state is `d` from(4). Applying Itô isometry to the difference between(4) and(12) yields

\[
 N_1(d-Z)\le N_2(d-Z)=g N_2(f-w)\le g\delta/4=2.             \tag{18}
\]

Combining(14) and(18) in the actual printed norm proves

\[
 N_1(d)\ge g(1-\delta/2)=16380.                              \tag{19}
\]

Thus the strictly positive preview length has been paid for quantitatively. It has not been silently replaced by zero.

## 7. Every controller is excluded, not just u=0

For any realized adapted control, linearity of(1) gives

\[
 y=d+S u,
\]

where the **control-only** response is

\[
 (Su)_t=\int_0^t e^{-\varepsilon(t-s)}u_sds
           +\int_0^t e^{-\varepsilon(t-s)}u_s\,dW_s.          \tag{20}
\]

This decomposition is valid even if the rule producing `u` is nonlinear, depends on the controlled state, uses all past Brownian information, or takes preview pre-action. It only treats the resulting adapted process as an input to a linear equation. Neither the plant nor the controller is reset.

The deterministic convolution in(20) has pathwise-L2 gain at most `1/epsilon`; the stochastic convolution has mean-square gain exactly `1/sqrt(2epsilon)`. Minkowski therefore proves, for every adapted square-integrable control input,

\[
 N_2(Su)\le M_2 N_2(u),\qquad
 M_2=\varepsilon^{-1}+(2\varepsilon)^{-1/2}=2^{29}+2^{14}.
                                                               \tag{21}
\]

The map `S` is strongly causal, linear, zero-preserving, and locally well posed for pathwise-square-integrable inputs. The source-checked causal transfer and its localization extension consequently give

\[
 N_1(Su)\le M N_1(u),\qquad
 M=\sqrt2(2^{29}+2^{14})<2^{31}.                             \tag{22}
\]

The extension is important: an attempted controller may have finite `N1(u)` but infinite `N2(u)`. It is not silently excluded. Stop its input at accumulated energy `b`, apply(22) on the square-integrable stopped input, then use Fatou and pathwise local uniqueness as in the pinned transfer proof.

If an attempted controller has infinite `N1(z)`, it already fails. Otherwise the separate `r*u` output implies finite `N1(u)` and hence pathwise finite total control energy. Thus(22) applies. Put `X=||y||_(L2 time)` and `U=||u||_(L2 time)`. Triangle followed by **pathwise** two-dimensional Cauchy–Schwarz gives

\[
 \begin{aligned}
 N_1(d)&\le N_1(y)+N_1(Su)\\
       &\le\mathbb E(X+MU)\\
       &\le c_*\mathbb E\sqrt{X^2+r^2U^2}
        =c_*N_1(z),
 \end{aligned}
\]

where

\[
 c_*=\sqrt{1+(M/r)^2}
 <1+2^{-24}<1+\delta/8.                                     \tag{23}
\]

Indeed `M/r<2^31/2^43=2^-12` and `sqrt(1+x)<=1+x`. This control-cost estimate includes all actuation in both drift and diffusion, not only deterministic actuation.

For the **single fixed admissible disturbance(8)**, equations(11),(19),(23) now imply for every controller

\[
 {N_1(z)\over N_1(w)}
 >g\,{1-\delta/2\over(1-\delta)(1+\delta/8)}
 >g(1+\delta/4)=\gamma=16386.                               \tag{24}
\]

The last strict inequality is entirely algebraic. The denominator is positive and

\[
 \begin{aligned}
 &(1-\delta/2)
 -(1+\delta/4)(1-\delta)(1+\delta/8)\\
 &\qquad=\delta/8+3\delta^2/16+\delta^3/32>0.
 \end{aligned}
\]

Thus **no adapted controller**, and in particular no controller with the book's state/window information, has literal induced gain below gamma. This proves the claimed reverse **controller-existence** separation.

## 8. What is and is not closed

**Closed by this candidate, subject to review:** a fully specified infinite-horizon positive-preview constant-matrix instance with effective drift and diffusion control is strictly mean-square feasible at gamma16386, yet the printed norm is infeasible at that same level for every admissible nonanticipative controller. It is not a comparison of two ratios for one law. The mean-square feasible law is internally mean-square stable.

Together with the independently preserved opposite-direction finite-horizon gamma6 baseline, this prevents using either direction of an **unqualified same-gamma substitution across the book's requested horizon regimes**. The two examples are on different stated horizons; this does not claim bidirectional failure for one single fixed horizon or one single plant. In particular, the present proof does not show that infinite-horizon literal feasibility fails to imply mean-square feasibility at the same level, or that finite-horizon mean-square feasibility fails to imply literal feasibility.

**Still unresolved:** necessary and sufficient synthesis for an arbitrary plant and prescribed literal gamma; the exact optimum for(1); the strength of the preview dependence; sharp transfer constants; and novelty of this exact embedding. The large/small rational parameters are deliberately conservative proof margins, not engineering-optimal values.

**Classical-versus-round distinction:** the stopped-Brownian `E sqrt(tau)<sqrt(E tau)` mechanism is classical stochastic-analysis territory, not a new probability discovery. The contribution claimed here is only a written candidate embedding with the actual book model, strictly positive preview paid for explicitly, and an all-controller feasibility separation. No priority assertion follows from a search miss.

**Evidence:** complete symbolic written candidate with explicit named classical dependency and ordinary Itô calculations; separate reconstruction and parent review requested at the pinned snapshot. No scientific executable, solver, simulation, proof-assistant kernel, human expert or independent-model CLI review was run.
