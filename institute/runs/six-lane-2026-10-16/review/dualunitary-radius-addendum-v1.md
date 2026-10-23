# Quantitative two-qutrit isolation: a nearest-orbit argument

Status: parent-derived candidate, 2026-10-17 PT. The finite spectral certificate has passed; the nonlinear argument is under independent hostile review. This supplements the pinned proof `dualunitary-parent-inputs-v1/review/PROOF.md`; it does not overwrite that proof.

## Group-action correction

In the pinned proof §0, use the compact connected Lie group
`G = U(3)^2 × U(3)_op^2`, with opposite multiplication on the two right factors, acting by
`(v1,v2,v3,v4)·U = (v1⊗v2)U(v3⊗v4)`.
It is isomorphic to U(3)^4. The transformations, orbit O9, real tangent space and all dimensions are unchanged. With ordinary componentwise multiplication the displayed formula is not a left action; the opposite factors repair that formal error.

## Proposition

For every dual-unitary U of order 9 outside O9,

`dist_F(U,O9) >= 1`.

The same bound holds for every T-dual U outside O9. Here the Frobenius norm is the unnormalised matrix norm: `||P9||_F = 3`. In particular, the open Frobenius tube of radius 1 about O9 contains no non-2-unitary dual/T-dual gate. No explicit entangling-power gap or optimality of this radius is claimed.

## 1. Exact normal singular-value bound

Use `F_D(U) = (UU†−I, U^R(U^R)†−I)` with the product Frobenius norm on Hermitian outputs; use Γ instead of R for F_T. Both maps have the same zero sets as in the pinned proof. At P9 their real derivatives J have

`spec(J*J) = {0^33, 2^48, 6^48, 8^33}`.

Moreover `ker J = T_{P9}O9` by the pinned proof's dimension argument. Hence

`||JH|| >= sqrt(2)||H||_F` whenever `H` is orthogonal to `T_{P9}O9`.

**Hand derivation of the spectrum.** Use the orthogonal coordinate decomposition of the pinned proof §§2–3, with ψ=1_C (no state-normalisation factor). On the nine code coordinates, each cut contributes the squared diagonal variation `(2 Re δψ(c))^2`. Two cuts therefore give eigenvalue 8 on the nine real code directions and 0 on the nine imaginary directions.

Each of the 12 free six-point off-code orbits has the graph whose edges are the two cut involutions. Its edges alternate between the two involutions, so it is a six-cycle. Each off-diagonal Hermitian entry is counted twice in the Frobenius norm. Writing δψ=f+ig, its contribution is therefore

`2 sum_edges (f_u+f_v)^2 + 2 sum_edges (g_u−g_v)^2`.

The signless Laplacian of a bipartite six-cycle is orthogonally conjugate to its Laplacian. The six-cycle Laplacian has eigenvalues `0,1,1,3,3,4`. Thus each orbit contributes `0^2,2^4,6^4,8^2`. Summing the 12 orbits and the code coordinates gives the displayed spectrum. The same argument applies to both pairs of cuts.

**Independent exact arithmetic certificate.** `check_dualunitary_radius.py` constructs the integer Jacobians from matrix entries without worker imports. It weights each off-diagonal real/imaginary output row by 2 in the Gram matrix (diagonal rows by 1), asserts symmetry, and verifies exactly

`G(G−2I)(G−6I)(G−8I)=0`, `rank G=129`, `rank T=33`, `GT=0`.

These identities alone give the lower bound on the orthogonal complement of the tangent space; the independently factored characteristic polynomial additionally agrees with the hand multiplicities. See `dualunitary-radius-parent-check-v1.json`. This is ordinary exact integer linear algebra, not a Lean proof.

## 2. Normal vector from a nearest orbit point

O9 is compact and is an embedded smooth orbit of the corrected compact Lie-group action. For any U choose Q∈O9 minimising `||U−Q||_F`. Differentiating squared distance along every orbit curve through Q gives

`H := U−Q` orthogonal to `T_Q O9`.

Apply an inverse local-unitary transformation taking Q to P9. It is a Frobenius isometry preserving D, T and O9. The transformed difference is still normal and has norm `δ=dist_F(U,O9)`. We may therefore assume Q=P9.

## 3. Quadratic remainder gives a global separation

For U=P9+H in D, the exact polynomial expansion is

`0 = F_D(P9+H) = JH + (HH†, H^R(H^R)†)`.

For any matrix X, `||XX†||_F <= ||X||_F^2` (square and compare `sum σ_i^4` with `(sum σ_i^2)^2`). Realignment and partial transpose preserve the Frobenius norm. Hence the product-norm remainder is bounded by `sqrt(2)||H||_F^2` for either F_D or F_T.

Using the normal singular-value bound,

`sqrt(2) δ <= ||JH|| = ||remainder|| <= sqrt(2) δ^2`.

If U is outside O9 then δ>0, so δ>=1. No smallness assumption or implicit-function theorem is used in this last argument. The choice of nearest Q and the LU isometry make the separation uniform over the whole orbit.

## Limits

- The statement is a geometric separation from one LU orbit. The published uniqueness theorem [44] is needed to identify that orbit with all order-9 2-unitaries and to obtain the qualitative entangling-power gap.
- No explicit value for `1−sup e_p`, and no proof of the source's 15/16 optimum conjecture.
- No extension to d>=4; the d=4 control has a larger kernel and a transverse enphasing curve.
- Correctness of this addendum awaits the separately recorded hostile review. Priority remains a separate bounded literature audit.
