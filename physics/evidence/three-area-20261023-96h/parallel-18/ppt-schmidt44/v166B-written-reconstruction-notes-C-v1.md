# v166-B reviewer working notes C — v11, v10, v9, v8, v7, v6, v5, v4, v3

Reviewer PhysicsPPT44-2. Preceding `/bin/date`: Tue Oct 27 05:30:42 PDT 2026. WRITTEN all-variable reconstruction only; no tools beyond reads/date/shasum/wc. Read frontier: parts 12, 13, 14 complete (part12 end S214|191; part13 end S217|245; part14 end S219|385).

## v11 (S211, 243 LF) — LOC-LIP, R > 0, truncated-energy buffers
- §2 block absorption (delta with ||Abar|| delta + 10||S|| sqrt(delta) <= 1/2; vector good-lambda 64/7). PASS (localize, absorb, Fatou).
- §3 conditional L1 EMS. §4 truncated-energy continuity for bounded cylinder probes. §5 buffers (4)–(5) via the GLOBAL gain for w_n (valid for every deterministic buffer choice ⇒ non-circular). §6 iid truncations. PASS.
- §7 all inputs: cylinder density + LOC-LIP input-Lipschitz stopped estimate + convergence in probability + Fatou. PASS (here input regularity IS used; it is a stated premise).
- §8 nonsharp 2sqrt2 upper. PASS.
- §9 cubic example: L(x^2) = -(7/4)x^2 - 2x^4 + 2xf <= f^2; V = x^2/2 + x^4/4, q = x + x^3, LV = -q^2 + x^2/8 + 3x^4/8 + qf <= -(13/16)q^2 + qf (coefficients 2/16 <= 3/16, 6/16 <= 6/16, 0 <= 3/16) <= -(13/32)q^2 + (8/13)f^2; |z|^2 <= q^2 ⇒ G2 <= 16/13, G1 <= 32sqrt2/13. PASS (all re-derived).

## v10 (S212, 289 LF) — R > 0 H1 bootstrap; forced unstable-hidden Gramian N&S
- Part I: delta = min(1, 1/(4(1+a)), 1/(1600(1+s)^2)) gives a delta + 10 s sqrt(delta) <= 1/4 + 1/4; recursion M_(j+1) <= 3 M_j + 2 input_j; (3). PASS. Mean bridge (4). PASS.
- Part II class: R > 0, D0 = A0 = 0, A anti-Hurwitz, (A,B) controllable, B0 R^(-1) B^T = 0.
- Gramians: A G_B + G_B A^T = D by -d/dt(e^(-At) D e^(-A^T t)); G_B > 0 by controllability; H_h = tail Gramian. PASS.
- §6 conditional L1 restart ⇒ E|x(t0 + s)| -> 0. PASS.
- §7 necessity: e^(-AT) m(T) -> 0 because |m(T)| <= E|x(T)| -> 0 and e^(-AT) -> 0; calB(nubar) = -calC_h(w); adjoint norms = y^T G_B y and y^T H_h y; H_h <= g^2 G_B ⇒ (FH). PASS.
- §8 sufficiency: X = G_B - rho H_h > 0, P = X^(-1); AX + XA^T = D - rho E_h C C^T E_h^T (A commutes with E_h) ⇒ (11). Predictor p' = A p + E_h C w(t) - C w(t-h) re-derived; chi' = (A - DP) chi + E_h C w; diffusion B0 u = 0 by ORTH. Acl Hurwitz: Acl X + X Acl^T = -D - rho E_h C C^T E_h^T re-derived; imaginary-axis left eigenvector forces Bcal^T v = 0 ⇒ A^T v = i omega v, contradiction with anti-Hurwitz. Storage identity V' + |z|^2 - eta^2 |w|^2 = -eta^2 |w - rho r|^2 re-derived (|z|^2 = chi^T P D P chi). PASS.
- §10 scalar: G_B = b^2/(2a), G_C = c^2/(2a) ⇒ gamma > (c/b) e^(-ah); law (16): chi' = (a - bk) chi re-derived. PASS.
- §11 flag countercontrol: boundary control only, outside the printed class (remote memory). Correctly labelled.

