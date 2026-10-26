# Infinite literal norm necessity under DUAL coercivity — occupation buffers cover unpriced non-H1 controls

InfoHinfPreview-2 / info-3. Earlier actual `/bin/date` observation before creation: **Sun Oct 25 18:07:33 PDT 2026**. Observation bound only. **ONE complete WRITTEN OWNER-CANDIDATE; its OWN complete fresh gate is required.** No full arbitrary-plant same-gamma N&S, novelty, formal/kernel/executable or configured-family acceptance is claimed.

## 0. Genuine new representation, exact union and limits

The new mechanism is an OCCUPATION estimate during a cleared-input buffer. It obtains a small actual state at the next start WITHOUT assuming the state at the preceding end is integrable and WITHOUT taking expectations of unpriced control noise. Thus the R-deficient non-H1-control obstruction in v8 does not itself block an RMS NECESSARY bound when the performance prices the state.

A second change is to replay an ARBITRARY canonical progressive compact probe as a nonanticipative Brownian-path functional. There is no cylinder-density/input-continuity step. Only initial-state continuity at the SAME input is needed. This removes input-Lipschitz/continuity from the R-positive local-state proof as well.

This paper PROVES one explicit dual-route theorem: EITHER control-price coercivity OR state-price coercivity, with the common local-state/EMS/current-window hypotheses below. It is not an automatic union of old v7/v11 domains. Both route proofs and all common links are provided. In particular it permits R=0, discontinuous input dependence and unpriced controls whose expected path-L2 norm is infinite.

An application settles a previously unclaimed global-gain boundary: the actual quadratic input-zero-indicator law of v8 has G2=G1=infinity at h0, despite its finite-energy pulse calibration and uniform zero-input EMS. This is a verdict for THAT LAW, NOT a synthesis impossibility for its plant; control0 is an available finite-gain stabilizer. Positive-delay infinite-gain classification is NOT claimed.

The ordinary inputs are canonical Wiener functional representation/independent increments, strong stopped-solution/local-state-Lipschitz estimates, autonomous-SDE restart, elementary probability/limits and, for the application, explicit radial-Brownian/Gaussian calculations reproduced below. No sharp Geiss–Scheutzow/Lenglart transfer, v9/v10/v12 synthesis theorem or expected-control-L2 admissibility is a premise. All old core/domain/gate boundaries remain separate.

## 1. Actual model, norms and the ENTIRE new law domain

Use the original scalar-Brownian constant-data model on INFINITY,

    dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW, z=D0x+D1u,

zero initial state/negative external-input history, any finite h>=0, and the canonical augmented Wiener filtration. Inputs are ALL progressive processes with E integral|w|^2<infinity. Let N1(f)=E||f||_time-L2, N2(f)=(E||f||_time-L2^2)^(1/2); G1,G2 are induced gains on that SAME full input class, in extended-real sense.

Fix ONE deterministic STATIONARY printed law u=F(x,eta_t), F(0,0)=0, using only actual current x and the current external-input window/finite taps. There is no auxiliary controller state, independent random controller, permanent input-history flag or clock. Require:

- strong nonanticipative well-posedness/nonexplosion and local PATHWISE control L2 for every allowed input/initial state;
- for each state radius R a finite L_R with

    |F(x,eta)-F(y,eta)|<=L_R|x-y|, |x|,|y|<=R,          (STATE-LOC)

  uniformly over the SAME arbitrary input tuple eta. NO continuity/Lipschitzness in eta is assumed;
- EXPLICIT uniform zero-input/zero-window EMS

    E_xi|X_s|^2<=M exp(-lambda s)|xi|^2                 (EMS)

  for all deterministic states xi, common M,lambda>0. It is not inferred from finite G1.

Finally require AT LEAST ONE of the following actual-data conditions:

    (A) R=D1^TD1>0;                                    (CONTROL-PRICE)

    (B) Qperp=D0^T(I-P_D1)D0>0,                        (STATE-PRICE)

