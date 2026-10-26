# Generic R-positive H1 bootstrap and an exact FORCED-hidden matrix preview criterion

InfoHinfPreview-2 / info-3. Earlier actual `/bin/date` observation before creation: **Sun Oct 25 15:50:10 PDT 2026**. This is an observation bound, not an invented exact completion clock. **ONE complete immutable WRITTEN OWNER-CANDIDATE; NOT independently reviewed/adopted.** The original arbitrary-plant problem remains open outside the exact domains below.

## 0. Genuine changes of representation, dependencies and current gate

This is NOT a refinement of v9's already isolated UNFORCED calibration. Part I proves a full-state finite-time H1 bootstrap for EVERY actual R>0 plant, including genuinely visible autonomous diffusion and QORTH failure: price-coercive controls plus local-time absorption handle the unobserved linear self-noise Sx. NEO/QMATCH are unnecessary for this NECESSARY mean bridge. Part II solves an entire MATRIX class of EXOGENOUSLY FORCED, unstable, performance-hidden states by a finite-dimensional GRAMIAN inequality, using the actual stationary current-window information class and a realized predictor. Here C need not vanish, actual zero-state x need not stay zero, and stabilization has a quantified nonzero gain price.

The forced-hidden theorem does NOT assume that a causal mean-history map can be Markovized. Necessity instead uses the actual printed law after a COMPACT external window clears, with a conditional L1 restart argument. An explicit weak-full-history countercontrol explains exactly why that information step cannot simply be dropped.

Nontrivial ordinary inputs are stated precisely: the elementary nonsharp continuous-martingale H1 maximal implication, finite linear algebra/controllability and Hurwitz semigroup facts, and deterministic-time restart of a strongly well-posed nonexplosive AUTONOMOUS Borel SDE with deterministic coefficients. All NEW applications, constants, moments, operator/Gramian links, controller identities and stability steps are proved below. No v4/v5 QARE theorem, unreviewed v9 synthesis, v6/v7 norm-ordering theorem, or SHARP Geiss–Scheutzow/Lenglart sqrt2 bound is a correctness premise.

After actual v96-A review RETURN, I read the complete39LF parent `preview-generic-norm-bridges-and-Rdef-parent-v1.md`, SHA256 `feb8b52a576161ffc85e670dc147f6f7df0802be5261099e523bc13a66e62860`, recovering raw19/23, and ALL208LF actual v91-A review, SHA256 `cb04b3664c4fa5542dd7ae72c2fa8147384e0bd2830f41174fcfef784b74385c`. Its THREE separate core adoptions do not certify this new source, v9 or a controller-domain union. The optional sharp sqrt2 assertion remains NOT_RECONSTRUCTED/unaccepted; its CLOCK control remains explicitly nonstationary, not book F. The nonsharp H1 argument needed here is reproduced in §2.

Checkpoints17–20 and exposureaddendum7 disclose the earlier reasoning; the proof was genuinely UNWRITTEN when v96 interrupted it and was not fake-frozen for that review. All prior files stay immutable. Everything here is WRITTEN, not scientific-executable/kernel checked, human/configured-family reviewed or novelty/SOTA cleared.

## 1. Actual model and the two distinct theorem scopes

The original constant-data scalar-Brownian plant is

    dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW, z=D0x+D1u.

Inputs have zero negative history and finite EXPECTED squared energy. N1(f)=E||f||_time-L2, not(E||f||^2)^(1/2). Base unknown controls have local PATHWISE L2 and strong nonanticipative well-posedness; no expected-control-L2 condition is smuggled in. Finite output is through T and counted input only through T-h; infinite output/input run to infinity.

Part I applies to ANY consistent admissible causal nonlinear/history law and ANY finite observation horizon, assuming R=D1^TD1>0 and finite output N1 for the tested input. It yields necessary means, NOT a stochastic realizer or full N&S.

Part II is INFINITE-horizon N&S on the explicit actual-data class in §5. Unknown controllers there are deterministic TIME-HOMOGENEOUS functions of the ACTUAL current x and external-input window[t-h,t], with no hidden controller state/permanent external-history flag. This is the stationary printed information class, not an assumed universal stationary optimality theorem. They may otherwise be nonlinear/nondifferentiable, provided the strong-well-posed/restart requirements and uniform zero-window internal EMS hold. Their gain is the declared strict UNIFORM G1<gamma. No finite-time F_t or alternative pointwise-strict endpoint classification is asserted for that theorem.

