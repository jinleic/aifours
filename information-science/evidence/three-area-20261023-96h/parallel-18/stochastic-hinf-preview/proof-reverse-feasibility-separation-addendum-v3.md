# Addendum v3 — explicit strict quadratic storage, with no Riccati import

Observed before creation: **2026-10-23T14:36:40-0700**, `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. Author: InfoHinfPreview. **Written candidate validation; separate/parent acceptance remains pending.** No scientific execution.

This belongs to the same reverse-separation packet: original manuscript SHA256 **33a3e60e43ef8e83f4351824fc708467728243a54846fda349350cabae10bb0f**, operative algebra correction **11922c3123990af68d812ab3d8a26dfe9449f6ee5868b3478986355ead1d36d8**, and finite-horizon extension **889ac912ab3dcd4ae6cd551f2b97739e80e53a512fa2c00aed6149d3880bfe3f**. It does not edit those snapshots, change the plant, or claim another independent result.

## 1. Certificate at a strict intermediate level

Use the same zero controller, same state `x=(f,y)^T`, actual delayed input `v_t=w(t-h)`, and parameters

`g=2^14=16384`, `epsilon=1/(2g^2)=2^-29`, `kappa=g^2=2^28`, `h=2^-29`, `gamma=g+2=16386`.

Take the strictly intermediate attenuation level

\[
 \eta=g+1=16385,\quad \alpha=\eta^2-g^2=2g+1>0,
\]

and the explicit diagonal positive storage

\[
 P=\operatorname{diag}(p_f,p_y),\qquad
 p_f={\eta^2\over\kappa}=1+2^{-13}+2^{-28},
 \qquad p_y={g^2+\eta^2\over2}=g^2+g+\tfrac12.               \tag{1}
\]

Both diagonal entries are positive exact rational numbers. No search, ODE solution, Riccati theorem or solver is hidden in their definition.

Under `u=0` the drift, diffusion and state-output matrices are

\[
 A=\begin{pmatrix}-\kappa&0\\0&-\varepsilon\end{pmatrix},
 \quad N=\begin{pmatrix}0&0\\1&0\end{pmatrix},
 \quad C_v=\binom\kappa0,\quad Z=(0\;1).
\]

Direct multiplication gives

\[
 A^TP+PA+N^TPN+Z^TZ
 =\operatorname{diag}(-2\kappa p_f+p_y,\;1-2\varepsilon p_y),
 \qquad PC_v=\binom{\eta^2}{0}.
\]

Consequently the complete input/state quadratic form of the strict bounded-real storage matrix is **exactly**

\[
\begin{aligned}
 &\begin{pmatrix}f&y&v\end{pmatrix}
 \begin{pmatrix}
 -2\kappa p_f+p_y&0&\kappa p_f\\
 0&1-2\varepsilon p_y&0\\
 \kappa p_f&0&-\eta^2
 \end{pmatrix}
 \begin{pmatrix}f\\y\\v\end{pmatrix}\\
 &\qquad=-{\alpha\over2}f^2
          -{\alpha\over2g^2}y^2
          -\eta^2(v-f)^2.                                  \tag{2}
\end{aligned}
\]

For verification in ordinary algebra: `kappa p_f=eta^2`, `p_y-eta^2=-alpha/2`, and `1-2epsilon p_y=1-p_y/g^2=-alpha/(2g^2)`. Expanding the square on the right of(2) reproduces its `f^2`, `fv`, `v^2` and `y^2` coefficients separately. All three weights are strictly positive. The quadratic form is zero only when `f=y=0` and `v=f=0`, so the displayed real symmetric matrix is **strictly negative definite**, not merely semidefinite on the realized trajectory.

## 2. The stochastic energy identity itself

For `V=p_f f^2+p_y y^2`, Itô's formula yields the exact differential identity

\[
\begin{aligned}
 dV_t+\big(y_t^2-\eta^2 v_t^2\big)dt
 &= -\left[{\alpha\over2}f_t^2
       +{\alpha\over2g^2}y_t^2
       +\eta^2(v_t-f_t)^2\right]dt\\
 &\quad+2p_y y_t f_t\,dW_t.                                \tag{3}
\end{aligned}
\]

This follows directly from `df=kappa(-f+v)dt`, `dy=-epsilon y dt+f dW`; the Itô correction is `p_y f^2dt`, precisely the term in(2). In particular the noise contribution is not discarded or replaced by deterministic dynamics.

Stop at bounded state and input-energy levels on a bounded deterministic time interval. The stopped martingale in(3) has zero expectation. Drop the nonnegative terminal storage and the nonnegative dissipative integral, then use localization/Fatou to obtain

\[
 \mathbb E\int_0^T y_t^2dt
 \le\eta^2\mathbb E\int_0^T v_t^2dt.                         \tag{4}
\]

All adapted square-integrable inputs are allowed; no deterministic-input restriction appears. On the finite horizon with input zero outside `[0,T-h]`,

`integral_0^T v^2=integral_0^(T-h) w^2`.

On the infinite horizon the full delayed and original input energies coincide. Increasing the deterministic terminal time in(4) and using monotone convergence therefore gives the correct mean-square input/output bounds in both regimes. Since the zero-control output is `z=(y,0)`, this is a full output bound at `eta=16385<gamma=16386`. The original isometry proof gave the stronger bound `G2<=g=16384`; the purpose of this addendum is a **fully explicit strict matrix/energy certificate**, not an improved gain.

For zero input, the same positive storage is strictly dissipative; the original direct `P=I` identity already proves exponential internal mean-square stability. Thus this certificate does not rely on treating an internally unstable system as admissible.

## 3. What this falsifies, and what it does not

The original candidate's all-controller literal lower bound is strictly greater than16386, while(1)–(4) exhibit a valid classical **quadratic mean-square storage certificate at the even stricter level16385**. Hence simply reading the quadratic bounded-real/Riccati objective as the printed `E sqrt(energy)` objective is invalid at the same gamma, even when a strict storage matrix can be displayed exactly. This conclusion does not depend on the correctness of any old unpublished preview Riccati candidate.

The standard stochastic bounded-real theory itself is not contradicted. I read the actual primary Damm–Benner–Hauth, *Computing the stochastic H-infinity-norm*, [arXiv1703.04440v1](https://arxiv.org/pdf/1703.04440), pp1–2, especially its §2 definition and Theorem2.2: its nonanticipating input norm is `sqrt(E integral |u|^2)` and its bounded-real theorem concerns that mean-square norm. Its theorem is **not imported** to establish(1)–(4); it is cited only to verify the true objective being compared. The 2014 preview sufficient theorem and 2020 discrete-time result remain non-imports.

No claim of novelty for quadratic storage or completion of squares is made. This additive certificate strengthens the auditability of the same counterexample packet and the source/criterion boundary. It supplies neither general literal synthesis nor an exact optimum, and it does not authorize a numerical or kernel replay.
