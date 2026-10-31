# v166-B reviewer working notes A — process parts 1–7 complete; bodies v26, v25, v24 (part8 complete)

Reviewer PhysicsPPT44-2 (slot physics-3). Assignment v166-B (author InfoHinfPreview-2). Preceding `/bin/date`: Tue Oct 27 05:10:53 PDT 2026. WRITTEN reviewer notes only; no Eval/interpreter/calculator/CAS/program/enumeration/checker/solver/replay/CLI/nested agent; no newly chosen state/control/parameter/boundary/limit/magnitude/decimal probe. Every reconstruction below is all-variable, at the source's own symbols. Working notes, not the review; the review will be `peer-review-v166-B-v1.md`.

## 0. Read frontier at this note

- Parts 1–7 (S1–S194) read completely through every ending, serially. Part 6 end S169|23; part 7 end S194|41.
- Part 8 (S195 v26 308 LF, S196 v25 348 LF, S197 v24 219 LF) read completely through `END OF COMPLETE v26.` / `END OF COMPLETE v25.` / S197|219.
- Process records relevant to the author's assurance that I have now read inside scope: S160 (v152, TWO author blocked cadences 33m09/31m47; 900 s wrapper proposal withdrawn), S172 (v161, author whole-75 ACK read), S188 (v179 parent service gap), S193 (v182: NEW post-material-STOP self-release control-method PROCESS MAJOR; 624 LF v163-A-v1 ACTUALLY RETURNED but HELD/not adopted; entire post-checkpoint-83 self-released assessment and consuming guidance ZERO; five authored Olson artifacts v31A/v55B/v60B/v65C/v83B).
- Main process observation 113 (05:06:37) received as CAPTION ONLY; record 113 NOT opened; it is not a body release, scope change or cadence waiver.

## 1. v26 (S195) — reconstruction

