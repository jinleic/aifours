# An exact local qubit-corner measure–prepare lemma, and the unpaid tensor step

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: Wed Oct 28 20:37:49 PDT 2026. This is a **WRITTEN, source-independent local analytic lemma** about the fixed map occurring in the original d4 q3 problem. It is not a proof of the three-copy target, a selected target state/control, an operational distillability theorem, a novel-priority claim, or a reviewed/adopted result. The full original target and the explicit remaining tensor gap are retained in §4.

## 1. Statement for every encoded qubit corner

Define the linear map on complex 4×4 matrices

`Psi(X)=Tr(X) I4−(1/2) X^T`,

where transpose is in the fixed original local basis. For **every** isometry `V:C²→C⁴`, let `iota_V(X)=V X V†`. The map `Psi∘iota_V` is an **entanglement-breaking positive map**, in the precise algebraic sense that for every finite ancillary space R and every PSD operator X on `C²⊗R`,

`((Psi∘iota_V)⊗id_R)(X)`

is a finite-dimensional separable PSD operator across the output `C⁴ | R` cut. The map need not be trace-preserving; multiplying it by a positive scalar would not affect the statement. No particular physical input vector or numerical test is used.

## 2. Exact all-corner Choi decomposition

Use the unnormalized Choi convention `J(Theta)=Σ_(i,j=0,1) Theta(|i><j|)⊗|i><j|`. Write `S=ran(conjugate(V))` and `P_S=conjugate(V) V^T`. The exact identity for all matrix units is

`J(Psi∘iota_V)
 = (I4−P_S)⊗I2
   +(conjugate(V)⊗I2)[I2⊗I2−(1/2)F2](conjugate(V)†⊗I2)`.       (1)

Here F2 is the swap on C²⊗C². The first term is a PSD product operator. To decompose the second, let ρ_ψ=|ψ><ψ| for a unit qubit ψ, let `ρ_ψ^perp=I2−ρ_ψ`, and integrate over **all** pure qubit directions with normalized unitary-invariant measure. The elementary Bloch-sphere moments are

`integral rho_psi dpsi = I2/2`,
`integral rho_psi⊗rho_psi dpsi = (I2⊗I2+F2)/6`.

The second identity follows from `rho=(I+r·sigma)/2`, rotational symmetry `integral r_i=0`, `integral r_i r_j=delta_ij/3`, and `F2=(I+Σ_i sigma_i⊗sigma_i)/2`. Therefore

`integral rho_psi⊗rho_psi^perp dpsi
 = (I2⊗I2)/3−F2/6
 = [I2⊗I2−F2/2]/3`.                                      (2)

Equations (1)–(2) express the entire Choi operator as a sum/integral of PSD product operators. The integral is over all directions, not a chosen target/control instance.

## 3. Direct measure–prepare proof

By the displayed Choi expansion, for every 2×2 complex matrix X the actual map is

`(Psi∘iota_V)(X) = Tr(X)(I4−P_S)
  +3 integral <conjugate(psi^perp), X conjugate(psi^perp)>
                 |conjugate(V) psi><conjugate(V) psi| dpsi`.          (3)

This identity follows by checking the four input matrix units, or by applying `Theta(X)=Tr_input[J(Theta)(I⊗X^T)]`. For PSD X on `C²⊗R`, each bracket becomes the PSD R-operator

`(<conjugate(psi^perp)|⊗I_R) X (|conjugate(psi^perp)>⊗I_R)`;

the first term similarly gives `(I4−P_S)⊗Tr_input(X)`. Hence (3), tensored with id_R, is a positive integral/sum of product PSD operators. Finite-dimensional closure of the separable cone pays the limit. This proves the stated **all-isometry/all-ancilla** local result without a numerical certificate or source verifier.

The transpose basis matters: it is `conjugate(V)` on the output and `conjugate(psi^perp)` in the input functional. Dropping either conjugation is not the same map for complex V.

## 4. Relation to the original three-copy target: exact gap

For the actual original map `Phi(X)=Tr(X)I4−X/2`, one has `Phi=T∘Psi`; hence on H=(C⁴)^tensor3,

`Phi^tensor3 = T_H ∘ Psi^tensor3`.

The original arbitrary-complex-rank<=2 q3 statement is equivalently 2-positivity of `Phi^tensor3`, by the complete eight-subset original-index proof in `frontier-20261028-d4-positive-map-all-subsets-addendum-v1.md`, SHA256 `8cd42f794b79fec63fd8d607b41554891b3b6409d75efb7278ac29c962cbf500`. It is **not** a consequence of the single-site lemma alone.

For a global isometry `A:C²→(C⁴)^tensor3`, a sufficient—but potentially stronger—analytic route would show that `Psi^tensor3∘iota_A` is entanglement-breaking for every A. Positivity under output transpose would then give the full original q3. The precise unpaid predicate is whether this global tensor/composition assertion, or a direct proof of its weaker PPT condition, holds for **all** global A. A two-dimensional **global** encoded range does not supply an a priori two-dimensional local input support on each of the three C⁴ sites; equation (3) therefore cannot simply be applied independently at each site. No tensor-stability claim, selected local/global example, counterexample or all-A proof is made here.

The already-public paper makes the full original target claim, and the separate computer-assisted d4 certificate is audited independently in `frontier-20261028-d4-consolidated-proof-dossier-v3.md`, SHA256 `5fd7eae54aecf154113461982fb429704dfe0cf53bbc786281c54356e280b223`. This local lemma is **not** used to manufacture a second full-target proof or a novelty claim. Main explicitly kept the earlier projector formulation unreviewed; this distinct written lemma is likewise unreviewed until a prospectively assigned review.

This work follows Main's actual read of `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`, and explicit prospective resumption. The earlier 20/30-minute timing gaps and unknown cause remain disclosed, with no continuous-supervision, parent/f62, human/family, formal/Lean, all-d or operational implication inferred.
