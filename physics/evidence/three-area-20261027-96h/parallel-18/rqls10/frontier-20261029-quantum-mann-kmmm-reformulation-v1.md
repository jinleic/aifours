# A quantum Mann problem: subsquare label squares force a K_{m,m,m} representation

**WRITTEN AUTHOR CANDIDATE + FLOATING DISCOVERY DATA, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 04:48:48 PDT 2026. This is an exact reduction and a numerical scope map. It is **not** a no-go for 1RQLS10.

## Reduction theorem

Let n=2m. Suppose A is a QLS(n) and B is a Latin square of order n such that every symbol class of B is an ONB of A. Equivalently, by [Zhang–Cao, Lemma 2.2](https://arxiv.org/html/2608.29201v2), A is 1-resolvable with transversal labels B. No distinctness or cardinality assumption is needed.

Suppose B has a Z2 quotient with all three classes of size m: subsets R of rows, C of columns and T of symbols, each of size m, with

`B(i,j) ∈ T` iff exactly one of `i∈R`, `j∈C` holds.

Equivalently B consists of four m×m Latin subsquares. Then the 3m bases given by rows in R, columns in C and B-classes in T form an orthonormal edge representation of `K_{m,m,m}` in C^(2m):

- the three vertex classes are R, C and T;
- the ray on edge `(i,j)` with `i∈R`, `j∈C` is cell `(i,j)`;
- the ray on edge `(i,t)` is the unique cell `(i,j)` with `j∉C` and `B(i,j)=t`;
- the ray on edge `(j,t)` is the unique cell `(i,j)` with `i∉R` and `B(i,j)=t`;
- the 2m rays incident to each vertex are exactly that row, column or B-class, hence an ONB.

The remaining m² cells (`i∉R`, `j∉C`) are not used. Conversely the problem is exactly the existence of an **orthonormal representation of the line graph L(K_{m,m,m}) in dimension 2m**, because a set of 2m orthonormal vectors in C^(2m) is automatically an ONB.

For odd m, Mann's classical counting theorem says such a B has no orthogonal mate. This reduction is the quantum version of that question. It contains every cyclic label square of order 10, because Z10 has an index-two subgroup.

## Exact identities for any representation

Let `X_AB`, `X_AC`, `X_BC` be the sums of rank-one projectors over edges between the indicated parts. Summing the vertex identities over each part gives

`X_AB+X_AC = X_AB+X_BC = X_AC+X_BC = m I`,

so `X_AB=X_AC=X_BC=(m/2)I`. For each vertex x define the reflection `S_x = P(first incident part) - P(second incident part)`. Concretely, for a∈A, b∈B and c∈C, `S_a=P_(U_a)-P_(U_a^⊥)` with `U_a=span{v_ab}`, `S_b=P_(V_b)-P_(V_b^⊥)` with `V_b=span{v_ab}`, and `S_c=P_(W_c)-P_(W_c^⊥)` with `W_c=span{v_ac}`. The preceding identities are equivalent to

`sum_(a∈A) S_a = sum_(b∈B) S_b = sum_(c∈C) S_c = 0`.

For m=3, three traceless reflections with zero sum satisfy `{S_1,S_2}=-I`. Hence `S_1S_2` has eigenvalues only primitive cube roots of unity, so the three reflections generate an S3-module isomorphic to `C^2_standard ⊗ C^3`. Each eigenspace `U_a` has the form `ell_a ⊗ C^3`. This is a strong rigidity statement for the m=3 case, not yet a proof of nonexistence.

## Floating discovery map (not proof)

Using the same Levenberg–Marquardt and averaged-projection code on unconstrained random starts:

| Graph | Dimension | Starts | Best floating residual |
|---|---:|---:|---:|
| K7, a control | 6 | 6 | about 1e-30, all successful |
| K2,2,2 | 4 | 6 | 0, all successful |
| K4,4,4 | 8 | 6 | 0, all successful |
| K3,3,3 | 6 | 24 | 0.4649, with only three recurring minima |
| K5,5,5 | 10 | 22 | 0.0597 |
| K6,6,6 | 12 | 3 | 0.0435 |

A Z_m-equivariant K_{m,m,m} ansatz forces the cyclic unitary to have each m-th root of unity with multiplicity 2. It succeeds for m=4. It stays positive for m=3, at 0.1746, for m=5, at 0.0031, and also for m=6, at 0.0049.

**Interpretation caution.** K6,6,6 is realizable: in Zhang–Cao's Construction 3.3 for v=12 and G=Z2×Z6, the first-coordinate quotient gives exactly such a representation, with the same Z6 symmetry. The numerical failure at m=6 therefore shows these searches **cannot** be used as evidence against K5,5,5. The repeated K3,3,3 failures suggest a theorem for m=3, but are not a proof.

## Status

Open problem isolated: does `L(K_{5,5,5})` have an orthonormal representation in C^10? A negative answer would exclude every 1RQLS10, of any cardinality, whose transversal-label square has four 5×5 subsquares, including all cyclic label squares. A positive answer would supply the 75-ray core but not the other 25 cells. The 4+6 sector analyses of the Pauli and 600-cell cores are special cases of this question. No conclusion is claimed here; review is required.
