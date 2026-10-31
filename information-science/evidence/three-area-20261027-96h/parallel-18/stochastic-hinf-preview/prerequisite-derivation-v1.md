# Literal expected-norm feasibility: an exact noise-free synthesis transfer

**WRITTEN author result, UNREVIEWED.** Native prewrite observation: **Tue Oct 27 14:48:03 PDT 2026**. No scientific calculation/program, legacy proof or proposed source was used. This is a stated-class coupling theorem, not general stochastic synthesis, an algebraic controller construction, a book-equivalence certificate or a novelty claim.

## 1. Inputs, provenance and explicit interpretation

The pre-body ACK is `S1-prebody-exposure-and-allowed-input-ack-v1.json`, written before opening the definition packet. The entire 55-LF packet `info-3-literal-criterion-packet-v1.md` was then read, SHA-256 `888307a4a094bc5fa7aca45484334f8a12b75e9fb3e86259d81acf31cad629f3`, together with its complete equality receipt. The packet gives the canonical dossier transcription, not a new book-image check:

`dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW`, `z=D0x+D1u`,

and the criterion `E ||z||_L2 / E ||w||_L2 < gamma`. S2 explicitly leaves interpretation of adaptedness, initial condition, window extension, strictness and information pattern to the author. Only these literals, the current safe intake/controls, and the elementary facts listed below are used. No v33–v57 argument, v248-reported method, storage identity, realization guide or changed-output construction is an input.

Adopt the following interpretation for this theorem, without asserting that every original-book interpretation has these properties.

- Dimensions n,m,p,q are arbitrary positive integers. A,B,C,A0,B0,D0,D1 are arbitrary real matrices of the displayed compatible sizes. The proved plant class is **A0=0 and B0=0**; every other matrix is unrestricted. There is no stabilizability, rank, invertibility or positivity hypothesis.
- Initial state and disturbance history are zero. The filtration is the completed canonical filtration of the one Brownian motion in the supplied model.
- For finite horizon, shift the starting time a to 0 and write T=b-a, with finite h>=0 and **T>h**. The disturbance domain is J=[0,T-h], output domain I=[0,T]. Extend w by zero outside J, including negative times. For infinite horizon I=J=[0,infinity), with the same finite h and zero negative-time history. A translation by a is only notational; no horizon quantifier is exchanged.
- Disturbances are all progressively measurable processes with `E integral_J |w|^2 < infinity` and `0<E ||w||_J<infinity`. This is the canonical progressive E2 domain, while the numerator and denominator remain expectations of pathwise norms. No RMS replacement is made.
- A law F is deterministic and stationary with precisely the displayed current-state/full preview-window information: `u(t)=F(x(t),w|_[t-h,t])`. At h=0 use the present value w(t). Laws are required to be well-defined modulo input changes on time-null sets. No extra Brownian history, private randomization, arbitrary past-state memory or input-dependent choice of F is added.

Define K_h(I) to contain those such F for which the following **admissibility hypotheses**, not unproved conclusions, hold: every deterministic v in L2(J) has a unique global-on-I closed-loop trajectory with local pathwise control-L2 and no finite-time explosion; its input/output map S_F:v->z is measurable (into local path spaces, with measurable extended global norm); and its samplewise lift to each progressive E2 input is the same unique progressive, locally pathwise-L2 solution. In particular, for this noise-free plant,

`z(omega)=S_F(w(omega))` almost surely, with the SAME F and original matrices on both sides.

These hypotheses restrict the controller class explicitly. They do not demand expected control-L2 or a homogeneous/linear law. They do not assert that every merely stochastic-a.s.-well-posed law in a different interpretation belongs to K_h(I). No controller is synthesized by declaring it a member.

## 2. Actual-object gains and theorem

For F in K_h(I), define

`d(F)=sup_{0!=v in L2(J)} ||S_F(v)||_I / ||v||_J`,

`l(F)=sup_{progressive E2 w, E||w||_J>0} E||S_F(w)||_I / E||w||_J`.

