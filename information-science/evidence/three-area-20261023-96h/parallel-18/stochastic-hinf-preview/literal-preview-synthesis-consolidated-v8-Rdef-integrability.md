# Rank-deficient output cost — an exact inverse-Bessel obstruction to an unproved mean-zero extension

**InfoHinfPreview-2 / info-3. WRITTEN METHOD CALIBRATION / OWNER-CANDIDATE. CLASSICAL MECHANISM, NO NOVELTY CLAIM.** Actual immediately preceding `/bin/date` observation: **Sun Oct 25 14:00:52 PDT 2026**, a precreation observation bound.

## 0. Precisely what this proves and what it does NOT

The supported mean-necessity bridge used output-controlled diffusion or a priced control residual. A tempting R-deficient shortcut is to replace that by per-input state/output integrability and internal mean-square stability, then take expectation of the SDE. This manuscript gives a FULL actual constant-plant/current-window controller calibration showing that shortcut is invalid under the frozen LOCAL-PATHWISE-L2 control convention.

For every a,c>0 and h>=0 there is a stationary original-information law, strongly well posed for EVERY progressive finite-expected-energy input, which is uniformly exponentially MS stable on zero input. For a specified deterministic finite-energy pulse from ZERO initial state, its visible output has finite EVEN EXPECTED SQUARED energy, but its control has INFINITE expected path-L2 norm on every positive post-pulse interval. Its actual mean is STRICTLY below the formal drift-only mean. Thus the uncontrolled-price noise is a strict-local-martingale obstruction, not a true H1 martingale justified by state cost.

This is NOT a counterexample to the original synthesis problem, NOT a claim that this law has finite UNIFORM G1, NOT G1<G2 for it, and NOT a failure of any supported R>0/NEO/quotient theorem. The plant also admits simpler controllers. The classical inverse-BESSEL3 mechanism is not presented as novel. Its purpose is the exact declared-admissibility barrier: adding expected-L2 controls would exclude this law, but that is an EXPLICIT extra restriction rather than a consequence of state cost/stability.

Exposure addendum5 preceded this body and disclosed the informal inverse-Bessel route and all nonclaims. The precise convention was reread in v2 RAW23–31: source SHA256 `d1e367cff5a4098c60bd0e44226eec72b7c91ce7a69c538c1b680fc043e22173` says local PATHWISE square-integrable controls, not automatic expected energy. Current parent V4/V5 support is at its exact named domains and does not certify this new method calibration. V6/V7 remain separate comparisons; their global state-Lipschitz hypotheses are not assumed here.

All v1–v11/HOLD and original October27 cutoff/deadline remain. No scientific interpreter/eval/program, symbolic calculation, enumeration, simulation, solver, replay, CLI or nested agent ran. Every identity, bound and pulse below is WRITTEN. No actual SDE trial or Gaussian integral was computed by a machine.

## 1. Actual plant, law, input information and admissibility class

Take the scalar constant matrices

    A=-a, B=0, C=c, A0=0, B0=1,
    D0=1, D1=0,  a,c>0,

so the ACTUAL system is

    dX_t=(-a X_t+c w(t-h))dt+u_t dW_t,
    z_t=X_t,  X_0=0.                                    (1)

The cost is state-coercive but control-rank deficient: R=D1^TD1=0. W is ONE scalar Brownian motion. Negative input history is0. Inputs are progressive with finite expected squared energy, as frozen. Finite horizons retain input end T-h; the later chosen pulse is compact and may also be considered on infinity.

Use the deterministic STATIONARY printed current-window rule

    v_t=w(t-h),
    u_t=F(X_t,w_[t-h,t])=-X_t^2*1_(v_t=0).              (2)

It uses only current state and the LEFT endpoint of the permitted current window; no clock, energy accumulator, controller state, future noise or model unit is added. For each fixed input it is locally Lipschitz in X, uniformly on bounded state sets because the indicator is bounded. It is not globally state-Lipschitz or input-Lipschitz. Those failures are declared, not hidden.

