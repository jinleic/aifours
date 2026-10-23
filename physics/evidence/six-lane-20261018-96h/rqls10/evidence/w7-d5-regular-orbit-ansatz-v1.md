# W7: the D_5 regular-orbit ansatz survives representation theory (written reduction, v1)

Recorded 2026-10-19T00:49:42-0700. Lane-internal derivation by ContinueRQLS10; unreviewed; restricted ansatz; no existence claim.

**Ansatz.** B = Cay(D_5) (B(g,h) = gh). K = D_5 x D_5^op acts regularly on cells by (x,y).(g,h) = (xg, hy), preserving
rows, columns and classes; via (x,y) -> (x, y^-1), K = G x G (G = D_5). Put q_(g,h) = pi(g, h^-1) q_0 for a unitary
projective representation pi of G x G on C^10. Then (up to unitaries pi(g,1), pi(1,h^-1), pi(1,s^-1)) the 30 lines are
the orbits of q_0 under G x 1 (columns), 1 x G (rows) and the diagonal Delta = {(g,g)} (classes). Hall-Paige: Cay(D_5)
has no transversal, so any solution is non-classical. (The abelian analogue G = Z_10 is R4.)

**Conditions.** {pi(h) q_0 : h in H} is an orthonormal basis for H in {G x 1, 1 x G, Delta} iff pi restricted to H is
(projectively equivalent to) the regular representation of D_5 = 1 + eps + 2 rho_1 + 2 rho_2 and q_0 has scaled-unitary
isotypic components.

**Classification of pi.** H^2(D_5 x D_5, U(1)) = Z_2 (Kuenneth term Hom(Z_2 (x) Z_2, U(1)); D_5 has trivial multiplier).
- Linear pi = sum rho_a (x) rho_b: the two factor restrictions force a dimension-preserving matching
  pi = (+)_a rho_a (x) rho_sigma(a); the Delta-restrictions (tensor products) are never regular (direct check of the
  four matchings: the trivial or sign character always has multiplicity >= 2).
- Nontrivial class alpha (s_1 = (s,1) and s_2 = (1,s) anticommute projectively). Clifford theory over N = Z_5^2 gives
  the alpha-irreducibles: P (dim 2, N trivial, s_1, s_2 as anticommuting Paulis), A_(j,+-) and B_(k,+-) (dim 2, from
  characters (+-j,0), (0,+-k)), C_(j,k) (dim 4, j,k in {1,2}); sum of squares 4 + 16 + 16 + 64 = 100.
  Factor restrictions: P -> 1+eps on both; A_(j) -> rho_j on factor 1 and 1+eps on factor 2; B_(k) symmetric;
  C_(j,k) -> 2 rho_j on factor 1 and 2 rho_k on factor 2. Regularity of both factor restrictions forces
  pi = P + C_(1,1) + C_(2,2) or pi = P + C_(1,2) + C_(2,1) (a P-free choice needs a half-integer multiplicity).
  On Delta the rotation (r^a, r^a) acts on character (j,k) by zeta^((j+k)a); C_(1,1) and C_(2,2) contribute only one
  rho each plus 1-dimensional pieces, while C_(1,2) and C_(2,1) each restrict to rho_1 + rho_2, and P restricts to
  1 + eps after removing the coboundary of the alpha restricted to Delta. Hence **pi = P (+) C_(1,2) (+) C_(2,1)** is the
  unique representation class compatible with the ansatz, and it is compatible with all three subgroups.

**Remaining system.** q_0 in C^10 must generate orthonormal bases under three copies of D_5: 3 x 9 = 27 real equations
(per subgroup: 2 complex rotation correlations, 5 real reflection correlations) against 18 - 2 = 16 real unknowns
(commutant U(1)^3, global phase removed). Maximal cardinality additionally needs q_0 to be an eigenvector of no
pi(k), k != 1. This is a small, explicit polynomial system (overdetermined by about 1.7, like every symmetric reduction
so far); it is a natural cheap numerical target (many random-start LM runs) and, if a zero exists, a natural exact
target. Not covered: other projective classes are excluded above; other Latin squares are not covered.
