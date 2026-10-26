# Literal preview synthesis through the visible quotient — genuinely uncancelled hidden multiplicative noise

**InfoHinfPreview-2 / info-3. ONE immutable consolidated WRITTEN successor; OWNER-CANDIDATE at the exact named v4 lemma dependency.** Actual immediately preceding `/bin/date` observation: **Sun Oct 25 12:17:37 PDT 2026**, a real precreation observation bound.

## 0. Genuine new representation and exact dependency/gate boundary

The v4 class canceled the ENTIRE state diffusion. This successor allows stochastic diffusion that genuinely remains in a performance-unobservable state subspace and can even make the FULL global NEO condition fail. A projected H1/Jensen argument supplies necessity without taking a nonexistent full-state expectation. A quotient Riccati law is lifted to the ACTUAL original state/current-window controller; only its VISIBLE diffusion is zero. Finite-horizon synthesis is exact on this explicit domain. An additional hidden-state Lyapunov certificate supplies full-state internal stability on infinity; visible gain alone is NEVER used to infer that stability.

Named mathematical dependency: the frozen COMPLETE488LF `literal-preview-synthesis-consolidated-v4-positive-preview.md`, SHA256 **`2def3e70fc69253fdda6428b36fe946d59986d9aae6d9f485f54b8131dd5ae43`**, specifically its deterministic finite-preview completion/converse/Hamiltonian/strict-Volterra lemmas and deterministic infinite stabilizable/detectable Riccati-limit/realization argument. These are WRITTEN owner proofs, NOT independently accepted from v3's verdict. The full v4+THIS source UNION must be actually reconstructed before promotion; a no-defect branch review is not a joint union audit. This source states the formulas/interface explicitly and proves every NEW quotient/lift/hidden-stability step, rather than repeat488LF of unchanged kernel algebra.

The separate later exposure record `primary-continuation-20261025-102319-ack-addendum-2.json` preceded this body. Informal quotient reasoning before that ACK is disclosed there and in checkpoints5/6, not called preregistration. Actual v83-B was fully returned before resumption. The current complete17LF parent v3 boundary was read with cutlines recovered: SHA256 `12729a9e09479d339982dcb29faccb53d6d2e5473329d8acc5cb28fa4f1db063`. It supports v3 ONLY, and expressly leaves v4 separate. Complete17LF model boundary SHA256 `c66113762df23694d3446fa48d716da9bc0c6a5e953d115cd706694017fef78a` was read.

Finite deterministic F_t and strict UNIFORM G1<gamma remain DECLARED research conventions; the book omits explicit t and the supremum symbol. This successor does not turn those into printed syntax, claim a stationary finite-horizon theorem or solve the unrestricted book problem. All v1–v11/HOLD and additive artifact/chronology corrections remain. No scientific interpreter/eval/program, arithmetic/symbolic calculation, enumeration, matrix/Riccati/LMI solve, simulation, replay, CLI or nested agent was used. Everything below is WRITTEN, not kernel-checked or novelty-cleared.

## 1. Actual plant and output completion

Use the same actual constant-data plant

    dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW,
    z=D0x+D1u,

with scalar Brownian W, h>=0, zero initial/negative-time input history and all progressive disturbances of finite expected squared energy. Finite output is[0,T], input ONLY[0,T-h], T>h; on infinity both run to infinity. Every controller is one fixed strongly well-posed, nonanticipative/event-local law across inputs. Finite-time deterministic clock dependence is allowed as declared; no enlarged memory or input-energy state is added.

Assume the ACTUAL full-column control-cost condition

    R=D1^TD1>0,
    K0=-R^(-1)D1^TD0,
    Abar=A+BK0,
    S=A0+B0K0,
    Q=D0^TD0-D0^TD1R^(-1)D1^TD0>=0,
    v=u-K0x.

Then

    Dtilde=D0+D1K0, Dtilde^TD1=0, Dtilde^TDtilde=Q,
    z=Dtilde*x+D1*v,
    |z|^2=x^TQx+v^TRv.                                  (1)

No finite N2(v) is inferred from finite N1(z).

## 2. A finite, coordinate-invariant visible quotient

Let U be the LARGEST Abar-invariant subspace contained in kerQ. It is obtained by the finite algebraic definition

    U=intersection_(k=0)^(n-1) ker(Q Abar^k).             (2)

Cayley–Hamilton proves invariance: the k<n-1 equations shift directly under Abar, and the final power reduces to lower powers. Conversely every invariant subspace in kerQ satisfies all these equations. Thus this is an actual computable matrix subspace, not an assumed hidden-state realization.

