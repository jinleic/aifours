# Infinite-horizon literal gain dominates RMS gain for every fixed stationary linear preview law

**InfoHinfPreview-2 / info-3. ONE immutable WRITTEN successor; OWNER-CANDIDATE / NOVELTY_UNCLEAR.** Actual immediately preceding `/bin/date` observation: **Sun Oct 25 13:14:53 PDT 2026**, a precreation observation, not an invented exact completion time.

## 0. New delta and non-widened target boundary

The earlier stationary-linear reverse bound was `G2/sqrt(3)<=G1`. It remains true and unchanged. This manuscript proves the SHARPER SAME-level inequality

    G2(F)<=G1(F)                                         (NEW)

on the INFINITE horizon for every fixed deterministic time-homogeneous linear current-state/fixed-window law below, for ARBITRARY constant plant matrices and multiplicative noise. No NEO, cancellation, visible-quotient, control-cost rank or internal-stability assumption is imposed. Inputs remain ALL square-integrable progressive Brownian inputs, not deterministic only.

The new representation is a GLIDING-BUFFER/disjoint-observation-window argument. Finite G1 gives small far-output tails in N1; long deterministic buffers isolate iid own-window energies, while every actual old tail remains in the physical plant and is bounded, never reset. It removes the sign-inequality loss sqrt3 without assuming G2 finite.

This is a consequential NECESSARY level bridge on a DECLARED controller class, NOT general nonlinear synthesis, a linear-optimality assumption, a finite-horizon theorem, G1=G2 or a sufficient controller-realization theorem. The exact original gap is §10. The proof is self-contained at the ordinary Brownian/linear-SDE/measure-theory imports listed below and does NOT depend on v4/v5's quotient/Riccati result.

The separate later exposure ACK `primary-continuation-20261025-102319-ack-addendum-3.json` preceded this body. It discloses informal gliding-buffer reasoning and the full earlier comparison lead. Actual v85-C was returned before resumption. No preregistration or blind-discovery claim is made.

The earlier `proof-v1.md` is unchanged, SHA256 `895a36cdc42565aa7b7b6fd4279a34aba6b3bb7f0c8918d14e49d59b72f5635c`; renewed actual reads were COMPLETE RAW1–31 and132–225, not a whole-file reread inferred from its hash. Its finite-sign proof deliberately did not assert sharpness. The new proof below does not import that lower bound as a premise. Its separate sqrt2 upper transfer keeps its own classical probability/import boundary.

All v1–v11/HOLD, source/clock/artifact corrections and original October27 cutoff/deadline remain binding. No scientific interpreter/eval/program, symbolic arithmetic, enumeration, simulation, matrix/ODE solve, replay, CLI or nested agent was used. Abstract input copies/partitions below are a WRITTEN proof construction, not executed trials or a scientific child.

## 1. EXACT plant, controller, filtration and gains

Use the actual constant-data plant with h>=0,

    dx=(Ax+Bu+Cw(t-h))dt+(A0x+B0u)dW,
    z=D0x+D1u,

zero initial state and negative input histories. W has its completed NATURAL Wiener filtration. Independent initial input randomization is permitted by the extension in §8. A general larger filtration is not silently substituted for this specified replayable class.

Fix ONE deterministic time-homogeneous LINEAR law of the printed information form

    u(t)=Kx(t)+sum_(j=1)^m J_j w(t-r_j)
                     +integral_0^h H(r)w(t-r)dr,
    0<=r_j<=h, H∈L2(0,h).                               (1)

All matrices, taps and kernels are fixed, not random or changed between probes. This includes static feedback and genuine preview feedforward relative to the delayed plant forcing. It uses only current x and[t-h,t] input. No hidden controller memory or energy accumulator is added.

Closed-loop finite-time strong well-posedness, zero response, causality and input/output LINEARITY hold for these linear-SDE coefficients and bounded finite-window operators. The kernel is L1 on the finite interval by Cauchy–Schwarz. The finite-time map is continuous from mean-square input energy to mean-square output energy, by ordinary linear-SDE isometry/Gronwall estimates. These statements require NO infinite-horizon stability or full-rank D1.

For I=[0,infinity), define

    N1(f)=E(integral_I |f|^2)^(1/2),
    N2(f)=(E integral_I |f|^2)^(1/2),
    Gp(F)=sup_(w!=0) Np(z_F,w)/Np(w), p=1,2.             (2)

