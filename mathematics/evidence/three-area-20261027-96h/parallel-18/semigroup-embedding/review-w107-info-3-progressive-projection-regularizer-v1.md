# w107 — complete progressive-projection regularizer review

Reviewer **MathSemigroup-2**, math-4. Author **InfoHinfPreview-2**, info-3. Same-harness WRITTEN only.

Actual native pre-body ACK observation: **Tue Oct 27 18:26:53 PDT 2026**. Actual native observation immediately before writing: **Tue Oct 27 18:32:25 PDT 2026**. Interior read/reasoning times were not separately observed or backdated.

## 1. Exact verdict and scope

**S3, ENTIRE94LF candidate, SHA`0c9f5686e7b336fa2d910c6176a6c1271919d9cbd6ab66c3a898cd6ef0f9aa1d`: NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE — 0 FATAL / 0 MAJOR / 0 MINOR.**

The complete proved scope is: for every supplied finite-horizon plant and fixed deterministic stationary law, every nonzero progressive E1 input and every deterministic c>0, the product-progressive conditional projection gives a genuine nonzero progressive E2 disturbance with the stated energy/first-moment bounds and pointwise channel-direction/zero-support preservation. All used finite-horizon original state/control/output callers, projection/completion representatives, nonintegrable-weight estimates, path-angle equality and feedforward commutator are reconstructed below.

**NR-ENDPOINT-FACE remains:** the regularizer has not been proved to preserve the actual operator's norm-attaining face. Full E2-pointwise-strict -> E1-pointwise-strict endpoint transfer is neither proved nor refuted. No output multiplier identity, physical endpoint attainer, counterfamily, strict example, common-controller synthesis theorem or novelty result follows. “Causal” here is the constructed input's admissible progressiveness; no stronger output intertwining is inferred.

S6's unused infinite-horizon assertions and S7's unused subclass/split conclusions are not blanket-adopted merely because their full bodies were read. The exact finite-horizon facts actually used by S3 are paid below without inherited review approval.

## 2. Required order, complete reading and exposure

S0 and the whole92LF manifest were read before any packet body or mathematics. Manifest SHA`2996638911d921f68f72056bb60c61e59d194190af0b2b53f7b193bd9f40e1b1`. I then wrote the required actual-clock pre-body ACK, SHA`bf03c9102366ee2fd77a5fbb5bc5c18b3efccabb38b89f2bf4f8829e07020ce3`, at18:26:53.

The entire packet was read through **all560LF /61273 bytes and all12 source endings**, with long lines fully displayed, in raw windows1–60,61–120,121–180,181–240,241–300,301–360,361–420,421–480,481–540,541–560. No window exceeded60LF. Its expected SHA`5804dc0e5e6d15075e47e253178e0d77bc85852f448c6655105733ae44b6405f` matched native metadata hashing.

Prior known contacts include outgoing Preview v143B/short-horizon and new w25, the incoming Preview full-Rees/corner semigroup review history, and the author's historical w98b SPR return read as status/findings during w102. These are retained contacts, not blindness, clean cognition or proof premises. No old proof/review body was reopened for this duty and no author/coauditor was contacted.

Own semigroup STOP/ENTIRE171 and every consumer, own v196 inventory PROCESS MAJOR, QOA display MINOR, w68 window deviation, w97b S43-display/Main packet qualification and all prior findings persist. Withdrawn S43, excluded truth-fiveflat and later held NL episodes/consumers are NONINPUT. The author's selected-reference/calibration episode, old annihilation/C1–C3/R4/v209 routes, L1 and ALL consumers remain excluded. Only their supplied safe status controls were read. No complete contact census or unaffected-cognition certification is made.

No selected distribution, input path, time, controller, plant, parameter, state, coefficient, operator or private sanity probe occurred. All auxiliaries below are universally quantified measure/Hilbert proof objects, never instantiated scientific tests. No scientific interpreter/calculator/Eval/CAS, enumeration, program, solver, replay/test, modelCLI, nested task, external source, author contact, Git/deletion or out-of-root write. Only the required ACK and this review were written.

