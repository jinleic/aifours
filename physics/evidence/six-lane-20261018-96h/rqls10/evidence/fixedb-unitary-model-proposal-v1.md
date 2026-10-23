# Fixed-B unitary model (no orbit symmetry) for maximal 1-RQLS(10): design, source screen, B choice

Recorded 2026-10-19T05:08:55-0700 (from /bin/date). Author ContinueRQLS10b. Status: DESIGN ONLY; unreviewed; nothing in
this note is parent-accepted. The target (existence of a 1-RQLS(10) with 100 distinct rays) is OPEN / UNKNOWN. No
numpy/native computation has been run for this model; the assay source below is frozen but NOT executed.

## 1. Model
A 1-RQLS(v) is a v x v array of unit vectors q_ij in C^v whose v rows, v columns and the v classes of a classical Latin
square B (the resolution: class s = {(i,j): B(i,j) = s}) are orthonormal bases; maximal = v^2 distinct rays.
- WLOG (global unitary) row 0 is the computational basis, so q_ij = U_i e_j with U_0 = I and U_1..U_{v-1} unitary:
  the row conditions hold identically.
- For i < i' put M = U_i^* U_i'. Columns: M[p,p] = 0 for all p. B-classes: M[p, pi(p)] = 0, where pi(p) = the column j'
  with B(i',j') = B(i,p); pi is a derangement because B is Latin. So each M_ii' is a unitary with zeros on two disjoint
  permutation patterns: 2v complex equations per pair, 2 v^2 (v-1) real equations in total (1,800 at v = 10).
- Chart: U_k <- U_k expm(A_k) with A_k skew-Hermitian with ZERO diagonal (right phases of U_k = phases of single rays,
  removed); v (v-1)^2 real parameters (810 at v = 10). The left-phase action U_k -> D U_k (D diagonal, k >= 1) leaves
  the zero patterns invariant (gauge, rank <= v - 1 after removing right phases). No orbit symmetry is imposed: every
  U_k is free.
- Analytic Jacobian: dM = -A_i M + M A_i' (A_0 = 0). Validated against central differences in pure Python (exact for
  the bilinear M): max relative error <= 4.9e-13 (evidence/fixedb_jacobian_v1.receipt.md 28c2789a...fc1ca4).
- The naive count (1,800 equations, 810 parameters at v = 10) is meaningless as a headroom argument: the equations are
  dependent, and solutions exist at v = 7, 8 where the count is equally "overdetermined" (v = 7: 588 vs 252).

## 2. Relation to earlier lane work
- The earlier unsymmetric path (code/rqls_assay_v3/v4/v8 `unsym`, read-only scout report 2026-10-19) is RRR over 100
  free unit vectors with Gram residuals on all 30 lines, phases free per slot. Its only v = 10 use (v3 stage T4: Parker,
  Cay(D_5), Cay(Z_10) x 2 seeds x 20,000 iterations) ended at MAX_ITER with error 0.47-0.50 on every run, never polished,
  no verified endpoint; the v3 receipt states that v = 10 sensitivity was NOT qualified (it missed known classical
  points). The v4 sens1/sens2 configs were never launched. The old-lane G10 probe (projected gradient, Cay(Z_10))
  stalled at f = 11.45-13.25.
- Differences here: rows built in (unitaries, U_0 = I) instead of 100 free vectors; only the 2v zero entries per pair
  as residuals; analytic Jacobian + Levenberg-Marquardt from the start (quadratic convergence near solutions) instead of
  RRR; gauge-fixed charts; a calibration ladder that includes v = 10 recovery of a KNOWN point (near the classical Parker
  point and random starts on its B) so that v = 10 convergence is at least observed; immediate stop rules.
- Orbit ansaetze already studied (forced Z7+3, Z9+1, W8 = WH_5 (x) C^2, WH_10) are special cases with imposed symmetry;
  WH_10 is additionally excluded by the prior result of Grassl-McNulty-Mista-Paterek (evidence/wh10-prior-art-addendum-v1.md).

