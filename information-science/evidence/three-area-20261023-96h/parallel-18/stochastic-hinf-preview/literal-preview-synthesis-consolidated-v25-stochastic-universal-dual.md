# Risk-retaining plant-only dual tests for EVERY original controller — stochastic output pricing and a complete matrix calibration

Owner **InfoHinfPreview-2 / info-3**. Actual preceding returned `/bin/date`: **Mon Oct 26 10:10:52 PDT 2026**. **NEW COMPLETE WRITTEN OWNER-CANDIDATE**, not reviewed/adopted. All-variable/source-fixed conventional proof only; no chosen numeric/physical-state/control/boundary/magnitude/decimal viability probe, scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay/build/test/CLI/nestedagent/newGO. No identity is claimed machine-checked.

## 0. Exact new edge and what this is NOT

V17's output-priced adjoints were DETERMINISTIC and could retain only selected mean-output pairings. V23's stochastic BSDE retained risk, but was attached to ONE FIXED LINEAR full-window controller and legitimately used its state/control second moments. Neither statement provided a stochastic, risk-sensitive NECESSARY test for EVERY original unknown nonlinear controller when unpriced state/control expectations can fail.

This successor supplies that test. A RANDOM adapted adjoint satisfies an exact plant-only control-annihilation constraint. Its product diffusion is priced by the ACTUAL output. Only this single scalar product martingale is proved H1, without E X, E u, expected control energy, full-state diffusion H1, NEO, R inverse, STATE-LOC or linear-controller optimality. The correct input dual remains the ADAPTED quotient norm, not the essential path supremum of a progressive adjoint.

The WHOLE test family has an equivalent finite-matrix stochastic descriptor with no q variable or control-price inverse. Its supremum is necessary for ANY original admissible controller at ANY matrix ranks and finite preview h. This is not claimed sufficient for actuated plants or causal/stationary controller synthesis.

A substantive completeness calibration is also proved: for the ENTIRE all-variable UNCONTROLLED constant-matrix class with full-column-rank D0, these bounded output-priced stochastic tests recover the EXACT finite-horizon literal gain. Smooth finite-Brownian-cylinder tests suffice; bounded adjoint diffusion is proved using the forward matrix flow/Gaussian semigroup, without commuting A,A0, a Girsanov shortcut or an opaque bounded-q assertion. Infinite gain is the supremum of these finite values. No numerical gain or optimal policy is evaluated.

Only a final explicitly CONDITIONAL strict-risk comparison consumes the WHOLE named v21 theorem. The core new universal necessity, descriptor equivalence and matrix completeness are independently proved below from ordinary facts. This closes a different edge from v23/v24's fixed-law characterization; it does NOT substitute the uncontrolled calibration or a surrogate norm/controller class for the original arbitrary-data synthesis task.

## 1. Actual prospective authority, source reads, original boundary

ACTUAL v129-B299LF RETURN preceded NEW whole post-return checkpoint53, SHA `41b2f6bc79b70997d19aa05765ee7364d245897d67aaad28de87cb781dbc2a22`, written after09:47:38 and SENT after09:49:24. Main ACTUALLY completely read that ACK and the review and then explicitly authorized FUTURE-ONLY ORIGINAL primary continuation in `RUN/Tuscan-intake-pause-privacy-cadence-and-prospective-directions-v60.json`, SHA `176b3cbbb8f31a0246a418199be52762cb7dc74aa51372a15537594003aabb85`. Its ENTIRE body was actually read BEFORE any new primary source/proof. No redundant ACK loop/self-resumption was used. Complete parentv59, SHA `d62146da6751cbfb742125d4954aa4399dca9662d95cb944737e946467dc763f`, was also actually read; reading an old reference is NOT permission for a new viability replay.

The new universal stochastic-dual derivation was saved in checkpoint54, actual10:02:28, SHA `6756aec3037521e37ff2d628612b928cc0fbcc97fca1c08cf9c4847a2b7b83d6`. That checkpoint labels the then-unpacketized scalar completeness step as pending. The complete matrix proof below is a subsequent ALL-variable proof covering that scalar class, not a retroactive assertion that its manuscript existed at54.

