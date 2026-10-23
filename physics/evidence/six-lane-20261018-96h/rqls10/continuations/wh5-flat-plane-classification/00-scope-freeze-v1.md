# phys-2 E1 written slice: are all Z/X/T-flat planes MUB-pair planes? - scope freeze v1 (BEFORE derivation)

Recorded after actual `/bin/date`: 2026-10-19T17:19:25-0700. Author ContinueRQLS10b. Lane-internal, single author.
Authority: RUN/control/written-slot-transitions-sun-physics-20261019-1700-v1.json
(b29119aa12222bf31cdaf6afdb59e81bc58ad2525fa9e08c5384bf86bc7d6bf2), slot phys2, plus the parent IRC of that transition.
Global HOLD unchanged; no launch authority. Package v9 / full matrix / supervisor19 and the W8 written slice
(continuations/wh5-c2-written, all 0444) stay immutable and are not edited.

## Frozen question (closure item E1 only; not RQLS(10))
zeta = e^(2 pi i/5); on C^5: X e_t = e_(t+1), Z e_t = zeta^t e_t; bases beta_Z = (e_t), beta_X = (f_m),
f_m = 5^(-1/2) sum_t zeta^(mt) e_t, beta_T = (g_m), g_m = 5^(-1/2) sum_t zeta^(2t^2+mt) e_t (eigenbasis of X Z^-1).
A "flat plane" is a rank-2 orthogonal projector P with v^* P v = 2/5 for every v in beta_Z u beta_X u beta_T. A
"MUB-pair plane" is span(psi^k_m, psi^k_m'), k in {1,2,3}, m != m', psi^k_m = 5^(-1/2) sum_t zeta^(3k t^2 + mt) e_t.
Question: is EVERY flat plane a MUB-pair plane?

## Admissible outcomes (exactly one)
NO  - an EXACT flat non-MUB-pair plane, given in closed form (algebraic numbers), with complete hand verification of
      rank 2, idempotence/orthogonal projection, all 15 diagonal values 2/5, and non-MUB-pair-ness.
YES - an exhaustive written classification proof.
GAP - exact statement of the elimination gap reached.

## Knowledge exposure (disclosed; none is a premise)
1. Lane float evidence (not re-run, not a premise): LM searches found 130 flat planes = 30 MUB-pair + 100 others
   ("exotic"), 4 WH-translation orbits of 25; each exotic plane commutes with exactly one of 25 conjugates
   W_w U W_w^* of an order-3 Clifford U := Q X Q F (Q = diag(zeta^(t^2)), F_(j,t) = zeta^(-jt)/sqrt5), U cycling the
   bases Z -> T -> X -> Z, eigen-multiplicities (1,2,2); each exotic plane = (line in omega-eigenspace) (+) (line in
   omega^2-eigenspace); block coefficients include 1 - sqrt5 numerically. Sources: evidence/w8-decision-v1.md section 6,
   evidence/w8-decision-v1-addendum-1.md section 1. I therefore EXPECT outcome NO and will aim for an exact
   U-symmetric example; the expectation is not evidence.
2. My own W8 written slice (unreviewed): Lemma 10 (vectors unbiased to Z, X, T are the 15 complementary vectors),
   Corollary 11, flat-plane normal form idea. Re-proved here if used.
3. evidence/wh10-flat-planes-v1.md Proposition F5 (C-symmetric planes: affine conditions on Bloch vectors in
   eigenspaces) - an analogous reduction idea for a different triple; context only.
No other prior sketch of this specific computation exists. Pre-freeze thought (16:55-17:19, nothing written): use
U-invariance to transport Z-flatness to X and T; parametrise l_omega, l_omega^2 inside the 2-dim eigenspaces.

## Constraints
Written math only: no scripts, assertions, enumeration, probes, CLI (other than /bin/date, shasum, chmod), tests,
nested agents, runtime. No Haagerup classification import. Named imports: character orthogonality on Z_5, Gauss sums
(re-proved inline if needed), elementary linear algebra, Weil/Clifford facts only if re-derived. Package <= 100 KB,
new files exclusive and 0444, full SHA-256 receipt, checkpoints <= 1800 s (target 1200 s), park after delivery.
