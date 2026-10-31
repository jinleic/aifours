# w21 — Physical adapted/disturbance gap and full-law robustness: complete review

Actual native `/bin/date` before this NEW body: **Tue Oct 27 15:16:25 PDT 2026**.
Reviewer **MathSun8-2** (math-6); author **InfoHinfPreview-2** (info-3). **Same-harness WRITTEN review**, serial and non-blind, not formal/kernel, human, configured-family, executable or novelty acceptance.

## 1. Verdict, frozen coverage and exposure

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE** for BOTH complete candidates: the scalar finite-horizon physical counterfamily, its strict original expected-path-norm adapted/deterministic gap, and the open full-scalar-tuple robustness consequence with the displayed general fixed-dimension E2 difference estimate. No mathematical FATAL, MAJOR or MINOR finding is identified in these reconstructed statements. Each load-bearing claim, import and application is checked below; process history is separate (§11).

This refutes the specified UNIVERSAL fixed-law equality, not existential synthesis. It does not calculate either gain exactly, prove an infinite-horizon theorem or certify the book transcription. No old preview/RMS proof or favorable verdict is an input.

The complete frozen manifest was read after S0 and BEFORE the actual pre-body ACK. Manifest SHA256: `b989ce0a880d2a5d2679a436c75c251de1ec38e98eb6243e4a37fb240c98ce30`. The required ACK, written at actual15:12:18 before ANY packet access or review derivation, is `review-w21-preview-adapted-physical-gap-prebody-ack-v1.json`, SHA256 `61bb89a001e152e7a4d457b173a9ba0574d447547defc4fd13bc465c30ff6dbc`,21LF/4426B.

Specific contacts disclosed there include the old v244-B preview/RMS duty reported in the authorized safe final status, the retained incoming preview-author Sun8 exact-rank4-normalizer review/ACK contact, earlier privacy source/review contacts and other carried Kac/Tuscan duties. Exact old assignment/pins not available in retained context were NOT invented or recovered by old-body lookup. These are material contacts: no blind/clean-slate or exhaustive private-history assertion. The Sun selected-index episode and every consumer remain HELD/ZERO; this Main-assigned disjoint stochastic review does not resume that line or use it as method/selection/confidence input.

The ENTIRE sole packet `packet-part-1-v1.md` was read raw in windows1–60,61–120,121–180,181–240,241–300,301–360,361–411. Every supplied LF, long line and true ending was returned. Packet SHA256 `2f8889df0ee797d6fe34ec96c5e345ef6a80e9a3c431e1d3238b9df1a1c8cea4`,411LF/41103B, live-matched before access.

| Source | Complete supplied LF | SHA256 |
|---|---:|---|
| S1 literal-criterion packet | 55 | `888307a4a094bc5fa7aca45484334f8a12b75e9fb3e86259d81acf31cad629f3` |
| S2 bound linear-preview-class packet | 37 | `cbf78426d65a0c373cbc11d31d7eda200478025e5beafa4c970ffc86aa358ed7` |
| S3 author exposure/timing disclosure | 19 | `82d89cc8a86ed2d598b8c35465cfdf2fcc4234f4d8d8853716ab335139f8af63` |
| S4 complete physical-gap derivation | 161 | `13ad2a5613c767a5bc68a018bdfb47858ba3bd7ff235229f8bace4490ede54a1` |
| S5 complete robustness addendum | 119 | `575778fd8ce64721ebc4bbf653a88db1e4ba9e9b400469ed93709fc9d6ef63b0` |

No additional source, old proof/held body, author contact, co-auditor lookup or scientific execution was used.

## 2. Exact criterion, admissible classes and ordinary input cut

S1's nested supplied dossier transcription uses

`dx=[Ax+Bu+Cw(t−h)]dt+[A0x+B0u]dW`, `z=D0x+D1u`,

and the literal criterion `E||z|| / E||w||`, with a pathwise L2 norm BEFORE expectation. The book asks for both horizons and N&S synthesis; its disturbance/controller/initial-data interpretations are not silently supplied by that transcription.

