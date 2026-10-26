# Tangent bridge addendum v2 — localize instead of assuming global Lipschitz regularity

Observed before creation **2026-10-23T14:51:11-0700**, `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. InfoHinfPreview, info-3. **CANDIDATE extension, not independently accepted.** Written mathematics only; no execution.

Read with `proof-nonlinear-tangent-bridge-v1.md`, SHA256 **c117257e7beca6725b735f2daf4c0428824ed9a8d31677b0f20c6d77b94c6923**. Its globally Lipschitz theorem remains correct as originally scoped. This additive proof removes that unnecessary regularity restriction by replacing global mean-square convergence of the nonlinear outputs with localized convergence in probability and a one-sided Fatou argument. It is the same necessary-condition bridge, not a new problem or an additional result tally.

## 1. Strengthened exact claim

Use precisely the same deterministic stationary state/tap/L2-window controller `u_t=F(x_t,xi_t)`, the same Hilbert argument space, actual book plant, zero initial/history data, fixed finite preview length `h`, all adapted mean-square-integrable disturbances and the same norm/gain definitions as in the original tangent manuscript.

Assume only:

1. `F(0)=0` and `F` is **Fréchet differentiable at zero**, with bounded linear derivative `D=DF(0)`.
2. `F` is an **admissible controller**: the original controlled equation has the required well-posed nonexplosive strong solution for every legal input, including every scaled bounded input, and its realized controls are progressively measurable and locally pathwise-square-integrable so the Itô equation is meaningful.

There is **no global or local Lipschitz assumption** in this strengthened statement. Differentiability at one point is not being misidentified with local Lipschitz continuity. Global well-posedness is retained as an actual admissibility assumption, not inferred from differentiability.

Then still

\[
 G_1(D)\le G_1(F),                                          \tag{1}
\]

on the fixed finite counted horizon or the infinite horizon. On the **infinite horizon only**, the earlier fixed-linear comparison therefore gives

\[
 G_2(D)\le\sqrt3\,G_1(F).                                  \tag{2}
\]

The derivative's state/tap/kernel representation and the exact dependency on `proof-v1.md` Theorem B are unchanged. Nondifferentiable, nonstationary and arbitrary-history controllers remain outside this result. No same-gamma or unobservable-mode internal-stability conclusion is implied.

## 2. Local growth/remainder supplied by true Fréchet differentiability

Let `q=(x,xi)` denote the controller's Hilbert argument. There are a radius `rho>0`, a finite `L0=||D||+1` (after decreasing rho if needed), and a nondecreasing modulus `omega(s)` tending to zero as `s` decreases to zero, such that

\[
 |F(q)|\le L_0\|q\|,\qquad
 |F(q)-Dq|\le\omega(\|q\|)\|q\|,\qquad \|q\|\le\rho.        \tag{3}
\]

One may define `omega(s)` as the supremum of `|F(q)-Dq|/||q||` over `0<||q||<=s`; Fréchet differentiability makes it finite for sufficiently small `s` and makes it tend to zero. No compactness of an infinite-dimensional argument ball, derivative continuity elsewhere, or Lipschitz estimate for `F(q)-F(q')` is used.

First fix a **bounded** adapted disturbance, `|w_t|<=M`, still in the original input class, and a finite output observation time `T`. With `d` taps as before, its preview argument has the deterministic a.e. bound

\[
 \|\xi_t\|\le C_M:=M\sqrt{d+h},\quad0\le t\le T.             \tag{4}
\]

The delayed forcing also has magnitude at most `M`; neither observation anticipates future Brownian noise.

For positive `lambda`, let `x^lambda` be the actual nonlinear response to `lambda*w`, set `X^lambda=x^lambda/lambda`, and write `F_lambda(q)=F(lambda*q)/lambda`. These are actual scaled inputs to the admissible controller, not a newly assumed globally Lipschitz system.

For a fixed `R>0`, stop the **normalized state** at

\[
 \sigma_R^\lambda=\inf\{t\ge0:|X_t^\lambda|\ge R\}.
\]

When `lambda(R+C_M)<=rho`, the actual scaled controller argument stays in the neighborhood(3) before this stop. Thus its normalized control there has the uniform local-growth bound

`|F_lambda(X_t^lambda,xi_t)|<=L0(|X_t^lambda|+||xi_t||)`.

No estimate is asserted for the actual controller after the stop.

## 3. A stopped moment bound with constants independent of R and lambda

For transparency, set

`a=||A||+||B||L0`, `b=||B||L0`, `c=||C||`,

`a0=||A0||+||B0||L0`, `b0=||B0||L0`.

Before the stop the normalized state drift is bounded by

`a|X^lambda|+b||xi||+c|w(.-h)|`,

and its diffusion by `a0|X^lambda|+b0||xi||`. All `B0` terms remain present. Cauchy–Schwarz for the drift integral and the ordinary Doob L2 maximal inequality for the stopped Itô integral give, with

`K_T=6T a^2+16a0^2`,

`A0_(T,M)=(6T b^2+16b0^2)T C_M^2+6T^2 c^2 M^2`,

\[
 \mathbb E\sup_{s\le T}|X^\lambda_{s\wedge\sigma_R^\lambda}|^2
 \le A_{T,M}:=A0_{(T,M)}e^{K_TT}.                            \tag{5}
\]

Indeed `|drift|^2<=3(a^2|X|^2+b^2||xi||^2+c^2|w|^2)` and `|diffusion|^2<=2(a0^2|X|^2+b0^2||xi||^2)` yield the scalar integral inequality with coefficient `K_T`; Gronwall proves(5). The stopped integrand is bounded by constants depending on the fixed `R,M`, so its L2 martingale property is justified before applying Doob. The final bound itself depends on `T,M` and the local coefficients, but **not** on `R` or `lambda` satisfying the indicated smallness condition.

Continuity of the state and Markov therefore give

\[
 \mathbb P(\sigma_R^\lambda\le T)\le A_{T,M}/R^2.             \tag{6}
\]

This is a mathematical localization of the actual trajectory, not a physical/controller reset or an assumption of controller inactivity outside the ball.

## 4. Compare only before the stop; no nonlinear Lipschitz difference is needed

Let `X` be the global linear tangent-system state for the same actual input `w`. Write the derivative as `D(x,xi)=Kx+L xi`, where `L` denotes its fixed bounded input functional, equivalently the tap/kernel part. Before the stop define

\[
 R_t^\lambda=F_\lambda(X_t^\lambda,\xi_t)-D(X_t^\lambda,\xi_t).
\]

Unlike the first manuscript's proof, this remainder is evaluated at the **actual normalized state**, not at the tangent state. The uniform Fréchet estimate(3) gives the deterministic bound

\[
 |R_t^\lambda|
 \le a_{\lambda,R}:=\omega(\lambda(R+C_M))(R+C_M)
 \longrightarrow0\quad\text{for fixed }R.                  \tag{7}
\]

The difference `e^lambda=X^lambda-X`, stopped at the same `sigma_R^lambda`, has before that stop the exact equation

\[
 de_t^\lambda=[(A+BK)e_t^\lambda+B R_t^\lambda]dt
        +[(A_0+B_0K)e_t^\lambda+B_0R_t^\lambda]dW_t.         \tag{8}
\]

The external derivative input `L xi` cancels exactly, and no estimate of `F(q)-F(q')` is required. The original delayed forcing also cancels. Standard integral Cauchy–Schwarz/Doob L2/Gronwall estimates applied to this **linear stopped error equation** give a finite constant `B_T`, independent of `R,lambda`, such that

\[
 \mathbb E\sup_{s\le T}|e^\lambda_{s\wedge\sigma_R^\lambda}|^2
 \le B_T a_{\lambda,R}^2\longrightarrow0
 \quad\text{for each fixed }R.                             \tag{9}
\]

For example the derivation of(5) can be repeated with `a=||A+BK||`, `a0=||A0+B0K||`, input bounded by `a_(lambda,R)`, and input matrices `B,B0`. No global moment estimate for the actual unstopped nonlinear system is invoked.

Before the stop the normalized output error is exactly

\[
 z^\lambda/\lambda-z^{lin}
 =(D_0+D_1K)e^\lambda+D_1R^\lambda.
\]

Equations(7)–(9) therefore imply, for another finite `C_T`,

\[
 \mathbb E\int_0^{T\wedge\sigma_R^\lambda}
 |z_t^\lambda/\lambda-z_t^{lin}|^2dt
 \le C_Ta_{\lambda,R}^2.                                   \tag{10}
\]

For any threshold `eta>0`, combine(6),(10):

\[
\begin{aligned}
 &\mathbb P\left(\|z^\lambda/\lambda-z^{lin}\|_{L2[0,T]}>\eta\right)\\
 &\quad\le A_{T,M}/R^2+C_Ta_{\lambda,R}^2/\eta^2.
                                                               \tag{11}
\end{aligned}
\]

First take `lambda->0` for fixed `R`, then `R->infinity`. This proves **finite-time path-L2 convergence in probability**. It does not assert global N2 convergence, uniform integrability, or a bound on nonlinear output moments after the localization exit.

## 5. Fatou transfers the printed gain; then linear approximation removes the input bound

Suppose `Gamma=G1(F)<infinity`; otherwise the claimed necessary inequality is vacuous. For every legal positive scaling,

`E ||z^lambda/lambda||_(L2[0,T]) <= Gamma N1(w;counted input)`.

By(11), the norm random variables converge in probability to `||zlin||_(L2[0,T])`. Select an a.s.-convergent subsequence and apply Fatou, obtaining

\[
 N_1(z^{lin};[0,T])\le\Gamma N_1(w;\text{counted input})      \tag{12}
\]

for bounded adapted inputs. No uniform integrability is needed for this **one-sided lower semicontinuity** step. On an infinite-horizon controller, the right side uses its full input interval while `T` is still only a finite observation time. On a finite book horizon the input remains zero beyond `T-h` throughout this argument.

For an arbitrary square-integrable adapted input `w`, clip its Euclidean amplitude at `M`:

`w^M=w min(1,M/|w|)` with the value0 when `w=0`.

This preserves progressive measurability and the actual input support, has `N1(w^M)<=N1(w)`, and converges to `w` in mean-square input energy by dominated convergence. **Only the linear tangent system** is now approximated: its finite-time linear-SDE continuity gives `zlin_(w^M)->zlin_w` in finite-time N2, hence N1. Apply(12) to `w^M` and let `M` increase. The result is(12) for every original adapted input, with right side at most `Gamma N1(w)`.

On a fixed finite book horizon, take the input supremum to conclude(1). On the infinite horizon, keep each fixed input and **only now** increase the finite output observation time `T`; monotone convergence gives its full literal output bound. Finally take the input supremum. Thus(1) holds, and the stationary-linear Theorem B gives(2).

The order is: bounded input and finite observation; fixed normalized-state stop R; `lambda->0`; `R->infinity`; Fatou; linear input clipping limit; output `T->infinity`; input supremum. No infinite-time nonlinear linearization, stochastic simulator or executable check is hidden in those steps.

## 6. Updated necessary-condition scope

The global Lipschitz premise in the first tangent candidate is therefore unnecessary for the proposed necessary condition. Under the usual original **admissibility/well-posedness** requirement, finite printed gain of a deterministic stationary zero-preserving controller that is merely Fréchet differentiable at0 forces a finite-mean-square-gain linear preview tangent, with the stated `sqrt(3)` quantitative factor. This does not infer local Lipschitz continuity from pointwise differentiability.

The remaining genuine regularity gap is now **differentiability/stationarity/finite-window state form**, not a missing global growth estimate. This still does not settle arbitrary nonsmooth, time-varying or arbitrary-history synthesis, nor prescribed-gamma optimality. All external classical imports (Riesz, Doob L2, Itô/Gronwall/Fatou) are stated; no unmatched Riccati theorem is used. Correctness and novelty remain separate; the original two manuscript snapshots and their timestamps/hashes are preserved.