## 2. Ordinary NONSHARP H1 implication, fully separated from sqrt2

For a continuous vector local martingale M starting0, let V=trace[M], M*=sup_(t<=T)|M_t|. After bounded localization, stop at the first absolute crossing of r. Reaching2r requires an increment of norm at least r. Stop that increment when its added trace bracket reaches r^2/16. Conditional Itô isometry and the weak L2 maximal bound for its squared norm give

    P(M*>2r, sqrt(V_T)<=r/4)<=P(M*>r)/16.

Therefore P(M*>2r)<=P(sqrt(V_T)>r/4)+P(M*>r)/16. Integrating r gives

    (1/2-1/16)E M*<=4 E sqrt(V_T),
    E M*<=64/7 E sqrt(V_T)<10 E sqrt(V_T).              (H1)

Apply this at norm/bracket localizations and use Fatou. If the right side is finite, the original maximal variable is integrable. The stopped martingales converge in L1 at each time, dominated by M*, so their conditional-expectation identities pass to the limit. M is then true/UI mean-zero on[0,T]. For vectors the weak bound uses the nonnegative submartingale |increment|^2 and its trace-bracket isometry; no scalar-only comparison is inserted.

I use the deliberately conservative constant10 below. Earlier exposed notes used the v3 constant8; neither affects the attenuation level, and no sharper probability transfer is needed.

## 3. Generic R>0 finite-time H1 bootstrap WITHOUT NEO/QMATCH/ORTH

Complete the actual output square:

    K0=-R^(-1)D1^TD0, Abar=A+BK0, S=A0+B0K0,
    Q=D0^TD0-D0^TD1R^(-1)D1^TD0>=0,
    nu=R^(1/2)(u-K0x), Bcal=B R^(-1/2), B0cal=B0 R^(-1/2),
    |z|^2=x^TQx+|nu|^2, nu=R^(-1/2)D1^Tz.             (1)

Thus N1(nu)<=N1(z), but there is NO claim E integral|nu|^2 finite. The actual state equation is

    dx=(Abar x+Bcal nu+C f)dt+(Sx+B0cal nu)dW,
    f(t)=w(t-h).                                      (2)

**Lemma.** On ANY finite T, if E|x0|,E||nu||_L2(0,T),E||f||_L2(0,T) are finite, then E sup_(t<=T)|x(t)| is finite and the FULL diffusion has H1 norm finite. No condition on S or Q is required.

Here is an explicit stopped proof. Set a=||Abar||,s=||S|| and choose

    delta=min(1,1/[4(1+a)],1/[1600(1+s)^2]),
    N=ceil(T/delta), t_j=jT/N,
    cnu=||Bcal||sqrt(delta)+10||B0cal||,
    cf=||C||sqrt(delta).

Then a delta+10s sqrt(delta)<=1/2. Stop at tau_n when |x| reaches n or integral|nu|^2 reaches n, also at T; if |x0|>n take tau_n=0. The martingale integrands before these stops have finite bounded-localized bracket, so(H1) applies WITHOUT first assuming the desired state moment.

For one block I_j=[t_j,t_(j+1)], let

    U_jn=E sup_(t in I_j)|x(t wedge tau_n)|,
    M_jn=E sup_(0<=t<=t_j)|x(t wedge tau_n)|.

The stopped integral equation, Cauchy–Schwarz for the two drift inputs, and(H1) for the martingale INCREMENT give

    U_jn<=E|x(t_j wedge tau_n)|
       +(a delta+10s sqrt(delta))U_jn
       +cnu E||nu||_L2(I_j)+cf E||f||_L2(I_j).

Indeed the self-noise bracket root is bounded by s sqrt(delta) times that block supremum, and the control-noise bracket root by ||B0cal||||nu||_L2(I_j). Hence

    U_jn<=2M_jn+2 input_j,
    M_(j+1),n<=M_jn+U_jn<=3M_jn+2 input_j,
    input_j=cnu E||nu||_L2(I_j)+cf E||f||_L2(I_j).

Iteration and the PATHWISE block inequality sum_j||v||_L2(I_j)<=sqrt(N)||v||_L2(0,T) give the finite bound

    M_Nn<=3^N[E|x0|+2sqrt(N)(cnu N1_T(nu)+cf N1_T(f))]. (3)