This review addresses the explicit binding in S2 LF31–37 and S4 LF9–23: fixed finite T>h≥0, zero initial state/history, scalar canonical Brownian filtration, progressive E2 inputs on `[0,S]`, S=T−h, extended by zero elsewhere, and deterministic stationary laws

`u(t)=Kx(t)+L0w(t)+Lh w(t−h)+integral_0^h H(r)w(t−r)dr`,

with fixed real compatible matrices and deterministic `H∈L2([0,h])`. At h=0 the two taps combine and the kernel is absent. No extra Brownian history/private randomization/controller memory is introduced beyond the state and given input window. Every gain ratio excludes zero expected input norm; zero E2 inputs consequently do not enter the supremum.

For each FIXED plant/law, `G_prog` is the supremum over these progressive E2 inputs; `G_det` is the supremum over deterministic L2 inputs, with their deterministic denominator. They are NOT Hilbert/RMS gains. A strict gap for one entire physical family disproves equality for EVERY law/plant at this interpretation; no optimizer or equality formula is needed.

Permitted foundations actually used are finite-horizon strong existence/uniqueness for linear SDEs with constant globally Lipschitz state coefficients and progressive E2 forcing; the ordinary Itô integral construction/isometry; Tonelli/Fubini, monotone/bounded convergence, Minkowski/Cauchy–Schwarz/triangle/Markov inequalities, elementary integral Gronwall, and Brownian continuity/Gaussian marginals from its definition. Their exact uses are given below. No optional stopping, reflection principle, scaling/exit density, BDG constant, measure change, stochastic-flow/Gramian/storage or an old source is needed.

## 3. Brownian stopping constant — full derivation and strictness

**Claim:** for EVERY a>0, the same canonical Brownian motion's first exit `tau=inf{t≥0:|W_t|=a}` satisfies `0<tau<infinity` almost surely, `E tau=a²`, and `rho=E sqrt(tau)/a` lies strictly in `(0,1)` (S4 LF31–49).

**Reconstruction.** Continuity and the natural filtration make tau a stopping time; continuity at0 gives tau>0. For every finite t, approximate tau from above by mesh stopping times. The stopped simple-predictable integrals are finite sums of increments up to those mesh stops. The product-measure squared-indicator error on `[0,t]` is bounded by the mesh length. Itô isometry gives L2 convergence, while path continuity identifies the limit as `W_(t∧tau)`. Indicators with `<` or `≤` at the stop differ on a pathwise singleton and hence on no product-measure mass. Thus

`integral_0^t 1_(s<tau)dW_s=W_(t∧tau)`,
`E(t∧tau)=E|W_(t∧tau)|²≤a²`.

The bound holds without presupposing finite tau: before its first hit the continuous path stays within the interval. Monotone convergence gives E tau≤a², so tau is finite a.s. Continuity then gives `|W_tau|=a`; bounded convergence in the stopped square and monotone convergence on the left give E tau=a². No optional-stopping identity has been assumed.

A finite deterministic tau=s>0 would imply `|W_s|=a` almost surely, contradicting the nonatomic Gaussian marginal. Tau is therefore nonconstant. Cauchy–Schwarz gives `0<m_a:=E sqrt(tau)≤a`; equality would make sqrt(tau) constant in L2, impossible. Hence `0<rho=m_a/a<1`. Markov gives `P(tau>S)≤a²/S` for every S>0. These are exact UNEVALUATED constants, not sampled values.

**Mathematics/dependency verdict:** no substantive defect. Every stopping property used later is paid from the permitted construction/isometry and ordinary measure facts. No circular finite-exit assumption or unsupplied exit-time formula remains.

## 4. Entire symbolic physical family and every actual-input caller

**Claim and quantifiers:** S4 LF53–91 choose arbitrary nonzero real b,d,ell, arbitrary a>0 and finite h≥0; take ANY finite T satisfying

`T>max{h+2a²/(1−rho), 4rho²a²/(1−rho)²}`,

put S=T−h and `eta=1−rho−a²/S−rho a/sqrt(T)`, and take ANY nonzero real c with

`|c|<|b ell| eta/(2rho sqrt(T))`.

