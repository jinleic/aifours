# Literal preview with singular control price — pathwise adjoint obstructions and an interacting R=0 synthesis family

Owner **InfoHinfPreview-2 / info-3**. Actual immediately preceding `/bin/date` BEFORE this write: **Mon Oct 26 06:25:09 PDT 2026**. **NEW COMPLETE WRITTEN OWNER-CANDIDATE**, requiring its own full source/mathematics/dependency/application gate. No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver, replay, simulation, build/test, external-model CLI or nested agent was used. All derivations are SOURCE-SYMBOLIC, including private reasoning; no numerical/rational parameter trial or approximate magnitude scout was used. No mathematical machine check is claimed.

## 0. New representation, actual reach and unchanged original gap

V15 showed that finite GLOBAL literal/RMS OUTPUT gain and full-state EMS do not imply H1 or expected-L2 integrability of a free control. Its visible output was uncontrollable, and u=0 achieved the same gain. That does not justify giving up all necessary estimates at singular control price, nor prove a general stronger-admissible replacement theorem.

Here the replacement representation is a **deterministic diffusion-annihilating ADJOINT identity applied PATHWISE**, not a full-state mean and not a projected H1 argument. It gives:

1. A finite-horizon necessary variational bound for EVERY original constant plant, arbitrary ranks of D0/D1 and arbitrary control-noise, against every strongly admissible nonlinear causal law with only LOCAL PATHWISE control-L2. Each test's contracted stochastic integral is algebraically ZERO; its state/control integrability is never inferred from output gain.
2. A finite linear-algebra necessary obstruction and an explicit finite-horizon sine-test matrix inequality. Infinite-horizon lower bounds use compact tests only, with no terminal-state or expected-state transversality.
3. An ENTIRE parameter family with **R=D1^TD1=0, B nonzero, A0 nonzero, B0 nonzero and genuinely control-dependent priced output**, on which strict-uniform infinite literal synthesis is exactly decided at every prescribed gamma and every finite h>=0. A stationary ORIGINAL current-state/left-window-tap controller attains the sharp value and is fully internally EMS. Its homogeneous multiplicative noise is not globally erased.

The exact synthesis family is not v15's uncontrollable visible subsystem with another unpriced augmentation. Its drift control changes the performance state through a nonzero coupling, and its optimum balances TWO priced state coordinates. Earlier v5/v12 synthesis domains require R>0; they do not silently include it. The general adjoint condition is NECESSARY ONLY; no claim that these tests characterize arbitrary-plant feasibility or optimality is made.

Original arbitrary-data prescribed-gamma literal synthesis and actual printed realization remain OPEN. The printed page has expectation OUTSIDE each time-L2 norm; strict UNIFORM G1<gamma is our declared research convention, not an invented printed supremum symbol. The new realizer is genuinely stationary, so no finite-time F_t convention is needed for its synthesis statement. No pointwise-strict endpoint or finite-horizon optimality extension is asserted.

## 1. Prospective chronology, actual source uses and imports

The ENTIRE v118-B233+280 review was pinned and ACTUALLY RETURNED before the NEW whole-primary ACK `primary-resumption-after-v118-ack-v1.json`, SHA256 `4e9e9fd5f3430ee5727e55a476cc2a30343d736d9da0a1ee51d22c14041c4edd`, observation06:15:19, SENT after actual06:15:53 and BEFORE all current primary source/reasoning. No live review was interleaved with the present development.

The initial adjoint-test idea was ALREADY exposed before WORKER RECEIPT of v118, after the preceding SENT post-v116 primary ACK, and fully saved in checkpoint36, SHA256 `49ee55856c879dda90a4a6929b00282fe62278027d790d3d4706fccf8db2f704`. It is not called a post-v118-ACK discovery or preregistration. The current arbitrary-rank/sine-matrix and interacting-family expansion was saved substantively in checkpoint37, actual06:23:09, SHA256 `f98f4d76dfe6f7544660917d8b33fde2d9d1c0ebed6288684043e77cb2c23dad`, before this complete body. Saving primary state during a review was not used to expand its proof.

Actual inputs/context read:

