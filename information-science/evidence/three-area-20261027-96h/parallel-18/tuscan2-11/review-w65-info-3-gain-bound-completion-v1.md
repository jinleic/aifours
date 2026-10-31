# w65 — complete serial review of the literal progressive-gain bound and continuity; NR-GAIN completion

Reviewer **InfoRecursiveMDS18-2**, info-4. Author **InfoHinfPreview-2**, info-3. Same-track, disjoint-slot, same-harness SERIAL review. Actual native prewrite clock: **Tue Oct 27 16:33:52 PDT 2026**.

**VERDICT ON THE SUPPLIED CANDIDATE: NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE.**

**New finding counts: FATAL0 / MAJOR0 / MINOR0.** The previously missing **NR-GAIN is now reconstructed** at the supplied finite-horizon, progressive-E2, bound deterministic-linear-preview class. The w55 progressive-finiteness sufficiency and the optional finite/continuous/open upgrades are paid as stated below. w55's separate fiber CONTROL-affinity wording MINOR is NOT repaired or withdrawn by this bound.

This is not a full-information nonlinear synthesis theorem, a prescribed-gamma success, an infinite-horizon result, source-book authentication, original-target solution or novelty/stronger-verification claim.

## 1. Mandatory intake, complete reading and input identities

S0 was read completely first, then the frozen manifest `review-waves/w65-info-3-gain-bound-completion/manifest-v1.json`, SHA256 `077ee04e4e1f45f402fc3c19703b0e7f1827022b1a9120c6b86919511fc454f3`,68LF/5984B. The required pre-body exposure ACK was actually written at **16:30:51 PDT BEFORE any packet read or mathematical assessment**.

The sole packet, SHA256 `dfcb27281e0ef1f80e2a1a4ee97b076c14c060b3835c4a80cc122decdda49449`,693LF/74731B, was then read entirely in raw physical windows1-60,61-120,121-180,181-240,241-300,301-360,361-420,421-480,481-540,541-600,601-660,661-693. Every source ending was returned before assessment; no truncated long-line content was inferred.

Sources, with ORIGINAL line references used below:
- **S1:** original literal packet, SHA256 `888307a4a094bc5fa7aca45484334f8a12b75e9fb3e86259d81acf31cad629f3`,55LF.
- **S2:** parent method/status decision, `e84b09baef996c0e947d70aefa46dbe7802035aabd43a9336d0a8672987a9897`,12LF, binding status NOT proof.
- **S3:** my prior w55 return, `3a6471b751aa25fb5c1db4f88efedcdb0a474ea2d536e1722802bd9f856ebcfd`,130LF, context for the prior gap NOT proof of the bound.
- **S4:** mean-caller dependency, `cdc743b8f7b50ad7fd674a310beb23e22bab834aabacc640847acb08c002a869`,55LF.
- **S5:** convexity/fiber dependency, `1127ad2e08baeb152fc9e3f258fb69d71ef41c0d1ec2be4f63e0bc648b3e046d`,87LF.
- **S6:** initial-state dependency, `bbe0c0255b3cd42d0eae6a99622e78255254f62bd684f83f7e51eb0db58c70ea`,93LF.
- **S7:** endpoint/kernel obstruction dependency, `4181508388f1d87614db22302ae48ead68f9d5056bb10373e8cf9dfe1ecd0851`,65LF.
- **S8:** COMPLETE164LF candidate `general-linear-preview-literal-bound-and-continuity-v1.md`, SHA256 `48a51780b14540091b369e6d5f964f38a40c90c580699debd85e45f0a45e3302`.

No author contact, other source, old/held body, selected instance or scientific execution was used. My earlier w55 verdict/confidence is not a premise: the newly supplied S8 arguments and used callers are reconstructed here. The w38 selected-control and own post-v13 selected-graph findings/entire consumer ZERO remain permanent. No clean-cognition, blindness, exhaustive-history or independent-family claim is made.

## 2. Exact object and proof obligations

The candidate covers fixed finite dimensions and T>h≥0, zero initial state/history, progressive inputs with `E∫|w|²<∞` on [0,T−h], zero extension, and deterministic stationary K,L0,Lh,H with H∈L2([0,h]). Ratios use the EXPECTED PATHWISE L2 norm, with positive input denominator. At h=0 combine endpoints and omit the kernel.