where P_D1 is the finite Euclidean orthogonal projection onto range(D1), defined even if D1 is singular. Under(B), |x|<=c_x|z| for c_x=lambda_min(Qperp)^(-1/2), for EVERY x,u, because (I-P_D1)z=(I-P_D1)D0x. There is NO R inverse in this branch and no requirement that u have H1 or expected squared energy.

**Theorem 1.** On this ENTIRE dual-coercive law/data domain,

    G2(F)<=G1(F).                                      (1)

Thus G1(F)<gamma implies G2(F)<gamma at the SAME level for this class. It is a necessary norm relation, not same-gamma synthesis sufficiency or equality. V7 still separately covers other globally Lipschitz domains without either coercivity; no unproved all-controller regularity is asserted.

## 2. Arbitrary canonical probe transport — no input approximation

Fix ANY progressive expected-L2 probe v supported on[0,S], b=E||v||^2>0, and a finite L>S+h. It need not be bounded, a cylinder, continuous in time, or independent of the Brownian path. On canonical Wiener space a progressive process has a jointly measurable nonanticipative path-functional version v_t=Psi_t(W_[0,t]), up to the standard dt-times-probability null equivalence. This is ordinary functional representation, not continuity of the input/output operator.

At a deterministic start t_i replay the SAME Psi under relative increments W_(t_i+s)-W_(t_i). It is a valid progressive input. Strong nonanticipative solution uniqueness with fixed deterministic F makes the corresponding zero-state response on[0,L] a measurable functional of that own increment segment. Across disjoint own windows the reference energies are iid in LAW. Stationarity is essential. No claim for unexplained larger filtrations or extra random controller parameters is made.

If Psi was originally described using a zero-state feedback stopping rule, it remains THAT fixed Brownian functional when replayed. It is NOT recomputed from the actual block's possibly nonzero state. This keeps the actual/reference input identical for the state comparison. It is a legitimate external progressive adversary, not a physical state reset.

## 3. Initial-state continuity of TRUNCATED energy at the SAME arbitrary input

Let z^xi,z^0 be probe responses on[0,L] under the SAME input functional/future Brownian segment, with zero external history. For H>0 put

    Phi_H(z)=min(integral_0^L|z|^2,H).

Then

    sup_(|xi|<=a) E|Phi_H(z^xi)-Phi_H(z^0)| ->0 as a->0. (2)

Indeed, before either state exits radius R, the drift DIFFERENCE is A delta_x+B delta_F, the diffusion difference A0 delta_x+B0 delta_F; forcing cancels and(STATE-LOC) bounds delta_F by L_R|delta_x|. The difference SDE therefore has the usual stopped Itô/isometry/maximal/Gronwall bound E sup|delta_x|^2+E||delta_z||_L2^2<=K_(R,L)|xi|^2. No individual control-noise expectation was taken. If necessary first localize each path's control bracket, then remove it: the DIFFERENCE integrand is bounded on the common state stop, independently of those control expectations.

The reference is nonexplosive, so its exit probability from R/2 tends0 with R. While it stays there, an actual exit at R requires a difference at least R/2, controlled by the stopped estimate. Thus the full output converges in probability in time-L2 uniformly as xi tends0. Phi_H is bounded by H and globally2sqrt(H)-Lipschitz in output L2 norm; local estimates plus the bad-exit probability prove(2).

There was NO input regularity/continuity/density step: the input is exactly the same fixed arbitrary probe on both sides. Conditioning on a past state independent of the fresh relative increment segment gives the same uniform small-state conclusion for random initial states with only L1 control of their norm.

For each H,n choose a_n>0 making the supremum in(2) at most1/(2n^2), and set epsilon_n=min(1,a_n/(2Hn^2)). If E|xi|<=epsilon_n, Markov on {|xi|>a_n} and boundedness by H give

    E|Phi_H(z^xi)-Phi_H(z^0)|<=1/n^2.                  (3)

No second moment of xi is assumed.

## 4. Conditional zero-window EMS applies to L1 past states

