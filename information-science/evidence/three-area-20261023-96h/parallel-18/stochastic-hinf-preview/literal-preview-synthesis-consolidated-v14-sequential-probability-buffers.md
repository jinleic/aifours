# Coercivity-FREE infinite norm bridge: deterministic sequential buffers chosen from PREFIX LAWS

Owner InfoHinfPreview-2 / info-3. Earlier actual `/bin/date` observation before creation: **Sun Oct 25 18:26:46 PDT 2026**. Observation bound only. **Complete WRITTEN OWNER-CANDIDATE; its OWN complete fresh gate is required.** No unrestricted prescribed-gamma synthesis, linear optimality, novelty or formal/kernel/executable acceptance is claimed.

## 0. The genuinely new representation and exact scope

The preceding v11/v13 lower bridges used control/state coercivity to obtain a uniform end-state moment and one common buffer length. That is sufficient but NOT needed for norm necessity. Here each finite prefix already fixes an ACTUAL finite-a.s. end-state distribution. Zero-input EMS returns ANY such distribution to0 IN PROBABILITY, even with NO moments. Choose the NEXT wait deterministically from THAT prefix law, then add the next probe. Causality prevents future choices from changing the law already used. The bounded truncated-energy comparison needs only a small bad-state PROBABILITY, not L1/L2 state control.

Consequently the theorem below has NO control-price R, state-price Q, rank, observability, NEO, MATCH or QORTH hypothesis. It also needs no input continuity or global state-Lipschitz constant. It treats the original nonlinear printed current-state/current-window law, not an enlarged-memory controller. This is a new proof replacing the quantitative common-buffer argument, not an automatic union or retroactive adoption of earlier sources.

For completeness a separate elementary NONSHARP upper bridge is proved too. Together they give G2<=G1<=2sqrt(2)G2 on the stated law domain: finite output gain is qualitatively equivalent, but SAME-gamma sufficiency/optimal realization remains unproved. This does NOT reconstruct the external SHARP sqrt2 Geiss–Scheutzow/Lenglart result or license an RMS Riccati theorem with stronger control-admissibility assumptions.

## 1. Actual model, full input class and ENTIRE controller domain

Use the original constant-data scalar-Brownian plant on INFINITY,

    dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW, z=D0x+D1u,

zero initial state/negative external-input history, any fixed finite h>=0, canonical augmented Wiener filtration, and ALL progressive inputs with E integral|w|^2<infinity. Define N1(f)=E||f||_time-L2,N2(f)=(E||f||_time-L2^2)^(1/2), and induced gains G1,G2 on that SAME full input class, in extended-real sense.

Fix ONE deterministic STATIONARY measurable law u=F(x,eta_t), F(0,0)=0, where eta contains finitely many fixed delayed/current taps in[-h,0] together with the Hilbert L2[-h,0] current external-input window. It uses ONLY actual current x and this tuple, with no other controller state, random controller or clock. Require:

- strong nonanticipative well-posedness/nonexplosion and local PATHWISE control L2 for every allowed input/initial state;
- for every state radius R, a finite L_R with

    |F(x,eta)-F(y,eta)|<=L_R|x-y|, |x|,|y|<=R,          (STATE-LOC)

  uniformly for the SAME arbitrary input tuple eta. No input continuity/Lipschitzness is required;
- EXPLICIT actual zero-input/zero-window internal EMS

    E_xi|X_r|^2<=M exp(-lambda r)|xi|^2                 (EMS)

  for every deterministic xi, common M,lambda>0. This is NOT inferred from G1 or admissibility.

All constant matrices and output/control ranks are otherwise arbitrary. Unpriced control channels may have infinite expected path-control norm or squared energy. Expected-L2 control is not silently imposed.

**Theorem 1.** On this ENTIRE law/data domain,

    G2(F)<=G1(F).                                      (LB)

It is an infinite-horizon norm NECESSITY theorem. No finite-horizon ordering, automatic controller regularity, stronger-filtration or arbitrary-controller-memory result is asserted.

## 2. Arbitrary canonical progressive probes can be replayed exactly

