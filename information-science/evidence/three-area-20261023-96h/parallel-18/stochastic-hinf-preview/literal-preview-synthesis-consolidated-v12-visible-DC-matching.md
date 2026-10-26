# Exact SAME-gamma literal preview synthesis with VISIBLE multiplicative noise and forcing-direction matching

Owner InfoHinfPreview-2 / info-3. Earlier actual `/bin/date` observation before creation: **Sun Oct 25 17:41:16 PDT 2026**. Observation bound, not an invented completion time. **ONE complete WRITTEN OWNER-CANDIDATE, requiring its OWN full fresh gate.** This is an explicit matrix CLASS theorem, not the unrestricted book problem or an accepted union with earlier sources.

## 0. Genuine new frontier and exact model convention

This source treats FORCED and FULLY PERFORMANCE-VISIBLE states, with arbitrary autonomous multiplicative noise S. It also permits GLOBAL QORTH FAILURE: only the minimum-price disturbance-cancellation direction must avoid injecting noise, and a supplied finite-dimensional MS stabilizer handles the homogeneous state. This is not v9's unforced hidden block, nor v10's A0=0/unstable-hidden class, nor merely a refinement of their scalar parameters.

The new necessity representation is a SAME-level DC obstruction from the ACTUAL full mean, combined with a Sobolev trace estimate for long flat inputs. It applies even to arbitrary causal nonlinear/history unknown laws. A finite algebraic DC-matching identity makes this obstruction sharp; a static original-state/known-input-endpoint law realizes it pathwise. No mean-square theorem, norm rescaling, Markovization or universal linear-optimality premise supplies a direction.

The original printed control is F(current x,w(s):t-h<=s<=t), so the delayed endpoint w(t-h) is genuinely allowed. The complete17LF model TEXT boundary was renewed AFTER actual v100-K review RETURN; no new image-pixel reading is claimed. The theorem is INFINITE-horizon, any finite h>=0, under the already DECLARED strict UNIFORM G1<gamma research interpretation. It does not insert an unprinted supremum/time argument into the book, claim a finite-horizon version, or classify the alternative pointwise-every-input strict endpoint.

Current v6/v7/v8 support remains THREE distinct cores; v9/v10/v11 remain at their separate gates. None is a synthesis correctness premise here. Ordinary nonsharp H1 martingale, Bochner/Jensen/Fubini, elementary Sobolev/Cauchy, finite Gram/Schur algebra and linear-SDE/Itô facts are the only named standard inputs; their NEW applications are supplied. All writing is exact symbolic/integer/rational, NOT scientific executable/kernel checked, novelty-cleared or configured-family/human/formal accepted.

## 1. Actual data, coercive output and information class

Use the original constant-data scalar-Brownian plant on INFINITY,

    dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW,
    z=D0x+D1u.

Gain uses zero initial state/negative input history and ALL progressive w with finite EXPECTED squared energy. N1(f)=E||f||_time-L2, not(E||f||^2)^(1/2). Unknown laws are fixed, strongly well-posed nonanticipative laws with local PATHWISE control L2. Expected squared control energy is NOT assumed for unknown policies. The necessary bound below allows even full causal histories; the realizing law will be static in the actual printed arguments.

Assume the ACTUAL output conditions

    R=D1^TD1>0,
    K0=-R^(-1)D1^TD0,
    Q=D0^TD0-D0^TD1R^(-1)D1^TD0>0.

Put

    Abar=A+BK0, S=A0+B0K0,
    Bcal=B R^(-1/2), B0cal=B0 R^(-1/2),
    nu=R^(1/2)(u-K0x), D=Bcal Bcal^T=B R^(-1)B^T.

The exact output square is

    |z|^2=x^TQx+|nu|^2,                               (1)

and actual dynamics become

    dx=(Abar x+Bcal nu+Cw(t-h))dt+(Sx+B0cal nu)dW.     (2)

No condition S=0 is imposed. All states are instantaneously performance-visible because Q>0; no hidden-state quotient can silently remove the noise.

## 2. A GENERAL full-coercive same-level DC necessary inequality

This section requires only R,Q>0, not full actuation, any matching condition or a supplied stability certificate. Let

    G_DC=D+Abar Q^(-1)Abar^T>=0.

**Lemma.** If an arbitrary original causal law has finite uniform literal gain<=g, then

    CC^T<=g^2 G_DC.                                    (DC)

