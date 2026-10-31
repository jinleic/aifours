# w95b — generic observable-noise short-horizon calibration gap

Reviewer **PhysicsResearch96h-2 / physics-1**. **SAME-HARNESS WRITTEN REVIEW ONLY**, not formal/kernel, human/configured-family, executable, novelty or original-target acceptance. Actual pre-body ACK: **Tue Oct 27 17:34:12 PDT 2026**. Native observation before writing: **Tue Oct 27 17:38:15 PDT 2026**.

## 1. Exact verdict

**NO SUBSTANTIVE DEFECT AT THE EXACT STATED GIVEN-LAW SCOPE. FATAL 0 / MAJOR 0 / MINOR 0.**

I reconstruct the entire sufficient-condition theorem: for every compatible fixed real plant/current-tap law with **J=D1L=0** and **M=(D0+D1K)B0L≠0**, and every fixed preview fraction theta in [0,1), the actual literal progressive gain is strictly larger than the deterministic-input gain for every sufficiently short horizon T with h=theta T. The proof retains the original output and every drift/state-noise/control-noise coupling, and pays the adaptive disturbance's exact E2-to-literal factor rather than assuming a false uniform norm equivalence.

This is a **sufficient condition for calibration failure for an already given law**, not a necessary condition, a controller construction, an optimized synthesis impossibility or a result for fixed positive h as T decreases to zero. No assertion of a nonempty satisfying class for every prescribed plant, a measure-theoretic/Zariski meaning of “generic,” or a solution of the original nonlinear/full-information N&S problem is inferred.

No selected reference radius, numeric value of rho, specific matrix/plant, individual horizon, amplitude, frequency or sanity case was chosen or tested, even privately. Every argument below quantifies over the entire source family. Main's instruction that a partial/NOT_RECONSTRUCTED return is acceptable was retained; it was not replaced by a test to gain confidence.

## 2. Actual gate, complete reads, exposure and noninputs

S0 was read completely FIRST, the entire replacement manifest SECOND, and the actual ACK was SAVED/SENT before packet body or mathematical reasoning:

- ACK `review-w95b-info-3-generic-observable-calibration-gap-replacement-prebody-ack-v1.json`, SHA256 `3463b07eafa53e79fe4cea07c7857eed51f3326c089f84cab3e6f66575f54f81`.
- Manifest SHA256 `020d0d3259c8af67dfff675766d9c474bf5a310a5688d71733d84092da65dd5a`.
- Single part SHA256 `1c54474c3e5926d2973d3834640cbe71a17d7c80f08d7eaa2f94893df155ab53`, matching Main's pin.
- ALL **250 LF**, including the actual ending and every long line, were read serially in exact raw windows **1–60,61–120,121–180,181–240,241–250**.

The packet contains complete S1 quarantine23LF, S2 recipient-frontier21LF, S3 literal criterion55LF, and S4 candidate135LF. References below use frozen original `S4|line` anchors, not mutable live files. The candidate's source SHA256 is `74c94b55c92b764f1c9ae7824358bd2a633b4e251348fb6f0e358709154f5cd8`.

This is a disjoint replacement for STOPPED w95; no w95 body/verdict was opened or inherited. The manifest's qualified pre-episode provenance is carried as **parent-supplied status**, not a new cognition or historical no-diagnostic certification. I judge only the supplied written mathematics. I had prior Preview143/w66/w86 contacts, and my w94 was stopped after a reported prohibited private check. Those exposures and all findings were disclosed before this ACK; the entire w94 episode/unprinted continuation/consumers remain ZERO/NONINPUT, and no w94 reasoning or result is used here. This is not blind or a clean-provenance certificate.

S1/S2 are binding status, never mathematical premises: L1 and all consumers remain HELD/ZERO/NONINPUT; no L1 body was opened. Old selected-reference/realization/held source and review bodies, private guides, other sources, author contact and prior favorable verdicts are not inputs. Only the current explicit packet and named ordinary mathematical facts enter the proof below. No scientific interpreter, calculator, CAS, enumeration, solver, program/replay/build/test/typechecker, model CLI or nested agent was used.

## 3. Claim-by-claim result and actual domain