It is uniform in the localization level n. Continuity/nonexplosion and pathwise-local control L2 give tau_n increasing to T; Fatou proves(3) for the original supremum. No horizon-uniform version of this possibly large constant is claimed.

Now

    E(integral_0^T|Sx+B0cal nu|^2)^(1/2)
       <=s sqrt(T) E sup|x|+||B0cal||N1_T(nu)<infinity.

The FULL diffusion integral is true/UI mean-zero by(H1). Also N1_T(u)<infinity follows from u=K0x+R^(-1/2)nu and(3). This is finite-time N1, not expected squared control energy. All expectations of the drift may be interchanged by Fubini.

## 4. Consequence: SAME-level full mean necessity on EVERY R-positive plant

Take ANY original feasible law and deterministic counted input. Equations(1)–(3) apply with x0=0 and N1(nu)<=N1(z). The actual full mean obeys

    xbar'=Abar xbar+Bcal nubar+Cw(t-h),
    ||(Q^(1/2)xbar,nubar)||_L2<=N1(z).                  (4)

The final inequality is Bochner Jensen on the Hilbert random variable whose path norm equals||z|| by(1). There is no squaring of the random denominator: for deterministic w, N1(w)=||w||_L2. Finite-time drift integrability proved above identifies its mean with the actual xbar.

Couple deterministic inputs with identical prefixes using the same Brownian path and fixed law; strong causality preserves their response prefixes, and averaging preserves this consistency. Thus(4) is ONE deterministic causal mean-history map across inputs, at the SAME gain level, without NEO/QMATCH/ORTH or Q>0. Infinite-time application uses finite prefixes and increasing output norms; NO true/UI infinite-terminal diffusion or uniform-in-T maximal-state bound is assumed.

Any valid deterministic preview necessary test may therefore be applied to the full R-positive data, even with visible autonomous state noise. Such a mean map may still use inadmissible remote history, and its deterministic optimal policy usually leaves nonzero actual diffusion. Equation(4) is NOT the missing generic sufficiency/realization theorem. The R0 example in v8 is not a counterexample: it supplies no priced N1(nu), and R^(-1/2) in(1) is unavailable there.

## 5. A genuinely FORCED unstable-hidden MATRIX class

Now take the ACTUAL infinite plant

    dx=(A x+B u+Cw(t-h))dt+B0u dW, z=D1u,             (5)

with all these entire-domain assumptions:

1. R=D1^TD1>0; D0=A0=0. State cost Q is IDENTICALLY ZERO, not secretly positive definite.
2. EVERY eigenvalue of real A has POSITIVE real part (A is anti-Hurwitz); Jordan blocks/complex pairs are allowed.
3. (A,B) is controllable. This is an explicit plant premise, not inferred from arbitrary nonlinear stochastic stabilizability.
4. B0 R^(-1)B^T=0. B0 may be nonzero; unknown controllers may use its actual stochastic channel.
5. h is ANY fixed finite nonnegative real. C is arbitrary, and can genuinely FORCE the whole unstable hidden state.

The unknown-law information/admissibility/EMS class is exactly §1's deterministic stationary current-state/current-external-window class, with no extra controller state. Internal EMS means for the zero input/window and ALL deterministic initial states xi,

    E_xi|X_s|^2<=M exp(-lambda s)|xi|^2,

for some common M,lambda>0. Strong well-posedness/nonexplosion is required for these original laws and inputs. These are NOT v9's exogenously unforced blocks: C need not be0. Neither v5's passive HID nor v4's detectability is silently assumed; Q=0,A unstable makes both fail.

Whiten Bcal=B R^(-1/2),D=Bcal Bcal^T. Define the unique finite matrices

    G_B=integral_0^infinity e^(-At)D e^(-A^Tt)dt,
    G_C=integral_0^infinity e^(-At)CC^T e^(-A^Tt)dt,
    E_h=e^(-Ah), H_h=E_h G_C E_h^T.                    (6)

They solve LINEAR Lyapunov equations

    A G_B+G_B A^T=D, A G_C+G_C A^T=CC^T.

Convergence/uniqueness follow because -A is Hurwitz. G_C>=0. If v^TG_Bv=0 then Bcal^Te^(-A^Tt)v=0 for all t; its derivatives give Bcal^T(A^T)^jv=0, and controllability gives v=0. Thus G_B>0. Also H_h is the tail Gramian integral_h^infinity e^(-At)CC^Te^(-A^Tt)dt; it decreases in h without a normal/diagonal A assumption.