## 3. Exact inputs and used dependency boundary

| Source | Exact role |
|---|---|
| S3,94LF | Entire candidate; every claimed theorem, inequality, equality criterion and actual-input caller reviewed. |
| S4,37LF, SHA`cbf78426d65a0c373cbc11d31d7eda200478025e5beafa4c970ffc86aa358ed7` | Full fixed-law finite T>h>=0, zero-history plant/controller and literal norm definitions. |
| S5,38LF, SHA`7f94e11b6ef89380506b127a354a372e041c30641d96c82a72b46706c89616ef` | Narrow endpoint authority; finite common gamma>0 and LOCAL control admissibility, no synthesis/source expansion. |
| S6,89LF, SHA`857ec99cc1be5d4ce2cd204fd7b0b01983d8bb8b3c8e633854b75370fb78da28` | Used finite-horizon causal window, actual E2 solution, local E1 extension and finite-gain actual-output bound. Reconstructed in §4. |
| S7,115LF, SHA`32a476df800c967f532adf6071461ee060e77435912814c814cd0122ffad1be2` | Complete prior context, not an assumed verdict. Its used finite-gain/deficit and missing-equality boundary are paid in §§4,8. |
| S1/S2/S8/S9 | Binding L1, author selected-reference and own primary STOP/status only. |
| S10/S11/S12 | Binding parent source-search/excerpt freeze and addenda. Already-pinned disjoint review remains allowed; no source-discovery permission. |

Named ordinary foundations used at their explicit scope: finite-dimensional linear algebra; Hilbert orthogonal projection (construction supplied below); finite-measure L2 subsequence/measure approximation; monotone/dominated convergence and Tonelli; Cauchy–Schwarz and L1(Omega;L2(I)) completeness; and the **permitted finite-horizon linear-SDE strong existence/uniqueness/linearity theorem for progressive square-integrable forcing**, with Itô isometry. No progressive optional-projection, martingale representation, first-moment flow/BDG bound, adjoint, calibration, risk or old realization theorem is imported.

## 4. Used original SDE/output caller, reconstructed at finite horizon

Fix arbitrary compatible real matrices and one given law on I=[0,T], J=[0,S], S=T-h>0, with zero input outside J and zero state/history. Keep the original

u=KX+Rw,
Rw=L0w(t)+Lh w(t-h)+integral_0^h H(r)w(t-r)dr,
z=D0X+D1u.

Zero extension, time translation and the deterministic integral inequality give

||Rw||_L2(I)<=(||L0||+||Lh||+sqrt(h)||H||_L2)||w||_L2(J).

The kernel has finite L1 norm by finite h and Cauchy–Schwarz. Each delayed value uses only past input; restricted product measurability and parameter integration preserve progressiveness. At h=0 the taps combine and the integral is absent; no division by h occurs. Agreement through a stopping time gives agreement of every forcing/window term there, modulo the usual time-null equality.

After substitution the state equation is

dX=[(A+BK)X+B Rw+Cw(t-h)]dt
   +[(A0+B0K)X+B0 Rw]dW.

For any E2 input the deterministic window bound makes both inhomogeneous forcings progressive and square-integrable on I. The admitted theorem for constant finite linear coefficients gives a unique continuous adapted strong solution on I, with finite second-moment state bound; consequently u,z are actual progressive E2 processes. The theorem also gives constant-scalar linearity, localized uniqueness and no finite-time explosion. These are exactly the supplied named SDE facts and their hypotheses. No law/plant is altered or controller memory added.

For any E1 input, U=integral_J|w|² is finite almost surely since E sqrt(U)<infinity. The adapted accumulated energy is continuous and nondecreasing. Its capped level stops tau_N are stopping times; w_N=w1_(t<tau_N) is progressive with energy<=N, hence actual E2. For M>=N, their inputs/window terms agree through tau_N; localized uniqueness makes their states agree there. A single countable full-probability consistency event permits patching. On every finite-energy path N eventually exceeds U, so the stop is T and the patched response agrees on all I with one nonexplosive E2 solution on that path. The resulting actual control is pathwise L2 on this finite interval; uniqueness follows from the same stops. This is local/pathwise admissibility, not an expected global E1 state/control estimate.

