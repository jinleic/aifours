# Review w25 — preview diagonal/graph-law obstruction

**Reviewer:** MathSemigroup-2 (math-4). **Author:** InfoHinfPreview-2 (info-3).

Actual first review-wake clock: **Tue Oct 27 15:16:40 PDT 2026**. Actual pre-body ACK clock: **15:16:57**. Actual native observation immediately before writing this review: **Tue Oct 27 15:19:30 PDT 2026**.

## 1. Verdict and essential scope

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE.**

- FATAL: **0**.
- MAJOR: **0**.
- MINOR: **0**.

The noise-free fixed-law transfer, zero-input random-branch obstruction, independent-mixture theorem and canonical graph-law decomposition are correct under the explicit input/controller/probability-space hypotheses below. The two packets do **not** identify a general noisy stochastic response by conditioning on its adapted disturbance. They correctly leave **NR-DIAGONAL** and **NR-COUPLING** unpaid and make no physical counterexample from graph singularity alone.

**Important reading precision:** the literal noise-free theorem says `o=0 => l=d`, and `o>0 => l=infinity`. Since d may itself be infinity, do not restate this as `l=d iff o=0` in the extended reals. The source does not make that stronger converse. Zero-input zero-output is necessary for any finite-threshold feasibility, not inferred merely from equality of two infinite gains.

## 2. Mandatory reading order and exposure

I read S0 completely, then the complete frozen manifest, SHA `c40a490b45abcdb182e508de65e7f20443ea5f89a82481dc122865198908cb11`. Before opening any packet body or mathematical reasoning I wrote:

`review-w25-preview-diagonal-graph-obstruction-prebody-ack-v1.json`, SHA `5594276d0c54fa98fe6c31faad18758fe58e0ecdbaef9e5f8e2382502927931c`, actual clock15:16:57.

Then I read the entire **276-LF / 33276-byte** frozen packet, SHA `2ecf7bf3a8f0a055a9caf1c5ea45276ce48a9ee9a9bacfb53a75cd12a6d8b2ca`, in raw windows **1–60, 61–120, 121–180, 181–240, 241–276**, including all endings and long lines. Outer source labels:

| Source | Complete literal body | SHA-256 |
|---|---:|---|
| S1, scope/printed-criterion transcription | 55 LF | `888307a4a094bc5fa7aca45484334f8a12b75e9fb3e86259d81acf31cad629f3` |
| S2, noise-free transfer | 102 LF | `f38fa78a0d1747771dbcafd18320cc593c1a90faf25fa6b862d52754f9097672` |
| S3, independent/adapted coupling | 107 LF | `755e7492d131c334454a673c8aa1dd9643ce85a77609dc56b901f5b05c0012d0` |

Prior contact survives: I previously authored Preview reviews (including v143-B and the short-horizon-opposite review), and read Preview-authored semigroup full-Rees/corner-compression material historically. These contacts are disclosed in the ACK; no old body, old verdict or private guide was reopened/transferred. This is not blind or independent-model evidence. My own semigroup excluded-route STOP is retained and supplies no mathematics here.

Only these frozen sources and the elementary facts explicitly reconstructed below are mathematical inputs. No author contact, extra source, legacy proof/checkpoint/park, public paper, held/corrective guide, scientific interpreter, calculator/Eval/CAS, selected plant/input/probe, solver, replay, test, execution or nested agent was used. Only the ACK and this review were written. Parent complete source/return reading and any adoption remain separate duties.

## 3. Claim dispositions and exact caller boundaries