The supremum is over ALL progressive inputs with finite expected squared energy. Gains take values in[0,infinity]. A finite zero-state output gain does not assert internal stability of unobservable modes.

## 2. The theorem and the only nontrivial case

**Theorem.** For every actual constant plant and fixed law(1), on the stated canonical infinite-horizon input class,

    G2(F)<=G1(F) in the extended nonnegative reals.       (3)

If G1=infinity, the inequality is immediate. Assume now

    g=G1(F)<infinity.

We will prove the RMS bound for every input with the SAME constant g. In particular G2=infinity cannot occur with finite G1. No G2-finiteness or mean-square tail bound is assumed in this proof.

It suffices first to use a nonzero bounded Brownian-CYLINDER adapted step template v, supported on[0,S]. Its coefficients are bounded Borel functions of finitely many past Brownian samples. Such templates are dense in canonical progressive L2 on each finite interval. Density is used only with the already available FINITE-time linear-SDE continuity, not an assumed infinite-horizon continuity.

Let Y be the FULL zero-state output to v. Since g is finite,

    E||Y||_L2(0,infinity)<=g E||v||_L2(0,S)<infinity.      (4)

Consequently Y belongs to time-L2 almost surely and its tail norm satisfies

    tau(a):=E||Y||_L2(a,infinity) ->0 as a->infinity.     (5)

This is dominated convergence, with integrable dominator ||Y||. It is NOT a conclusion about E||Y||^2 and introduces no circular mean-square assumption.

Fix any finite own-observation length L>S+h. Set

    B=integral_0^S |v|^2, A=integral_0^L |Y|^2,
    b=E B>0, a=E A<infinity.                            (6)

Finite-time SDE estimates supply the last finiteness.

## 3. Legal iid copies with long DETERMINISTIC buffers

For each positive integer n, choose a deterministic H_n>L+h with

    tau(H_n)<=1/n.                                      (7)

Such a finite buffer exists by(5). It depends on the LAW of one template response and n, never the realized future Brownian path. It is therefore not an anticipative stopping rule or a computed simulation prescription.

Put t_i=iH_n, i=0,...,n-1. In[t_i,t_i+S], replay the SAME template functional using the relative Brownian samples

    W(t_i+s)-W(t_i), 0<=s<=S.

Call that input v_i; it is progressive for the ORIGINAL global Brownian filtration, with zero input elsewhere. Its finite support/energy is legal. Let Y_i be the FULL zero-state component output to v_i, driven by the SAME global Brownian motion as all components.

Before t_i, Y_i and its state are zero because that component has zero input/history and the fixed law is zero-preserving. On the own window I_i=[t_i,t_i+L], its response is a deterministic causal functional of the fresh Brownian increments in THAT window. Constant coefficients and time-homogeneity make it have the same law as Y on[0,L]. Different own windows use disjoint Brownian increment intervals, so

    A_i=integral_(I_i)|Y_i|^2

are iid copies of A. Likewise input energies B_i are copies of B. Dependence between A_i and B_i inside a window is allowed. NO independence of the FULL overlapping tails is asserted.

Although the deterministic buffers may vary with n, every row has the SAME iid product law of these fixed energies. The later averaging argument is a statement about this fixed law, not a claim that different n constructions form a nested independent sequence on one Brownian path.

## 4. The ACTUAL plant is never reset; all tails have a controlled error

Take the actual admissible input

    w_n=sum_(i=0)^(n-1) v_i.

Supports are disjoint, so `E integral|w_n|^2=n b<infinity`. Input nonanticipativity and expected-energy admissibility hold for every finite n. Infinite waiting gaps do not have a cost, but every chosen gap is FINITE; each w_n has compact support.

Linearity under the SAME Brownian path gives exactly

    z_(w_n)=sum_i Y_i.                                  (8)

This includes the physical old state and every response tail. The actual plant is not reset or switched to independent physical trajectories. Virtual component decomposition follows from Itô linearity and strong uniqueness for the one fixed closed-loop law.

Let R_n be restriction of output to the UNION of disjoint own windows I_i, and define the ideal window vector

    Z_n^ideal=sum_i 1_(I_i)Y_i.