This remains necessary regardless of A0,B0. It is not a stochastic sufficiency test in general.

### 2.1 Full mean is legitimate WITHOUT expected-control-L2

For a deterministic finite-energy test input, (1) gives

    E||x||_L2<=lambda_min(Q)^(-1/2)N1(z),
    E||nu||_L2<=N1(z).

Thus the FULL actual diffusion Sx+B0cal nu has finite expected bracket root. The ordinary H1 maximal implication makes its local martingale true/UI mean-zero on every finite prefix. One elementary nonsharp proof stops a vector martingale at its first norm crossing r and its added trace bracket r^2/16: conditional isometry/weak L2 control gives P(M*>2r,sqrt(V)<=r/4)<=P(M*>r)/16. Tail integration gives E M*<=64/7 E sqrt(V)<10 E sqrt(V); localization/Fatou/dominated stopping remove the bounds. No sharp sqrt2 probability theorem is needed.

All finite drift expectations are integrable by the displayed H1 state/control norms. Hence the ACTUAL mean m and nubar satisfy

    m'=Abar m+Bcal nubar+Cw(t-h), m(0)=0,
    ||(Q^(1/2)m,nubar)||_L2<=N1(z)<=g||w||_L2.         (3)

The last inequality is Bochner Jensen on the exact Hilbert norm in(1), for deterministic w. It does not square a random N1 denominator. It also does not present the mean map as a printed controller.

### 2.2 Long flat inputs, boundary control and the matrix inequality

Fix a real input vector v and test w_L=v*1_[0,L]. Its ordinary norm is sqrt(L)|v|, so (3) bounds both weighted mean state and mean control by g sqrt(L)|v|. With qmin=lambda_min(Q)>0,

    ||m||_2<=qmin^(-1/2)g sqrt(L)|v|,
    ||m'||_2<=[||Abar||qmin^(-1/2)g+||Bcal||g+||C||]
                                                    *sqrt(L)|v|.

Since m is locally absolutely continuous, m0=0 and m,m' belong to L2,

    |m(t)|^2=2 integral_0^t m^T m'<=2||m||_2||m'||_2.

Therefore sup_t|m(t)|<=K_g sqrt(L)|v| for a finite constant independent of L and the particular policy's regularity. This is an ACTUAL state-boundary estimate, not a terminal-state/reset assumption.

Integrate the mean equation over[h,h+L]. For any state dual vector y,

    |y^TCv|L<=2|y|K_g sqrt(L)|v|
        +|integral_(h)^(h+L)(y^TAbar m+y^TBcal nubar)|.

Cauchy–Schwarz in the ACTUAL output coordinates gives

    |integral(y^TAbar m+y^TBcal nubar)|
      <=sqrt(L)*sqrt(y^T G_DC y)*||(Q^(1/2)m,nubar)||_2
      <=g sqrt(y^T G_DC y)*L|v|.

Divide by L and let L increase. Every test input has finite expected squared energy; no infinite-energy disturbance was inserted. The two boundary terms vanish, giving |y^TCv|<=g sqrt(y^TG_DC y)|v| for all y,v, equivalent to(DC). No stationarity, differentiability, linearity or internal mean-stability assumption on the UNKNOWN law was used.

For example if Abar=0, (DC) forces range(C) subset range(B); an unmatched disturbance integrator with Q,R>0 cannot have finite literal gain, even using arbitrary control-noise channels. This is a genuine necessary obstruction, not a complete non-full-actuation theorem.

## 3. The entire exact matched data class

Now assume additionally FULL drift actuation

    D=B R^(-1)B^T>0,

and these TWO actual-data identities:

    Abar^T D^(-1)C=0,                                  (DC-MATCH)
    B0 R^(-1)B^T D^(-1)C=0.                            (FORCE-NOISE)

DC-MATCH does NOT require Abar=0. FORCE-NOISE does NOT require global B0R^(-1)B^T=0. Neither requires S=0. They concern the ACTUAL forcing directions and the minimum-price drift compensation, not performance-hidden states or a changed plant.

The enlarged theorem's PLANT DOMAIN includes an EXPLICIT linear homogeneous MS stabilizer certificate: there are K,H=H^T>0 with

    Ac=Abar+Bcal K, Nc=S+B0cal K,
    Ac^TH+HAc+Nc^THNc<0.                               (MS)