| Frozen candidate claim | Disposition |
|---|---|
| S4 lines7–31: fixed law, J=0/M≠0, exact T/h quantifiers and same original caller | Correct at the explicitly adopted zero-state progressive-E2, zero-extended domain; §§3,7,9 |
| S4 lines35–49: exit moments, nonconstant stopping time, universal unevaluated rho and admissible a | Reconstructed, §4; no optional-stopping theorem or evaluated reference radius |
| S4 lines57–61: upper bound for EVERY deterministic input to the reference | Reconstructed, §5 |
| S4 lines63–85: actual adaptive E2 family, scaling, denominator and positive reference lower | Reconstructed, §§5–6 |
| S4 lines91–109: original dynamics and exact all-coupling E2 error coefficient | Reconstructed with the displayed constants, §§7–8 |
| S4 lines113–127: deterministic upper/adaptive lower and strict separation for ALL sufficiently small T | Reconstructed, §9 |
| S4 lines131–135: boundaries, sufficient-only/given-law/original-output limits | Correctly retained, §10; no broader synthesis or assurance acceptance |

The adopted law is explicitly `u=KX+Lw`, with fixed real matrices, zero initial state/history, input on [0,S], S=T−h, and zero extension elsewhere **including (S,T]**. The actual regulated output is the original D0X+D1u. Progressive E2 means finite expected squared time energy; a nonzero input then has finite positive expected path norm. This is an adopted mathematical disturbance interpretation, not independent certification that the book uniquely intends it.

For positive preview the theorem covers this current-tap subclass only. At h=0 any deterministic stationary linear map of the current information (X,w) has the displayed matrix form; the condition applies to all such given laws satisfying J=0/M≠0. It does not thereby cover arbitrary nonlinear/time-varying/memory controllers.

## 4. Brownian exit facts — ALL radii, no chosen reference or numerical constant

For every r>0 let tau_r be Brownian first exit from (−r,r). The stopped-integrand identity

`W_(t∧tau_r)=integral_0^t 1_(s<tau_r)dW_s`

follows from the defining simple/predictable approximation; its Itô-isometry statement is

`E(t∧tau_r)=E|W_(t∧tau_r)|²<=r²`.

Monotone convergence gives E tau_r<=r² and hence finiteness a.s. Path continuity gives |W_tau_r|=r, and bounded convergence in the same identity gives **E tau_r=r²**. Continuity at zero gives tau_r>0 a.s. This uses a stopped-integral construction, not an unprovided optional-stopping theorem.

The exit time cannot be almost surely deterministic: a positive deterministic exit time would force its Brownian marginal to lie on the two boundary points, contradicting the non-atomic Gaussian marginal; zero is excluded by continuity. Strict Cauchy–Schwarz therefore gives

`0<E sqrt(tau_r)<sqrt(E tau_r)=r`.

For ALL positive radii r,s, Brownian scaling from its continuous independent Gaussian increments gives tau_r distributed as (r/s)² tau_s. Hence

`rho=E sqrt(tau_r)/r`

is constant over the whole positive-radius domain, with **0<rho<1**. No radius was substituted or rho value approximated.

Fix the source's arbitrary theta<1. Continuity as a decreases to zero and 1−rho>0 show that the ENTIRE admissible positive-a set defined by

`eta=1−rho−a²/(1−theta)−rho a>0`

is nonempty. No root, sample a or threshold value is evaluated. For any a in that set, xi=tau_a∧(1−theta) is positive a.s. and bounded above by the positive finite time 1−theta. Thus m=E sqrt(xi)>0 and v=E xi are finite, and R_stop=sqrt(v)/m is finite. These constants are fixed before T varies; no uniform bound over different a/theta is assumed.

## 5. Reference upper and exact physical disturbance normalization

Set P=A+BK, Q=A0+B0K, O=D0+D1K, G=B0L, J=D1L and M=OG, exactly as in S4. For the auxiliary integrator use the **same** input and Brownian motion:

`X0_t=G integral_0^t w_s dW_s`, `Y_t=M integral_0^t w_s dW_s`.

For EVERY deterministic input supported on [0,S], the Itô isometry and Tonelli give

`E||Y||²_[0,T]=integral_0^S (T−s)|M w_s|² ds
                 <=T||M||²||w||²_[0,S]`.

Cauchy–Schwarz on the output random norm gives exactly the literal upper `E||Y||<=sqrt(T)||M||||w||`. This is an upper estimate for all deterministic inputs, not a stochastic RMS replacement or an exact deterministic norm assertion.

M≠0 supplies a real unit norm-maximizing direction e by ordinary finite matrix norm attainment. For the ENTIRE frozen family, every T>0 and amplitude q>0,

`w_(T,q)(t)=q e 1_(t<S)1_(t<sigma_T)`,