## 3. Source screen: Hall-Paige / quantum complete-mapping no-go for B = Cay(Z_10)
Read directly (lane sources/): Zhang-Cao arXiv:2608.29201v2 (RQLS.tex), Huang-Li arXiv:2606.27758 (MCDQLS.tex),
Ball-Simoens arXiv:2607.12933 (large_sets_of_MOQLS.tex), Han-Zang-Zhang-Tian arXiv:2507.20154
(MOQLS-submission-5.30.tex; added as sources/han-zang-zhang-tian-2507.20154.eprint 3f85d526...891). Web searches
(2026-10-19 04:4x-05:0x): quantum Latin square + complete mapping / orthomorphism / Hall-Paige / Cayley table /
pandiagonal even order / quantum transversal; no further relevant source surfaced.
- Classical facts: a Latin square has a classical orthogonal mate only if it has transversals; Cay(G) has a transversal
  iff G has a complete mapping (Hall-Paige, proved); Z_n for even n has none (Euler / Hall-Paige). Both groups of order
  10 (Z_10, D_5) have a nontrivial cyclic Sylow 2-subgroup, so neither has a complete mapping: for B = Cay(Z_10) or
  Cay(D_5) every solution of the model is NON-classical.
- Constructions: Huang-Li (Theorem "Construction--complete mapping": phi_ij(t) = omega^(tj + i mu(t)) / sqrt v with
  pan-diagonal transversals) needs a complete mapping of Z_v (odd v); Zhang-Cao Construction "Z2Zm" (characters of
  G = Z_2 x Z_m, transversals T_c = {(i, i + c)}, i.e. B = Cay(G)) needs a complete mapping of Z_2 x Z_m, which exists
  only for m even (their explicit mu: m = 2k >= 6); Ball-Simoens (Frobenius rings: f with x -> f(x) - m x a permutation
  for all m in M, differences of M units) would need, over Z_10, an orthomorphism of Z_10 (substitute y = u x), which does
  not exist. Zhang-Cao's 17 open orders (10, 14, ..., 94) are exactly orders = 2 mod 4 left by these routes. None of the
  sources states a nonexistence result for QLS orthogonal to Cay(Z_n), n even; Huang-Li list MCPQLS(n) with
  gcd(n,6) != 1 (pandiagonal in both directions, stronger than our condition) as undetermined.
- Imported small cases (Zhang-Cao Sec. 3, citing Ball-Simoens): every 1-RQLS(4) and 1-RQLS(5) is classical (cardinality
  v); no 1-RQLS(6) exists. Hence no 1-RQLS(v) with B = Cay(Z_v) for v = 2, 4, 6. No positive instance with an
  even-order cyclic B is known to me; v = 8 is the first even order where it is open to me (S8 probe below).
- Han-Zang-Zhang-Tian construct non-classical 2-MOQLS(v) for v >= 8 (v = 10 from an ISOLS(10;3) by filling holes); that
  is not stated as a 1-RQLS and is not a no-go.
- Written observation (mine, unreviewed): the classical parity proof does not transfer. If the classes {j - i = s} of a
  QLS are orthonormal bases, then with P_ij = |q_ij><q_ij| and integer labels, sum_ij (j - i) P_ij = 0 (row and column
  sums are I) while sum_ij ((j - i) mod n) P_ij = (n(n-1)/2) I (class sums), hence sum_{j < i} P_ij = ((n-1)/2) I.
  Classically the left side has integer eigenvalues (multiplicities), which forces n odd; quantumly it only says that
  the n(n-1)/2 rank-one projectors of the strictly lower triangle form a tight frame with bound (n-1)/2, which the trace
  allows (both sides have trace n(n-1)/2). For n = 2 it excludes (one rank-one projector cannot equal I/2), consistent
  with the import; for n >= 4 it is not an obstruction by itself.
Screen verdict: no quantum Hall-Paige / quantum complete-mapping no-go for Cay(Z_10) found; the classical obstruction
removes all classical points but its proof mechanism does not carry over.

## 4. Choice of B and headroom
- Primary target B = Cay(Z_10) in the diagonal convention B(i,j) = (j - i) mod 10. It is the order-10 member of the
  group-table resolutions on which every known maximal construction lives (Huang-Li cyclic, odd v; Zhang-Cao Z_2 x Z_m
  with m = 5 gives exactly this B; Ball-Simoens), and those constructions fail at v = 10 only at the classical
  complete-mapping step. Headroom: (a) no classical attractor exists for this B, so every verified endpoint is
  non-classical; (b) at the analogous v = 7 cyclic point the solution is first-order isolated modulo gauge (excess 0)
  and at the v = 8 XOR point first-order excess is 6 (receipt above), so maximal points can be isolated or come in
  families - no counting argument predicts either way at v = 10; (c) risk: even-order cyclic B has no known positive
  instance (v = 2, 4, 6 negative by imports), which the v = 8 Cay(Z_8) probe tests at the next even order.