| Literal claim | Mathematical verdict | Scope/import consequence |
|---|---|---|
| S2:15–25, controller/input interpretation | Explicit and coherent | Arbitrary compatible real matrices/dimensions, but A0=B0=0 for TheoremA; zero initial/history; finite T>h or infinite horizon; canonical progressive E2; one deterministic stationary law satisfying the stated robust pathwise K hypotheses. |
| S2:37–54, zero-output equality | CORRECT in extended reals | Uses samplewise deterministic ODE lift, not a stochastic-integral version or independent conditioning. |
| S2:64–76, nonzero zero-input obstruction | CORRECT | Requires the actual canonical Brownian filtration at a positive time, a nonzero input supported later, and K's samplewise lift. No continuity or linearity at zero. |
| S2:41–42,56–60, strictness | CORRECT | Pointwise strict for each input is distinct from a uniform common strict margin; no attained supremum is assumed. |
| S2:80–88, synthesis transfer | CORRECT for the same K class | Same one F both ways. The deterministic objective is modified to infinity when o>0; no general algebraic constructive criterion or finite/infinite limiting controller follows. |
| S3:22–38, independent-mixture threshold | CORRECT | Requires a measurable f and, for physical use, a product-caller lift. Nontrivial independent mixtures may require a product probability-space extension and are not identified with canonical adapted inputs. |
| S3:42–50, density bridge | CORRECT conditionally | Requires actual Q<=M(mu x P), e(v)<=H||v|| and the appropriate actual response caller. No domination for general adapted inputs is assumed. |
| S3:56–78, graph-law theorem | CORRECT | Canonical full-path measurability V=Phi(W), standard Borel/separable path spaces. Purely nonatomic input law gives mutual singularity; mixed laws have the stated singular part; bounded density exactly for finite atom support. |
| S3:82–99, diagonal/version obstruction | CORRECT | Slice-wise or product-a.e. response versions need not identify the actual adapted diagonal response. The source expressly does not alter a physical output or claim a physical counterexample. |
| S2:92–98/S3:96–107, excluded/general cases | ACCURATE | NR-SOURCE, NR-K, NR-NOISE/NR-SYNTHESIS and NR-DIAGONAL/NR-COUPLING prevent upgrading this to the full printed noisy synthesis problem. |

## 4. Noise-free gain theorem: direct reconstruction

### 4.1 Precise adopted model

The printed quantity is `E||z|| / E||w||`, with the square root inside each pathwise norm, not an RMS ratio. The source makes the following interpretation explicit rather than attributing it silently to the book:

- zero initial state and zero negative-time history;
- finite output I=[0,T] and input J=[0,T-h] with T>h, or I=J=[0,infinity) for finite h;
- positive input dimension and canonical progressive processes with finite expected **squared** input energy and positive expected path norm;
- one deterministic stationary law with current x and the displayed preview window, no extra W-history/private randomization;
- robust deterministic-path global existence/uniqueness, measurability, local control-L2/nonexplosion, and the samplewise progressive lift are **hypotheses defining K**, not existence results.

Under A0=B0=0, those K hypotheses give the actual `z(omega)=S_F(w(omega))` with the same law and original output. This is the key physical caller. It is not automatic for every alternative merely a.s.-well-posed controller class.

### 4.2 o(F)=0 gives exactly l(F)=d(F)

Every fixed nonzero v in L2(J) is a deterministic progressive E2 input and gives the same output, so l>=d. If d<infinity, its definition bounds ||S_F(v)||<=d||v|| at every nonzero deterministic v and at zero because o=0. A progressive E2 input is an L2(J) path almost surely. The stipulated samplewise lift therefore gives the same inequality on each random path, including paths that are zero.

Cauchy–Schwarz on the probability space makes E||w|| finite from E||w||^2<infinity. Taking expectations proves l<=d and numerator integrability. If d=infinity the deterministic-input lower bound already makes l=infinity; no expression infinity times zero is used. d=0 is included.

This is a pathwise bound integrated over the **actual** coupled paths; conditioning on w and replacing a conditional Wiener law never occurs.

### 4.3 Positive zero-input output gives an actual canonical random-branch obstruction

Fix any positive tau strictly within J with time remaining and any nonzero deterministic v supported strictly after tau. The finite assumption T>h and positive input dimension ensure such functions exist; the infinite horizon does also. No parameter is evaluated or selected as a test.

A one-dimensional Brownian marginal at positive tau is nonatomic, so for every r in (0,1) there is an event A_r in F_tau of probability r. Set w_r=1_(A_r)v. It is progressive: before tau it is zero and afterwards the selecting event is already measurable. Its squared expected energy is r||v||^2, and E||w_r||=r||v||>0.

The K lift yields S_F(v) on A_r and S_F(0) on its complement, with **the same law F**. This remains correct even though A_r depends on W, because no direct W coefficient remains in the plant/law once the input path is fixed and the samplewise caller is explicitly assumed. Thus E||z_r|| >= (1-r)o.

