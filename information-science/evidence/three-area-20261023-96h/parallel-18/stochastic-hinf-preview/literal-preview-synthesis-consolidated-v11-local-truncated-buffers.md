# Generic visible-noise norm bridge with LOCAL state regularity: truncated energies, not mean-square errors

Owner InfoHinfPreview-2 / info-3. Earlier actual `/bin/date` observation before creation: **Sun Oct 25 16:18:41 PDT 2026**. Observation bound only. **Complete WRITTEN OWNER-CANDIDATE, pending its OWN fresh reconstruction/application gate.** No arbitrary-plant same-gamma N&S, linear optimality, novelty or kernel/executable acceptance is claimed.

## 0. Exact new representation and separation from old gates

V7's supported nonlinear norm proof uses a GLOBAL state-Lipschitz constant to compare each actual own-window output with its zero-state reference in mean square. This source replaces that step by BOUNDED TRUNCATED-ENERGY continuity. The actual state at a block start need only be small in L1, obtained from R-positive output pricing, a finite-time H1 bootstrap, and the explicit zero-window EMS. No global state growth/Lipschitz bound or forced-state second moment is assumed.

The result gives G2(F)<=G1(F) on an explicitly larger LOCAL-state-regular domain within the R-positive part of v7. It does NOT subsume v7's rank-deficient domain: price coercivity is essential to this proof. Genuine uncancellable visible autonomous noise/control-noise coupling are allowed. The final cubic feedback example lies outside global state Lipschitzness and has actual visible Brownian state noise, finite literal gain and uniform EMS.

A separate elementary stopped-energy argument gives the NONSHARP converse estimate G1<=2sqrt(2)G2 for any zero-preserving strongly causal well-posed operator with the stated stopping consistency. This is NOT the unreconstructed SHARP sqrt2 Geiss–Scheutzow/Lenglart import. In particular it does not reaccept the optional v7 assertion G1<=1/sqrt2. The two results do not give same-gamma equivalence.

The current v91 parent supports v6/v7/v8 THREE distinct old cores only. V9 and v10 synthesis remain separate candidates. This source uses NONE of their unreviewed synthesis conclusions. Its H1/restart estimates are supplied operatively below; ordinary continuous-martingale maximal, Itô/localization/continuous-dependence, canonical-cylinder density and autonomous-SDE restart facts are named at their exact use. Earlier v10/checkpoint22/addendum8 reasoning is exposed, not relabeled preregistration. All frozen sources stay unchanged.

## 1. Actual model, norms and the ENTIRE new law domain

Use the same scalar-Brownian constant plant on INFINITY,

    dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW, z=D0x+D1u,

zero initial state/negative input history, finite h>=0, canonical augmented Wiener filtration, and ALL progressive inputs with E integral|w|^2<infinity. N1(f)=E||f||_L2, N2(f)=(E||f||_L2^2)^(1/2), with induced gains G1,G2 defined over that same full input class. Base control admissibility is local PATHWISE L2, not an assumed expected-L2 control condition.

Fix ONE deterministic STATIONARY original law u=F(x,eta_t), F(0,0)=0. Eta consists of finitely many delayed/current input taps and the Hilbert L2[-h,0] external-input window. There is NO other controller state or remote input memory. Strong well-posedness/nonexplosion for all allowed inputs is an explicit domain premise.

The NEW regularity condition is:

    for every R<infinity there is L_R<infinity such that
    |F(x,eta)-F(y,zeta)|<=L_R(|x-y|+||eta-zeta||)
    whenever |x|,|y|<=R, for ALL eta,zeta.               (LOC-LIP)

There need not be a finite global state-Lipschitz constant. The input-tuple Lipschitz bound is uniform over ALL tuples on each state ball; it is not silently replaced by arbitrary measurable input dependence. In particular on each state ball F has at most linear input growth. Taps/window form a bounded linear map in time-L2: each tap contributes at most one input energy and the window at most h input energy.

Also require the EXPLICIT actual uniform zero-input/zero-window EMS:

    E_xi|X_s|^2<=M exp(-lambda s)|xi|^2                 (EMS)

for all deterministic initial states xi, some common M,lambda>0. This is not inferred from G1 finite or local regularity. Autonomous strong restart after the exogenous window clears is valid under these state-local-Lipschitz/well-posed hypotheses.