**Theorem (exact forced-hidden current-window criterion).** On this ENTIRE class, strict UNIFORM literal G1<gamma synthesis WITH full-state internal EMS is equivalent to the finite-dimensional matrix inequality

    gamma^2 G_B-H_h>0.                                 (FH)

The Lyapunov equations plus(FH) are LMI-type conditions at the given actual matrices; no stochastic norm replacement occurs. The necessity covers ALL admissible nonlinear stationary printed laws, not just linear ones. The sufficiency below gives the ACTUAL printed law. This is not an unrestricted-plant theorem or a theorem for arbitrarily enlarged controller-memory classes.

## 6. The crucial conditional L1 restart, not a hidden N2-state assumption

The ordinary deterministic-time restart fact used here is precise: after the external current window is identically zero, a deterministic stationary current-state law gives an AUTONOMOUS Borel SDE. Strong existence/pathwise uniqueness/nonexplosion identify its conditional future law, given the current state xi, with the zero-input transition law started from that deterministic xi and fresh Brownian increments. This is the standard strongly well-posed autonomous-SDE restart, NOT a Markovization of an arbitrary history law.

By the stated internal EMS and conditional Cauchy–Schwarz, its deterministic-state first-moment kernel obeys

    E_xi|X_s|<=sqrt(M)exp(-lambda s/2)|xi|.             (7)

Consequently(7) integrates for an arbitrary PAST-MEASURABLE L1 initial state, EVEN when its second moment is infinite. This follows by integrating the transition-kernel inequality, not by pretending that state belongs to L2.

For a compact deterministic disturbance w, choose t0 strictly AFTER its support plus h, so the ACTUAL current window and delayed forcing are zero forever afterward. Part I gives E|x(t0)|<infinity from finite output N1. Conditional restart and(7) therefore give

    E|x(t0+s)|<=sqrt(M)exp(-lambda s/2)E|x(t0)| ->0.   (8)

No expected control-L2, forced-state L2 or hidden-controller-memory reset was assumed to reach this actual terminal mean condition.

## 7. Full all-printed-law necessity: pole moment to finite Gramian inequality

Let an unknown original printed law for(5) have G1<=g<gamma. For any compact deterministic input, nu=R^(1/2)u has N1 equal to N1(z), and its Bochner mean nubar lies in L2 with norm<=g||w||_L2. Part I makes the full finite-time diffusion true mean-zero, so

    m'=A m+Bcal nubar+Cw(t-h), m(0)=0.

Multiply by e^(-At), integrate to T, then let T increase. Condition(8) makes e^(-AT)m(T) vanish. The control integral converges by Cauchy–Schwarz against the L2 exponential kernel. The forcing shift gives EXACTLY

    mathcalB(nubar)=-mathcalC_h(w),
    mathcalB(v)=integral_0^infinity e^(-At)Bcal v(t)dt,
    mathcalC_h(w)=E_h integral_0^infinity e^(-At)Cw(t)dt. (9)

No infinite-terminal expectation of the stochastic integral was taken: means were justified on each finite prefix, and only deterministic integrals were passed to the limit.

For ANY vector y, (9) and the gain bound give

    |<mathcalC_h^*y,w>|<=||mathcalB^*y||_L2*g||w||_L2.

Compact deterministic inputs are dense in L2, so

    ||mathcalC_h^*y||_L2<=g||mathcalB^*y||_L2,
    y^T H_h y<=g^2 y^T G_B y.

These adjoint norms are exactly the Gramians(6). This argument needs NO linearity/differentiability of the unknown mean-control map; the support-functional estimate holds input by input. Since G_B>0 and g<gamma,

    gamma^2 G_B-H_h >=(gamma^2-g^2)G_B>0,

which proves necessity of(FH). Enlarging to permanent-history laws would lose(8); §11 gives the exact boundary.

## 8. Actual current-window controller from(FH), with full proof

Choose rho>gamma^(-2) sufficiently close to gamma^(-2) that

    X=G_B-rho H_h>0, P=X^(-1)>0.                       (10)

This is possible by strict positivity in(FH); if H_h=0 any larger rho works. Because A commutes with E_h, the Lyapunov equations give

    AX+XA^T=D-rho E_h CC^T E_h^T,
    A^TP+PA-PDP+rho P E_h CC^T E_h^T P=0.              (11)