The closed-loop matrices are P=A+BK, Q=A0+B0K and N_out=D0+D1K. The SAME original output is used. No stability, inverse, rank restriction, noise cancellation or new output is assumed. Continuity keeps dimensions, T and h FIXED; it does not identify changing input domains for variable preview length.

Permitted classical inputs are exact finite-horizon strong existence/uniqueness/linearity of the constant-coefficient linear SDE for progressive E2 forcing, ordinary Itô isometry, Fubini/Tonelli and standard L2 facts. The candidate does NOT simply quote a first-moment BDG estimate: that is the main step checked next.

## 3. First-moment martingale estimate — fully reconstructed

**S8 LF18-54.** Retain the candidate's arbitrary symbolic beta>1, delta>0 with `r=delta²/(beta−1)²` and beta r<1. Write c_M for its universal scalar `beta/[delta(1−beta r)]`, to avoid confusing it with the plant input matrix C. No numerical pair is selected or evaluated.

### 3.1 Conditional stopped isometry and weak maximal inequality

For a bounded stopping time tau, an event E∈F_tau, and a later bounded stopping sigma, the integrand `1_E 1_(tau<s≤sigma) g_s` has a predictable/progressive integral version and remains E2. Ordinary isometry gives the identity after multiplication by1_E; testing all E yields

`E[|∫_tau^sigma g_s dW_s|² | F_tau] = E[∫_tau^sigma |g_s|² ds | F_tau]`.

The stopped-integral identity follows from simple-predictable approximation in the isometry norm, not a separately imported optional-stopping theorem. These statements apply to the finite vector-valued martingale using squared Euclidean/Frobenius norms.

Stop the increment after at most v units of its integrated squared integrand and further at its first norm hit x. Continuity makes the stopped norm exactly x on the hitting event. Conditional isometry bounds its conditional second moment by v, so the conditional hitting probability is at most v/x². Horizon truncation only reduces the quadratic-integrand budget. This pays S8 LF32-38 without assuming a maximal theorem.

### 3.2 Good-lambda/tail coupling

For any lambda>0, on the event `M*>beta lambda` and `sqrt(A_T)≤delta lambda`, the first norm hit of lambda occurred. Thereafter the increment must reach norm at least `(beta−1)lambda`, while its remaining squared-integrand budget is at most delta²lambda². The preceding conditional bound is r. Multiplying by the F_tau-measurable first-hit event and integrating yields exactly

`P(M*>beta lambda)≤P(sqrt(A_T)>delta lambda)+rP(M*≥lambda)`.

The capped-time non-hit event is excluded as the source states; strict/weak tail distinctions are harmless only at the subsequent Lebesgue tail integral, not asserted as equality of all events.

First apply this to M stopped at its norm hit R. Its maximum is bounded, so tail integration and rearrangement do not presume the desired first moment:

`E M_R*/beta ≤ E sqrt(A_T^R)/delta + r E M_R*`.

Since beta r<1 and A_T^R≤A_T, this gives `E M_R*≤c_M E sqrt(A_T)`. By continuity `M_R*=min(M*,R)` and these maxima increase to M*; monotone convergence proves

`E M*≤c_M E sqrt(A_T)`.

E2 integrability makes the right side finite by Cauchy–Schwarz. The proof is symbolic for EVERY integrand and tail parameter, not a finite-field/state/time test, and it does not assume first-maximum integrability circularly.

## 4. Expected-path-norm linear-SDE bound — constants and absorption paid

**S8 LF60-82.** For `dX=(PX+f)dt+(QX+g)dW`, X0=0, the permitted linear-SDE theorem provides its actual E2 solution. The referenced unsupplied robustness addendum is not needed as a premise: directly, integral Cauchy–Schwarz/isometry gives an inequality of the form

`E|X_t|²≤c∫_0^t E|X_s|²ds+c∫_0^t E(|f_s|²+|g_s|²)ds`

for a finite c depending only on P,Q,T; elementary Gronwall/iteration gives finite state E2 norm. Thus all martingales below are E2. The just-proved maximum bound also makes the first maxima finite before absorption.