Once the actual external window AND delayed forcing are zero, the stationary law is the deterministic autonomous F(x,0). Under the stated strong well-posedness/local-state-Lipschitz conditions, its conditional future transition law at a deterministic time is the zero-input law from that current state and fresh Brownian increments. This is an actual restart property of this printed law, not Markovization of an arbitrary remote-history controller.

From(EMS), pointwise in deterministic xi,

    E_xi|X_s|<=sqrt(M)exp(-lambda s/2)|xi|.             (4)

Integrating this transition-kernel inequality gives(4) for a past-measurable L1 initial state, EVEN with infinite second moment. In the state-price occupation argument below the selected starting time need not be chosen at all: inequality(4) is integrated over almost every deterministic time with finite first moment.

## 5. Deterministic buffers — BOTH coercivity routes proved

If G1=infinity,(1) is immediate. Otherwise let g=G1<infinity. For each fixed n,H repeat the probe n times with own duration L and a deterministic buffer R_n>=1. Let w_n be their actual disjoint sum. Expected input energy is nb, so N1(w_n)<=sqrt(nb), and the ACTUAL global output satisfies

    N1(z(w_n))<=g sqrt(nb).                            (5)

This bound holds for EVERY deterministic choice of buffers, so choosing them from the following fixed constants is not circular. It includes ALL buffer output, not merely own-window restrictions. Every own end at L>S+h has already cleared external history and forcing.

### 5A. CONTROL-PRICE route, without state observation

When R>0 complete the square with K0=-R^-1D1^TD0, nu=R^(1/2)(u-K0x), Q>=0. Then |z|^2=x^TQx+|nu|^2. In the actual state equation use Abar=A+BK0,S=A0+B0K0,Bcal=BR^-1/2,B0cal=B0R^-1/2.

A finite-time L1 estimate follows from short-block H1 absorption. The ordinary nonsharp vector maximal bound E sup|M|<=10 E(trace[M])^1/2 follows, for example, from the stopped good-lambda estimate with bracket threshold r^2/16 and integration64/7<10. Stop in state/control energy first and choose delta with ||Abar||delta+10||S||sqrt(delta)<=1/2. The stopped state equation then absorbs its self-noise term, bounding a block supremum by twice its initial L1 norm plus fixed multiples of N1_block(nu),N1_block(wlag). Finite iteration, sum-block-norm Cauchy and Fatou give, for fixed L,

    E|x_end|<=C_L(E|xi_start|+N1_own(nu)+N1_own(wlag)).

No N2 state/control or NEO hypothesis was used. From(5), N1_own(nu)<=g sqrt(nb), and the own forcing norm has mean<=sqrt(b). Thus if the start L1 norm is<=epsilon_n,

    E|x_end|<=C_L(epsilon_n+g sqrt(nb)+sqrt(b)).

Choose finite deterministic R_n so sqrt(M)exp(-lambda R_n/2) times this last bound is<=epsilon_n. Conditional(4) gives the next actual start bound. Induction begins at0. This proves the control-price route with only(STATE-LOC), not input Lipschitzness: arbitrary-probe replay in §2 removed the old input-density requirement.

### 5B. STATE-PRICE OCCUPATION route, even when free control is not H1

Let t_e be an own end and t_b=t_e+R_n the next start. By state coercivity and(5),

    integral_0^1 E|x(t_e+r)|dr
       <=E||x||_L2(t_e,t_e+1)
       <=c_x N1(z(w_n))<=c_x g sqrt(nb).              (6)

Hence for almost every r in[0,1] that past state is L1. The input/window remain zero throughout the buffer. For each such r, actual conditional(4) gives

    E|x(t_b)|<=sqrt(M)exp[-lambda(R_n-r)/2]E|x(t_e+r)|.

The left side is therefore finite, and integrating r (not selecting a random or future-dependent start) yields

    E|x(t_b)|<=sqrt(M)exp[-lambda(R_n-1)/2]
                                             *c_x g sqrt(nb). (7)

