# Initial-output rectification: a positive degree-one theorem and its noise obstruction

Date: 2026-10-14 (America/Los_Angeles). This continuation was requested by the parent after the rational-memory proof was drafted. The explicit positive candidate came from the parent; the Bessel-integral proof and arbitrary-noise obstruction below sharpen its scope. No novelty claim and no solution of the full original problem.

## 1. An admissible output-value P modification

Fix `T>0`, `0<h<=T`, `ell>0`, and define

\[
\phi(t)=\min(t/h,1),\qquad \theta(t)=1-\phi(t).
\]

For the integrator `dot y_i=u_i`, uncontrolled starts `y_i(0)=a_i`, `|a_i|<=epsilon0`, zero initial input `u_0=0`, feasible reference `r=Jv`, `v` continuous, use

\[
u_{i+1}(t)=u_i(t)+\ell[e_i(t)-\theta(t)e_i(0)],\qquad e_i=r-y_i.
\]

This uses only the current-time and initial values of the previous measured error. It does not differentiate error, invert the plant, request additional state observations, impose resets, or restrict the target to a finite-dimensional span. It is physically causal but not pointwise-local, so Theorem D in `continuation-theorems.md` does not apply. The positive theorem in this section assumes **no process or measurement noise**. Section 4 rules out removing the arbitrary-measurement-noise exclusion; Section 5 separately proves an arbitrary-process-noise obstruction at degree one.

Put `A=I-ell J` and

\[
S_{h,T,\ell}=\sum_{k=0}^\infty\|A^k J\phi\|_\infty.
\]

**Theorem F1.** This constant is finite. For every bounded, possibly adversarial and nonconvergent start sequence,

\[
\|e_i\|_\infty\le\|A^i r\|_\infty+
(1+\ell S_{h,T,\ell})\epsilon_0,
\qquad \|A^i r\|_\infty\longrightarrow0.
\]

Consequently the law has a full-interval **output-error** bound linear in the arbitrary initial-error radius and nominal zero-output-error convergence. If the start is fixed, `a_i=a`, then `e_i -> -theta a` uniformly: exact tracking on `[h,T]` and a residual ramp on the whole interval `[0,h)`. No zero-mean, bias-zero, or random-start assumption occurs. The initial-only statement also applies to the genuinely nonlinear degree-one coordinate plant `dot x=u/(1+alpha cos x)`, `y=x+alpha sin x`, `0<alpha<1`, because its output equation is exactly the integrator and no cancellation is used by the learner. This coordinate transfer is not evidence for general nonlinear input-output dynamics or hidden states: the scalar output here determines the scalar state.

No uniform input boundedness or input convergence is claimed. In particular, `theta(0)=1` fixes `u_i(0)=0` forever, so nominal uniform input convergence already fails whenever the required input v has `v(0)!=0`, even though output tracking converges. This distinction is essential if a stronger formulation also demands internal stability.

## 2. Uniform Laguerre bounds without an endpoint asymptotic gap