| Source | Current actual use/read | SHA256 |
|---|---|---|
| `RUN/preview-v3-model-source-boundary-v1.md` | COMPLETE17LF; literal model, expected-norm/strictness/information boundary | `c66113762df23694d3446fa48d716da9bc0c6a5e953d115cd706694017fef78a` |
| own `literal-preview-synthesis-consolidated-v5-visible-quotient.md` | RAW15–98, entire operative R>0/quotient/projected-H1 domain, comparison ONLY | `0ecb7a5d574ad5a4c58b8c24037a5a384aaf6d20777ede08f747e133d9b9e3c7` |
| own `literal-preview-synthesis-consolidated-v12-visible-DC-matching.md` | RAW15–58, operative R,Q>0/DC necessary domain, comparison ONLY | `c19440f3dc2197e0be0aa0dc0548707758668b03fe013902e08fd06ee5cb6fde` |
| own complete v15 | COMPLETE255LF before v118, comparison/per-law limitation ONLY | `b7a2984a8ee1985c5c1a38c4d78e729fdef82a35a4a9fb1deabf99c481b7a571` |
| `RUN/preview-v15-global-gain-nonH1-and-strictness-parent-v1.md` | COMPLETE true ending before v118, scoped boundary ONLY | `a75ffce8bd111693fb9786f1811bdb8762d52757ebdc13daf18e5c1cb7c71e99` |
| `RUN/preview-v14-sequential-probability-parent-v1.md` | COMPLETE true ending before v118, scoped norm comparison ONLY | `e89a06e05bb1506ff1d896ab9541bb9a6a4f00c89e8fea5e9731ea1e1f4cba07` |

RUN means `institute/runs/three-area-2026-10-23-96h/`; own files are in this exclusive owner root. Targeted earlier-domain searches are not full-body proof reading. No linked old author/reviewer library is freshly claimed read from a source pin. The actual book rasters were viewed in the earlier v15/source-boundary work; this new packet does not pretend a new pixel read from their hashes.

**No v4/v5 Riccati theorem, v10 mean bootstrap, v12 DC theorem, v14 norm bridge or v15 scalar Bessel proof is a mathematical premise of the NEW proofs below.** All necessary new identities are displayed. Ordinary imports are deterministic finite-variation/semimartingale integration by parts and construction/localization of Brownian Itô integrals, finite-dimensional linear algebra/Gram order, elementary L2 Cauchy/Young inequalities and trigonometric integrals, global linear-SDE well-posedness/finite-prefix second moments, stopped Itô/Lyapunov expectation and Gronwall. These are named standard interfaces, not formalized foundations. No stochastic bounded-real/Riccati synthesis theorem or unpriced-control martingale expectation is imported.

## 2. The actual arbitrary-rank original plant and deterministic test space

Let state X∈R^n, control u∈R^m, disturbance w∈R^q, output z∈R^p and ONE scalar Brownian W satisfy the ORIGINAL constant-data equation

```text
dX=(A X+B u+C w(t-h))dt+(A0 X+B0 u)dW,
z=D0 X+D1 u.                                           (P)
```

All dimensions/ranks of the fixed real matrices are arbitrary. No R inverse, positivity, noise-output factorization, detectability or invariance condition is placed on(P). Gain initial state/negative input history are0. The allowed disturbances are all canonical progressive w with finite expected squared time energy. Unknown controls are progressive, strongly well posed/nonexplosive and locally PATHWISE time-L2. They may be nonlinear and may have infinite expected control norm, expected bracket root or state moments. The lower theorem allows the larger consistent causal-history class; consequently it applies to the printed current-state/current-window subclass.

For finite T>h>=0, count input on[0,L], L=T-h, and output on[0,T]. Put

```text
N1(f)=E||f||_time-L2,
G1,T(F)=sup_(nonzero allowed w) N1(z(w))/N1(w).
```

On infinity both norms are over[0,infinity). Gains are extended nonnegative reals; no assertion that finite G1 implies free-control integrability is made.

A deterministic adjoint test consists of

```text
lambda∈H1_0((0,T);R^n),   g∈L2((0,T);R^p),
A0^T lambda=0,   B0^T lambda=0,
lambda_dot+A^T lambda=D0^T g,
B^T lambda=D1^T g,                                    (ADJ)
```

all identities a.e. in time. H1_0 means the absolutely continuous representative has BOTH endpoint values0 and square-integrable derivative. Define the counted disturbance dual

```text
q_lambda(s)=C^T lambda(s+h),  0<=s<=T-h.                 (Q)
```