Choose deterministic R_n>=1 making(7)<=epsilon_n. This needs NEITHER E|x(t_e)| nor N1(u) nor any expected stochastic-integral mean. It proves every next actual start small in L1; the first is0. A strict local martingale in an unpriced control channel does not invalidate(6)–(7), because only the given state transition bound was integrated.

If both coercivities hold, either proof may be used. They do not mix incompatible hypotheses, and no automatic prior-domain union is assumed. Both route choices are finite/deterministic, depend on law/probe/n/H constants rather than future Brownian paths, and NEVER reset the physical state.

## 6. Exact constant1 from bounded reference energies, then ALL inputs

On each own window create a VIRTUAL zero-state response with the SAME probe/Brownian segment. Its truncated energy A_i^H has the common bounded law Phi_H(z^0), iid across windows. The actual start bound and(3) give expected absolute difference of actual/reference truncated energies<=1/n^2. Errors need not be independent.

For nonnegative energies, pointwise sqrt(sum actual)>=sqrt(sum reference-truncated)-sqrt(sum absolute-truncated-differences). Restricting output to own windows and Jensen for this ERROR give

    N1(z(w_n))>=E sqrt(sum_i A_i^H)-1/sqrt(n).

The bounded iid averages concentrate by variance<=H^2/n and Chebyshev, so E sqrt(n^-1 sum A_i^H) tends sqrt(E A_1^H). Combine with(5), divide by sqrt(n), let n increase, and obtain E A_1^H<=g^2b. Monotone limits H->infinity and L->infinity give

    E integral_0^infinity|z(v)|^2<=g^2 E integral_0^S|v|^2

for EVERY canonical progressive COMPACT probe, not merely a dense subclass. The argument did not assume reference energy integrable before truncation or actual state square integrable during inputs.

For arbitrary infinite progressive input w, take its TIME prefix w*1_[0,S]. It is already an allowed compact probe, with NO change in input values before S. Strong causality/current-window information identifies its output with the true one through S. The compact bound then controls true E integral_0^S|z|^2 by g^2 E integral_0^S|w|^2. Let S increase by monotone convergence. This proves(1) on the FULL input class without any input-continuity assumption. Infinite G2 with finite G1 is excluded; g0 and zero output cases require no output-norm division.

The theorem is infinite-horizon and stationary. It gives no finite-horizon ordering, norm equality, same-gamma N1 sufficiency, universal stationarity/regularity theorem, or result for larger unexplained filtrations/random controllers.

## 7. The actual R0 calibration law satisfies the new state-price domain

For the new application set h=0 and take the SAME actual law/plant as v8,

    dX=(-aX+c w)dt+u dW, z=X,
    u=-X^2*1_(w=0), a,c>0.                            (8)

R=0, Qperp=1, c_x=1. The law is stationary/current-input and locally state-Lipschitz with constant2R on a radius-R ball, UNIFORM over the same arbitrary input value. It is DISCONTINUOUS in the input at0, so input-continuity could not simply be imported from v7/v11. It is precisely covered by Theorem1's new route.

For completeness the operative admissibility/EMS/path-law facts are reconstructed, not a full-gain claim inherited from v8. With g_t=1_(w_t=0), psi=log(1+X^2),

    Lpsi=-2aX^2/(1+X^2)+2cXw/(1+X^2)
               +g_t^2 X^4(1-X^2)/(1+X^2)^2<=1+c|w|.

At bounded state exits the martingale coefficient is bounded. Expected-L2 input makes E integral|w| finite on every finite prefix; the stopped bound divided by log(1+R^2) sends exit probabilities to0. Uniformly locally state-Lipschitz progressive coefficients therefore have a unique global strong solution. Compact continuous paths give pathwise-local control L2, NOT N1(u).

At w=0 and positive xi, let R_s be three-dimensional Brownian radius started at r=1/xi. Harmonic1/|x|/annulus stopping bounds small-radius hitting by epsilon/r, hence the origin is not hit. Radial Itô gives dR=d beta+R^-1 ds with ONE radial Brownian beta; Y=1/R solves dY=-Y^2 d beta. With

    theta(t)=(1-exp(-2at))/(2a), X_t=exp(-at)Y_theta(t),

