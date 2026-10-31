# Literal stochastic preview — exact OUTPUT-closure relaxation, full terminal adjoints and a realization-gap control

Owner **InfoHinfPreview-2 / info-3**. Actual immediately preceding `/bin/date` BEFORE this write: **Mon Oct 26 06:56:00 PDT 2026**. **NEW COMPLETE WRITTEN OWNER-CANDIDATE**, requiring a fresh full mathematics/dependency/application gate. Conventional SOURCE-SYMBOLIC proofs only; no numerical/rational parameter instance, finite-word trial, decimal/magnitude scout, scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay/simulation/build/test/CLI/nestedagent/newGO. No mathematical identity is machine checked.

## 0. New exact representation, not a claimed original realization

V16/v17 supplied necessary adjoint tests that do not assume an unjustified full-state mean at singular control price. This successor answers a DIFFERENT, exact question: **what deterministic relaxation is characterized by the ENTIRE output-priced adjoint family?**

For each finite horizon, the Bochner mean of the ACTUAL output belongs to an explicitly defined CLOSED deterministic output relation. The minimum-norm element of that relation is an orthogonal projection of the deterministic forced output. Its operator norm is EXACTLY the full terminal-adjoint lower bound. The relaxation introduces free drift directions equal to the image of the unpriced instantaneous noise directions; it is an OUTPUT relation, not an assertion that an actual full-state mean solves a drift-only SDE.

This also removes an unnecessary test restriction: the gain initial state is0, so lambda(0) need NOT vanish. Only lambda(T)=0 is needed. The old both-zero tests remain valid but are not declared exhaustive.

Neither the orthogonal projection nor the free drift input is a printed controller. Closure and causality are genuine boundaries. An entire SYMBOLIC two-integrator family below has relaxed minimum output0 for every input, while no original locally pathwise-L2 controller can attain zero output even for one legal discontinuous pulse. Thus the relaxation cannot silently be promoted into an exact original realization theorem.

General prescribed-gamma literal synthesis/printed-current-window realization remains OPEN. This is a new exact characterization of a necessary relaxation, not an arbitrary-plant N&S, a new optimum for all data, a norm-equivalence theorem or a novelty claim.

## 1. Authority, sources and exact imports

The ENTIRE v120-B review ACTUALLY RETURNED before the NEW whole-primary ACK `primary-resumption-after-v120-ack-v1.json`, SHA256 `00671413a6b56430de28200b355cdfdba71eb22c9e620e8fe4082b603cb2ed28`, written06:44:04 and SENT after06:44:42 BEFORE the current source/reasoning. The complete new output-closure derivation was substantively saved in checkpoint40, actual06:54:00, SHA256 `e9eaf7b86e9ec64a28082f4d5517df5e8507f4be78d7a89125fe625dd183bf27`, before this manuscript. No live review was interleaved with the current development.

The original model/expected-path-norm/current-window/declared-uniform-strictness boundary is COMPLETE17LF `RUN/preview-v3-model-source-boundary-v1.md`, SHA256 `c66113762df23694d3446fa48d716da9bc0c6a5e953d115cd706694017fef78a`, actually read in the earlier current primary interval. No new book-pixel read is inferred from its image hashes. RUN means `institute/runs/three-area-2026-10-23-96h/`.

Comparison predecessors remain immutable: own v16 SHA256 `3f8632430eb33b699ba03c1585d8f06b55ef865756c0d3c8cf825cd47873440d` and v17 SHA256 `6092eff31f60daf42be3e3b7ceb49dde823296e37bce13dbaa58f7501c4c15c0`. They are UNGATED owner candidates, not accepted premises. The needed price-space/scalar-H1/grouped-identity arguments are reproduced at their operative scope below; no v16 exact-family or v17 verdict is imported. Earlier Riccati/mean/quotient/norm/synthesis packets are context, not correctness premises.

Named ordinary imports: finite-dimensional kernel/row-space duality, finite-interval Volterra/Fubini estimates, semimartingale integration by parts and stopped Itô isometry/weak-L2 localization, separable-Hilbert Bochner expectation/Jensen, elementary Hilbert orthogonal projection and `(ker S*)^perp=closure(range S)`, adjoint operator-norm equality, density of smooth compactly supported functions in time-L2, elementary AC/Sobolev facts and Cauchy/Gronwall. Every model-specific operator, adjoint sign, delay/counting, moment/integrability and closure/realization step is proved below. No stochastic or deterministic Riccati synthesis theorem, opaque model-specific range theorem, numerical assay or external sharp probability result is used.

