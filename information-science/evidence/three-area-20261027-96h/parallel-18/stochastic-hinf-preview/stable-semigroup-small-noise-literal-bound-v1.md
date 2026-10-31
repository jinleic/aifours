# An infinite-horizon literal certificate for a GIVEN full-matrix linear preview law

**WRITTEN CONDITIONAL AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 16:54:16 PDT 2026**. The literal first-moment part imports only the current author martingale lemma in `general-linear-preview-literal-bound-and-continuity-v1.md`, SHA `48a51780b14540091b369e6d5f964f38a40c90c580699debd85e45f0a45e3302`, still under NR-GAIN/w65. The separate E2/global-control argument does not depend on that lemma. This tests an ALREADY GIVEN law; it does not select gains or enter the NOT-ADMITTED diffusion-annihilating-controller construction.

## 1. Entire original matrix/law scope and analytic condition

Fix all compatible real original matrices, positive dimensions, finite h>=0, zero state/history and one supplied deterministic stationary linear preview law. Set

`P=A+BK`, `Q=A0+B0K`, `N_out=D0+D1K`,

`Rw=L0w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr`,

`r=||L0||+||Lh||+sqrt(h)||H||_L2`,

`f=||B||r+||C||`, `g=||B0||r`.

Use the combined tap and no kernel at h=0. All noise/feedback/feedforward/output couplings remain; Q and B0R may be nonzero. The physical closed loop is exactly

`dX=(P X+F w)dt+(Q X+G w)dW`, `z=N_out X+D1Rw`,

where `F=B R+C S_h`, `G=B0 R` and S_h is the original zero-extended delay.

Assume the GIVEN P is strictly stable and define exact analytic constants

`l_P=integral_0^infinity ||exp(Pt)||dt`,

`k_P=[integral_0^infinity ||exp(Pt)||^2dt]^(1/2)`.

They are finite by ordinary finite-matrix stable-semigroup decay. They are not numerically evaluated or defined as a storage/Gramian object. Let C_M be the constant of the named current first-moment martingale lemma. Require

**max(1,C_M) k_P ||Q|| < 1.**                               (S)

This is an explicit small-state-noise test on an already specified law, NOT the equation Q=0 and not a method for constructing a law satisfying it.

Define

`M2=(l_P f+k_P g)/(1-k_P||Q||)`,

`M1=(l_P f+C_M k_P g)/(1-C_M k_P||Q||)`.

**Conditional Theorem.** For every canonical progressive disturbance with finite expected squared energy on [0,infinity), the actual state/control/output are globally E2, and the ORIGINAL literal gain satisfies

**G_prog,infinity <= Gamma1 := ||N_out|| M1+||D1||r.**         (L)

Hence Gamma1<gamma is a sufficient uniform-strict literal-feasibility certificate for this SAME law and every input in the stated domain. No N&S claim or controller search/construction follows. Global expected-control energy is paid separately below, not inferred from the literal estimate or from zero noise.

## 2. Physical mild identity, not a stochastic-flow replacement

For each finite T the permitted linear-SDE theorem supplies the unique actual strong E2 solution. Its exact deterministic-semigroup identity is

`X_t=integral_0^t exp(P(t-s))Fw(s)ds`

`+ integral_0^t exp(P(t-s))[Q X_s+Gw(s)]dW_s`.                 (M)

This identity can be derived from the integral equation by deterministic time-kernel step approximation, ordinary Fubini and Itô isometry: on a finite square exp(P(t-s)) is bounded and all forcing/state terms are E2, so the approximations and time/integral interchange converge in L2. Substitution verifies the same original equation; strong uniqueness identifies the actual state. No stochastic-flow/Doss-Sussmann, Riccati, storage or controller-realization formula is imported.

## 3. Hilbert-output stochastic convolution estimate with exact import use

Take H_T=L2([0,T];R^n). For a progressive E2 vector forcing v_s, the stochastic convolution in (M) is the terminal H_T-valued integral with integrand

`a_s(t)=1_(s<=t<=T) exp(P(t-s))v_s`.