Choose pi with orthonormal rows spanning U-perpendicular and Z with orthonormal columns spanning U. Put r=n-dimU, y=pi*x and q=Z^T*x. Then

    pi*pi^T=I_r, x=pi^T*y+Z*q,
    pi*Abar=Avis*pi, Avis=pi*Abar*pi^T,
    Bvis=pi*B, Cvis=pi*C, Qvis=pi*Q*pi^T,
    Q=pi^T Qvis*pi,
    Dtilde*Z=0.                                         (3)

The final equality follows because |Dtilde*a|^2=a^TQa=0 for a in U. Thus the ACTUAL output vector, not just an average, factors as

    z=Dvis*y+D1*v, Dvis=Dtilde*pi^T,
    |z|^2=y^TQvis*y+v^TRv.                              (4)

The quotient pair(Avis,Qvis^(1/2)) is observable. Indeed a quotient vector invisible under all quotient powers lifts to a vector in U-perpendicular satisfying every equation(2), hence also lying in U and therefore zero. Cayley–Hamilton gives the equivalent finite observability test.

Changing pi to O*pi for orthogonal O only conjugates the barred matrices, graph/Riccati solution and quotient state. The lifted controller below is unchanged. Changing Z by an orthogonal hidden basis gives congruent hidden Lyapunov tests. The result is independent of arbitrary coordinate choices.

## 3. Exact actual-data domain and a projected H1 bridge

The NEW finite theorem assumes

    pi*S=0,                                             (QMATCH)
    pi*B0*R^(-1)*B^T*pi^T=0.                            (QORTH)

These are finite algebraic conditions on actual matrices and the actual U from(2). They do NOT require S=0 or full B0R^(-1)B^T=0. The entire state diffusion may remain nonzero. Global NEO need not hold.

For ANY original nonlinear law, projection gives

    dy=(Avis*y+Bvis*v+Cvis*w(t-h))dt
                                  +B0vis*v dW,
    B0vis=pi*B0.                                        (5)

The hidden coordinate has disappeared from the DRIFT because U is Abar-invariant; QMATCH removes autonomous visible diffusion. Moreover

    v=R^(-1)D1^T z,
    B0vis*v=B0vis*R^(-1)D1^T z.                        (6)

So finite literal output N1(z) controls the PROJECTED diffusion's H1 norm. The full-state diffusion, and the full-state mean, need not be integrable and are not used.

Explicitly, for a deterministic counted input and a law of gain at most g, (4) bounds E||v||_L2 and(6) bounds `E(integral|B0vis*v|^2)^(1/2)`. The H1 good-lambda/localization argument in v3/v4 makes this PROJECTED martingale true mean-zero. Gronwall on(5) gives E sup|y|<infinity, independently of any hidden moment. Fubini and Bochner Jensen therefore give

    ybar'=Avis*ybar+Bvis*vbar+Cvis*w(t-h),
    ||(Qvis^(1/2)ybar,R^(1/2)vbar)||_L2
                         <=g||w||_L2.                  (7)

Common-law causality survives averaging by coupling identical deterministic input prefixes with the same Brownian path/seed. This is ONE deterministic causal map across inputs, not a per-input clairvoyant control selector. It may use mean histories and is NOT presented as an implementation. On infinity the argument is applied on finite prefixes and increasing output norms, without assuming uniform integrability at an infinite terminal time.

Thus the deterministic finite/infinite CONVERSE lemmas of the named v4 source apply on the visible quotient, even if the ORIGINAL plant fails global NEO. This is the new necessity bridge beyond full-state noise cancellation.

## 4. Exact finite-horizon criterion and explicit printed lift

For r>=1 define

    Gvis=Bvis R^(-1)Bvis^T,
    H0vis=[[Avis,-Gvis],[-Qvis,-Avis^T]],
    Hgvis=H0vis+[[0,gamma^(-2)Cvis*Cvis^T],[0,0]],
    Hhvis=exp(-hH0vis)Hgvis exp(hH0vis),
    L=T-h.

Let

    [X;Y](t)=exp((t-T)H0vis)[I;0],              L<=t<=T,
    [X;Y](t)=exp((t-L)Hhvis)exp(-hH0vis)[I;0], 0<=t<=L. (8)

The finite criterion at the SAME prescribed gamma is

    det X(t)!=0 for EVERY t in the CLOSED[0,T].          (QHAM)