## 2. The ACTUAL arbitrary-rank stochastic model and gain class

Let real constant matrices of arbitrary ranks define

```text
dX=(A X+B u+C w(t-h))dt+(A0 X+B0 u)dW,
z=D0 X+D1 u,                                           (P)
```

with n states, m controls, q disturbances, p outputs and ONE scalar Brownian motion. Gain state X(0)=0 and negative input history are0. Finite output is[0,T], finite counted input is[0,L0], L0=T-h>0. Allowed disturbances are ALL canonical progressive inputs with finite expected squared energy. Unknown controls are progressive, strongly well posed/nonexplosive, consistent nonanticipative/event-local and locally PATHWISE time-L2. No expected control energy, full-state mean, full-state H1 or output coercivity is assumed. The necessary statements allow the larger causal-history class, so apply to the printed current-state/current-window laws.

Write `N1(f)=E||f||_time-L2`; gain is the supremum of output/input N1 ratios, in extended nonnegative reals. The expectation is OUTSIDE the path norm. A strict UNIFORM level G1<gamma remains the declared research convention, not a newly printed book supremum.

Set

```text
H=[D0 D1],   N=[A0 B0],
U=N(ker H) subset R^n.
```

Choose an orthonormal basis matrix E_U for U, allowing zero columns when U={0}. A covector lambda satisfies `E_U^Tlambda=0` IFF there exists k with `H^Tk=N^Tlambda`: the row lambda^TN vanishes on ker H exactly when it factors through H. Choosing such a factor on a basis of U-perp gives a FIXED linear map lambda↦k. Thus a deterministic finite-interval H1 lambda in U-perp gives bounded deterministic k(t). No full NEO factorization or matrix inverse is required.

## 3. Terminal-only scalar-adjoint identity without E X or E u

For deterministic g∈L2(0,T;R^p), let lambda be the UNIQUE H1 solution

```text
lambda_dot+A^Tlambda=D0^Tg,
lambda(T)=0.                                           (A)
```

There is NO condition lambda(0)=0. Define

```text
q_lambda(s)=C^Tlambda(s+h),   0<=s<=L0.
```

Suppose additionally

```text
B^Tlambda=D1^Tg,
E_U^Tlambda=0.                                         (B)
```

For any deterministic allowed input w whose actual output has finite N1, semimartingale product rule groups the ACTUAL terms as

```text
d(lambda^TX)
 =[g^Tz+lambda^TCw(t-h)]dt+k(t)^Tz(t)dW.                 (GROUP)
```

Both endpoint products vanish: terminal lambda(T)=0 and initial X(0)=0. The latter is why lambda(0) may be arbitrary. Finite nonexplosive state paths and local pathwise-L2 controls justify the pathwise product/integrals; no state/control expectation is used to derive GROUP.

The scalar martingale M=integral k^Tz dW has

```text
E sqrt([M]_T)<=||k||_infinity*N1(z)<infinity.
```

For completeness, the ordinary H1 implication follows by stopping a continuous local martingale at its first norm crossing r and its added bracket delta²r². Conditional Itô isometry/weak-L2 maximality give `P(M*>2r,S<=delta*r)<=delta²P(M*>r)`, S=sqrt([M]_T). Tail integration gives `(1/2-delta²)E M*<=E S/delta`; delta=1/2 yields a nonsharp8. Localization/Fatou then give an integrable full maximum, so the stopped conditional-expectation identities pass in L1 and M is true/UI with E M_T=0. The constant is ONLY an integrability tool, not an attenuation loss.

The GROUP drift is absolutely integrable in expectation because `E integral|g^Tz|<=||g||N1(z)`. The input term is deterministic finite by Cauchy. Integrating GROUP, taking expectation and translating the delayed input gives

```text
E integral_0^T g^Tz dt
       =-integral_0^L0 q_lambda(s)^T w(s)ds.             (ID)
```

