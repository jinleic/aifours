# The literal adapted/deterministic gap persists on an open full-law neighborhood

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 15:06:45 PDT 2026**. Append-only substantive continuation of `linear-preview-class-derivation-v1.md`, SHA-256 `13ad2a5613c767a5bc68a018bdfb47858ba3bd7ff235229f8bace4490ede54a1`. Its process-MINOR timing disclosure and every source/assurance limitation remain. No new source, scientific execution, selected probe, changed output or controller realization is used.

## 1. Statement and non-substitution of the criterion

Fix any one member of the ENTIRE symbolic counterfamily in the preceding proof, with its finite T>h>=0 and stopped-input family. No numerical member is selected. The present result proves that its strict fixed-law gap is not confined to exactly zero A,A0,B,K,D1 or exactly vanishing delayed/kernel controller coefficients: it survives an open neighborhood of the whole scalar plant/law tuple, including the L2 preview kernel.

The perturbation estimate is in expected squared L2 **only as a continuity tool**. The gains being compared remain exactly `E||z|| / E||w||`; the conversion factor for the fixed actual adapted input is carried explicitly. No equality to an RMS gain is asserted.

We first give the estimate for every compatible fixed matrix dimension. A tuple theta consists of the seven original matrices, K,L0,Lh and H. Dimensions, T and h are fixed. Norms of finite matrices are Euclidean operator norms; the kernel norm is `(integral_0^h ||H(r)||^2 dr)^(1/2)`, equivalent to the supplied finite-matrix L2 convention. At h=0 the kernel is absent and the two endpoint gains combine, with the same estimates still valid if their two norms are retained as an upper bound.

## 2. Explicit closed-loop operators and well-posedness

Let `S_h w(t)=w(t-h)` with the original zero extension, and put

`R_theta w(t)=L0 w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`,

`r_theta=||L0||+||Lh||+sqrt(h)||H||_L2`.

Zero extension, the triangle inequality and the deterministic L1-kernel/L2 convolution bound give `||R_theta w||_E2[0,T]<=r_theta ||w||_E2[0,T-h]`; also ||S_h||<=1. The convolution estimate itself follows by Minkowski and translation contraction, followed by Cauchy-Schwarz `integral ||H||<=sqrt(h)||H||_L2`. These inequalities hold pathwise first and then in E2. The deterministic past-window kernel of a progressive input is progressive, by measurable time integration and zero extension; no future input is queried.

Define the ACTUAL closed-loop coefficients/operators

`P_theta=A+BK`, `Q_theta=A0+B0K`,

`F_theta=B R_theta+C S_h`, `G_theta=B0 R_theta`,

`N_theta=D0+D1K`.

Then the original plant and law are exactly

`dX=(P_theta X+F_theta w)dt+(Q_theta X+G_theta w)dW`,

`Z=N_theta X+D1 R_theta w`, `u=KX+R_theta w`.                 (1)

This is direct substitution, not a new state/output or a controller realization. Named allowed linear-SDE existence/uniqueness gives a unique strong continuous, nonexplosive finite-horizon state for each progressive E2 w: constant P,Q and progressive E2 forcing satisfy its global linear/Lipschitz and integrability hypotheses. The estimates below establish E2 state, output and control. Hence the original actual-input caller is secured for every tuple in this fixed finite-dimensional/kernel class, not only deterministic inputs or a product-a.e. version.

## 3. An explicit state bound from isometry and an elementary integral inequality

Write `||Y||_2=(E integral_0^T |Y_t|^2dt)^(1/2)` and `||w||_2=(E integral_0^(T-h)|w_t|^2dt)^(1/2)`. For the linear equation with arbitrary progressive E2 drift/diffusion forcing f,g, its integral form, the inequality `|sum_(i=1)^4 v_i|^2<=4 sum_i |v_i|^2`, and Itô isometry give

`E|X_t|^2 <= alpha integral_0^t E|X_s|^2ds + 4T ||f||_2^2+4||g||_2^2`,

`alpha=4(T||P||^2+||Q||^2)`.

The elementary integral Gronwall bound (obtained by iterating this nonnegative integral inequality and summing the exponential series) implies, after integration over 0<=t<=T,

`||X||_2 <= J(P,Q) sqrt(T||f||_2^2+||g||_2^2)`,

`J(P,Q)=2sqrt(T) exp(2T[T||P||^2+||Q||^2])`.                (2)

If needed the argument first applies on localization intervals and then passes by monotone bounds; the allowed linear-SDE theorem already supplies finite second moments. No martingale maximal/BDG, measure-change or storage theorem is used.

For each tuple define finite bounds

`f_theta=||B||r_theta+||C||`, `g_theta=||B0||r_theta`,

`M_theta=J(P_theta,Q_theta) sqrt(T f_theta^2+g_theta^2)`.

Thus `||X_theta(w)||_2<=M_theta||w||_2`. This also gives E2 control/output through (1) with no additional admissibility restriction.

## 4. All-coupling difference bound

Let theta_* be any fixed reference tuple in the same dimension, with state bound M_*. A star on a matrix denotes its reference value, not the plant's matrix B0. Write

