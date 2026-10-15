# Continuation: finite-memory P-local obstruction and compact-inverse boundary

Date: 2026-10-14 (America/Los_Angeles). These are written analytic proofs, not kernel certificates. Independent review and finite checks are recorded separately. No originality claim is made. The original broader nonlinear design question remains unresolved outside the explicitly defined learner class.

## 1. Frozen claim and information boundary

We study all real, stationary, constant-coefficient, finite-dimensional, pointwise-in-time linear error learners, not only a fixed-gain P update. Coefficients are independent of both physical time and trial index. With zero learner state, their trial-domain convolution is

\[
u_i(t)=\sum_{j=0}^{i-1}c_{i-1-j}e_j(t),\qquad C(z)=\sum_{k\ge0}c_kz^k,
\]

where `C` is a real rational function analytic at zero. The learner may have finite-dimensional internal memory with arbitrary real state matrices, including transfer-function poles on or outside the unit disk. This is strictly causal in trial index and completely local in physical time. It uses only previous output-error values at the same time; no error derivatives, state observations, plant cancellation, inverse, reset control, or reference feedforward are admitted. Constant-gain accumulation, fixed forgetting factors, momentum, and every constant-coefficient finite-history linear P rule with zero initialization belong to this class. Explicit iteration/time-varying gains, nonlinear dead zones, and anticipation do not.

The requested properties are (i) nominal uniform tracking for every feasible continuous-input target of the q-fold integrator from zero starts and zero learner state, and (ii) a bound uniform over arbitrary bounded trial-dependent initial shifts, at every fixed positive physical time. Property (ii) is weaker than the book's requested full-interval robust bound; failure of it suffices.

**Theorem D.** For every integer `q>=1`, no learner in this whole rational finite-memory class has both properties. This rules out all constant-coefficient finite-history linear P-local modifications at once. Theorem E below states exactly why a compact-inverse argument alone cannot rule out output robustness for more general learners.

## 2. Definitions to be used in the proof

Let `Jv(t)=integral_0^t v(s) ds`, `G=J^q`, and `y_i=a_i 1+G u_i`. Define `K(z)=z C(z)`. For a zero reference, the initial-shift-to-output generating function is

\[
H_q(z,t)=(I+K(z)G)^{-1}1(t)
       =E_q(-t^qK(z)),\qquad E_q(w)=\sum_{k\ge0}w^k/(qk)!.
\]

The identity initially holds in a neighborhood of zero; any use beyond that neighborhood must explicitly justify analytic continuation. Bounded-input/bounded-output stability for arbitrary initial shifts is equivalent at a fixed `t` to absolute summability of the scalar impulse coefficients of `H_q`, and hence implies continuous extension of its power series to the closed unit disk.

## 3. Proof of Theorem D

### 3.1 Nominal exactness forces a pole at one

Suppose robust initial-shift-to-output boundedness holds. At any fixed `t>0`, the output at trial `N` is a bounded linear functional of `(a_0,...,a_N)`. Its norm is exactly the partial absolute impulse sum `sum_{j=0}^N |h_j(t)|`. If these norms were unbounded, the uniform boundedness principle on the real Banach space `ell_infinity` would give one bounded infinite initial-shift sequence producing unbounded output. Thus robust boundedness, even without a specified common gain, implies `sum_j |h_j(t)|<infinity`.

The power series `H_q` consequently is analytic in the open unit disk and continuous on its closure. A pole of rational `K` inside the disk is impossible: `E_q` is a nonpolynomial entire function, and its composition with a pole has an essential singularity. The identity in Section 2 analytically continues from zero through the punctured disk; the putative singularity would have to be removable because `H_q` is analytic there, a contradiction. For completeness, a pole maps every sufficiently small punctured neighborhood onto the complement of a sufficiently large disk, with multiplicity; boundedness of the composition would bound `E_q` outside that disk. An entire function bounded there is bounded everywhere and hence constant by Liouville, which `E_q` is not.
Here the disk with the finitely many poles of K removed is connected, so the identity theorem supplies the stated continuation from zero.

Use just the feasible target `r(t)=t^q/q!`, whose required input is the constant one. Let `e_i` be its nominal errors, with zero initial states. If `e_i` tends uniformly to zero, its Banach-valued Abel means tend to zero:

\[
(1-z)\sum_{i\ge0}z^i e_i=(I+K(z)G)^{-1}r
 \ \longrightarrow\ 0,\qquad z\uparrow1.
\]

The generating identity follows near zero by convolution. The left side is analytic on the disk because a convergent sequence is bounded. The resolvent is an entire operator function of `K`, since `G` is Volterra and `||G^n||<=T^{qn}/(qn)!`; thus the identity continues to all real `0<=z<1`.