Tests are PROOF variables, not additional controller states, preview taps or randomized adversaries. No change in the controller information class occurs.

## 3. Rank-free PATHWISE identity and literal-gain obstruction

**Theorem1 — WRITTEN arbitrary-rank necessary bound.** For every test(ADJ), every original locally admissible response and every allowed input, pathwise on the finite horizon,

```text
integral_0^T g(t)^T z(t)dt
 =-integral_0^(T-h) q_lambda(s)^T w(s)ds.                (ID)
```

In particular, for any admissible law,

```text
G1,T(F)>=||q_lambda||_L2/||g||_L2  for every g!=0.       (LB-T)
```

On infinity, the same ratio over ANY finite compact test interval is a lower bound for G1,infinity(F). No state/control expectation or terminal-state limit is needed.

**Proof.** X is a continuous nonexplosive semimartingale; on each finite interval its paths are bounded. Local pathwise-L2 of u makes the drift locally integrable and the original diffusion locally square integrable. The deterministic AC lambda has finite variation, so the semimartingale product rule is legitimate after ordinary localization, or directly with the localized Itô integral:

```text
d(lambda^T X)
 =[ (lambda_dot+A^Tlambda)^T X+(B^Tlambda)^T u
                                      +lambda^T C w(t-h)]dt
       +lambda^T(A0X+B0u)dW.
```

The contracted diffusion integrand is IDENTICALLY ZERO by ADJ, not a merely local martingale being declared mean-zero. The two drift terms are exactly g^T(D0X+D1u). The endpoint products vanish because lambda(0)=lambda(T)=0, irrespective of any finite-moment property. Negative input history is0 and changing variables gives(ID). Every time integral is pathwise defined by finite-prefix continuity/local-L2 and Cauchy.

For deterministic w, Cauchy applied to(ID) gives

```text
||g||_L2 * ||z(w)||_L2 >= |integral q_lambda^T w|.
```

The right side is deterministic. Taking EXPECTED output norm is therefore valid even if it is infinite. If q_lambda!=0 choose the legal deterministic w=q_lambda; then ||w||=||q_lambda||, proving(LB-T). If q_lambda=0 the bound is0. If g=0, the ODE lambda_dot=-A^Tlambda and lambda(0)=0 force lambda=0, so no positive numerator is hidden behind a zero denominator. On infinity use the same compactly supported deterministic input and compare the full output norm with its prefix norm. This completes the proof without H1, Bochner state means, expected control energy, STATE-LOC, EMS or stochastic norm equivalence.

The variational supremum of(LB-T) is thus an exact NECESSARY obstruction. It is not claimed equal to an arbitrary plant's optimal gain, nor to be exhausted by the simpler constant-direction tests next.

## 4. Finite linear algebra and explicit sine-test matrix conditions

Choose ANY real vectors ell∈R^n, g0,g1∈R^p satisfying

```text
A0^T ell=0,   B0^T ell=0,
D0^T g0=A^T ell,   D1^T g0=B^T ell,
D0^T g1=ell,       D1^T g1=0.                          (LIN)
```

These form a finite-dimensional LINEAR subspace; its basis is a finite algebraic nullspace computation, not a solver run or an asserted numerical certificate. For any scalar f∈H1_0(h,T), extended by0 on[0,h], set

```text
lambda=f*ell,   g=f*g0+f_dot*g1.
```

The extension remains AC because f(h)=0, and(LIN) makes(ADJ) hold exactly. Moreover `integral f*f_dot=0`, so the cross term in ||g||² vanishes even if g0 and g1 are not orthogonal.

Take `f(t)=sin(pi*(t-h)/L)` on[h,T], L=T-h. Its exact integrals are ||f||²=L/2 and ||f_dot||²=pi²/(2L). The counted shifted f has the same norm. Thus Theorem1 gives

```text
G1,T(F)>=||C^T ell||
          /sqrt(||g0||^2+(pi^2/L^2)||g1||^2).            (SINE)
```

No explicit deterministic time variable is inserted into a controller: f is only a dual test/disturbance construction. Preview pre-actuation before h cannot evade the estimate, because the test vanishes there and has zero value at h; the ACTUAL control remains unrestricted throughout[0,T].

For infinity let L increase while applying these finite compact tests to the SAME law. If g0!=0,