Actual current reads: COMPLETE17LF `RUN/preview-v3-model-source-boundary-v1.md`, SHA `c66113762df23694d3446fa48d716da9bc0c6a5e953d115cd706694017fef78a`; ENTIRE222LF v17 raw1–130/131–222; ENTIRE276LF v23 raw1–140/141–276; ENTIRE219LF v24 raw1–110/111–219; ENTIRE284LF v21 raw1–145/146–284. Existing immutable pins are retained. No fresh book-pixel/publication/PDF/linked-library reading is inferred from these text reads or hashes. V16's three scoped adoptions do NOT accept v17–v25. No inaccessible1990-paper proof or new source-theorem authentication is claimed.

The original printed boundary remains: expectation is OUTSIDE time-L2; the actual plant and current-state/current-window formula are retained; h is nonnegative. The displayed book feedback omits an explicit t argument. Permitting deterministic F_t on finite horizons and interpreting strict UNIFORM induced gain are declared research conventions, NOT invented printed wording. The present lower theorem works for stationary printed laws and the larger causally consistent progressive class; it does not declare a larger class to be the original synthesis target.

Ordinary foundations: finite-dimensional linear algebra; Brownian Itô/product/localization and linear-SDE moment/flow identities; ordinary conditional expectation on the progressive sigma-field, Tonelli/dominated convergence; scalar RN/Hahn–Banach/separable-Hilbert Bochner duality as proved below; finite-dimensional Gaussian convolution/heat semigroup and continuity of Brownian paths. Every special unknown-controller/mixed-norm/descriptor/bounded-cylinder/application step is supplied. These are standard duality/semigroup methods with PRIOR ancestry, not a novelty or formal-foundations claim.

## 2. Original plant, legal inputs and literal norms

Use the ACTUAL arbitrary-rank constant-data plant driven by ONE Brownian motion:

```text
dX=(A X+B u+C w(t-h))dt+(A0 X+B0 u)dW,
z=D0 X+D1 u.                                             (P)
```

State/control/disturbance/output dimensions are n,m,q,p. Gain state and negative input history are0. Unknown original controllers may be nonlinear. Their responses are strongly well posed/nonexplosive and progressive, with local PATHWISE time-L2 control, using only original information; no finite expected control energy, full-state first moment or diffusion H1 is added. Internal zero-input EMS remains a separate requirement for actual synthesis; the necessary theorem does not pretend to prove it from a gain bound.

For finite T>h set L=T-h, H_in=L2(0,L;R^q), H_out=L2(0,T;R^p). Inputs are ALL original progressive expected-L2 inputs on[0,L], extended by0 outside that interval. Output is counted on[0,T]. This counted zero extension is the explicit convention used in the prior finite-horizon work, not a license for uncounted future window data. On infinity count both full norms.

Write E1(H) for the progressive subspace of L1(Omega;H), with norm `N1(v)=E||v||_H`, and E2(H) for its progressive L2 subspace. The original allowed input class is E2, not arbitrary anticipative signals. Gains may be extended nonnegative reals:

```text
G1(T,h;F)=sup_(0!=w in original E2) N1(z_F(w))/N1(w).
```

The output map need not be linear. The theorem below only uses its actual response, never an assumed mean-state realization or an RMS replacement.

Let Pi_in,Pi_out be the L2(dt dP) orthogonal projections onto progressive processes. Equivalently these are conditional expectations on the completed progressive sigma-field of the finite product measure. This definition supplies a joint measurable version without requiring unrelated pointwise conditional versions at every time. In the usual Brownian filtration it agrees dt dP-a.e. with the familiar conditional expectation at time t.

## 3. Two exact duality facts needed BEYOND second-moment output responses

### 3.1 Projection pairing still holds for arbitrary progressive E1 output

Take ANY raw output dual `phi∈Linf(Omega;H_out)`, possibly anticipative as a PROOF variable, and put f=Pi_out phi. No physical controller/input sees phi's future information. If z is progressive with N1(z)<infinity, then BOTH products below are absolutely integrable and

```text
E integral f^T z = E integral phi^T z,
E integral |f| |z| <= E integral |phi| |z|
                    <= ||phi||_Linf(Hout)*N1(z).          (PROJ-E1)
```

Indeed `|f|<=E[|phi| | progressive-sigma-field]` by conditional Jensen. Multiply by the nonnegative progressive |z|; first truncate it, use the defining conditional-expectation identity, then increase the truncation by Tonelli. The last inequality is pathwise time-Cauchy followed by the essential path-norm cap. Componentwise truncation gives the signed pairing identity. Thus no state/control E2 assumption, and no claimed Linf(Omega;time-Hilbert) contraction of Pi_out, is hidden here. The required fact is exactly its conditional-expectation property on dt dP.

