# Internal mean-square exponential stability of a GIVEN law, without a storage construction

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 17:09:05 PDT 2026**. Independent isometry/semigroup structural result. No controller is selected to annihilate noise; the direct diffusion-annihilating-controller construction remains NOT ADMITTED. This result does not import NR-GAIN, a Lyapunov/storage/Gramian theorem or any new source.

## 1. Actual homogeneous closed-loop property and condition

Fix all original real compatible matrices and one bound linear preview law. With disturbance/history identically zero its ACTUAL state/control/output are

`dX=P Xdt+Q XdW`, `P=A+BK`, `Q=A0+B0K`,

`u=KX`, `z=(D0+D1K)X`.

For this INTERNAL property only, allow every specified deterministic initial vector x0. This is not a change to the ZERO-initial performance ratio, and no ratio at zero disturbance is evaluated.

Assume the already given P is strictly stable and put

`k_P^2=integral_0^infinity ||exp(Pt)||^2dt`.

Suppose

**eta_0=||Q||^2 k_P^2 < 1.**                                (S)

No numeric matrix/parameter is evaluated. The test is sufficient, not necessary; Q may be nonzero and no equation for K is solved.

**Theorem.** There exists lambda>0 for which

`eta_lambda=||Q||^2 integral_0^infinity exp(lambda t)||exp(Pt)||^2dt<1`,

`M_lambda=sup_(t>=0) exp(lambda t)||exp(Pt)||^2<infinity`.

For EVERY initial x0 and EVERY t>=0 the actual solution satisfies

**E|X_t|^2 <= [M_lambda/(1-eta_lambda)] exp(-lambda t)|x0|^2.** (EMS)

Thus the given law has the explicitly defined full-state mean-square exponential stability property. Its homogeneous state/control/output expected squared energies are finite, with the displayed constants below. No first-moment martingale maximum lemma is required.

## 2. Existence of a strict decay weight is paid analytically

Ordinary finite Jordan theory for strictly stable P gives constants M,alpha>0 with `||exp(Pt)||<=M exp(-alpha t)`. Choose a symbolic positive upper weight below 2alpha; the resulting weighted squared semigroup norm is integrable and uniformly dominates all smaller weights. Dominated convergence at lambda=0 therefore makes eta_lambda converge to eta_0<1. For all sufficiently small positive lambda, eta_lambda<1, and the same semigroup bound makes M_lambda finite.

This is an all-parameter continuity proof, not a chosen boundary test, eigensolver or numerical scan of lambda. If Q=0, eta_lambda=0 and the same ordinary deterministic-semigroup conclusion applies as a GIVEN degeneracy, not a designed cancellation controller.

## 3. Exact actual-state second-moment inequality from Itô isometry

The allowed linear-SDE theorem gives the unique global-on-each-compact strong solution and finite continuous second moments. The actual deterministic-semigroup identity is

`X_t=exp(Pt)x0+integral_0^t exp(P(t-s))Q X_s dW_s`.

It follows from the original integral equation by deterministic-kernel approximation/Fubini and Itô isometry; substitution plus strong uniqueness identifies the actual state. It is not a stochastic-flow transformation or an imported storage certificate.

The deterministic initial term has zero mean cross product with the E2 Itô integral. The Itô isometry thus gives

`m(t):=E|X_t|^2`

`<= ||exp(Pt)||^2 |x0|^2 + ||Q||^2 integral_0^t ||exp(P(t-s))||^2 m(s)ds`.

Define `v(t)=exp(lambda t)m(t)` and `a_lambda(t)=||Q||^2 exp(lambda t)||exp(Pt)||^2`. The inequality becomes

`v(t)<=M_lambda |x0|^2+(a_lambda*v)(t)`.

On any compact [0,T], v is finite and continuous by the already paid local theory. Taking its finite supremum gives

`sup_[0,T]v <= M_lambda |x0|^2+eta_lambda sup_[0,T]v`.

Absorb eta_lambda<1. The resulting bound is independent of T, so it holds for every time and is exactly (EMS). There is no circular assumption of a global moment bound, and no exchange of the literal input denominator with a second-moment norm.

## 4. Actual eligibility consequences and a distinct necessary mean condition

Writing `C_lambda=M_lambda/(1-eta_lambda)`, ordinary integration gives

`E integral_0^infinity |X_t|^2dt <= C_lambda |x0|^2/lambda`,

`E integral_0^infinity |u_t|^2dt <= ||K||^2 C_lambda |x0|^2/lambda`,

`E integral_0^infinity |z_t|^2dt <= ||D0+D1K||^2 C_lambda |x0|^2/lambda`.

These are homogeneous internal-stability/energy properties, not the original disturbed performance gain. In particular a decaying but nonzero homogeneous output still cannot be charged to a disturbance-only denominator for all initial states; the earlier initial-compatibility result is not erased by EMS.

Conversely, if the homogeneous given law is EMS for every x0, its actual mean is `E X_t=exp(Pt)x0` by finite-prefix E2 zero mean of the Itô term. Jensen gives an exponentially decaying deterministic-semigroup norm, forcing P to be strictly stable. Thus P stability is a genuine NECESSARY condition for THIS internal property. The small norm (S) is only a sufficient noise condition, and P stability is not claimed necessary for finite INPUT/OUTPUT gain when unstable states are unobservable.

## 5. Relation to the current literal certificate and exact residuals

The current source `stable-semigroup-small-noise-literal-bound-v1.md`, SHA `9b60754d7a4ab9488a1f0b70b5b73e66c3361ea636a63e2370444b8604fba064` (UNREVIEWED), assumes the stronger condition max(1,C_M)k_P||Q||<1. That implies (S), so its given-law class also has the EMS property proved HERE independently of its conditional NR-GAIN first-moment import. No source bytes or prior assurance labels are changed. The literal performance estimate remains separately conditional on that first-moment gate.

This theorem pays an actual extra admissibility property if one explicitly adopts this EMS definition; it does not establish which convention the original source requires, construct a controller, solve arbitrary prescribed-gamma synthesis, prove necessity of the norm test, or replace the original criterion by RMS. Feedforward taps/kernel do not enter the zero-disturbance homogeneous equation; no unprovided controller memory states are inferred.

Named facts and uses are exactly finite-prefix linear-SDE well-posedness/isometry/zero mean, deterministic matrix semigroup/Jordan decay, deterministic-kernel approximation, dominated convergence and elementary nonnegative convolution inequalities. No stochastic support/flow/Gramian/Riccati/storage theorem, old guide, source-page method, parent physics-2 L1 material, scientific interpreter/CAS/enumeration/solver, selected diagnostic/model CLI or nested agent was used. All prior process/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP/source-render/copyright controls persist; written only, with no peer/parent, formal/kernel, executable, human/configured-family or novelty acceptance.