Finally assume the actual R=D1^TD1>0. There is no NEO, MATCH, QMATCH, QORTH, detectability, drift stability or noise-cancellation hypothesis. This source does not assert that every original feasible printed law belongs to(LOC-LIP)/(EMS).

**Theorem 1.** On this ENTIRE law/data domain, in extended-real sense,

    G2(F)<=G1(F).                                      (LB)

The proof below is nonlinear, uses no actual reset/superposition, and extends to ALL the stated progressive inputs rather than cylinder probes alone.

## 2. Operative finite-time L1 state estimate from R-positive price

Complete the actual output square with

    K0=-R^(-1)D1^TD0, Abar=A+BK0, S=A0+B0K0,
    nu=R^(1/2)(u-K0x), Bcal=B R^(-1/2), B0cal=B0 R^(-1/2),
    Q=D0^TD0-D0^TD1R^(-1)D1^TD0>=0.

Then |z|^2=x^TQx+|nu|^2 and the state has drift Abar x+Bcal nu+Cwlag, diffusion Sx+B0cal nu. In particular N1(nu)<=N1(z), NOT E||nu||^2<=N1(z)^2.

The ordinary nonsharp vector H1 bound used here is E sup|M|<=10 E(trace[M])^(1/2). For completeness its stopped good-lambda estimate is P(M*>2r,sqrt(V_T)<=r/4)<=P(M*>r)/16, from conditional stopped isometry/weak L2 maximal control. Integration gives64/7<10; simultaneous norm/bracket localization, Fatou and dominated stopping give the true/UI implication when the bracket root has finite mean. This is independent of every sharp probability import.

On a sufficiently short deterministic interval delta,

    ||Abar||delta+10||S||sqrt(delta)<=1/2.

Localize in state norm/control energy first. The stopped state integral equation gives

    E sup_block|x|<=E|x_start|+(1/2)E sup_block|x|
       +(||Bcal||sqrt(delta)+10||B0cal||)E||nu||_block
       +||C||sqrt(delta)E||wlag||_block.

Absorb, iterate finitely many blocks (a bound3^N suffices), use sum of block norms<=sqrt(N) times the whole norm, then Fatou. Thus for each fixed L there is a finite deterministic C_L, depending on plant/L but NOT F's global Lipschitzness or an input amplitude, such that

    E|x(L)|<=C_L(E|x(0)|+N1_L(nu)+N1_L(wlag)).         (1)

The same proof bounds E sup|x|. The FULL diffusion has H1 norm bounded by ||S||sqrt(L)E sup|x|+||B0cal||N1_L(nu), so its finite-prefix mean is legitimate. No N2 control/state premise was used. Stops are removed only after the level-uniform estimate; this is not a circular BDG application to an unproved state moment.

## 3. Zero-window EMS contracts L1 past states, not only L2 states

After the actual external window and delayed forcing clear, the law is the deterministic autonomous F(x,0). Strong restart and(EMS) give the POINTWISE transition-kernel bound

    E_xi|X_s|<=sqrt(M)exp(-lambda s/2)|xi|.

Integrating this kernel against ANY past-measurable L1 initial state proves the same estimate with E|xi| on the right. A finite second moment of that random initial state is NOT required. Future Brownian increments are independent of the past; there is no new seed/controller state. This conditional argument is an actual property of the stated printed law, not a Markovization of an arbitrary full-history controller.

## 4. Uniform small-initial-state continuity of TRUNCATED own-window energy

Fix a bounded canonical Brownian-cylinder step probe v supported on[0,S], E||v||^2=b>0, and ANY finite L>S+h. Let z^xi be its response on[0,L] from deterministic state xi and zero external history. Define

    Phi_H(z)=min(integral_0^L|z|^2,H), H>0.

For each fixed H,

    sup_(|xi|<=a) E|Phi_H(z^xi)-Phi_H(z^0)| ->0 as a->0. (2)

Here is the operative proof. Stop both state paths in a radius-R ball. Under(LOC-LIP), the SAME-input/SAME-Brownian stopped differences satisfy the ordinary Itô/BDG/Gronwall estimate E sup|delta x|^2+E||delta z||_L2^2<=K_(R,L)|xi|^2. This is a LOCAL estimate, not a global bound. The zero-state reference is nonexplosive, so its probability of exiting radius R/2 before L tends0 as R increases. While it stays there, an actual exit from radius R requires difference at least R/2, controlled by the stopped estimate. Thus the full output difference tends0 in probability, uniformly as xi tends0.