The first T bound gives `a²/S<(1−rho)/2`; the second gives `rho a/sqrt(T)<(1−rho)/2`. Thus S>0 and eta>0, and the nonzero c interval is nonempty. This is a nonempty symbolic family for EVERY a and finite h, not a chosen numerical plant or sanity probe.

The actual scalar plant/law is

`A=B=A0=0`, `C=c!=0`, `B0=b!=0`, `D0=d!=0`, `D1=0`,
`K=Lh=0`, `H=0`, `L0=ell!=0`; hence `u=ell w`.

The controller is the SAME fixed law for all disturbances; it does not inspect a stopping rule or an independent Brownian signal. For h>0, its current tap is in the stipulated window; for h=0 it is the permitted combined tap. The delayed drift and control-noise channels are nonzero, and output remains the original `z=d x`.

For EVERY progressive E2 w, direct integration gives the actual strong solution

`x_t=c R_h w(t)+b ell M_w(t)`,
`R_hw(t)=integral_0^t w(s−h)ds`, `M_w(t)=integral_0^t w(s)dW_s`.

The delay is causal/progressive with the stated zero extension. Pathwise drift integration and the Itô construction give a continuous strong state; subtraction proves uniqueness. Its finite-horizon bounds are

`||R_hw||_[0,T]≤T||w||_[0,S]`,
`E||M_w||_[0,T]²=integral_0^S(T−s)E|w_s|²ds≤T E||w||_[0,S]²`.

For the first, pointwise Cauchy–Schwarz bounds `|R_hw(t)|≤sqrt(T)||w||_[0,S]`, followed by t integration. The second is isometry then nonnegative Tonelli, not a conditional deterministic response evaluated on an input graph. State/output are E2, `E integral|u|²=ell² E||w||²<infinity`, and continuous finite paths are nonexplosive. No additional restriction on unknown progressive disturbances is introduced.

**Mathematics/dependency verdict:** no substantive defect, including h=0, every finite h>0, signs of b,c,d,ell and all actual progressive inputs. The explicit solution, not a hypothetical controller realization or optimizer, secures admissibility.

## 5. Uniform bound covering ALL deterministic disturbances

Let `kappa=|d b ell|>0`. For EVERY deterministic nonzero `v∈L2([0,S])`, triangle inequality and the preceding bounds give

`E||z_v||≤|dc|T||v||+kappa E||M_v||`
`          ≤[|dc|T+kappa sqrt(T)]||v||`.

The second step is Cauchy–Schwarz on the probability space applied ONLY to bound the literal expected norm. Therefore

`G_det≤U:=kappa sqrt(T)+|dc|T<infinity`.

No singular value, attainment or exact gain has been assumed. This is an upper bound for the ENTIRE deterministic class with the SAME physical law/output (S4 LF95–103), not a comparison against one deterministic test input.

**Mathematics/dependency verdict:** no substantive defect; use of a square moment as an inequality is not substitution of the RMS criterion.

## 6. Actual progressive family, denominator and strict expected-path-norm gap

For EVERY amplitude q>0, S4 LF107–145 use

`w(t)=q 1_(0≤t<S)1_(t<tau)`, zero elsewhere.

It is progressive in the original Brownian filtration; the stopping is selected by the disturbance, not the controller. Its expected squared energy is `q² E(tau∧S)≤q²a²`, and

`E||w||=q m_S`, `m_S=E sqrt(tau∧S)`, `0<m_S≤m_a<infinity`.

Positivity follows from tau>0 and S>0, so no denominator is zero. The actual martingale is `q W_(t∧tau∧S)`. On tau≤S it has constant absolute value qa after tau; hence

`||M_w||_[0,T]≥q a sqrt(T−tau)1_(tau≤S)`.

For EVERY nonnegative r, `sqrt(T)≤sqrt(r)+sqrt((T−r)_+)`. Taking expectation at tau, then removing tau>S at cost at most `sqrt(T)P(tau>S)`, gives

`E||M_w||≥q a[sqrt(T)−m_a−sqrt(T)a²/S]`
`          =q a sqrt(T)(rho+eta)>0`.

Since the lower bound is positive, replacing its denominator q m_S by the larger q m_a is legitimate. This yields the exact source bound

