# v166-B reviewer working notes B — v23, v22, v21, v20, v19, v18, v17, v16, v15, v13 addendum, v14, v13, v12

Reviewer PhysicsPPT44-2. Preceding `/bin/date`: Tue Oct 27 05:22:56 PDT 2026. WRITTEN all-variable reconstruction at the sources' own symbols; no Eval/interpreter/calculator/CAS/program/enumeration/checker/solver/replay/CLI/nested agent; no newly chosen probe. Read frontier: parts 9, 10, 11 complete (part9 end S201|269; part10 end S205|345; part11 end S210|276).

## v23 (S198, 276 LF) — fixed linear full-window law, exact N1 dual
- CL product drift re-derived: -f^T Dc X + p^T C w(t-h) + (B^T p + B0^T q)^T M w (S198|159–160). E<f,z> = E int (C^T p)^T w(t-h) + E int b_phi^T M w.
- Window adjunction re-derived by s = t - delta_j and s = t - theta (Fubini): r_raw = C^T p(s+h) + sum L_j^T b(s+delta_j) + int L(theta)^T b(s+theta) dtheta; all indices in [0,T].
- True martingale: bracket root <= sup|X| ||q|| + ||Nc|| sup|p| ||X|| + ||B0|| sup|p| ||Mw||, integrable by S2/H2 Cauchy. PASS.
- §3 E1 bound for the fixed law by stopping w in its own (physical) time: legitimate because the law reads w(s) only for s <= t; same Lenglart domination as v26. PASS.
- §5 BSDE contraction (Ac, Nc): same estimate as v26. PASS. §7 quotient duality PASS. §8 EXACT (two suprema). PASS.
- §9 INF: stop the global input after S, finite horizon T = S + h with counted length S; compares only the prefix through S; correctly avoids a false T-h prefix-dependence claim for a law with direct current-window feed. PASS.
- Source cut: Pardoux–Peng 1990 failed access (ECONNREFUSED/403) = NAMED_NOT_RECONSTRUCTED source, non-load-bearing; Perkowski notes read only to a bounded prefix (sketch) = context only; the needed linear estimate is derived inline. Application: ONE fixed linear law only; no evaluation/synthesis.

## v22 (S199, 232 LF) — monotone continuous Lenglart, G1 <= sqrt2 G2
- MON/TRUNC: X_T ∧ r <= X_tau ∧ r + r 1(A_T >= theta r) with tau the input-energy level stop; identical to my v26 reconstruction. PASS (continuous case fully reconstructed; Geiss–Scheutzow attribution is context, not a premise I verified).
- UP-INF, UP-FIN: DOM from the RMS bound applied to the stopped input + stopped-input consistency. PASS on the stated fixed-law domain (finite RMS output bound; stopped-input consistency).
- 7.1 composition with v14 lower: logical, CONDITIONAL on the v14 domain. 7.2 RISK-UP: storage identity L(P0 X^2) + d^2 X^2 = -d^2 (X - 2cw/q0)^2 + gamma*^2 w^2 re-derived (P0 = 2d^2/q0). PASS.

## v21 (S200, 284 LF) — strict stochastic-risk gap
- MEAN: kappa_rel = ||T_C|| for this uncontrolled family (U = N kerH = {0}, S = 0); deterministic convolution value dc/a via Young and long constant inputs. PASS (consistent with v18/v20 definition of the closed-output relaxation).
- STORE identity re-derived. G2 <= gamma*. PASS.
- RMS lower probes: on the feedback segment X = Y by strong uniqueness; E X^2 growth rate 2ck - q0 = r0; energies (ENERGY) re-derived incl. tail b0 e^(r0 T)/q0; ratio limit d^2(1 + r0/q0)/k^2 = 2cd^2/(q0 k); k ↓ q0/(2c) gives gamma*^2. PASS.
- Common-buffer replay (§6): reference FUNCTIONAL replay; actual-minus-reference = Phi_i xi_i (linearity), E Phi^2 = e^(-q0 t); recurrence E xi_(i+1)^2 <= 2e^(-q0(L+R)) E xi_i^2 + 2 e^(-q0 R) m_L; fixed point 4 e^(-q0 R) m_L; triangle inequality in l2 over own windows; LLN for H-truncated iid energies; limits n, R, H, L in that order. PASS.
- Nonsharp upper 2sqrt2 (Lenglart with delta = lambda/2; half-moment integral sqrt(2a) split at 2a). PASS.
- gamma* = dc/(a - sigma^2/2) > dc/a. PASS. Exact G1 left open by the author (correct).