A rational function at one has either a finite limit or a pole. If `K(z)` has finite limit `kappa`, continuity of the Volterra resolvent gives limit `(I+kappa G)^{-1}r`, a nonzero function because the inverse is injective and `r!=0`. Therefore nominal tracking forces a pole:

\[
K(z)=a(1-z)^{-m}(1+O(1-z)),\quad m\ge1,\quad a\in\mathbb R\setminus\{0\}.
\]

This conclusion required only this single nonzero compatible reference, not an unbounded or finite-span family.

### 3.2 Every possible pole contradicts robust initial-shift boundedness

Fix any `t>0`. For `z=1-rho exp(i theta)` with `rho>0` small and `|theta|<pi/2`, the point lies inside the unit disk. Put `w=-t^q K(z)` and choose any root `v` satisfying `v^q=w`. Root-of-unity filtering gives the exact identity

\[
E_q(w)=\frac1q\sum_{j=0}^{q-1}\exp(v\exp(2\pi i j/q)).
\]

For `q>=2`, choose one fixed `theta` in the open interval so that the limiting argument of `w` is not one of the finitely many rays where two of its qth roots have equal largest real part, and, when `q=2`, is not the negative-real ray. Such a choice exists because `arg(w)` varies with nonzero slope `-m` as `theta` varies. A unique root then has strictly greatest real part, which is positive: at least one qth root has argument in `[-pi/q,pi/q]`, and the only zero-cosine case is the excluded `q=2` negative-real ray. Its real part tends to positive infinity as `rho^{-m/q}`. The remaining exponentials are smaller by an exponential factor tending to zero, so `|E_q(w)|` tends to infinity. The lower-order Laurent terms perturb root angles by `o(1)` and cannot remove the strictly positive angular gap. This contradicts boundedness of `H_q` on the closed disk.

For `q=1`, `H_1=exp(-tK)`. If `a<0`, the radial path already makes its modulus tend to infinity. If `a>0` and `m>=2`, choose `|theta|<pi/2` with `cos(m theta)<0`; the leading real part of `-tK` is positive, so the modulus again tends to infinity.

The sole remaining case is `q=m=1`, `a>0`. Write

\[
K(z)=\frac{a}{1-z}+b+O(1-z),\qquad a,b\in\mathbb R.
\]

Along the real radius, `H_1` tends to zero. But fix `h>1/2` and take `z_R=1-1/(h+iR)`. Exactly

\[
|z_R|^2=1+\frac{1-2h}{h^2+R^2}<1,\qquad
|H_1(z_R,t)|\longrightarrow\exp[-t(ah+b)]>0.
\]

Thus there is no continuous boundary value at one. Absolute summability fails in this last case as well. QED.

### 3.3 One adversarial sequence, nonlinear plants, and MIMO

For every nominally exact learner in this class and every prescribed `t_*>0`, the argument implies unbounded norms of the finite initial-shift response functionals; therefore **one** bounded infinite real sequence `(a_i)` gives `sup_i |y_i(t_*)|=infinity`. Rescaling gives any prescribed positive bound on initial shifts. The theorem does not rely on a different adversary for every finite trial horizon. Zero process and measurement noise suffice. In particular it defeats a claimed guarantee for arbitrary persistent bounded disturbances; no stochastic assumptions or averaging are available.

The class of smooth nonlinear book plants contains this linear witness. There are also genuinely nonlinear coordinate witnesses, with no model cancellation by the learner: set `g(x)=x+alpha sin(x)`, `0<alpha<1`. At degree one use `dot x=u/g'(x)`, `y=g(x)`; at degree q>1 use `dot x_1=x_2/g'(x_1)`, `dot x_j=x_{j+1}` for `2<=j<q`, and `dot x_q=u`, `y=g(x_1)`. Then `y^(q)=u` exactly, the nominal relative degree is q, and starts `(g^{-1}(a_i),0,...,0)` have physical magnitude at most `|a_i|/(1-alpha)`. This is a global smooth coordinate change, not a feedback cancellation or an inverse used by the controller. These plants are forward complete on each finite trial for every continuous trial input.

The scalar theorem refutes a universal theorem for nonlinear/MIMO plants if SISO plants are included. It does not claim that every matrix-valued rational learner on every MIMO plant has the scalar obstruction; that stronger matrix classification has not been proved here.

### 3.4 What fixed forgetting gains and loses

