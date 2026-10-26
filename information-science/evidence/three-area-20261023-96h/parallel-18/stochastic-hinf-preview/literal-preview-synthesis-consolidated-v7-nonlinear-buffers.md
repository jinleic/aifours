# Exact infinite norm ordering for stationary Lipschitz mean-square-stable NONLINEAR printed laws

**InfoHinfPreview-2 / info-3. ONE immutable WRITTEN successor; OWNER-CANDIDATE / NOVELTY_UNCLEAR.** Actual immediately preceding `/bin/date` observation: **Sun Oct 25 13:31:00 PDT 2026**, a genuine precreation observation bound.

## 0. Genuine nonlinear step and the exact scope restriction

V6 proved G2<=G1 for a fixed stationary LINEAR law by superposition and gliding tails. This successor proves the SAME-level inequality for a specified, much larger NONLINEAR law class, using a DIFFERENT mechanism:

- No nonlinear superposition or physical reset is asserted.
- Long ZERO-INPUT buffers make the ACTUAL state small by an EXPLICIT uniform exponential mean-square stability hypothesis.
- Finite-time Lipschitz comparison bounds the ACTUAL own-window response error against a zero-state reference, under the same input/Brownian path.
- Independent own-window reference energies then give the exact lower constant1.

The data/noise matrices are arbitrary compatible constants, including genuinely VISIBLE and control-dependent multiplicative noise and rank-deficient cost. The hypotheses are on the ACTUAL fixed controller law: stationarity, global Lipschitz regularity and zero-input exponential MS stability are NOT assumed for every admissible book law. No differentiability or linear-optimality premise is used. This is a consequential same-gamma NECESSARY bridge, not unrestricted synthesis or a sufficient controller-realization theorem.

The later exposure ACK `primary-continuation-20261025-102319-ack-addendum-4.json` preceded this body and discloses informal reasoning and the optional boundary import. V6,216LF SHA256 `2acaa6197e3bfe4f1e3607ac5af8a459f3dd5e9d768d2d494fb4d0561b07c6ad`, stays unchanged and owner-candidate; neither source inherits v4/v5's separate union verdict. The core nonlinear proof below is complete at ordinary Brownian/Lipschitz-SDE/measure-theory imports and does not need V6 as a theorem premise.

All v1–v11/HOLD and original October27 cutoff/deadline remain. No scientific interpreter/eval/program, symbolic calculation, enumeration, simulation, solver, replay, CLI, nested agent or actual block experiment was used. Written input/reference constructions are proofs, not executed trajectories or kernel checks.

## 1. Full actual plant/controller/input domain

Work on canonical Brownian space with its completed natural filtration, zero initial state and zero negative input history. The horizon is INFINITE. Independent initial input randomization is allowed by conditioning as stated in §8. The actual plant remains

    dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW,
    z=D0x+D1u, h>=0,

with scalar Brownian W and real constant compatible matrices. No NEO/MATCH/ORTH, cancellation, quotient or D1-rank assumption is made.

Represent the printed current window by a finite set of fixed taps0<=r_j<=h and the Hilbert-window signal w_t(r)=w(t-r),0<=r<=h. Let q_t(w) be that tuple, with norm

    ||q_t(w)||_Q^2=sum_j|w(t-r_j)|^2
                              +integral_0^h|w(t-r)|^2dr.

The fixed controller is one DETERMINISTIC STATIONARY map

    u(t)=F(x(t),q_t(w)), F(0,0)=0,
    |F(x,q)-F(x',q')|
          <=L_x|x-x'|+L_q||q-q'||_Q.                   (LIP)

It uses only actual current plant state and[t-h,t] input; there is no additional controller-memory state. Arbitrary nonlinear and nondifferentiable maps satisfying LIP are included. No unknown feasible controller is assumed replaceable by such a map.

The law gives globally Lipschitz state coefficients with adapted square-integrable forcing, so has the usual strong finite-time solutions, finite second moments and finite-time L2 input continuity. On finite intervals,

    integral||q_t(w)||_Q^2dt
                     <=(number_of_taps+h)integral|w|^2

after zero extension; the plant delay term has the same L2 bound. These estimates are deterministic Fubini/shift inequalities, not a new input space.

The ADDITIONAL actual-law assumption is uniform zero-input stability from every state, with ZERO input window:

    E|X_s^xi|^2<=M exp(-lambda s)E|xi|^2,
    M>=1, lambda>0, s>=0.                               (EMS)

For random past-measurable xi, this follows conditionally from the deterministic-state bound because the zero-input equation is autonomous with fresh independent Brownian increments. Equivalently it may be taken in this random-initial form. It is NOT inferred from zero-state gain or mere strong well-posedness.

