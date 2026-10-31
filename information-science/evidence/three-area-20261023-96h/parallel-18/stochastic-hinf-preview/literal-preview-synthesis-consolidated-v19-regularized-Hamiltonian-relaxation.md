# Closed-output preview relaxation — exact compact regularization limit and a finite Hamiltonian spectral representation

Owner **InfoHinfPreview-2 / info-3**. Actual immediately preceding `/bin/date` BEFORE this write: **Mon Oct 26 07:03:15 PDT 2026**. **NEW COMPLETE WRITTEN OWNER-CANDIDATE**, requiring its own full mathematics/dependency/application gate. SOURCE-SYMBOLIC analysis only, including privately; no numerical/rational parameter instance, finite-word control trial, decimal/magnitude scout or withdrawn-probe guidance. No scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay/matrix-exponential run/build/test/CLI/nestedagent/newGO. No machine-checked identity is claimed.

## 0. Exact advance and the essential nonpromotion warning

V18 identifies a CLOSED deterministic OUTPUT relaxation of arbitrary-rank literal stochastic preview synthesis. Its exact lower value was expressed by a Hilbert projection, not yet by finite-state differential equations.

This successor supplies an exact finite-horizon representation:

1. Strictly priced deterministic PROOF controls give a positive Hilbert resolvent and a unique regularized minimum for each deterministic disturbance.
2. At EVERY fixed finite T>h, the original forced-output operator is COMPACT. This upgrades strong resolvent convergence into OPERATOR-NORM convergence after forcing, so the regularized worst-input values decrease EXACTLY to the closed-output relaxation value.
3. Every positive regularized spectral value is equivalent to a singular block of an explicit2n-dimensional, TWO-piece constant Hamiltonian transfer. When the forced-output operator is nonzero, its largest positive spectral root is exactly the regularized squared norm. All zero, multiplicity and delay/counting branches are retained.

**Crucial:** a finite regularization value is an UPPER approximation of the NECESSARY RELAXATION value. It is NOT itself an original-controller lower bound. Pricing fictitious proof controls cannot be silently imposed on unknown unpriced stochastic controllers. Only the exact relaxation limit, together with the separately proved stochastic-to-output-closure bridge, is a necessary original gain bound. No same-gamma original synthesis or printed realizer is produced by the Hamiltonian calculation.

## 1. Prospective authority and exact dependency cut

ENTIRE v120-B was ACTUALLY RETURNED before the new whole-primary ACK SHA256 `00671413a6b56430de28200b355cdfdba71eb22c9e620e8fe4082b603cb2ed28`, written06:44:04 and SENT after06:44:42 BEFORE all current primary work. The whole new regularization/Hamiltonian derivation was saved in checkpoint41, actual07:01:28, SHA256 `333691d5d14e36ccd3df8269317442c421fce2aeb7dcf8744614d7e823340b99`, before this complete source. No live review was interleaved.

The complete predecessor is own `literal-preview-synthesis-consolidated-v18-closed-output-relaxation.md`,275LF/21014B, SHA256 `7139d396c8efbb62482a025bdeefcd0111d3c73d84b7969c6c2b523b514b13f3`. It remains an UNGATED written owner candidate, not an accepted theorem by hash. The NEW deterministic operator/compactness/Hamiltonian claims below have complete proofs independent of its stochastic bridge. Applying their limit as an ORIGINAL stochastic lower bound is explicitly CONDITIONAL on that named v18 whole compatibility theorem; its operator definitions are reproduced next. No automatic v16/v17/v18/v19 union adoption is claimed.

Named ordinary inputs: bounded Hilbert operator/adjoint/orthogonal projection facts; coercive strictly convex quadratic minimization; finite-interval Volterra/Fubini estimates and Hilbert–Schmidt compactness (also proved in the needed scope); weak compactness in Hilbert space; elementary finite-dimensional ODE/fundamental-matrix algebra and integration by parts. No stochastic bounded-real lemma, Riccati synthesis theorem, graph/finite enumeration, external scientific code or numerical root theorem is a premise. Every delay, variational sign, compactness, singular-control and positive-root application is given below.

The original model/source boundary remains COMPLETE17LF `RUN/preview-v3-model-source-boundary-v1.md`, SHA256 `c66113762df23694d3446fa48d716da9bc0c6a5e953d115cd706694017fef78a`, actually read in the current primary chain. Expectation stays OUTSIDE the path norm and the uniform-strict convention is declared, not a printed supremum. No new book-pixel read is claimed.

