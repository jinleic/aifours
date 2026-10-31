# Local filtering cannot turn the original map into a completely positive one

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN universal structural theorem for the exact weighted-filter route; it is not a rank-two q3 counterexample or original three-copy positivity proof. No particular physical state/control, numerical parameter, or target functional value is selected. No novelty, physical operational, formal/Lean, independent human/family or parent/f62 acceptance is claimed.

## 1. Weighted local Choi matrix

For any positive-definite complex 4×4 A, let

`Phi_A(X)=Tr(A X) A^−1−X/2`.

This is precisely the transformed map in `frontier-20261028-d4-exact-weighted-filter-law-v1.md`, SHA256 `67a55d296defa686c099318ee5bac3e81a48d0a549edaa6a7b68266c6df664f5`. Use the **input⊗output** Choi convention

`J(Phi_A)=Σ_(i,j) |i><j| ⊗ Phi_A(|i><j|)`.

With the unnormalized `Omega=Σ_(i=0)^3 |i i>`, direct matrix-unit substitution gives

`J(Phi_A)=A^T⊗A^−1−(1/2)|Omega><Omega|`.                    (1)

Set the positive invertible operator `S=A^(T/2)⊗A^(−1/2)`. The identity `(M⊗N)|Omega>=(I⊗N M^T)|Omega>` gives `S|Omega>=|Omega>`. Consequently

`J(Phi_A)=S [I⊗I−(1/2)|Omega><Omega|] S†`.                  (2)

All roots are the positive spectral square roots of positive A; the identity is valid for arbitrary complex Hermitian A>0, not just real or diagonal A.

## 2. Exact inertia for every filter

`||Omega||²=4`, so the unweighted bracket in (2) is the involution `I−2|Omega/2><Omega/2|`. It has **15 positive eigenvalues, one negative eigenvalue, and no zero eigenvalues**. By Sylvester's law of inertia, every invertible congruence S preserves these counts. Directly from the definition, `J(Phi_A)=(id_4⊗Phi_A)(|Omega><Omega|)` is the image of a PSD input and has a negative eigenvalue, so **no** Phi_A is completely positive, for every A>0.

For arbitrary positive-definite A1,A2,A3, the three-factor weighted-map Choi matrix is, up to the fixed input/output tensor regrouping, the tensor product of the three local Choi matrices. Tensoring the congruences yields the same inertia as three local involutions:

`positive dimension = 15³+3·15=3420`,
`negative dimension = 3·15²+1=676`, `zero dimension = 0`.

Thus invertible local filtering/weighting cannot make the full three-copy map completely positive either. No eigenvalue **magnitudes** are inferred under a nonunitary congruence; only signs/counts are invariant.

## 3. Exact limitation relative to q3

The original q3 target requires **2-positivity**, equivalently nonnegativity of the unweighted Choi form on every Schmidt-rank<=2 vector, not full complete positivity. A Choi matrix can have negative eigenvalues and still be nonnegative on that low-rank cone. Thus the inertia theorem rules out a direct 'filter to a completely positive map' shortcut but is **not** a rank-two physical counterexample and does not settle the target. It also does not rule out a proof using positive weighted maps restricted to the actual correlated low-rank inputs, nonlocal transformations, or another exact method.

The source-free all-target positivity gap and dense-boundary extension remain as recorded in `frontier-20261028-d4-dense-local-support-boundary-extension-v1.md`, SHA256 `4e6fe20463ddba8ebf32fba9cfd9139d058837b05a618732cc0b85eb91bffff3`. The public-source d4 certificate/independent-review route is separate. Old held results are nonpremises; the previously disclosed 19:04 cadence deviation and all f62/parent review boundaries remain unchanged.