## v20 (S201, 269 LF) — finite generator of all safe terminal adjoints
- GROUP for deterministic lambda in L = (N kerH)^perp re-derived (drift g^T z + lambda^T C w(t-h), diffusion k^T z). ID, LOW. PASS.
- ITER: linear decreasing chain, fixed point; every ADJ trajectory stays in V (AC derivative in a subspace a.e.; continuity). FRIEND. W0. GEN re-derived: C_d lambda + D_d g = 0 and lambda_dot = A_d lambda + B_d g using the projector E_V E_V^T on V. Surjectivity: g - F_v x ∈ W0 a.e. Injectivity via terminal ODE uniqueness. Bounded inverse ||v|| <= (1 + ||F_v|| C_T) ||g||. PASS.
- FINITE-LOW: generalized eigenvalue of (A_N, B_N) = sup of ||q_g||^2/||g||^2 over R(V_N). PASS.
- DENSE and identification: S*g = (D1^T g - B^T lambda, -E_U^T lambda), T_C* g = -C^T lambda(.+h) re-derived from d(lambda^T x)/dt; K = ker S*; sup = ||P_K T_C|| = kappa_rel. PASS. §8 two-sided comparison CONDITIONAL on v19.

## v19 (S202, 304 LF) — regularized resolvent, compact limit, Hamiltonian
- RES push-through identity, VAL, bounds eta/(eta+||S||^2) <= R_eta <= I, monotone in eta, R_eta >= P_K. PASS.
- STRONG R_eta -> P_K (test a = -b on range S; R_eta^2 <= R_eta). PASS.
- T_C Hilbert–Schmidt (square-integrable kernel on finite rectangle; no direct w term). PASS. Norm convergence on compact image; LIMIT. PASS.
- Hamiltonian: Q, S0, R0, Atilde, Qbar, Bbar; STAT; x_dot = Atilde x - Bbar p + C w(t-h), p_dot = -Qbar x - Atilde^T p re-derived; EIG-OUT (T_C* y)(s) = C^T p(s+h); BVP with H0 on [0,h), H1 on [h,T]; ROOT via p(T) = F22 xi; no spurious root (w = 0 ⇒ a = 0 ⇒ x = p = 0). MAX-ROOT for compact positive K_eta. PASS.
- §6 warning correct: kappa_eta >= kappa_rel is an UPPER approximation, never an original lower bound. DBL illustration: kappa_rel = 0 < kappa_eta. PASS. Application CONDITIONAL on v18 (reviewed below: PASS).