## v9 (S213, 244 LF) — active unforced hidden blocks
- Structural theorem §§1–5: new decompositions re-checked (visible isolation, hidden unforced, B0v Bv^T = 0, AH LMI ⇔ certificate (3) by Schur/congruence). Necessity and sufficiency CALL the named v4 deterministic infinite-preview converse and realization/transversality (v4 §10, reviewed below) and the v5 quotient/projected-H1 lemma. Status: CONDITIONAL on v4 §10 + v5 §§2–3 at their reviewed depth.
- Family (5) §§6–9 independent of v4: matrices re-checked (BU = 1, B0U = 1/4, Bv = (b,0), B0v = (0,sigmaV)); passive HID impossible (3H > 0); K = -3 ⇒ -2, 1/4, -4 + 1/16 = -63/16; AH Schur complement -63/16. Law (7): lambda = (a^2 + b^2 d^2)/a, p lambda = d^2 + k^2 re-derived; identity (8) re-derived with gstar^2 = p c^2/lambda = c^2 d^2/(a^2 + b^2 d^2). Necessity via flat inputs: |ybar| <= (bg + c) sqrt(L/(2a)); c <= sqrt(a^2/d^2 + b^2) g. Hidden EMS rate 63/16. PASS. Pointwise endpoint (13) PASS.

## v8 (S214, 191 LF) — Rdef inverse-Bessel obstruction (method calibration)
- psi = log(1 + x^2) nonexplosion; inverse BES(3) law; 100 bound (inside term 16 sqrt2 · 2 · (2pi)^(-1/2) < 64); strict mean; E(int X^4)^(1/2) = inf; zero-start pulse with finite output energy (12) but infinite post-pulse control N1. PASS. Nonclaims correct (no finite uniform G1 claimed; later v13 shows G1 = ∞ at h = 0).

## v7 (S215, 220 LF) — stationary globally Lipschitz EMS laws: G2 <= G1
- (2), (3) by global Lipschitz/Gronwall; induction M e^(-lambda R_n) A_L (1 + b) <= n^(-2). PASS.
- §4 error N1(Rz - Yideal) <= sqrt(C_L/n); Chebyshev truncation bound (13)-type. PASS. §5 dense extension (joint LIP gives finite-time L2 continuity). PASS.
- §6 saturation example: L(x^2) = -10x^2 - 2x sat(x) + (x - sat(x))^2 <= -9x^2; with forcing <= -8x^2 + w^2; |z|^2 <= 2x^2 ⇒ G2 <= 1/2. PASS. Optional G1 <= 1/sqrt2 uses the then-unreconstructed sharp transfer (later v22 supplies the continuous monotone case; as stated in v7 it is an import) — non-load-bearing.
- §7 clock GATE boundary: CONDITIONAL on the NAMED v2 unit-cascade Gaussian-gap lemma (ell <= (1 - 1/18432) m, m^2 >= 1/384); non-load-bearing for the core.

## v6 (S216, 216 LF) — fixed stationary linear law: G2 <= G1 by gliding buffers
- tau(a) -> 0 by dominated convergence (finite G1 only); tau(H_n) <= 1/n; superposition z = sum Y_i; error (9) = sum_i 1(∪_(j>i) I_j) Y_i bounded by n tau(H_n) <= 1 (component tails after t_(i+1) = t_i + H_n, stationarity). PASS. Averaging (13)–(15), dense/prefix extension. PASS.

## v5 (S217, 245 LF) — visible quotient
- U = ∩ ker(Q Abar^k) (Cayley–Hamilton), pi Abar = Avis pi, Dtilde Z = 0, observability of the quotient. PASS.
- Projected dynamics with QMATCH; v = R^(-1) D1^T z; projected H1 ⇒ visible mean ODE (7). PASS.
- Finite theorem: necessity CALLS v4's finite deterministic converse (v4 §6); sufficiency: lift (9), B0vis v = 0 by QORTH, pathwise visible deterministic dynamics, v4 squares + strict Volterra inverse (v4 §§5,7). CONDITIONAL on v4 §§3–7.
- Infinite theorem: v4 §10 converse; cascade (12) re-derived (d/dt E q^T H q expansion; G, J blocks). PASS for the new cascade step; whole theorem CONDITIONAL on v4 §10.
- Example §6 re-checked: R = I, K0 = 0, Q = diag(1,0), U = span(e2), Bvis = (1,0), B0vis = (0,1), product 0; HID -2 + 1 = -1; global NEO fails at x = e2. PASS.

