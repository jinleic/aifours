# Restricted results v2: AGL(1,9) + inf symmetric ansatz is impossible (any cardinality)

Recorded 2026-10-18T23:57:27-0700. Lane-internal written derivation by ContinueRQLS10; unreviewed; restricted ansatz only.

**Ansatz.** Rows, columns and symbols are F_9 u {inf}; the affine group G = AGL(1,9) = {x -> alpha x + beta} acts on all
three in the same way (inf fixed), is an autotopism group of B, and q_(g.p) is parallel to pi(g) q_p for a unitary
projective representation pi of G on C^10.

**Step 1 (B is forced).** G is sharply 2-transitive on F_9, so B(x,y) for x != y is determined by z0 = B(0,1):
B(x,y) = (1 - z0) x + z0 y, with z0 not in {0, 1, inf} for Latinity. B(x,x) is fixed by the stabiliser of x, so lies in
{x, inf}; B(x,x) = x would force B(x,inf) = inf for every x (the only remaining value fixed by the stabiliser of x),
which is not Latin. Hence B is the prolongation B'_lambda: B(x,x) = inf, B(x,inf) = x, B(inf,y) = y, B(inf,inf) = inf.

**Step 2 (representation).** H^2(G, C^*) = H^2(F_9, C^*)^(F_9^*) = 0 (F_9^* acts on the symplectic form of F_3^2 by the
norm, which is -1 for non-squares), so pi is linear. If pi does not contain the 8-dimensional irreducible rho_8, the
translations act trivially and the nine translates in row inf coincide. So pi = rho_8 (+) chi_a (+) chi_b with
characters chi of F_9^* ~ Z_8 (a = b allowed). Restricted to F_9^* (multiplications), rho_8 is the regular
representation; restricted to F_9 it is the sum of the eight nontrivial characters; V0 := chi_a (+) chi_b is the
F_9-trivial part.

**Step 3 (contradiction).** Row inf = {pi(t_y) w} u {c} with w = q_(inf,0): the translates are orthonormal iff
||P_psi w||^2 = 1/9 for all nine characters psi of F_9, so P_V0 w != 0; w is an eigenvector of the stabiliser F_9^* of
(inf,0), with character kappa, so kappa is a or b and w = sqrt(8/9) u_kappa + (1/3) v with u_kappa the kappa-eigenvector
of rho_8 (automatically flat on the nontrivial characters) and v a unit vector in V0 of character kappa; c (a G-fixed
ray in V0) must be orthogonal to v. The same holds for w' = q_(0,inf) (column inf) and d0 = q_(0,0) (class inf =
diagonal u corner), with the same corner c. If a != b, c is one of the two lines of V0 and v, v', v_d0 are all the other
line, so w', d0 have the same character and the same V0 line; if a = b, V0 is 2-dimensional, of character a, and v, v',
v_d0 are all parallel to the complement of c. In both cases <d0, w'> = (8/9) e^(i phi) + (1/9) e^(i phi') != 0, but d0
and w' lie in row 0 and must be orthogonal. Contradiction.

**Conclusion (restricted).** No 1-RQLS(10) of any cardinality admits this AGL(1,9) + inf symmetry. Not covered: other
actions of AGL(1,9) (different on rows, columns, symbols, or twisted by Frobenius), subgroups (e.g. F_9 + inf, the
non-cyclic analogue of Z_9 + 1), and every non-symmetric configuration.