For the admissible P-local law `u_{i+1}=rho u_i+ell e_i`, with `|rho|<1`, one has `K(z)=ell z/(1-rho z)` and finite `K(1)=kappa=ell/(1-rho)`. On any q-integrator, the iteration operator `A=rho I-ell G` has spectral radius `|rho|<1`; hence its powers are summable in operator norm, and arbitrary bounded additive output traces yield bounded inputs and outputs. Explicitly choose `lambda>0` with `beta=|rho|+|ell|lambda^{-q}<1`. In the weighted sup norm, `||G||_lambda<=lambda^{-q}`, so for zero reference and disturbances `||d_i||_infinity<=delta`, zero learner initialization gives

\[
\|y_i\|_\infty\le e^{\lambda T}
\left(1+\frac{|\ell|\lambda^{-q}}{1-\beta}\right)\delta.
\]

This covers arbitrary initial-state polynomials, process disturbances, and measurement noise once their combined output bound is called `delta`; no independence or mean-zero hypothesis is used.

But nominal tracking has the exact nonzero residual

\[
e_\infty=(I+\kappa G)^{-1}r,\qquad
r(t)=t^q/q!,\qquad
e_\infty(t)=
\begin{cases}
(1-E_q(-\kappa t^q))/\kappa,&\kappa\ne0,\\
t^q/q!,&\kappa=0.
\end{cases}
\]

The whole function is nonzero, even if an isolated endpoint happens to vanish. Thus fixed forgetting is a genuine robust P-type modification, but cannot supply zero-uncertainty exact tracking. Theorem D proves this is not cured by replacing it with any other fixed finite-dimensional linear memory filter in the stated class.

## 4. Theorem E: the compact inverse limits robust input reconstruction, not output tracking alone

Take `G=J^q:L_infinity[0,T] -> C[0,T]`. Suppose arbitrary reconstruction maps `R_n:C[0,T] -> L_infinity[0,T]` satisfy

1. `||R_n(f)||_infinity<=M||f||_infinity` for one finite M, every n, and every feasible `f=Gu`;
2. `||G R_n(Gu)-Gu||_infinity ->0` for every `u` in `L_infinity`.

The maps need not be linear, stationary, causal, P-type, or continuous. **No such family exists.**

**Proof.** For fixed u the sequence `R_n(Gu)` is norm bounded. The unit ball of `L_infinity` is weak-star sequentially compact here because `L_1[0,T]` is separable. Take a weak-star convergent subsequence with limit v; weak-star lower semicontinuity gives `||v||<=M||Gu||_infinity`. The integral kernel at every fixed t is in `L_1`, so `G R_{n_k}(Gu)(t)` tends to `Gv(t)`. Nominal consistency also makes this limit `Gu(t)`. Repeated integration is injective: peel off the absolutely continuous antiderivatives and use their almost-everywhere derivatives, obtaining `v=u` almost everywhere. Therefore

\[
\|u\|_\infty\le M\|Gu\|_\infty\quad\hbox{for every }u.
\]

This is false. For `0<h<=T`, take `u_h=1_{[T-h,T]}`. It has input norm one but `||Gu_h||_infinity=h^q/q!`. Let h tend to zero. QED.

The same contradiction holds even when the consistency requirement is restricted to continuous inputs: replace `u_h` by the terminal ramp, zero until `T-h` and `(t-T+h)/h` afterwards. Its norm is one and its output norm is `h^q/(q+1)!`.

**Sharp information statement.** On an admissible input class `U`, any exact reconstruction map with perturbation Lipschitz constant M must satisfy

\[
\|u-v\|_\infty\le M\|G(u-v)\|_\infty\quad(u,v\in U).
\]

Conversely this inequality makes the exact inverse on `G(U)` M-Lipschitz, simply by defining `R(Gu)=u`; it is an information-theoretic necessity and sufficiency, not a claim that this inverse is an admissible P controller or extends Lipschitzly off `G(U)`. If a uniformly Lipschitz family of consistent reconstruction maps is asserted instead, apply the weak-star argument to their differences to obtain the same necessary inequality. This needs boundedness at one datum (for instance `R_n(0)=0`) to extract limits of the individual sequences.

For a nonzero noise radius delta, any two inputs satisfying `||G(u-v)||<=2 delta` are indistinguishable under deterministic bounded additive output noise: both may yield the midpoint observation. Any single estimator then has worst-case input error at least `||u-v||/2`. Terminal pulses and ramps show why unrestricted input reconstruction cannot be uniformly noise-stable.

**Boundary of the conclusion.** The original target asks for an output-error bound, not a Lipschitz inverse or an input-to-data gain bound. Arbitrarily large inputs can have arbitrarily small outputs. Therefore Theorem E is not a general impossibility theorem for the book problem. Unlike an unjustified compactness argument, Theorem D directly proves output failure, but only for its stated rational stationary P-local class.
