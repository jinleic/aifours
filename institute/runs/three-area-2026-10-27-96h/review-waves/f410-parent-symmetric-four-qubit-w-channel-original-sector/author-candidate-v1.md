# Symmetric four-qubit W input: full physical depolarizing output majorization

**Status: PARENT AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.** Native parent observation before composition: 2026-10-30T10:46:10-0700 PDT. The theorem is a constructive exact spectral inequality for a restricted actual-state class, not unrestricted four-qubit majorization or a novelty claim. Two parent-owned exact computations are reported below with their actual provenance; neither is an independent proof review.

## 1. Exact statement and improvement over the previous hull

Let

|W4>=(|1000>+|0100>+|0010>+|0001>)/2,
Phi_p(X)=(1−p)X+(p/2)Tr(X)I2, Lambda_p=Phi_p tensor4,
0<=p<=4/3, t=|1−p|, a=(1+t)/2, b=(1−t)/2.

**Candidate theorem.** For every physical p, every complex rank-k orthogonal projector Q, k=1,...,16,

Tr(Q Lambda_p(|W4><W4|)) <= K_k(diag(a,b) tensor4).

It extends to arbitrary local-unitary images of |W4> and finite convex mixtures of them, and to mixtures with the previously adopted Class A/B hull [S1](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-two-coefficient-and-paired-repetition-all-prefix-majorization-parent-v1.md). No common local basis or common maximizing projector is assumed. The finite W orbit is not every W-class state with unequal amplitudes; no larger claim is made.

This is a strict state-class enlargement over the earlier Class A/B hull. For any physical pairing, the reduced support on a pair is span{|00>,|01>+|10>}. A generic vector x|00>+y(|01>+|10>) has 2x2 coefficient determinant −y², so the subspace has exactly ONE product ray. The Schmidt rank of |W4> across the paired cut is2, so its reduced support is the entire two-dimensional subspace. Every Class A vector of rank2 across that cut has pair support spanned by TWO independent product vectors. Every Class B state with rank2 across its defining pairing has support equal to a locally rotated repetition space span{|e0 f0>,|e1 f1>}, also with two independent product vectors. Local product unitaries preserve product rays and all three pairings are equivalent by W symmetry. Hence W is neither A nor B. A rank-one density decomposed as a positive mixture of A/B densities forces every nonzero pure component to be parallel to W, so W is outside their convex hull. This argument requires neither support count alone nor a claim that all biseparable states lie in C.

## 2. Actual channel blocks and exact spectrum

Work first on the positive Bloch branch p=1−t, 0<=t<=1. In the computational basis a fourfold matrix-unit calculation shows the actual output preserves Hamming weight. For an index x of weight k, the diagonal value is

d_k=[k a^(5−k)b^(k−1)+(4−k)a^(3−k)b^(k+1)]/4, 1<=k<=3;
d_0=a³b, d_4=ab³.

For distinct x,y of equal weight k, the only nonzero off-diagonal entries occur when their supports differ by exchanging one occupied site, and have the common value

g_k=t² a^(3−k)b^(k−1)/4, 1<=k<=3.

Thus the weight-k block is d_k I+g_k A(J(4,k)), where J(4,k) is the Johnson adjacency matrix. J(4,1), J(4,3) have eigenvalues3 (multiplicity1), −1 (multiplicity3). For J(4,2), the 4x6 vertex-edge incidence matrix B of K4 satisfies B^T B=2I+A and BB^T=2I+J4. Its eigenvalues imply A has eigenvalues4 (multiplicity1),0 (multiplicity3),−2 (multiplicity2). Hence the sixteen actual output eigenvalues are the following nine groups, with the indicated multiplicities:

| Group | Multiplicity | Eigenvalue |
|---|---:|---|
| weight0 | 1 | a³b |
| weight1+ | 1 | d1+3g1 |
| weight1− | 3 | d1−g1 |
| weight2+ | 1 | d2+4g2 |
| weight2 zero | 3 | d2 |
| weight2− | 2 | d2−2g2 |
| weight3+ | 1 | d3+3g3 |
| weight3− | 3 | d3−g3 |
| weight4 | 1 | ab³ |

The reference has eigenvalues a4 (once), a³b (four times), a²b² (six), ab³ (four), b4 (once), in that order for t>=0. Here a4=a^4 and b4=b^4.

## 3. Exact all-prefix Bernstein certificate

Let B_j^4(t)=binom(4,j)t^j(1−t)^(4−j), j=0,...,4. Each eigenvalue above and each ordered reference eigenvalue has a degree-four Bernstein expansion.

For a fixed j and k, let G_(j,k) be the coefficient of B_j^4 in the reference k-prefix, minus the sum of the k largest individual W-eigenvalue coefficients for that same j (counting multiplicities). The maximum over choices of k distinct eigenvalue positions is exactly that sum, independently for each j. Direct exact rational conversion and sorting yields the complete table of 192 G_(j,k), with k=0,1,...,16 in each row:

| j | 192 G_(j,k), in ascending k |
|---|---|
| 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| 1 | 0, 6, 9, 12, 15, 18, 18, 18, 18, 18, 18, 18, 15, 12, 9, 6, 0 |
| 2 | 0, 24, 24, 28, 36, 44, 36, 32, 28, 24, 20, 20, 12, 8, 4, 0, 0 |
| 3 | 0, 36, 24, 24, 36, 48, 36, 24, 12, 0, 0, 0, 0, 0, 0, 0, 0 |
| 4 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |

