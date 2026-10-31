# Actual E1/E2 disturbance-domain equality for the bound linear preview class

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 15:22:25 PDT 2026**. Continued admitted all-variable work; no new source or execution. This pays a physical caller rather than merely completing an abstract normed space. Its load-bearing current-author import is `general-linear-preview-literal-bound-and-continuity-v1.md`, SHA-256 `48a51780b14540091b369e6d5f964f38a40c90c580699debd85e45f0a45e3302`; that source is itself UNREVIEWED, not an adopted premise or independent check. All process/exposure/STOP/HOLD/ZERO qualifications persist.

## 1. Precisely stated comparison domains

Keep every original matrix arbitrary, fixed positive dimensions, finite T>h>=0, S=T-h, zero state/history, the exact bound deterministic stationary linear full-information preview controller F, and the canonical Brownian filtration. Input representatives are progressive and zero outside [0,S]. Define

`E2 = {w: E integral_0^S |w|^2 < infinity}`,

`E1 = {w: E sqrt(integral_0^S |w|^2) < infinity}`.

The latter condition entails finite pathwise L2 energy almost surely. Both performance denominators are the SAME literal `E||w||`, not one squared version. The bound release adopted E2 for its original-object question; E1 here is an EXPLICIT COMPARISON domain. No claim that it is the actual book domain, or that unspecified original admissibility permits every constructed solution, is made.

Write `Z_F(w)` for the output of the original plant with the same F. The preceding general theorem supplies finite constants K_X,K_Z for all E2 inputs, with

`E||X_F(w)||_[0,T] <= K_X E||w||_[0,S]`,

`E||Z_F(w)||_[0,T] <= K_Z E||w||_[0,S]`.                       (B)

The original preview operator R also obeys the PATHWISE bound `||Rw||_[0,T]<=r_F||w||_[0,S]`, and is causal/progressiveness preserving. These exact facts, not a product-a.e. solution version, are the inputs to the extension.

**Theorem.** Every w in E1 has a unique nonexplosive strong local-square-integrable solution of the SAME bound linear closed loop, with control and output having finite expected pathwise L2 norm. It is the physical causal-localization limit of E2 solutions. Moreover

**G_E1(F)=G_E2(F)**,

where each gain is the supremum of `E||Z_F(w)||/E||w||` on that domain with positive denominator. The constants in (B) apply unchanged. No unrestricted nonlinear/local-only-controller conclusion is included.

## 2. Legal causal E2 approximations

For a given w in E1, keep its zero extension on [0,T] and define the genuine stopping times

`tau_N=inf{t in [0,T]: integral_0^t |w_s|^2 ds >= N} min T`,

with inf(empty)=infinity. Define the actual disturbance `w^N(t)=w(t)1_(t<tau_N)` on [0,S], zero elsewhere. The time-integrated energy is continuous, so `integral |w^N|^2<=N` pathwise, and w^N is progressive E2. This is an all-N analytic localization construction, not an executed enumeration or selected-energy test.

Because w has finite energy almost surely, tau_N is nondecreasing and equals T for all sufficiently large N on each such sample path. Importantly the stop is defined through T, even though w vanishes after S; if no input-energy threshold is hit, the stop is T, not prematurely S.

The pathwise bound `||w-w^N||<=||w||` and eventual equality on every finite-energy path give

`E||w-w^N|| ->0`

by dominated convergence. The input processes and their windows agree up to tau_N, not merely at separately fixed deterministic paths.

## 3. The SAME physical state/control, not an arbitrary Banach completion

Let X^N be the actual globally well-posed E2 solution for w^N. For M>=N, the two input processes coincide up to tau_N. Since the bound law uses only the current state and the past/current finite window, their forcing/preview terms also coincide there. Strong uniqueness for the linear SDE, localized if necessary, gives

`X^M=X^N on [0,tau_N]` almost surely,

and the same local identity holds for their controls and original outputs. One obtains this simultaneously for the countable sequence by intersecting the probability-one consistency events.