The admissibility assertion here is strong nonanticipative/pathwise-unique GLOBAL existence with controls locally square integrable ALMOST SURELY. It is NOT the different expected-control-L2 class of the older quadratic substitute. If the latter is imposed instead, this example is expressly OUTSIDE that class.

## 2. Strong well-posedness for ALL allowed inputs; no special-pulse-only existence

For a progressive v, write g_t=1_(v_t=0). The coefficients

    b(t,x)=-a x+c v_t, sigma(t,x)=-g_t x^2

are progressively measurable and uniformly locally Lipschitz in x. Their stopped/global-cutoff equations have the usual unique strong solutions. To exclude finite explosion for the ORIGINAL equation, use the proper nonnegative function

    psi(x)=log(1+x^2),
    psi'=2x/(1+x^2),
    psi''=2(1-x^2)/(1+x^2)^2.

Its ACTUAL generator is

    Lpsi=-2a x^2/(1+x^2)+2c x v/(1+x^2)
                 +g_t^2*x^4(1-x^2)/(1+x^2)^2
         <=1+c|v|.                                      (3)

The diffusion term is<=1 on |x|<=1 and nonpositive outside; |2x/(1+x^2)|<=1. On exit-time localization the Lyapunov martingale is square integrable because its coefficient is bounded on the stopped state set. Hence for tau_R=first exit from[-R,R],

    E psi(X_(T wedge tau_R))
        <=psi(X_0)+T+c E integral_0^T|v_t|dt<infinity.

The final finiteness follows from the stipulated expected-L2 input. At exit psi=log(1+R^2); Markov's inequality makes P(tau_R<=T) tend0. Thus the local solutions patch to a unique nonexplosive strong solution for EVERY allowed input, not only the test pulse.

On every finite sample interval, a continuous nonexplosive state is bounded. Therefore

    integral_0^T|u_t|^2dt
                 <=T sup_(t<=T)|X_t|^4<infinity a.s.     (4)

This proves the exact local-pathwise control admissibility. It does NOT prove its expectation finite. Strong uniqueness/causal coefficient construction preserves nonanticipativity, event locality and zero response. Discontinuity of the zero-input indicator is allowed under this declared class; equal input versions almost everywhere give equal coefficients almost everywhere.

## 3. Classical inverse-BESSEL3 law, derived for the ONE-Brownian actual model

With external input0, (1)–(2) become

    dX=-aXdt-X^2dW.                                     (5)

For positive initial xi, put r=1/xi. Let R_s be the norm of a THREE-dimensional Brownian motion started at(r,0,0). This is used ONLY to derive a LAW, not as extra information/noise available to the controller. Three-dimensional Brownian motion started away from0 does not hit0: stopping the harmonic potential1/|x| on an annulus bounds the chance to hit radius epsilon by epsilon/r, then let epsilon decrease to0. Itô on its radius gives

    dR_s=d beta_s+R_s^(-1)ds,

where the radial martingale beta is one-dimensional Brownian by its unit quadratic variation. Thus Y_s=1/R_s satisfies

    dY_s=-Y_s^2 d beta_s, Y_0=xi.                       (6)

These positive nonexplosive laws agree with the unique scalar solution's law from §2. The physical plant still has ONE scalar W and the elementary controller(2).

Define the deterministic clock

    theta(t)=(1-exp(-2at))/(2a).

Then X_t=exp(-at)Y_(theta(t)) solves(5) in law: d beta_(theta(t))=exp(-at)dW_t after the deterministic Brownian time change, giving exactly -X_t^2dW_t and -aX_tdt. This law calculation does not make the controller implement a time change.

## 4. An EXPLICIT uniform second-moment bound and genuine MS stability

The Gaussian radial representation gives

    E Y_s^2=xi^2 E|e1+sqrt(s xi^2)Z|^(-2),
    Z standard Gaussian in R^3.

