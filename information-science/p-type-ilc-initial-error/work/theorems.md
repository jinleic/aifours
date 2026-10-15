# Scoped theorems: the pure-P obstruction and a filtered value-error benchmark

Date: 2026-10-14 (America/Los_Angeles). This is an analytic proof, not a kernel-checked formalization. Independent review and numerical checks are recorded separately. No novelty claim is made.

## 1. Contract and notation

The book uses `r` for the input dimension. Here `p` is the input dimension and `q` is the (integer) relative degree, to avoid confusing them. A trial is on `[0,T]`, `T>0`. The nominal plant is

\[
\dot x=f(x,t)+B(x,t)u,\qquad y=g(x,t).
\]

Assume sufficient smoothness to define relative degree, local Lipschitz continuity in `x`, and forward existence for the inputs under discussion. Let `D_f h=∂_t h+∂_x h f`. For a SISO output, relative degree `q` means

\[
\partial_x(D_f^j g)B=0\quad(0\le j\le q-2),\qquad
b_q=\partial_x(D_f^{q-1}g)B\ne0.
\]

For multiple outputs use a constant vector relative degree `(q_1,...,q_m)` and the full-row-rank decoupling matrix with rows `∂_x(D_f^{q_a-1}g_a)B`; assume a bounded right inverse on the relevant domain. For `q=1`, the decoupling matrix is `g_x B` (the linear-system `CB`). For `q>=2`, `g_x B=0`; a condition `||I-CBL||<1` is therefore unavailable. These are nominal definitions: bounded nonsmooth disturbances need not themselves admit output derivatives.

The actual trials obey

\[
\dot x_i=f(x_i,t)+B(x_i,t)u_i+\eta_i(t),\qquad y_i=g(x_i,t)+\xi_i(t),
\]

with `||x_i(0)-x_d(0)||∞<=ε0`, `||η_i||∞<=εη`, and `||ξ_i||∞<=εξ`, uniformly in `i`. In the theorems here, disturbances are continuous on each trial and may vary arbitrarily between trials; no stochastic assumptions are needed. The original research target may also admit bounded measurable disturbances, but that extension requires Carathéodory solutions and essential-sup norms rather than undefined integrals of arbitrary bounded functions. The desired nominal trajectory must be feasible for a continuous nominal input `u_d` and initial state `x_d(0)`.

The requested robustness property is boundedness for all trials plus

\[
\limsup_{i\to\infty}\|y_d-y_i\|_\infty
 \le c_0\epsilon_0+c_\eta\epsilon_\eta+c_\xi\epsilon_\xi,
\]

where constants are independent of the disturbance sequence and trial number. When all bounds are zero the tracking error must converge to zero. The weighted norm `||e||λ=sup_{0<=t<=T} exp(-λt)|e(t)|`, with one fixed finite `λ`, is equivalent to the sup norm, so it cannot cure unboundedness. The physical-output error differs from the measured error by at most `εξ`.

Controller classes must not be conflated:

* **P0 (the book's displayed law):** `u_{i+1}(t)=u_i(t)+L e_i(t)`, constant finite matrix `L`, no reset control.
* **P-local extensions:** bounded time/iteration-varying pointwise gains, forgetting, dead zones, finite histories, or explicitly specified initial-error rectification. Each needs its own theorem; P0 impossibility is not a theorem about all such extensions.
* **P-value/nonlocal extension:** derivative-free processing of the whole previous error trace by an integral/basis filter. This is not the book's pointwise P law. The positive benchmark below belongs here and additionally uses known state feedback.

Neither derivatives of a measured error, derivatives disguised by exact inversion, nor controlled resetting of an allegedly arbitrary initial state may be silently admitted as P0.

## 2. Theorem A: no strict Banach contraction for pure P on a strictly proper plant

Let the linear input-output operator on `C([0,T];R^p)` be

\[
(Gv)(t)=\int_0^t K(t,s)v(s)\,ds,
\]

with a continuous bounded kernel. For a continuous pointwise gain `L(t)`, both `GL` (output space) and `LG` (input space), when dimensionally defined, are Volterra operators. Continuity is needed to keep both operators on `C([0,T])`; a merely bounded discontinuous gain need not do so. Their spectral radii are zero. Spectra below are taken on the complexifications of these real Banach spaces. Consequently

\[
\sigma(I-GL)=\{1\},\qquad \|I-GL\|\ge1
\]

in every equivalent Banach norm, including every fixed `λ`-norm. The analogous statement holds for `I-LG`.

**Proof.** If the norm of the composite kernel is at most `M`, iterating the triangular integral gives

\[
\|(GL)^n\|_\infty\le (MT)^n/n!.
\]

The spectral-radius formula gives radius zero. Zero belongs to the spectrum: a Volterra operator is not onto `C([0,T])`, since every image vanishes at zero. Spectral mapping gives the assertion for `I-GL`. Equivalent norms do not change invertibility or spectrum, and an operator norm bounds the spectral radius. The same conclusion holds on the nonzero compatible subspace `{e:e(0)=0}`: the restriction is quasinilpotent and cannot have an empty spectrum. Thus merely deleting the initial value does not produce a contraction. QED.

For a `C^1` nonlinear input-output map along a fixed feasible trajectory with fixed initial state, its Fréchet derivative is `Gv(t)=g_x(x_d(t),t)∫_0^t Φ(t,s)B(x_d(s),s)v(s)ds`, where `Φ` is the variational state transition matrix (including the derivative of `B u_d`). The input-space P0 learning map is `u ↦ u+L(y_d-F(u))`, with derivative `I-LG`. Therefore it cannot be a strict local contraction in an equivalent norm: its derivative at the fixed point has spectral radius one.

**Limit of the theorem.** Spectral radius one does NOT prove divergence, rule out nongeometric convergence, or apply unchanged to nonlocal/anticipatory/derivative learning. It specifically invalidates a strict-contraction proof for an identity-minus-Volterra iteration.

## 3. Theorem B: bounded arbitrary initial shifts can cause unbounded output for every integer relative degree

For any integer `q>=1`, any `T>0`, any nonzero real scalar learning gain `ell`, and any `ε0>0`, consider the chain of integrators

\[
\dot x_{i,j}=x_{i,j+1}\;(j<q),\quad \dot x_{i,q}=u_i,\quad y_i=x_{i,1},
\]

with `y_d=0`, `u_0=0`, `x_i(0)=(a_i,0,...,0)`, `|a_i|<=ε0`, and no process or measurement disturbance. Under P0, `u_{i+1}=u_i-ell y_i`, there is one bounded real sequence `(a_i)` such that

\[
\sup_i |y_i(t_*)|=\infty
\]

at any prescribed `t_*∈(0,T]`. Hence the robustness property fails in both the sup and every fixed `λ`-norm. The plant has smooth globally Lipschitz drift, relative degree `q`, unit decoupling gain, and complete finite-horizon solutions. No failure of controllability or rank is being exploited.

**Proof.** Let `Jv(t)=∫_0^t v(s)ds`, so `y_i=a_i 1+J^q u_i`. With `V=I-ell J^q`,

\[
u_i=-\ell\sum_{j=0}^{i-1}V^{i-1-j}(a_j1),
\qquad y_i(t)=\sum_{j=0}^i h_{i-j}(t)a_j,
\]

where `h_0(t)=1` and `h_n(t)=-ell J^q V^{n-1}1(t)` for `n>=1`. These are real polynomials in `t`.

For complex `|z|<1`, the generating function is

\[
H_q(z,t)=\sum_{n=0}^\infty h_n(t)z^n
 =\left[(I+\frac{\ell z}{1-z}J^q)^{-1}1\right](t)
 =E_q\left(-\frac{\ell t^q z}{1-z}\right),
\]

where `E_q(w)=Σ_{k>=0} w^k/(qk)!`. The inverse exists by Volterra quasinilpotence. The identity is initially obtained near zero by geometric series and extends throughout the unit disk analytically. Equivalently, it follows by taking the `q`th time derivative and the zero-derivative initial conditions of `H_q`.

We show `Σ_n |h_n(t_*)|=∞`. Absolute summability would make `H_q(·,t_*)` continuous on the closed unit disk, in particular at `z=1`.

* If `ell<0`, let `z` tend to one along the real radius. The argument of `E_q` tends to positive infinity, and its nonnegative power series is unbounded.
* If `ell>0` and `q=1`, the real radial limit is zero. Set `z=iR/(1+iR)`, `R>0`. Then `|z|<1`, `z→1`, `z/(1-z)=iR`, and `|H_1(z,t_*)|=1`. There is no common limit.
* If `ell>0` and `q=2`, on the real radius `H_2(z,t_*)=cos(t_* sqrt(ell z/(1-z)))`, which has no limit.
* If `ell>0` and `q>=3`, put `R=t_*(ell z/(1-z))^{1/q}` on the real radius. Root-of-unity filtering of the exponential power series gives
  
  \[
  E_q(-R^q)=\frac1q\sum_{j=0}^{q-1}\exp(R e^{(2j+1)\pi i/q}).
  \]
  
  The conjugate terms at angles `±π/q` have strictly largest real exponent, so
  
  \[
  E_q(-R^q)=\frac2q e^{R\cos(\pi/q)}\cos(R\sin(\pi/q))
       +O(e^{c_q R}),\quad c_q<\cos(\pi/q).
  \]
  
  Along `R=2πk/sin(π/q)` the main term grows without bound. Thus continuity at one fails.

Now regard `F_i(a)=Σ_{j=0}^i h_{i-j}(t_*)a_j` as bounded real linear functionals on the Banach space `ell∞(N)`. Their norms are exactly `Σ_{n=0}^i |h_n(t_*)|`, which are unbounded. The uniform boundedness principle, by contrapositive, supplies one bounded real `a` for which `sup_i |F_i(a)|=∞`. Scale this sequence to satisfy `|a_i|<=ε0`. This is a single infinite disturbance sequence, not merely a different maximizing sequence for every horizon. QED.

For `ell=0`, choose the feasible target `y_d(t)=t^q/q!`, nominal input `u_d=1`, zero initial states, and `u_0=0`. Actual outputs remain zero, disproving zero-uncertainty convergence. Therefore no constant scalar P0 gain meets the full specification for this class.
The exact quantifier in the nonzero-gain result is `for every t_*>0 there exists a bounded sequence a`; the sequence may depend on `t_*`. No simultaneous divergence at all positive times is claimed.

### Finite witnesses and what they do not establish

For any finite horizon `N`, choosing `a_j=ε0 sign(h_{N-j}(t_*))` for `0<=j<=N` gives exactly

\[
y_N(t_*)=\epsilon_0\sum_{n=0}^N |h_n(t_*)|.
\]

These finite witnesses are easy to reproduce, but by themselves are not a single infinite divergent sequence; the proof above closes that quantifier gap. For `q=1`, one may compute `h_n=L_n(ell t)-L_{n-1}(ell t)` using the Laguerre recurrence, with `h_0=1`. Constant initial error also gives `u_i(0)=-ell i a`, but that input divergence alone would not prove output divergence. The theorem deliberately proves the stronger output claim.

## 4. Theorem C: a derivative-free filtered benchmark for all relative degrees

This is a restricted positive result, not a solution for all book plants or for P0. Assume a known, fully measured, SISO feedback-linearizable normal form without internal dynamics:

\[
\dot x_j=x_{j+1}+\eta_j\;(j<q),\qquad
\dot x_q=a(x,t)+b(x,t)u+\eta_q,\quad y=x_1+\xi,
\]

with `a,b` continuous on all of `R^q × [0,T]` and locally Lipschitz in `x`, `|b|>=b_min>0` globally, and exact state measurement for the feedback cancellation (the bounded `ξ` is on the output channel used for learning). Apply `u=b^{-1}(v-a)`. A local normal form would instead require a separately established common compact containment inside its domain; bounded coordinate values alone do not imply that containment.

Choose `d` fixed linearly independent continuous input basis functions `φ_k`, set `ψ_k=J^q φ_k`, `ψ=(ψ_1,...,ψ_d)^T`, and `v_i=φ^T θ_i`. The reference is required to satisfy the finite-dimensional realizability assumption

\[
y_d(t)=p_d(t)+\psi(t)^T\theta_d,\quad
p_d(t)=\sum_{j=1}^q x_{d,j}(0)t^{j-1}/(j-1)!.
\]

Define `W=∫_0^T ψ(t)ψ(t)^Tdt`, and use the derivative-free whole-trace update

\[
\theta_{i+1}=\theta_i+\gamma W^{-1}\int_0^T\psi(t)(y_d(t)-y_i(t))dt,
\qquad 0<\gamma\le1.
\]

This is an integral learning filter on error values. The actual physical input additionally contains the stated state feedback; it does not obey P0.

Let

\[
\delta=\epsilon_0\sum_{j=1}^q\frac{T^{j-1}}{(j-1)!}
       +\epsilon_\eta\sum_{j=1}^q\frac{T^j}{j!}+\epsilon_\xi,
\quad
\kappa=\max_{t\in[0,T]}\int_0^T|\psi(t)^TW^{-1}\psi(s)|ds.
\]

Then `W` is positive definite, all coefficient and state sequences are bounded, and for every arbitrary disturbance sequence satisfying the bounds,

\[
\|y_d-y_i\|_\infty\le
(1-\gamma)^i\|\psi^T(\theta_d-\theta_0)\|_\infty
 +(1+\kappa)\delta.
\]

In the zero-uncertainty case,

\[
y_d-y_i=(1-\gamma)^i\psi^T(\theta_d-\theta_0).
\]

For `γ=1`, nominal tracking is obtained after one update. If realizability fails by a residual `r=y_d-p_d-ψ^Tθ_d`, the same proof bounds tracking by the nominal term plus `(1+κ)(δ+||r||∞)`; it cannot claim exact tracking in that case.

**Proof.** Repeated integration of the canceled chain gives

\[
y_i=p_d+\psi^T\theta_i+d_i,\quad
d_i=\sum_{j=1}^q\Delta x_{i,j}(0)t^{j-1}/(j-1)!
         +\sum_{j=1}^q J^j\eta_{i,j}+\xi_i.
\]

Consequently `||d_i||∞<=δ`. Linear independence of the `φ_k` and injectivity of `J^q` imply independence of the `ψ_k`, so `W` is positive definite. With `b_i=W^{-1}∫ψ d_i` and `a_i=θ_d-θ_i`,

\[
a_{i+1}=(1-\gamma)a_i+\gamma b_i.
\]

The finite-rank projection `Pd(t)=ψ(t)^TW^{-1}∫ψ(s)d(s)ds` has sup-norm operator norm `κ`. Writing `ρ=1-γ`, the exact identity is `e_i=ρ^i ψ^T a_0+γ Σ_{k=0}^{i-1}ρ^{i-1-k} P d_k-d_i`. Its norm is at most `ρ^i ||ψ^T a_0||∞+[1+κ(1-ρ^i)]δ`, which implies the stated bound. Coefficients are bounded by the finite-dimensional recurrence, virtual inputs by continuity of the basis, and all chain states by finite-horizon integration and the bounded initial/disturbance data. Because `a,b` are globally defined and continuous, they are bounded on the resulting common compact state-time set; the lower bound on `|b|` then bounds the physical inputs. QED.

### Concrete nonlinearity for the simulations

* `q=1`: `dot x=0.3 sin(x)+u+η`, `y=x+ξ`; `g_x B=1`.
* `q=2`: `dot x1=x2+η1`, `dot x2=0.3 sin(x1)+0.2 sin(x2)+u+η2`, `y=x1+ξ`; `g_x B=0`, `D_f g=x2`, and the relative-degree-two decoupling gain is one.

The filtered controller uses exact state feedback to cancel the displayed nonlinear terms. Simulations must also integrate the uncancelled physical equations independently to verify that the coordinate reduction is implemented consistently. Comparison with P0 cannot be called a matched-information optimality result, since the filtered controller has more model/state information.

## 5. What remains unresolved

Theorem B completely refutes a universal robustness guarantee for the exact displayed constant-gain P0 law. Theorem C shows how one explicit relaxation avoids its obstruction, but depends on a finite-dimensional realizable target, an exactly known normal form, and full-state feedback. It is not a general output-only, model-light, local P-type solution under arbitrary bounded trial-varying initial shifts and noise. Neither additional random trials nor finer simulation can bridge those information and controller-class differences. A claimed full positive solution must specify which restriction is relaxed and prove a disturbance-to-output bound without assuming control of the initial state or a false Volterra contraction.