`sigma_T=inf{t:|W_t|=a sqrt(T)}`.

The stopping-time indicator is progressive, so this is a legal adaptive disturbance, not future information supplied to a controller. It is bounded, supported on [0,S], and E2. Scaling W_(Ts)/sqrt(T) gives

`(sigma_T∧S)/T` distributed as xi,

`E||w_(T,q)||=q sqrt(T)m`,

`||w_(T,q)||_E2=q sqrt(T)sqrt(v)`.

Consequently its E2/literal factor is the fixed **R_stop**, independent of T and q. Positivity of m and q pays the actual nonzero denominator, and no E2/L1 norm equivalence is claimed for arbitrary disturbances.

## 6. Reference lower — full event, tail and denominator calculation

The stochastic integral for this input is the Brownian path stopped at sigma_T∧S, times q e. On the event A={sigma_T<=S}, its magnitude after sigma_T is a sqrt(T), so

`||Y|| >=q||M||a sqrt(T) sqrt(T−sigma_T) 1_A`.

For all exit times in this event, `sqrt(T−sigma_T)>=sqrt(T)−sqrt(sigma_T)`. Therefore

`E[sqrt(T−sigma_T)1_A]
 >=sqrt(T)(1−P(sigma_T>S))−E sqrt(sigma_T)`.

The already proved moments/scaling give E sigma_T=a²T and E sqrt(sigma_T)=rho a sqrt(T). Markov's inequality at the **actual** S=(1−theta)T yields the source tail bound, and hence

`E||Y|| >=q||M||a T[1−a²/(1−theta)−rho a]`.

The bracket equals rho+eta and is strictly positive. Also `E sqrt(sigma_T∧S)<=rho a sqrt(T)`. Dividing this positive lower numerator by that upper denominator is legitimate and gives

`E||Y||/E||w_(T,q)||
 >=||M||sqrt(T)[1+eta/rho]`.

This verifies the exact coefficient and direction of the inequalities at S4|77–83. The analytical use of the exit event/exit-time distribution is not future access in w: membership of {t<sigma_T} at time t is already known from the path up to t. No radius, horizon or trajectory was selected as a check.

## 7. Full original state and elementary E2 estimate

J=0 is used in the original output ONLY to write z=OX. It is a hypothesis on a **given law**, not a solved controller equation. The actual equation remains

`dX=[PX+BLw+Cw(t−h)]dt+[QX+Gw]dW`.

All coefficients P,Q,BL,C,G remain. The current and delayed input maps have L2 norm at most one after the stated zero extension, so the drift-input bound is f=||BL||+||C||. These forcing terms are progressive E2; the permitted standard strong linear-SDE existence/uniqueness theorem for finite constant coefficients and progressive square-integrable forcing supplies actual finite-horizon strong nonexplosive state/control/output.

The needed quantitative estimate does not require BDG or an unprovided first-moment operator theorem. For

`dV=(PV+f0)dt+(QV+g0)dW`, V0=0,

expand the integral equation into its four terms. Squared four-term Cauchy, time Cauchy–Schwarz and Itô isometry yield, for t<=T,

`E|V_t|²<=4(T||P||²+||Q||²) integral_0^t E|V_s|² ds
             +4[T||f0||_E2²+||g0||_E2²]`.

The elementary integral Gronwall bound and integration in t then give

`||V||_E2<=2sqrt(T)exp(2T[T||P||²+||Q||²])
                       sqrt(T||f0||_E2²+||g0||_E2²)`.

This reconstructs the displayed source estimate with its constants. f0,g0 need not be deterministic or independent of W.

## 8. Exact all-coupling reference error — no plant substitution

For EVERY actual admitted input, Itô isometry/Tonelli give

`||X0||_E2<=sqrt(T)||G||||w||_E2`.

Subtracting the actual equations, V=X−X0 has homogeneous P,Q, drift forcing `PX0+BLw+Cw(t−h)` and diffusion forcing QX0. Thus

`||f0||_E2<=(f+||P||sqrt(T)||G||)||w||_E2`,

`||g0||_E2<=||Q||sqrt(T)||G||||w||_E2`.

Substitution into §7, and z−Y=OV, proves exactly

`||z−Y||_E2<=epsilon(T)||w||_E2`,

`epsilon(T)=2T||O||exp(2T[T||P||²+||Q||²])
              sqrt((f+||P||sqrt(T)||G||)²+||Q||²||G||²)`.