### 3.2 Adapted quotient norm, with full proof at the original input class

For progressive r∈E2(H_in), define

```text
nu(r)=inf {||g||_Linf(Omega;Hin):
           g∈Linf(Omega;Hin), Pi_in g=r},                (QUOT)
```

with infinity for an empty set. g is a DUAL functional extension, NOT an anticipative disturbance. Then

```text
nu(r)=sup_(0!=w∈original E2)
                 |E<r,w>|/N1(w).                       (DUAL-NORM)
```

Here is the needed foundation proof, not an adoption of the full fixed-law v23 theorem. E1 is closed in full Bochner L1: L1(Omega;H) convergence implies L1(dt dP) convergence on the finite interval, and an a.e.-convergent subsequence has a progressive version. E2 is dense in E1 by stopping any w when its OWN accumulated path energy reaches an arbitrary R and capping at L; the stopped path energy is at most R, and the L1(H) error tends to0 by dominated convergence. No anticipative global-energy cutoff is used.

A bounded functional ell on full L1(Omega;H), H separable Hilbert, of norm C has an H-valued Linf representative: for an orthonormal basis e_j, scalar RN of `E↦ell(1_E e_j)` gives coordinate densities g_j. Bounds for EVERY finite rational coefficient vector a imply `|sum a_j g_j|<=C||a||` a.s. on ONE countable intersection. Continuity in finite coefficients gives `sum g_j^2<=C^2`; their Hilbert series is strongly measurable and bounded by C. Density of simple finite-coordinate functions proves `ell(v)=E<g,v>`. Cauchy gives one norm inequality, and testing its near-maximal-norm sets/directions gives equality.

Any g in QUOT bounds the adapted E2 functional by its Linf(H) norm. Conversely, a finite E2 functional bound extends by density to E1, then by Hahn–Banach to full L1 with the SAME norm. The proved coordinate representation supplies g of that norm. Equality against every progressive E2 input means exactly Pi_in g=r. This proves DUAL-NORM, including the unbounded case and attainment of the infimum whenever finite. It does NOT assert `nu(r)=esssup||r||_Hin`; Pi_in was never shown contractive in that mixed norm. No sup/inf exchange is used.

## 4. Entire stochastic output-priced adjoint family, independent of the controller

A finite-T test consists of raw phi with `||phi||_Linf(Hout)<=1`, f=Pi_out phi, a continuous adapted state covector p_t with bounded path supremum and terminal p_T=0, a bounded progressive/predictable output-price k_t∈R^p, and q_t∈R^n satisfying dt dP-a.e.

```text
dp=(-A^T p-A0^T q+D0^T f)dt+q dW,   p_T=0,             (SADJ)
B^T p+B0^T q=D1^T f,                                  (CONTROL)
A0^T p+q=D0^T k,     B0^T p=D1^T k.                   (NOISE-PRICE)
```

All are universally quantified DUAL processes for the given plant, NOT selected physical controls, new plant/state instances or a law-specific numerical scout. Bounds may depend on the particular test; there is no claimed common derivative bound over the whole dual ball. NO solution for every phi is presumed at arbitrary actuated data. The zero test is always allowed.

NOISE-PRICE automatically gives bounded q from bounded p,k and constant coefficients. Thus q is square-integrable on the finite horizon, and SADJ is a legitimate continuous semimartingale equation with f∈L2. No diffusion moment of an unknown controller is being inferred. The B0^Tq term in CONTROL and q^TX in the product's stochastic integrand are both ESSENTIAL.

For0<=s<=L define

```text
r=Pi_in [ C^T p(s+h) ].                               (INPUT)
```

The raw shifted covector is bounded on dt dP, hence in L2. Conditional expectation preserves that pointwise product-space bound, so r is bounded on dt dP and nu(r)<infinity (a finite deterministic time-length bound suffices). This is a PRODUCT-SPACE Linf fact, not the false Linf(Omega;time-Hilbert) contraction used in some tempting shortcuts. No future p(s+h) is declared an admissible physical input.

### 4.1 Scalar-H1 fact used, with the needed proof