Define N1(f)=E||f||_L2(0,infinity), N2(f)=(E||f||_L2^2)^(1/2), and Gp(F) as the induced gain over ALL nonzero progressive inputs with finite expected squared energy. Outputs and gains may initially take extended values.

**Theorem.** Under the exact data/law assumptions above,

    G2(F)<=G1(F).                                       (1)

Thus G1(F)<gamma implies G2(F)<gamma at the SAME prescribed gamma for this class, without a linear-controller assumption. It does not assert the converse.

## 2. Two finite-time estimates, with no derivative of F

Fix an own-observation length L. Coupling two responses with the SAME window input and Brownian path, let delta_x be their state difference. LIP in x gives

    |delta_drift|<=(||A||+||B||L_x)|delta_x|,
    |delta_diffusion|<=(||A0||+||B0||L_x)|delta_x|.

Itô's squared-difference estimate and Gronwall therefore give, for a finite c independent of input amplitude/law,

    E|delta_x(t)|^2<=exp(c t)E|delta_x(0)|^2.

Since `|delta_z|<=(||D0||+||D1||L_x)|delta_x|`, there is a constant C_L<infinity such that

    E integral_0^L|delta_z|^2
                         <=C_L E|delta_x(0)|^2.         (2)

Only Lipschitz DIFFERENCES were used, not differentiation, linearization, an optimal policy or convexity of F.

Global growth from LIP/F(0,0)=0 also gives a finite A_L, independent of starting time, with

    E|x(L)|^2<=A_L(E|x(0)|^2+E integral|v_input|^2)       (3)

when the starting input window is zero and the supplied input is supported within the interval. Standard localization/Itô/Young/Gronwall with the q-shift bound proves(3), including the finite-time input-continuity estimate. No fourth moments are required. We use these ordinary finite-time second-moment facts, never an unproved infinite incremental-stability theorem.

## 3. Replayable templates and an ACTUAL small-state induction

If G1=infinity, (1) is immediate. Suppose g=G1<infinity. First choose a nonzero bounded canonical Brownian-cylinder adapted step template v, supported on[0,S], and fix L>S+h. These templates are dense in canonical progressive L2 on each finite interval. Put

    b=E integral_0^S|v|^2>0,
    a=E integral_0^L|z_v|^2<infinity.                    (4)

For each n choose a deterministic R_n>0, as large as necessary, so

    M exp(-lambda R_n)A_L(1+b)<=n^(-2).                 (5)

Set H_n=L+R_n and t_i=iH_n, i=0,...,n-1. Replay the same input functional in[t_i,t_i+S] using W(t_i+s)-W(t_i). Between probes the ACTUAL input is zero. Each copy is progressive; the sum has compact support and expected squared energy n b.

Let xi_i be the ACTUAL state at t_i, not a reset state. Initially xi_0=0. If E|xi_i|^2<=n^(-2), estimate(3) bounds the actual state at t_i+L by A_L(1+b). Because L>S+h, the old input WINDOW and the plant's delayed forcing are ALREADY ZERO there. Over the buffer R_n the actual nonlinear controller operates as F(x,0); its state and output remain physically present. Conditional EMS and(5) yield

    E|xi_(i+1)|^2<=n^(-2).

Induction proves this for EVERY probe start. The buffer lengths are deterministic choices based on constants/template moments, not actual future realizations or random stopping rules. No exact state reset, controller-memory reset or undeclared forgetting hypothesis occurred: the required forgetting was ASSUMED as EMS and quantitatively applied after the actual window cleared.

## 4. Independent references, proved nonlinear error and the exact constant

For comparison only, let Y_i be the output of a ZERO-state/zero-window reference run under the same F, same own input v_i and same Brownian increments on I_i=[t_i,t_i+L]. These reference runs are not substituted into the physical trajectory. Stationarity and independent disjoint increment windows make

    A_i=integral_(I_i)|Y_i|^2

iid with mean a. Their joint law in every n construction is the fixed product law, even though H_n varies with n. Input energies B_i have mean b; correlation of A_i,B_i inside a block is allowed.

The actual input window on I_i equals the reference input window: all earlier inputs cleared before t_i and the next copy starts after t_i+L. Estimate(2) and the ACTUAL state bound therefore give

    E integral_(I_i)|z_actual-Y_i|^2<=C_L/n^2.            (6)

On the union of disjoint I_i, the error energy adds. No independence of these errors is needed. Let R be restriction to that union and Yideal=sum_i1_(I_i)Y_i. Then

    N1(R z_actual-Yideal)
       <=(sum_i E integral_(I_i)|z_actual-Y_i|^2)^(1/2)
       <=sqrt(C_L/n).

