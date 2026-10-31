# Exact finite-horizon literal synthesis for noise-only actuation

**WRITTEN AUTHOR CANDIDATE — UNREVIEWED, UNADOPTED.** Actual native prewrite clock: **Tue Oct 27 15:11:48 PDT 2026**. Continued work inside the standing info-3 definition-first releases and bound linear preview controller class. No new source or scientific execution. The previously disclosed late-ACK PROCESS MINOR and all old controls/findings remain.

## 1. Original-object class and theorem

Fix arbitrary positive dimensions n,m,p,q, finite h>=0 and T>h; put S=T-h. Use zero state/history, zero-extended progressive E2 disturbances on [0,S], the canonical Brownian filtration and the original literal expected-path-norm criterion. Let the ACTUAL plant be

`dx=[A x+C w(t-h)]dt+B0 u dW`, `z=D0 x`,                         (1)

where A,C,B0,D0 are arbitrary real matrices of their original compatible sizes. Thus the original matrices B,A0,D1 are zero; no rank, stability, invertibility, positivity or observability assumption is imposed on the remaining matrices.

The controller class is EXACTLY the bound deterministic stationary linear full-information class

`u=Kx+L0 w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`,

with finite real gains, H in L2, no extra Brownian history/private randomness, and the stated h=0 endpoint convention. All such laws are finite-horizon E2-admissible as verified below. The theorem does not strengthen the original unspecified controller domain and silently call that unrestricted synthesis.

Define the deterministic operator on the actual disturbance interval,

`(V_A v)(r)=D0 integral_0^r exp(A(r-s)) C v(s)ds`, `0<=r<=S`,

and `sigma=||V_A||_(L2([0,S];R^p)->L2([0,S];R^q))`.

**Theorem.** On the stated entire plant/controller class:

1. `inf_F G_prog(F)=inf_F G_det(F)=sigma`, and the single explicit stationary law **u=0** attains both infima.
2. For each prescribed gamma>0, a law meeting the original **pointwise-strict** criterion for EVERY nonzero progressive E2 disturbance exists iff **gamma>sigma**. The same condition is necessary and sufficient for uniform-strict feasibility `G_prog<gamma`.
3. When A=0, the condition is the explicit matrix inequality

   **gamma > [2(T-h)/pi] ||D0 C||**.                           (2)

The corresponding controller is u=0, not a controller selected separately for each disturbance. The result is literal expected-norm synthesis for this class, not a mean-square replacement. It coexists with the earlier fixed-law calibration failure: a bad fixed law need not be an optimal law.

## 2. Every bound controller is legally well posed on this finite horizon

Write the preview feedforward operator as Rw. Its time/probability L2 norm is bounded by

`||Rw||_E2[0,T] <= (||L0||+||Lh||+sqrt(h)||H||_L2) ||w||_E2[0,S]`.

This follows by zero extension, translation contraction, Minkowski and Cauchy-Schwarz on the deterministic kernel interval; R preserves progressive measurability. Substituting the actual law in (1) gives

`dx=(A x+C w(t-h))dt+(B0 K x+B0 Rw)dW`.

The explicitly permitted finite-horizon linear-SDE theorem applies: constant linear/Lipschitz state coefficients and progressive square-integrable forcing give a unique strong continuous nonexplosive solution with finite state second moments. An entirely explicit E2 estimate follows from the integral equation, Itô isometry and the elementary integral Gronwall bound, as in the current `linear-preview-class-robustness-addendum-v1.md` (SHA `575778fd8ce64721ebc4bbf653a88db1e4ba9e9b400469ed93709fc9d6ef63b0`, sections 2–3). Thus x, u=Kx+Rw and z have finite expected time-L2 energy on [0,T] for every admitted w.

This verifies the actual original progressive-input caller and, in particular, E2 control for all laws in THIS class. Nothing here asserts that arbitrary merely local pathwise-L2 controllers from a different source interpretation are E2 or have mean-zero stochastic integrals.

## 3. Lower bound valid for EVERY law in the bound class

Take ANY deterministic v in L2([0,S]) and ANY one law in the class. Because its control is E2, its actual Itô integral has zero mean. This fact follows from zero mean of simple-predictable Brownian-increment integrals and the Itô-isometry L2 approximation, not an unproved drift-only mean for a nonintegrable control.

Taking expectations in (1), with legitimate deterministic time integration, gives

`E x_t=integral_0^t exp(A(t-s)) C v(s-h)ds`.

The actual mean output is zero on [0,h] and, at t=r+h, equals V_A v(r). Jensen's inequality for the L2 norm (equivalently the expectation triangle inequality) gives

`E||z||_[0,T] >= ||E z||_[0,T] = ||V_A v||_[0,S]`.

Divide by the unchanged deterministic denominator ||v||. Since deterministic inputs are admitted progressive E2 inputs,

**G_prog(F)>=G_det(F)>=sigma for EVERY F.**                     (3)

This is the same common-law quantifier as the synthesis question. The expectation identity is paid by the proven control E2 property and contains no control contribution to the drift; neither assertion is inferred for a different plant/controller class.

## 4. Matching actual controller and all-input upper bound