When it holds let Pvis=Y X^(-1), and use Phi_vis(t,s)=exp((t-s)H0vis) to define

    Kvis(t,s)=[Pvis(t),-I]Phi_vis(t,s)[Cvis;0],
    gvis(t)=integral_max(0,t-h)^min(t,L)
                          Kvis(t,a+h)w(a)da.

The ORIGINAL actual controller is

    u(t)=K0*x(t)-R^(-1)Bvis^T(Pvis(t)pi*x(t)+gvis(t)).    (9)

It uses ONLY original current state, deterministic time and current[t-h,t] input. It does not estimate hidden states or simulate an extra controller memory. The zero extension after L adds no terminal-preview energy.

**Finite theorem.** On R>0/QMATCH/QORTH, for every finite T>h>=0 and gamma>0, QHAM is equivalent to literal G1<gamma synthesis in the ORIGINAL plant over all printed laws, and even over consistent causal nonlinear history laws. The full-state hidden diffusion need not vanish, and no finite-horizon internal-stability claim is attached.

**Necessity.** A feasible law gives(7) with some g<gamma. The exact deterministic all-causal converse/Hamiltonian equivalence in frozen v4, with the visible matrices substituted, gives QHAM. No original full-state expectation, policy linearization or quotient mean-map realization is assumed.

**Sufficiency and lift.** Under(9), transformed v is the quotient deterministic optimal-window feedback. Its actual visible diffusion is

    B0vis*v=-pi*B0*R^(-1)*Bvis^T(Pvis*y+gvis)=0

by QORTH. Hence y follows EXACTLY the deterministic preview ODE path by path, while the hidden q may remain stochastic. Equation(4) identifies the actual performance with the quotient deterministic performance. V4's exact squares and finite Volterra inverse give ONE strict constant below gamma for all L2 sample inputs, so taking expectation preserves literal N1 on both sides.

The lifted FULL state equation is a linear SDE with bounded deterministic state coefficients and adapted L2 forcing from w and gvis. Standard finite-time linear-SDE localization/isometry/Gronwall gives strong existence, uniqueness and finite expected state/control energy on every compact interval for the frozen disturbance class. Thus the law is genuinely admissible for the original plant, not just a formal projected implementation. Event locality and zero response are preserved. Hidden coordinates do not feed y through Abar, and the performance/control formula uses only y outside the allowed baseline K0x, so uncancelled hidden randomness cannot spoil the pathwise bound.

If r=0, Q=0 and Dtilde=0. There is no visible graph condition: u=K0x gives z=0 exactly and a finite-time linear SDE, so every gamma>0 is feasible. This explicit degenerate case is not represented by an undefined zero-dimensional optimization.

## 5. Infinite horizon: hidden internal stability is an EXPLICIT domain condition

Finite visible performance does NOT imply hidden or full-state stability. To state an exact infinite theorem, add the following actual-data assumptions for dimU>0:

    (Avis,Bvis) stabilizable,                            (VSTAB)
    AU=Z^T Abar Z, SU=Z^T S Z,
    exists H=H^T>0:
       AU^TH+H AU+SU^TH SU<0.                           (HID)

Detectability of the visible pair is automatic by maximality of U. HID is a finite-dimensional Lyapunov LMI for the PASSIVE hidden subsystem after baseline K0. It is NOT claimed necessary for original synthesis outside this theorem's domain: other controls might stabilize hidden states at a different cost, and that case is unclosed. If dimU=0, HID is vacuous and the result reduces to v4. For r=0, omit VSTAB and the quotient ARE; HID alone makes u=K0x internally MS stable with zero output at every gamma.

For r>=1 take Evis,Fvis as the first block column of exp(-hH0vis). The exact quotient algebraic test is

    exists rho>gamma^(-2), Pvis=Pvis^T>=0,
    kvis=(Pvis*Evis-Fvis)Cvis,
    Avis^TPvis+Pvis*Avis+Qvis
        -Pvis*Gvis*Pvis+rho*kvis*kvis^T=0.               (QARE)

This is finite-dimensional Riccati-type feasibility with one strict scalar inequality at the requested gamma. It is not claimed convex, a universal stochastic LMI or a fixed-factor change of level. Put eta=rho^(-1/2)<gamma.

The stationary original printed controller is

    Khvis(tau)=[Pvis,-I]exp(-tau H0vis)[Cvis;0],
    gvis(t)=integral_0^h Khvis(tau)w(t-h+tau)dtau,
    u(t)=K0*x(t)-R^(-1)Bvis^T(Pvis*pi*x(t)+gvis(t)).       (10)