Every entry is nonnegative. Consequently, for ANY fixed subset of k actual eigenvalue positions, its reference-prefix gap has every degree-four Bernstein coefficient nonnegative. Since B_j^4(t)>=0 for t in[0,1], that subset sum never exceeds the reference k-prefix. Taking the maximum over subsets proves all sixteen Ky Fan comparisons, WITHOUT assuming an eigenvalue ordering remains fixed as t changes. Equality and degeneracies at t=0,1 are included.

For reproducibility, the actual W group coefficients multiplied by192 for j=1,2,3 are, in the group order in §2:

| Group | 192 B1 coefficient | 192 B2 coefficient | 192 B3 coefficient |
|---|---:|---:|---:|
| weight0 | 18 | 24 | 24 |
| weight1+ | 15 | 24 | 60 |
| weight1− | 15 | 16 | 12 |
| weight2+ | 12 | 20 | 36 |
| weight2 zero | 12 | 12 | 12 |
| weight2− | 12 | 8 | 0 |
| weight3+ | 9 | 12 | 0 |
| weight3− | 9 | 4 | 0 |
| weight4 | 6 | 0 | 0 |

The reference coefficient vectors, in the fixed ordered-reference position order, are:

- j=1: (24,18,18,18,18,12,12,12,12,12,12,6,6,6,6,0).
- j=2: (48,24,24,24,24,8,8,8,8,8,8,0,0,0,0,0).
- j=3: (96,24,24,24,24,0,0,0,0,0,0,0,0,0,0,0).

At j=0 both coefficient vectors are uniform12/192. At j=4 both have one coefficient192/192 and fifteen zeros. Thus the table can be independently checked by elementary integer prefix sums; it is not a numerical root search or a dependence on any one ordering at physical t.

For the physical negative branch p=1+t, 0<=t<=1/3, full spin-flip/transpose gives Lambda_(1+t)(rho)=Y^tensor4 [Lambda_(1−t)(rho)]^T Y^tensor4. Transposition and unitary conjugation preserve eigenvalues, and the negative-branch product reference has the same multiset. The inequality therefore covers the full physical interval [0,4/3]. The map transports an arbitrary complex consuming projector by Q -> Y^tensor4 Q^T Y^tensor4 if evaluated directly.

Local physical covariance and convexity of each Ky Fan k-sum extend the result to finite mixtures of arbitrary physical local-unitary images of W4 and, by averaging already-supported inequalities, their finite convex hull with the previous Class A/B hull. It does NOT give a common local-unitary postprocessing channel independent of the input or prove arbitrary-density majorization.

## 4. Actual parent calculations and verification boundary

Parent froze [author scope and inputs](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f410-parent-symmetric-four-qubit-w-channel-original-sector/manifest-v1.json) before any selected calculation; current prose and conceptual route are parent-authored. A nonexistent guessed earlier-prefix path caused one pre-freeze ENOENT and created no wave files; the actual prior disposition was then obtained from the f372 manifest. Sympy was not installed or used.

- [Exact direct physical channel control](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f410-parent-symmetric-four-qubit-w-channel-original-sector/parent-w4-physical-symbolic-v1-receipt.json): parent one-shot stdlib Fraction script evaluated all256 matrix entries as polynomials from the four local matrix-unit actions, matched the claimed block formula, independently checked J(4,1)/J(4,2) polynomial/trace spectra, and rejected four named scientific mutations; exit0/PASS. [Source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f410-parent-symmetric-four-qubit-w-channel-original-sector/parent-w4-physical-symbolic-v1.py).
- [Exact all-subset polynomial calculation](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f410-parent-symmetric-four-qubit-w-channel-original-sector/parent-w4-polynomial-exploration-v1-receipt.json): parent one-shot stdlib Fraction script enumerated all6144 multiplicity count vectors, yielding2072 distinct (k,gap) polynomials;2070 had nonnegative exact Bernstein certificates and two were identically zero; no unresolved polynomial, exit0. [Source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f410-parent-symmetric-four-qubit-w-channel-original-sector/parent-w4-polynomial-exploration-v1.py). The compact coefficientwise-minimum table is [recorded separately](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f410-parent-symmetric-four-qubit-w-channel-original-sector/parent-w4-bernstein-minimum-gaps-v1.json). This second check assumes the derived spectrum; its sampled rational orderings are not the universal proof.

Both calculations are parent-owned, not blinded or independent-family verification. The small Bernstein table is a self-contained universal certificate conditional on the explicit spectrum; the physical-matrix and Johnson derivation makes the candidate about an actual channel, not an abstract spectral relaxation. Neither calculation is a complete formal/kernel proof. No external model CLI, new package, heavy/paid run, deletion or remote mutation was used.

## 5. Unpaid gates

A disjoint written reconstruction of all physical matrix entries, Johnson spectra, Bernstein table, class separation and negative-branch/mixture quantifiers is REQUIRED before parent adoption. A separately authored exact physical/coefficients checker with intended-mutation controls is also requested. Source and priority comparison remains unpaid; published arbitrary-n log-determinant ordering and approximate-majorization results are prior material, not a proof of this exact sector without an explicit derivation. Arbitrary amplitudes W states, other 1|3-separable states, unrestricted k3/all-prefix and original whole-target majorization remain open.
