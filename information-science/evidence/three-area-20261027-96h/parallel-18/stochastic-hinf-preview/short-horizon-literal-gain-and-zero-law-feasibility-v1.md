# An all-matrix short-horizon literal threshold and a zero-law feasibility bound

**WRITTEN CONDITIONAL AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 16:45:23 PDT 2026**. Exact load-bearing current-author import: the first-moment martingale estimate in `general-linear-preview-literal-bound-and-continuity-v1.md`, SHA `48a51780b14540091b369e6d5f964f38a40c90c580699debd85e45f0a45e3302`, still pending NR-GAIN completion w65. No adoption/independent proof of that import is inferred. This is a class-level bound, not the STOPPED diffusion-annihilating-controller construction.

## 1. Exact general fixed-law short-time statement

Use ALL original compatible real matrices, positive dimensions, zero state/history and canonical progressive E2 disturbances. First set h=0 and keep ONE fixed law with combined tap L=L0+Lh (no kernel), arbitrary K, and the ORIGINAL output. Define

`P=A+BK`, `Q=A0+B0K`, `F=BL+C`, `G=B0L`,

`N_out=D0+D1K`, `J=D1L`.

The actual equation is `dX=(P X+Fw)dt+(Q X+Gw)dW`, `z=N_out X+Jw`. Matrices and law remain fixed as T varies; no controller or input is numerically chosen.

Let C_M be ANY finite constant paid by the named current martingale estimate `E sup |integral g dW|<=C_M E sqrt(integral |g|^2)`. Its exact symbolic beta/delta expression is provided in that source; no external BDG constant is imported here. Put

`a(T)=||P||T+C_M||Q||sqrt(T)`.

Whenever a(T)<1, define

`d(T)=||N_out|| [T||F||+C_M sqrt(T)||G||]/[1-a(T)]`.

**Conditional Theorem A.**

`||J|| <= G_det(T,0) <= G_prog(T,0) <= ||J||+d(T)`.          (1)

In particular BOTH literal gain limits as T decreases to zero equal ||J||. For prescribed gamma>0,

`there exists T0>0 such that EVERY 0<T<T0 has G_prog(T,0)<gamma`

holds iff **gamma>||J||**. This is a same-law uniform-strict short-horizon equivalence, not a general fixed-arbitrary-horizon synthesis test or pointwise endpoint assertion.

## 2. Actual expected-norm state estimate, no RMS denominator swap

All progressive E2 inputs have unique strong nonexplosive E2 state/control/output on each finite horizon by the permitted linear-SDE theorem. Apply the named first-moment estimate to the ACTUAL martingale part of the integral equation. Triangle/Cauchy-Schwarz in time give

`E sup_(0<=t<=T)|X_t|`

`<= (||P||T+C_M||Q||sqrt(T)) E sup|X| + sqrt(T)E||Fw|| + C_M E||Gw||`.

The maxima are integrable: the known E2 state makes the martingale integrand E2, and the imported maximum estimate pays its first moment. Absorbing a(T)<1 and multiplying by sqrt(T) gives

`E||X|| <= [T||F||+C_M sqrt(T)||G||]/[1-a(T)] E||w||`.

Thus the ORIGINAL output difference from its actual direct tap obeys

`E||z-Jw|| <= d(T) E||w||`.

The direct path operator J has exact literal and deterministic gain ||J||, with the same actual input norm on [0,T]. The triangle inequality proves the upper bound in (1) for every progressive input; the criterion itself remains expectation of a pathwise norm throughout.

For the lower bound, the ACTUAL deterministic-input mean output is `Jv` plus a finite-horizon compact Volterra state operator. The true control is E2, so the Itô term has zero mean. Take a maximizing matrix direction of J and an orthonormal weak-null input sequence in that direction; the compact term vanishes, leaving a deterministic mean-output lower supremum ||J||. Jensen gives the actual literal lower bound. This is the paid h=0 direct-tap argument, not a claim that a particular deterministic input must attain the full stochastic gain.

Since a(T)->0 and d(T)->0, (1) gives both limits and sufficiency for gamma>||J||. If gamma<=||J||, the lower bound prevents UNIFORM-strict feasibility at every T. At gamma=||J|| no general pointwise-strict conclusion is supplied. Zero J, zero state/output terms and every rank/sign case are included.

## 3. A universal short-horizon feasibility statement for u=0, ALL 0<=h<T

Return to any h>=0 with T>h and the original full matrices. The admissible explicit law u=0 does NOT cancel or remove A0 state noise; it simply uses no control. Its actual equation/output are

`dX=(A X+Cw(t-h))dt+A0 XdW`, `z=D0X`.

For this SAME law the forcing shift is pathwise L2-contractive regardless of h. Put

`a0(T)=||A||T+C_M||A0||sqrt(T)`.

The identical actual expected-norm argument, with no direct input diffusion forcing, proves

**G_prog(T,h;u=0) <= ||D0||T||C||/[1-a0(T)]**                 (2)

whenever a0(T)<1, UNIFORMLY for every 0<=h<T. No global state/control energy or internal EMS is assumed; finite-horizon linear well-posedness and zero control are enough.

Therefore, for EVERY original finite matrix tuple and every given gamma>0, there exists T0>0 such that the one legal stationary law u=0 meets the uniform-strict literal criterion for EVERY 0<T<T0 and EVERY 0<=h<T. The right side tends to zero analytically; no horizon, numeric state or control diagnostic is selected to test the claim.

This is an original finite-horizon local feasibility statement only. It does not solve a prescribed larger T, prove infinite-horizon feasibility, improve the optimum, authorize another controller-construction method or infer a source initial-state convention. If the original problem imposes additional nonlocal controller admissibility, that premise must still be stated separately.

## 4. Exact status, degeneracies and remaining gap

All original B,B0,D1 may be arbitrary in (2), because the actual control is zero, not because they were silently deleted from the source. A0 may be nonzero and completely unrestricted; no diffusion-annihilation equation or old construction is used. At zero C or D0 the upper bound is zero directly. At T<=h the adopted nonzero input interval is unavailable and no gain is defined here. The h=0 direct-tap theorem and the uniform-in-h zero-law estimate are separate exact scopes.

The substantive new bridge is a quantitative expected-path-norm small-time asymptotic and a source-class local feasibility guarantee; it is CONDITIONAL on the current M lemma, not new support for NR-GAIN. It does not replace the original criterion by RMS, solve arbitrary gamma/T synthesis or broaden the controller class. All old timing/cadence/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP and source-render/copyright controls persist.

No new source, source-page method, mixed-norm dual guide, realization/storage argument, selected numerical/control/boundary probe, scientific interpreter/CAS/enumeration/solver, model CLI or nested agent was used. Written only, with no peer/parent, formal/kernel, executable, human/configured-family or novelty acceptance.