- Secondary target B = Cay(D_5), B(i,j) = index(g_i^-1 g_j), the only other group of order 10 (same Hall-Paige status).
- Not chosen as targets: squares with classical mates (Parker-type, Z9+1). Their classical points are rigid in the
  restricted models and attracted every earlier search (R9, v7, v8); the Parker pair-0 B is used here only as the v = 10
  recovery calibration (classical point = known solution of the same model).

## 5. Calibration ladder and target (code/rqls_fixedb_lm_v1.py 5a4e7956...895e, frozen, NOT run)
S (gate): input pins; Jacobian vs central differences at Haar-random U for cyclic v = 4, 5, 7, 10, XOR v = 8, Cay(D_5)
(< 1e-9 rel.); block normal equations vs dense at v = 5, 7 (< 1e-12); retraction unitarity; float anchors Huang-Li v = 7
(49 rays), Zhang-Cao v = 8 (64 rays), classical Parker v = 10 (10 rays) with residual and full Gram < 1e-12, U_0 = I, and
a failing mutation. N (gate): Cay(Z_4), Cay(Z_6): 0 verified (imports). C (gate): Cay(Z_5): every verified endpoint has
5 rays (import). KP (gate): near-anchor recovery at the three anchors, amp 1e-3, 1e-2, 0.1, 0.3 x 4 seeds; all amp <=
1e-2 runs verified with 49 / 64 rays (v = 10: verified, rays recorded). KR (no count gate): random starts on the cyclic
v = 7, XOR v = 8 and Parker v = 10 B's (recovery of KNOWN classes - not v = 10 detection power). S8 (recorded): v = 8,
B = Cay(Z_8). Targets W = Cay(Z_10), WD = Cay(D_5) random starts; WS = starts seeded at verified non-maximal W/WD
endpoints. Every endpoint: full float Gram of all 3v lines; "verified" in the run = float deviation < 1e-8 (a numerical
screen only); rays counted (merge 1 - |<q,q'>|^2 < 1e-7, minsep recorded).

## 6. Stop rules (copied from rqls_wh10_lm_v2) and verification of any candidate
- In run: v = 10 endpoint (ANY stage) float-verified with 100 rays and minsep > 1e-6 -> U, B, seed written at full
  precision, flush, IMMEDIATE exit 7 (CANDIDATE_UNVERIFIED_STOP receipt). LM residual < 1e-10 with full deviation >= 1e-8 -> U written,
  exit 8. Gate failure -> exit 3; output cap 8 MiB -> 4; SIGTERM -> 5; no GO line -> 6.
- After a stop 7, before any statement: (i) exact rational evaluation of the stored doubles (all 30 Gram matrices and
  all 4,950 pairwise ray margins) and (ii) 60-digit Newton-Schulz + chord Gauss-Newton refinement followed by the full
  Gram check at high precision, both by code/fixedb_candidate_verify_v1.py (9b915c42...6735; selftest receipt
  evidence/fixedb_candidate_verify_v1.selftest.receipt.md 3a1321cc...6db4: perturbed v = 7 / 8 anchors refined to
  5e-61 / 6e-69, negative control rejected). Step (ii) at v = 10 may exceed 300 s in pure Python and is then run only
  under a parent GO. (iii) Independent exact/algebraic or certified-interval verification (the contract's three
  independent checkers, chosen by the parent). Boundary: 60-digit residuals plus a near-zero full Gram (status REFINED)
  are numerical CANDIDATE evidence only, never labelled VERIFIED and not an existence certificate; no existence
  statement before (iii).

## 7. Claims discipline
Target misses are a scoped UNKNOWN for this model and these B's, never nonexistence. Recovery rates (KP, KR) are not
detection power for maximal v = 10 basins. A verified non-maximal Cay(Z_10) / Cay(D_5) endpoint would be recorded as a
numerical observation only. No novelty or priority claims; one implementation is not independent verification.