This uses ONLY the zero endpoint products and the integrable GROUP terms. It never takes separate expectations of A X+B u, of the full original diffusion, or of an unpriced u. If actual N1(z) is infinite, subsequent lower bounds are already trivial. If g=0, terminal ODE uniqueness gives lambda=0, so no undefined positive ratio is concealed.

## 4. An explicit deterministic relaxed OUTPUT relation

For a FIXED deterministic counted w, introduce the PROOF system

```text
x_dot=A x+B v+C w(t-h)+E_U r,
x(0)=0,
y=D0 x+D1 v,                                          (REL)
```

where v∈L2(0,T;R^m) and r∈L2(0,T;R^dimU) are arbitrary deterministic proof controls. They need not be causal functions of w. r is NOT a physical actuator granted to the original controller, and x is NOT asserted equal to E X. REL is a relaxation used to describe output constraints only.

Let the real Hilbert spaces be

```text
W=L2(0,L0;R^q),
Y=L2(0,T;R^p),
V=L2(0,T;R^m) x L2(0,T;R^dimU).
```

Extend w by0 outside its counted interval and before0. Define bounded LINEAR operators

```text
(T_C w)(t)=D0*integral_0^t exp(A(t-s))*C*w(s-h)ds,
(S(v,r))(t)=D1*v(t)
    +D0*integral_0^t exp(A(t-s))*[B*v(s)+E_U*r(s)]ds.     (OPS)
```

On finite T, exp(At) is bounded, and elementary Volterra/Cauchy or Young estimates give finite operator norms, whether or not A is Hurwitz. Direct D1 multiplication is bounded. Hence REL's actual deterministic output set is exactly

```text
B(w)=T_Cw+range(S),
closed B(w)=T_Cw+closure(range S).                      (OUT)
```

The closure is norm closure in OUTPUT time-L2. It is not silently claimed to be actual outputs of finite-energy state/control pairs.

## 5. The ENTIRE adjoint kernel is exactly the price-safe test family

For arbitrary g∈Y solve(A). Explicitly,

```text
lambda(t)=-integral_t^T exp(A^T(s-t))*D0^Tg(s)ds.        (SOL)
```

Its terminal value is0 and its derivative is `D0^Tg-A^Tlambda`; the bounded Volterra operator gives lambda∈H1. Define the positive-sign auxiliary integral I=-lambda. Fubini for bounded finite-time kernels and L2 inputs gives

```text
S* g=(D1^Tg-B^Tlambda, -E_U^Tlambda),
(T_C* g)(s)=-C^Tlambda(s+h),   0<=s<=L0.                (STAR)
```

The signs matter. The usual backwards integral I contributes+B^TI in the control adjoint and+E_U^TI in the nuisance adjoint; since I=-lambda, these are the displayed negative signs. For T_C, the delayed input at s first appears at s+h, giving exactly that shifted terminal integral, with no lost h factor or a shifted output count.

Consequently

```text
K:=ker S*
 = {g: the terminal lambda from(A) satisfies(B)}.       (KER)
```

This is an EXACT characterization, not merely some convenient annihilators. It uses the ENTIRE terminal-only price-safe family. The earlier both-endpoint-zero test space can be a proper smaller subspace and is not substituted for K.

Every solution of(B) has lambda(t)∈U-perp and the bounded factor k from §2, so §3 applies to EVERY g∈K. Conversely every full price-safe terminal adjoint is represented by its g and lies in K by STAR. No generic rank, full output price, covariance assumption or finite-dimensional closure of the time-operator range is used.

## 6. Actual mean OUTPUT belongs to the closed relaxation

**Theorem1 — WRITTEN output compatibility.** For any original controller and any deterministic counted w for which N1(z(w))<infinity, the OUTPUT Bochner mean m(w)=E[z(w)] exists in Y and

```text
m(w) in T_Cw+closure(range S).                         (COMP)
```

No original state/control mean is asserted.

**Proof.** The progressive output is a strongly measurable Y-valued random variable because Y is separable and its finite-prefix paths are time-L2. Finite E||z|| is exactly Bochner integrability; in particular `||m(w)||<=N1(z(w))`.

For EVERY g∈K, the terminal lambda satisfies(B), so ID and STAR give

```text
<g,m(w)>=-<q_lambda,w>
         =<T_C* g,w>=<g,T_Cw>.
```