deterministic time change gives exactly dX=-aXdt-X^2dW. Local uniqueness identifies the continuous PATH LAW with the actual ONE-Brownian scalar plant. Three-dimensional Brownian motion is only a law derivation, not an extra controller noise or a reset.

Gaussian scaling gives E Y_s^2=xi^2 E|e1+sqrt(s xi^2)Z|^-2. The last expectation is uniformly<=100. One exact bound: for zeta>=1/4, split radius sqrt(zeta); maximal density inside plus1/zeta outside give(1+sqrt(2/pi))/zeta<=12. For0<zeta<=1/4, outside radius1/2 contributes<=4; inside contributes at most(2pi)^-1/2 zeta^-3/2 exp[-1/(8zeta)]. Setting q=1/(8zeta), q^(3/2)e^-q is maximized at3/2 and is<2, since(3/2)^3=27/8<4. The prefactor becomes16/sqrt(pi), so the inside term is<32. The loose100 bound includes zeta0. Therefore

    E_xi X_t^2<=100 exp(-2at)xi^2,
    E_xi integral_0^infinity X_t^2dt<=50xi^2/a.         (9)

Reflection X->-X,W->-W covers negative xi;0 is absorbing. This proves uniform zero-input EMS and conditional past-initial versions, without fourth moments or control H1.

Angular Gaussian integration gives the radial density

    p_s(r,y)=y/[r sqrt(2pi s)]
          *[exp(-(y-r)^2/(2s))-exp(-(y+r)^2/(2s))].

Multiplying by1/y and integrating gives

    E Y_s=xi*P(|N(0,s)|<=1/xi)<xi, s>0.                (10)

The strict gap is a symbolic positive Gaussian tail, not a computed decimal. Facts(8)–(10) are the exact v8 calibration interfaces; they do NOT by themselves assert finite UNIFORM G1, which was never claimed there.

## 8. An actual compact ADAPTED input family proves G2=infinity at h0

Prepare xi>0 from ZERO initial state by w=q0>0 on[0,S], then0. During that pulse the SAME law sets u0, so

    xi=(c q0/a)(1-exp(-aS))>0.

Let the BASE unforced scalar solution after S start from xi under the original future Brownian increments. Fix finite T>0 and hold duration Delta>0. Let tau_R be its first hitting time of R>xi; it is a canonical stopping time. This base process is used to DEFINE the external input functional, not recomputed from another block's actual state.

We first give an exact lower hitting bound WITHOUT a new Bessel hitting formula. For driftless inverse-BES Y, stop at sigma_K=inf{Y>=K}, K>xi. The bounded stopped local martingale is true, so for q=theta(T)>0,

    xi=K P(sigma_K<=q)+E[Y_q*1_(sigma_K>q)].

By(10), delta_q=xi-EY_q>0, hence P(sigma_K<=q)>=delta_q/K. Take K=R exp(aT). If Y reaches K by theta(T), its corresponding actual base X reaches at least R by T. Continuous path-law identification therefore gives

    P(tau_R<=T)>=exp(-aT)delta_q/R.                   (11)

Now define the ACTUAL external input w_R: retain the preparation pulse; afterward keep0 until S+tau_R; IF tau_R<=T, use a fixed epsilon>0 on[S+tau_R,S+tau_R+Delta], then0 forever. If no hit before T, there is no second pulse. This is progressive: before the hitting time it is0, and at that time the event tau_R<=T is already known. It does not inspect a future event before it is observable. Support is within[0,S+T+Delta] and PATHWISE input energy is<=q0^2S+epsilon^2Delta, independent of R.

Strong stopped-input consistency makes the actual state agree with the base until the trigger, so it equals R there on the triggering event. For h0, positive epsilon IMMEDIATELY switches the SAME current-input indicator law to u0. During the hold its actual state is the ODE solution

    X_(trigger+s)=R exp(-as)+(c epsilon/a)(1-exp(-as))
                      >=R exp(-aDelta), 0<=s<=Delta.

