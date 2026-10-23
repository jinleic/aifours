# Physics-2 checkpoint050 - E1 slice: exact counterexample derived (working form), note being written

Actual `/bin/date` before this write: 2026-10-19T17:27:08-0700. Previous checkpoint049 16:53:59 (then parked; resumed by
the parent IRC for RUN/control/written-slot-transitions-sun-physics-20261019-1700-v1.json b29119aa...6bf2 about 17:05).
Next target 17:47:08, binding 17:57:08.

## Actual state
- Scope frozen before derivation: continuations/wh5-flat-plane-classification/00-scope-freeze-v1.md
  (e925c1a4ddd1d6a591cab3b721c140121f326d7a0cd00c9a3d7908a75f1f0f85, 0444), with knowledge exposure disclosed (float
  evidence of 100 U_w-invariant exotic planes; expectation of outcome NO, not a premise).
- Derived by hand (to be written with full proofs in 01-...): U := Q F^* (Q = diag(zeta^(2t^2)), F e_m = f_m) satisfies
  U e_s = g_(-s), U g_(-s) = -zeta^(3s^2) f_s (Gauss sum G(2) = -sqrt5), U f_s = zeta^(2s^2) e_s, U^3 = -I; it cycles the
  bases Z -> T -> X and the complementary lines L_1 -> L_3 -> L_2. Explicit eigenvectors v = e_s - mu^2 g_(-s) -
  mu zeta^(3s^2) f_s (eigenvalue -mu, mu in {omega, omega^2}); even/odd vectors a, b in each 2-dim eigenspace with all
  moduli in the real subfield of Q(zeta_15). Exact solution: p = 3(5 - sqrt5)/20, x = sqrt(p) a^ + i zeta sqrt(1-p) b^,
  y = sqrt(p) a'^ + i zeta sqrt(1-p) b'^; P = xx^* + yy^* has Z-diagonal 2/5 (hand-verified: t = 0 and t = +-1, +-2 give
  (11 - 3 sqrt5)/40 + (5 + 3 sqrt5)/40 = 2/5), is U-invariant (so flat in X and T), and is NOT a MUB-pair plane
  (U-invariance + Weyl diagonal argument). Outcome class (pending write-up): NO - not every flat plane is a MUB-pair plane.
- No computation, scripts, CLI (other than /bin/date, shasum, chmod), imports, tests or nested agents used.

## Scope
Restricted to closure item E1 (flat-plane question); nothing about W8 solutions or unrestricted 1-RQLS(10) (OPEN / UNKNOWN).
Package v9 / full matrix / W8 slice untouched. Global HOLD unchanged.