Thus m(w)-T_Cw is orthogonal to ker S*. The standard Hilbert identity `(ker S*)^perp=closure(range S)` proves COMP. This is a statement about the ACTUAL output mean only, derived from all grouped scalar identities. It neither extracts E X/E u nor supplies an actual r representing a martingale defect in L2. In particular no unclosed-range or causal-policy claim is hidden in the proof.

If a candidate controller has infinite output norm for the chosen deterministic w, the gain lower conclusion is trivial. Otherwise the theorem applies input by input. It does not assume that the unknown map w↦m(w) is linear, printed-realizable or Markovian.

## 7. Exact value of this CLOSED noncausal output relaxation

Let P_K be the orthogonal projection of Y onto the CLOSED subspace K=ker S*. Since closure(range S)=K-perp,

```text
T_Cw+closure(range S)=P_K T_Cw+K-perp.
```

**Theorem2 — WRITTEN exact relaxed value and full dual equality.** The unique minimum-norm element of this closed affine relation is P_K T_Cw, and

```text
min_(y in closed B(w)) ||y||_Y=||P_K T_Cw||_Y.
```

Every original controller therefore obeys the same-level necessary finite-horizon bound

```text
G1,T(F)>=kappa_rel(T,h):=||P_K T_C||_(W->Y).             (REL-LB)
```

Moreover

```text
kappa_rel(T,h)
 =sup_(g in K,g!=0) ||T_C* g||_W/||g||_Y
 =sup_(ALL terminal-only price-safe adjoints,g!=0)
                 ||C^Tlambda(.+h)||_W/||g||_Y.          (DUAL)
```

Use0 for the supremum when K={0}. All these finite-horizon values are finite because T_C is bounded.

**Proof.** Orthogonal decomposition gives `||P_KT_Cw+v||²=||P_KT_Cw||²+||v||²` for v∈K-perp, proving the first claim and uniqueness. COMP then gives

```text
||P_K T_Cw||<=||m(w)||<=N1(z(w)).
```

Take deterministic nonzero w and the operator supremum; its input N1 norm is its deterministic L2 norm, giving REL-LB. If the original gain is infinite it remains true.

Hilbert adjoints give `||P_K T_C||=||T_C* P_K||`. Projection has range K and norm at most1. The supremum of `||T_C*P_Kg||/||g||` equals the supremum over nonzero g∈K: projection supplies one inequality, and restricting to K supplies the other. STAR proves the final identity. Thus the ENTIRE adjoint bound is exactly this CLOSED relaxation value; no assertion of original controller optimality was used to obtain equality.

For an infinite-horizon original controller, each compact deterministic input and finite prefix gives the same inequality, so

```text
G1,infinity(F)>=sup_(T>h) kappa_rel(T,h).
```

No monotonicity, existence of a horizon limit, finite ARE/Riccati characterization or expected terminal-state limit is asserted. Strict-uniform original feasibility at gamma necessarily makes each finite kappa_rel and their supremum strictly below gamma whenever the actual gain g<gamma bounds them. This is necessary only, not a printed realizer.

The linear map P_K T_C is a mathematical minimum-output selector for a closed NONCAUSAL relation. It may use future input beyond the permitted preview window and may not belong to the unclosed output range at all. Its existence is NOT a Markovization/mean-policy realization theorem.

## 8. A SYMBOLIC control against silently dropping closure

Fix ANY positive symbolic a,b,c,d and finite T>h. Consider the ORIGINAL deterministic special family of(P)

```text
dx=(a*y+c*w(t-h))dt,
dy=b*u dt,
z=d*x,
A0=0, B0=0, D1=0.                                     (DBL)
```

The physical Brownian may be present but has zero coefficients. It remains an actual arbitrary-rank member of the original model; R=0. Here U={0}, so no nuisance r is even added.

For zero disturbance, the deterministic control-output map is `z=d*a*b*V2 u`, where V2 is twice Volterra integration with zero x(0),y(0). Its range contains EVERY smooth compactly supported phi on(0,T): choose `u=phi''/(d*a*b)`, then x=phi/d and y=phi'/(d*a), with the required zero initial values. Since those phi are dense in Y=L2(0,T), closure(range S)=Y. Therefore K={0}, P_K=0 and the closed-relaxation minimum is0 for EVERY counted w.