Under the task's finite E2 gain gamma, every E2 input satisfies E||Z(v)||_I<=gamma E||v||_J, including zero by zero history/linearity. Input stopping gives E||w-w_N||->0 by dominated convergence, bounded by the integrable ||w||. The actual difference inputs are E2 and constant-scalar linearity gives

E||Z(w_M)-Z(w_N)||<=gamma E||w_M-w_N||->0.

Completeness of L1(Omega;L2(I)) gives an output limit. It is the **actual patched output**, not an abstract completion: outside the countable consistency null set, outputs eventually agree on all I with the patched response; an almost-sure norm-convergent subsequence of the L1 limit identifies that same response. Therefore every E1 actual output has finite expected path norm and

E||Z(w)||<=gamma E||w||.

No global expected state/control bound, noncausal terminal-factor identity or assumption of gain finiteness from E2 well-posedness is inserted. Only the stipulated finite-gain branch is used; S6's other horizon/branch is not newly adjudicated. This pays the actual E1/E2/deficit caller used later in S3.

## 5. Product-progressive projection exists, with a legitimate representative

Let m=dt times P on J times Omega; its mass is the finite positive S. Let G0 be the progressive sigma field on J and G its completion modulo m-null sets. The real L2(m) classes admitting G-measurable versions form a linear **closed** subspace: from L2 convergence select a subsequence converging m-almost everywhere, and take its measurable pointwise limit where finite. Completion makes any exceptional null modification harmless at the level of these classes.

For completeness, orthogonal projection needs no conditional-martingale theorem. Minimize squared distance of the bounded lifted r_c to that closed subspace. A minimizing sequence is Cauchy by the parallelogram identity, since its pairwise midpoint is still in the subspace. Its Hilbert limit alpha attains the minimum. Variations by every subspace vector give orthogonality. Uniqueness follows by taking the difference of two projections. Since every G indicator is in this finite-measure L2 subspace,

integral_A alpha dm=integral_A r_c dm for every A in G.

This is precisely the conditional-expectation property; bounded G-measurable tests follow by simple approximation and dominated convergence. The same construction applies to r_c².

A completion-measurable L2 function has a G0-measurable version: approximate by a sequence of simple functions and replace each of their countably many completed level sets by its G0 representative modulo m-null sets. Their pointwise finite limit, set to zero elsewhere, is G0-measurable and represents the same class. Equivalently the subspace may be described directly by such progressive versions. This pays the representative assertion without an unprovided progressive-version/optional-projection theorem.

Here r_c=c/(c+sqrt(U)) is a bounded measurable **terminal random variable**, lifted constantly in time. E1 gives finite U almost surely, so0<r_c<=1 m-almost everywhere. Values on the exceptional P-null set can be assigned arbitrarily consistently; none of the equalities divides by infinite U. The construction never asserts that r_c itself is adapted or multiplies it through the SDE.

Testing the conditional identity on the G sets where alpha<0 or alpha>1 gives0<=alpha<=1. On A={alpha=0}, positive m(A) would give integral_A r_c>0 but integral_A alpha=0. Hence alpha>0 m-almost everywhere. A progressive representative can be reset on its progressive null exceptional set to a value in(0,1], retaining all identities. There is no asserted uniform positive lower bound.

Multiplication of the progressive representatives alpha and w is progressive. Such m-null modifications do not change the input's time-integral class. Once its E2 estimate below is established, equal input versions have zero L2 difference; fixed delays and R preserve this equality, and Itô isometry/strong uniqueness give the same actual state, control and output. Thus completion cannot insert anticipative forcing or a different physical response.

