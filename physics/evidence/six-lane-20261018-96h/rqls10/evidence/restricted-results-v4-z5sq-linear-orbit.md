# R11 (new restricted result): the linear Z_5^2-orbit ansatz for B = Cay(Z_10) is impossible

Recorded 2026-10-19T01:08:21-0700. Lane-internal; written reduction + exact computer check (receipts: evidence/z5sq_twoplex.receipts.md,
sha256 69e687a1cc10eb0021f252826ddd5d574ee096d3c5b7a269b9c571fae2f0bc45); unreviewed; restricted ansatz; any cardinality.

**Ansatz.** Rows, columns, symbols Z_5 x Z_2, B(i,j) = i + j (Cayley table of Z_5 x Z_2 = Z_10). The group Z_5^2 acts by
(a,b).((i1,i2),(j1,j2)) = ((i1+a,i2),(j1+b,j2)) (symbols shifted by a+b), and q_(g.p) is parallel to pi(g) q_p for a
LINEAR (diagonal, character) representation pi of Z_5^2 on C^10. Four orbit representatives x_ab = q_((0,a),(0,b)).

**Reduction.** Rows, columns and classes are orthonormal iff, for the eigen-decomposition of pi into characters
(mu_k, nu_k) and the fibres of nu (rows), mu (columns) and mu - nu (classes): each fibre carries total weight 1/5 of
every representative, and the two representatives paired by that direction (rows: 00-01, 10-11; columns: 00-10,
01-11; classes: 00-11, 01-10, the three perfect matchings of K4) are orthogonal inside every fibre. Hence every fibre
is 2-dimensional; a character of multiplicity 2 would put all three K4 matchings into one 2-dimensional space, which is
impossible (x_00 orthogonal to x_01, x_10, x_11 forces those three parallel, but x_01 is orthogonal to x_10). So the 10
characters are distinct and form a 2-plex K of the cyclic Latin square of order 5. Within a 2-element fibre the 2x2
block of a paired couple is (1/sqrt5) x unitary, so |x_r'(k)| = |x_r(k')|; around the triangles of K4 this forces all
moduli to be 1/sqrt10 (flat). The remaining conditions are linear in the phases: 30 equations
phi_r2(k1) - phi_r1(k1) - phi_r2(k2) + phi_r1(k2) = pi (mod 2 pi) in 40 unknowns.

**Check.** All 130 2-plexes were enumerated; for each, unimodular integer elimination gives rank 27 and a 3-dimensional
integer left kernel whose basis has an odd parity sum, so no real (hence no root-of-unity) phase assignment exists.

**Conclusion (restricted).** No 1-RQLS(10) of any cardinality arises from this ansatz. It strictly contains the flat
Fourier-permutation family with Cayley resolution and the diagonal Z_10^2 orbit case (old R3/R4 cover parts of it).
Not covered: projective pi (WH_5 (x) C^2), other symmetry groups, non-orbit configurations.