## 2. Reproduced finite-horizon output relation

The original constant-data model is

```text
dX=(A X+B u+C w(t-h))dt+(A0 X+B0 u)dW,
z=D0 X+D1 u,
```

with one scalar Brownian motion, arbitrary real matrix ranks, gain initial state/negative input history0 and ALL progressive expected-time-L2 disturbances. Unknown original controls need only strong nonexplosive nonanticipative well-posedness and local PATHWISE control-L2. No stronger expected control energy is inserted.

For FIXED finite T>h>=0, set L0=T-h, H=[D0 D1], N=[A0 B0], U=N kerH, and choose a basis E_U of U. On the proof system introduce a=(v,r),

```text
G=[B E_U],   D=[D1 0],
x_dot=A x+G a+C w(t-h),   x(0)=0,
y=D0 x+D a.                                           (REL)
```

Here w is deterministic and counted on[0,L0], extended by0 before0. a is an arbitrary deterministic time-L2 PROOF control, not a physical actuator or causal/current-window policy granted to the original controller.

Let W=L2(0,L0;R^q), Y=L2(0,T;R^p), and V=L2(0,T;R^(m+dimU)). Define

```text
(T_C w)(t)=D0*integral_0^t exp(A(t-s))*C*w(s-h)ds,
(S a)(t)=D*a(t)+D0*integral_0^t exp(A(t-s))*G*a(s)ds.
```

Both are bounded on their finite-time Hilbert spaces, regardless of stability of A. Let K=ker S* and P_K its orthogonal projection. The closed output relation is `T_Cw+closure(range S)`, with exact minimum-norm output P_K T_Cw. Denote

```text
kappa_rel(T,h)=||P_K T_C||.
```

This last output-space statement follows directly from Hilbert orthogonal decomposition. The ADDITIONAL assertion that an original finite-N1 stochastic output mean belongs to that closed relation is the named v18 theorem, not a new assumption that E X/E u exist. This packet does not replace its scalar-H1/source/application gate with a deterministic title.

## 3. Exact strictly priced PROOF-control resolvent

For eta>0 and arbitrary y∈Y, consider

```text
j_eta(y)=inf_(a in V) {||y+S a||_Y^2+eta||a||_V^2}.
```

This is strictly coercive quadratic optimization on a Hilbert space. The unique stationarity solution is

```text
a_eta=-(S*S+eta I)^(-1)S*y.
```

The inverse exists/bounds by1/eta: `<a,(S*S+eta I)a>>=eta||a||²`, and the ordinary coercive quadratic minimization/Riesz argument gives surjectivity. Put

```text
R_eta=I-S(S*S+eta I)^(-1)S*
     =(I+eta^(-1)S S*)^(-1).                           (RES)
```

The second identity follows by multiplying by I+SS*/eta and using `(S*S+eta I)^(-1)(S*S+eta I)=I`; no finite-dimensional inversion or numerical resolvent is assumed.

The actual optimal output is y_eta=y+S a_eta=R_eta y. Stationarity gives `S*y_eta=-eta a_eta`, so

```text
j_eta(y)=||y_eta||²+eta||a_eta||²
        =<y_eta,y_eta-S a_eta>=<y,R_eta y>.             (VAL)
```

Thus R_eta is positive selfadjoint, and0<R_eta<=I. More quantitatively,

```text
[eta/(eta+||S||²)]I <=R_eta<=I.
```

For each y the value increases with eta, by the defining nonnegative penalty. Hence R_eta decreases in quadratic-form order as eta decreases. On K=kerS*, R_eta is identity; on K-perp it remains selfadjoint invariant. In particular R_eta>=P_K.

These are PROOF optimization values. No original unknown controller is asserted to have finite expected a-energy or to solve this noncausal minimization.

## 4. Strong convergence and why finite-time forcing makes the NORM limit exact

### 4.1 Strong resolvent limit without a closed-range assumption

For y=S b with arbitrary b∈V, testing a=-b gives

```text
<y,R_eta y>=j_eta(y)<=eta||b||².
```