## 6. Squared inequality with nonintegrable input energy, and every nonzero/zero boundary

Construct beta=E_m[r_c²|G] by the same projection. It is bounded between0 and1. For every bounded nonnegative G-measurable q, the tests q and q alpha are legitimate L2 tests because alpha is bounded and m finite. Expand the nonnegative integral:

0<=integral q(r_c-alpha)² dm
  =integral q beta dm-integral q alpha² dm.

Thus alpha²<=beta almost everywhere. This proves the needed conditional-square inequality rather than presuming Jensen with an inadmissible weight.

Now q_n=min(|w|²,n) is bounded progressive for every n. The conditional identity for beta gives

integral q_n alpha² dm<=integral q_n beta dm
                         =integral q_n r_c² dm.

Monotone convergence on both nonnegative sides yields the same inequality with |w|² even when its m integral is infinite. Tonelli is applicable to the nonnegative, possibly initially nonintegrable quantities. Because r_c is time-constant, the right side is exactly

E[r_c² U]=E[c² U/(c+sqrt(U))²]<=c².

The scalar expression is well-defined on the almost-sure finite-U set, with value0 at U=0; c>0 prevents any zero denominator. All identities are assertions up to the original null conventions, not evaluations at a chosen U. Consequently v=alpha w, zero outside J, satisfies E integral_J|v|²<=c² and is an actual E2 input.

A nonzero E1 disturbance has positive probability of positive path norm, equivalently its time-product nonzero set has positive m measure. Strict alpha positivity retains that nonzero set, so v is not the zero input. Fubini gives, almost surely, identical time-zero support and pointwise channel direction wherever w is nonzero. On zero-energy paths v is also zero, with no division by ||w||. No lower bound on alpha or initial-information event is needed.

Cauchy–Schwarz in probability gives E||v||<=sqrt(E||v||²)<=c, and alpha<=1 gives ||v||<=||w|| pathwise. Nonzero v gives E||v||>0. Hence exactly

0<E||v||<=min(c,E||w||).

This includes w already in E2, infinite E U, all zero-support portions, individual zero channel components and arbitrary positive c. It asserts no c=0 case or c-limit/equality-preserving approximation.

Applying §4's E2 SDE theorem supplies the actual original X_v,u_v,z_v on **all of I**, not only J. The input is zero on(S,T], but delayed forcing, the state and output tail there are not discarded. Zero/degenerate plant matrices cause no problem: the input remains nonzero even if the actual output is zero. No claim of global E1 state/control energy for the original w is needed.

## 7. Exact time-path angle criterion, not an operator equality

Outside one probability-null set, fix any nonzero input path in the Hilbert space L2(J;R^p). Its v=alpha w has finite norm, and

<v,w>=integral_J alpha(t)|w_t|²dt>=0.

Cauchy–Schwarz gives

A_c=||v||-<v,w>/||w||>=0.

The nonnegative inner product also gives A_c<=||v||, so A_c is integrable. Its definition is measurable from the norms and integral; on zero input paths it is set to zero and v is zero as already proved.

On a nonzero path, Hilbert equality holds iff v is a nonnegative constant multiple of the **whole path** w. Strict alpha positivity makes that scalar positive. Since v(t)=alpha(t)w(t), this is exactly alpha(t) constant with respect to the measure |w_t|²dt on that path. The condition concerns the whole time path, not merely parallel channel vectors at each time. Conversely that weighted constancy gives A_c=0 directly. No assertion of positive A_c for some physical input or constancy from projection is supplied.

Even such pathwise collinearity would not by itself license pulling an unrevealed random path scalar through the original Itô equation. The candidate does not infer such an output identity, and this review does not supply one.

## 8. Original feedforward commutator, endpoints and the exact unpaid face

For any bounded progressive scalar alpha on I, form alpha w using the given zero-extended input. Choose consistent bounded extensions on negative times and outside J when needed; the candidate regularizer can use zero extension after S. Multiplying by bounded alpha retains all required local input integrability. Directly expand the same deterministic feedforward map:

R(alpha w)(t)-alpha(t)Rw(t)
 =Lh[alpha(t-h)-alpha(t)]w(t-h)
  +integral_0^h H(r)[alpha(t-r)-alpha(t)]w(t-r)dr.

The current tap cancels exactly. All equalities are in the natural time/path almost-everywhere process sense for L2 inputs, where the integrals are defined; endpoint representative choices do not alter the original time/Itô equations. If a lagged time is negative or outside J, that input is zero. At t=0 the same zero history applies; at the delay or input-end boundary there is no extra impulse or division. For h=0 both differences vanish and the integral is absent, consistently with combining the two current taps.

No differentiability or semimartingale structure of alpha was used, and no product rule for alpha X was invented. The formula names possible unproved commutations; it neither exhibits a nonzero commutator for a chosen law nor proves that every nonconstant alpha fails. Even if the feedforward commutator vanishes, the dynamic state/output map is not thereby proved to commute with alpha.

Under the task's finite common endpoint gamma>0, §4 gives the finite nonnegative actual-input deficit

D(v)=gamma E||v||_J-E||Z(v)||_I for every E1 v.

The assumed strict inequality on every nonzero E2 input therefore gives D(v_c)>0, because the regularizer is genuine nonzero E2. If an original E1-only endpoint attainer w existed, D(w)=0 would **not** contradict this: no theorem here gives D(v_c)=0 for any c. To prove transfer through this construction one still needs a uniform actual-SDE equality/face-preservation implication, or a different admissible equality-preserving regularization. Supremum equality, output continuity, pointwise input alignment or the finite energy bound do not provide it.

This is **NR-ENDPOINT-FACE**, exactly as the candidate states, not an undisclosed essential premise of the proved input theorem. No endpoint attainer, counterfamily, strict angle/commutator example, impossibility theorem or all-route exhaustion is asserted. The unused energy-split/revealed-amplitude arguments in S7 are context, not a hidden premise of these conclusions.

## 9. Final boundary/NR ledger and assurance

- **Fully paid:** finite positive product measure; closed progressive L2 subspace and projection; completed-to-progressive representative; strict positivity and upper bound; conditional-square inequality with bounded tests; nonintegrable |w|² via truncation/monotone/Tonelli; finite controlled E2 energy and nonzero first moment; zero supports/paths and every c>0; actual unchanged-law E2 state/control/output; exact path-angle equality and memory commutator with all zero/history/delay boundaries.
- **Used named SDE import:** finite-horizon strong existence/uniqueness/linearity for progressive square-integrable forcing and its Itô-isometry conventions, applied explicitly in §4. It is an admitted ordinary theorem, not a newly formalized proof or an external source retrieval.
- **NR-ENDPOINT-FACE:** full uniform strict endpoint transfer, actual output multiplier/intertwining and equality-preserving regularizer are not proved. No reverse inference from the newly constructed E2 process is accepted.
- **Outside this exact dependency scope:** infinite-horizon/global state-control E1 bounds, deterministic-reference optimization, calibration, general synthesis/book admissibility and unused prior-context theorems. No broader caller is silently paid.
- **NR provenance/source/novelty:** dossier/book-image equivalence, source-history/noninfluence, current worldwide status, novelty/priority and clean cognition are not certified by correct algebra.

The parent public-source/search/excerpt freeze S10–S12 is binding; only this already-pinned disjoint written duty was performed, with no new discovery/fetch/extraction. The author's selected-reference and older annihilation episodes, own semigroup STOP/ENTIRE171, parent L1 and all their consumers remain HELD/ZERO/NONINPUT. All earlier findings, HOLDv2, N4 UNKNOWN/historical child exit unestablished and auxiliary214 STOP persist.

This return is same-harness WRITTEN support only, not Main adoption, formal/kernel/human/configured-family/executable/independent-model or novelty acceptance. Main must itself read the complete operative sources and actual return, retaining every boundary above, before disposition.