**Infinite theorem.** On R>0/QMATCH/QORTH/VSTAB/HID, QARE is equivalent to literal G1<gamma synthesis WITH internally exponentially mean-square-stable original state, and(10) realizes it with exactly the printed current state/window. Necessity allows every consistent causal nonlinear history law. No inference of hidden stability from quotient stability is used.

### 5.1 Necessity

Equation(7) gives the consistent deterministic mean quotient with strict gain g<gamma on infinity. Apply the OPERATIVE deterministic infinite converse in v4: visible stabilizability supplies a stable homogeneous comparison, uniformly bounding finite preview values at any eta with g<eta<gamma; the fixed-extremal adjoint calculation gives their value monotonicity; the autonomous finite-dimensional flow limit gives QARE. Visible detectability needed by its realization side is guaranteed by §2. This exact named lemma dependency must be reviewed with the complete v4 source, not inferred from an old v3 verdict. The original hidden state never needs an expectation or a reset in this argument.

### 5.2 Visible performance and actual internal cascade

V4's Lyapunov identity for a nonnegative QARE solution and visible detectability make

    Aclvis=Avis-Gvis*Pvis

Hurwitz. Under(10), visible diffusion is ZERO by QORTH. Thus the quotient has v4's stable convolution/transversality proof, giving PATHWISE performance at most eta<gamma. Actual z has exactly that same norm by(4), even while hidden noise persists.

To prove FULL internal mean-square stability, set external w=0 with zero input history, so gvis=0. In the ACTUAL orthogonal coordinates the homogeneous closed loop has

    y'=Aclvis*y,
    dq=(AU*q+G*y)dt+(SU*q+J*y)dW,                       (11)
    G=Z^T Abar*pi^T-Z^TB R^(-1)Bvis^T Pvis,
    J=Z^T S*pi^T-Z^TB0 R^(-1)Bvis^T Pvis.

No q term is hidden in the visible equation, because pi Abar Z=0 and the lifted performance feedback depends on pi*x only. Let WU=-(AU^TH+H AU+SU^TH SU)>0 from HID. Itô gives exactly

    d/dt E(q^THq)
      =-E(q^TWUq)+2E[q^T(HG+SU^THJ)y]+E(y^TJ^THJ y)
      <=-c1 E|q|^2+c2 E|y|^2,                          (12)

for constants c1>0,c2>=0 by the elementary Young inequality. Choose Lvis>0 with `Aclvis^TLvis+Lvis*Aclvis=-I`, which exists by Hurwitz exponential integration. Adding `(c2+1)E(y^TLvis*y)` to the hidden storage makes its derivative at most `-c1 E|q|^2-E|y|^2`. Norm equivalence yields a strict exponential mean-square bound for the FULL original x from every square-integrable initial state. This is an actual cascade proof, not an unproved hidden-stability slogan.

No fourth moments are assumed in taking the quadratic Itô expectation. On every finite interval the constructed linear closed loop has `E sup|q|^2<infinity` and finite expected integrated squared diffusion. Its Lyapunov martingale therefore has expected square-root bracket at most `2||H||(E sup|q|^2)^(1/2)*(E integral|hidden_diffusion|^2)^(1/2)`, which is finite. The same H1 argument makes it true mean-zero. Localization and Fatou then pass the nonnegative storage/energy bounds to infinity. This justifies both the internal estimate and its finite-expected-energy input extension without importing N2 assumptions for the UNKNOWN nonlinear law.

For nonzero admissible input, gvis and y have finite expected L2 energy by the finite-window/stable quotient filters. The hidden drift/diffusion forcings are bounded linear combinations of y,gvis and w(t-h). The SAME Itô/Young estimate adds their squared energies to(12), giving finite expected hidden/state/control energy and global well-posedness. Thus no unpenalized hidden blow-up is concealed in admissibility. Performance remains the pathwise visible bound, so the literal N1 conclusion is unaffected by correlations of w with W.

## 6. A concrete strict extension: global NEO and full MATCH fail

The following EXACT constant matrices illustrate that the new domain is not merely a relabeling of full-state cancellation. It is a WRITTEN algebraic illustration, not an executed finite witness/certificate:

    A=diag(-1,-1), B=[[1,0],[0,0]], C=(1,1)^T,
    A0=[[0,0],[0,1]], B0=[[0,1],[0,0]],
    D0=[[1,0],[0,0],[0,0]],
    D1=[[0,0],[1,0],[0,1]].