A scalar continuous local martingale M starting at0 with `E sqrt([M]_T)<infinity` is true/UI on[0,T], with E M_T=0. One elementary nonsharp proof is the good-lambda argument. Localize first. Stop on first |M|=r and then stop its increment after added bracket delta^2*r^2. Conditional Itô isometry/weak L2 maximal inequality give

`P(M*>2r)<=P(sqrt([M]_T)>delta*r)+delta^2 P(M*>r)`.

Tail integration gives `(1/2-delta^2) E M*<=E sqrt([M]_T)/delta`. The source-fixed proof constant delta=1/2 yields `E M*<=8E sqrt([M]_T)`. Remove the localizations by Fatou; the integrable supremum dominates stopped values, so conditional martingale identities pass in L1. This proves UI/zero mean. The constant8 is ONLY an integrability device and does not multiply any attenuation level.

### 4.2 Grouped product identity for EVERY actual unknown response

For any original response with N1(z)<infinity, apply Itô to p^TX. All terms are locally defined by continuous nonexplosive state paths, local pathwise control-L2 and the test's bounded coefficients. The drift, grouped BEFORE expectation, is

```text
(-A^Tp-A0^Tq+D0^Tf)^T X+p^T(AX+Bu+Cwlag)
                                      +q^T(A0X+B0u)
 = f^T D0X+(B^Tp+B0^Tq)^T u+p^TCwlag
 = f^T z+p^TCwlag.                                    (DRIFT)
```

The scalar stochastic integrand is

```text
q^TX+p^T(A0X+B0u)
 =(A0^Tp+q)^T X+(B0^Tp)^T u
 = k^T(D0X+D1u)=k^Tz.                                 (DIFFUSION)
```

Thus the ACTUAL product satisfies

```text
d(p^TX)=[f^Tz+p^TCw(t-h)]dt+k^Tz dW.                  (GROUP)
```

For its SINGLE scalar martingale M, `E sqrt([M]_T)<=||k||_infty*N1(z)<infinity`; the proved H1 fact gives E M_T=0. PROJ-E1 proves integrability of f^Tz without assuming z∈E2. Bounded p and original N1(w)<infinity prove integrability of the delayed input drift. The endpoint products are identically0 from X_0=0 and p_T=0. No integrability of intermediate p^TX, E X or E u is taken for granted.

Integrating GROUP and taking expectation, with the actual delay and zero history, gives

```text
E<phi,z>=E<f,z>
 =-E integral_0^L (C^Tp(s+h))^T w(s)ds
 =-E<r,w>.                                            (ALL-LAW-ID)
```

The final projection identity is legitimate against original E2 input. The output identity remains valid for nonlinear controllers; it singles out a linear dual functional of their possibly nonlinear response, not an assumed linear response map.

## 5. Entire necessary bound, null cases and exact descriptor equivalence

From the unit raw-output-dual cap and ALL-LAW-ID,

`|E<r,w>|<=N1(z)` for EVERY original E2 input.

DUAL-NORM therefore proves, for EVERY original admissible controller F,

```text
G1(T,h;F)>=nu(r)  for EVERY test in §4,
G1(T,h;F)>=kappa_st(T,h):=sup_(all §4 tests) nu(r).     (NEC)
```

If an actual output has infinite N1, the gain bound is already trivial. No controller expected energy is required in the finite-gain branch. If phi=0, f=0 and the bounded p/q solution of the homogeneous terminal linear BSDE is0: Itô on |p|^2, Young and backward Gronwall give `E|p_t|^2+(1/2)Eint_t^T|q|^2<=Cint_t^TE|p|^2`, hence p=q=0. Thus r=0; no positive obstruction is hidden behind a zero dual norm.

On infinity, zero-extend each finite counted input after L. Its original global output norm is at least its[0,T] prefix. Thus every global original law obeys

```text
G1,infinity(F)>=sup_(T>h) kappa_st(T,h).                (INF-NEC)
```

No stochastic restart, STATE-LOC, terminal mean, stationary-law replacement, horizon/regularization exchange or RMS-to-literal equality enters. Under the declared strict UNIFORM induced-gain convention, existence of F with G1<gamma requires the right side strictly below gamma. This is NOT a new assertion about a merely pointwise printed ratio at an endpoint.

### 5.1 Exact finite-matrix stochastic descriptor — no inverse of R

