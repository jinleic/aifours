# Desk static citation/step audit, phase-type-complex3 v3 (Ph3HostileDesk)

Written 2026-10-18 PDT by the desk (orchestrator, claude-opus-5-5) before reading either delegate note. Static only:
nothing was executed except sha256 hashing, JSON reading/counting of existing run outputs, and page rendering of the
pinned PDF (pdftoppm/pdftotext). No numerical, symbolic, SAT or checker run was made. The parent derivation and parent
smoke were not opened. Correctness only; this desk makes no novelty statement (the parent's 01:29 scope notice says the
eigenvalue-placement/angle mechanism and the beta = 1, n* = 4 example have prior literature; nothing below calls them new).

Target: snapshot/target/ph3-theorem-v3.md, sha256 260711591c812c30f01f7662d30b583da2d7baa7c28608ce1d882090b47a2ef5
(switched from v2 0fa0876d...37e7 on the parent's 01:07 instruction, before any delegate launch). Line numbers below
are 1-based LF lines of that file ("v3:N").

## 1. Citation audit (against the page images primary/pages/cm2003-pdfNN-NN.png; transcription primary/EXCERPTS.md)

| v3 lines | Claim | Primary | Result |
|---|---|---|---|
| 61-62 | irreducibility quote, "p.570, PDF6" | p.570 left col. (E3) | verbatim; page/PDF correct. The PH-specific definition is p.568 (E2, Neuts 1981: "connected to the initial vertex and to the absorbing vertex"); equivalent |
| 81-83 | Proposition 1, "p.570 (PDF6), verbatim" | p.570 right col. (E3) | verbatim |
| 84-86 | printed proof pointer | p.570 (E3) | verbatim |
| 86-87 | "The same result was proved for PH-representations in Neuts (1984)." | p.570, paragraph after the proof | verbatim ("followed by" is accurate) |
| 87 | dictionary g = C(sI-A)^-1 B, edge x_i -> x_j iff a_ji > 0 | p.570 (E3) | correct; x' = Ax + Bu, y = Cx is on p.569 (not in snapshot), implied by the transfer formula |
| 88 | (A,B,C) = (T_RR^T, alpha_R^T, t_R^T) | desk derivation | correct: a_ji = (T_RR)_ij gives the PH edge orientation; C(sI-A)^-1 B = (alpha_R (sI-T_RR)^-1 t_R)^T = F |
| 92-95 | Theorem 6 quote, "p.574, PDF10", Dmitriev-Dynkin 1945 / O'Cinneide 1991 | p.574 right col. (E5) | verbatim incl. (27) |
| 193-196 | Theorem 14 quote with (42), (43), "p.577, PDF13", Commault-Chemla 1996 | p.577 right col. (E6) | verbatim; (42) shown as a bracketed display, correctly |
| 26-27 | "non-singular PH generator" (in quotation marks) | p.567 (E1): "...the matrix T is non-singular. This matrix is called a PH-generator."; p.568 (E2): "The non-singular matrix T represents an infinitesimal generator" | paraphrase in quotation marks (NIT) |
| 205 | Conjecture 1 | p.577 (E6) | statement matches: n_min is the least n satisfying (27) with lambda_1 = c, lambda_2 = a, theta = b, i.e. n*; for b > 0 this n is automatically >= 3 |
| 5-6 | book p.544 | not in snapshot | not checked (scope remark only, non-load-bearing) |

Source/target (Q1): 1/q(s) with q from (42) equals c(a^2+b^2)/((s+c)((s+a)^2+b^2)) = F exactly (poles -c, -a -+ ib);
numerator constant, three distinct poles, so lowest terms, degree 3. Order = dim T (E1). F(0) = 1 forces alpha 1 = 1
for any representation (F(0) = alpha (-T)^-1 (-T)1 = alpha 1), so the stochastic-alpha convention loses nothing.
n* = ceil(pi / arctan((a-c)/b)) (contract) agrees with min{n >= 3 : b <= (a-c)cot(pi/n)}. Domain: a > c > 0, b > 0 is
exactly the non-degenerate part of the printed "a, b, c >= 0": c = 0 makes (42) undefined, a <= c with b > 0 gives no
unique dominant real pole (not PH), and b = 0 (three real poles, no complex pair) is outside the contract's frozen
statement; covering b = 0 would need a separate (classical, real-pole) argument the target does not give or claim.

## 2. Step audit (each step re-derived by the desk)

* §0 / (0.1) v3:24-38: Metzler + T1 <= 0 => s(T) <= 0 via left Perron vector; Hurwitz <=> nonsingular (s(T) is an
  eigenvalue). beta <= cot(pi/n) <=> phi <= pi/2 - pi/n <=> psi >= 2 pi/n; bands (0.1) correct. OK.
* A1 v3:44-46: each pole of the lowest-terms F is a zero of det(sI - T). OK.
* A2 v3:48-53: R closed under T-edges => T_RS = 0; block lower-triangular resolvent; F = alpha_R (sI-T_RR)^-1 t_R;
  t_R = -T_RR 1 since T_RS = 0; spec(T_RR) subset spec(T) => Hurwitz; three poles => n_R >= 3. OK.
* A3 v3:55-63: U (states that reach no exit) is forward-closed, X_UU 1 = 0 => 0 in spec(X) if U nonempty. OK. Gives
  realization irreducibility (graph sense), not matrix irreducibility; correctly labelled. Not used by A4/A5.
* A4 v3:65-79: Y = T_RR + kappa I >= 0; rho(Y) eigenvalue with left u >= 0; Re(lambda)+kappa <= |lambda+kappa| <= rho(Y)
  and rho(Y) - kappa in spec(T_RR) => rho(Y) = mu + kappa, u T_RR = mu u (no irreducibility used). Positivity of
  e^{T_RR tau}: Y^k entries count weighted paths, k = 0 term gives the diagonal; every j in R is reachable from
  supp(alpha) => p > 0; eps = min p / max u gives p >= eps u. u.t_R = -mu (u.1) > 0. For real s > mu the resolvent
  equals the Laplace integral, so F(s) >= eps (u.t_R) e^{-s tau}/(s - mu) -> +inf; a rational function is bounded
  near a non-pole, so mu is a real pole of F, i.e. mu = -c. Also no non-real eigenvalue can have real part s(T_RR)
  (Lemma A or primitivity of the blocks), so "the eigenvalue of maximal real part" is unambiguous. OK.
* A5 v3:92-97: Theorem 6 hypotheses (PH generator of order n_R, lambda_1 = c > 0, lambda_2 = a > 0, theta = b > 0,
  -c of maximal real part by A4) all met. OK.
* A6 v3:103: the set {m >= 3 : beta <= cot(pi/m)} is upward closed; n >= n_R >= n*. OK.
* Appendix A v3:211-239 (Lemma A): irreducible case - r > 0, Re lambda < mu (primitivity), Q = D^-1 (X - mu I) D has
  zero row sums, e^{Qr} stochastic, K = conv{w_i} invariant under e^{zr}; 0 in K; K not in a line (argument of
  e^{zr}w_i moves continuously at rate y > 0); 0 in int K (supporting-line contradiction); polygon, ccw vertices,
  omega_k in (0, pi) since 0 is interior, sum 2 pi; tangent cone C_k at v_k, z v_k in C_k by closedness; with v_k
  rotated to the positive axis, v_{k+1} - v_k has direction pi - eps_k (upper half plane, v_{k+1} is ccw), the cone's
  upper boundary, so direction pi - phi of z v_k forces phi <= eps_k (orientation checked; conjugation fixes y > 0);
  law of sines |v_{k+1}|/|v_k| = sin eps_k / sin(omega_k + eps_k) (opposite sides checked); cyclic product 1;
  log g_k increasing on (0, pi - omega_k) and phi <= eps_k < pi - omega_k; Jensen for concave log sin gives
  sin phi <= sin(phi + 2 pi/p); the "sin u <= sin v <=> u + v <= pi" lemma (0 < u < v < pi) checked in all cases;
  tan phi <= cot(pi/p) <= cot(pi/m) since 3 <= p <= m. Zero or coinciding w_i are harmless (vertices are a subset of
  the distinct nonzero hull points; p >= 3 follows from 0 in int K). General case: Frobenius normal form, 1x1 blocks
  real, irreducible 2x2 Metzler blocks have discriminant >= 0, so m_B >= 3; mu_B <= s(X), cot(pi/m_B) <= cot(pi/m),
  and mu_B - Re lambda > 0. Correct. Symbol r is reused for the Perron vector and time (NIT).
* B0 v3:110-113: C(A^2+beta^2) = c(a^2+b^2)/delta^3; sigma + C = x - 1; time scaling of a representation correct. OK.
* B1 / Lemma B1 v3:115-135: (B1.1) from (0.1) for n >= 4 and n = 3; s >= sin phi exactly on [0, psi]; t0 < S/3 from
  S <= 3 psi < 3(pi - phi); domains; G(S/3) >= 0; G(t0) < 0 in both cases (t0 > 0: s(pi - phi) = 0; t0 = 0: S/2 in
  (psi, pi - phi]); IVT root t* in (t0, S/3]; theta_1 > 0 strictly so every m_i finite; t0 = 0 for n >= 4 iff
  (n-2) psi >= pi (true since psi >= 2 pi/n, n >= 4); t0 = 2 phi for n = 3. Upper endpoint: G(S/3) = 0, t* = S/3,
  all theta = 2 pi/n. Lower endpoint: S = 2 psi, G(0) = 0, theta_1 = 0 would give m_1 = -inf; the point belongs to
  band n - 1 by the definition of n*. No root finder is a premise. OK.
* B2 v3:137-144: (I1), (I2) verified; 1 - m_i > 0 on (0, pi - phi); m_* = beta cot 2 phi = (1 - beta^2)/2. OK.
* B3 v3:146-153: only the identity and the full n-cycle are supported; cycle term (-1)^{n-1} (-1)^{n-1} (-W) = -W;
  q(i beta) formula with beta^n = sin^n phi / cos^n phi; sum theta = 2 pi; product of sines = sin^n phi; D | q
  (distinct roots 1, +-i beta). OK.
* B4 v3:155-158: Mu = u with u > 0 (last row uses W = (1 - m_n) u_n); primitive => s(M) = 1, 1 simple. OK.
* B5 v3:160-162: column checks of y (xI - M) = e_1 (column 1 meets -W in row n; column j >= 2 meets -1 in row j-1);
  orientation consistent with alpha = e_1, forward edges i -> i+1, closing edge n -> 1. OK.
* B6 v3:164-172: 1 - m_* = rho, m_*^2 + beta^2 = rho^2, D(m_*) = -rho^3; N_t = K[z^{n-3} + W sum h_k z^k];
  P = W h + z^{n-3} R_3/D in R[[z]] fixes the coefficients of z^k, k <= n-4; P monic => N_t = K P. The cancelled
  roots are the n - 3 roots of P; 1 is simple (B4) so P(1) != 0; a common root of P with +-i beta would not affect
  the rational identity K P/(D P) = K/D; dominance and Hurwitz come from s(M) = 1 < A, not from the transform. OK.
* B7 v3:174-182: u = z/rho factorization (m_*/rho = cos 2 phi = -cos psi); Chebyshev U_k generating function; partial
  sums by telescoping give c_k = [cos(psi/2) - cos((k + 3/2) psi)]/[2 sin(psi/2) sin psi]; for 0 <= k <= n-4,
  psi/2 < (k + 3/2) psi <= (n - 5/2) psi < 2 pi - psi/2 (needs (n-2) psi < 2 pi, implied by the band); cos < cos(psi/2)
  there; sin(psi/2), sin psi > 0. t >= 0 with t_1 = t_2 = 0 (title says "positive": wording). OK.
* B8 v3:184-189: T0 irreducible Metzler, s(T0) = 1 - A = -C < 0, (-T0)^-1 > 0, v > 0; T' = D_v^-1 T0 D_v Metzler,
  T' 1 = -D_v^-1 t, transform invariant; v_1 = Phi(0) = K/D(A) = C/(A-1) = 1 => alpha' = e_1; delta T' and the
  original-unit formula T = D_v^-1 (delta M - a I) D_v correct. OK.
* n = 3 branch (Q8): S = 2 pi, t0 = 2 phi, bracket [2 phi, 2 pi/3] nonempty iff phi < pi/3 (band gives phi <= pi/6);
  G(2 phi) = -sin^3 phi; G(2 pi/3) >= 0 iff psi >= 2 pi/3; theta_2 = theta_3 = pi - t*/2 in [2 pi/3, pi - phi);
  q monic cubic vanishing at 1, +-i beta => q = D, P = 1; N_t = t_3 = K (empty product, empty Taylor sum); m_*, rho,
  h are only a dummy expansion point and B7 is vacuous; v > 0 and alpha' = e_1 as in B8. Independent of Theorem 14. OK.
* Part C v3:193-207: route (ii) is valid, so the unconditional conclusion holds given Part A + Appendix A + Part B.
  Route (i): Theorem 14's printed hypothesis begins "Consider a PH-distribution with Laplace transform 1/q(s)";
  v3:196-197 checks only the parameter domain. F is PH for all a > c > 0, b > 0 (by Part B itself, or by Theorem 1:
  f(t) = (c(a^2+b^2)/b) e^{-ct} int_0^t e^{-(a-c)u} sin(bu) du > 0 for t > 0), so the import is valid, but the text
  should say so (MINOR, non-load-bearing).
* Appendix B v3:246-249: W = beta^n / prod sin theta_i and the exit list agree with B2/B6; the uniform cycle at
  beta = cot(pi/n) has spectrum m_* + rho e^{2 pi i k/n} with ratio exactly cot(pi/n). OK.

## 3. Evidence audit (Q7; inspect only)

Hash bindings checked by the desk (hashlib on byte-identical copies): pin-v1 code_sha256 15/15 match; pin-v1 run
outputs 11/11 match; pin-v1 primary proof (v2), contract, PDF match; pin-v1 frozen README sha equals the sha of the
first 7,366 bytes of the current README (log rows appended after the freeze only); pin-v2 previous pin, primary proof
(v3), kept v2, d01 script/output/pre/post receipts 7/7 match; every pre-receipt's code_sha256 list equals the current
code files (12/12 receipts); every post-receipt's pre_receipt_sha256 and outputs_sha256/bytes match (12/12).

Counts recomputed from the JSON outputs: e01 33 items, 32 ok, the FAIL is E4_mstar_eq_minus_beta_cot_psi; e02 three
symbolic methods true, worst residual 5.7475e-47; b01 98 instances, 10 OK=false (n=20: 1, n=24: 2, n=32: 7), all
with q1/q_ibeta/remainder flags false; b02 112/112, ph_checks 336; d01 1,605 instances, 3,210 PH checks, 0 failures
(code docstring: f = k/40, k = 1..40, plus 1e-3, 1e-9 for n = 3..40, so 41 interior n = 3 positions); f01 exit code 1
(ZeroDivisionError "matrix is numerically singular"); f01d first failure k = 60, n* = 35, beta = 10.8547,
rho^(n-3) = 5.807e56; f02 187 records = 160 random + 14 upper-endpoint + 13 just-above-lower, all OK, 67 with density
fields, max_n 29; m01 core 71/87 rejected = A exit 15/15, I alpha=e2 15/15, D repeated angle 15/15, G jet reversed
12/12, C orientation 14/15 (miss at n = 4, f = 1), H all-exit scaling 0/15; order mutations B 0/24; positive controls
30/30 PH_OK (15 unmutated, 15 first-three permuted); order n*-1 27/27; lower endpoint 9/9 refused; m02 T invariant
15/15 (v1 no longer 1), corrected normalization 15/15, start state 90/90, orientation 10/10, arrangements
30+60+105 per f, two f, = 390, all nonnegative and checker-pass; s01 47,070 complex eigenvalues, 0 violations,
uniform ratio 1.0 for m = 3..9, trimming 3/3; max RSS over runs 104.4 MB. All statements in pin-v1/v2 and README §7
match these numbers. No document counts b01's flagged instances, f01, the H (all-exit scaling) mutation or the B
(reordering) mutations as passing negative controls: pin-v1 labels them "Superseded", "ABORTED", "NOT rejected
(ineffective)" and "valid alternative orderings"; README §7 likewise.

## 4. Desk findings (none FATAL or MAJOR; none load-bearing)

1. [MINOR] target/ph3-theorem-v3.md:196-197 - the Theorem 14 import is checked against the parameter domain only;
   the printed hypothesis also presupposes a PH-distribution with transform 1/q(s) - add "F is a PH Laplace
   transform for all a > c > 0, b > 0 (e.g. by Part B, or by Theorem 1 since the density
   (c(a^2+b^2)/b) e^{-ct} int_0^t e^{-(a-c)u} sin(bu) du is positive for t > 0)". load-bearing: no (route (ii)).
2. [MINOR] target/ph3-theorem-v3.md:250-253 - Appendix B lists b01 with b02 without saying b01 had 10/98 instances
   flagged (absolute-radius test), superseded by b02 - add "b01: 88/98 OK, 10 large-n absolute-radius flags; b02
   112/112 with a relative test". load-bearing: no (smoke only; pin-v1 and README report it).
3. [MINOR] lane/receipts/pin-candidate-v1.json:39 - "flagged ONLY by absolute radius 2^-150": the stored flags are
   conjunctions contains(0) AND rad < 2^-150 (code/ph3_ball_v1.py:58-61), so ball.json alone cannot show which
   conjunct failed; the claim follows from rigorous ball enclosures of exact identities (containment of 0 is
   automatic) plus b02. Reword to "flags = contains(0) AND absolute radius < 2^-150; containment is guaranteed by
   ball rigour, so the failing conjunct is the radius [inference]". load-bearing: no.
4. [MINOR] target/ph3-theorem-v3.md:13 - "No mathematical step changed" is true of the steps, but the headline
   dependency claim changed from v2:196-197 ("conditional only on the imported Theorem 14 ... and ... Theorem 6") to
   v3:206-207 ("Imports: none are needed"); say so explicitly. load-bearing: no (the desk verified both pieces the
   stronger claim rests on: Part B's n = 3 branch and Appendix A).
5. [NIT] target/ph3-theorem-v3.md:174 - "every exit positive": t_1 = t_2 = 0 (v3:167); write "every exit
   nonnegative; t_3..t_n > 0".
6. [NIT] target/ph3-theorem-v3.md:214-218 - r denotes both the Perron vector and time; rename one.
7. [NIT] target/ph3-theorem-v3.md:26-27 - "non-singular PH generator" is in quotation marks but is a paraphrase of
   p.567/p.568; drop the quotation marks or quote p.567.
8. [NIT] target/ph3-theorem-v3.md:61-62 - the PH-representation definition of irreducibility is p.568 (Neuts 1981);
   p.570 is the positive-realization one; cite both (equivalent).

## 5. Unresolved assumptions (desk)

* Ordinary background only: Perron-Frobenius for nonnegative matrices (reducible: rho is an eigenvalue with a
  nonnegative left eigenvector; irreducible: positive eigenvector, primitivity with positive diagonal), Frobenius
  normal form, IVT, Jensen, Laplace transform of matrix exponentials, plane convex geometry, Chebyshev generating
  function. No other assumption found.
* Scope: b = 0 and the general (book p.544) question are outside the statement; the theorem answers Conjecture 1 only
  for the frozen domain a > c > 0, b > 0.
* Novelty: not assessed by this desk (parent notice: prior spectral angle construction exists).

## 6. Verification counts (desk)

Primary quotations/citations checked against page images: 9 rows (7 verbatim quotes incl. (27), (42), (43), 3
page/PDF mappings, 1 dictionary); 1 not checkable (book p.544). Proof steps re-derived: 21 (§0, A1-A6, Lemma A
irreducible steps 1-6 and general case, B0-B8, n = 3 branch, Part C, Appendix B formulas). Hash bindings: 15 code +
11 run outputs + 4 pin-v1 inputs/README prefix + 7 pin-v2 + 12 pre-receipt code lists + 12 post-receipts = 61.
Run-count claims recomputed: 14 runs/sub-runs (all match).