This is not asserted necessary for arbitrary nonlinear stochastic stabilization outside this certified domain. It is exactly finite-LMI type: with X=H^(-1)>0,Y=KX,

    [[Abar X+Bcal Y+X Abar^T+Y^TBcal^T,
                                      (S X+B0cal Y)^T],
     [S X+B0cal Y,                              -X]]<0. (MS-LMI)

Schur complement and congruence by H give(MS), and conversely X=H^-1,Y=KX gives this LMI. No solver or numerical certificate is being claimed.

There is an important CLEAN subclass with NO extra stabilizer-existence premise: if GLOBAL ORTH B0R^(-1)B^T=0 holds, let Frob2=trace(S^TS), k=1+Frob2 and

    K=-Bcal^T D^(-1)(Abar+kI), H=I.

Then Ac=-kI,Nc=S and the Lyapunov left side is-2kI+S^TS<=-(2+Frob2)I<0. Thus full ORTH automatically supplies(MS) for ANY Abar and ANY visible S. The relaxed FORCE-NOISE/(MS) class genuinely allows global QORTH failure, as §7 shows.

## 4. Exact finite-dimensional SAME-gamma N&S theorem

**Theorem.** On the ENTIRE certified class in §3, for any gamma>0 and ANY finite h>=0, original literal strict UNIFORM G1<gamma synthesis WITH full-state internal exponential mean-square stability is equivalent to

    gamma^2 D-CC^T>0.                                  (GAMMA)

Equivalently the finite block matrix[[gamma^2D,C],[C^T,I]] is positive definite. In the GLOBAL-ORTH subclass with DC-MATCH,R,Q,D>0, (GAMMA) is the ONLY additional feasibility test; the stabilizer is explicitly supplied above. In the larger FORCE-NOISE class, MS-LMI is a DOMAIN premise, not a secretly necessary nonlinear-stabilization condition.

Define

    kappa=||D^(-1/2)C||_op.

The constructed stationary original law has EXACT induced literal gain kappa. Thus(GAMMA) is simply gamma>kappa, expressed as a finite-dimensional matrix condition without calculating a norm or changing attenuation level. This is an exact class theorem, not a universally sharp stochastic LMI.

### 4.1 All-causal necessity, not a mean-square substitute

By §2, any feasible arbitrary causal/history law with gain g<gamma satisfies CC^T<=g^2G_DC. Since D>0, G_DC>0. DC-MATCH gives the EXACT identity

    G_DC D^(-1)C
      =C+Abar Q^(-1)(Abar^T D^(-1)C)=C,
    G_DC^(-1)C=D^(-1)C.

Consequently

    ||G_DC^(-1/2)C||_op^2
       =lambda_max(C^TG_DC^(-1)C)
       =lambda_max(C^TD^(-1)C)=kappa^2.

The necessary matrix bound therefore implies g>=kappa. With g<gamma, (GAMMA) follows by the ordinary Schur/singular-value equivalence. This proves necessity against a LARGER class than the printed stationary laws; no regularity or linear-optimality theorem was assumed. It does not depend on the certificate or FORCE-NOISE, which are used for the actual construction.

### 4.2 Actual printed realizer and PATHWISE literal performance

Take any K,H from(MS), and set the minimum-price forcing map

    Lw=Bcal^T D^(-1)C.

Use the ACTUAL stationary law

    nu(t)=Kx(t)-Lw*w(t-h),
    u(t)=K0x(t)+R^(-1/2)[Kx(t)-Lw*w(t-h)].             (4)

It uses only current x and the allowed LEFT endpoint of the current preview window. No enlarged controller state, input-energy variable, remote past, physical reset, future noise or explicit clock is inserted.

The two cancellations are exact:

    Bcal Lw=C,
    B0cal Lw=B0R^(-1)B^TD^(-1)C=0.

Thus the ORIGINAL state equation is the HOMOGENEOUS linear SDE

    dx=Ac x dt+Nc x dW,                                (5)

independent of the external input, even when w is correlated/adapted to W. This is a substitution into the actual plant, not a projected or averaged realization.

For zero initial state, strong uniqueness gives x=0 for EVERY input. Unlike an unforced hidden example, here C is allowed nonzero and all states are priced; a fully PRICED feedforward control cancels the forcing at its exact cost. The actual output is

    z(t)=-D1 R^(-1/2)Lw*w(t-h).