If o=infinity this is already infinite. For finite o>0, dividing by r||v|| gives an unbounded lower bound as r decreases to zero. This proves l=infinity without continuity, homogeneity, linearity or expected-control-L2 assumptions. Global nonzeroness of the input random variable does not exclude its positive-probability zero-input branch.

### 4.4 Strictness and common law

Assume all nonzero deterministic ratios are strictly below gamma and o=0. Then Delta=gamma||w||-||S_F(w)|| is nonnegative and integrable, and positive on {||w||>0}, an event of positive probability. Hence E Delta>0, proving the printed stochastic strict ratio. Deterministic callers prove the converse deterministic strict inequalities, while §4.3 forces o=0 for any finite gamma requirement.

Uniform strictness is l<gamma iff o=0 and d<gamma. This is not equivalent to the pointwise strict condition when a supremum might equal gamma without attainment. The source makes no claim that an actual selected plant realizes that endpoint.

Taking existence over **one common F in the same K** gives the stated synthesis equivalence. It is not optimization over separate path-dependent laws and not an algebraic controller construction. Empty feasible classes, zero gains, singular/zero plant matrices and infinite output norms are covered as stated. p=0, finite T<=h, nonzero initial state, infinite h, and different controller/input interpretations are explicitly outside this theorem.

## 5. Independent comparison and domination: direct reconstruction

Let f(v,omega)>=0 be jointly measurable and e(v)=int f(v,omega)P(domega), with e(0)=0. Tonelli gives `int f d(mu x P)=int e dmu` for each independent input-path law mu. Finite second input moment implies finite first norm moment; positive first moment supplies a valid denominator.

For finite H=sup_(v!=0)e(v)/||v||, the pointwise bound including zero integrates to the H ratio upper bound. Dirac input laws give every deterministic ratio and hence the reverse supremum. If H=infinity those same deterministic callers give an unbounded supremum. Pointwise strictness is paid by the positive integrable gap gamma||v||-e(v) on nonzero inputs; uniform strictness needs H<gamma. The two notions are not interchanged.

If e(0)>0, independent mixtures assigning small positive mass to a nonzero input and the rest to zero have unbounded ratios. This is a comparison model: independent randomized paths can be realized on a product extension. It is not a claim that the original completed canonical Brownian filtration contains extra independent initial randomness. Indeed V measurable with respect to the entire W path and independent of it is independent of itself, so every Borel event of V has probability0 or1; on a standard Borel path space this forces a deterministic V a.s.

For physical use, separate deterministic-input solutions do not by themselves supply a jointly measurable parameterized strong solution representing independent random inputs. S3:13–18 states this as the **product caller**, and separately requires the **adapted caller** when substituting V=Phi(W). Those premises are not reconstructed from the literal matrices.

If Q<=M(mu x P) actually holds, monotonicity of integration gives E_Q f <= M int f d(mu x P) <= M H E_mu||V|| at the stated finite-gain/positive-denominator caller. This argument is correct as a conditional implication only, not a proof of either domination or a sharp physical gain.

## 6. Canonical graph-law theorem: complete reconstruction

### 6.1 Exact probability-space hypothesis

E=L2(J) is separable Hilbert. The finite- or infinite-horizon continuous Wiener path space with the specified topology is standard Borel. A canonical progressive E2 input gives a full E-valued random variable measurable with respect to the completed full Wiener sigma-field. The stated measurable-factorization/version fact gives a Borel Phi with V=Phi(W) almost surely. This is the named ordinary factorization input; it does not assert a parameterized stochastic solution map.

The theorem is for this **canonical dependence**. An adapted input on an enlarged filtration carrying external randomness need not be a function of W alone and is not covered by this graph conclusion. An independent non-atomic input law is therefore not in conflict with the theorem.

Let mu=Law(V), R=mu x P, Q=Law(Phi(W),W), and Gamma={(v,omega):v=Phi(omega)}. The graph is measurable: the distance ||v-Phi(omega)|| is measurable and Gamma is its zero set. The atom set D is at most countable and hence measurable.

### 6.2 Nonatom graph is singular

For each omega, R's conditional mass at the graph point is mu({Phi(omega)}). On Phi(omega) outside D this is0, so Tonelli gives R(Gamma outside D)=0. But Q puts mass mu(E\D) there. If that mass is positive Q is not absolutely continuous with respect to R. If it is1, Q is concentrated on an R-null set, hence Q and R are mutually singular.