Both suprema take values in [0,infinity]. Let `o(F)=||S_F(0)||_I`, also extended-valued on the infinite horizon. These are values for the actual original output and the actual fixed law, not an auxiliary output or a relaxed per-input control.

**Theorem A (lossless transfer, including the zero-input obstruction).** For every admissible dimension/matrix tuple, horizon and F above:

1. If o(F)=0, then **l(F)=d(F)** in the extended reals.
2. If o(F)>0, then **l(F)=infinity**. This requires neither continuity at zero nor linearity of F.
3. For each gamma>0, the printed **pointwise-strict** requirement (ratio<gamma for every admitted nonzero stochastic input) holds iff o(F)=0 and `||S_F(v)||_I<gamma ||v||_J` for every nonzero deterministic v. No common strict margin is asserted by this equivalence.
4. The **uniform-strict** requirement l(F)<gamma holds iff o(F)=0 and d(F)<gamma. Thus it is equivalent to one deterministic bound with a common constant k<gamma.

This removes the entire optimization over Brownian-adapted random disturbances for this plant/controller class. It does not replace one expectation convention by another, change the law, choose a different law for each path, or weaken legal control admissibility.

## 3. Proof: deterministic witnesses and pathwise lift

Assume first o(F)=0. Every nonzero deterministic input is progressive E2 and is an actual caller of the stochastic problem, with the same trajectory and law. Hence l(F)>=d(F).

If d(F) is finite, its definition gives `||S_F(v)||<=d(F)||v||` for every deterministic v!=0, and the same inequality at v=0 because o(F)=0. A progressive E2 input has an L2(J) path almost surely, so the stipulated samplewise lift yields

`||S_F(w(omega))||<=d(F)||w(omega)||` almost surely.

Taking expectations proves l(F)<=d(F). The expected denominator is finite by Cauchy-Schwarz on the probability space. This also establishes numerator integrability when the deterministic bound is finite. If d(F)=infinity, the deterministic-witness lower bound already gives l(F)=infinity; no invalid multiplication of infinity by a zero norm is used. This proves item 1, including d(F)=0.

For pointwise strictness, suppose the deterministic inequality is strict for each v!=0 and o(F)=0. For any admitted random input the gap

`Delta(omega)=gamma ||w(omega)||-||S_F(w(omega))||`

is nonnegative, bounded above by the integrable random variable gamma||w||, and strictly positive on {||w||>0}. That event has positive probability because E||w||>0. The elementary strict-positivity property of expectation gives E Delta>0, proving the literal strict inequality. Conversely deterministic inputs give every required deterministic strict inequality; item 2 below forces o(F)=0. This proves item 3 once item 2 is established. Item 4 follows from items 1–2. No maximizer or uniform separation from gamma is assumed for item 3.

## 4. Proof: the zero-input branch is a real admissibility constraint

Suppose o(F)>0. Choose arbitrary tau>0 within J with nonzero time remaining, and any nonzero deterministic v in L2(J) supported strictly after tau. Such a v exists whenever finite T>h; it also exists on the infinite horizon. This is a quantified symbolic construction, not a selected numerical or boundary probe.

By nonatomicity of the Brownian marginal at tau, for every probability parameter r in (0,1) there is an event A_r in F_tau with P(A_r)=r. Define the disturbance

`w_r(t)=1_(A_r) v(t)`.

It is progressively measurable because v vanishes until after tau. Its expected squared energy is `r ||v||^2`, hence finite; and `E||w_r||=r ||v||>0`. The controller remains exactly F. The law's pathwise lift gives output S_F(v) on A_r and S_F(0) on its complement; there is no conditional-independence assumption, since the plant and law have no direct Brownian dependence once the input path is fixed. Local pathwise control admissibility/nonexplosion follows on each of the two deterministic paths from K_h(I), without expected control-L2.

Consequently

`E||z_r|| >= (1-r) o(F)`.