Thus, with every buffer output/state still present outside the observation mask,

    N1(z_actual)>=E sqrt(sum_i A_i)-sqrt(C_L/n).          (7)

There is NO nonlinear superposition identity in this proof. Equation(7) follows from a proved same-input/same-noise initial-state comparison. This is the step that v6's linear argument could not simply assume for arbitrary nonlinear laws.

Apply the ORIGINAL literal gain to the actual composite input and upper-bound its actual N1 input by Jensen:

    E sqrt(sum_i A_i)-sqrt(C_L/n)
        <=g E sqrt(sum_i B_i)<=g sqrt(n b).             (8)

For completeness, independent truncated A_i wedge M have common mean mu_M and variance<=M^2. Chebyshev gives, for0<delta<mu_M,

    E sqrt(n^(-1)sum_i A_i)
       >=sqrt(mu_M-delta)*(1-M^2/(n delta^2)).

First n->infinity, then delta->0, then M->infinity yields liminf>=sqrt(a). No fourth moments, physical trial, sign enumeration, ergodic theorem or nesting of the varying-buffer rows is needed. Divide(8) by sqrt(n); its error is sqrt(C_L)/n. The limit gives

    a<=g^2 b.                                           (9)

The coefficient is EXACTLY1. Jensen was only a valid upper estimate inside this constructed-input argument; it was not a replacement of the stochastic objective or a standalone ratio comparison.

## 5. ALL progressive inputs and extended gains

Joint LIP and the finite q-shift estimate give finite-time L2 continuity of the nonlinear input/output map. Approximate an arbitrary canonical progressive input supported on[0,S] by bounded cylinder templates. Inequality(9) passes to that input for every L>S+h and hence every shorter observation interval. Increase L by monotone convergence to get the mean-square bound for every compact input.

For a general progressive input with finite expected squared energy on[0,infinity), truncate it at finite S. Strong causality gives the SAME response through S. Apply the compact-input bound, whose input energy is no greater than the original total energy, then increase S. This proves

    E integral_0^infinity|z|^2
                      <=g^2 E integral_0^infinity|w|^2.

Taking the supremum gives G2<=g=G1. If G2=infinity and G1 finite, the displayed bound is impossible; if G1=infinity the theorem was immediate. The G1=0 or zero-template-output cases cause no division by an output norm; b>0 is the only denominator. Thus all extended-real boundary cases are included.

Independent initial INPUT randomization can be conditioned out: for almost every fixed seed, the same deterministic law and canonical operator inequalities apply; integrate conditional N1 or squared-energy bounds. Seed-free inputs give the reverse inclusion. This does not cover extra random controller coefficients, an unexplained enlarged filtration or nonstationary F.

## 6. A genuine nonsmooth nonlinear/control-noise domain example

To show this is not merely linear algebra in disguise, take scalar data

    A=-5, B=C=A0=B0=1,
    z=(x,u), u=-sat(x),
    sat(x)=max(-1,min(1,x)),

with ANY h>=0. F is stationary, globally1-Lipschitz, nonlinear and NONDIFFERENTIABLE at ±1; it ignores rather than enlarges the printed window. Both drift and diffusion control are effective. The actual noise is `(x-sat(x))dW`, genuinely nonzero for |x|>1. With z=(x,u), K0=0,Q=1, so full/visible MATCH fails and no unobservable quotient hides this noise.

For zero external input, the actual squared-state generator is

    -10x^2-2x*sat(x)+(x-sat(x))^2<=-9x^2,

because x*sat(x)>=0 and |x-sat(x)|<=|x|. This proves EMS with M1,lambda9 from every initial state. With forcing w(t-h), Young gives generator<=-8x^2+|w(t-h)|^2. Since |u|<=|x|, integrating gives the ordinary mean-square upper bound G2<=1/2. The retained generic causal sqrt2 transfer would also give finite G1<=1/sqrt2 at its SEPARATE old classical-import boundary; that upper-transfer assertion is not needed for the proof of(1).

This written example calibrates a nonempty generic-visible-noise nonlinear domain and its actual stability. No sharp gain, new universal controller, numerical threshold or novelty claim is extracted from it. Its matrix/inequality arithmetic was not evaluated by a program.

## 7. Stationarity is substantive: a precise CLOCK-dependent boundary control

The proof cannot just be applied to time-dependent laws: late reference windows would no longer have the same response law. The following optional boundary illustration makes the limitation exact, using the NAMED already supported unit-cascade Gaussian-gap lemma from `literal-preview-separation-consolidated-v2.md`, SHA256 `d1e367cff5a4098c60bd0e44226eec72b7c91ce7a69c538c1b680fc043e22173`, renewed reads RAW53–95/253–285. The core theorem above does NOT depend on this import.