Since0<=R_eta<=I, `||R_eta y||²<=<y,R_eta y>`, so R_eta y tends to0 on range S. The contraction bound extends that convergence by norm density to closure(range S)=K-perp. On K the operator is identity. Therefore

```text
R_eta ->P_K STRONGLY as eta decreases0.                (STRONG)
```

No equality range S=closed range S, compactness of S, spectral gap or expected-control regularity was used. STRONG alone does NOT justify operator-norm convergence on all of Y.

### 4.2 T_C is compact for the ACTUAL original output model

Written on the counted-input/output rectangle, T_C has matrix kernel

```text
K_C(t,s)=D0 exp(A(t-s-h))C *1_(t>=s+h),
0<=t<=T, 0<=s<=L0.
```

It is bounded and square integrable on this finite rectangle. Approximate its finitely many entries in L2 by finite sums of rectangle/simple tensor functions. The corresponding operators have finite rank, and Cauchy bounds the operator norm error by the L2 kernel error. Thus T_C is compact (the needed Hilbert–Schmidt conclusion) with no Hurwitz or smooth-kernel assumption. The discontinuity along t=s+h and h=0 are harmless L2 boundaries.

The absence of an unfiltered DIRECT w term in the original z=D0X+D1u is important. This compactness is not asserted for a different model containing a direct disturbance-output term, nor for an infinite-time convolution operator.

### 4.3 Exact worst-input value convergence

Set E_eta=R_eta-P_K, a positive uniformly bounded operator converging strongly to0. The closure of T_C's unit-ball image is compact. For any finite accuracy, choose a finite net in that image; strong convergence at those finitely many net points plus the uniform operator bound gives

```text
||E_eta T_C|| ->0,
||T_C*E_eta T_C|| ->0.
```

Therefore the compact positive operators

```text
K_eta=T_C*R_eta T_C
```

converge in OPERATOR NORM to `T_C*P_K T_C`. Define the regularized worst-input value by

```text
kappa_eta(T,h)^2
 =sup_(w!=0) j_eta(T_Cw)/||w||²
 =||K_eta||.
```

Their squares are nonincreasing as eta decreases, and the exact limit is

```text
lim_(eta down0) kappa_eta(T,h)^2
     =||T_C*P_K T_C||=kappa_rel(T,h)^2.                 (LIMIT)
```

The final equality is the ordinary norm identity for P_K T_C. This is an actual compactness-based optimization/norm-limit proof, not an unproved interchange of an infimum and a limit. It holds at EACH FIXED finite T>h.

No sup-over-horizons/eta-limit interchange is claimed. When invoking v18's stochastic compatibility theorem, the valid original necessary bound is `sup_(T>h) lim_(eta down0) kappa_eta(T,h)`, in that order. Infinite-time compactness and any different order remain unproved here.

## 5. Exact finite2n Hamiltonian representation of EACH positive regularized spectrum

### 5.1 Matrix data, all singular original prices retained

For fixed eta>0 define

```text
Q=D0^T D0,
S0=D0^T D,
R0=D^T D+eta I >0,
Atilde=A-G R0^(-1)S0^T,
Qbar=Q-S0 R0^(-1)S0^T >=0,
Bbar=G R0^(-1)G^T.
```

R0 is positive even if the ORIGINAL D1^TD1 is singular/zero. Qbar>=0 is the Schur complement of the actual nonnegative quadratic cost `|D0x+D a|²+eta|a|²`; equivalently minimize that instantaneous cost over a. This regularization is of fictitious PROOF controls only. If the proof-control dimension is zero, omit the corresponding inverse/products; the equations reduce to the no-control formulas.

For a spectral scalar lambda>0 introduce the TWO constant Hamiltonian matrices

```text
H0(lambda)=[[Atilde, -Bbar],[-Qbar,-Atilde^T]],
H1(lambda)=[[Atilde, -Bbar+lambda^(-1)C C^T],
                         [-Qbar,-Atilde^T]].            (HAM)
```

H0 does not actually depend on lambda. Let

```text
Phi_lambda=exp((T-h)H1(lambda))*exp(h H0),
F22(lambda)=lower-right n-by-n block of Phi_lambda.     (TRANSFER)
```

Order of multiplication is essential: no counted forcing reaches the plant before h, so H0 acts first. h=0 simply removes its duration; all controls remain available from0, including noncausal proof pre-actuation.

### 5.2 Eigenvalue -> actual state/adjoint boundary problem