Consequently define X by patching these consistent actual stopped states. On each sample path, some finite N has tau_N=T, so the patched path coincides with a full continuous nonexplosive X^N on the whole horizon. Its control is exactly `u=KX+Rw`, is progressive and pathwise L2; its stochastic integral is the consistent localized Itô integral. Thus it satisfies the ORIGINAL SDE on the whole finite horizon with its actual input w. No extra information, time-dependent choice of controller or change of output is introduced. The localization index is a proof device, not a controller policy.

Uniqueness follows by the same stopped strong uniqueness: any other locally square-integrable nonexplosive solution with this fixed law agrees up to every tau_N (localize its state norm first if needed), hence agrees on [0,T]. This is not a claim of uniqueness for arbitrary unbounded nonlinear policies.

## 4. Identification of the expected-norm limit

The fixed linear closed-loop solution/output is linear on E2, by subtraction and strong uniqueness. Thus applying (B) to w^M-w^N gives

`E||Z_F(w^M)-Z_F(w^N)|| <= K_Z E||w^M-w^N|| ->0`.

The sequence is Cauchy in the ordinary Banach space L1(Omega;L2[0,T]); its limit is uniquely identified with the actual patched output, since the paths agree with it for all sufficiently large N almost surely. The corresponding state argument uses K_X. Therefore

`E||Z_F(w^N)-Z_F(w)|| ->0`, `E||X_F(w^N)-X_F(w)|| ->0`.

Passing (B) to the limit proves the same state/output literal bounds on E1. The control is also E1 because `E||u||<=||K||E||X||+r_F E||w||`; no expected squared control energy on E1 is assumed or concluded.

This pays the actual-object caller missing from a purely abstract completion: every limiting output is attached to the same original physical plant, Brownian input, causal window, state and fixed law.

## 5. Equality of gains and the exact strictness boundary

The inclusion E2 subset E1 gives G_E1>=G_E2. Conversely fix an E1 input with finite positive literal norm. Its E2 truncation norms tend to that positive norm, so they are positive for all sufficiently large N; output literal norms also converge by section 4. The actual ratios therefore converge to the E1 ratio, and every truncation ratio is at most G_E2. Taking the E1 supremum proves the reverse inequality and the theorem.

Hence uniform-strict feasibility `G<gamma` and nonstrict boundedness `G<=gamma` are unchanged by this domain comparison for each law, and likewise under an unchanged existential quantifier over the bound controller class.

**Do not silently strengthen this to endpoint pointwise strictness.** E2 pointwise ratios may all be strictly below gamma while their supremum is gamma; convergence only gives a nonstrict inequality for a newly admitted E1 input. No general E2-pointwise-strict -> E1-pointwise-strict implication at such an endpoint is proved here, and no physical example of its failure is claimed. E1 pointwise strictness implies E2 pointwise strictness; a common margin below gamma is sufficient in both domains.

For the separately proved noise-only/unobservable-channel synthesis classes, their threshold gamma>sigma also remains the exact POINTWISE-strict threshold on E1: the same u=0 pathwise bound supplies sufficiency; the compact deterministic-input norm-attainer already in E2 supplies endpoint necessity. This is a specific paid endpoint caller, not the unproved general implication above.

## 6. Scope, imports and the remaining original-target gap

The comparison is all-variable in the released finite-horizon linear preview class, including every matrix degeneracy and both h=0 and h>0. It changes neither the original information pattern nor the ratio. It does not extend the synthesis theorem to arbitrary nonlinear or merely local pathwise-admissible unknown laws, and it does not certify the book/source disturbance convention. Infinite horizon and a domain with no finite expected pathwise input norm are not covered.

Load-bearing imports are the fully pinned current-author literal-bound theorem (still UNREVIEWED), permitted strong linear-SDE uniqueness/existence on E2 localized to consistent stopping intervals, causality of the explicit bounded preview operator, dominated convergence and standard L1(L2) completeness/linearity. No old probability-buffer/cylinder/adjoint/realization guide, source outside the release, scientific computation or selected numerical test is used.

General prescribed-gamma synthesis outside the stated structural subclasses remains OPEN. All STOP/HOLD/ZERO, source-equivalence and process findings, including the acknowledged late-ACK PROCESS MINOR, N4 UNKNOWN historical exit and auxiliary214 STOP, persist. This is written only; peer/parent, formal/kernel, executable, human/configured-family and novelty/priority gates remain unpassed.