1. (E1-BOUND) N1(z) <= sqrt(2) K_T N1(j). Reconstructed: for a bounded stopping time tau, the input j·1[0,tau] is progressive E2 and by pathwise uniqueness its output agrees with z on [0,tau]; hence E Y_tau <= K_T^2 E int_0^tau |j|^2 = E A_tau (domination of Y by the continuous adapted increasing A). With sigma = inf{t: A_t >= theta r} ∧ T: on {A_T < theta r} sigma = T, so E(Y_T ∧ r) <= E Y_sigma + r P(A_T >= theta r) <= E(A_T ∧ theta r) + r P(A_T >= theta r) (continuity of A gives A_sigma = A_T ∧ theta r). Fixed V>=0: int_0^inf (V∧r) r^(p-2) dr = V^p/p + V^p/(1-p), so E V^p = p(1-p) int E(V∧r) r^(p-2) dr. Substituting s = theta r: first term gives theta^(1-p) E A_T^p; second gives p(1-p) theta^(-p) int s^(p-1) P(A_T>=s) ds = (1-p) theta^(-p) E A_T^p. Factor theta^(-p)(theta+1-p); theta=p gives p^(-p); p=1/2 gives sqrt 2. With Y_T^(1/2)=||z||, A_T^(1/2)=K_T||j||. PASS (Lenglart-type domination, fully reconstructed).
2. E1 closedness/density of E2 by own-energy stopping: PASS (ordinary).
3. MAPS: restriction v(t)=w(t-h) is progressive and isometric; T_C bounded by the same constant. The stopped-domain remark is correct: the enlargement is only used for an operator bound. PASS.
4. SUPPORT: Hahn–Banach on the quotient, extension to L1(Omega;Hout), L1(Omega;H)* = Linf(Omega;H) for separable Hilbert H (coordinate RN sketch). PASS at ordinary-foundation level (NAMED ordinary; the coordinate argument is standard).
5. BSD existence/uniqueness: a-priori estimate re-derived (Itô on e^(beta t)|p|^2 gives E int e^(beta t)[(beta/2)|p|^2+|q|^2] <= (2/beta) E int e^(beta t)|F|^2); with |dF|^2 <= 2||A||^2|dp|^2 + 2||A0||^2|dq|^2 the squared factor is <= 8||A||^2/beta^2 + 4||A0||^2/beta. PASS (uses NAMED canonical ONE-Brownian scalar MRT).
6. PAIR: Itô drift re-derived: d(p^T X) drift = -f^T D0 X + (B^T p + B0^T q)^T u + p^T C v, matching S195|152; true martingale by sup|pX| integrable (S2×S2) and integrable drift; projection of phi onto progressive f against progressive z ∈ L2(dt dP); delay shift. PASS.
7. Annihilator IFF b_phi = 0 (test u = b_phi ∈ E2; density of E2 in U; S bounded). PASS.
8. nu duality and EXACT-RISK (two suprema commute; no minimax). PASS.
9. CP bridge §5: u = Jz pathwise; own-control-energy stopping u_R; pathwise uniqueness identifies reference and actual through tau_R; tau_R = T eventually on each path (countable R); L1 limit vs a.s. eventual equality → z = T_C w + S u in Zout. PASS. CP-NEC finite and infinite (zero-extended inputs, prefix comparison). PASS. This applies to every progressive control process, hence to every original printed law with finite N1 output, under CP only.
10. §6 closed complemented range: JS = I_U, J T_C = 0 by E1 continuity; SJ projection; P0 = I - SJ projection onto ker J along range S; OUTPUT-ID P0 z = T_C w re-derived; ||T_C||/||P0|| <= kappa_risk <= ||T_C||; P0 = 0 ⇒ T_C = S J T_C = 0. PASS.
11. §7.1 CONTAINS: sign change p=-p0, q=-q0 maps a v25 bounded-price test to a BSD solution with b_phi = 0 and r_phi = -r_test; nu even. PASS (uses uniqueness in S2×H2; bounded q0 from NOISE-PRICE).
12. §7.2 UC-ALL any D0 rank: S=0, Z={0}, z = T_C w for every response; finite and infinite (output through T depends only on w through T-h in the uncontrolled plant). PASS.
13. Application cut: lower bound only; CP not established for arbitrary data; realization (ONE causal stationary F with internal EMS) open; non-E1 controls outside CP unbridged. The source states all of these itself (S195|19, 253, 298). Remark (not a defect): "v25's original all-law proof remains the broader established necessary route" (S195|271) is the author's characterization of an unreviewed predecessor; this review assesses v25 below.

## 2. v25 (S196) — reconstruction