For the fixed matrix tuple this is O(T), so epsilon(T)/sqrt(T) tends to zero. Zero drift factors, singular matrices or vanishing norm terms require no division and cause no problem. In particular no smallness assumption on Q is made. The comparison Y has **not** been asserted identical to the plant output; the actual original error is bounded and retained.

## 9. Actual deterministic/progressive ratios and ALL-small-T gap

For every deterministic input, its E2 norm equals its deterministic L2 norm and its literal denominator. Triangle inequality, §5 and the actual error bound therefore give

`G_det(T,h)<=U(T)=||M||sqrt(T)+epsilon(T)`.

For the actual adaptive family, `E||z−Y||<=||z−Y||_E2` and the exact R_stop factor give instead

`E||z(w_(T,q))||/E||w_(T,q)||
 >=L(T)=||M||sqrt(T)[1+eta/rho]−epsilon(T)R_stop`.

Every such input is physically E2 and has a finite positive denominator, so its actual ratio is finite. Since ||M||eta/rho>0 and R_stop is fixed finite,

`L(T)−U(T)=||M||eta sqrt(T)/rho−epsilon(T)(1+R_stop)>0`

for **EVERY sufficiently small positive T**. This follows from the proved limit; no particular T0, a, matrix tuple or horizon is tested/evaluated. Any admissible a first fixed by the nonempty symbolic condition supplies such a T0, proving existence for each matrix/law/theta tuple in the theorem.

The progressive supremum contains this actual input family, so `G_prog>=L(T)>U(T)>=G_det`. No exact value or finiteness of G_prog is needed. Since U(T)>0 here, every threshold strictly between U(T) and L(T) is an admissible positive gamma: all deterministic tests pass the SAME given law while a legal progressive disturbance fails its original literal inequality. This is the promised calibration obstruction, not optimization over controllers.

## 10. Boundaries, remaining scope and final assurance

All stated hypotheses are used correctly:

- M≠0 yields a positive gap coefficient and maximizing direction; no conclusion is claimed when it fails.
- J=0 removes only the instantaneous output term, not control diffusion G or state-noise Q. No conclusion is claimed for J≠0.
- theta<1 guarantees positive input length and finite tail denominator; theta=1 is not included. The proof includes theta=0 without a separate chosen case; positive theta uses h=theta T, not fixed positive h as T tends to zero.
- a,q are positive, m,rho positive by proof, and R_stop finite; no zero denominator or endpoint convention is fabricated.
- All matrix ranks/signs and all remaining finite drift/noise/feedback coefficients are unrestricted. No stabilizability, observability beyond the explicitly nonzero channel M, noise-smallness or selected-type condition is added.
- Positive-preview left/kernel-tap laws, arbitrary nonlinear/time-varying controllers, nonzero initial states, optimized synthesis and infinite-horizon eligibility are outside this theorem, not silently solved.

The title's “generic” is supported only as the expressly quantified algebraic sufficient condition on given tuples. This review supplies no extra density/nonemptiness-for-every-plant theorem. The book's exact process-space/common-margin intention and image equivalence remain unverified. The source's reference to a larger released h0 stationary-linear class is read at the displayed fixed-matrix current-information law, not as a claim about all printed nonlinear F.

Named ordinary imports used and reconstructed where needed: the defining Brownian Gaussian/continuity/scaling properties, stopped-integrand Itô construction and isometry, Fubini/Tonelli, finite matrix norm attainment, Cauchy–Schwarz/Markov, elementary integral Gronwall and the expressly named finite linear-SDE existence/uniqueness theorem. No optional-stopping or BDG theorem, NR-GAIN proof, held realization/source guide, current coauditor verdict or selected-reference episode is a premise.

**Final: FATAL0 / MAJOR0 / MINOR0, NO SUBSTANTIVE DEFECT AT THE EXACT GIVEN-LAW SHORT-HORIZON SCOPE.** This does not certify author/reviewer private-history separation, transfer a stopped w95/w94 verdict, solve general original synthesis, prove novelty, or confer formal/kernel/human/configured-family/executable acceptance. Main must read complete sources and return before adoption. All S0/HOLD/STOP/ZERO/L1-consumer controls, N4 UNKNOWN/historical child exit UNESTABLISHED, auxiliary214 STOP, same18/OWN and the unchanged Oct31 deadline persist.

**END COMPLETE w95b REVIEW — ALL250LF READ; UNIVERSAL ARGUMENT ONLY; NO SELECTED CHECK.**
