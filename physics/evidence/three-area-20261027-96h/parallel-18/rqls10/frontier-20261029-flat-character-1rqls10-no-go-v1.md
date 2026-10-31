# No flat abelian-character 1-RQLS(10) from a large free diagonal action

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 06:26:24 PDT 2026. This written reduction combines two inputs:
- the classical Hall–Paige theorem for Z10;
- the exact finite search Theorem C in `frontier-20261029-quantum-mann-dichotomy-k333-k555-v1.md` (SHA-256 `9fba4852172abd8629d1695ad2ec05bc14563628880c377108b21f9fa31dde3c`), with certificate script SHA-256 `585c04b8f2db270157301008919963b2802e0906d6b3c53247053dcb51b7a12a`.

It is a restricted-construction no-go. It is not a no-go for 1-RQLS(10) in general.

## Statement

Let Q be a 1-RQLS(10) of any cardinality: a 10x10 array of unit vectors in C^10 whose rows, columns and ten resolution classes are orthonormal bases. Suppose an abelian group A acts on Q and satisfies:
- A acts on the 100 cells freely, and on rows, columns and resolution classes compatibly;
- each a in A acts on C^10 by a diagonal unitary in one fixed basis, so the coordinates carry characters c_j of A, and psi(a·x) is proportional to D(a) psi(x);
- every vector is flat (all coordinates of modulus 1/sqrt10);
- |A| >= 25.

**Claim.** No such Q exists.

## Proof

Free action means |A| divides 100, so |A| is 25, 50 or 100.

*Case |A| = 100.* A acts regularly on cells. The stabilizer S of a row has order 10, and the row is one S-coset. Its orthonormality is Sum_j chi_j(s) = 0 for s in S, s != 1. Equivalently, the restriction of the ten characters to S takes each value of S^ exactly once. The same holds for columns and resolution classes.

The three stabilizers S_R, S_C, S_L meet pairwise trivially and pairwise generate A (Latin property). So A = S_R x S_C with |S_R| = |S_C| = 10, and S_L is the graph of an isomorphism. Hence A is isomorphic to Z10 x Z10, the only abelian group of order 100 containing two complementary subgroups of order 10.

Writing coordinates as characters (alpha_j, beta_j) of S_R x S_C:
- the row condition makes beta a bijection;
- the column condition makes alpha a bijection;
- the resolution condition makes alpha + phi*(beta) a bijection.

So beta = mu(alpha) with mu and alpha + phi* mu(alpha) both bijections of Z10. That is an orthomorphism, up to an automorphism, of Z10. By Hall–Paige it does not exist, because the Sylow 2-subgroup of Z10 is cyclic and nontrivial.

Flatness is not even needed here. Weighted uniformity forces each of the ten classes to have weight 1/10, hence exactly one coordinate per class.

*Cases |A| = 25 or 50.* The Sylow 5-subgroup P has order 25. It is not Z25: then every row, column and class stabilizer of order 5 would be the same subgroup, and a row and a column inside one P-orbit would share 0 or 5 cells, contradicting the Latin property. So P = Z5^2, acting diagonally and freely, with four cell-orbits of size 25.

The P-orbits on rows, columns and classes all have size 5, giving halves R0, R1, C0, C1, T0, T1. Each quadrant R_i x C_j is one P-orbit and carries labels from a single half. So the resolution square has a Z2 quotient, and each basis is the union of two cosets of its order-5 stabilizer line, lying in two different quadrants.

This is exactly the flat Z5^2-diagonal four-orbit ansatz of Theorem C. Theorem C was decided by an exact exhaustive search over all character multisets, lines and offsets, without any extra symmetry assumption, and found no solution. ∎

## Scope and what remains

- Smaller groups, |A| in {1, 2, 4, 5, 10, 20}, give 5- or 10-term phase sums with no linear torus reduction. They are untouched.
- Non-flat weights for |A| in {25, 50} are only numerically probed: best residual 0.0955, packet `frontier-20261029-half-resolved-maximal-qls10-and-m7-v1.md`.
- Non-diagonal (Heisenberg or Clifford) actions are untouched.

The unrestricted 1-RQLS(10) is OPEN. Independent review is requested of the case analysis and of the Theorem C certificate.
