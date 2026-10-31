# Zero-excess supports: exact phase-normal form and the remaining code obligation

Status: **WRITTEN candidate**, with exact integer finite controls named below. This is an all-variable equivalence at zero excess, not a support bound, a witness, a formal proof, a novelty claim, or parent adoption. No held review/candidate is an input. No no-OLS theorem, no no-Hamming-one theorem and no prior numerical enumeration is used.

## 1. Definitions and scope

Let psi be an AME(4,6) state in any fixed product basis. Write U=6psi in each of its three2|2 cuts. Each U is a36x36 unitary. Let P consist of t entries of modulus1 in U (the maximal coefficients); let E be the remaining nonzero positions. Put n=36-t. Assume **zero excess**:

`|E|=2n`, equivalently the support is `N=t+2n=72-t`.

A maximal entry is the unique nonzero in its row and column of every cut: the squared norm of that row/column is1 and that entry already contributes1. Consequently P is pair-injective, E shares no pair value with P, and in each of the six pair-coordinate systems the t P values and n E values partition all36 pair values. Every E pair value has at least two extensions, since a singleton nonzero row/column of a unitary would itself have modulus1. Zero excess makes every such multiplicity exactly two.

A *support specification* below is a pair of disjoint sets P,E of words in {0,...,5}^4 satisfying:

1. |P|=t, |E|=2n and n=36-t.
2. In every pair-coordinate system, P uses t different values, E uses the complementary n values, and every E value occurs exactly twice.
3. In each of the three cuts, the E support is a disjoint union of full2x2 bipartite components.

Condition3 is forced by any unitary realization, not an additional ansatz: the E support graph in that cut has degree2 at every active row and column. Every component is a cycle. A cycle with more than two row vertices has neighboring rows sharing exactly one nonzero column, whose inner product cannot vanish. Thus every component has exactly two rows and two columns. Parallel/double positions do not occur because the tensor has one coefficient per word.

No assumption on distances between words, on residual alphabet sizes, or on the phases/moduli of the original E entries is made.

## 2. Phase matrix

For each full2x2 E block in every cut, order its two rows r,s and its two columns c,d. If its four positions are a=(r,c), b=(r,d), e=(s,c), f=(s,d), place the row

`M_block = e_a - e_b - e_e + e_f`

in an integer matrix M with columns indexed by E. Blocks from different cuts may give dependent/repeated equations; retain all of them. Write a complex phase as exp(pi*i*x_w), with x_w in R/2Z. The required equation is

`x_a - x_b - x_e + x_f = 1 (mod2)`.                 (1)

Changing either block ordering negates the row; the right side1 is unchanged modulo2. Thus ordering cannot affect solvability.

## 3. Complete support-realization equivalence

**Theorem.** A support specification P,E admits an AME(4,6) realization if and only if

`M x = 1 (mod2)`                                  (2)

is solvable. Moreover, whenever *any* AME realizes that support specification, there is another AME with the same support and exactly the coefficients

`psi_w = 1/6` for w in P,

`psi_w = exp(pi*i*x_w)/(6*sqrt2)` for w in E.       (3)

This assertion does **not** say that the original tensor has those E moduli, or that the replacement tensor is LU-equivalent to it.

Necessity: take the phases x_w of any realization. In a full2x2 unitary block its two rows are orthogonal, so its two nonzero product terms a*conj(e) and b*conj(f) are negatives. Their phases differ by pi, which is exactly(1). This argument does not assume that the two products have any preassigned common modulus; their equality of moduli follows from their sum being zero.

Sufficiency: define(3). In each cut, a P row/column has exactly one entry of U=6psi, with value1. It is disjoint from every other occupied row/column position except itself. Each E block has all four entries of modulus1/sqrt2. Its row and column norms are1, and(1) makes the two terms in its row inner product exact negatives. The block is unitary. Hence the whole36x36 matrix is a disjoint direct sum of singleton unitaries and2x2 unitaries in **all three cuts**, which proves the AME condition. Normalization follows already from any one cut, or directly from t/36+2n/72=(t+n)/36=1.

Therefore equal E moduli lose no *support-realization* possibilities at zero excess. Restricting the allowed phase group, in contrast, may lose possibilities and must always be disclosed.

## 4. Exact integer criterion, with no phase sampling

Equation(2) is solvable if and only if every integer left-kernel vector lambda satisfies