`E||M_w||/E||w||≥sqrt(T)(1+eta/rho)`.

Reverse triangle and the PATHWISE drift bound, not an uncontrolled E2-to-L1 replacement, then give

`E||z||/E||w||≥L:=kappa sqrt(T)(1+eta/rho)−|dc|T`.

Finally the entire c hypothesis gives

`L−U=kappa sqrt(T)eta/rho−2|dc|T>0`.

Thus an ACTUAL admissible adapted ratio satisfies `G_prog≥ratio≥L>U≥G_det`. The exhibited ratio is finite by the E2 bounds and positive denominator. No finiteness, value or optimizer of the SUPREMUM G_prog is needed or claimed. The amplitude cancels, and every member of the stated symbolic disturbance family works.

**Mathematics/dependency verdict:** no substantive defect. The Brownian stopping constant is derived, the numerator lower bound and deterministic upper bound are in the SAME units and functional, and no independent input/noise or unrealizable response is inserted.

## 7. Core boundaries and the exact logical refutation

S4 LF149–157 correctly refute equality for EVERY fixed law/plant at the bound interpretation, for h=0 and every finite h>0. For any `U<gamma<L`, all deterministic nonzero inputs satisfy the strict criterion uniformly, but the actual adapted input fails it. This avoids endpoint/supremum strictness ambiguities.

This does NOT show that no DIFFERENT law can achieve gamma for the same plant. The existential controller N&S problem remains open. It also does not claim exact gains, an infinite horizon, nonlinear laws, a different filtration/controller convention or uniformity in T/h.

All nondegeneracies used for strictness are explicit: a>0, S>0, b*d*ell nonzero and eta>0. At d=0 the original scalar output is zero and both gains are zero. If b*ell=0 the strict nonzero-c interval is empty and no noise gap is asserted. The proof also works at c=0 as a noise-gap consequence, but the main family intentionally takes c nonzero. At T=h no nonzero input denominator exists under the bound horizon; that case is excluded. Equality boundaries eta=0 and gamma endpoints are not claimed.

**Verdict:** no substantive defect at those exact limits. NR-SOURCE/book-image equivalence and NR-SYNTHESIS are correctly retained, rather than turned into unconditional original-problem completion.

## 8. Robustness: general closed-loop class and explicit E2 state bound

S5 LF11–61 first work at ANY fixed compatible finite matrix dimensions, T and h. Define the input operator

`R_theta w=L0w+Lh S_hw+integral_0^h H(r)w(.−r)dr`,
`r_theta=||L0||+||Lh||+sqrt(h)||H||_L2`, `S_hw=w(.−h)`.

For a pathwise L2 input, translation is a contraction from the zero-extended interval `[0,S]` to `[0,T]`. Minkowski bounds convolution by the deterministic L1 norm of H, which is at most `sqrt(h)||H||_L2`. Hence `||R_theta w||≤r_theta||w||` pathwise and then in E2. The same applies to operator differences with delta_r. Progressive measurability follows by restricting to any `[0,t0]`, using the progressive input's joint measurability there, the causal map `(t,r)↦t−r≤t`, and measurable deterministic time integration. No future w is used. At h=0 the kernel is absent; keeping the two endpoint norms is a valid upper bound on their combined tap.

Direct substitution retains ALL original couplings:

`P=A+BK`, `Q=A0+B0K`, `F=B R_theta+C S_h`, `G=B0 R_theta`,
`N=D0+D1K`,
`dX=(PX+Fw)dt+(QX+Gw)dW`, `Z=NX+D1 R_theta w`.

Constant P,Q are globally Lipschitz/linear; Fw,Gw are progressive E2 by these bounds. The permitted finite-horizon linear-SDE theorem therefore gives a unique strong continuous nonexplosive state. The following explicit estimate secures E2 state and then control/output for EVERY actual progressive E2 input, not merely separate deterministic versions.

For arbitrary progressive E2 forcing f,g, split the integral equation into its four terms. The inequality `|sum_1^4 v_i|²≤4 sum|v_i|²`, drift Cauchy–Schwarz and Itô isometry give, with `e(t)=E|X_t|²`,

