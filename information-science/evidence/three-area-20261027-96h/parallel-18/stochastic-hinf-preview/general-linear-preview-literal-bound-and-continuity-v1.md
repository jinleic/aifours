# Every bound finite-horizon linear preview law has finite literal gain

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Native prewrite observation: **Tue Oct 27 15:18:29 PDT 2026**. Continued standing-S1 work on the original literal criterion. No new source or scientific execution; the late-ACK PROCESS MINOR and every old STOP/HOLD/ZERO/history boundary remain. The martingale estimate below is DERIVED from the admitted Itô isometry rather than imported as an unadmitted BDG theorem.

## 1. All original matrices and the exact result

Fix arbitrary positive dimensions, finite T>h>=0, zero initial state/history and zero-extended canonical progressive E2 disturbances on [0,T-h]. Use ALL real compatible original matrices A,B,C,A0,B0,D0,D1 and the entire bound deterministic stationary linear preview class, including K,L0,Lh and H in L2([0,h]). At h=0 use the combined endpoint tap and no kernel.

**Theorem.** For every such FIXED law/plant:

1. The original literal gain `G_prog=sup E||z||_[0,T]/E||w||_[0,T-h]` is finite, with the explicit symbolic upper bound below. The estimate is in the EXPECTED pathwise norm, not just an RMS estimate followed by an invalid denominator substitution.
2. Within fixed dimensions/T/h, the actual progressive-input/output operator is continuous in the original matrix/gain/L2-kernel tuple for this same expected-path-norm operator topology. In particular G_prog is continuous and its uniform-strict feasible sets `{G_prog<gamma}` are open. No openness claim is made for endpoint-only pointwise strictness with G_prog=gamma.

This supplies a general fixed-law literal boundedness/domain bridge for the released finite-horizon linear class, not a sharp gain formula, prescribed-gamma N&S synthesis, infinite-horizon result or source-book equivalence.

## 2. A universal first-moment martingale bound proved from isometry

Let `M_t=integral_0^t g_s dW_s` be any finite-dimensional continuous Itô martingale with progressive E2 integrand, let `M*=sup_(0<=t<=T)|M_t|` and `A_t=integral_0^t |g_s|^2 ds`. Choose ANY symbolic beta>1 and delta>0 satisfying

`r=delta^2/(beta-1)^2`, `beta r<1`,

and define the finite constant

`C=beta/[delta(1-beta r)]`.

Such pairs exist, without selecting or evaluating a numerical one. We will prove

**E M* <= C E sqrt(A_T).**                                   (M)

### 2.1 Conditional stopped isometry is paid, not assumed

For a stopping time tau<=T, bounded stopping of an integral after tau and an event E in F_tau, apply ordinary Itô isometry to the progressive integrand multiplied by `1_E 1_(s>tau)`. This tests the conditional second-moment identity against every E, proving the corresponding conditional isometry. Random stopping is justified by simple-predictable stopping approximations and isometry, as in the physical-gap proof; no optional-stopping theorem is imported.

Consequently a martingale increment started at tau and stopped after at most v units of integrated squared integrand satisfies

`P(sup |increment|>=x | F_tau) <= v/x^2`.

Indeed stop it further at the first norm hit of x. Continuity gives norm x on that hit; the conditional isometry bounds its stopped terminal squared norm by v. This proves the weak maximal bound using only the stated construction, including vector-valued martingales.

### 2.2 The tail coupling

Let tau_lambda be the first norm hit of lambda by M, capped at the horizon in the usual event-restricted argument. After that hit, stop again when the additional integrated squared integrand reaches delta^2 lambda^2. On the event

`{M*>beta lambda, sqrt(A_T)<=delta lambda}`,

there must be a post-tau_lambda increment with norm at least (beta-1)lambda before that latter stop. The conditional weak bound just proved is at most r. Multiplying by the event that the first hit occurred and integrating gives

`P(M*>beta lambda) <= P(sqrt(A_T)>delta lambda) + r P(M*>=lambda)`.

