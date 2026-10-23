# Restricted results v3: F_9 x| H + inf symmetric ansatze with |H| >= 4 are impossible (any cardinality)

Recorded 2026-10-19T00:03:21-0700. Lane-internal written derivation by ContinueRQLS10; unreviewed; restricted ansatz only. Generalises
evidence/restricted-results-v2-agl19.md (sha256 40534c10d10cb8f170fdba131751b4236989e55589a72be41d1e9cecda6af543), which is the case |H| = 8.

**Ansatz.** H <= F_9^* (|H| = h), G = {x -> a x + b : a in H, b in F_9} acts on rows, columns and symbols F_9 u {inf} in
the same way (inf fixed) as autotopisms of B, and q_(g.p) is parallel to pi(g) q_p for a unitary projective
representation pi of G on C^10.

**Step 1 (B).** The stabiliser of a point x is H (multiplications about x); its fixed points are x and inf. As in v2,
B(x,x) = x would force B(x,inf) = inf for all x; hence B(x,x) = inf, B(x,inf) = x, B(inf,y) = y, B(inf,inf) = inf, and
B(x,y) for x != y is determined on each regular G-orbit of off-diagonal cells.

**Step 2 (pi).** If the cocycle restricted to F_9 is nontrivial, every irreducible constituent has dimension divisible
by 3 (Heisenberg type), impossible in dimension 10; so the F_9-restriction is a sum of characters. Row inf =
{pi(t_y) w} u {c} (w = q_(inf,0)) forces ||P_psi w||^2 = 1/9 for all nine characters psi of F_9; hence every
nontrivial character occurs, and since H permutes them freely in orbits of size h, the eight nontrivial characters
fill 8 dimensions with multiplicity one, leaving a 2-dimensional F_9-trivial part V0. In each induced block rho_j
(one per H-orbit, 8/h of them) H acts by its regular representation (after rephasing the basis), so each character
kappa of H has a one-dimensional eigenline u_(kappa,j) in rho_j, and the eigenvectors are flat on the orbit.

**Step 3 (three vectors).** The cells (inf,0), (0,inf), (0,0) have stabiliser H, so w, w' = q_(0,inf), d = q_(0,0) are
H-eigenvectors. Row inf, column inf and class inf (= diagonal u corner) each consist of the nine F_9-translates of
w, w', d respectively plus the corner c, a G-fixed ray in V0. Flatness forces a nonzero V0 component of norm 1/3 for
each of w, w', d, orthogonal to c; hence (whether V0 is chi_a (+) chi_b with a != b, or 2-dimensional of one
character) all three have the same H-character kappa and their V0 components are parallel. So w, w', d lie in the
(8/h + 1)-dimensional space spanned by the u_(kappa,j) and one line of V0, with coefficient moduli sqrt(h/9) on every
u_(kappa,j) and 1/3 on the V0 line. Row 0 contains d and w', column 0 contains d and w, and class 0 contains w and w'
(B(0,inf) = B(inf,0) = 0), so w, w', d are orthonormal. Then for each basis line u_(kappa,j) the three squared moduli
sum to at most 1: 3h/9 <= 1, i.e. h <= 3.

**Conclusion (restricted).** For |H| in {4, 8} no 1-RQLS(10) of any cardinality has this symmetry. |H| in {1, 2}
(F_9 + inf, the non-cyclic analogue of Z_9 + 1, and F_9 x| {+-1} + inf) survive this test and remain open.
