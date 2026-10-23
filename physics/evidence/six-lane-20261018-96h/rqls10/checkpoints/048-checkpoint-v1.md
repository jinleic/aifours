# Physics-2 checkpoint048 - W8 written slice: derivation complete in working form, note being written

Actual `/bin/date` before this write: 2026-10-19T16:46:24-0700. Previous checkpoint047 16:33:49 (12m35s). Next target
17:06:24, binding 17:16:24.

## Actual partial result (derived after the scope freeze 00-scope-freeze-v1.md 79394cc6...7c12; being written with full
proofs into continuations/wh5-c2-written/01-...; unreviewed, single author)
1. Exact reduction of all 30 row / column / transversal ONB conditions to the representative conditions over the
   three eigenbases Z, X, T = eig(X Z^-1) (g_m(t) = zeta^(2t^2 + m t)/sqrt5), via character orthogonality; Gram lemma
   re-proved.
2. Ray distinctness: the 25 rays of one orbit are always distinct (rank-2 argument); two orbits either coincide as ray
   sets or are disjoint; cardinality in {25, 50, 75, 100}; maximal iff 120 explicit inequations |tr(X_r^* W_w X_s)| < 1
   (w outside the line of the couple's basis); all 30 on-line traces vanish automatically.
3. Equivalent system: one flat plane P and antiunitary involutions A = D K, B = C_X Pi K, C = Q C_T Q Pi K (D diagonal,
   C_X, C_T circulant unitaries, Q = diag(zeta^(2t^2))) with image flatness and diag_Z(BPC) = diag_X(APC) = diag_T(APB) = 0.
4. Triangle identity Theta V = V J (Theta = product of the three couple maps), so Theta^2 = -1 on the plane; Kramers
   parity in dimension 5 then excludes every triangle whose three couple maps are of Weyl-Heisenberg type.
5. NEW, import-free: a vector unbiased to Z, X and T is (up to phase) one of the 15 complementary-basis vectors
   (lag-one autocorrelations of X and T kill two Fourier coefficients of the unimodular ratio sequence; constant
   modulus on the remaining frequency window {1,2,3} forces one character). Consequences: a flat plane containing such
   a vector, or of the form span(u, W u) with W Weyl-Heisenberg, is a MUB-pair plane; the couple partner of a MUB-pair
   plane is a MUB-pair plane WITHOUT the earlier Haagerup import; with Theorem A (re-proved) NO representative plane
   of any W8 solution is a MUB-pair plane (unconditional; supersedes the conditional Proposition B).
Outcome class so far: UNRESOLVED (no witness; no ansatz-wide no-go): the remaining exact system is the non-MUB-pair
flat-plane case.

## Scope / constraints
No computation, CLI tool (other than `/bin/date` and hashing), import, test or nested agent. Float W8 evidence cited
only, not re-run, not a premise. Guard package v9 untouched/NOEXEC. Target OPEN / UNKNOWN; no unrestricted claim.