If o(F)=infinity, the numerator is already infinite for every such r. If 0<o(F)<infinity, the literal ratio is at least `(1-r)o(F)/(r||v||)`, which is unbounded as r decreases to zero. This proves item 2 and completes Theorem A. The random input is never globally zero as a random variable, even though it is zero on a positive-probability event; excluding the globally zero disturbance does not remove that branch.

## 5. Synthesis consequence with unchanged common-law quantifiers

Define the deterministic synthesis condition D_gamma on this same class as existence of **one F in K_h(I)** with o(F)=0 and d(F)<gamma. Define the literal uniform synthesis condition L_gamma as existence of **one F in that same class** with l(F)<gamma. Theorem A proves

**D_gamma iff L_gamma**, with the identical F witnessing both directions.

The deterministic optimal threshold equals the literal optimal threshold if the deterministic objective is defined as d(F) for zero-output-zero-input laws and infinity otherwise. Infima over an empty class are infinity. This is an exact reduction to deterministic preview synthesis, not a solution or a claimed finite-dimensional N&S test for that remaining deterministic synthesis problem.

For pointwise strict synthesis use, instead, one F with every nonzero deterministic ratio<gamma and o(F)=0. Do not replace that by d(F)<gamma: the supremum can equal gamma without a deterministic input attaining it. The theorem preserves this distinction without claiming that a particular plant realizes an unattained endpoint.

The theorem applies separately to each finite T>h and to the infinite horizon. If a problem requires the same F for several horizons, retain that common-F quantifier on both sides. If it permits a different F at each horizon, retain that different quantifier. No finite/infinite-horizon implication, limiting controller or attainment is asserted.

## 6. Degeneracies, imports and exact remaining gap

Zero C, B, D0 or D1, nontrivial unobservable modes, singular matrices, zero deterministic gain and absent finite gain are all included; no division by a plant parameter occurs. Nonzero output at zero disturbance is handled by item 2. If p=0, or finite T<=h makes the adopted disturbance interval empty/nonpositive, there is no admitted nonzero disturbance denominator: the ratio problem needs a separate convention, and this theorem does not declare it solved with gain zero. No infinite preview h or nonzero initial state is covered.

Ordinary facts used are: deterministic-input inclusion in the progressive E2 class; the stipulated pathwise uniqueness/lift; Cauchy-Schwarz for E||w||; monotonicity and strict positivity of expectation of nonnegative random variables; and nonatomicity of a Brownian marginal at positive time. No stochastic-flow energy identity, martingale-dual theorem, storage/Gramian, Riccati/LMI condition, controller realization or legacy proof is imported. All algebra is displayed symbolically; nothing is machine-checked.

**NR-SOURCE:** S2 is a canonical-dossier transcription. Source/book-image equivalence and unprovided original admissibility conventions remain unestablished. **NR-K:** robust pathwise well-posedness/measurability and the lift are explicit controller-class hypotheses, not proved for all original legal laws. **NR-NOISE:** for A0 or B0 nonzero, deterministic input paths generally still have random outputs; the deterministic pathwise lift used in sections 3–4 is unavailable. **NR-SYNTHESIS:** D_gamma is not yet an algebraic constructive criterion, and no general noisy-plant controller or obstruction has been supplied.

What changes: an all-matrix noise-free-class exact literal synthesis transfer, including a zero-input random-branch obstruction and the strictness/actual-law caller. What does not change: the original general stochastic synthesis target remains OPEN; all prior adopted results retain their old scope, all unreviewed/held candidates remain noninputs, and every STOP/HOLD/ZERO and process finding persists.

## 7. Next genuinely admitted branch

Next analyze the NR-NOISE failed implication by separating a physical plant's Brownian randomness from an independent input-law mixture, using only the supplied matrices, a measurable strong-solution hypothesis and elementary product integration. The concrete question is whether a deterministic-input expected-norm bound lifts exactly to independent mixtures, and precisely which conditioning step fails for the original Brownian-adapted inputs. This will not assert that independent disturbances equal the original domain, enlarge the original admissible controller class, or invoke excluded controller/energy methods.