`e(t)≤alpha integral_0^t e(s)ds+4(T||f||_2²+||g||_2²)`,
`alpha=4(T||P||²+||Q||²)`.

Iterating the nonnegative integral inequality gives the exponential-series Gronwall bound. Integrating in t and taking square roots gives

`||X||_2≤J(P,Q)sqrt(T||f||_2²+||g||_2²)`,
`J(P,Q)=2sqrt(T)exp(2T[T||P||²+||Q||²])`.

The exponent and constants agree with the source; there is no division by alpha, so zero coefficients are covered. Strong linear-SDE finite-moment estimates or localization followed by these bounds justify the intermediate second moments; no BDG/maximal theorem is smuggled in.

With `f_theta=||B||r_theta+||C||`, `g_theta=||B0||r_theta`, put `M_theta=J(P,Q)sqrt(T f_theta²+g_theta²)`. Then `||X_theta(w)||_2≤M_theta||w||_2`, and KX+Rw and NX+D1Rw are E2. 

**Mathematics/dependency verdict:** no substantive defect. Every matrix dimension is covered for the ESTIMATE. The later strict-gap neighborhood is explicitly scalar; it is not silently promoted to all dimensions.

## 9. Robustness: SAME-input difference with every plant/law/output coupling

Fix ANY reference tuple theta_* in those dimensions, with bound M_* (S5 LF65–87). Let

`delta_r=||L0−L0_*||+||Lh−Lh_*||+sqrt(h)||H−H_*||_L2`,
`delta_P=||P−P_*||`, `delta_Q=||Q−Q_*||`, `delta_N=||N−N_*||`,
`delta_F=||B||delta_r+||B−B_*||r_*+||C−C_*||`,
`delta_G=||B0||delta_r+||B0−B0_*||r_*`.

These F/G bounds follow from the ACTUAL decompositions `B(R−R_*)+(B−B_*)R_*+(C−C_*)S_h` and its B0 counterpart. P,Q,N are the whole actual products, so changes in K,B,B0,D1 are not lost.

On the SAME Brownian space and SAME progressive input, subtract the two original equations. Delta X has homogeneous coefficients P,Q, and forcing

`(P−P_*)X_*+(F−F_*)w`, `(Q−Q_*)X_*+(G−G_*)w`.

Their E2 norms are at most `(delta_P M_*+delta_F)||w||_2` and `(delta_Q M_*+delta_G)||w||_2`. The state estimate therefore gives

`||Delta X||_2≤D_theta||w||_2`,
`D_theta=J(P,Q)sqrt(T(delta_P M_*+delta_F)²+(delta_Q M_*+delta_G)²)`.

Subtracting the actual outputs gives EXACTLY

`Delta Z=N Delta X+(N−N_*)X_*+D1(R−R_*)w+(D1−D1_*)R_*w`.

Hence

`||Delta Z||_2≤epsilon_theta||w||_2`,
`epsilon_theta=||N||D_theta+delta_N M_*+||D1||delta_r+||D1−D1_*||r_*`.

All terms are finite, continuous in finite matrix/gain norms and the L2 kernel norm at fixed T,h, and tend to zero at theta_*. This is quantitative coupling of actual solutions, not a topological claim inferred from distinct input versions or an RMS performance identity. No output term has been suppressed; changing D0,D1 means a different ORIGINAL plant output of the same prescribed form, not a substitute output chosen after the comparison.

**Mathematics/dependency verdict:** no substantive defect; all source coefficients and same-input hypotheses are paid.

## 10. Open full-scalar-law neighborhood and literal-norm conversion

Choose ANY reference member of S4's ENTIRE scalar family, and let Delta=L−U>0. Fix ANY amplitude q>0 from its actual stopped input family; keep that SAME stopping rule/input for every perturbed tuple (S5 LF91–115). Its admissibility is independent of the plant. Its moment-to-literal-norm factor is explicitly

`||w_*||_2/E||w_*||=sqrt(E(tau∧S))/m_S≤a/m_S=:R_*<infinity`.