Eliminate q using the FIRST NOISE-PRICE block. The WHOLE §4 family is equivalently described by bounded continuous adapted p, bounded k, unit raw phi, f=Pi_outphi, terminal p_T=0 and

```text
dp=[(-A^T+A0^T A0^T)p-A0^T D0^T k+D0^T f]dt
                         +[D0^T k-A0^T p]dW,
B0^T p=D1^T k,
(B^T-B0^T A0^T)p+B0^T D0^T k=D1^T f.                 (SDESC)
```

From SDESC set `q=D0^Tk-A0^Tp` and recover SADJ/CONTROL/NOISE-PRICE term by term. Conversely those original equations immediately give SDESC. In particular the square is the ORDERED product `A0^T A0^T`, not A0^TA0. All matrices retain their actual dimensions, including singular/zero D1 price. This is a stochastic descriptor/test representation, NOT a claim that solving it is a finite-dimensional feasibility algorithm or a causal synthesis certificate.

For deterministic lambda,g satisfying `lambda_dot+A^Tlambda=D0^Tg`, `B^Tlambda=D1^Tg`, terminal lambda_T=0 and `[A0^Tlambda;B0^Tlambda]=[D0^T;D1^T]k`, put p=lambda/||g||, q=0, phi=g/||g||. Bounded lambda,k give a §4 test. Its r is deterministic and `nu(r)=||C^Tlambda(.+h)||/||g||`, by time-Cauchy and the legal deterministic aligning input. Thus the old deterministic output-priced family, and its exact-noise-annihilating subfamily, are INCLUDED at the SAME attenuation level. Lambda_0=0 may be retained for that predecessor comparison, but is not needed in the new gain-zero-state proof. No unreviewed predecessor headline is used to supply this inclusion.

The original full current-state/current-window information was not discarded. CONTROL cancels the coefficient of the ACTUAL u for ANY such law; it does not remove the physical actuator or assume a specific window kernel. That is why there are no missing law-specific future-window feed terms in ALL-LAW-ID, unlike the fixed-controller adjoint of v23.

## 6. A COMPLETE all-variable matrix calibration — bounded-cylinder tests suffice

This section proves equality, not just a plausible restriction, on the ENTIRE class

```text
dX=(A X+Cw(t-h))dt+A0X dW,    z=D0X,
D0 has FULL COLUMN RANK.                              (UC)
```

A,A0,C are arbitrary real constant matrices, h>=0 is arbitrary finite, and dimensions are arbitrary finite. Equivalently retain original control coordinates with B=B0=D1=0; no chosen control affects the state/output. D0 need not be square. No commutation/diagonalization of A,A0, stability, scalar parameter choice or special noise value is assumed. This is a calibration theorem INSIDE the original arbitrary-data domain, not a substitute target or a conclusion for all actuated data.

On every finite horizon, linear-SDE localization/Itô/Doob/Gronwall gives a strong response and finite-prefix state/output second moments for every original expected-L2 input. That legitimate E2 fact is used ONLY in this uncontrolled linear calibration, not imposed on arbitrary competitors in §§4–5.

### 6.1 Unit smooth finite-Brownian-cylinder/time-step duals are norming

On the canonical usual augmented Brownian filtration, restrict raw output duals to

```text
phi(t)=sum_(j=1..N) b_j(t) Phi_j(W_t1,...,W_tm),         (CYL)
```

where b_j are a finite orthonormal set of deterministic vector-valued TIME-STEP functions in H_out, `0<t1<...<tm<=T` are arbitrary distinct finite observation times, and Phi=(Phi_1,...,Phi_N) is globally C_b^infinity with `||Phi(x)||_2<=1` for EVERY x. Thus `||phi(omega)||_Hout<=1` on every path. No numeric observation time or physical input/state/control instance is selected; the entire all-variable family is quantified.

These tests are L2(Omega;H_out)-dense in the full unit path-norm dual ball. First orthogonally project any unit raw phi onto finite step-function time spaces; each projection is a pointwise Hilbert contraction and converges in L2. Its coefficient vector remains in the unit Euclidean ball. Then condition that vector on increasing finite Brownian observation sigma-fields. Conditional Jensen preserves the ball; Brownian continuity and conditional L2 convergence give density in F_T. A measurable unit-ball-valued coefficient function on R^m can finally be convolved with a nonnegative smooth compactly supported unit-mass mollifier. Convexity preserves the unit ball at EVERY x; all derivatives of the convolution are bounded. Approximate-identity convergence gives L2 convergence under the nondegenerate finite Brownian Gaussian law. Distinct positive observation times ensure that law has a density; repeated/zero coordinates can simply be omitted. A diagonal approximation proves the claim.

