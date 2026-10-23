# Quantitative two-qutrit isolation: a nearest-orbit argument (v2)

Status: revision v2, 2026-10-17 PT. Claude hostile review of v1 returned **ACCEPT** with clarity edits m1–m5 and e1–e4, all applied here. This supplements the corrected proof `dualunitary-parent-inputs-r3/PROOF.md`; neither earlier file is overwritten.

## Group-action correction

In the pinned proof §0, use the compact connected Lie group
`G = U(3)^2 × U(3)_op^2`, with opposite multiplication on the two right factors, acting by
`(v1,v2,v3,v4)·U = (v1⊗v2)U(v3⊗v4)`.
It is isomorphic to U(3)^4. The transformations, orbit O9, real tangent space and all dimensions are unchanged. With ordinary componentwise multiplication the displayed formula is neither a left nor a right action; the opposite factors repair that formal error. The nonlinear argument below needs only that each `Φ_g` is a Frobenius isometry preserving D, T and O9, which holds either way.

## Proposition

For every dual-unitary U of order 9 outside O9,

`dist_F(U,O9) >= 1`.

The same bound holds for every T-dual U outside O9. Here the Frobenius norm is the unnormalised matrix norm: `||P9||_F = 3`. Thus the open Frobenius tube of radius 1 about O9 contains no dual or T-dual gate outside O9 at all. The imported uniqueness theorem [44] is needed only to equate "outside O9" with "not 2-unitary". This argument independently reproves the qualitative Theorem 1 of the corrected proof, including relative openness and the connected-component statement, without the implicit-function step. No explicit entangling-power gap or optimality of this radius is claimed.

## 1. Exact normal singular-value bound

Use `F_D(U) = (UU†−I, U^R(U^R)†−I)` with the product Frobenius norm on Hermitian outputs; use Γ instead of R for F_T. Both maps have the same zero sets as in the pinned proof. At P9 their real derivatives J have

`spec(J*J) = {0^33, 2^48, 6^48, 8^33}`.

Inner products: on M_9(C) use `<X,Y> = Re tr(X†Y)`; on Herm_9 × Herm_9 use `<(A,B),(A',B')> = tr(AA') + tr(BB')`. `J*` is the adjoint for these, and "orthogonal" always refers to `Re tr(X†Y)`. With unit weights on off-diagonal real/imaginary coordinates the smallest nonzero eigenvalue would be 1 instead of 2, so the stated weights matter.

Moreover `ker J = T_{P9}O9`: the hand spectrum below has zero eigenvalue with multiplicity 33; `T_{P9}O9 ⊆ ker J` because `O9 ⊆ D ∩ T`; and `dim T_{P9}O9 = 33` by Proposition 3.1 of the corrected proof. Hence

`||JH|| >= sqrt(2)||H||_F` whenever `H` is orthogonal to `T_{P9}O9`.

**Convention bridge.** `UU† = M_34 M_34†`, while `U^R U^R† = Π ρ_13 Π^T` and `U^Γ U^Γ† = Π' ρ_23 Π'^T` for row-reordering permutations Π, Π'. Also `τ_S = τ_{S̄}`, and at a unitary P, `d(U†U)_P[H] = P†·d(UU†)_P[H]·P`. Kernels and Frobenius norms therefore agree with the conventions of the corrected proof.

**Hand derivation of the spectrum.** Use the orthogonal coordinate decomposition of the corrected proof §§2–3, with ψ=1_C (no state-normalisation factor). On the nine code coordinates, each cut contributes the squared diagonal variation `(2 Re δψ(c))^2`. Two cuts therefore give eigenvalue 8 on the nine real code directions and 0 on the nine imaginary directions.

Each of the 12 free six-point off-code orbits has the graph whose edges are the two cut involutions. Because `τ_{S'}τ_S` acts freely, `τ_S y ≠ τ_{S'} y`, so there are no double edges; the orbit is connected, so its graph is `Cay(S_3,{τ_S,τ_{S'}}) ≅ C_6`, with edges alternating between the two involutions. Each off-code point lies in exactly one conjugate pair of off-diagonal entries per cut, and code points appear only on diagonals, so there are no cross terms. Each off-diagonal Hermitian entry is counted twice in the Frobenius norm. Writing δψ=f+ig, its contribution is therefore

`2 sum_edges (f_u+f_v)^2 + 2 sum_edges (g_u−g_v)^2`.

The signless Laplacian of a bipartite six-cycle is orthogonally conjugate to its Laplacian. The six-cycle Laplacian has eigenvalues `0,1,1,3,3,4`. Thus each orbit contributes `0^2,2^4,6^4,8^2`. Summing the 12 orbits and the code coordinates gives the displayed spectrum. The same argument applies to both pairs of cuts.

**Independent exact arithmetic certificate.** `check_dualunitary_radius.py` constructs the integer Jacobians from matrix entries without worker imports. It weights each off-diagonal real/imaginary output row by 2 in the Gram matrix (diagonal rows by 1), asserts symmetry, and verifies exactly

`G(G−2I)(G−6I)(G−8I)=0`, `rank G=129`, `rank T=33`, `GT=0`.

These identities alone give the lower bound on the orthogonal complement of the tangent space; the independently factored characteristic polynomial additionally agrees with the hand multiplicities. See `dualunitary-radius-parent-check-v1.json`. This is ordinary exact integer linear algebra, not a Lean proof.

## 2. Normal vector from a nearest orbit point

O9 is compact and is an embedded smooth orbit of the corrected compact Lie-group action. For any U choose Q∈O9 minimising `||U−Q||_F`. Differentiating squared distance along every orbit curve through Q gives

`H := U−Q` orthogonal to `T_Q O9`.

Let `Q = g·P9` and `Φ := Φ_{g^{-1}}`. It is real-orthogonal, and by §1.3 of the corrected proof (with `v^T` unitary) `Φ(D)=D`, `Φ(T)=T`, `Φ(O9)=O9`. Φ maps orbit curves through Q to orbit curves through P9, so `Φ(T_Q O9) = T_{P9}O9`; hence `<ΦH,X> = <H,Φ^{-1}X> = 0` for every `X ∈ T_{P9}O9`. Thus `ΦU = P9 + ΦH` lies in D (or T), with `ΦH` normal at P9 and `||ΦH|| = δ = dist_F(U,O9)`. We may therefore assume Q=P9.

## 3. Quadratic remainder gives a global separation

P9, P9^R and P9^Γ are permutation matrices, because every 2-coordinate projection of the MDS code C is bijective; so the constant terms cancel. For U=P9+H in D, the exact polynomial expansion is

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
