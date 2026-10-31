# Exact local-filter transformation for the original three-copy map

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN all-variable identity giving the correct replacement for the invalid free-whitening shortcut. It does **not** prove the original q3 inequality, assert simultaneous whitening exists, select a physical state/control, or claim a source-independent full solution or review/novelty acceptance.

## 1. Single-factor identity for every invertible filter

Let `Phi(X)=Tr(X)I4−X/2` and let G be any invertible complex 4×4 matrix. Set the positive-definite matrix `A=G†G` and define

`Phi_A(X)=Tr(A X) A^−1−X/2`.

Then for every complex X,

`G^−1 Phi(G X G†) G^−† = Phi_A(X)`.                                  (1)

Indeed, `Tr(GXG†)=Tr(A X)` and `G^−1 I G^−†=(G†G)^−1=A^−1`; the `−X/2` term follows directly. This is an identity of maps on the **whole** matrix algebra, with no numerical spectrum or chosen target input.

The prior exact criterion `frontier-20261028-d4-local-whitening-covariance-obstruction-v1.md`, SHA256 `c49e04ec137e417c667269a689cf14da1458a1b34a5413162c84d022dddc2c0d`, says `Phi_A=Phi` under the same G congruence only when G is scalar-unitary. Equation (1) gives the correct transformed map in every other case instead of silently cancelling the filter.

## 2. Exact three-factor and reference identity

For arbitrary invertible `G_i` on the three C⁴ sites, put `G=G1⊗G2⊗G3` and `A_i=G_i†G_i`. Tensoring (1) gives for every operator X on H=(C⁴)^tensor3,

`G^−1 Phi^tensor3(G X G†) G^−†
  = (Phi_(A1)⊗Phi_(A2)⊗Phi_(A3))(X)`.                            (2)

The same identity holds after tensoring both sides with id_Q for Q=C², with `G⊗I_Q` as the congruence. For every PSD input R on H⊗Q, invertible congruence therefore preserves the sign of the **actual** output:

`(Phi^tensor3⊗id_Q)[(G⊗I) R (G†⊗I)] >=0`

if and only if

`((Phi_(A1)⊗Phi_(A2)⊗Phi_(A3))⊗id_Q)[R] >=0`.                    (3)

For the full original q3 domain this may be applied to an arbitrary vector `a=(G⊗I_Q)b`; no assumption is made that b retains the Stiefel Q marginal. The exact equivalence between arbitrary such a and the original complex-rank<=2 q3 target was separately derived in `frontier-20261028-d4-positive-map-all-subsets-addendum-v1.md`, SHA256 `8cd42f794b79fec63fd8d607b41554891b3b6409d75efb7278ac29c962cbf500`.

## 3. What remains unpaid

The dense-support lemma `frontier-20261028-d4-dense-local-support-boundary-extension-v1.md`, SHA256 `4e6fe20463ddba8ebf32fba9cfd9139d058837b05a618732cc0b85eb91bffff3`, permits working on a dense set whose three local reductions are invertible, then restoring all original degenerate boundaries by continuity. It does **not** prove the existence of a simultaneous three-site whitening satisfying any chosen normalization: filtering one site changes reductions on the others. Even if a valid simultaneous filter were available, (3) leaves a new all-variable positivity problem for the correlated weights A_i, not the original unweighted map for free.

The precise analytic gap is therefore to justify any desired global filter construction **and** establish (3) for the resulting full family of weighted maps and inputs, or to find another direct all-isometry proof. No such positivity argument is supplied here. Equation (3) is exact and reversible; it does not narrow the final complex-rank<=2 domain or evaluate any instance.

No physical distillability theorem, q3 counterexample/strict gap, all-d result, source novelty, human/model-family, formal/Lean, parent/f62 acceptance or retrospective cure of the disclosed cadence gaps is claimed. Historical held outcomes are not premises.