For ANY progressive E1 output z, not just E2, unit-cap L2 convergence of phi_i to phi also preserves its pairing: truncate the path norm ||z|| at an arbitrary R, use Cauchy/L2 convergence on the bounded piece, and bound the remainder by `2E[||z||1_(||z||>R)]`. Hence CYL is NORMING for E1 output. In particular it recovers the full Bochner dual norm `N1(z)=sup_CYL E<phi,z>`. Anticipation is solely in these proof tests; no future Brownian information is supplied to the plant/input/controller.

### 6.2 Complete bounded-adjoint construction, including bounded q

Fix ANY CYL test, put f=Pi_outphi. Conditional Gaussian increments show that, between its finitely many observation times and the finitely many time-step boundaries, f_t is a smooth bounded function of the already observed W_ti and CURRENT W_t. All derivatives in these finite coordinates are bounded: conditioning is Gaussian convolution of the bounded derivatives of Phi. A common translation of all not-yet-frozen Brownian coordinates has a finite uniform derivative bound D_phi. There is also a finite pointwise bound F_phi for f. These constants may depend on the test; no common bound over all CYL is claimed.

Let the forward matrix flow be

```text
dGamma_(t,s)=A Gamma_(t,s)ds+A0 Gamma_(t,s)dW_s,
Gamma_(t,t)=I.
```

It depends only on future increments after t, not the current absolute Brownian value or earlier observed coordinates. Itô on its Frobenius norm and localization/Gronwall give

```text
E||Gamma_(t,s)||_F^2
 <=n exp[(2||A||+||A0||^2)(s-t)].                       (FLOW)
```

No inverse stochastic flow or commutation is needed. In particular `E||Gamma_(t,s)||` is bounded by a finite deterministic C_T uniformly in t<=s<=T.

Define the adapted covector

```text
p_t=-E[ integral_t^T Gamma_(t,s)^T D0^T f_s ds | F_t ]. (REP)
```

The bound on f and FLOW imply `sup|p|<=T C_T ||D0|| F_phi` a.s. More importantly, p is a smooth function V(t;past-observations,W_t) on each finite open time piece. Differentiate its conditional Gaussian representation with respect to the CURRENT Brownian coordinate while holding already observed coordinates fixed. Gamma depends only on increments, so this derivative acts ONLY on the future f_s. All not-yet-observed Brownian coordinates translate together. Dominated differentiation and the bound D_phi give

```text
sup |partial_x V| <= T C_T ||D0|| D_phi <infinity.      (DQ)
```

Thus bounded q is actually proved, not inferred from a generic L2 BSDE or a BMO statement.

For completeness, the representation really solves the required BSDE. Between observation/step times define the matrix-Gaussian semigroup

`(H_tau v)(x)=E[Gamma_(0,tau)^T v(x+W_tau)]`.

Flow composition and independent increments give its semigroup law even for NONCOMMUTING A,A0. Itô on `Gamma^T v(x+W)` gives generator

`L v=(1/2)v_xx+A^T v+A0^T v_x`.

This also directly gives `H_tau v-v=int_0^tau H_s L v ds` for smooth bounded derivatives, using FLOW to justify expectations. REP's conditional dynamic decomposition across the next time boundary is the ordinary Duhamel formula for this semigroup, with source D0^Tf and terminal0. Differentiation yields on each piece

`V_t+(1/2)V_xx+A^T V+A0^T V_x=D0^T f`.

At an observation time its newly frozen coordinate is the actual continuous Brownian value; the left/right conditional Gaussian limits agree. Step changes in f cause no jump in its time integral. Therefore p is continuous across ALL finitely many boundaries. Piecewise Itô, with `q=V_x`, glues to

```text
dp=(-A^Tp-A0^Tq+D0^Tf)dt+q dW,   p_T=0.               (UC-BSDE)
```

The bounds REP/DQ hold globally across those finitely many pieces (values at deterministic boundary times are dt-null and can be predictably chosen). Higher finite-coordinate derivatives are likewise bounded by the bounded Phi derivatives and FLOW, which justifies the displayed classical generator/Duhamel differentiations. This construction is an actual written bounded solution proof, not a numerical Gaussian computation, scientific interpreter or an appeal to an unavailable source theorem.