The normalized expectation is bounded uniformly over its nonnegative variance parameter zeta. Here is a nonsharp written bound100, not a numerical assertion.

If zeta>=1/4, split the integral at |y|=sqrt(zeta). Near0 use the maximum Gaussian density; outside use |y|^(-2)<=1/zeta. The result is

    E|e1+sqrt(zeta)Z|^(-2)
        <=(1+sqrt(2/pi))/zeta<=12.

If0<zeta<=1/4, the part |y|>=1/2 is<=4. On |y|<1/2 the distance from e1 is at least1/2, and the integral of |y|^(-2) over that ball is2pi. The remaining contribution is at most

    (2pi)^(-1/2) zeta^(-3/2) exp(-1/(8zeta)).

Set q=1/(8zeta). The function q^(3/2)exp(-q) has its maximum at3/2 and is<2; also8^(3/2)=16sqrt2<32 and(2pi)^(-1/2)<1. Thus that contribution is<64, and the total<68<100. At zeta0 the expectation is1. This proves

    E Y_s^2<=100 xi^2,
    E X_t^2<=100 exp(-2at)xi^2,
    E integral_0^infinity X_t^2dt<=50 xi^2/a.            (7)

Negative initial states have the same squared law after X->-X,W->-W, and0 is absorbing. Conditional future Brownian independence extends(7) to every square-integrable initial state. The zero-input law therefore IS uniformly exponentially mean-square stable, with a uniform mean-square integral bound, despite the unpriced nonlinear diffusion control. This stability was proved, not inferred from a zero-state gain.

## 5. STRICT loss of the formal mean

Integrating the three-dimensional Gaussian over angular coordinates gives the radial density, for s>0,y>0,

    p_s(r,y)= y/(r sqrt(2pi s))
       *[exp(-(y-r)^2/(2s))-exp(-(y+r)^2/(2s))].

To check the normalizing factor, the angular integral is the difference of the two exponentials divided by r*y/s, with surface factor2pi; multiplying by y^2(2pi s)^(-3/2) gives precisely the displayed formula. Therefore

    E(1/R_s)=1/(r sqrt(2pi s))
        *integral_(-r)^r exp(-v^2/(2s))dv
       =xi*P(|N(0,s)|<=r)<xi.                           (8)

The inequality is STRICT for every s>0 because the Gaussian has positive mass outside every finite interval. With the stable time change,

    E X_t=exp(-at)xi*P(|N(0,theta(t))|<=1/xi)
             <exp(-at)xi, t>0,xi>0.                    (9)

This is the classical strict-local-martingale defect; no Gaussian value was evaluated by a program. If the diffusion integral in(5) were a true mean-zero martingale, the already finite state first moments/Fubini would give the deterministic mean equation m'=-a m, contradicting(9).

In fact for EVERY T>0,

    E(integral_0^T X_s^4ds)^(1/2)=infinity.              (10)

Otherwise the H1 implication `E sqrt(bracket)<infinity => true mean-zero martingale`, proved earlier by the good-lambda/localization argument and used here only as an ordinary martingale fact, would make the integral -int X^2dW true mean-zero on[0,T]. State integrability in(7) justifies drift Fubini and the resulting mean ODE, again contradicting(9). Thus (10) follows, although its inside integral is FINITE ALMOST SURELY by path continuity. This distinguishes pathwise-L2, N1 control integrability and N2 control integrability exactly.

## 6. The defect occurs after a deterministic pulse from ZERO initial state

To place the calculation inside an actual zero-data response, choose q,S>0 and the deterministic finite-energy input

    w(t)=q for0<=t<S, and0 otherwise.

Its counted energy is q^2 S. Before h the state remains0. On[h,h+S], delayed forcing is q and controller(2) sets u=0, so the state follows the ordinary deterministic equation. At t0=h+S it is exactly

    xi=(c q/a)*(1-exp(-aS))>0.                          (11)