Fix ANY compact progressive expected-L2 input v supported on[0,S], b=E||v||^2>0. It need not be bounded/cylindrical or continuous in the input tuple. On canonical Wiener space it has a jointly measurable nonanticipative functional version v_t=Psi_t(W_[0,t]), up to dt-times-probability null equivalence.

One ordinary construction is to approximate the PROCESS for measurability by adapted simple/cylinder functions, use Doob–Dynkin on the stopped Brownian path, then take an almost-everywhere subsequence limit to obtain Psi. This is ONLY a representation of v, not convergence of SDE responses or an input-continuity assumption. Fixed taps preserve dt-times-probability equality under shifts, and Hilbert windows do so by Fubini; strong event locality therefore makes the functional version legitimate even for input-discontinuous F.

At a deterministic start t_i replay Psi on relative Brownian increments W_(t_i+s)-W_(t_i). Strong solution uniqueness and stationarity of data/F identify its zero-state own-window response with the same functional law. For a fixed finite observation length L>S+h, independent relative increment segments give iid reference own-window energies in LAW, even if the deterministic waiting times are unequal.

If v was originally defined by a stopping rule involving its zero-state response, its replay is THAT fixed Brownian functional, not a new stopping feedback recomputed from the ACTUAL block state. This preserves the SAME-input comparison below. No input seed/controller randomization or unexplained enlarged filtration is inserted.

## 3. Bounded energy continuity requires NO forced-state moment

For responses z^xi,z^0 on[0,L] under the SAME probe/future increments and zero external history, put

    Phi_H(z)=min(integral_0^L|z|^2,H), H>0.

Then

    sup_(|xi|<=a) E|Phi_H(z^xi)-Phi_H(z^0)| ->0 as a->0. (C)

Proof: stop both states in radius R. Drift/diffusion DIFFERENCES are A delta_x+B delta_F and A0 delta_x+B0 delta_F; the external forcing cancels. Under(STATE-LOC), these differences are Lipschitz in delta_x with deterministic constants on that ball. The usual stopped Itô/isometry/maximal/Gronwall calculation gives

    E sup|delta_x|^2+E||delta_z||_L2^2<=K_(R,L)|xi|^2.

This does NOT take expectations of either individual unpriced control-noise integral. One may first stop its individual brackets; the DIFFERENCE integrand remains bounded by the state difference, so the estimate is uniform in those additional stops and passes by Fatou.

The reference is nonexplosive. Its probability of leaving radius R/2 before L tends0 with R. While it stays inside, an actual radius-R exit requires a difference at least R/2, controlled by the stopped estimate. Thus the full output converges in probability in time-L2 uniformly as xi tends0. Phi_H is bounded by H and globally2sqrt(H)-Lipschitz in output L2 norm. Taking R large and then a small proves(C), with no global state/output second moment and no input regularity.

Choose, for each fixed n,H, a_n>0 making the supremum in(C)<=1/(2n^2), and let

    d_n=min(1,1/(2H n^2)).

For any past-measurable actual start state xi independent of the fresh increment segment, if P(|xi|>a_n)<=d_n, conditioning gives

    E|Phi_H(z^xi)-Phi_H(z^0)|<=1/n^2.                 (3)

The bad event costs at most H*d_n. There is NO E|xi| or E|xi|^2 premise.

## 4. Weak restart of an ARBITRARY finite-a.s. past distribution

After the external window and delayed forcing clear, the actual law is the deterministic autonomous F(x,0). State-local Lipschitzness, strong well-posedness and nonexplosion give its ordinary deterministic-time transition kernel driven by fresh Brownian increments. This is an ACTUAL restart property of this printed law, not a Markovization of a remote-history map.

For any deterministic xi, Chebyshev and(EMS) give

    P_xi(|X_r|>a)<=min(1,M exp(-lambda r)|xi|^2/a^2).

For ANY past random state zeta finite almost surely, integrate this kernel inequality:

    P(|X_r^zeta|>a)
       <=E min(1,M exp(-lambda r)|zeta|^2/a^2) ->0.    (W)