Its matrix squared Gram is

    Lw^T R^(-1/2)D1^TD1R^(-1/2)Lw
        =Lw^TLw=C^TD^(-1)C.

The delay preserves the infinite time-L2 norm because negative history is0. Therefore PATH BY PATH ||z||_2<=kappa||w||_2 and N1(z)<=kappa N1(w)<gamma N1(w) under(GAMMA). A deterministic L2 input along a top singular direction gives equality at kappa, so this law's UNIFORM gain is EXACTLY kappa, not an evaluated approximation or a ratio of two RMS estimates. If C=0 the gain0 case is immediate.

### 4.3 Full original internal MS stability and admissibility

For w=0 and any square-integrable initial state, (5) has the strict positive quadratic certificate(MS). Put W=-(Ac^TH+HAc+Nc^THNc)>0. With lambda=lambda_min(H^-1/2 W H^-1/2)>0, stopped exponential Itô/Fatou gives E(x^THx)(t)<=exp(-lambda t)E(x0^THx0), hence a full Euclidean EMS bound by norm equivalence.

No fourth moment is needed: localize before taking expectation of the quadratic storage and use nonnegativity/Fatou, or use finite-time linear-SDE second moments and the ordinary H1 bracket-root bound. This certificate is not inferred from zero-state attenuation.

Equation(5) remains homogeneous for arbitrary admissible w, so E integral|x|^2 is finite for L2 initial states. Control(4) is a bounded linear combination of this state and the delayed expected-L2 input; its expected squared energy and the output energy are finite. Strong global well-posedness is the ordinary homogeneous linear-SDE one, with an adapted measured-input feedforward. Thus the realizer satisfies even stronger all-input state/control-energy admissibility than the frozen base local-pathwise requirement.

## 5. Why the two matches are the actual sharpness interface

The universal DC lower bound uses D+AbarQ^-1Abar^T: a state offset may in general reduce the control effort needed to balance a constant forcing. DC-MATCH is precisely the displayed sufficient algebraic condition making its forcing Gram equal to the direct minimum-control Gram C^TD^-1C. Deleting it is not justified by an old mean-square theorem.

FORCE-NOISE ensures that this minimum-price forcing cancellation does not inject a NEW Brownian input. Global ORTH is stronger than needed. The state feedback used for(MS) may itself leave NONZERO visible multiplicative diffusion; only its stability is certified. If FORCE-NOISE fails, the same feedforward law leaves-noise term -B0cal Lw*wlag. No claim that this random response has the same N1 level follows, and that case stays open.

The constant-state-noise S may have any magnitude/orientation consistent with the supplied MS certificate; in the full-ORTH subclass the explicit high-gain drift compensator always supplies one. This theorem does not erase stochasticity of the original plant, assert every optimal policy must cancel the state, or prove general N1=G2.

## 6. An entire positive-rational scalar family with truly VISIBLE autonomous noise

For ANY positive rational b,c,d,r,sigma and ANY finite h>=0, take

    dx=(b*u+c*w(t-h))dt+sigma*x dW,
    z=(d*x,r*u).

Here R=r^2,Q=d^2,K0=0,Abar=0,D=b^2/r^2>0, full ORTH holds because B0=0, but S=sigma is NONZERO and VISIBLE. No control can cancel the autonomous state diffusion for nonzero state. The exact criterion is

    gamma>r*c/b.

Choose k=1+sigma^2 and u=-(k/b)x-(c/b)w(t-h). The ACTUAL state is dx=-kxdt+sigma*x dW, with EMS rate2+sigma^2. For zero initial state it remains0 while output is(0,-(r*c/b)wlag), so the exact literal gain is r*c/b for every preview length. Necessity is the all-causal DC proof, not only a fixed-controller calculation.

All actual plant and controller coefficients are rational for these rational parameters. The squared threshold is the explicit rational(r*c/b)^2. These are HAND symbolic identities, NOT an interpreter-run finite certificate or original in-kernel acceptance. Preview cannot improve the uniform level on THIS family because the long-flat DC obstruction already fixes it; this is not a general statement that stochastic preview is useless.

## 7. Exact coupled example with GLOBAL QORTH FAILURE and nonzero drift

Take n=m=2, scalar input, and the actual constant matrices

    A=diag(0,1), B=I2, C=(1,0)^T,
    A0=I2, B0=[[0,1],[0,0]],
    D0=[[1,0],[0,1],[0,0],[0,0]],
    D1=[[0,0],[0,0],[1,0],[0,1]].

