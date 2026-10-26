# All-reference obligation — regular inverse and fixed-coordinate certificate interfaces

Before-creation clock observed: **2026-10-23T16:50:03-07:00**. PhysicsResearch96h. Intermediate unreviewed written checkpoint. No new scientific execution, matrix sampling, CAS or model CLI. The finite exact assay remains only finite evidence; the universal polynomial proposal remains pending a fresh decision.

The universal target is unchanged. The significance here is removing artificial q_i singularities and moving-basis complications, not replacing all references with positive-only spectra. A full proof on the interior plus the explicitly regular physical matrices would cover every boundary value by continuity; the all-reference inequalities themselves remain unproved.

## 1. A positive denominator on the ENTIRE probability simplex

Let c_i>=0, x_i=c_i^2, sum x_i=1 and d_i=1-x_i. Define

`W=sum_i product_(j!=i) d_j=1+2e2(x)-e3(x)`.

For a pair split with T=x_a+x_b, m=x_a x_b and n=x_j x_k,

`W=1+2T(1-T)+(1+T)m+(2-T)n>=1`.

Thus W has no singular product-reference vertex. All d_ij for i!=j are at least1/2. The full reference operator A_eta splits into the12 off-diagonal-pair coordinates with eigenvalues d_ij and the4 diagonal-pair coordinates with matrix

`A_diag=diag(d_i)+c c^T/4`.

The determinant identity is

**`det A_diag=W/4>0`.**

For rank>=2 it follows from the matrix determinant lemma and `(4+z)product d_i=W`. It then extends as a polynomial identity to the boundary. It proves invertibility there directly, rather than invoking an inverse of a singular diagonal D.

## 2. Explicit inverse with no1/d_i poles

For distinct i,j let{k,l} be the complementary pair. The diagonal-pair block G of the FULL reference inverse has entries

`G_ij=-c_i c_j d_k d_l/W`, i!=j,

`G_ii=[product_(j!=i)d_j + sum_(j<k, j,k!=i)d_j d_k]/W`.

These are regular at every zero/repeated probability, including a product vertex. Off the diagonal-pair subspace the full inverse is simply1/d_ij. There is no missing coupling between these subspaces: A_eta has only the stated diagonal rank-one update.

For rank>=2 these formulas follow by cancelling the Sherman-Morrison expressions

`G_ij=-r h_i h_j`,

`G_ii=1/d_i-r x_i/d_i^2`,

using r=(product d_i)/W. In the diagonal calculation,

`W=d_i sum_(j<k, j,k!=i)d_j d_k+product_(j!=i)d_j`,

so the apparent d_i^2 denominator cancels exactly. Because det A_diag=W/4>0, the regular entries coincide with the actual inverse also at the boundary. This supplies an explicit endpoint implementation of the same physical inverse, not a separate reduced model.

## 3. Regular form of every Q-P coupling in a12-weight block

Fix a!=b and complementary j,k. Checkpoint002 defined

`D_Q,Pi=kappa_i(e_i-c_i c)`,

`kappa_i=[sigma_i/4-r nu]/d_i`,

`nu=z/4-(q_a+q_b)/2`.

The complete cancellation is

`kappa_a=-d_b(d_j+d_k)/(2W)`,

`kappa_b=-d_a(d_j+d_k)/(2W)`,

`kappa_j= d_k(d_a+d_b)/(2W)`,

`kappa_k= d_j(d_a+d_b)/(2W)`.

To derive it, put u=q_a+q_b and v=q_j+q_k. On the first pair `sigma/4-r nu=-r(2+v)/2`; on the other pair it is `r(2+u)/2`. Since `2+u=1/d_a+1/d_b` and similarly for v, multiplying by r=(product d_i)/W cancels every apparent pole. These regular formulas retain all generic inverse corrections and hold at product vertices as limits of the actual physical map.

Together with the regular beta/E formulas and the d_ij denominators, checkpoint004's full12-weight table can therefore be written without ANY singular q_i or d_i^-1 parameter at the simplex vertices.

## 4. Fixed-coordinate complements for possible universal certificates

For all-positive amplitudes choose one input index b. In a12-weight block, the persistent reference vector is `K=sum_i c_i Q_i`. The ordered vectors `(K, Q_i for i!=b, P4, R/T4)` are an invertible basis because c_b>0. For the upper difference the K row/column is exactly zero. Hence full upper positivity is equivalent to positivity of the **fixed computational principal11x11 matrix obtained by deleting Q_b**. No coefficient-dependent orthogonal basis is necessary for that equivalence.

For the zero block, the four references are `K_l=sum_i c_i p(i,l)`. Replacing the four p(b,l) coordinates by K_l gives an invertible basis when c_b>0. The upper difference has zero reference rows/columns. Its upper quotient is therefore equivalently the **fixed coordinate principal24x24 matrix deleting those four p(b,l)**. The q- symmetry and the positive q+ elimination from checkpoint003 can still be used to reduce its size.

These fixed-coordinate complements are useful for symbolic determinant identities: their entries have only explicit positive physical denominators, and no square roots introduced by a moving orthonormal basis. They do not prove any residual sign. A certificate proved strictly on all-positive amplitudes would extend to every zero/repeated spectrum by the regularity in Sections1-3 and continuity of the full physical matrix.

For the lower sign the reference directions are NOT zero modes. One must retain and eliminate the true positive reference block before taking any complement, exactly as in checkpoints002-004. Deleting the same coordinates without that Schur term would be an invalid shortcut.

## 5. Source lead screened, but no Schwarz shortcut imported

Two actual primary sources were read as possible structural interfaces:

- Carlen-Muller-Hermes, *Characterizing Schwarz maps by tracial inequalities*, <https://arxiv.org/html/2203.03433v4>, especially the introduction's Schur characterization of2-positive maps and generalized Schwarz definitions.
- Garcia-Velo-Ibort, *Schwarz maps with symmetry*, <https://arxiv.org/pdf/2601.02282>, especially its map definitions and tensor-unitary TheoremV.7/small-dimension scope.

Their ordinary pointwise/tracial Schwarz properties do not state complete copositivity of the reference-dependent B-M_eta map. The latter source's tensor criteria are necessary Schwarz conditions/small-dimensional families, not the present all-reference4x4 co-Choi inequalities; fixing a generic reference also breaks the full input-unitary symmetry. No theorem from either source has been imported to close the target, and no correctness/priority judgment about their entire papers is claimed here. In particular, known two-copy2-positivity cannot simply be relabeled the required full co-Choi positivity.

## 6. Exact residual

No exact route failure is known and all-reference domination remains NOT PROVED. Current written frontier: generic4 upper, both seven-dimensional residuals of the nonzero12-weight blocks, and both zero-weight12-dimensional remainders. All four Schmidt coefficients, including zero and repeated values, remain in scope. A coefficient ansatz or a finite positive assay is not substituted for those matrix inequalities.