`lambda^T M=0 => sum(lambda) is even`.             (4)

Necessity follows by applying lambda to(2). For sufficiency, perform unimodular integer row operations to obtain H=UM with its first r rows linearly independent and its remaining rows zero. U is square integer with determinant plus/minus1, so these operations preserve equations modulo2 and their inverse is also integer. The zero rows of U form an integer basis of the left kernel: an integer relation on H has zero coefficients on its first r rows, and conjugation by U gives precisely all integer relations on M. Thus(4) says that every zero row of H has right side zero in U1 modulo2.

The remaining r real equations H_nonzero*x=(U1)_nonzero can be solved *as exact real equations*, because their r rows are independent. They have rational coefficients and right sides, so a rational solution exists (choose an invertible r-column minor and set other variables to zero). This rational solution, reduced modulo2, solves the transformed system. Hence it solves(2). This proves(4), without requiring that every nonzero pivot be1.

A single explicit integer lambda with lambda^T M=0 and odd sum is consequently an arbitrary-complex phase obstruction for that individual support specification. A floating-rank calculation, a mod2-only nullspace calculation, or an UNSAT result after restricting phases to signs/fourth roots is not interchangeable with(4).

## 5. The code-completion obligation is independent and indispensable

A valid residual E with phases does not by itself provide an AME(4,6) tensor. P must still be a **single simultaneous t-word code** that uses, in all six pair systems, exactly the pair values not used by E. For n=12 this is an exact cover of144 tagged pair values by24 words, each covering six tags. Separate completions in different cuts are not enough. In particular the24 permutation words on four symbols have a fourth-root residual phase realization, but this control is not a full AME(4,6) witness and supplies no P code.

Conversely, once the actual P code, E and an exact solution of(2) are supplied, formula(3) gives a literal tensor and all three unitary matrices can be checked directly. No outside classical existence theorem is needed for that positive witness.

## 6. Current exact controls and deliberately restricted searches

The source `frontier-20261029-zero-excess-phase-solve-v1.py` implements the integer phase test, with an explicit unimodular row transformation, and verifies constructed phases by exact cyclotomic Gram arithmetic. Its earlier known60-term control is `sat-20261029/v2-real-t12.phase-independent.json`; it checks all3888 full Gram entries. Its1080 exact random unimodular/transformation checks and deliberately inconsistent-kernel controls are recorded in `sat-20261029/phase-hnf-controls-v1.json`. Those controls do not turn this written theorem into a formal proof.

A new Boolean encoding, `frontier-20261029-fourth-root-zero-excess-z3-v1.py`, searches only x_w in {0,1/2,1,3/2}. Its row-sum formula is independently checked for all256 assignments to the four phases of a2x2 block in `frontier-20261029-fourth-root-phase-equivalence-control-v1.json`: exactly64 are orthogonal, with zero mismatches against integer Gaussian inner products.

The fixed permutation-support positive control `frontier-20261029-fourth-root-positive-control-v1.json` is SAT and directly checks144 active Gram entries per cut, using integer Gaussian arithmetic. The same support with signs only is UNSAT in `frontier-20261029-fourth-root-real-negative-control-v1.json`. This is an honest strictness control: complex fourth roots can do more than signs, but the positive control is still only a residual component.

Two newly obtained residual supports, one of profile3555 and one of profile4455, both fail the exact arbitrary-complex phase test. Their individual records are `frontier-20261029-n48-t24-profile3555-coupling-v1.json` and `frontier-20261029-n48-t24-profile4455-coupling-v1.json`. No global profile exclusion is inferred from those two examples. The source-only support searches also contain timed-out cases; no timeout is called an obstruction or scientific progress.

`frontier-20261029-residual-support-coupling-assay-v1.py` reconstructs the three cut block systems independently from each supplied residual support, applies the exact phase test, and, only if it passes, searches for the *single six-pair* complement P code. A bounded exact-cover search is explicitly UNKNOWN; a prospective positive requires direct pair-partition and all3888 exact Gram checks.

## 7. Precisely what remains open

This normal form does not enumerate every residual support, does not decide N=48, does not replace any frozen review scope, and does not adopt the unreviewed N=46/N=47/N=48 branch candidates. It identifies the complete remaining coupling obligation at zero excess: the same residual support must pass(4) and admit the simultaneous complement P code. An exact successful instance would be a witness; an all-instance exclusion still requires a complete argument covering the relevant supports.