Here R=I, K0=0, Q=diag(1,0), U=span(e2), pi=(1,0), Z=e2. Thus

    pi*S=0, Bvis=(1,0), B0vis=(0,1),
    B0vis*R^(-1)*Bvis^T=0.

But S=A0 is NONZERO. For x=e2,u=0 the performance z is0 while the full diffusion is e2, so no matrix Lambda can factor the full diffusion through z: global NEO FAILS. Full MATCH also fails. No control can cancel the hidden q-diffusion since the second row of B0 is zero.

The actual equations are

    dy=(-y+u1+w(t-h))dt+u2 dW,
    dq=(-q+w(t-h))dt+q dW,
    z=(y,u1,u2).

The hidden multiplicative noise remains genuinely present under the lifted controller. Its passive Lyapunov test is `AU=-1,SU=1,H=1`, giving `-2+1=-1<0`. The visible quotient is observable/stabilizable and satisfies QORTH. Thus the finite and infinite quotient criteria/theorems apply for ANY h>=0, with all original admissible disturbances, although the old global-NEO/full-cancellation hypotheses do not. This example calibrates the domain extension only; no numerical optimal gamma, expanded Riccati value, separate endpoint refinement or stronger scientific credit is asserted.

## 7. Exact dependency and assurance ledger

The ONLY nontrivial theorem dependency beyond ordinary finite-dimensional/stochastic facts is the exact deterministic preview machinery in complete frozen v4: finite Hamiltonian/Riccati converse for ALL causal nonlinear controls, actual preview-window completion and strict finite Volterra realization, and the stabilizable/detectable infinite Riccati criterion with uniform-value/transversality proof. Those equations are applied to(Avis,Bvis,Cvis,Qvis,R), not to the original stochastic objective. The NEW projected H1 step justifies that necessary deterministic problem, and the NEW lifted controller/cascade proof closes the ORIGINAL implementation/stability directions on the stated domain.

No old stochastic mean-square N&S, abstract Markovization, unknown controller realization, full-state Jensen with missing moments, general N1=N2 claim, arbitrary extra history/energy state, or inherited no-defect v3 verdict fills a step. The H1 mean-zero argument and accepted declared model conventions are at v3/current-parent support; v4 and this extension still require their ACTUAL union proof review.

Ordinary facts used: finite Gram completion, Cayley–Hamilton/invariant-subspace quotient algebra, the previously displayed H1 local-martingale argument, Bochner/Jensen/Fubini/Gronwall, finite-time linear-SDE well-posedness/moment estimates, Hurwitz Lyapunov integration and Itô/Young cascade estimates. All new actual matrix equalities, quotient closures, lift conditions and hidden Lyapunov directions are written explicitly. No scientific computation, finite matrix routine, sampled ODE/ARE/LMI, program/replay, external-model/human/formal/kernel/novelty gate was performed.

## 8. ENTIRE remaining original problem

The result is a CONSEQUENTIALLY LARGER STRUCTURED CLASS, not unrestricted literal stochastic preview synthesis. Its finite theorem allows hidden noise with no stability restriction but claims attenuation only. Its infinite theorem assumes the PASSIVE hidden HID certificate and visible stabilizability; these are not silently removed or asserted necessary outside the class.

Still OPEN:

- Autonomous noise with a genuinely VISIBLE component after every performance-unobservable invariant reduction, or projected drift/noise actuator directions failing QORTH. The deterministic mean lower test is not generally a sharp stochastic controller criterion there.
- Hidden components failing HID but potentially stabilizable by additional cost-bearing controls, interaction of such stabilization with the prescribed literal gain, and removal of visible stabilizability assumptions.
- Rank-deficient R/unpenalized control directions and original well-posedness/cost issues outside the declared domains.
- A universal same-gamma necessary-and-sufficient finite-dimensional criterion and printed realizer for arbitrary actual constant data, plus its unrestricted infinite-horizon internal-stabilization theorem. No globally optimal stationary/linear policy theorem or full-book solution is claimed.

Full v4+v5 body reading, named-import union reconstruction and parent disposition are REQUIRED before any promotion of these new quotient conclusions; v3 support is not that gate. Older frozen sources stay unchanged. No novelty/priority, configured-family/human/formal/executable acceptance, new GO, continuous18-way runtime or round completion follows. Original October27 cutoff/deadline and v1–v11/HOLD remain binding.
