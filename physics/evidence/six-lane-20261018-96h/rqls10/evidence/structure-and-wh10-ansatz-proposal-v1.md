# Structural constraints on maximal 1-RQLS(10) (scoped) and one new ansatz with built-in controls (proposal, not run)

Recorded 2026-10-19T02:39:32-0700 (from /bin/date). Author ContinueRQLS10b. Lane-internal, unreviewed; every item names
its ansatz; the target stays OPEN / UNKNOWN; no novelty claim.

## A. What a maximal solution needs that the classical / forced-symmetric points found so far do not have
1. Classical points (q_p = e_(L(p)), L a Latin mate of the resolution B) have exactly 10 rays; a maximal solution has
   100. In the pair-graph theory (evidence/classical-tangent-theory-v1.md, 733e4548...a375) the unsymmetric excess at a
   classical point is 2 sum_(a<s) (c_(a,s) - 1). Hence a classical point can lie on a curve of NON-classical solutions
   only if some pair graph G_(a,s) is disconnected (an independent 2-symbol trade). The 40 classical Z_9+1 points have
   all G_(a,s) connected (excess 0, receipt classical_tangent_count_z9_v1): no non-classical 1-RQLS(10) of any
   cardinality lies near them, in the FULL unsymmetric solution set. The 10 Parker-type Z_7+3 points have excess_forced 0
   (isolated inside the forced Z_7+3 ansatz; unsymmetric excess 6 there).
2. Forced Z_7+3 (W2 Lemma 5): maximality forces U to have eigen-multiplicities (2,2,2,1,1,1,1) with the three corner
   mate classes in distinct 2-dimensional eigenspaces and nine distinct corner rays; at the classical forced-form points
   each mate class collapses to ONE ray (W2 erratum 1). Forced Z_9+1 (W2 Lemma 6): one 2-dimensional eigenspace E_m*
   holding the corner ray, and P_m* u, P_m* w, P_m* w' all equal to the complement of the corner in E_m*.
3. B = Cay(Z_10) (= Cay(Z_5 x Z_2)) has no classical solution at all (Z_10 has no transversal, Hall-Paige), so every
   1-RQLS with this B is non-classical. The symmetric families tried for it are excluded or empty so far: R3 (flat
   Fourier-permutation), R4 (three of the four cocycle classes of the Z_10^2 orbit ansatz), R11 (linear Z_5^2 orbit),
   W8 (WH_5 (x) C^2 orbit: Theorem A of evidence/w8-decision-v1.md, b24334cf...5829, kills every configuration with three
   stabilizer-type (MUB-pair) planes; the float evidence leaves no solution). A recurring mechanism: discrete
   (Clifford / root-of-unity) phase structure meets the Z_2 part of Z_10 and produces a parity contradiction
   (-1 = zeta^c impossible): R11, addendum-1 Proposition 3, Theorem A, and classically Hall-Paige. [INFERENCE] A maximal
   solution with B = Cay(Z_10), if any, needs non-Clifford phases; within W8 the only non-stabilizer flat planes seen are
   the 100 "exotic" ones, and they do not couple into a K4 pattern (float evidence).

## B. Proposed new ansatz: the WH_10 single-orbit ansatz (the open fourth cocycle class of R4)
Definition. B = Cay(Z_10), q_(i,j) = D_(i,j) x for ONE unit vector x in C^10, where D_(a,c) = X^a Z^c are the
Weyl-Heisenberg operators of Z_10 (X e_t = e_(t+1), Z e_t = omega^t e_t, omega = e^(2 pi i/10)). This is the
irreducible-cocycle case of the Z_10^2 projective orbit ansatz that R4 left UNKNOWN (r-items-validation-v1.md). It is
materially different from W8 (there Z_5^2 acts by WH_5 (x) I_2 with four representatives; here the Z_2^2 part acts by
the Pauli group and there is a single representative) and from all forced Z_n + h ansatze.
Exact reduction (written; short proof). Row i: {X^i Z^j x}_j is orthonormal iff {Z^j x}_j is, iff |x_t|^2 = 1/10 for
all t. Column j: X^i Z^j = omega^(-ij) Z^j X^i, so iff |hat x_k|^2 = 1/10 (Fourier basis). Class s (cells (i, s - i)):
X^i Z^(s-i) = omega^(-is) Z^s (X Z^-1)^i up to i-dependent phases, so iff x has flat modulus in the eigenbasis of
X Z^-1 ((X Z^-1)^10 = -I, ten distinct eigenvalues). So: 1-RQLS(10) in this ansatz  <=>  x unbiased to the three
Weyl-Heisenberg bases Z, X, X Z^-1 of C^10 (in particular x is a bi-unimodular sequence of length 10). Cardinality:
maximal iff x is an eigenvector of no D_w, w != 0 (automatic for w in the three used cyclic subgroups by flatness).
Size: 20 real unknowns (19 mod phase), 30 modulus conditions (27 independent); tiny.
Built-in controls (same reduction and code path, dimension d as the only parameter):
- NEGATIVE: d = 2 (Pauli bases; a pure qubit state cannot have <sigma_x> = <sigma_y> = <sigma_z> = 0: exact, no import)
  and d = 6 (no vector, since its existence would give a 1-RQLS(6); IMPORT no 1-RQLS(6), as gate C1 of v7/v8): the
  solver must report no solution.
- POSITIVE: d = 5, 7 and 9 (odd): exact anchors x_t = omega_d^(a t^2 + b t)/sqrt d with gcd(2a, d) = gcd(2a + 1, d) = 1
  (Gauss sums; for prime d these are the eigenvectors of X Z^k, k not in {0, -1}; for d = 9 take a = 2 mod 3) are unbiased
  to Z, X, X Z^-1; the reduced residual must vanish at them to 1e-12 (exact-anchor gate), the full d x d verification
  must pass, and random-start recovery is recorded (calibration of the solver only; it does not transfer to maximal
  d = 10 basins).
- TARGET: d = 10, any cardinality, rays counted; a numeric 100-ray lead is frozen and handed to exact recognition.
Status. Not run. A float search here is a numerical programme item and needs a parent GO (frozen source/config,
fresh stability gate + owned supervisor); exact follow-ups (bi-unimodular sequences of length 10, i.e. unimodular
cyclic 10-roots, tested against the X Z^-1 basis) are written/exact work that needs no GO.