Its integrated squared H_T norm is bounded by `k_P^2 integral_0^T |v_s|^2ds`. The H_T integral is constructed by finite orthonormal output projections and ordinary scalar-Brownian Itô isometry; these projections converge in L2(Omega;H_T). For each finite projection the CURRENT finite-dimensional first-moment lemma gives

`E||terminal integral||_H_T <= C_M E sqrt(integral_0^T ||a_s||_H_T^2ds)`.

Pass to the Hilbert terminal limit by isometry/L2 convergence, without importing a Hilbert-space BDG theorem or a new constant. Thus

**E||stochastic convolution(v)||_[0,T] <= C_M k_P E||v||_[0,T].** (H1)

The ordinary Hilbert Itô isometry, proved by the same finite projections, independently gives the E2-time bound

**||stochastic convolution(v)||_E2[0,T] <= k_P ||v||_E2[0,T].**  (H2)

Every projection is an analytic limiting proof, not an executed dimension/frequency enumeration. All integrability for these finite-T steps is already paid by the actual finite-horizon solution.

## 4. Global E2 state and control, with no first-moment circularity

The deterministic convolution in (M) has pathwise L2 operator norm at most l_P, by the semigroup's L1 norm and Young/Minkowski. Use (H2) at v=QX+Gw, then the pathwise preview/shift bounds, to obtain

`||X||_E2[0,T] <= l_P f ||w||_E2[0,T] + k_P||Q|| ||X||_E2[0,T] + k_P g ||w||_E2[0,T]`.

By (S), the state term absorbs and `||X||_E2[0,T]<=M2 ||w||_E2[0,T]`, with a constant INDEPENDENT of T. Let T increase and use monotone convergence of squared energies. The consistent local actual solution is globally E2, and

`||u||_E2 <= (||K||M2+r)||w||_E2`,

`||z||_E2 <= (||N_out||M2+||D1||r)||w||_E2`.

This proves global expected-control admissibility for every input, rather than silently restricting a local-only control domain. It does not assert internal EMS for arbitrary nonzero initial states or any other unprovided source convention.

## 5. The ORIGINAL expected-path-norm gain is a separate estimate

Apply (H1), not (H2), to the actual finite-T identity (M). The state-noise term has

`E||QX+Gw|| <= ||Q||E||X||+g E||w||`.

Together with the deterministic convolution bound this gives

`E||X||_[0,T] <= l_P f E||w||_[0,T] + C_M k_P||Q|| E||X||_[0,T] + C_M k_P g E||w||_[0,T]`.

After absorbing (S), `E||X||_[0,T]<=M1 E||w||_[0,T]`. Prefix norms increase to their infinite norms, so monotone convergence yields the SAME inequality on [0,infinity). The original output equation then gives (L).

The E2 estimate was used to establish actual integrability/admissibility, not substituted into the literal input denominator. The literal inequality has E||w|| on both sides from (H1) itself. All forcing maps are causal on the same input/Brownian space; no deterministic-input calibration or independence assumption is used.

## 6. All boundaries and remaining original-target gaps

If Q=0 the estimates include that algebraic degeneracy, but no controller is chosen to make it zero; the direct diffusion-annihilating construction remains STOPPED. If g=0 or f=0 the corresponding term vanishes without division. Zero outputs/rank-deficient matrices and h=0/h>0 are included. The strict inequalities in (S) are required for this sufficient bound; equality or failure is NOT declared infeasible. Stability/size of the given P,Q are hypotheses, not universally necessary conditions.

For an arbitrary prescribed gamma, this supplies a genuine sufficient same-law infinite-horizon literal bound with actual global-control energy. It does not produce a controller, prove general N&S synthesis, settle the book's exact admissibility/stability convention or certify source equivalence. The first-moment part is CONDITIONAL on the current unreviewed M lemma/NR-GAIN gate; the E2-control part is independently paid by the displayed isometry argument.

Only current admitted definitions and ordinary matrix semigroup/Young/L2 facts plus the explicitly constructed isometry limits are used. No old private guide, source-page method, parent physics-2 L1 content, stopped realization/storage branch, scientific interpreter/CAS/enumeration/solver, selected state/control probe, external model or nested agent occurred. All prior process/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP and rights/render controls persist; written only, no peer/parent/formal/kernel/executable/human/configured-family/novelty acceptance.