More explicitly Phi_H is bounded by H and is globally2sqrt(H)-Lipschitz as a function of the OUTPUT's L2 norm. On the no-exit event use the stopped L2 estimate; the bad event contributes at most H times its probability. First choose R large for the reference exit probability, then |xi| small. This proves(2) without E||z^0||^2 or forced-state second moments. Every path energy on a finite window is finite by the stated local admissibility.

Since the probe is a fixed functional of future relative Brownian increments, the uniform deterministic-state bound in(2) also applies CONDITIONALLY to a past state independent of those fresh increments. This is the exact form used next.

## 5. Deterministic buffers using ONLY actual end-state L1 and finite G1

If G1=infinity,(LB) is immediate. Otherwise fix g=G1<infinity. For fixed H and n choose a_n>0 so that the supremum in(2) is at most1/(2n^2). Put

    epsilon_n=min(1,a_n/(2H n^2)).

Then a random past initial state with E|xi|<=epsilon_n gives

    E|Phi_H(z^xi)-Phi_H(z^0)|<=1/n^2,                  (3)

because P(|xi|>a_n)<=epsilon_n/a_n and the difference is at most H. No second moment of xi is assumed.

Replay the probe n times on own intervals of length L, separated by a deterministic zero-input buffer R_n. Let w_n be their actual sum, with fresh relative Brownian increments in each copy. Its expected input energy is nb, hence N1(w_n)<=sqrt(nb). The gain property for THIS actual global input gives

    N1(z(w_n))<=g sqrt(nb), N1(nu on ANY own interval)<=g sqrt(nb).

If its actual own-window start state has E|xi_i|<=epsilon_n, the plant estimate(1) therefore gives

    E|x_end,i|<=C_L(epsilon_n+g sqrt(nb)+sqrt(b)).       (4)

The bound is independent of the buffer length and block number. It uses the GLOBAL actual gain for w_n, not a guessed per-block gain or a conditional gain theorem. L>S+h ensures the input window AND delayed forcing have already cleared at each own end.

Choose FINITE DETERMINISTIC R_n large enough that

    sqrt(M)exp(-lambda R_n/2)
          C_L(epsilon_n+g sqrt(nb)+sqrt(b))<=epsilon_n. (5)

These choices depend on fixed law/probe/n/H constants, NEVER on future realized Brownian increments. Conditional L1 EMS during the ACTUAL buffer then makes the next start state satisfy the required bound. Induction begins at xi_0=0. The simultaneous input w_n is already a valid compact progressive input for every deterministic choice of R_n; its gain bound holds independently of that choice. Thus(4)–(5) contain no circular input-selection/reset assumption.

The actual state is NEVER reset. There is no nonlinear superposition and no replacement of a mean-history controller by a printed one. The controller is the same fixed original F throughout.

## 6. Truncated iid energies supply the exact constant1 lower bridge

For each own window construct a VIRTUAL zero-state reference under the SAME input/Brownian segment. Its truncated energy A_i^H has the common law of Phi_H(z^0); these variables are iid across own windows by canonical fresh increments and STATIONARITY. They need not be independent of within-window input energies B_i. Actual errors/buffer histories need NOT be independent.

Let A_i^act be actual own-window energy and A_i^ref its reference energy. Equation(3) holds conditionally/in expectation for each block. Pointwise,

    sqrt(sum_i A_i^act)
      >=sqrt(sum_i min(A_i^ref,H))
                   -sqrt(sum_i|min(A_i^act,H)-min(A_i^ref,H)|).

Restriction to own windows and Jensen for this ERROR give

    N1(z(w_n))>=E sqrt(sum_i A_i^H)-sqrt(n/n^2).

For bounded iid A_i^H in[0,H], variance of their average is at most H^2/n. Chebyshev and bounded convergence of square roots show

    E sqrt((1/n)sum_i A_i^H) ->sqrt(E A_1^H).