Since D0 has full column rank, D0^T is surjective. Choose ANY fixed finite linear right inverse J of D0^T, and put

```text
k=J(A0^Tp+q).
```

Then k is bounded by REP/DQ and `D0^Tk=A0^Tp+q`. With B=B0=D1=0, the remaining price/control constraints are identities. Thus EVERY CYL output dual is accompanied by an ACTUAL §4 bounded test for UC. No physical control was constructed or substituted; this is a dual-variable existence proof.

### 6.3 Exact finite gain — two independent suprema, no minimax shortcut

For UC let T_UC map original E2 input to its actual output. Each CYL test has the preceding feasible p,q,k, so ALL-LAW-ID gives

`E<phi,T_UC w>=-E<r_phi,w>`.

For EVERY original w, CYL is norming by6.1. The CYL ball is symmetric, so signs/absolute values cause no change. Taking the two independent SUPREMA over CYL and original input E2 commutes and DUAL-NORM gives

```text
G1(T,h;UC)=sup_(CYL phi) nu(r_phi)
          =kappa_st(T,h).                             (COMPLETE)
```

The first equality uses the SAME actual output/input class and norm. For the second, CYL-feasible tests are a subset of all §4 tests, giving one inequality; the universal NEC gives the opposite inequality. There is NO inf/sup swap, presumed simultaneous lifting, essential path supremum of r, or replacement by an RMS/deterministic gain. The assertion is valid in extended reals; no numerical value or attaining physical input is asserted.

This is the ENTIRE constant-matrix/full-column-D0 uncontrolled class, not just scalar noise, commuting matrices or a chosen example. It is a completeness calibration of the plant-only necessary family. It does not prove the family complete for genuinely actuated unknown nonlinear controllers or select a controller.

### 6.4 Exact infinite calibration and the actual delay count

For the SAME UC data and h, with original global expected-L2 inputs,

```text
G1,infinity(UC)=sup_(T>h) G1(T,h;UC)
              =sup_(T>h) kappa_st(T,h).                (UC-INF)
```

A finite counted input extended by0 gives the lower direction by prefix comparison. Conversely, UC's output through T depends only on input through T-h: its ONLY input appearance is the physical delayed forcing, and strong uniqueness preserves the response under truncation after T-h. This particular statement is legitimate for UC, not for a general printed controller with direct current-window feed. Therefore each actual prefix is bounded by the finite counted gain times N1(input_0..T-h), then by the supremum times full N1(input). Increase T and use monotone convergence of path norms/expectations. Infinite values are covered as well. No infinite-terminal BSDE, EMS inference or horizon/regularization limit exchange is needed.

## 7. Explicitly CONDITIONAL strict stochastic-risk comparison — no reference replay

This section ONLY consumes the WHOLE284LF `literal-preview-synthesis-consolidated-v21-strict-stochastic-risk-gap.md`, SHA `918e883ec3e68fd7876c2cb198a4d177b581675eeb05308dc7158f459c5a615e`, actually freshly read in its entirety. V21 is still an UNREVIEWED owner candidate; neither v16 adoption nor the present paper automatically accepts it. A complete joint review must include ALL its storage/input-domain/legal-probe/common-buffer/literal/mean-relaxation proof, not just its value headline.

Its ALL-positive-symbolic family at h=0 has `q0=2a-sigma^2>0`, `dX=(-aX+cw)dt+sigmaX dW`, z=dX. Its independently supplied whole theorem states

`G1>=gamma_star=2cd/q0>dc/a=kappa_mean`,

where kappa_mean is the COMPLETE deterministic output-adjoint/mean-output relaxation, already closed and causal. UC includes this ENTIRE symbolic family. Therefore, CONDITIONAL on that WHOLE named v21 theorem, UC-INF yields

```text
sup_T kappa_st(T,0)=G1,infinity
                  >=gamma_star>kappa_mean.             (STRICT-RISK)
```

This is a logical ALL-variable theorem composition, NOT re-evaluation of an old fixed control/state/reference as a viability check of a new bound. No v21 probe is run/recomputed, no selected parameter tuple is compared and no numerical value or new RMS/literal exact value is claimed. The new theorem supplies completeness of the STOCHASTIC dual family, not a repaired deterministic mean equation. The strict comparison has an explicit extra named284LF import and must not be merged with the core proof's ordinary-facts-only cut.