This proves the nonatomic/mixed statements without assuming any density exists.

### 6.3 Atomic density and total mass

For atoms v_i with p_i=mu({v_i})>0, define

r(v,omega)=sum_i 1_(v=v_i)1_(Phi(omega)=v_i)/p_i.

For any nonnegative measurable g, the i-th term integrates against R to

p_i/p_i · int_(Phi(omega)=v_i) g(v_i,omega)P(domega),

exactly Q's integral on {V=v_i}. Countable Tonelli sums these terms; their total mass is sum_i p_i. The remaining Q mass is the already identified singular graph on nonatom values. Thus this is the complete absolute-continuous/singular decomposition, not just a candidate density with a missing residual piece.

Each nonzero density level1/p_i occurs on R-positive set {v_i} x {Phi=v_i}, of measure p_i^2. Hence its essential supremum is sup_i 1/p_i. Purely atomic finite support has the exact least domination constant1/min_i p_i. Infinite positive atoms cannot have a uniform positive lower mass, so their density is unbounded and no finite M works. A nonzero nonatomic component prevents domination regardless of how bounded the atomic density is.

Therefore Q<<R iff mu is purely atomic, and finite domination holds iff mu is concentrated on finitely many atoms. Deterministic one-atom laws give Q=R and least M=1. The graph theorem may include the zero deterministic law even though that law alone is not an admitted nonzero gain denominator; its application to a gain still requires the original denominator convention.

## 7. Why the diagonal caller really remains unpaid

For entirely nonatomic mu, every fixed deterministic slice {omega:Phi(omega)=v} is P-null. Yet the whole graph has Q-probability1. The measurable indicator of this graph can therefore alter a jointly measurable version on every actual diagonal point without changing **any fixed-v P-a.s. slice statement**. It also changes no product-a.e. statement.

This proves the exact quantifier gap: `for every fixed v, for P-a.e. omega` does not justify substituting the adapted V=Phi(W) inside that assertion. It does not authorize modifying the physical output of the SDE. Actual joint/coupled solution identification must be established by the physical model and one lawful common F.

The second attempted inference is also unpaid: conditioning on V generally changes W's law; the full joint graph measure is not a product, and in the nonatomic canonical case has no finite product-law domination at all. Thus deterministic-input **Wiener average** bounds cannot simply be reused as conditional expectations for adapted inputs.

Neither conclusion is a physical noisy-plant counterexample or a general impossibility theorem. A structural pathwise response bound could avoid a product density entirely, as S2's noise-free class does. The source correctly keeps both NR-DIAGONAL and NR-COUPLING, rather than declaring every general synthesis condition false.

## 8. Imports, unresolved original target and assurance

Paid mathematical inputs are elementary deterministic-input inclusion, pathwise lifting **as an explicit K hypothesis**, Cauchy–Schwarz/strict positivity of expectation, nonatomic Brownian marginals at positive time, Tonelli, standard-Borel/separable measurable factorization, countability of atoms, and the explicit measure decomposition. No Girsanov theorem, stochastic-flow estimate, stochastic integral construction, storage/Riccati/Gramian, controller realization or legacy argument is imported.

Limits remain exactly:

- **NR-SOURCE:** no book-image/transcription equivalence or missing original conventions were verified.
- **NR-K:** robust all-path well-posedness/measurability is a stated controller-class restriction, not proved for all legal stochastic laws.
- **NR-NOISE:** noisy diffusion lacks S2's deterministic pathwise output map.
- **NR-SYNTHESIS:** the deterministic objective is not an algebraic constructive N&S controller theorem.
- **NR-DIAGONAL/NR-COUPLING:** actual noisy coupled response identification and the needed structural dependence control are unproved.

The full original finite- and infinite-horizon stochastic synthesis target remains OPEN. Same-F/different-F horizon quantifiers must be carried exactly as the chosen problem states; no limiting controller or horizon equivalence is inferred. The printed expectation-of-path-norm criterion is never replaced by RMS.

All STOP/HOLD/ZERO/process findings, N4 UNKNOWN with historical child exit unestablished, and auxiliary214 STOP remain. This review is same-harness WRITTEN support at the frozen scope only—not parent adoption, formal/kernel/human/configured-family/executable/independent-model, public-status or novelty clearance.