```text
G1,infinity(F)>=||C^T ell||/||g0||.                     (DC-ANN)
```

If g0=0 but C^T ell!=0, SINE tends to infinity and EVERY admissible law has infinite gain. If both vanish the triple supplies no obstruction. This is a genuine all-input necessary divergence statement, not an invalid division by zero or an invented finite-horizon counterpart.

A finite matrix formulation retains every triple and all singular cases. Choose basis columns of the entire(LIN) subspace, written as E for ell, G0 for g0 and G1 for g1. Put

```text
Qann=E^T C C^T E,
Mann=G0^T G0,
Mann,L=G0^T G0+(pi^2/L^2)G1^T G1.
```

If a finite-horizon law has gain<=g, SINE for every linear combination gives `Qann<=g^2 Mann,L` in PSD order. If an infinite-horizon law has finite gain<=g, the compact-test limit gives

```text
Qann<=g^2 Mann.                                       (MAT)
```

Consequently strict-uniform feasibility at gamma requires such an inequality for SOME0<=g<gamma. Equivalently the finite generalized singular lower bound

```text
kappa_ann=inf{g>=0: Qann<=g^2 Mann}
```

must be<gamma; use infinity for an empty set and0 for the zero test space. A nonzero Qann direction in ker(Mann) is the infinite-gain obstruction. The basis choice does not matter, since the statement quantifies over the whole linear subspace. This is a finite necessary certificate for arbitrary ranks, not a general sufficient LMI, a Riccati solution or an executed matrix calculation.

## 5. NEW genuinely interacting unpriced data family

Fix ARBITRARY positive symbolic parameters

```text
a,b,c,d,e,beta,sigma,nu >0,   any finite h>=0.
```

Define the positive data constants

```text
k=beta*d^2/(a*e^2),
p=a+beta*k,
kappa=c/sqrt(a^2/d^2+beta^2/e^2).                       (K)
```

There are TWO states x,y, TWO controls u1,u2, scalar disturbance and output z∈R². The original constant plant is

```text
dx=(-a*x+beta*y+c*w(t-h))dt,
dy=(-b*y+u1)dt+[sigma*(y+k*x)+nu*u2]dW,
z=(d*x,e*y).                                          (FAM)
```

In the original matrix notation,

```text
A=[[-a,beta],[0,-b]],       B=[[0,0],[1,0]],
C=(c,0)^T,
A0=[[0,0],[sigma*k,sigma]], B0=[[0,0],[0,nu]],
D0=diag(d,e),              D1=0_(2x2).
```

Thus R=0, B!=0, A0!=0 and B0!=0. Both state coordinates are priced, and u1 changes y, which changes the priced x through beta>0. Unlike v15, the visible output is NOT uncontrollable. The genuine state-control tradeoff is not a hidden output-zero augmentation.

Full NEO fails: the direction X=0,u=(0,1) has z=0 but diffusion(0,nu) nonzero. Hence no full-state mean/H1 conclusion is licensed merely by z. The earlier R>0 quotient and full-coercive DC synthesis theorems do not cover this data class. The v13/v14 norm inequalities, even when applicable to a particular law, do not themselves supply this sharp same-gamma synthesis result.

**Theorem2 — WRITTEN exact infinite synthesis on ENTIRE(FAM).** Over every strongly admissible nonlinear causal controller, including the printed subclass with internal full-state EMS required, the optimal UNIFORM literal output gain is exactly kappa. It is attained by a stationary ORIGINAL current-state/left-tap controller satisfying even stronger expected control-energy admissibility. Thus, under the declared strict-uniform convention,

```text
exists printed internally-EMS controller with G1<gamma
               IFF gamma>kappa.                       (IFF)
```

This holds for EVERY parameter tuple in the displayed positive symbolic family and EVERY fixed finite h>=0. It is not an arbitrary singular-R synthesis theorem.

## 6. Necessity against ALL nonlinear/free-noise competitors

Use the actual test vectors

```text
ell=(1,0)^T,
g0=(-a/d,beta/e)^T,
g1=(1/d,0)^T.
```

The first row of A0 and B0 is0, so their transpose contractions with ell vanish. Directly,

```text
D0^T g0=(-a,beta)^T=A^T ell,
D0^T g1=ell,
D1^T g0=D1^T g1=0=B^T ell,
C^T ell=c.
```