Let a_eta(w) be the unique proof minimizer, x its actual deterministic REL state and y=D0x+D a its output. Define

```text
p(t)=integral_t^T exp(A^T(s-t))*D0^T y(s)ds.
```

Then p(T)=0 and `-p_dot=A^T p+Qx+S0 a`. The control stationarity equation is

```text
S0^T x+R0 a+G^T p=0,
a=-R0^(-1)(S0^T x+G^T p).                              (STAT)
```

It is equivalent to `D^Ty+eta a+G^Tp=0`, the exact first variation of the strictly convex cost; no causal feedback assumption is made.

The optimal output is `y=R_eta T_Cw` by §3. Fubini/variation of the forced output therefore gives

```text
(K_eta w)(s)=C^T p(s+h), 0<=s<=L0.                     (EIG-OUT)
```

Thus an eigenvalue equation `K_eta w=lambda w` is EXACTLY

```text
lambda w(s)=C^T p(s+h).
```

Eliminating a by STAT and this w by the delayed forcing gives

```text
[x;p]_dot=H0[x;p] on[0,h),
[x;p]_dot=H1(lambda)[x;p] on[h,T],
x(0)=0, p(T)=0.                                       (BVP)
```

The chi switch is the original counted interval: at plant time t>=h the optimizing input index is s=t-h, and for t<h its forcing is0. No input before0 or afterT-h is silently supplied.

### 5.3 Boundary problem -> eigenvalue, with no spurious zero-input solution

Conversely, suppose BVP has a nonzero solution. Define `w(s)=C^Tp(s+h)/lambda` and a by STAT. They are genuine finite-time L2 proof functions, and x is the REL solution. The p equation is its exact output-cost adjoint, so STAT makes a the unique strictly convex minimizer for that w. EIG-OUT then gives K_eta w=lambda w.

It remains to prove w is NONZERO. If w=0, STAT is stationarity for the homogeneous strictly convex control problem whose cost is `||S a||²+eta||a||²`. Its unique minimizer is a=0. The zero initial state then gives x=0, and the terminal homogeneous adjoint gives p=0, contrary to nonzero BVP. Thus there is no spurious positive root arising from an uncontrolled/invisible state or an arbitrary terminal mode.

Starting x(0)=0, a solution is determined by p(0)=xi. Its terminal adjoint is F22(lambda)xi. If xi=0 the whole solution is0. Therefore

```text
lambda>0 is an eigenvalue of K_eta
   IFF det F22(lambda)=0.                              (ROOT)
```

All kernel dimensions/multiple roots are retained; no derivative, simple-root, generic-rank or selected-minor premise is used.

### 5.4 The LARGEST positive root is exactly the regularized squared norm

K_eta is compact, positive and selfadjoint. If T_C!=0, the lower bound on R_eta gives K_eta!=0. Its positive norm is attained by a unit vector: take a maximizing unit sequence, select a weakly convergent subsequence, and use compactness of K_eta to pass its quadratic forms. The limit cannot have norm<1, since scaling it would exceed the positive supremum. The stationary Rayleigh variation then gives an eigenvector at the norm. Every other positive eigenvalue is at most that norm.

Combining this with ROOT proves

```text
kappa_eta(T,h)^2
       =LARGEST positive root of det F22(lambda)=0
       whenever T_C!=0.                               (MAX-ROOT)
```

If T_C=0 then K_eta=0, kappa_eta=0 and ROOT proves there are NO positive roots. This separate branch is not an undefined “largest root.” The possible accumulation of positive roots at0 and their multiplicities do not affect the largest-root statement. No eigenvalue/root was evaluated or isolated by a scientific program.

This is an exact finite-state spectral REPRESENTATION of each regularized proof value. It is not a finite-step root algorithm, complexity estimate, solver convergence certificate, original controller realization or assertion of an elementary inverse.

## 6. Why the finite regularized value is NOT an original necessary lower bound

By §4, kappa_eta>=kappa_rel and decreases to it. The regularization prices proof controls that the original stochastic problem does NOT require to have any finite expected norm. Even an actual deterministic original controller's output may be arbitrarily cheaper than the penalized proof objective. Therefore one may NOT conclude `G1(original)>=kappa_eta` from v18 compatibility.

