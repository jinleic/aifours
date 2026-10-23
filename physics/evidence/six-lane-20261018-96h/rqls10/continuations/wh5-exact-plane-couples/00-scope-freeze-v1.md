# phys-2 E2/E3 written slice: couple compatibility of the exact U-invariant flat planes - scope freeze v1

Recorded after actual `/bin/date`: 2026-10-19T17:43:24-0700. Author ContinueRQLS10b. Lane-internal, single author.
Authority: RUN/control/written-rqls10-exact-plane-couple-transition-v1.json
(2449f8e15327fe63d011e51e6d248f938008395c4a279433e14be811be76aef1) plus the parent IRC. Written only; runtime HOLD.
Immutable and not edited: package v9 / full matrix / supervisor19, continuations/wh5-c2-written/*,
continuations/wh5-flat-plane-classification/* (E1 candidate f41c5326...cdbe, UNREVIEWED, not a premise), and the
directory continuations/guard-v10-repair/ (not created by this slice; not touched).

## Frozen objects and equations
Notation as in the E1 candidate (zeta = e^(2pi i/5), bases beta_Z = (e_t), beta_X = (f_m), beta_T = (g_m), Q =
diag(zeta^(2t^2)), U = Q F^*, D_(a,c) = X^a Z^c, lines L_Z, L_X, L_T, couples M_Z = {00-01, 10-11},
M_X = {00-10, 01-11}, M_T = {00-11, 01-10}). The family F (DEFINITION, no property assumed):
F := { D_w P_tau D_w^* : w in Z_5^2, tau = (sigma, sigma') in {+-1}^2 }, P_tau := x x^* + y y^* with
  x = (e, zeta(-g + i sigma bb), zeta^4(-d + i sigma aa), zeta^4(-d - i sigma aa), zeta(-g - i sigma bb)),
  y = (e, zeta(-d + i sigma' aa), zeta^4(-g - i sigma' bb), zeta^4(-g + i sigma' bb), zeta(-d - i sigma' aa)),
  e = 1/sqrt5, g = c gamma, d = c delta, bb = s sqrtB, aa = s sqrtA, c = sqrt((3 - sqrt5)/40), s = sqrt((3 + sqrt5)/120),
  alpha, gamma, beta, delta = 2cos(2pi k/15) for k = 1, 2, 4, 7, A = sqrt5 + alpha - delta, B = sqrt5 + beta - gamma.
Anti_b := {D K_b : D unitary diagonal in beta_b}, K_b complex conjugation in beta_b.
(E2) For P, P' in F and b in {Z, X, T}: C_b(P, P') := {A in Anti_b : A P A = P'}. Deliverable: C_b(P, P') exactly for
     all 100 x 100 x 3 cases (all phases of the diagonal/circulant part retained; frames: every isometry V with V V^* = P
     and its partner A V J).
(E3) If compatible pairs allow, the K4 system: four planes S_r in F with C_(b(r,s))(S_r, S_s) nonempty for all six pairs
     and the frame consistency; then either an exact W8 construction with distinct rays or exclusion of
     "all four representative planes in F". Necessary-condition basis: W8 reduction (re-derived in this package):
     every couple {r, s} of a W8 solution has P_s = A P_r A with A in Anti_(b(r,s)).

## Outcomes (exactly one)
CONSTRUCTION (exact W8 solution with four planes in F, distinct rays proved) | EXCLUSION (no W8 solution, of any
cardinality, has all four representative planes in F) | OBSTRUCTION (exact remaining compatibility statement).
Explicitly NOT claimed in any case: that F exhausts the flat planes; anything about W8 solutions with a plane outside F;
anything about unrestricted 1-RQLS(10) (OPEN / UNKNOWN).

## Knowledge exposure and prior sketches (disclosed; none is a premise)
1. Float evidence (lane, not re-run): each "exotic" plane had exactly 5 compatible exotic partners per basis, stabiliser
   labels of compatible b-couples differ by L_b, and 0 all-exotic K4 patterns (evidence/w8-decision-v1-addendum-1.md).
   I therefore EXPECT outcome EXCLUSION.
2. My unreviewed W8 slice (Theorems 1, 4, 5: reduction, antiunitary couple maps) and E1 candidate (U, eigenvectors,
   coordinates). Every fact used is re-derived in this package.
3. Pre-freeze mental sketch (17:36-17:43, nothing written): Q conj(P_tau) Q^* = P_(-tau); Z-couples of P_tau are diagonal
   conjugates of P_(-tau); moduli |P_(t,t')| are invariant under diagonal conjugation; a cyclic-distance invariant
   separating {++,--} from {+-,-+}; non-coplanar row Bloch vectors exclude E P_(-tau) E^* = P_tau; U transports Z to T to X;
   hence every couple flips tau and a K4 triangle (three couples) gives a parity contradiction. Unverified until written.

## Constraints
No scripts, assertions, symbolic computation, floating search, CLI beyond /bin/date, shasum, chmod; no tests, imports,
nested agents. Decimal approximations may appear only as orientation, never as proof steps; every inequality used is
proved from exact bounds. Package <= 100 KB, files exclusive and 0444, SHA-256 receipt, checkpoints <= 1800 s.