Define the known-current-window functional

    p(t)=integral_0^h e^(-A tau)Cw(t-h+tau)dtau,
    chi(t)=x(t)+p(t),
    u(t)=-R^(-1)B^TP chi(t).                           (12)

Here chi is an ALGEBRAIC abbreviation computed from current x and the permitted window, NOT an extra stored controller state. For L2 input sample paths, p is locally absolutely continuous and

    p'=A p+E_h Cw(t)-Cw(t-h).

The ACTUAL original diffusion is B0u=-B0R^(-1)B^TPchi=0 by the stated ORTH. Thus actual chi obeys

    chi'=(A-DP)chi+E_h Cw, nu=-Bcal^TPchi.              (13)

This verifies the original plant, not a conditional-future-state model. For zero initial state/history, chi(0)=0. All functions in(12) use ONLY current state and[t-h,t]; there is no permanent history, energy accumulator, reset, future noise or auxiliary controller state.

First prove Acl=A-DP Hurwitz WITHOUT detectability. From(11),

    Acl X+X Acl^T=-D-rho E_h CC^T E_h^T<=0.

Since X>0, every Acl eigenvalue has nonpositive real part. If Acl^T v=i omega v, the displayed identity forces Bcal^Tv=0 (and C^TE_h^Tv=0), hence A^Tv=Acl^Tv=i omega v. This contradicts A anti-Hurwitz. Therefore no imaginary-axis eigenvalue exists and Acl is Hurwitz.

Now take POSITIVE actual storage V=chi^TPchi. Direct differentiation using(11)–(13), with r=C^TE_h^TPchi and eta=rho^(-1/2), gives

    Vdot+|z|^2-eta^2|w|^2
                     =-eta^2|w-rho r|^2.              (14)

Indeed |z|^2=|nu|^2=chi^TPDPchi, the remaining state coefficient is-rho|r|^2 and the cross term is2r^Tw. Integrate from0 to any S: V(S)>=0, so integral_0^S|z|^2<=eta^2 integral_0^S|w|^2. Monotone limits give the PATHWISE infinite inequality, and expectation of the ordinary norms gives

    N1(z)<=eta N1(w), eta<gamma.

No comparison of random N1 denominators with RMS denominators is involved.

For nonzero admissible input, the finite-window kernel maps pathwise/expected L2 input to L2 p, and Hurwitz(13) maps it to L2 chi,nu. Hence x=chi-p and u also have finite expected squared energy. The realized law is strongly nonanticipative/global; its actual diffusion vanishes and its remaining linear integral equation has a unique solution. Thus even stronger all-input state/control-energy admissibility is satisfied by the construction.

For arbitrary square-integrable initial state and w=0/window0, p=0, x=chi and x'=Acl x. Ordinary Hurwitz exponential bounds give full internal exponential mean-square stability from EVERY initial state. This is not inferred from zero-state output attenuation. Equations(10)–(14) complete the N&S theorem.

## 9. Why an unstabilized QARE would be wrong OUTSIDE the old domain

In this class Q=0, the preview Hamiltonian has first block column[E_h;0]. Thus its algebraic equation is exactly(11), and P=0 solves that equation at EVERY rho/level. It would falsely certify every gamma if one simply deleted old v4's detectability/stability boundary and retained P>=0 alone.

The NEW stabilizing branch is P>0, with inverse X in(10); uniqueness of the linear Lyapunov equation identifies it precisely with G_B-rho H_h. Its actual stability is proved above. This is NOT a counterexample to v4/v5, whose added detectability/passive-HID hypotheses exclude these unstable-hidden data. It is an exact calibration of the genuine missing stabilization step, now closed on this forced class.

## 10. Explicit multi-parameter scalar realization for every positive preview

Take ANY positive rational a,b,c,sigma, ANY finite h>=0, with

    dx=(a*x+b*u1+c*w(t-h))dt+sigma*u2 dW,
    z=(u1,u2), R=I2.

All actual constant matrices are rational, B=(b,0),B0=(0,sigma), so ORTH holds, but every state is hidden/unstable and C=c genuinely forces it. G_B=b^2/(2a),G_C=c^2/(2a),E_h=e^(-ah). Hence the EXACT strict-uniform criterion is

    gamma>(c/b)e^(-ah).                                (15)

This is all positive parameters/ALL finite preview, not selected matrix values. An especially explicit norm-attaining stationary law is obtained with

    p(t)=c integral_0^h e^(-a tau)w(t-h+tau)dtau,
    k>a/b,
    u1=-k(x+p)-(c/b)e^(-ah)w(t), u2=0.                 (16)