Thus(11) gives

    E integral|z_R|^2
       >=Delta*exp[-a(T+2Delta)]*delta_q*R.            (12)

The denominator E integral|w_R|^2 is bounded by the fixed preparation/hold energy. Let R increase through integers larger than xi. The RMS induced gain is therefore INFINITE.

Each such probe can even have finite output expected energy: before the trigger or T, the base is bounded by R; during the hold it is bounded by R+c epsilon/a; afterward(9), conditionally at the last-input end, bounds its entire tail. This gives a finite bound of the form S(cq0/a)^2+TR^2+(Delta+50/a)(R+c epsilon/a)^2. No output-energy infinity for a SINGLE probe was needed; the ratios are unbounded across the family. All inputs use the SAME plant/law, not a new initial state/controller per R.

## 9. Why this also proves literal G1=infinity — and what it does NOT prove

Law(8) meets EVERY state-price hypothesis of Theorem1 by §7. Hence G2<=G1 applies despite unpriced control N1 possibly being infinite. Since(12) proves G2=infinity, it follows that

    G1(F_quadratic,h0)=G2(F_quadratic,h0)=infinity.

A SINGLE rare hitting event would not justify this: its expected ROOT output need not grow like its expected squared energy. The occupation-buffer/replayed truncated-energy theorem is the essential transfer to literal gain. This is not an invalid Jensen comparison of two random denominator norms.

For ANY h the original v8 delayed-indicator law still meets Theorem1's hypotheses, so its extended norm ordering follows. But the immediate noise-stop construction(11)–(12) used h0; NO h>0 infinite-gain assertion is made. The old actual finite pulse can retain finite output energy and infinite N1-control as already proved. The new global gain conclusion does not contradict that per-input calibration.

This is NOT original-plant synthesis infeasibility: the same R0 plant admits u0, a deterministic stable convolution with literal gain c/a. Whether other unpriced controls improve the original prescribed-gamma optimum is not settled here. No input-energy variable, stopping flag or extra Brownian source was inserted into the CONTROLLER; only the external progressive adversary used its allowed stopping history.

## 10. Whole proof/gate boundary and remaining original problem

The new theorem's decisive edges are explicit: arbitrary canonical probe transport without input regularity; local same-input initial-state continuity of bounded energies; TWO separately proved coercivity/buffer routes; the STATE-PRICE occupation integration with no endpoint moment/control H1; deterministic waits/no actual reset; iid reference energies with dependent actual errors; and direct time-prefix extension to ALL inputs. The R0 global-gain application adds exact bounded stopping/hitting lower bounds and an actual same-law compact adversarial input.

This is a NEW explicit domain union PROOF candidate, not automatic adoption of v7/v11 or the separately supported v8 core. Ordinary functional representation/strong-flow/Markov/Itô/Gaussian facts remain named mathematical inputs; no unprovided sharp probability theorem or synthesis lemma fills a step. A fresh complete gate must reconstruct both coercivity branches and the full new application before promotion.

Still OPEN: same-gamma literal sufficiency outside v12's DC/forcing matching, nonlinear optimality/printed-realizer characterizations for arbitrary noise/actuation, unobservable/unpriced states and controls when neither coercivity holds, original state-irregular laws, larger filtrations/random controller domains, arbitrary nonlinear MS stabilization, and the h>0 gain classification of the quadratic law. No finite-horizon norm ordering, N1=RMS generally, unrestricted book N&S, novelty/priority or stronger acceptance is claimed.

All new arguments are EXACT WRITTEN integers/rationals/symbols. No scientific interpreter/calculator/eval/program/CAS/enumeration/SDE experiment/matrix routine/solver/replay/build/tests/formatter/CLI/nested agent/GO occurred. Old approximate-gloss PROCESS MAJOR has ZERO proof credit and is not repaired by this exact writing; all other owner/parent/reviewer findings/HOLD/exposure/clock qualifications remain. Frozen sources are unchanged, original eighteen owners/cutoff/deadline remain, and no round completion or indefinite park is declared.