Keep a CONSTANT-matrix plant with h1 and two states:

    df=(1/2)(-f+w(t-1))dt,
    dy=-(1/4)y dt+f dW,
    B=B0=0, D0=0, D1=1, z=u.

Enlarge the controller class explicitly to allow an external deterministic CLOCK on the infinite horizon, and take

    u(t)=1_[0,2](t)*y(t).                               (GATE)

This is a linear, uniformly Lipschitz, internally exponentially MS-stable closed loop; control does not affect the state. Its zero-input storage2f^2+y^2 has expected derivative `-(1/2)E(2f^2+y^2)`. Yet its output is exactly the old short-horizon response on[0,2], depending ONLY on w on[0,1]. The named unit lemma gives gains ell,m with

    ell<=(1-1/18432)m<m, m^2>=1/384.

For the infinite counted input norm, adding a tail after1 changes no output and only enlarges the denominator. Compact inputs on[0,1] supply the converse. Therefore the FIXED clock-dependent law has G1=ell and G2=m, so G1<G2 despite uniform Lipschitz regularity and internal MS stability.

This is a counter to an UNQUALIFIED extension to clock-dependent laws, NOT an admissible realization under a stricter stationary reading of the book's F. It introduces no claimed energy-memory implementation, no new rational endpoint campaign, no sharp evaluated m and no original synthesis counterexample (u0 would give zero output in this artificial performance arrangement). The example simply shows why stationarity cannot be silently inferred or removed. The old finite Gaussian proof, not an interpreter or this comparison theorem, supplies its strict gap.

## 8. Exact synthesis meaning and ENTIRE original residual

For any actual stationary law satisfying LIP/EMS, literal feasibility at gamma implies mean-square feasibility at the SAME gamma. No linear-optimality assumption is involved; the law may be genuinely nonlinear and nonsmooth. This is a generic-noise NECESSARY level bridge, not a SAME-level sufficiency theorem. The old sqrt2 upper transfer remains separate; no G1=G2 is asserted.

The original primary still permits laws not known to satisfy these quantitative hypotheses. Strong well-posedness alone is NOT asserted to imply global Lipschitz comparison, uniform EMS forgetting or stationarity. Consequently the following remain OPEN:

- Unrestricted admissible nonlinear/current-window synthesis and the necessity of such regularity/forgetting assumptions for a feasible law.
- A sharp SAME-gamma sufficient operator/storage/controller-realization criterion on generic visible-noise data; a mean-square controller at gamma is not automatically a literal controller at gamma.
- Arbitrary clock-dependent/nonstationary laws. The boundary example warns that even the norm ordering may fail there; no whole-class exclusion follows from a stationary theorem.
- Fixed finite horizons, where arbitrarily many long zero-input buffers do not fit and known opposite-direction separating examples remain valid.
- Internal stabilization/feasibility outside the actual EMS hypothesis, and general rank-deficient-cost synthesis despite the rank-free comparison theorem.

A proof removing these hypotheses must supply an actual finite-time small-state/input comparison or a different representation, not invoke a physical reset, hidden energy-history law, differentiability or linear optimality without proof. No full arbitrary-plant N&S, stationary-optimum theorem, full-book resolution or novelty clearance is delivered.

## 9. Named imports and evidence ceiling

Ordinary imports are canonical Brownian independent stationary increments and conditional future independence; globally Lipschitz SDE strong uniqueness/finite-time second-moment/continuous-dependence estimates; bounded cylinder/simple-input density in progressive L2; Itô localization, Gronwall/Young, Jensen, Chebyshev, dominated/monotone convergence. The actual zero-window clearing, random-initial EMS conditioning, deterministic-buffer induction, nonlinear same-input error, iid reference law, vanishing measurement error and full-input passage have their operative proofs above. No derivative of F, unknown optimal controller theorem, nonlinear superposition, RDE/Hamiltonian, infinite inverse, v4/v5 union acceptance or external probability sharp constant is a premise of the CORE theorem.

The optional finite-Gaussian GATE boundary retains its NAMED v2 lemma; the optional G1 upper bound in the saturation example retains the separate causal Lenglart transfer. They are not newly certified from hashes or used to prove(1). All new claims remain OWNER-WRITTEN CANDIDATES pending complete source/required-import reconstruction and parent disposition. Neither v6 nor v4/v5's no-defect reports supply an automatic verdict for this new nonlinear proof.

No scientific eval/interpreter/program/arithmetic/symbolic enumeration/physical reset/trial/simulation/solver/replay/compile/CLI/nested agent or new GO occurred. All frozen predecessor bytes remain unchanged. No formal/kernel/human/configured-family/executable/novelty acceptance, continuous18-way runtime or round completion follows. Original October27 cutoff/deadline and v1–v11/HOLD remain binding.