After t0 the delayed input is0, and the SAME stationary current-window rule automatically becomes u=-X^2. No clock switch, state reset, controller-memory switch or new initial-state hypothesis was inserted. The future Brownian increments are fresh, so §3–§5 apply to the continuation from deterministic xi.

The actual output for this input has finite EXPECTED SQUARED full-time energy:

    E integral_0^infinity|z|^2
       <=S(cq/a)^2+50xi^2/a<infinity,                   (12)

and therefore finite N1 output as well. Nevertheless for EVERY positive post-pulse interval length T,

    E||u||_L2(t0,t0+T)=infinity,
    E X_(t0+s)<xi exp(-as) for every s>0.               (13)

Thus neither a state-coercive output nor even this per-input RMS integrability plus internal zero-input MS stability makes the FREE control's diffusion H1. Taking expectation of the original zero-start SDE as if its local martingale were true is invalid for this actual input/law.

## 7. Exact inference blocked, and nonclaims that MUST remain

The example blocks the shortcut

    local-pathwise admissibility + state/output integrability
      + internal MS stability => diffusion H1/mean-zero.

It does NOT disprove an as-yet-unproved stronger implication using a GLOBAL UNIFORM gain hypothesis. I have NOT proved finite uniform G1 for(2), or its comparison with G2; adversarial other inputs may give infinite gain. Nothing here is a new stationary G1<G2 counterexample, nor does it contradict V7's globally-Lipschitz law theorem (x^2 violates that hypothesis).

It is NOT a nonexistence/solvability counterexample for the plant: for example u0 removes this deliberately chosen free noise, and the original synthesis question must optimize over controllers. The control is deliberately unpriced, R0; supported R>0/NEO and visible-quotient proofs remain unchanged and valid at their hypotheses.

If one changes admissibility to require E integral|u|^2<infinity, or even N1(u)<infinity, the law is excluded by(13). That is an explicit additional control-space condition. It cannot be silently read into the frozen local-pathwise interpretation to claim an unrestricted rank-deficient theorem. Conversely this countermodel must not be used against a theorem that ALREADY states such a stronger control-space assumption.

The Brownian radial/time-change mechanism is CLASSICAL; no priority/publishability is asserted. The new useful scope is its precise placement in actual constant plant/printed stationary-window coordinates with all-input strong admissibility, zero-input uniform MS stability, and a zero-initial finite-energy pulse producing finite output but an invalid mean-zero step.

## 8. Exact remaining general route and evidence ceiling

A genuine R-deficient synthesis proof must either control the free-channel martingale by a proved global-gain argument, supply a different necessary/realization representation not requiring this mean, or explicitly declare and justify a narrower expected-control admissibility class. No such general implication is established here. Likewise generic visible noncancellable noise, cost-bearing hidden stabilization outside HID and unrestricted same-gamma controller realization remain OPEN.

Named ordinary imports: local-Lipschitz progressively measurable SDE existence/uniqueness with localization, stopped Itô/exit estimates, three-dimensional Brownian radial Itô formula and nonhitting of a point (with its harmonic-potential argument), Brownian deterministic time change, Gaussian spherical integration, Gronwall/Fubini and the ordinary H1 martingale implication. Every operative nonexplosion, moment, mean and zero-data pulse calculation is displayed above. No unread classification, numerical inverse-Bessel result, stochastic H-infinity theorem or prior review headline fills a step.

All conclusions remain owner-WRITTEN method-calibration candidates pending fresh exact-body/import review. No scientific evaluator/program/table/replay, simulation/trial, physical state reset, external-model CLI, nested agent or new GO occurred. Frozen predecessor bytes stay unchanged. No formal/kernel/human/configured-family/executable/novelty acceptance, continuous18-way runtime or round completion is claimed. Original October27 cutoff/deadline and v1–v11/HOLD remain binding.