Set K=L0=Lh=H=0, i.e. u=0. It is a deterministic stationary law with the exact original information restriction. The control-noise term vanishes, and for EVERY actual progressive E2 input the samplewise state is the ordinary deterministic convolution driven by that input path. The original output is zero on [0,h] and is V_A applied to the sample input on the remaining interval.

Thus `||z(omega)||_[0,T] <= sigma ||w(omega)||_[0,S]` almost surely. Taking expectations yields G_prog(u=0)<=sigma. Deterministic inputs, or (3), give the reverse inequality. The same argument identifies G_det(u=0)=sigma, proving theorem item 1 with the SAME actual u=0 for both callers.

No controller is reconstructed from an abstract optimizer, no state/output is changed, and no RMS performance equivalence is invoked.

## 5. Strictness at the exact finite-horizon endpoint

Finiteness of sigma follows from boundedness of the matrix exponential on [0,S] and the square-integrable convolution kernel. If gamma>sigma, u=0 satisfies a common strict margin and therefore the printed strict ratio for every admitted nonzero input.

To handle gamma=sigma rather than silently replacing pointwise strictness by a supremum condition, note that V_A is compact. Indeed its matrix kernel

`D0 exp(A(r-s)) C 1_(0<=s<=r<=S)`

is square-integrable on the finite square. Finite sums of separated step kernels approximate it in the square-integral norm. Their integral operators have finite rank, and Cauchy-Schwarz bounds the operator-norm error by the kernel's square-integral error. Thus V_A is an operator-norm limit of finite-rank operators.

A nonzero compact operator between these L2 Hilbert spaces attains its norm: choose unit inputs approaching the norm, extract a weakly convergent subsequence in the Hilbert unit ball, and use compactness for strong convergence of the images. The limit has norm at most one, image norm sigma, and must have norm one when sigma>0 (otherwise rescaling contradicts the definition of sigma). These are the precise standard L2 compactness/weak-unit-ball facts used.

Hence if sigma>0 there is one actual nonzero deterministic v_* with `||V_A v_*||=sigma||v_*||`. For EVERY law, (3)'s Jensen inequality at that same v_* makes the actual literal ratio at least sigma. Consequently no law meets pointwise strictness at gamma=sigma; smaller gamma also fail. If sigma=0 the prescribed gamma is positive, so u=0 is feasible. This proves item 2, including all zero/singular channels, without claiming the endpoint behavior of an infinite-horizon problem.

## 6. Exact closed form when A=0, with the norm inequality derived

Let N=D0 C. The operator is N times the Volterra integration operator on [0,S]. Its norm is

`||V_0|| = (2S/pi)||N||`.

Here is a proof rather than an imported synthesis formula. Put lambda=pi/(2S). For an absolutely continuous scalar y with y(0)=0 and y' in L2, the sharp inequality is

`integral_0^S |y|^2 <= lambda^(-2) integral_0^S |y'|^2`.

For smooth y, write y(r)=sin(lambda r)v(r). Direct differentiation gives

`integral_0^S (|y'|^2-lambda^2|y|^2) = integral_0^S sin^2(lambda r)|v'|^2 >=0`;

the boundary term `lambda sin(lambda r)cos(lambda r)|v(r)|^2` vanishes at both endpoints. The standard H1 approximation of functions with y(0)=0 extends the inequality to all such y. Applying it coordinatewise to y(r)=integral_0^r v(s)ds and then multiplying by N gives the upper bound `(1/lambda)||N||`.

If N!=0, choose an arbitrary unit right maximizing vector e for the finite matrix N and the symbolic deterministic input `v(s)=e cos(lambda s)`. The integral is `e sin(lambda r)/lambda`; both sin-squared and cos-squared integrals on [0,S] equal S/2. The ratio is exactly ||N||/lambda. This is an all-matrix analytic extremizer, not a chosen numerical test state or executed probe. If N=0 the norm is zero directly. This proves item 3, every matrix-rank boundary and the deterministic actual caller at its strict endpoint.

## 7. What is and is not established

This supplies a genuine same-controller synthesis condition and explicit optimal law for the whole stated finite-horizon noise-only-actuation matrix class, plus a closed-form criterion for its arbitrary-matrix A=0 subfamily. B0 and the available preview gains/kernel are unrestricted; the optimum is independent of them because their only state influence is a zero-mean E2 martingale and u=0 removes it.

The theorem does not address general drift control B, uncontrolled state diffusion A0, direct control output D1, arbitrary nonlinear/non-E2 legal controllers, infinite horizon, book-image equivalence or every original source quantifier. Removing those zero-matrix hypotheses changes the lower-bound/attainment argument and is not licensed by this result. General literal preview synthesis remains OPEN.

Named facts and exact use are given above: permitted linear-SDE well-posedness/linearity, Itô isometry/zero mean from its construction, Fubini/Tonelli with E2 integrability, expectation/norm inequalities, standard L2 kernel approximation/compactness and ordinary one-dimensional integration. No Riccati, storage/Gramian, stopped old realization method, new source, scientific program or numerical check is used. Same-harness written candidate status, NR-SOURCE and all STOP/HOLD/ZERO/process findings (including the acknowledged sequencing MINOR) persist; no peer/parent, formal/kernel, executable, human/configured-family or novelty acceptance is asserted.