Combine with N1(z(w_n))<=g sqrt(nb), divide by sqrt(n), and let n increase. The normalized error is at most1/n, so

    E min(integral_0^L|z(v)|^2,H)<=g^2 b.              (6)

Let H increase by monotone convergence, then let L increase. This gives FULL infinite expected output energy<=g^2 E||v||^2 for every bounded cylinder probe, including the possibility that the untruncated reference expectation was initially unknown/infinite. There is no fourth moment or full-tail decay assumption.

## 7. ALL progressive inputs: localized continuity in probability and Fatou

The result is not left at cylinder probes. On any fixed finite observation horizon, bounded canonical cylinder inputs approximate every progressive L2 input in L2(dt times probability). Taps and Hilbert windows are bounded linear shifts/Fubini operators in that topology.

Under(LOC-LIP), until either state exits a radius-R ball, the ordinary SAME-Brownian difference estimate is

    E sup|x^k-x|^2+E||z^k-z||_L2^2
       <=K_(R,T) E||w^k-w||_L2^2.

On the state ball the coefficients have only linear input growth, uniformly over input tuples, so this stopped estimate needs no global state growth bound. The reference state is nonexplosive. If it stays in R/2 while the approximant exits R, their stopped difference is at least R/2. Hence, first taking k to infinity and then R to infinity, z^k tends z in probability in time-L2 on the full finite observation interval.

Choose an almost surely convergent subsequence for that L2-valued convergence. Fatou passes the already proved expected-energy bound to z, while the input energies converge. There is NO unproved uniform integrability or global mean-square input/output continuity. For arbitrary infinite input, apply this to its compact prefixes; causality identifies the true output through each prefix time, and monotone convergence gives

    E integral_0^infinity|z|^2<=g^2 E integral_0^infinity|w|^2.

This proves G2<=G1 for ALL canonical progressive expected-L2 inputs. G1=0 and zero output-energy cases require no division by output norm; b>0 was used only to select a nonzero probe. Infinite G2 with finite G1 is excluded by(6). The theorem is INFINITE-horizon only; no finite-horizon norm ordering follows from the block argument.

## 8. A separate SELF-CONTAINED NONSHARP causal RMS-to-literal upper bound

**Lemma 2.** Let a fixed zero-preserving strongly causal well-posed input/output operator have RMS gain<=k over ALL progressive expected-L2 inputs, with stopped-input consistency as for the original strong current-window laws. Then

    G1<=2sqrt(2) k.                                    (UB)

This needs neither stationarity, R>0, EMS nor a global/local Lipschitz premise. It is an upper bound only, not a sharp theorem.

For a fixed input define ANALYTICAL processes X_t=integral_0^t|z|^2 and A_t=k^2 integral_0^t|w|^2. These are proof variables, NOT controller states. For ANY bounded stopping time tau, apply the RMS bound to the progressive stopped input w*1_(s<=tau). Strong stopped-input consistency identifies output up to tau, and the later output is nonnegative energy. Thus

    E X_tau<=E A_tau.                                 (7)

For fixed T stop at the first X crossing of lambda or first A crossing of delta, also at T. Both are continuous increasing processes. On {X_T>=lambda,A_T<delta}, X at this stop is at least lambda. Moreover A_stop<=min(A_T,delta). Equation(7) therefore gives

    P(X_T>=lambda)<=E[min(A_T,delta)]/lambda+P(A_T>=delta).

Set delta=lambda/2 and integrate the half-moment tail formula. For a fixed value A_T=a, splitting the first integral at lambda=2a gives

    (1/2)integral_0^infinity lambda^(-3/2)min(a,lambda/2)dlambda
       =sqrt(2a).

The second integral is E sqrt(2A_T). Hence E sqrt(X_T)<=2sqrt(2)E sqrt(A_T). Let T increase to infinity by monotone convergence. This proves(UB) with exactly the ordinary N1 denominator. k0 is immediate from the same domination; no sharp external probability result was used.

Combining(LB)/(UB) on Theorem1's domain gives

    G2(F)<=G1(F)<=2sqrt(2)G2(F).

This proves qualitative finite-gain equivalence on that domain, NOT same-gamma N&S or equality. A conservative sufficient RMS level is gamma/(2sqrt2); the necessary RMS level is gamma. The optional SHARP sqrt2 transfer from older sources remains separately NOT_RECONSTRUCTED/unaccepted; this proof does not claim its optimal constant or its optional numerical saturation bound.

