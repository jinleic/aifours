# phys-2 slice: flat rank-2 planes OUTSIDE the explicit family F - scope freeze v1 (BEFORE derivation)

Recorded after actual `/bin/date`: 2026-10-19T21:25:39-0700. Author ContinueRQLS10b. Lane-internal, single author.
Authority: RUN/control/written-RQLS10-outside-F-transition-v1.json
(c327f30ca5cadbf9fba6ff9fa5ae1ad4af8be8ae01500c4193f1bff22843c962) plus the parent IRC. Written only; runtime HOLD.
Immutable, not edited: package v9 / full matrix / supervisor19 and every earlier file, in particular
continuations/wh5-c2-written/*, wh5-flat-plane-classification/* (E1 candidate f41c5326...cdbe),
wh5-exact-plane-couples/* (internal-F candidate c625b377...08ec), wh5-family-couple-closure/* (closure candidate,
receipt ba334147...c396), continuations/guard-v10-repair/ (not created by this slice).

## Frozen objects and exact equations
zeta = e^(2 pi i/5); bases beta_Z = (e_t), beta_X = (f_m), f_m(t) = zeta^(mt)/sqrt5, beta_T = (g_m),
g_m(t) = zeta^(2t^2 + mt)/sqrt5 (indices mod 5). A FLAT PLANE is a rank-2 orthogonal projector P on C^5 with
  (Fl) e_t^* P e_t = f_m^* P f_m = g_m^* P g_m = 2/5 for all t, m.
Equivalent exact form (to be re-proved inside this package, not imported): with phi_a(t) := P_(t+a,t),
  P_(t,t) = 2/5, and for a = 1, 2: sum_t phi_a(t) = 0 and sum_t phi_a(t) zeta^(-4at) = 0,
plus P^2 = P, tr P = 2. Real count: Gr(2,5) has dimension 12; (Fl) imposes 12 independent real conditions.
MEMBERSHIP IN F (definition only): P in F iff P = D_w P_tau D_w^* for some w = (a,c) in Z_5^2 (D_w = X^a Z^c) and
tau in {+-1}^2, with P_tau the frozen explicit projectors of wh5-exact-plane-couples/00-scope-freeze-v1.md
(c29b8bf7...877a). No property of F (flatness, U-invariance, closure, internal-F exclusion) is assumed; "outside F"
means a flat plane equal to none of these 100 matrices. NO assumption that flat implies F.
Couple data to retain for any plane exhibited: labels (w, any symmetry label), all phases, and for b in {Z,X,T} the
full antiunitary sets {A in Anti_b : A P A flat} as circles/unions of circles, Anti_b = {D K_b : D diagonal in beta_b}.

## Questions (in this order) and allowed outcomes
Q1. Exact elementary non-F flat planes: verify in writing that every plane spanned by two orthonormal vectors of a
    basis unbiased to beta_Z, beta_X, beta_T is flat, and decide its membership in F without importing E1.
Q2. Symmetry: the finite group G of unitaries/antiunitaries permuting {beta_Z, beta_X, beta_T} up to vector phases
    (modulo scalars) acts on flat planes; determine G exactly as far as needed and classify the flat planes with a
    NONTRIVIAL stabiliser in G (by conjugacy class of stabiliser elements), with complete proofs.
Q3. General case: a complete classification of flat planes, OR an exact obstruction/parametrization of flat planes
    with trivial stabiliser, OR an exact new flat plane outside F and outside Q1 (written verification).
Outcomes (exactly one, stated with its precise scope): CLASSIFICATION | PARTIAL (exact classification of an explicitly
delimited subfamily + exact remaining equations) | CANDIDATE (exact new non-F flat plane) | GAP.
Not in scope / never claimed: full W8; anything about unrestricted 1-RQLS(10) (OPEN / UNKNOWN); novelty/priority.

## Knowledge exposure (disclosed; none is a premise)
1. Lane float evidence (not re-run): LM searches reported exactly 130 flat planes (30 "MUB-pair" + 100 "exotic"),
   suggesting that flat = MUB-pair union F. Expectation: no further planes; float data cannot prove this.
2. My unreviewed candidates: E1 (U-invariant planes of type (-omega line)+(-omega^2 line) are exactly the four P_tau;
   no U-invariant plane is MUB-pair), W8 slice (MUB-pair representatives excluded from W8), internal-F E2/E3, and
   F-closure. They may appear only as named conditional hypotheses; every fact used is re-derived here.
3. Pre-freeze thoughts (during 21:25, nothing written): the dimension count above; reformulation P = V V^* with the
   rows of the 5 x 2 isometry V in each basis forming an equal-norm tight frame (five Bloch vectors of length 2/5
   summing to zero per basis); Q1 planes are flat trivially; a stabiliser-type classification via G (Q2) looks
   tractable by hand, while a full classification (Q3) may not be; then report PARTIAL or GAP honestly.

## Constraints
No scripts, assertions, symbolic computation, floating search, enumeration; CLI only /bin/date, shasum, chmod, wc
(metadata). No tests, imports, nested agents. Decimals only as orientation, never proof steps. Files exclusive in
continuations/outside-F-flatplanes/, frozen 0444; corrections only in new versioned files. Package <= 100 KB,
SHA-256 receipt, checkpoints <= 1800 s (target 1200).