The source identities actually inspected are the NIST DLMF [Laguerre–Bessel integral 18.10.9](https://dlmf.nist.gov/18.10.E9.tex) and [fixed-order Bessel asymptotic 10.17.3](https://dlmf.nist.gov/10.17.E3.tex). For `alpha=0,2`, continuity near zero and that asymptotic at infinity give a finite constant `B_alpha` with

\[
|J_\alpha(s)|\le B_\alpha s^{-1/2}\quad(s>0).
\]

Here `J_alpha` is the Bessel function, not the integration operator J. The integral identity reads, for `x>0` and the nonnegative integer parameters used here,

\[
L_n^{(\alpha)}(x)=\frac{e^x x^{-\alpha/2}}{n!}
\int_0^\infty e^{-s}s^{n+\alpha/2}J_\alpha(2\sqrt{xs})\,ds.
\]

Substitution yields the explicit bound

\[
|L_n^{(\alpha)}(x)|\le
\frac{B_\alpha}{\sqrt2}\,e^x x^{-\alpha/2-1/4}
\frac{\Gamma(n+\alpha/2+3/4)}{n!}.
\]

The integral identity can also be checked directly: expand the Bessel series, integrate each term (absolute summability follows from the factorial denominators), and apply Kummer's transformation to the resulting confluent hypergeometric series. Thus no Laguerre asymptotic uniform down to zero is being assumed. The directly inspected [gamma-ratio asymptotic, DLMF 5.11.12](https://dlmf.nist.gov/5.11.E12.tex), gives `Gamma(n+7/4)/n!=O((n+1)^(3/4))` and `Gamma(n+3/4)/n!=O((n+1)^(-1/4))`.

A finite binomial expansion of `(I-ell J)^n` gives the exact identities

\[
A^n(t^2/2)=\ell^{-2}L_{n+2}^{(-2)}(\ell t)
=\frac{t^2 L_n^{(2)}(\ell t)}{(n+1)(n+2)},
\qquad A^n1=L_n(\ell t).
\]

The alpha=2 bound above proves

\[
\|A^n(t^2/2)\|_\infty\le C_{T,\ell}(n+1)^{-5/4}.
\]

Although the intermediate bound has `x^(-5/4)`, multiplication by `t^2` leaves `t^(3/4)` and the estimate extends to zero continuously. The alpha=0 bound, integrated over `[0,T]`, proves

\[
\|A^n J\|_{C\to C}\le\int_0^T|L_n(\ell s)|ds
\le C'_{T,\ell}(n+1)^{-1/4}.
\]

The kernel identity for `A^nJ` follows by expanding J powers; this is not the sup norm of `A^n` itself. Therefore `A^n r=A^nJv ->0` for every feasible continuous input v.

## 3. Proof of the initial-only robustness statement

Causal delay by h commutes with J. With `f(t)=t^2/2` and `D_h f(t)=0` before h and `f(t-h)` thereafter,

\[
J\phi=(f-D_hf)/h,\qquad
\|A^nJ\phi\|_\infty\le(2/h)\|A^nf\|_\infty.
\]

The preceding summable `n^(-5/4)` bound proves `S<infinity`.

Since `e_i(0)=-a_i`, the learner obeys `u_{i+1}=Au_i+ell(r-phi a_i)`. Iterating and using `ell J=I-A` gives the exact physical-error formula

\[
e_i=A^i r-a_i1+\ell\sum_{j=0}^{i-1}A^{i-1-j}J\phi\,a_j.
\]

Its norm proves F1 for every start sequence. If `a_i=a`, telescoping gives

\[
e_i=A^i(r-\phi a)-\theta a.
\]

Both r and phi lie in the range of J on bounded functions; the same integrable-kernel bound applies to the essentially bounded derivative `phi'=h^{-1}1_{[0,h]}`. Thus the first term tends uniformly to zero, proving the fixed-start tail claim. QED.

**Regularity correction.** The parent's more general Lipschitz-theta suggestion is not needed. Mere `phi=O(t)` or Lipschitz continuity does not by itself justify a `n^(-5/4)` operator estimate: writing `Jphi=J^2 phi'` leaves an arbitrary bounded derivative, whereas the kernel of `A^nJ^2` has the slower `n^(-3/4)` scale. The explicit piecewise-linear theta above is proved. More generally the same proof works when phi(0)=0 and phi' has bounded variation: represent Jphi as a bounded-variation superposition of delayed quadratics. No claim of necessity of that regularity is made.

**A genuine layer-width tradeoff.** The robustness gain cannot be made uniform as h tends to zero. Since `||Jphi_h-J1||<=h/2`, each fixed `A^kJphi_h` tends uniformly to `A^kJ1`. For zero reference, at each positive t the exact worst-case gain through trial i is

\[
1+\ell\sum_{k=0}^{i-1}|A^kJ\phi_h(t)|.
\]

The trial starts independently realize each sign. Theorem B implies `sum_k |A^kJ1(t)|=infinity`. Taking any finite partial sum first and then h to zero proves that the supremum over trials of the displayed gain tends to infinity as h tends to zero. Thus one cannot make the prescribed boundary layer arbitrarily short while retaining one fixed uniform initial-error gain. This is a lower bound on the actual worst-case gain, not just looseness of S.

## 4. Theorem F2: every initial-output rectifier fails arbitrary measurement noise

Fix **any** continuous rectifying function theta, any nonzero real ell, any integer `q>=1`, any `t_* in (0,T]`, and a zero reference. On the q-fold integrator with zero initial states and `u_0=0`, use the same law `u_{i+1}=u_i+ell[e_i-theta e_i(0)]`. There exists one bounded infinite sequence of continuous measurement-noise traces, each identically zero on a common nontrivial initial interval, such that both the measured and physical outputs at t_* are unbounded across trials. In particular, the promising F1 rectifier does not solve the original arbitrary-noise problem, even at relative degree one.

**Proof.** Choose `0<tau<t_*`. Let X be the closed Banach subspace of `C[0,T]` whose functions vanish on `[0,tau/2]`. For any noise sequence in `ell_infinity(X)`, zero starts imply `e_i(0)=0`. Hence rectification is identically inactive in every update. Write `G=J^q`, `A_q=I-ell G`. Measured output at trial N is

\[
y_N^m=\xi_N-\ell\sum_{j=0}^{N-1}G A_q^{N-1-j}\xi_j.
\]

Define bounded linear functionals `F_N:ell_infinity(X)->R` by evaluation of this expression at t_*. Choose smooth ramps with `0<=psi_epsilon<=1`, zero up to tau and one after `tau+epsilon`. They belong to X and converge pointwise away from tau to the delayed unit step `D_tau 1`. For each fixed k>=1, the integral operator `G A_q^(k-1)` has a continuous integrable kernel, so dominated convergence gives

\[
[-\ell G A_q^{k-1}\psi_\epsilon](t_*)
\longrightarrow h_{q,k}(t_*-\tau),
\quad h_{q,0}=1,
\]

where `h_{q,k}` are exactly the pure-P initial-shift impulse coefficients of Theorem B in `theorems.md`. For sufficiently small epsilon, `psi_epsilon(t_*)=1` too. For each finite N choose the trial signs that maximize the delayed-step convolution; let epsilon tend to zero after fixing N. Thus

\[
\|F_N\|\ge\sum_{k=0}^N|h_{q,k}(t_*-\tau)|.
\]

Theorem B proves these partial sums unbounded for every q and every nonzero ell. Uniform boundedness on `ell_infinity(X)` therefore supplies a **single** bounded sequence xi for which `sup_N |F_N(xi)|=infinity`. Rescale to any positive prescribed noise radius. Each trial noise is continuous and zero on `[0,tau/2]`. The physical output differs from the measured one by bounded xi_N(t_*), so it too is unbounded. QED.

The proof uses smooth ramps only as finite-horizon approximants. This construction's infinite witness is in the Banach space of continuous traces; this construction alone does not assert uniform smoothness or equicontinuity. At degree one, the independent argument in Section 5 strengthens the measurement-noise witness to uniformly Lipschitz traces. The theorem rules out initial-value subtraction as a cure for arbitrary measurement noise; it does not rule out more substantial nonlinear, nonlocal, time-varying or noise-aware learning mechanisms.

## 5. Degree-one process noise and a regularity distinction

The independent referee supplied the following separate process-noise argument; it is included because a measurement-noise counterexample alone would not establish it.

### F3: arbitrary bounded continuous process noise also defeats this rectifier at q=1

Let `dot y_i=u_i+d_i`, with zero starts and reference, `ell!=0`, and any continuous theta. Fix `0<s_0<t_*`. Let X consist of continuous functions vanishing on `[0,s_0]`. Again `e_i(0)=0`, so the correction is inactive. Direct iteration gives

\[
y_N=Jd_N-\ell\sum_{j=0}^{N-1}J^2 A^{N-1-j}d_j.
\]

The kernel of `-ell J^2 A^{k-1}` is the old scalar initial-shift impulse `h_{1,k}(sigma)=-ell(A^{k-1}J1)(sigma)`. Therefore the norm of the time-t_* output functional on `ell_infinity(X)` is

\[
\|F_N\|=(t_*-s_0)+
\sum_{k=1}^{N}\int_0^{t_*-s_0}|h_{1,k}(\sigma)|\,d\sigma.
\]

Each trial's continuous disturbance may independently approximate the sign of its continuous kernel, while vanishing on the common initial interval; this proves equality of the norm with the sum of the L1 norms. By Theorem B, `sum_k |h_{1,k}(sigma)|=infinity` for every sigma>0. Tonelli/monotone convergence makes the displayed norms unbounded. Uniform boundedness supplies one bounded continuous disturbance sequence with unbounded output. Rescaling realizes any positive process-noise radius. QED.

As a measurement-noise-only construction, take `xi_i=Jd_i`. The measured outputs follow exactly the same recurrence, and `sup_i||xi_i'||<=sup_i||d_i||`. Physical output differs by bounded xi_i, so is also unbounded. Thus even a uniformly Lipschitz, equicontinuous measurement-noise class can defeat the degree-one rectifier. No corresponding process-noise proof for every q is asserted here; F2 already handles arbitrary measurement noise at every q.

### A sufficient stronger noise regularity, not a sharp threshold

For the F1 law at q=1, suppose instead `xi_i=J^2 g_i`, with `sup_i||g_i||<=M`, no process noise, and arbitrary starts of radius epsilon0. This is an additional noise-class restriction, not something inferred from a mere amplitude bound. Because xi_i(0)=0, the physical tracking-error formula in Section 3 gains the term

\[
\ell\sum_{j=0}^{i-1}A^{i-1-j}J^3g_j.
\]

The kernel of `A^kJ^3` is `A^k(t^2/2)`. With `C_{T,ell}` as in Section 2, the physical-error bound becomes

\[
\|r-y_i^{physical}\|\le\|A^ir\|+
(1+\ell S)\epsilon_0+
\ell T C_{T,\ell} M\sum_{k\ge0}(k+1)^{-5/4}.
\]

For measured error add `T^2 M/2`, the current-noise bound. This statement tolerates every trial sequence in this restricted class and uses no measured derivatives in the controller. F3 proves that merely restricting noise to `J(L_infinity)` does not suffice. We do not claim that `J^2(L_infinity)` is a necessary condition or that the unresolved fractional/Hölder regularity boundary has been classified.