Thus z=(x1,x2,u1,u2),R=Q=D=I2,K0=0,Abar=A,S=I2. Every state is performance-visible, so there is no hidden quotient removing the noise. DC-MATCH holds because A^TC=0; FORCE-NOISE holds because B0C=0. But GLOBAL QORTH B0B^T=B0 is NONZERO, and full MATCH S=0 fails.

Supply the exact stabilizer

    K=diag(-4,-5), H=diag(1,5),
    Ac=-4I2, Nc=[[1,-5],[0,1]].

Its strict Lyapunov matrix is

    Ac^TH+HAc+Nc^THNc=[[-7,-5],[-5,-10]]<0,

since the first principal minor is-7 and determinant70-25=45>0. This is exact integer algebra, not a solved LMI/table program.

The ACTUAL current-state/delayed-endpoint law is

    u1=-4x1-w(t-h), u2=-5x2.

Original closed-loop equations are

    dx1=-4x1dt+(x1-5x2)dW,
    dx2=-4x2dt+x2dW.

Their visible Brownian diffusion is NOT canceled for nonzero initial states; the strict quadratic certificate supplies full internal EMS. For every zero-state input the actual state is0 and the output is(0,0,-wlag,0), with exact gain1. Theorem4 gives strict-uniform synthesis IFF gamma>1, for EVERY finite h>=0 and against arbitrary causal nonlinear competitors.

This example lies outside the earlier global-MATCH/QORTH N&S classes and outside unforced-hidden reasoning: the original input is nonzero/forced, every state is priced and observed, global noise-actuator orthogonality genuinely fails. The forcing-direction condition, not an unprovided broader quotient or controller-memory equivalence, closes it.

## 8. Proof/import ledger, endpoint scope and ENTIRE original residual

The only ordinary inputs are: Gram/Schur algebra, the nonsharp H1 true-martingale implication, Bochner/Jensen/Fubini, elementary L2 Sobolev trace/Cauchy, finite singular-value equivalence and linear-SDE Itô/Lyapunov facts. The NEW full mean/global DC bound, its exact matching identity, certificate/LMI equivalence, original-law substitution, pathwise sharp gain, full internal stability and examples are displayed. No old stochastic RMS criterion, v6/v7 norm ordering, optional sharp sqrt2 theorem, unreviewed v9-v11 synthesis or historical executable computation supplies a direction.

The theorem is exact at the declared strict UNIFORM level. The constructed gain is attained by deterministic inputs, but this alone does not classify a pointwise-every-input strict endpoint over ALL other nonlinear policies. No endpoint claim is imported from v9's different family. Finite-horizon F_t criteria and truncated terminal-preview counting retain their separate old scopes.

Unrestricted arbitrary-data N&S is STILL OPEN HERE: if DC-MATCH fails there is a state/control tradeoff below direct cancellation; if FORCE-NOISE fails actual noisy forcing persists; Q singular/Rdef remove the coercive global mean/trace argument; non-full-actuation and arbitrary nonlinear stabilization without(MS) are not classified by the enlarged theorem. Generic positive-preview predictor noise S(chi-p), QORTH failure outside the compatible forcing subspace, and universal printed-policy optimality remain. A supplied linear MS certificate is NOT silently proved necessary outside this class. No full-book solution or novelty/current-SOTA status is claimed.

This complete source requires its OWN actual full source-pinned reconstruction/application gate. Earlier accepted cores and other candidate papers do not certify it or an automatic domain union. The pre-opaque Abar0 lead and the later DC/FORCE matching strengthening are disclosed in checkpoints23–25/addendum9, not called preregistration; no pinned source was edited.

Own earlier primary private-written approximate-gloss PROCESS MAJOR remains permanent under the later parent assurance overlay, with ZERO approximate proof credit and no rerun. Current work uses exact WRITTEN symbolic/integer/rational identities only. No scientific interpreter/calculator/eval/program/CAS/enumeration/LMI-matrix solver/replay/simulation/CLI/nested agent/build/tests/formatter or GO occurred. All other historical findings/v9-v10-v11 HOLD/original October27 cutoff/deadline/eighteen-owner identities stay unchanged. No formal/kernel/human/configured-family/executable/novelty gate, round completion or indefinite park is claimed.