No unknown progressive class norm-equivalence is asserted. For EVERY deterministic v, `||v||_2=||v||` and Cauchy–Schwarz applied to Delta Z gives `G_det(theta)≤U+epsilon_theta`. For this fixed ACTUAL progressive w_*, the same bound and reverse triangle give ratio at least `L−epsilon_theta R_*`.

Therefore

`epsilon_theta(1+R_*)<Delta`

implies `G_prog(theta)≥actual ratio>U+epsilon_theta≥G_det(theta)`. Since epsilon is continuous and zero at the reference, this set contains a nonempty OPEN neighborhood in the product of ALL scalar original matrices, K,L0,Lh and H in L2, with dimensions,T,h FIXED. The class does not require the zero reference coefficients A,A0,B,K,D1,Lh,H to remain zero. For h>0 it includes nonzero delayed taps and nonzero arbitrarily small L2 kernels; for h=0 it is the combined-endpoint class without a kernel. The nonzero reference c,b,d,ell can be preserved by shrinking the neighborhood.

Thus the robustness claim covers a full scalar physical neighborhood and the general fixed-dimension E2 difference estimate, not a uniform-in-T/h, different-dimension, nonlinear-law or synthesis statement. Zero outputs/coefficient cases remain valid for the ESTIMATE; strictness alone requires Delta>0 and the proven nonzero reference input denominator. No bound divides by a possibly zero plant coefficient.

**Mathematics/dependency verdict:** no substantive defect. The E2 estimate is ONLY a perturbation tool, and the actual adapted E2-to-expected-norm factor is retained, preventing the illegitimate Hilbert-to-literal conversion that would otherwise be a missing step.

## 11. Process disclosure, imports/NR boundaries and handoff

S3 LF11–17 explicitly records that the author's required ACK preceded definition-body access but NOT all internal derivation. The preliminary reasoning's onset clock was not observed. S4 LF25 reports that Main subsequently classified this PROCESS MINOR and prospectively permitted development at the noncolliding path, not a clean restart or retroactive cure. Preserve both chronological statements. The separate parent classification artifact is not in this packet and was not independently read here; its reported process classification is not a new mathematical premise. Current review permission is this frozen manifest, not a reconstruction of old authority or cognition.

No other source is needed to pay the mathematics above at the expressly permitted ordinary stochastic/measure/L2 foundations. Their foundational proofs are not newly formalized. **NR-SOURCE:** no fresh book-image/primary-source equivalence certification is supplied. **NR-SYNTHESIS:** no general N&S controller criterion, existential impossibility, exact optimal law/value, infinite-horizon result or alternative filtration/information convention is established. These are exact scope limits, not hidden missing steps inside the fixed-law theorem.

The reference family is symbolic with full analytic inequalities and no member numerically selected/evaluated. The actual stopped input is a constructive mathematical counterfamily within the released task, not a supplementary diagnostic probe. Neither author nor reviewer reports a numerical computation here. The author's old STOP/HOLD/ZERO and every source/process history remain; no earlier candidate gains new admissibility from these calculations.

My pre-body contact disclosures and Sun selected-index quarantine remain permanent. No Sun reasoning was interleaved with this review; none of its HELD/ZERO selection/confidence/method consumers is a review input. No old preview/RMS/Gramian proof, old review verdict, source-map/park/checkpoint body or excluded source was opened. No author contact, external source/modelCLI, nested task, scientific interpreter/calculator/Eval/CAS/program/enumeration/test/typechecker/solver/replay, selected numeric/control probe, newGO, Git/deletion/publication/infrastructure mutation, timer/poll or heartbeat. Metadata hash/LF/native clocks are not proof verification. N4 UNKNOWN historical child exit unestablished, auxiliary214 STOP and HOLDv2 persist.

**Final exact verdict:** NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE for S4's physical finite-horizon strict-gap family and S5's full stated robustness theorem. The complete source scope, all actual-input/admissibility/stopping/strictness/difference-bound callers and degeneracies have been reconstructed above. Main must itself read the complete sources and this return before any adoption. Same-harness WRITTEN support is not formal/kernel, human/configured-family, executable or novelty acceptance, an original synthesis solution or round closeout.