The actual chi=x+p satisfies chi'=(a-bk)chi. With zero initial data chi=0, so x=-p is generally NONZERO and u1=-(c/b)e^(-ah)w(t). Its literal induced gain is EXACTLY(c/b)e^(-ah); internal EMS at zero input has rate2(bk-a). The law uses only current state/current window/current endpoint. It does not eliminate a forced state's price by declaring that state zero, as the unforced v9 construction did. Actual control-noise channels remain available to all unknown policies, but the lower bound proves they cannot improve this class's criterion.

Equation(15) is under the frozen strict-UNIFORM convention. I do NOT promote a pointwise-every-input strict endpoint theorem for arbitrary nonlinear policies here; law(16) itself has ratio equal to its gain for every nonzero input. No scalar or matrix bound in this section was evaluated by an interpreter.

## 11. Exact information-class countercontrol: why full histories change the problem

This is ONLY a boundary control, NOT an admissible printed realization. Consider a WEAK enlarged class allowing permanent input memory, imposing only local strong well-posedness and zero-INPUT-HISTORY internal EMS, without all-input state-energy or arbitrary-controller-memory-state stability. Let P0=G_B^(-1); the preceding Lyapunov stability proof at rho0 makes K=R^(-1)B^TP0 a noise-erasing stabilizer. Define the permanent flag

    I_t=1_(integral_0^t|w(s)|^2ds>0),
    u(t)=-(1-I_t)K x(t).

At w=0 the flag is always0, so EVERY plant initial state decays exponentially. At zero plant initial state, before the first nonzero input the state/control are0; once input energy becomes positive the flag stays1, so u=0 forever. Hence zero-state output is0 for EVERY input and G1=0, while forced hidden state may grow without bound after a compact input. Coefficients are a switched linear ODE, the ORTH diffusion is0, and there is no finite-time explosion.

This policy is NOT F(current x,current window): after the window clears it remembers whether an input ever occurred. Its input-energy memory cannot be silently inserted into the book law. If all-input state-energy admissibility or internal stability for arbitrary controller-memory initial states is ADDED, the flag is excluded on those grounds as well. It is NOT a counterexample to the original theorem( FH ).

It proves why enlarging the necessity argument to unconstrained remote-history maps with only that weak zero-history stability would invalidate terminal decay(8) and yield the wrong answer. Part I's finite-time mean equation still holds for it; what fails is exactly the required current-window stabilization/realization interface. No Markovization or memory-erasing theorem was assumed in Part II.

## 12. First genuinely unproved extension and entire original residual

For generic autonomous diffusion Sx, the same predictor change produces S(chi-p), hence a known-window Brownian forcing -S*p. With nonorthogonal control noise, B0R^(-1)B^TPchi need not vanish either. The deterministic Gramian/storage construction above no longer realizes the literal N1 bound at the requested gamma. This is the actual next representation gap, not an omitted computation or another closed-unforced-family refinement.

Part I removes NEO/QMATCH only for NECESSARY full means when R>0. It does not remove those stochastic realization obstacles, prove N1=RMS, finite-horizon norm ordering, full nonlinear optimality, or a universal stabilizing criterion. Rank-deficient R still permits unpriced-control H1 failure as in v8. Mixed stable/unstable state spaces, nonzero Q/D0, arbitrary autonomous diffusion/control-noise coupling, broader controller classes, and original finite-book syntax/pointwise-endpoint interpretations remain outside this NEW N&S theorem unless separately proved. No general theorem that every feasible law is globally Lipschitz or linearly stabilizing is asserted.

This new source needs OWN complete source-pinned written reconstruction/parent disposition before promotion. The v91 three-core verdicts, earlier v4/v5 support and v9 candidate do NOT cover it. It is not a solution of the unrestricted book problem, a novelty/priority claim or a configured-family/human/formal/kernel/executable gate. No scientific interpreter/eval/program/CAS/enumeration/Gramian/Riccati/LMI solver/simulation/replay/CLI/nested agent/build/tests/formatter or GO was used; all identities are HAND-WRITTEN. Every earlier process major/clock/exposure qualification and v9/v10/v11/HOLD remains; original October27 cutoff/deadline and eighteen-owner identities are unchanged. No round completion or indefinite park is declared.