Choose an arbitrary integer N sufficiently large that Delta=T/N satisfies `a_N=||P||Delta+c_M||Q||sqrt(Delta)<1`, and let r_N=(1−a_N)^−1≥1. Existence is a symbolic limit argument, not a run over candidate partitions.

On each interval I_j, the initial endpoint is bounded by the preceding maximum. Drift Cauchy–Schwarz contributes `||P||Delta S_j+sqrt(Delta)E||f||_Ij`. The proved martingale estimate contributes `c_M||Q||sqrt(Delta)S_j+c_M E||g||_Ij`. This gives the exact displayed absorption and recurrence.

Iterating yields `S_j≤r_N^N Σ_k [sqrt(Delta)E||f||_Ik+c_M E||g||_Ik]`. Summing all N interval maxima, bounding the path L2 norm by sqrt(T) times the global maximum, and using pathwise `Σ||f||_Ik≤sqrt(N)||f||` proves the supplied loose bound

`E||X||≤D_N[sqrt(Delta)E||f||+c_M E||g||]`,

`D_N=sqrt(T)N^(3/2)r_N^N`.

All constants are finite for each fixed tuple. This is already the expected path norm; no RMS denominator conversion occurs.

## 5. All physical/preview terms and literal gain bound

**S8 LF88-116.** Zero extension and translation are L2 contractions. Minkowski and the finite-window inequality `||H||_1≤sqrt(h)||H||_2` give the PATHWISE bound `||Rw||≤r_theta||w||`, including all endpoint taps. Deterministic causal kernel approximation supplies a progressive version, so these are legitimate original-information inputs to the actual SDE.

Thus `f=Fw=(BR+CS_h)w`, `g=Gw=B0Rw` satisfy the stated pathwise f_theta,g_theta bounds. Substituting into §4 gives `E||X||≤M1_theta E||w||`. The ORIGINAL output `z=N_out X+D1Rw` then obeys

`E||z||≤(||N_out||M1_theta+||D1||r_theta) E||w||`.

Taking the unchanged nonzero progressive-E2 input supremum proves the finite literal G_prog bound. Restriction gives finite G_det as well. Every rank/sign/noise degeneracy is included. At h=0 the kernel is absent and combining the taps only improves the displayed upper bound. Zero output gives zero gain; no nonzero-channel inverse or zero-denominator ratio is used.

This proves the previously absent NR-GAIN input rather than treating mean output, a deterministic calibration or an RMS estimate as that input.

## 6. Full uniform literal operator continuity — reconstructed

**S8 LF120-156.** Fix arbitrary theta_* in the same dimensions/T/h. One partition N has a strict absorption margin at the reference, and the SAME N retains a strict margin in a neighborhood by continuity of P,Q. Thus D_N(theta) is locally bounded/continuous; no globally fixed N across all tuples is assumed.

The displayed delta_r bounds `R−R_*` pathwise. Expanding

`F−F_*=B(R−R_*)+(B−B_*)R_*+(C−C_*)S_h`

and the analogous B0 identity proves delta_F,delta_G exactly. Subtracting actual SDEs at the SAME w,W gives coefficients P,Q on the state difference and forcing `delta P X_*+delta F w`, `delta Q X_*+delta G w`. Every term is progressive E2. The reference expected-path bound and §4 prove the uniform D1_theta estimate on `E||X−X_*||`.

For the original output, use

`N_out(X−X_*)+(N_out−N_out,*)X_*+D1(R−R_*)w+(D1−D1_*)R_*w`.

The candidate's epsilon1_theta is exactly the sum of the four corresponding expected-path bounds and tends to zero. Hence EVERY admitted input satisfies `E||z_theta−z_*||≤epsilon1_theta E||w||` with a constant independent of w. Taking the supremum and using finiteness gives `|G_prog(theta)−G_prog(theta_*)|≤epsilon1_theta`; restriction gives the deterministic version.

This verifies continuity in the original matrix/gain/L2-kernel topology and openness of uniform-strict sets. It does not prove openness of merely all-input pointwise strictness with a supremum equal to gamma. No changing h/T domain, nonlinear controller or completion to all L1-only stochastic solutions is included.