## v4 (S218, 488 LF) — finite positive preview on R > 0/MATCH/ORTH; infinite on SD
- §2 H1 bridge under NEO; MATCH ⇒ NEO with Lambda = B0 R^(-1) D1^T (A0 x + B0 u = B0 v re-derived). PASS.
- §3 conjugation: symplectic inverse bottom row [-F^T, E^T] re-derived; Hh blocks (Ah, Mh, Qh) re-derived; graph derivative gives (5); expansion of (5) to PRE with k = (PE - F)C re-derived; terminal LQ window; P(L) = F E^(-1) ⇒ k(L) = 0. PASS.
- §4 (K) re-derived (∂_t K difference = -γ^(-2) k m via PRE). (MD) re-derived (∂_t Φ22(s,t) = Φ21(s,t) D + Φ22(s,t) Abar^T; inverse blocks Φ21(s,t) = -Φ21(t,s)^T, Φ22(s,t) = Φ11(t,s)^T). (MB) re-derived: M(t,t,r) = C^T K(t,r); upper boundary M(t,s,t+h) = C^T Φ11(t,s)^T k = m(t,s)^T using K(t,t+h) = (P E - F) C = k (Φ(t,t+h) = exp(-hH0)); symmetry reduced to Φ22(s,t)Φ21(r,t)^T + Φ21(s,r) = Φ21(s,t)Φ22(r,t)^T, proved by Φ(s,t) = Φ(s,r)Φ(r,t) and the symplectic relations Ψ11Ψ22^T - Ψ12Ψ21^T = I, Ψ21Ψ22^T - Ψ22Ψ21^T = 0 (from ΨJΨ^T = J; H0 Hamiltonian because D, Q symmetric). PASS.
- §5 exact preview square (11)/(12) re-derived TERM BY TERM (second pass): ġ = k w - P C f(t) + ∫∂_t K f; Ṅ = 2 w^T μ - 2 f(t)^T C^T g + ∫∫ f^T ∂_t M f; the two outgoing-forcing pairs cancel; completing the v- and w-squares leaves x-x = PRE (0), x-window = (Abar^T - PD) g + γ^(-2) k μ + ∫∂_t K f = 0 by (K), window-window = -g^T D g + γ^(-2) μ^T μ + ∫∫ f^T ∂_t M f = 0 by (MD). PASS.
- §6 sample-and-hold converse: Young step to (13) re-derived; (18) re-derived from (12) with 2γ^2 ε^2 <= d/4. PASS given (12).
- §7 strict Volterra inverse ||D^n|| <= (c_D L)^n/n! ⇒ ||(I - D)^(-1)|| <= e^(c_D L); strict gain γ sqrt(1 - M^(-2)). PASS.
- §8 realization: diffusion (A0 + B0 K0)x - B0 R^(-1) B^T (Px + g) = 0. PASS. §9 example matrices re-checked (K0 = (0, -alpha/beta)^T, MATCH, ORTH, Q = d^2, Abar = a). PASS.
- §10 infinite: uniform finite values via stabilizing F0; lower-game value identification and monotonicity in T; local fixed point of the autonomous flow ⇒ ARE-PRE. The p-equation re-derived: p = P x° + g°, p' = -Abar^T p - Q x° + k(w° - w*) (uses PRE, (K), ġ above), p(T) = 0, B^T p + R v° = 0. PASS. Detectability ⇒ Acl Hurwitz re-derived from (24). Stationary transversality/identity: the same (K)/(MB)/(MD) algebra with γ^(-2) → rho and ARE-PRE in place of PRE; PASS at that substitution (finite-window decay of Vcal re-checked from its bound).
- Source cut: Tadmor–Mirkin 2005 PDF HTTP 418 / closed — not imported; correct.

## v3 (S219, 385 LF) — h = 0 MATCH/ORTH; B = 0 matched preview; infinite LMI
- Lemma 1 H1 (constant 8). Theorem 2 NEO bridge. PASS.
- Lemma 3: square (4) re-derived term by term; P >= 0; uniform bound via sample-and-hold; strict Volterra (11)–(12). PASS.
- §5 HAM ⇔ bounded RDE (graph flow). PASS. Theorem 4 (MATCH/ORTH, h = 0) with realizer (14); diffusion cancels. PASS. Example re-checked as in v4 §9.
- Theorem 5 (B = 0, MATCH, any h): mean state unchanged by control; N1(z) >= ||G_L w||; u = K0 x attains pathwise. PASS.
- Theorem 6 (B = 0, MATCH, A Hurwitz): LMI sufficiency by storage; necessity by Q_ε, monotone bounded finite values, flow equilibrium (17), P∞ > 0, Schur at γ. PASS.

## NAMED_NOT_RECONSTRUCTED (reviewer depth) items from this batch
- The first draft of these notes listed N-V4-SQUARE (v4 (11), (MB), §10 p-equation). It was CLOSED by the second-pass reconstruction above before this file was pinned; no NR remains from it.
- Ordinary named facts only: finite-dimensional matrix-ODE local existence/continuation and continuity of the autonomous Riccati flow; Sobolev sampling; Young convolution; Cayley–Hamilton; stabilizability/detectability PBH equivalences.
- No specialized edge in this batch left unreconstructed.