## v18 (S203, 275 LF) — exact closed output relaxation
- GROUP/ID with terminal-only lambda (lambda(0) free because X(0) = 0). H1 lemma as v25. PASS.
- STAR signs re-derived; KER = ker S* exactly. PASS.
- Theorem1 COMP: <g, m(w)> = <g, T_C w> for all g ∈ K ⇒ m(w) - T_C w ∈ closure range S. PASS (deterministic w; Bochner mean; no state/control mean).
- Theorem2 REL-LB ||P_K T_C w|| <= ||m(w)|| <= N1(z(w)); DUAL. PASS. Infinite horizon by prefixes. PASS.
- DBL control: range S ⊃ C_c^inf(0,T) via u = phi''/(dab) (x = phi/d, y = phi'/(da)); zero output for a pulse impossible because y is AC while -(c/a) w(t-h) jumps. PASS.

## v17 (S204, 222 LF) — output-priced scalar adjoint
- PRICE factorization lemma; GROUP; MEAN-ID; LOW (both endpoints zero — subfamily of v18). PASS.
- LIN-P constant-direction tests re-derived; ∫ f f_dot = 0; sine norms L0/2 and pi^2/(2 L0); SINE-P; Gram inequalities. PASS.
- EX family: g0 = (-a/d, beta/e, 0), g1 = (1/d, 0, 0), k0 = (sigma/d, 0, 0) re-derived from LIN-P with the displayed A, B, A0, B0, D0, D1; bound c/sqrt(a^2/d^2 + beta^2/e^2); nonvacuity E int x^2 <= (4c^2/q^2) E int v^2 re-derived. PASS.

## v16 (S205, 345 LF) — the three adopted scopes
- Theorem1: pathwise ID with contracted diffusion identically 0 (A0^T lambda = B0^T lambda = 0); LB-T by the deterministic input w = q_lambda; g = 0 case; infinite horizon by compact tests. PASS (pathwise, no expectation of the unknown control).
- §4 LIN/SINE/DC-ANN/MAT/kappa_ann: as v17 with k0 = 0. PASS.
- Theorem2 FAM: test vectors re-checked against A, B, A0, B0, C, D0, D1 (first rows of A0 and B0 are 0). FIN-LB and DC-ANN. Realizer: dr = -rho r dt + sigma r dW (all drift terms cancel, re-derived), dx = (-p x + beta r + c v) dt, r ≡ 0 from zero state; PERF coefficient identity (d^2 + e^2 j^2)(a^2 e^2 + beta^2 d^2) - d^2 e^2 (a + beta j)^2 = (a e^2 j - beta d^2)^2 re-derived; zero at j = k. EMS: LV <= -p x^2 - q r^2 with L0 = 1 + beta^2/(p q) re-derived. IFF at strict-uniform convention. PASS for EVERY positive tuple and every h >= 0; realizer is a stationary current-state + left-tap law with expected-L2 control.

## v15 (S206, 255 LF) — finite global gain does not price free-channel martingales
- Nonexplosion via psi = log(1 + y^2): L psi re-derived, <= 1 + k|v|. PASS.
- Inverse BES(3): Y = 1/R solves dY = -Y^2 dbeta (Itô re-derived); time change y_t = e^(-bt) Y_(theta_b(t)) re-derived. PASS.
- E Y_s^2 <= 100 q^2: outside/inside split re-derived (inside contribution (2pi)^(-1/2) zeta^(-3/2) e^(-1/(8 zeta)) and r^(3/2) e^(-r) max at 3/2). PASS (I note a sharper ordinary fact E|m + Z|^(-2) <= E|Z|^(-2) = 1 in 3D, not needed).
- E y_t = e^(-bt) q P(|N(0,theta)| <= 1/q) < e^(-bt) q (Newtonian potential). PASS. Hence E(int y^4)^(1/2) = inf (else H1 contradiction). PASS.
- Exact gains kappa = dc/a; pulse energy L - (1 - e^(-aL))/a re-derived. PASS. Zero-start pulse → non-H1 control on every post-interval. PASS.
- Endpoints: energy identity c^2 ||v||^2 = ||x'||^2 + a^2 ||x||^2 re-derived (x(0) = 0, x(∞) = 0); strict pointwise inequality; (22) and (26). PASS.

## v13 window-domain addendum (S207, 11 LF)
- Restricts eta to (Hilbert L2[-h,0] window + finitely many fixed taps); F measurable on the tuple; withdraws arbitrary raw-path-functional reading. Additive, after first pin; mandatory for v13 consumption. Applied below.

## v14 (S208, 173 LF) — coercivity-free G2 <= G1 by prefix-law buffers
- (C): stopped difference estimate under STATE-LOC with the SAME input tuple; Phi_H is 2sqrt(H)-Lipschitz in the output norm. PASS.
- (3): 1/(2n^2) + H d_n <= 1/n^2. PASS. (W): dominated convergence with a.s.-finite zeta, no moments. PASS.
- §5 deterministic buffers chosen from prefix LAWS before the next probe is added (causality ⇒ non-circular). PASS.
- §6: sqrt-subadditivity triangle, E sqrt(sum |diff|) <= 1/sqrt(n), Chebyshev for bounded iid truncations, limits n, H, L; time-prefix extension. PASS.
- §7 nonsharp 2sqrt2 upper. PASS. Domain: stationary measurable F(x, eta), STATE-LOC uniform in eta, F(0,0) = 0, strong well-posedness, zero-window EMS.

## v13 (S209, 246 LF) — dual coercivity occupation buffers + quadratic-law application
- (3) with epsilon_n = min(1, a_n/(2H n^2)) via Markov. PASS. (4) by Jensen. PASS.
- 5A control-price route: vector good-lambda constant 64/7 re-derived (bracket threshold r^2/16); block absorption ||Abar|| delta + 10 ||S|| sqrt(delta) <= 1/2; E|x_end| <= C_L(...). PASS at written level (localization then Fatou).
- 5B state-price occupation: ∫_0^1 E|x(t_e + r)| dr <= c_x g sqrt(nb), integrate the conditional EMS over r. PASS.
- §6 as v14. PASS.
- §7 quadratic law u = -X^2 1(w=0), h = 0: R = 0, Qperp = 1, STATE-LOC 2R, EMS (100 bound), strict mean. PASS.
- §8 G2 = ∞: optional stopping of bounded stopped inverse-BES gives P(sigma_K <= q) >= delta_q/K; K = R e^(aT) ⇒ P(tau_R <= T) >= e^(-aT) delta_q/R; hold lower bound R e^(-a Delta); E int |z_R|^2 >= Delta e^(-a(T + 2 Delta)) delta_q R; bounded input energy. PASS. G1 = ∞ via Theorem1 (state-price route). PASS, h = 0 only (author says so).
- Addendum applied: the h = 0 indicator uses a fixed current tap; unchanged.

## v12 (S210, 276 LF) — visible multiplicative noise, DC matching
- |z|^2 = x^T Q x + |nu|^2 (cross term D0^T D1 + K0^T R = 0). Full mean legitimate (vector H1, 64/7). PASS.
- DC lemma via long flat inputs and |m(t)|^2 <= 2||m|| ||m'||; Cauchy with constant row vectors gives sqrt(y^T G_DC y). PASS.
- Matched class: G_DC D^(-1) C = C under DC-MATCH; ||G_DC^(-1/2) C|| = kappa. Realizer: Bcal Lw = C, B0cal Lw = 0 (FORCE-NOISE) ⇒ homogeneous dx = Ac x dt + Nc x dW; output Gram Lw^T Lw = C^T D^(-1) C. PASS. Global-ORTH stabilizer K = -Bcal^T D^(-1)(Abar + kI) re-derived (Ac = -kI, Nc = S). PASS.
- §6 scalar family and §7 coupled example: Ac = -4I, Nc = [[1,-5],[0,1]], H = diag(1,5): Ac^T H + H Ac + Nc^T H Nc = [[-7,-5],[-5,-10]] re-derived, det 45 > 0. Closed loop and output (0,0,-w_lag,0). PASS.
- Domain cut: MS certificate is a DOMAIN premise (not proved necessary), DC-MATCH/FORCE-NOISE, R, Q, D > 0; infinite horizon; strict-uniform convention.

## Running NAMED (ordinary, not re-proved) list additions
- Scalar/vector BDG-type H1 implication (author's good-lambda proofs re-derived; accepted).
- Inverse-BES(3)/Newtonian potential identities (classical; re-derived at the needed level).
- Canonical Wiener functional representation of progressive processes (Doob–Dynkin); measurable dependence of strong solutions on initial states (transition kernel) used in v13/v14 restarts.
- Pardoux–Peng 1990 (failed access) and Perkowski notes (prefix sketch) are non-load-bearing; the needed linear BSDE estimate is derived.
