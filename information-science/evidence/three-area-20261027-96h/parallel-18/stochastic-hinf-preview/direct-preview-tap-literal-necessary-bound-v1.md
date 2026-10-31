# An unavoidable direct-tap bound for every bound linear preview law

**WRITTEN AUTHOR CANDIDATE — UNREVIEWED AND UNADOPTED.** Native prewrite observation: **Tue Oct 27 15:28:19 PDT 2026**. Continued original-object necessary-condition work with all supplied matrices/couplings and the original literal expectation of path norms. No new source, scientific evaluation, special numerical state or controller realization. All acknowledged process/STOP/HOLD/ZERO limitations remain.

## 1. Exact all-variable statement and h=0 boundary

Keep the full original plant and bound deterministic stationary linear preview class, every compatible finite real matrix, every H in L2, zero state/history, canonical progressive E2 input domain, finite T>h>=0 and S=T-h. Define actual output tap matrices

`J0=D1 L0`, `Jh=D1 Lh`.

For h>0 put `a_tap=||[J0;Jh]||`, the Euclidean operator norm of the vertically stacked matrix. For h=0 put instead `a_tap=||D1(L0+Lh)||`, because the endpoints coincide and must combine.

**Theorem.** For EVERY fixed law/plant in the bound class,

**G_prog >= G_det >= a_tap.**                                (1)

Therefore uniform-strict literal feasibility `G_prog<gamma` requires `a_tap<gamma`. Pointwise-strict feasibility for every individual input requires only the deducible condition `a_tap<=gamma`; no failure at the equality endpoint is claimed merely from (1). If a_tap>gamma, some actual deterministic disturbance already violates the criterion. These are fixed-law necessary conditions, not sufficient conditions or existential synthesis obstructions over all possible gains.

No observability, stabilizability, rank, invertibility, sign or state-noise condition is assumed. All A,B,C,A0,B0,D0,D1,K and kernel couplings are retained.

## 2. Paid actual mean caller, not a drift-only shortcut

The bound finite-horizon linear closed loop has E2 state and control for every progressive E2 input: substitute the law to obtain constant state coefficients `P=A+BK`, `Q=A0+B0K` and bounded progressive E2 feedforward terms. The permitted linear-SDE well-posedness/isometry estimate supplies strong nonexplosive solutions and the stated integrability. Hence for a deterministic v the actual stochastic integral has zero mean, justified by the simple-predictable integral and isometry approximation.

Let R be the original full preview operator and `N=D0+D1K`. Its ACTUAL mean output is

`M v(t)=N integral_0^t exp(P(t-s))[B Rv(s)+C v(s-h)]ds + D1 Rv(t)`.  (2)

Expectation of the original output norm obeys `E||z_v||>=||M v||`, by the expectation triangle inequality. This is a lower estimate for the printed criterion, not a replacement performance definition. Nonintegrable arbitrary local-control laws are outside this proved caller.

## 3. Compact dynamic/kernel terms cannot cancel both taps on all inputs

On the finite time intervals write E0v(t)=v(t), Ehv(t)=v(t-h), always zero-extended. The controller kernel operator

`(R_H v)(t)=integral_0^h H(r)v(t-r)dr`

has square-integrable matrix kernel on [0,T] x [0,S]; its squared kernel norm is bounded by S times the H squared norm. It is compact by finite separated-kernel approximation and Cauchy-Schwarz, as reconstructed in the current controller-interface proof. Endpoint operators are bounded, with norm at most one before their matrix factors.

The drift-state Volterra operator `f->N integral_0^t exp(P(t-s))f(s)ds` also has a square-integrable finite-horizon kernel and is compact. Its composition with the bounded operators B R+C Eh remains compact. Therefore (2) is EXACTLY

`M=J0 E0+Jh Eh+K_compact`,                                  (3)

with no omitted direct term or independent input/state choice. All noisy coefficients are still present in the physical model; they disappear only from the paid mean identity for deterministic inputs, not from the actual output distribution.

## 4. Both direct taps when h>0

Take ANY interval I strictly inside (0,S) of positive length less than h. Then I and I+h are disjoint and lie in [0,T]. Let e be a unit maximizing vector for the matrix [J0;Jh], and let phi_n be an orthonormal sequence in L2(I). The original deterministic inputs `v_n=e phi_n`, zero-extended, have norm one and are admitted E2 inputs.

The two direct terms in (3) have disjoint supports and their combined output norm is exactly

`sqrt(|J0e|^2+|Jhe|^2)=a_tap`.

The input sequence is weakly null in L2 and compactness gives `K_compact v_n->0` strongly. Thus `liminf ||M v_n||>=a_tap`. Applying the actual literal Jensen lower bound to every v_n and taking the full deterministic supremum proves (1). The state dynamics, kernel or feedback can cancel selected inputs but cannot cancel this entire universally quantified weak-null sequence.

This is an analytic all-sequence argument, not an executed frequency enumeration, chosen high-frequency diagnostic or claimed Boolean/finite witness. No bound on admissible input bandwidth was supplied or imposed.

## 5. Coincident endpoints and degeneracies

For h=0, R has no kernel and the two taps combine as L0+Lh. Formula (3) is `M=D1(L0+Lh)E0+K_compact`. The same weak-null argument with a maximizing vector of that matrix proves the stated h=0 bound. The stacked h>0 formula must NOT be used at h=0, where exact endpoint cancellation is possible.

If both tap products vanish, the bound is zero and makes no feasibility claim. Singular/zero D1 and arbitrary matrix ranks are included. If a_tap>gamma, the lower-limit argument gives an actual member of the deterministic sequence with ratio>gamma; if a_tap=gamma it gives no strict violation, so no endpoint conclusion is fabricated. A prescribed law can avoid this particular necessary bound by choosing zero taps; that does not make it feasible nor eliminate the other stochastic/dynamic requirements.

The bound does not assert that the gain or its optimum is continuous in preview h as h approaches zero; the admissible input interval and possible overlap of delayed taps change with h. The theorem compares the stated physical problems separately at each h and preserves all horizon/controller quantifiers.

## 6. Exact remaining gap and assurance

This is an explicit matrix necessary condition for the bound original-information controller class. It strengthens the paid deterministic-mean lower interface by identifying a noncancelable direct-tap contribution. It neither determines the complete mean operator norm nor G_det/G_prog, and does not solve general prescribed-gamma synthesis or certify that the original book intended this particular law class.

Named facts: admitted finite-horizon linear-SDE/isometry well-posedness and zero mean, expectation triangle inequality, boundedness/compactness of square-integrable-kernel operators, finite matrix norm attainment and weak-null orthonormal L2 sequences. No old proof/guide, new source, scientific execution, selected state/control probe, changed physical performance output, storage/Gramian or realization method is used. All source-equivalence, process and STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP boundaries persist; no review/adoption, formal/kernel, executable, human/configured-family or novelty gate is claimed passed.