Hence every nonlinear locally pathwise-admissible law on(FAM), whether or not its unpriced diffusion is H1 or its state has a mean, obeys the finite-horizon necessary bound

```text
G1,T(F)>=c/sqrt(a^2/d^2+beta^2/e^2
                              +pi^2/[d^2(T-h)^2]).     (FIN-LB)
```

On infinity DC-ANN gives G1>=kappa. This lower bound permits preview actions before h, arbitrary causal memory and arbitrary non-H1 u2; it does not assume that the eventual explicit law is optimal among linear controllers. It is already a lower bound for a LARGER controller class than the required printed internally-EMS class.

## 7. Stationary printed realizer, exact gain and genuine full internal EMS

Choose ANY positive symbolic rho with `rho>sigma^2/2`. This is a controller design parameter, not a numerical parameter trial. Put

```text
v=w(t-h),   r=y+k*x,
u2=0,
u1=b*y+k*a*x-k*beta*y-k*c*v-rho*r.                      (CTRL)
```

This ONE deterministic STATIONARY law uses ONLY current original(x,y) and the allowed fixed LEFT tap. r is an algebraic expression of the original current state, NOT an extra controller memory/state, reset, clock or input-energy statistic.

Substitution into the ACTUAL original SDE gives, for every allowed input,

```text
dr=-rho*r dt+sigma*r dW,
dx=(-p*x+beta*r+c*v)dt.                                (TRI)
```

All drift terms in dr cancel exactly; u2's free diffusion actuator is set to0. From zero initial state r is identically0 by strong uniqueness. Hence y=-k*x and

```text
x(t)=c*integral_0^t exp(-p*(t-s))*v(s)ds,
z(t)=(d,-e*k)^T*x(t).                                 (VIS)
```

The original output remains nonzero for nonzero deterministic forcing. Weighted Cauchy/Tonelli or the elementary convolution bound gives PATHWISE

```text
||z||_L2(0,infinity)
 <=[c*sqrt(d^2+e^2*k^2)/p] ||v||_L2
 =kappa*||w||_L2.                                    (PERF)
```

Finite delay preserves the full infinite input norm. Thus taking EXPECTED norm proves G1<=kappa on ALL allowed progressive inputs. The same pathwise inequality also bounds RMS output, but no general G1/RMS equivalence is needed.

The final algebra in PERF is exact. For any real j,

```text
(d^2+e^2*j^2)(a^2*e^2+beta^2*d^2)
       -d^2*e^2*(a+beta*j)^2
 =(a*e^2*j-beta*d^2)^2.
```

At j=k the square is0 and p>0. This proves the displayed coefficient equals kappa, without optimization by a numerical trial. The universal lower bound already proved G1>=kappa, so this realizer's gain and the ALL-controller optimum are exactly kappa. No separate finite pulse table, RMS substitute or unjustified state mean establishes sharpness.

### Full-state zero-window EMS, not just zero-state attenuation

For arbitrary square-integrable initial original state and zero input/window, set

```text
q=2rho-sigma^2>0,
L0=1+beta^2/(p*q),
V=x^2+L0*r^2.
```

The generator of TRI gives

```text
LV=-2p*x^2+2beta*x*r-L0*q*r^2
  <=-p*x^2+[beta^2/p-L0*q]r^2
   =-p*x^2-q*r^2
  <=-min(p,q/L0)*V.                                  (EMS)
```

Linear-SDE finite-prefix moments, stopped Itô/Fatou or the explicit r solution justify expectation; here it is the CONSTRUCTED globally linear law, not an unknown free-control martingale being assumed integrable. Gronwall and equivalence of V with the original state norm under the invertible map(x,y)↦(x,y+kx) give uniform full-state exponential MS stability. No gain-to-internal-stability implication is used.

The autonomous diffusion `sigma*r dW` is genuinely NONZERO away from the zero-state invariant graph. It has not been globally canceled from the homogeneous plant. The two-state internal problem is therefore actually checked, rather than removed from the performance calculation.

### All-input strong admissibility and control energy of the constructed law