## 7. Exact completion of the w55 dependencies

My resupplied w55 report is context, not evidence. The used dependency arguments give the following exact callers.

### 7.1 Initial-state finiteness sufficiency is now paid

For dependency S6, same-input/same-Brownian linearity splits output as NY plus the zero-initial output. If LY≡0 for the homogeneous SDE, conditional expectation of its increments and L2 continuity give LPY≡0; Itô isometry then gives LQY≡0. Iteration yields NWx0=0 for every word. Conversely the span of words of length≤n−1 stabilizes/increases to an invariant subspace; under (I), N annihilates it and uniqueness identifies the actual homogeneous solution in it. Thus `(I) iff NY≡0` is reconstructed from the supplied body.

If (I) fails, its continuous homogeneous output has positive expected norm and the arbitrary deterministic small-amplitude input family makes BOTH gains infinite. If (I) holds, the whole actual output map equals the zero-initial map. The newly proved S8 bound therefore makes its progressive gain finite, closing the previously unpaid sufficiency. This also completes the finite iff in S6 LF19-25/81 for BOTH input classes, without replacing the literal ratio. Zero x0, invariant hidden components, singular matrices, and the length-zero word boundary are preserved.

For one fixed law finite for EVERY deterministic x0, the length-zero condition forces N=0; then output D1Rw has the direct pathwise bound. That statement was already separately reconstructable and is consistent with the new general bound. It is not a book-imposed initial-state interpretation or a controller-construction theorem.

### 7.2 Optional convexity upgrades are now paid, with M1 retained

Dependency S5 fixes P,Q,N under fixed K (or its specified physical-product fiber). Actual same-w/W linearity gives the output-affine relation in R; pathwise triangle inequality and the common EXPECTED norm denominator give gain convexity and both strict-set convexities. The new bound makes the objectives finite, and §6 makes them continuous. Uniform-strict feasibility is therefore open, including relative openness on the affine fiber. This pays S5 LF59's optional upgrade.

It does NOT repair w55 M1: on the feedback fiber it is state/output/gain affinity/convexity that extends, not an unqualified assertion of joint actual CONTROL affinity. The physical-channel residual can vanish while the control difference itself need not. This remains a wording qualification from w55, not a new w65 mathematical finding.

### 7.3 Other dependencies are not promoted beyond their used scopes

The endpoint/kernel formula and its boundedness are directly reconstructed in §5. S4/S7's compact interior-tap obstruction is not needed to prove this gain bound; their bodies were completely read but no larger controller-realization theorem is inherited from them. The new estimate does not convert a mean-operator representation error into an infeasible synthesis claim, nor imply equality of deterministic and progressive gains.

## 8. Final disposition and ceilings

**S8 ALL164LF mathematical and application claims are reconstructed at their stated finite-horizon class. FATAL0 / MAJOR0 / MINOR0; NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE.**

The w55 **NR-GAIN is closed at this exact written scope**: general progressive zero-initial finiteness, the nonzero-initial sufficiency caller and optional finite/continuous/open upgrades now have a supplied reconstructed proof. The separate w55 fiber CONTROL-affinity wording MINOR remains. Source-book/controller-class equivalence, infinite horizon, sharp gain evaluation, prescribed-gamma N&S synthesis, broader abstract/nonlinear controls, and actual L1-only solution-domain completion remain unproved/out of scope exactly as the sources state.

S2's diffusion-annihilating construction branch remains NOT ADMITTED; this bound and serial review do not lift it or any original-source/method STOP. Main must read complete source/returns and disposition the union before adoption; no parent approval is asserted here.

Only this assigned output and mandatory pre-body ACK were written for w65. No selected numerical/dimension/plant/state/frequency case or sanity probe, other source, execution, calculator/Eval/CAS, solver/test/replay, author contact, nested task, modelCLI, Git, deletion or publication. All prior exposure and permanent PROCESS MAJOR/ZERO consumer boundaries, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist. My own primary is still STOPPED pending a separately frozen narrow separated release. Same-harness serial written review is not formal/kernel, human, configured-family/cross-vendor, executable, original-target solution or novelty acceptance.

**END OF COMPLETE w65 REVIEW.**