The convergence is DOMINATED convergence by1, pointwise because zeta is finite almost surely. It remains valid with infinite first AND second moments. No unpriced-control H1, output observability, linearity or mean-zero argument is used.

This is why a state-price occupation estimate is unnecessary for the present EXISTENCE of sequential waits. It was useful in v13 for a quantitative COMMON buffer bound; its correctness is not contradicted.

## 5. Finite prefix-law induction chooses DETERMINISTIC buffers without circularity

Fix n,H,L and the probe. We construct ONE actual compact input containing n copies, with starts t0=0 and t_(i+1)=t_i+L+R_i. Every R_i will be a FINITE DETERMINISTIC integer>=1. It may depend on the fixed controller/probe and prefix DISTRIBUTION, NEVER on a future realized Brownian path or a random stopping wait.

Begin with the first copy and extend its input by0 forever. At its deterministic own end t0+L, the current external window and forcing have cleared because L>S+h. The state zeta0 is finite almost surely by nonexplosion, whether or not it has ANY moment. Its law is now fixed. Use(W) to choose a deterministic integer R0 making the next start probability P(|x(t0+L+R0)|>a_n)<=d_n under this zero-continuation law.

ONLY THEN add the next replayed probe at that deterministic start. Strong causality leaves every earlier state and the selected start probability unchanged. At the next own end, the new prefix already fixes its end distribution. Again continue by0, invoke(W), choose R1, and only afterward add the next probe. Continue this FINITE induction n-1 times.

Thus at every ACTUAL own start the required bad-state probability is<=d_n; the first is exactly0. No uniform end-law/moment bound across blocks is needed. There is no dependence of an already used prefix law on a future buffer choice: future inputs have not begun, and causality preserves the earlier law when they are added. All choices are constants fixed from laws before the resulting input is used, not an experiment that learns future states. Their existence is mathematical, not a launched search or execution.

After the construction, all starts are deterministic; relative Brownian segments on the equal own lengths L are independent/stationary. References therefore retain the SAME iid product law even though the R_i differ and can be large. The actual plant/controller state is NEVER reset. No superposition is assumed.

## 6. Full input/gain proof with exact constant1

If G1=infinity,(LB) is immediate. Otherwise put g=G1<infinity and apply its gain inequality to the just-constructed actual input w_n. Its expected input energy is nb, so

    N1(z(w_n))<=g N1(w_n)<=g sqrt(nb).                 (4)

This global bound includes ALL buffer/tail output. It was not used to choose the waits.

On each own window let A_i^act be actual output energy, A_i^ref its virtual zero-state reference energy. Equation(3) bounds expected absolute difference of their H-truncations by1/n^2. Reference truncations A_i^H=min(A_i^ref,H) are iid in[0,H]; neither actual errors nor within-window input/output energies need be independent.

Pointwise restriction and the square-root difference inequality give

    N1(z(w_n))>=E sqrt(sum_i A_i^H)
       -E sqrt(sum_i|min(A_i^act,H)-min(A_i^ref,H)|)
       >=E sqrt(sum_i A_i^H)-1/sqrt(n).

Their iid average has variance<=H^2/n. Chebyshev plus bounded square roots therefore gives E sqrt(n^-1 sum A_i^H)->sqrt(E A_1^H). Divide(4) and the lower bound by sqrt(n), let n increase, and obtain

    E min(integral_0^L|z(v)|^2,H)<=g^2 b.

The changing n rows need not be nested/coupled: the COMMON iid product LAW is enough. Let H increase and then L increase by monotone convergence. This proves the full RMS output bound for EVERY compact canonical progressive probe, even if its untruncated expectation was initially unknown/infinite.

For an arbitrary infinite expected-L2 input, use its TIME prefix w*1_[0,S]. That is already an allowed compact probe; it is not an input-value approximation. Strong causality identifies its output with the actual one through S. Monotone limits yield

    E integral_0^infinity|z|^2<=g^2 E integral_0^infinity|w|^2

on ALL the stated progressive inputs. This proves(LB), including zero-output/g0 and extended-real cases, without division by a random input norm or unproved input continuity.