Replacing strict/weak inequalities on the final tail has no effect on its Lebesgue tail integral. First localize M at its first norm hit of R, so its maximum is bounded. Integrating the tail inequality over all lambda>0 yields

`E M*/beta <= E sqrt(A_T)/delta + r E M*`.

Rearrangement proves (M) for the localized process with the displayed C. Its integrated squared integrand is at most A_T. Let R increase to infinity and use monotone convergence of the localized maxima (the continuous martingale is finite on the compact horizon) to obtain (M) as stated. Thus no finiteness of the desired first maximum moment was assumed circularly. Brownian continuity, Itô isometry, measurable stopping and elementary integration/Markov inequalities are the only ingredients.

## 3. General linear-SDE estimate in the ACTUAL expected path norm

Consider

`dX=(P X+f)dt+(Q X+g)dW`, `X_0=0`,

with constant P,Q and progressive E2 f,g. The permitted linear-SDE theorem and the isometry/integral-inequality estimate already supplied in the current robustness addendum give an E2 state, so every integral used below is well defined. Applying (M) to its actual martingale part also gives finite first maxima, making the following absorption legitimate.

Choose an integer N large enough, put `Delta=T/N`, and require

`a_N=||P||Delta+C||Q||sqrt(Delta)<1`, `r_N=(1-a_N)^(-1)`.

Existence follows because both summands tend to zero as N increases; this is a symbolic partition argument, not an executed enumeration. For the j-th interval I_j of length Delta, write `S_j=E sup_(t in I_j)|X_t|`. The integral equation, the triangle inequality, (M), and Cauchy-Schwarz in time give

`S_j <= E|X_(left endpoint)| + a_N S_j + sqrt(Delta) E||f||_(L2(I_j)) + C E||g||_(L2(I_j))`.

Thus, with S_0=0 for the initial endpoint bound and interval numbering adjusted accordingly, the recurrence is

`S_j <= r_N S_(j-1) + r_N [sqrt(Delta) E||f||_(L2(I_j)) + C E||g||_(L2(I_j))]`.

For the first interval its endpoint term is zero. Iterating the nonnegative finite recurrence, bounding each power by r_N^N, summing the N interval maxima, and using the pathwise inequality `sum_j ||f||_(L2(I_j))<=sqrt(N)||f||_(L2[0,T])` (and the same for g) proves

`E||X||_[0,T] <= D_N [sqrt(Delta) E||f||_[0,T] + C E||g||_[0,T]]`,

`D_N=sqrt(T) N^(3/2) r_N^N`.                                (L)

The loose constant is finite; no sharpness is claimed. This estimate is already in the norm needed by the printed criterion and does not divide by a square-moment input norm.

## 4. Apply (L) to ALL original couplings and preview kernels

For each actual tuple theta put

`Rw=L0 w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`,

`r_theta=||L0||+||Lh||+sqrt(h)||H||_L2`,

`P=A+BK`, `Q=A0+B0K`, `F=B R+C S_h`, `G=B0 R`,

`N_out=D0+D1K`, where S_h is the original zero-extended shift.

The original plant/law, without any state/output replacement, is exactly

`dX=(P X+Fw)dt+(Q X+Gw)dW`, `z=N_out X+D1 Rw`.

The deterministic preview operators have PATHWISE L2 bounds

`||Rw||<=r_theta||w||`, `||Fw||<=f_theta||w||`, `||Gw||<=g_theta||w||`,

`f_theta=||B||r_theta+||C||`, `g_theta=||B0||r_theta`.

Minkowski/translation contraction/Cauchy-Schwarz prove the kernel bound, and all operators preserve progressiveness. Substituting f=Fw,g=Gw in (L) yields

`E||X|| <= M1_theta E||w||`,

`M1_theta=D_N [sqrt(Delta)f_theta+C g_theta]`.

Consequently the ACTUAL original criterion obeys