Its path energy is exactly sum_i A_i, since its time supports are disjoint. Future components vanish on earlier windows. Thus the ACTUAL restricted error is

    R_n z_(w_n)-Z_n^ideal
       =sum_i 1_(union_(j>i)I_j)Y_i.                    (9)

For each i the indicated future part lies after relative time H_n. Its N1 norm is at most tau(H_n), by stationarity of that component's FULL law. It may be arbitrarily correlated with later inputs/outputs; no independence is used in this error estimate. Triangle inequality and(7) give

    N1(R_n z_(w_n)-Z_n^ideal)<=n*tau(H_n)<=1.            (10)

Restriction only decreases the path-L2 norm, so

    N1(z_(w_n))>=E sqrt(sum_i A_i)-1.                   (11)

Discarding UNOBSERVED buffer intervals in this LOWER bound does not delete their state or output from the physical plant; their later effects are exactly the terms in(9).

## 5. Averaging with no fourth moment or sign loss

The literal gain bound and the ACTUAL input norm give

    E sqrt(sum_i A_i)-1
       <=N1(z_(w_n))<=g N1(w_n)
       =g E sqrt(sum_i B_i)<=g sqrt(n b).               (12)

Jensen is used only for this valid UPPER estimate of a constructed input norm. It does not replace the book objective or by itself compare a random denominator. The infinite-window construction supplies the missing output average.

For completeness the required iid averaging LOWER limit is elementary. For M>0 let mu_M=E(A wedge M). The independent bounded A_i wedge M have variance at most M^2. For0<delta<mu_M, Chebyshev gives

    E sqrt(n^(-1)sum_i A_i)
       >=sqrt(mu_M-delta)*(1-M^2/(n delta^2)).          (13)

The right side may be negative for small n, harmlessly. Let n->infinity, then delta->0, then M->infinity. Monotone convergence gives

    liminf E sqrt(n^(-1)sum_i A_i)>=sqrt(a).             (14)

If a=0 it is immediate. No variance/fourth moment of A, full-output second moment, strong law/ergodic theorem, physical sample average or sign enumeration is needed. Rowwise iid law is enough even though H_n varies with n.

Divide(12) by sqrt(n), use(14), and obtain

    a<=g^2 b.                                           (15)

The coefficient is EXACTLY1, not1/3, because disjoint own windows are orthogonal in TIME and old tails were made negligible using finite G1. There is no Hilbert-sign inequality to lose a factor.

## 6. Dense input extension and the FULL extended-real G2

Inequality(15) holds for every bounded cylinder template and every L>S+h. Approximate an arbitrary progressive L2 input supported on[0,S] by those templates in expected squared input energy. The finite-time linear-SDE map is continuous in that norm, so (15) passes to that arbitrary input for every such finite L. Smaller observation intervals are bounded by these larger ones. Thus every compactly supported adapted input has

    E integral_0^L|z|^2<=g^2 E integral_0^S|w|^2

at every finite observation horizon, and then on infinity by monotone convergence.

For an arbitrary square-integrable input on[0,infinity), truncate it at any finite S. Causality makes its response identical to the original through S. Apply the compact-input inequality to an observation interval covering that prefix; the truncated input energy is no larger than the original total input energy. Increase S and use monotone convergence:

    E integral_0^infinity|z_w|^2
        <=g^2 E integral_0^infinity|w|^2.                (16)

No infinite-horizon continuity is presumed; this is where it is proved at the output-energy level. Taking the supremum gives G2<=g=G1. If G2 were infinite, assumption G1 finite would contradict(16); hence all extended-real cases are covered. This proves the theorem.

## 7. SAME-gamma necessity and exact synthesis limitation

For EVERY fixed law(1),

    G1(F)<gamma =>G2(F)<=G1(F)<gamma.                    (17)

It is a SAME-level NECESSARY condition at the requested gamma for this class, including arbitrary VISIBLE multiplicative noise and rank-deficient control cost. There is no NEO/MATCH/ORTH or hidden-stability hypothesis here, because this is a transference result about a fixed linear input/output map, not a new Riccati realization theorem.