`delta_r=||L0-L0_*||+||Lh-Lh_*||+sqrt(h)||H-H_*||_L2`,

`delta_P=||P_theta-P_*||`, `delta_Q=||Q_theta-Q_*||`,

`delta_F=||B||delta_r+||B-B_*||r_*+||C-C_*||`,

`delta_G=||B0||delta_r+||B0-B0_*||r_*`.

These last two numbers bound the actual E2 operator differences F_theta-F_* and G_theta-G_*. Subtracting the original closed-loop equations gives a linear SDE for Delta X with homogeneous coefficients P_theta,Q_theta, drift forcing `(P_theta-P_*)X_*+(F_theta-F_*)w` and diffusion forcing `(Q_theta-Q_*)X_*+(G_theta-G_*)w`. Every forcing is progressive E2, so (2) yields

`||Delta X||_2 <= D_theta ||w||_2`,

`D_theta=J(P_theta,Q_theta) sqrt( T(delta_P M_*+delta_F)^2 + (delta_Q M_*+delta_G)^2 )`.

Let `delta_N=||N_theta-N_*||`. Subtracting the original outputs, without changing either output definition, gives

`||Z_theta(w)-Z_*(w)||_2 <= epsilon_theta ||w||_2`,             (3)

`epsilon_theta=||N_theta||D_theta + delta_N M_* + ||D1||delta_r + ||D1-D1_*||r_*`.

Every term is finite and tends to zero when the original matrices/K/taps converge in their ordinary norms and H converges in L2 to the reference. Thus epsilon_theta->0. The statement is quantitative for the actual shared Brownian motion/input, not a topological assertion inferred from separate deterministic solution versions.

## 5. Literal gain conversion and open strict-gap family

Now take theta_* from the preceding scalar counterfamily, with its proved deterministic upper U and actual adapted lower L>U. Put `Delta=L-U>0`. Fix ANY one of its whole symbolic inputs `w_*=q 1_(t<tau_a) 1_(t<S)` with q>0. Its same canonical Brownian stopping rule is used for the perturbed physical system; its admissibility is independent of the plant/law tuple.

The input has

`||w_*||_2 / E||w_*|| = sqrt(E(tau_a min S)) / m_(a,S) <= a/m_(a,S)=:R_*<infinity`.

No value of m_(a,S) is evaluated, and its strict positivity was proved in the core packet. From (3), for EVERY deterministic input v,

`E||Z_theta(v)|| <= E||Z_*(v)|| + epsilon_theta ||v||`,

so **G_det(theta)<=U+epsilon_theta**. For the fixed ACTUAL adapted input, (3) and Cauchy-Schwarz give

`E||Z_theta(w_*)||/E||w_*|| >= L-epsilon_theta R_*`.

Consequently every tuple satisfying

**epsilon_theta (1+R_*) < Delta**                             (4)

has **G_prog(theta)>G_det(theta)**, with the same literal finite-horizon criterion. The interval between the displayed deterministic upper and adapted lower is still nonempty. Since epsilon_theta->0 at theta_*, (4) contains a nonempty open neighborhood of theta_* in the full product topology of ALL scalar original matrices, K,L0,Lh and H in L2. The estimate does not require an algebraic constraint such as A0=0, B=0, D1=0 or K=0 in that neighborhood.

For fixed h>0 this includes nonzero delayed gains and nonzero kernels of arbitrarily small L2 norm; for h=0 it is the corresponding endpoint-gain class with no kernel. The physical nonzero c,b,d,ell of the core can also be kept nonzero by shrinking the neighborhood. The state-diffusion coefficient A0, feedback K, control drift B and direct output D1 may vary freely within it. Every perturbed law remains one deterministic stationary original-information law for all its inputs.

## 6. Scope, boundaries and continuation limit

This is an open-family robustness strengthening of a fixed-law counterexample to universal deterministic-input calibration. It is NOT existential synthesis impossibility, an exact gain formula, a general N&S condition, an infinite-horizon claim or a uniform-in-T/h perturbation estimate. The topology keeps T and h fixed; the core proof supplies starting families for every finite h. The difference bound remains valid for zero coefficients/outputs; only the strict-gap consequence needs Delta>0 and a nonzero fixed input denominator. No bound divides by a potentially zero plant coefficient.

All calculations are symbolic written inequalities. The only named classical imports are the explicitly permitted finite-horizon linear-SDE existence/uniqueness/linearity, Itô isometry and Tonelli/Minkowski/Cauchy-Schwarz standard L2 facts; the elementary integral inequality is proved as indicated. No source, execution, selected evaluation or hidden controller/energy route is added. NR-SOURCE/book equivalence and NR-SYNTHESIS remain; all old STOP/HOLD/ZERO/history findings, including the late-ACK PROCESS MINOR, persist. Main/peer review, formal/kernel, human/configured-family, executable and novelty acceptance have not occurred.

The released universal fixed-law equality has now been refuted and the obstruction continued to a nontrivial open full-law family. A materially different next synthesis task requires Main's binding of its actual criterion/controller quantifiers; I do not convert this fixed-law refutation into a self-released general synthesis or a stronger claim about every law.