**G_prog(theta) <= ||N_out||M1_theta+||D1||r_theta < infinity.** (B)

Here C in the martingale/estimate constants is the universal scalar from section 2; C in the plant formulas is the original input matrix, distinguishable by its norm and matrix products. No matrix or control is selected for evaluation. Every finite dimension, sign, matrix rank, zero-output case and h=0/h>0 case is included.

## 5. Uniform literal operator continuity, without a fixed-input conversion factor

Fix a reference tuple theta_* in these same dimensions/T/h. Choose one integer N making a_N<1 at the reference. The SAME N continues to work in a neighborhood because P,Q depend continuously on the matrices/gains. The resulting D_N(theta) stays finite and continuous there.

Use star for the reference, and define the exact difference bounds

`delta_r=||L0-L0_*||+||Lh-Lh_*||+sqrt(h)||H-H_*||_L2`,

`delta_P=||P-P_*||`, `delta_Q=||Q-Q_*||`,

`delta_F=||B||delta_r+||B-B_*||r_*+||C-C_*||`,

`delta_G=||B0||delta_r+||B0-B0_*||r_*`,

`delta_N=||N_out-N_out,*||`.

Subtraction of the original SDEs at the SAME progressive input and Brownian motion gives the difference-state equation with coefficients P,Q and forcing

`f_diff=(P-P_*)X_*+(F-F_*)w`,

`g_diff=(Q-Q_*)X_*+(G-G_*)w`.

All are E2 by the allowed finite-horizon linear theory. Since the reference state already satisfies `E||X_*||<=M1_* E||w||`, (L) gives

`E||X-X_*|| <= D1_theta E||w||`,

`D1_theta=D_N(theta)[sqrt(Delta)(delta_P M1_*+delta_F)+C(delta_Q M1_*+delta_G)]`.

Subtracting the ORIGINAL outputs proves, for EVERY admitted progressive E2 input,

`E||z_theta-z_*|| <= epsilon1_theta E||w||`,

`epsilon1_theta=||N_out||D1_theta+delta_N M1_*+||D1||delta_r+||D1-D1_*||r_*`.

Each term tends to zero at theta_*. The domain of input processes is unchanged, and both gains are finite by (B); taking suprema gives

**|G_prog(theta)-G_prog(theta_*)|<=epsilon1_theta ->0.**        (C)

The deterministic gain has the same continuity conclusion by restriction to deterministic inputs. Unlike the earlier robustness proof's sufficient fixed-input conversion, (C) controls the whole progressive literal input/output norm uniformly. It is not inferred from RMS-operator continuity, which alone would not control the ratio of input norms in this problem.

## 6. Exact scope and residuals

The result supplies finite literal gain and uniform-strict feasibility openness for ALL bound finite-horizon original linear preview tuples. This improves the available domain/continuity interface; it does not compute G_prog sharply or turn the deterministic calibration into a sufficient test (the physical strict-gap candidate refutes that). It does not certify that any requested gamma is feasible or optimize over laws. Endpoint-only pointwise strictness with a supremum equal to gamma is not asserted stable under perturbation.

Only actual E2 progressive inputs are treated. An extension of the bounded linear operator to a completion of this expected-norm domain would require separate identification with physical locally square-integrable stochastic solutions; that unproved caller is NOT claimed here. Nonlinear controllers, infinite horizon, input/source convention changes and book-image equivalence also remain outside scope.

Every displayed step is written and symbolic. Named inputs are only the supplied definitions/current derivations and the allowed classical linear-SDE/isometry/Fubini/standard L2 facts; the first-moment martingale bound is proved rather than cited. No optional stopping, BDG source/constant, model CLI, scientific calculator/Eval/CAS/program/enumeration, special numerical control/state, held guide or old proof was used. All source/assurance limitations, STOP/HOLD/ZERO findings, N4 UNKNOWN historical exit and aux214 STOP persist. No peer/parent adoption, stronger verification or novelty is claimed.