## 8. Exact acceptance scopes, residual and permanent history

Delivered complete mathematical claims, each still WRITTEN/UNGATED:

1. **Universal original-controller necessity:** PROJ-E1, correct quotient dual, full stochastic output-priced product/control-NOISE identity and finite/infinite kappa_st lower bounds for EVERY actual original admissible nonlinear law, all matrix ranks/h. No unknown state/control mean is used.
2. **Whole descriptor equivalence/inclusion:** SDESC is exactly the entire bounded test family; deterministic output-priced and noise-annihilating tests embed at the SAME literal attenuation level. No control-price inverse or finite algorithm is assumed.
3. **Complete matrix calibration:** ENTIRE UC full-column-D0 class, canonical Brownian filtration, ANY constant A,A0,C/finite h; norming unit CYL ball, actual bounded p AND q construction for NONCOMMUTING matrices, and exact finite/infinite literal kappa_st equality. No gain value/controller is evaluated.
4. **Separate conditional strict-risk composition:** only at WHOLE named v21, the stochastic family is strictly stronger than the COMPLETE deterministic mean-output relaxation on its entire symbolic family. That extra import is NOT silently adopted with1–3.

The first original general gap remains completeness/usable evaluation of the stochastic descriptor for ACTUATED plants and realization by a causal, actual printed stationary controller with full internal stability. A plant-only annihilator lower bound is not general N&S; its witnesses are proof processes, never controller memory/noise. Even in UC, exact representation does not compute the scalar literal value. No linear-policy WLOG, expected-control-strengthening replacement, same-gamma RMS equivalence, pointwise strict endpoint or arbitrary-data prescribed-gamma synthesis certificate is claimed. The original unrestricted task remains OPEN.

All predecessor sources/reviews/ACKs/checkpoints/park-v2/addenda remain immutable. ENTIREv1-v24/all held failed withdrawn leads are preserved by whole53/54. V16 ONLY retains its three adopted full scopes; v17–v24 remain candidates and this v25 needs fresh ENTIRE mathematics AND dependency/application review. It is not part of any older frozen packet by ancestry. The complete v23/v24 fixed-law theorem is not needed as a hidden premise for1–3: its quotient notation is reused, and the necessary dual proof is independently supplied in3.2. No future-field optimization is smuggled in as a physical input.

All FIVE own findings remain distinct/permanent: private written-exactness; post-v100 ACTUALRETURN/pre-primaryACK order; actual v107 post-body/pre-RETURN LIVE primary interleaving with old blanket pause assurance withdrawn; false historical receipt counts/nonexistent coverage withdrawn; and v120 material SPECIFIC prior RQLSv7/v10 inventory omission adoptedv48. The fifth is narrower than denial/blindness/pre-ACK-body/interleaving/execution/falsity; historical definition contact is not denied by old fresh-source NR. Explicit old RQLS/Sun/other serial exposures and v129 review remain preserved, not false blind/clean thought evidence.

Four old unadmitted Eval records, every withdrawn annotation/probe and ALL consuming guidance receive ZERO credit; none is rerun/replayed/back-converted or used to choose a new instance. All parent/source-author-reviewer v9–v60/parent091/other root/freeze/coverage/clock/cadence/format/intake/admission/mathematical-withdrawal/quarantine findings stay at their exact scopes. N4 remains UNKNOWN/incomplete/historical exit unestablished, auxiliary214 UNADMITTED/STOP, and scientific HOLD binding. No process finding is cured by exact mathematics or inferred to make an author theorem false. Conventional proofs/observable source chronology are not an exhaustive hidden-model-reasoning/cognition/runtime/continuous18-way/provenance-unaffected census.

No pinned/source/shared/parent file was edited; no Git/deletion/config/publication/paid-model/scientific launch occurred. No formal/Lean/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty/SOTA/priority/public-refutation acceptance is conferred. Same ORIGINAL eighteen owners/target, science cutoff2026-10-27T11:05:38-07:00 and delivery12:35:38; substantive actual-clock checkpoints remain at most30minutes. This complete increment is NOT an early final park or96-hour closeout. If any future scope/provenance failure is recognized, STOP/report/WAIT explicit direction rather than laundering a chosen probe.

**END OF COMPLETE v25.**