## 9. A genuine uncancellable visible-noise, nonglobally-Lipschitz control

Take the original scalar plant/law, for ANY finite h>=0,

    dx=(-x+u+w(t-h))dt+(x/2)dW, z=(x,u), F=-x^3.

R=1,Q=1. The diffusion is genuinely VISIBLE and cannot be canceled by ANY control since B0=0. F is stationary/current-state, satisfies(LOC-LIP) on every state ball and F00=0, but has NO global state-Lipschitz constant.

For every allowed input f=wlag, the quadratic generator obeys

    L(x^2)=-(7/4)x^2-2x^4+2xf<=f^2.

Stopped expectation therefore rules out explosion for all expected-L2 inputs and square-integrable initial states. Local polynomial coefficients give strong local existence/uniqueness, so this proves the stated global admissibility; compact continuous paths give pathwise-local control L2. At f=0 the exponential quadratic test/Fatou gives

    E_xi|X_t|^2<=exp(-7t/4)|xi|^2,

with no fourth-moment assumption on a random L2 initial state (condition on deterministic states).

To prove actual expected output/control energy from ZERO initial state, put V=x^2/2+x^4/4 and q=x+x^3. Exact generator algebra gives

    LV=-q^2+(1/8)x^2+(3/8)x^4+q f
       <=-(13/16)q^2+q f
       <=-(13/32)q^2+(8/13)f^2.

The first inequality compares the x^2,x^4,x^6 coefficients; the second is ordinary Young. Also |z|^2=x^2+x^6<=q^2. At bounded state exits the storage martingale is bounded-localized. Since V>=0 and V(0)=0, stopped Itô followed by Fatou gives

    E integral|z|^2<=256/169 E integral|f|^2
                        =256/169 E integral|w|^2.

Thus G2<=16/13. Lemma2, using stopped-input consistency of this strong SDE, gives the actual finite literal bound

    G1<=32sqrt(2)/13.

No sharp sqrt2 theorem is invoked. This is a nonempty domain example with real uncancellable visible noise and cubic state feedback; its exact optimal gain is NOT claimed. It is not a synthesis impossibility or a counterexample to v7's correct global-Lipschitz theorem.

## 10. Exact assurance and the STILL unproved original step

Every decisive new link is supplied: R-price finite-H1 state control; conditional EMS for merely L1 past states; uniform TRUNCATED-energy continuity rather than a false N2 error assumption; deterministic-buffer induction using the actual GLOBAL gain; iid bounded reference energies and the vanishing normalized error; FULL progressive-input Fatou extension; and the independent nonsharp stopped-energy upper bound. No physical reset, nonlinear superposition, remote controller memory or clairvoyant waiting time occurs.

Theorem1 does NOT cover arbitrary measurable original F, arbitrary input discontinuity, additional controller randomness/filtrations, Rdef or laws lacking explicit zero-window EMS. Its local regularity is a genuine premise, not automatically inferred from G1 or strong admissibility. V7 still separately covers certain Rdef/global-Lipschitz laws. No automatic union of those domains is certified by this source.

The FIRST remaining same-gamma synthesis barrier is unchanged: even exact RMS necessity does not make a stochastic RMS controller's N1 gain equal at the SAME level. The nonsharp upper has a genuine level loss. Visible autonomous predictor forcing -S*p, QORTH failure, unpriced-channel H1 failure and arbitrary printed-law optimality/realization remain unclosed. No unrestricted finite/infinite matrix N&S, finite-book stationary syntax solution, pointwise-strict endpoint theorem or general G1=G2 is asserted.

This is a complete WRITTEN candidate requiring an independent complete source-pinned gate. No old core review, v9/v10 source or optional sharp import silently certifies it. No scientific interpreter/eval/program/CAS/enumeration/matrix routine/solver/replay/simulation/CLI/nested agent/build/tests/formatter or GO occurred. Coefficients, identities and limits are HAND proofs, not in-kernel checks. All old process majors/clock/exposure corrections/v9-v10-v11 HOLD, the original cutoff/deadline and eighteen-owner identities remain; no novelty/priority, formal/human/configured-family/executable acceptance, round completion or indefinite park is claimed.
