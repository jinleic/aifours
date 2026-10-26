# Candidate bridge: what finite literal gain forces for a smooth nonlinear preview law

Observed before creation: **2026-10-23T14:43:17-0700**, `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. InfoHinfPreview, same info-3 primary problem. **CANDIDATE written derivation, not independently accepted or novelty-cleared.** No scientific executable was run. This is a bounded bridge beyond the fixed-linear-law boundary in the first manuscript, not another active problem or a full synthesis result.

## 1. Exact nonlinear restriction, not a hidden replacement of the book

Keep the printed continuous-time plant, actual fixed finite `h>=0`, zero initial/history data and all progressively measurable mean-square-integrable disturbances:

\[
 dx_t=(Ax_t+Bu_t+Cw(t-h))dt+(A_0x_t+B_0u_t)dW_t,
 \qquad z_t=D_0x_t+D_1u_t.                                  \tag{1}
\]

Fix finitely many taps `r_j in[0,h]`, `1<=j<=d`, and let

\[
 \xi_t=\big(w(t-r_1),\ldots,w(t-r_d),\theta_t\big),
 \qquad \theta_t(r)=w(t-r),\quad0\le r\le h.
\]

The input-argument Hilbert space is

`H_in=(R^q)^d direct-sum L2([0,h];R^q)`.

Negative-time input is zero; the endpoint values in the L2 window do not supply extra information, while taps are separately included as a.e.-defined observations. The actual controller has the book's information pattern:

\[
 u_t=F(x_t,\xi_t),\qquad F:\mathbb R^n\oplus H_{in}\to\mathbb R^m.
                                                               \tag{2}
\]

Assume `F` is **deterministic, stationary, globally Lipschitz, zero-preserving, and Fréchet differentiable at zero**. These are real restrictions beyond the general book formulation. They do not cover arbitrary history-dependent, time-varying, nondifferentiable or merely measurable laws. The result below does not silently promote them to necessary properties of every feasible controller.

Let `L_F` be a global Lipschitz constant and let `D=DF(0)` be the bounded linear derivative, with operator norm at most `L_F`. Decomposing the derivative over the finite-dimensional arguments and using the classical Riesz representation theorem componentwise on its L2-window part gives fixed real matrices and a square-integrable deterministic kernel:

\[
 D(x,\xi_t)=Kx+\sum_{j=1}^dJ_jw(t-r_j)
                    +\int_0^h H(r)w(t-r)dr.                \tag{3}
\]

Thus the tangent law is exactly of the specified stationary linear preview class in `proof-v1.md`, not a new controller-information enlargement. Riesz representation is a named standard functional-analysis import; no Riccati theorem is used.

Define the induced literal gains `G1(F)` and `G1(D)` using `N1(v)=E sqrt(integral |v|^2)` over the same adapted input class and stated horizon. `G2(D)` uses the mean-square norm only when explicitly named.

## 2. Claim and dependency boundary

**Tangent domination.** On either a fixed finite counted horizon or the infinite horizon,

\[
 G_1(D)\le G_1(F).                                          \tag{4}
\]

For the finite case the input support remains exactly `[0,T-h]`. For the infinite case, combining(4) with Theorem B of `proof-v1.md` gives

\[
 G_2(D)\le\sqrt3\,G_1(F).                                  \tag{5}
\]

Theorem B is imported only at its **infinite-horizon**, same stationary-linear-class boundary. Its source snapshot is SHA256 **895a36cdc42565aa7b7b6fd4279a34aba6b3bb7f0c8918d14e49d59b72f5635c**. InfoSPR7 separately reconstructed that manuscript in `robust-spr7/peer-review-Hinf-printed-criterion-v1.md`, SHA256 **f54b3cbb52dc3a91cad084493eda4d14a57df228838a92c54577c595e4851013**; parent reconstruction and novelty/formal acceptance remain separate. Neither theorem gives a same-gamma replacement or internal stability of unobservable modes.

The actual new obligation is the finite-time linearization under the `B0*u` diffusion and adapted preview arguments. It is proved below, rather than importing a deterministic linearization theorem or taking an unproved infinite-time limit.

## 3. Finite-time normalized-state convergence

Fix any adapted input `w` in the stipulated square-integrable class and any finite observation time `T`. All tap/window arguments are adapted. Tonelli and the zero past give

\[
 \mathbb E\int_0^T\|\xi_t\|^2dt
 \le(d+h)\mathbb E\int_0^T|w_t|^2dt<\infty.                 \tag{6}
\]

A shifted tap contributes at most one copy of the counted right-hand input energy; the window integral contributes at most `h` copies. On a finite book horizon the input is zero after `T-h`, so this remains valid without adding uncounted input values. The Hilbert-valued window is interpreted a.e.; all resulting finite-dimensional control processes are progressively measurable.

For positive `lambda`, drive the **actual nonlinear controller** by `lambda*w` and call its state `x^lambda`. Define

`X^lambda=x^lambda/lambda`,

`F_lambda(q)=F(lambda*q)/lambda`.

Because `F(0)=0`, every `F_lambda` is zero-preserving with the **same** Lipschitz constant `L_F`. Its argument is the actual scaled state together with the actual scaled preview input. Thus

\[
\begin{aligned}
 dX_t^\lambda
 &=[AX_t^\lambda+B F_\lambda(X_t^\lambda,\xi_t)+Cw(t-h)]dt\\
 &\quad+[A_0X_t^\lambda+B_0F_\lambda(X_t^\lambda,\xi_t)]dW_t.
                                                               \tag{7}
\end{aligned}
\]

Let `X` be the tangent-system state, obtained by replacing `F_lambda` in(7) by `D`. Global Lipschitz/linear growth give strong finite-time well-posedness and finite second moments for both systems, using(6). Infinite-horizon stability is **not assumed** in this finite-time step.

The residual evaluated at the **fixed tangent state** is

\[
 R_t^\lambda=F_\lambda(X_t,\xi_t)-D(X_t,\xi_t).
\]

Fréchet differentiability at zero implies `R_t^lambda ->0` for a.e. `(omega,t)`. Also

`|R_t^lambda|<=2 L_F ||(X_t,xi_t)||`.

The right side is square-integrable on `Omega x[0,T]`. Dominated convergence therefore gives

\[
 \mathbb E\int_0^T|R_t^\lambda|^2dt\longrightarrow0.          \tag{8}
\]

This evaluates differentiability only at a fixed finite random argument before letting `lambda` tend to zero; no uniform differentiability on the entire random state space is presumed.

Put `e_t^lambda=X_t^lambda-X_t` and

`Q_t^lambda=F_lambda(X_t^lambda,xi_t)-F_lambda(X_t,xi_t)`.

Then `|Q_t^lambda|<=L_F|e_t^lambda|` and the actual error SDE is

\[
 de_t^\lambda=(Ae_t^\lambda+BQ_t^\lambda+BR_t^\lambda)dt
          +(A_0e_t^\lambda+B_0Q_t^\lambda+B_0R_t^\lambda)dW_t.
                                                               \tag{9}
\]

The `B0` terms are all retained. Apply Itô to the squared Euclidean error, localize at bounded state/input energy, and use `2ab<=a^2+b^2` and `|a+b|^2<=2|a|^2+2|b|^2`. The resulting scalar bound is

\[
 {d\over dt}\mathbb E|e_t^\lambda|^2
 \le C_*\mathbb E|e_t^\lambda|^2
       +D_*\mathbb E|R_t^\lambda|^2,                        \tag{10}
\]

where one admissible pair of finite constants is

`C_*=2||A||+2||B|| L_F+1+2(||A0||+||B0|| L_F)^2`,

`D_*=||B||^2+2||B0||^2`.

Localization/Fatou justifies this estimate with only second moments; no unstated fourth-moment hypothesis is required. Since the initial error is zero, the integral Gronwall estimate gives

\[
 \mathbb E\int_0^T|e_t^\lambda|^2dt
 \le T D_*e^{C_*T}\mathbb E\int_0^T|R_t^\lambda|^2dt
 \longrightarrow0.                                         \tag{11}
\]

The normalized actual control minus tangent control is `Q^lambda+R^lambda`, hence also tends to zero in `L2(Omega x[0,T])`. The normalized output satisfies

\[
 z^\lambda/\lambda-z^{lin}
 =D_0e^\lambda+D_1(Q^\lambda+R^\lambda),
\]

so it tends to zero in `N2` on this finite observation interval, and therefore in **N1** by Cauchy–Schwarz. This is a finite-time convergence result with all actual drift/diffusion/input terms accounted for.

## 4. Passing the original literal gain bound, without exchanging infinite-time limits

If `G1(F)=infinity`, inequality(4) is vacuous, so suppose it is finite. The uniform induced-gain definition, applied to every legal scaled disturbance `lambda*w`, yields

\[
 N_1(z^\lambda;[0,T])/\lambda
 \le G_1(F)N_1(w;I_{input}),                                 \tag{12}
\]

where the right side uses the full original counted input interval: `[0,T-h]` on a fixed finite book horizon, or `[0,infinity)` for an infinite-horizon controller observed temporarily through `T`. Positive scaling preserves support and adaptedness, and `N1(lambda*w)=lambda*N1(w)`.

Take `lambda->0` in(12) using the just-proved finite-time `N1` convergence. This gives

\[
 N_1(z^{lin};[0,T])\le G_1(F)N_1(w;I_{input}).                \tag{13}
\]

For a fixed finite book horizon, taking the supremum over its actual counted input class proves(4) directly. For the infinite horizon, **first keep any fixed input `w` and apply(13) separately at each finite `T`**, then increase `T` and use monotone convergence of its pathwise output norm. The result is the full infinite-horizon literal bound for that input. Only afterward take the input supremum. No convergence of nonlinear/tangent trajectories uniformly over infinite time is asserted or needed.

Thus `G1(D)<=G1(F)`. Theorem B for the actual derivative law(3) then gives(5) on the infinite horizon. The finite-horizon reverse comparison from Theorem B is **not** asserted; the old finite gamma6 separation would forbid that extrapolation.

## 5. Consequential necessary condition and exact remaining gap

For this explicitly smooth stationary class, finite literal gain forces the existence of a deterministic stationary linear preview tangent with finite mean-square induced gain. In particular, if **no** state/tap/L2-window-kernel law of the prescribed information pattern has finite `G2`, then **no controller in this smooth nonlinear class** can have finite printed gain. More quantitatively, a printed gain below `gamma` forces its tangent to have `G2<sqrt(3)*gamma`, not necessarily below `gamma`.

This is a genuine bridge past fixed linear controllers, but it does **not** remove the regularity restrictions. An unrestricted nonexistence theorem would still have to handle nonsmooth, nonstationary and arbitrary-history laws without unjustified differentiation or superposition. Also, finite zero-state `G2` does not establish internal stability of unobservable modes; no stabilizability/detectability theorem has been silently imported to claim otherwise.

The proof mechanism is standard finite-time stochastic linearization plus the earlier candidate norm-comparison theorem; novelty remains UNCLEAR. This candidate supplies neither an optimal nonlinear controller nor an N&S criterion at a prescribed literal gamma. It is one scoped necessary-condition bridge for the same primary target, not a solved-book count. All claims remain written candidates pending actual separate reconstruction and full parent read; no scientific execution, formal kernel, external-model review or publication occurred.