At a fixed eta, finding kappa_eta>=gamma does NOT prove original infeasibility; it may decrease below gamma later. Finding kappa_eta<gamma proves only a bound on this relaxed value, not original sufficiency. The mathematically valid original necessity is the EXACT limit kappa_rel (or a separately valid actual adjoint test), conditional on the full v18 bridge. This warning prevents a silent clean cutover to a stronger expected-control problem.

The symbolic DBL family in v18 supplies an exact illustration. For positive a,b,c,d,

```text
x_dot=a*y+c*w(t-h),  y_dot=b*u,  z=d*x,
```

with zero Brownian coefficients and D1=0, the zero-input control-output range contains every smooth compactly supported output, by u=phi''/(d*a*b). Its closure is the whole output L2, so kappa_rel=0. Yet T_C is nonzero because positive forcing produces nonzero integrated output. R_eta is strictly positive, hence kappa_eta>0 for EVERY eta>0. Thus a finite priced value cannot be substituted for the zero exact relaxation value. V18's stronger pulse nonattainment control remains separate; it is not needed to establish this positive-versus-zero regularization warning.

No scalar numerical parameter substitution, trial threshold or scientific execution is used in this entire symbolic family. The original fixed-positive-gamma synthesis question for that family is not being settled by this warning.

## 7. Exact theorem boundary and original remaining work

The deterministic theorem delivered here is COMPLETE: for each fixed finite T>h, the regularized proof optimization has the exact resolvent/quadratic form; compact original forcing yields exact operator-norm convergence to the closed output relaxation; and its positive regularized spectrum/norm is exactly the explicit finite2n transfer-block singularity, including all delay/zero/multiplicity cases.

The APPLICATION as a necessary ORIGINAL stochastic literal-gain bound retains the NAMED v18 output-compatibility theorem. This packet does not make a new full-state expectation, force old unpriced controls into expected-L2, or independently re-adopt v18's scalar-H1/source proof from a headline. Its full source and every operative edge must be included in a future joint gate if that application is promoted. The deterministic spectral theorem itself does not use the old exact-synthesis family or any external bounded-real/Riccati theorem.

Still OPEN: causal/printed current-window selection, actual unclosed-range realization, original stochastic internal stability, arbitrary-data prescribed-gamma N&S, unmatched stochastic state/control tradeoffs and general stronger-admissible replacement. The projection/proof control can use more future input than the original information class allows. Compact finite-horizon regularization does not remove that obstacle or permit an infinite-horizon/supremum limit swap.

No original finite-price synthesis criterion, controller certificate, evaluated norm/root, finite matrix assay, algorithm/optimizer/accountant convergence, finite scientific execution, world-wide novelty/source-equivalence/priority/SOTA/publication, full-book solution, formal/kernel/human/configured-family/executable/triple-finite acceptance or new GO is claimed. All methods have ordinary Hilbert regularization/variational/Hamiltonian ancestry; only the exact current model-specific representation and its qualified application are supplied.

## 8. Permanent process and continuation

All FOUR own findings remain distinct/permanent: private written-exactness ZERO credit; post-v100 ACTUALRETURN/pre-primaryACK order; actual post-v107-body/pre-ACTUALRETURN primary/review interleaving with old blanket pause assurance withdrawn; and unsupported historical receipt counts with nonexistent extra coverage withdrawn. Four old unadmitted Eval records and every withdrawn scout are not replayed/back-converted or credited. Later exact mathematics does not cure history.

Every parent/author/reviewer v9–v35/later source/root/freeze/read/clock/cadence/admission/withdrawal qualification, N4UNKNOWN/historical-exit-unestablished, auxiliary214 UNADMITTED/STOP and HOLD stays binding. Conventional proofs/tool chronology are not hidden model reasoning or an exhaustive clean cognition/runtime census. No pinned/shared/parent/source edit, Git/deletion/config/publication or scientific launch occurred.

All older v1–v18 sources, reviews, ACKs, checkpoint/park/addendum chains remain immutable. Same ORIGINAL stochastic-preview problem/eighteen owners, science cutoff2026-10-27T11:05:38-07:00 and delivery deadline2026-10-27T12:35:38-07:00; substantive actual-clock checkpoints remain at most30minutes. This complete new representation is NOT an early finalpark or96-hour closeout. The original general synthesis gap remains active; fresh complete mathematics AND dependency/application review is required before promotion.