If g_p^lin denotes the infimum over the SAME stationary linear class, then `g_2^lin<=g_1^lin`. Therefore mean-square infeasibility at gamma inside that class rules out literal feasibility at gamma inside that class. The earlier sqrt3 exclusion loss is removed. The older separate sqrt2 upper-transfer theorem, at its retained Geiss–Scheutzow scope, is not sharpened here and supplies no same-gamma sufficiency. The separately supported long-direction separating family also remains consistent with a STRICT inequality G1>G2; no norm equality is asserted.

This is NOT a theorem that a general nonlinear/time-dependent printed law can be replaced by(1). Such a replacement would be the very missing linear-optimality/realization theorem; it is not inserted as an assumption about the registered primary.

## 8. Input randomization and precise replay boundary

The proof used only canonical Brownian cylinder probes, no added random signs or seeds. They are dense in the canonical square-integrable progressive class. If an independent initial input seed is allowed, condition on that seed: for almost every fixed seed the deterministic coefficients/law give the same canonical input/output operator and its inequalities. Integrating the conditional bounds shows that independent initial randomization enlarges neither norm; seed-free inputs already give the reverse inclusion. Thus the theorem retains the old optional independent-initial-randomization convention.

No general transfer from an arbitrary enlarged filtration with unexplained nonreplayable additional information is claimed. No extra CONTROLLER randomness or random/time-varying controller coefficients are covered by this deterministic stationary theorem. Brownian stationarity, independence of disjoint increment windows, deterministic coefficients and finite-time causality are the precise mechanisms used.

## 9. Actual source, proof and verification ceiling

The earlier proof-v1 TheoremB is an exposed lead with a weaker deliberately nonsharp sign bound; it is neither edited nor withdrawn as false. This new proof uses an additional implication available under G1finite: integrable FULL-output tails decay, permitting deterministic gliding buffers. That implication is proved BEFORE using output averaging, so there is no hidden G2-finite premise or circular global stability argument.

Ordinary named imports: canonical Brownian independent/stationary increments, measurable bounded cylinder/simple-input density in progressive L2, finite-time linear-SDE strong uniqueness/linearity/second-moment continuity, triangle/restriction/Jensen inequalities in time-L2, dominated and monotone convergence, bounded-variable Chebyshev. The decisive component law, correlated-tail estimate, denominator bound, averaging and full-input passage are displayed above. No Riccati/Hamiltonian theorem, v4/v5 acceptance, stochastic BRL, ergodic theorem, controller-reset result, sampled experiment or probability sharp-constant result is imported.

No scientific interpreter/eval, simulation, program, finite sign/window enumeration, solver or replay was executed. None of H_n, n copies, expectations or limits was evaluated in a kernel. This is owner-WRITTEN candidate mathematics pending fresh full-body reconstruction and parent disposition, not formal/kernel/human/configured-family/executable/novelty acceptance. The actual297LF v85-A union review of DIFFERENT v4/v5 results was read completely (sole cutline35 recovered); its0F/0M/0m does NOT certify this new transference theorem. All later exposure is recorded before this body, not backdated.

## 10. ENTIRE remaining original problem

The book primary is STILL general prescribed-gamma literal N1 synthesis with arbitrary actual constant matrices, full admissible printed laws and both horizons. This theorem advances a generic-noise NECESSITY direction ONLY for a named stationary-linear infinite-horizon law class.

STILL OPEN here:

- General nonlinear/nonstationary/current-window synthesis and a controller-realization bridge at the SAME gamma. No linear optimality is proved.
- A SAME-level sufficient criterion on generic visible-noise plants. G2<=G1 does not give G1<=G2 or convert a mean-square controller directly at gamma.
- Any finite-horizon version. The arbitrarily many long buffers do not fit a fixed finite horizon; existing opposite-direction finite separating examples remain valid.
- Internal mean-square stabilization from arbitrary nonzero states. The theorem is zero-state input/output and says nothing about unobservable unstable modes.
- Norm equality, sharp literal optimum or novelty. Time-varying coefficients and nonlinear laws do not satisfy the required stationary replay/superposition argument.

The exact next nonlinear obstacle is quantitative decoupling of repeated probes WITHOUT linear superposition and WITHOUT an unproved forgetting/continuity/reset assumption. The physical no-reset proof above cannot simply be repeated for a nonlinear law. New general research must address that realization/visible-noise gap, not call this controller-class comparison a book solution. Original October27 cutoff/deadline and v1–v11/HOLD remain binding; the round is not completed by this source.
