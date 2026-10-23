# phys-2 slice: closure of the family F under all flat couple maps - scope freeze v1

Recorded after actual `/bin/date`: 2026-10-19T17:59:49-0700. Author ContinueRQLS10b. Lane-internal, single author.
Authority: RUN/control/written-sun56-import-cutover-and-E2-closure-v1.json
(e1317e565a1c6218dbd594ec6530f76080a41d9fefab559e8639b60578990193), slot phys2, plus the parent IRC. Written only;
runtime HOLD. Immutable, not edited: package v9 / full matrix / supervisor19; continuations/wh5-c2-written/*,
wh5-flat-plane-classification/*, wh5-exact-plane-couples/* (the internal-F candidate c625b377...08ec, UNREVIEWED, not
a premise); continuations/guard-v10-repair/ (not created by this slice).

## Frozen question and exact equations
Notation and the family F = {D_w P_tau D_w^*} exactly as in wh5-exact-plane-couples/00-scope-freeze-v1.md
(c29b8bf7...877a): P_tau = x x^* + y y^*, x_t = zeta^(t^2) X_t, y_t = zeta^(t^2) Y_t with the explicit X, Y there.
(Q) For each tau and each diagonal unitary E (modulo a global phase), decide exactly when P' := E P_(-tau) E^* has
    f^* P' f = 2/5 for all f in beta_X and g^* P' g = 2/5 for all g in beta_T (beta_Z is automatic). Equivalently, with
    psi_a(t) := P'_(t+a,t) (a = 1, 2) and hat(psi)(c) = (1/5) sum_t psi(t) zeta^(-ct):
      hat(psi_1)(0) = hat(psi_1)(4) = 0 and hat(psi_2)(0) = hat(psi_2)(3) = 0  (columns 3, 4 are adjoint).
    Unknowns: w(t) := e_(t+1) conj(e_t) (unimodular, product 1), psi_1 = w * phi_1, psi_2(t) = w(t) w(t+1) phi_2(t),
    phi_a(t) := (P_(-tau))_(t+a,t).
Closure statement to prove or refute: (Q) holds only for E = lambda Z^c (then P' = Z^c P_(-tau) Z^(-c) in F). Extension
to all WH translates and all bases via proved conjugations (WH covariance; U, U^2 transport). Consequence if proved:
a W8 solution with one representative plane in F would be excluded, CONDITIONAL on separate review of the internal-F
theorem. If refuted: an exact outside-F flat partner with written verification.
Allowed outcomes: CLOSURE (proof) | NON-CLOSURE (exact partner) | GAP (exact remaining obligation).
Not in scope: classification of all flat planes; full W8; 1-RQLS(10) (OPEN / UNKNOWN).

## Knowledge exposure and pre-freeze sketch (disclosed; none is a premise)
1. Float evidence (lane, not re-run): LM searches found exactly 130 flat planes (30 MUB-pair + 100 others) in three
   independent runs; suggests closure (every flat diagonal conjugate would be among them). Expectation: CLOSURE.
2. My own unreviewed slices (E1, internal-F E2/E3); facts used will be re-derived or stated as explicit hypotheses.
3. Pre-freeze mental sketch (17:51-17:59, nothing written): (a) column-a reformulation above; (b) column 1 is a
   degree-2 phase-retrieval problem: psi_1 = zeta^(t) f(zeta^t) with f of degree 2, |psi_1| fixed, so (by the
   Fejer-Riesz zero-flipping description of polynomials with prescribed modulus on the circle) at most four classes
   modulo phase: the trivial one, the conjugate-reversed one, and two single root flips; column 2 likewise after the
   dilation t -> 2t; (c) the symmetry E -> Pi conj(E) Pi (from the antiunitary Pi Q K, which fixes P_(-tau) and swaps
   X and T) exchanges the two single-flip classes; (d) column 2 is determined by column 1 through the Z-triangle
   (Bargmann) invariants P_(t+2,t) P_(t,t+1) P_(t+1,t+2); (e) for the conjugate-reversed class this gives a single
   complex test equation in the imaginary parts of three triangle invariants; (f) the single-flip classes need the roots
   of K1 Y^2 + K2 Y + K1 (K1, K2 explicit) - possibly not tractable by hand. All unverified until written.

## Constraints
No scripts, assertions, symbolic computation, floating search, CLI beyond /bin/date, shasum, chmod; no tests, imports,
nested agents. Decimal values only as orientation, never as proof steps; inequalities proved from exact bounds. Every
non-standard imported theorem named at point of use. Package <= 100 KB, files exclusive and 0444, SHA-256 receipt,
checkpoints <= 1800 s.