TRI is globally linear with progressive expected-L2 forcing v; it has a unique strong nonexplosive causal solution. r is autonomous and has finite total expected squared energy for square-integrable initial state, since E r(t)^2=exp(-q*t)E r(0)^2. Stable convolution in the x equation then bounds the full expected time energy of x by fixed multiples of initial energy, expected r energy and expected input energy. y=r-kx inherits the same bound. CTRL is a fixed linear combination of x,y,v and u2=0, so its expected control energy is finite as well. In particular it satisfies the weaker original local-pathwise admissibility.

For the zero-state gain test, the sharper VIS/PERF formulas hold input by input, even when the input is adapted to the same Brownian motion. The proof is pathwise and does not assume deterministic disturbances for the upper bound. The lower tests were deterministic LEGAL inputs, so together they cover the full same-domain optimum.

If gamma>kappa, CTRL proves sufficiency in IFF with strict uniform margin. If gamma<=kappa, the universal lower certificate excludes every candidate law, even without imposing EMS, so it excludes the required printed EMS class. This proves both directions at the prescribed gamma. No pointwise-each-input endpoint claim is silently added; the declared uniform convention remains unchanged.

## 8. Exact advancement, limitations and no automatic union

The new useful general result is ID/LB-T and its arbitrary-rank finite matrix restriction. Its contracted noise is exactly ZERO, which makes it immune to the unpriced strict-local-martingale obstruction: one does not fix v15's false full-state-mean shortcut by imposing a hidden expected-control hypothesis. It supplies usable necessary conditions even where R is singular or0 and NEO fails.

The genuinely interacting family FAM then matches that lower bound by an ORIGINAL stationary controller. The actuator changes priced performance, both states are observed/priced, autonomous state diffusion and a separate free diffusion actuator are nonzero, full internal stability is proved, and every finite preview horizon h is allowed on the infinite-time synthesis problem. This is not another scalar endpoint estimate, a restriction restatement or a stronger norm-comparison theorem only.

What is NOT proved:

- Completeness of deterministic noise-annihilating tests, or that their supremum equals the general optimal gain.
- A general sufficient condition from MAT, a universal singular-R Riccati/LMI or a lower bound for directions not represented by ADJ/LIN.
- Arbitrary unmatched stochastic state/control tradeoffs, a stronger-admissible replacement theorem for every feasible nonlinear law, universal linear optimality or a full-data prescribed-gamma N&S.
- Finite-horizon optimality/realization for FAM or general plants; FIN-LB is necessary only.
- A pointwise-strict gamma=kappa endpoint, arbitrary raw-path/remote-history implementation theorem, a new printed supremum/time argument, or a full-book solution.

The previously adopted conditional/price-controlled/quotient/norm and per-law non-H1 results retain their exact scopes. This new packet requires its OWN complete mathematics AND dependency/application reconstruction before parent promotion; a previous no-defect review does not accept the new arbitrary-rank identity, finite matrix extraction or interacting singular-price class. All classical techniques here have standard duality/invariant-manifold/Lyapunov ancestry; no novelty, SOTA, publishability or priority clearance is claimed.

## 9. Permanent process and round boundary

All FOUR own findings remain distinct and permanent: private written-exactness, post-v100 actual RETURN/pre-primaryACK order, actual post-v107-body/pre-ACTUALRETURN PRIMARY/REVIEW INTERLEAVING with its frozen blanket pause assurance withdrawn, and unsupported historical receipt counts with nonexistent extra coverage withdrawn. The four old unadmitted Eval records retain ZERO verification credit and were not rerun. No later exact proof or prospective ACK cures those events.

All author/reviewer/parent findings, actual-clock/read-order/cadence/root/freeze corrections, N4 UNKNOWN/historical-exit-unestablished and auxiliarySTOP/HOLD remain. The current bounded interval report is not an exhaustive clean cognition/runtime or continuous-eighteen-way census. No scientific program/Eval/calculator/CAS/enumeration/solver/replay/build/test/CLI/nestedagent/newGO, frozen/shared/parent edit, publication, Git/deletion/config change or stronger formal/kernel/human/configured-family/executable/triple-finite/novelty acceptance occurred.

All original sources, reviews, ACKs, park-v2/addenda and checkpoint chains stay immutable. Same ORIGINAL problem/eighteen owners, science cutoff2026-10-27T11:05:38-07:00 and deadline2026-10-27T12:35:38-07:00; substantive actual-clock checkpoints remain at most30minutes while active. This complete primary increment is NOT an early final park or96-hour closeout. The arbitrary-data original gap remains active.