Now choose legal SYMBOLIC times `0<s0<s1<T-h` and amplitude q>0, and the deterministic input `w=q*1_[s0,s1]`. Its delayed forcing has a jump at the interior time h+s0. Suppose an original locally pathwise-L2 controller, even randomized/nonlinear/causal-history, attained N1(z)=0 for this input. Nonnegativity makes the output path-L2 norm0 almost surely. Path continuity gives x identically0 on each such path. The state equation then forces

```text
y(t)=-(c/a)w(t-h)  for a.e.t.
```

But y(t)=b*integral_0^t u(s)ds is absolutely continuous and hence continuous on every finite path. It cannot equal0 a.e. on the open interval immediately before h+s0 and the nonzero constant -cq/a a.e. immediately after it. Continuity extends each a.e. constant to the whole corresponding open interval and gives contradictory one-sided values at the jump. Thus NO original locally admissible controller can attain zero output for that pulse.

This is an ENTIRE symbolic structural family and an exact admissible-input argument, not an invented numerical parameter probe or a simulated control. It demonstrates a REAL distinction between closure(range S) and actual finite-energy output realization, even before stochastic free-noise complications or a causal-selector constraint. It does NOT assert a positive-gamma infeasibility result, evaluate the original induced-gain infimum, classify internal stabilization for DBL, or claim that the closed relaxation is useless as a lower bound.

## 9. Exact interpretation and what is STILL missing

The new output-closure theorem identifies precisely what the full output-priced terminal-adjoint constraints imply. The extra relaxed drift directions U=N kerH are derived from the ACTUAL unpriced instantaneous noise directions, not chosen to hide a difficult state. The conclusion stays at OUTPUT means/closure and remains valid even where the full-state drift-only mean is false. It is therefore a substantive replacement representation for that blocked approach.

A future exact original synthesis theorem would still need to address at least the missing causal/current-window selection and actual unclosed state/control realization, as well as original stochastic internal stability. Hilbert projection alone supplies neither. DBL proves that actual realization cannot simply be read off a closed output relation. V16's exact interacting class remains a separate constructive result; no general optimal linear controller or stronger-admissible replacement is inferred from it, v17 or this successor.

The original arbitrary-plant prescribed-gamma literal N&S, unmatched stochastic and singular state/control tradeoffs, finite-horizon realization and general infinite stabilization remain OPEN. No finite matrix/Riccati algorithm computing the full time-operator projection, no numerical bound/solver/accountant, no pointwise-strict endpoint, full-book source promotion, new mechanism/priority/SOTA/publication or formal/kernel/human/configured-family/executable/triple-finite acceptance is delivered. Standard Hilbert duality/martingale/relaxation ideas have prior ancestry; novelty is not cleared.

## 10. Immutable process and same-round continuation

All FOUR own findings remain distinct/permanent: private written-exactness ZERO credit; post-v100 ACTUALRETURN/pre-primaryACK order; actual post-v107-body/pre-ACTUALRETURN PRIMARY/REVIEW INTERLEAVING with old blanket pause assurance withdrawn; and unsupported historical receipt counts with nonexistent extra coverage withdrawn. Four old unadmitted Eval records and every withdrawn scout receive ZERO verification/proof credit and are not rerun/back-converted. A later exact representation does not cure any finding.

Every parent/author/reviewer v9–v35/later root/freeze/source/read/clock/cadence/admission/withdrawal qualification, N4UNKNOWN/historical-exit-unestablished, auxiliary214 UNADMITTED/STOP and scientific HOLD remains. Current conventional proofs/tool chronology are not hidden model reasoning or a global clean cognition/runtime census. No scientific program/Eval/calculator/CAS/enumeration/solver/replay/build/test/CLI/nestedagent/newGO, frozen/shared/parent/source edit, Git/deletion/config/publication action occurred.

All older v1–v17 sources/reviews/ACKs/checkpoint/park/addendum chains remain immutable. Same ORIGINAL stochastic-preview target/eighteen owners, science cutoff2026-10-27T11:05:38-07:00 and delivery deadline2026-10-27T12:35:38-07:00; substantive actual-clock checkpoints remain at most30minutes while active. This complete increment is NOT an early finalpark or96-hour closeout. Fresh complete current mathematics AND dependency/application review is required before any promotion; previous branch/gate headlines do not accept it.