## 7. Independent NONSHARP upper bound and the exact level gap

For completeness the ordinary strong-causal upper bound is reproduced, not imported as an unreviewed sharp theorem. If the SAME operator has finite RMS OUTPUT gain<=k, stopped-input consistency implies, for every bounded stopping time tau,

    E X_tau<=E A_tau,
    X_t=integral_0^t|z|^2, A_t=k^2 integral_0^t|w|^2.

Indeed apply the RMS bound to w*1_(s<=tau); its output agrees up to tau and later output energy is nonnegative. The processes X,A are analytical proof variables, not controller states.

Stop at the first X crossing lambda or A crossing delta, also at T. Continuity/increase and the displayed domination give

    P(X_T>=lambda)<=E[min(A_T,delta)]/lambda+P(A_T>=delta).

Set delta=lambda/2. Tail integration of the half moment gives, for fixed a=A_T, the first contribution sqrt(2a) by splitting the integral at lambda=2a, and the second contribution E sqrt(2A_T). Thus

    E sqrt(X_T)<=2sqrt(2)E sqrt(A_T).

Monotone T limits prove G1<=2sqrt(2)G2. The k0 case is immediate. No stationarity, EMS, coercivity or state/control moment inference is needed for THIS upper statement, only the original strong causal stopped-input consistency and RMS bound over ALL allowed inputs.

On Theorem1's domain, therefore,

    G2(F)<=G1(F)<=2sqrt(2)G2(F).

For each fixed law, finite literal OUTPUT gain is equivalent to finite RMS OUTPUT gain, but NOT equality of values or same-gamma sufficiency. Necessary level is G2<gamma; a conservative sufficient level is G2<gamma/(2sqrt2). The external SHARP sqrt2 transfer remains NOT_RECONSTRUCTED/unaccepted by this proof; its optimal constant and optional numerical consequences are not claimed.

Most importantly, G2 here uses the SAME frozen base local-PATHWISE control admissibility. A standard stochastic RMS synthesis/Riccati theorem that assumes EXPECTED-L2 controls cannot be applied to unpriced non-H1 channels without checking that stronger hypothesis separately. This norm theorem does not silently un-scope the old mean-square substitute.

## 8. Relation to the previous domains and the actual remaining original gap

This moment-free sequential proof removes the coercivity and input-regularity premises from the lower cores of v11/v13 under their common STATE-LOC/EMS/current-window hypotheses, and extends v7's global-state-Lipschitz lower core. Those older proofs remain valid weaker/quantitative records; they are not edited or retrospectively promoted. V6's stationary LINEAR theorem without an EMS assumption remains a DIFFERENT domain and is not subsumed unqualified.

The actual v8 indicator law has state-local constant2R, input discontinuity, zero-window EMS and strong nonexplosion, so the norm relation applies despite infinite expected control path norm. This fact neither supplies nor automatically reaccepts v13's SEPARATE h0 gain-infinity stopping application; that application retains its own complete proof/gate. No h>0 global gain verdict for that law is inferred.

The first unproved original step is still SAME-gamma literal sufficiency/optimal printed realization for unmatched stochastic forcing/state-control tradeoffs, outside v12's data matching classes. This operator norm bridge cannot choose or validate a universally optimal linear controller. State-irregular/non-Feller or remote-history laws, larger unexplained filtrations/random controllers, lack of zero-window EMS, finite horizons and the exact pointwise-strict endpoint reading remain outside its claim. No unrestricted finite-dimensional book N&S, priority/SOTA or full scientific solution is asserted.

The new theorem needs its OWN complete source-pinned review/application gate; no old review or domain union certifies it. All arguments are exact WRITTEN symbolic/integer/rational reasoning, not in-kernel checking. No scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/simulation/CLI/nested agent/build/tests/formatter or GO occurred. Own earlier primary approximate-gloss major has ZERO credit and remains permanent with every other finding/HOLD/exposure/clock qualification. Original eighteen owners/cutoff/deadline remain unchanged; no96-hour completion or indefinite park is declared.