1. PROJ-E1: |f| <= E[|phi| | progressive sigma-field] (conditional Jensen on [0,T]×Omega), truncation + Tonelli; pathwise Cauchy then path-norm cap. PASS.
2. DUAL-NORM: same as v26 §4.4, with the coordinate-RN representation written out. PASS (ordinary).
3. Scalar H1 fact (good-lambda): re-derived P(M* > 2r) <= P(sqrt[M]_T > delta r) + delta^2 P(M* >= r) (stop at |M| = r, stop the increment after added bracket delta^2 r^2, Doob weak-L2); tail integration (1 - 2 delta^2) E M* <= (2/delta) E sqrt[M]_T; delta = 1/2 gives E M* <= 8 E sqrt[M]_T after localization/Fatou. The printed P(M*>r) vs my P(M*>=r) is immaterial after integration in r. PASS.
4. GROUP: drift re-derived = f^T D0 X + (B^T p + B0^T q)^T u + p^T C v = f^T z + p^T C v under CONTROL; diffusion = (A0^T p + q)^T X + (B0^T p)^T u = k^T z under NOISE-PRICE. E sqrt[M]_T <= ||k||_inf N1(z). Endpoint products 0. ALL-LAW-ID E<phi,z> = -E<r,w>. PASS for EVERY actual response with N1(z) < inf (no E2 assumption on the unknown control).
5. NEC and INF-NEC: |E<r,w>| <= N1(z_F(w)) <= G1 N1(w); zero-test uniqueness. PASS, at all ranks, without CP, for every original law (the family is restricted, not the controller class).
6. SDESC: substitution q = D0^T k - A0^T p re-derived term by term (ordered product A0^T A0^T). PASS.
7. Deterministic inclusion: lambda/||g||, q=0, phi = g/||g|| satisfies SADJ/CONTROL/NOISE-PRICE with k/||g||; nu of a deterministic r equals its H_in norm (aligned deterministic input). PASS.
8. §6.1 CYL norming: time-step projection, conditioning on finite Brownian observation sigma-fields (martingale convergence), mollification preserving the unit ball, approximate identity under a Gaussian law with density; norming for E1 output via truncation at ||z|| = R. PASS. Precision remark (non-load-bearing): density "in the full unit dual ball" presumes raw duals are F_T^W-measurable (canonical space); norming is unaffected because E<phi,z> = E<E[phi|F_T],z>.
9. §6.2 bounded p and q for CYL: REP p_t = -E[int_t^T Gamma_(t,s)^T D0^T f_s ds | F_t] re-derived from d(Gamma^T p) = -Gamma^T g ds + Gamma^T(A0^T p + q) dW with g = -D0^T f; FLOW bound via Itô on the Frobenius norm; Gamma_(t,s) independent of F_t; DQ via common translation of not-yet-frozen coordinates (Gamma depends only on increments). Semigroup law for noncommuting A, A0 re-derived (Gamma_(0,t+s) = Gamma_(t,t+s) Gamma_(0,t)); generator (1/2)v_xx + A^T v + A0^T v_x re-derived. PASS at written level for the load-bearing bounds (sup|p|, sup|V_x|, q = V_x). The classical-regularity steps (dominated differentiation, Duhamel across finitely many pieces, boundedness of higher finite-coordinate derivatives) are standard Gaussian-smoothing facts written at sketch depth; I accept them as NAMED ordinary Gaussian-convolution facts, not as reconstructed line by line.
10. k = J(A0^T p + q) with J a right inverse of D0^T (full column rank). PASS.
11. COMPLETE: G1(UC) = sup_CYL nu(r_phi) = kappa_st. PASS (two suprema; CYL subset of §4; NEC gives reverse).
12. UC-INF: PASS (same truncation argument as v26).
13. §7 STRICT-RISK: logical composition CONDITIONAL on the whole v21 theorem; arithmetic 2cd/(2a - sigma^2) > cd/a iff sigma^2 > 0 (a, c, d > 0, q0 > 0). Conditional PASS; unconditional status depends on v21 (reviewed separately).

## 3. v24 (S197) — reconstruction

1. Terminal reduction by Bochner conditional expectation. PASS.
2. H-valued MRT from scalar MRT + Parseval. PASS (NAMED scalar MRT).
3. PROJ, PAST, MATCH by isometry. PASS.
4. COMPLETE: every L2 extension is r + future-triangle stochastic integral and conversely; isometric bijection onto ker Pi. PASS.
5. FIELD-NORM and attainment when finite (Hahn–Banach representative conditioned on F_T, its MRT future kernel). nu = 0 ⇒ r = 0. PASS.
6. §7 GAIN-FIELD: CONDITIONAL on the whole v23 fixed-linear-law theorem. §8 NONSTRICT and STRICT quantifier equivalences: both directions re-derived (forward uses attainment and G1 itself as the common g). Conditional PASS.
7. Application: fixed linear law only; not an evaluation, synthesis or nonlinear-law statement. The source says so (S197|11, 207, 213).

## 4. NAMED_NOT_RECONSTRUCTED / named ordinary items so far

- NAMED (ordinary, not re-proved here): canonical ONE-Brownian scalar L2 martingale representation; Hahn–Banach; L1(Omega;H)* = Linf(Omega;H) for separable Hilbert H (author's coordinate sketch accepted); linear-SDE finite-prefix second-moment bound K_T (Itô/BDG/Gronwall); Gaussian-convolution regularity details in v25 §6.2.
- Propagation: none of these is a specialized edge; all specialized edges in v24–v26 listed above were reconstructed.

## 5. Next

Part 9 (S198 v23, S199 v22, S200 v21 at line 523, …), then parts 10–19 serially.
