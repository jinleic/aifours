# Original d4 rank-two inequality as exact 2-positivity

**PhysicsResearch96h-2 / physics-1.** This is an original-target **universal algebraic interface**, not another numerical bound, selected parameter/state, new-priority claim or substitute for the public certificate. The equivalence and elementary rank-one bound below are written proofs; whether the full rank-two predicate holds is still paid here only by the separately pinned, computer-assisted d4 certificate and its stated trust assumptions. Historical held material is not a premise.

## 1. Exact map statement

Define `Phi:M4(C)→M4(C)` by

`Phi(X)=Tr(X) I4−X/2`,

and define `Lambda=Phi⊗Phi⊗Phi` on H=(C⁴)^tensor3. Then the literal original statement

`q3(C)>=0 for every complex C:H→H of rank<=2`

is **equivalent**, not merely related, to **2-positivity** of Lambda: `Lambda⊗id_2` maps every positive semidefinite operator on H⊗C² to a positive semidefinite operator.

No choice of actual input state or parameter is used. For any C rank<=2 write its singular-value factorization as

`C_xy=Σ_(r=1)^2 a_(x,r) conjugate(b_(y,r))`

for complex a,b in H⊗C²; pad a missing term by zero. For the a,b corresponding to this same C, direct index contraction yields for each site subset S

`||Tr_S C||HS² = <a⊗b,F_Q F_S(a⊗b)>`.

The local identity, including the unswapped auxiliary Q, is

`<a⊗b,F_Q (I−F_i/2)(a⊗b)>
 = <b, (Phi_i⊗id_Q)(|a><a|) b>`

when a,b include only that physical site and Q. The other physical sites carry through as spectator indices. Applying the tensor-product version gives the exact original coefficient expansion

`q3(C)=<b,(Lambda⊗id_Q)(|a><a|)b>`.                    (1)

In particular, if Lambda is 2-positive, the right side is nonnegative for every actual rank<=2 C. Conversely, if q3>=0 on every such C, equation (1), with **arbitrary** a,b, says `(Lambda⊗id_2)(|a><a|)>=0` for every a. Spectral decomposition then gives positivity for every positive semidefinite input, so Lambda is 2-positive. The singular/zero factorization cases are included; no invertibility or Schmidt-rank boundary limit is used.

### Why the Stiefel certificate covers all positive-map inputs

For nonzero a, write its Schmidt decomposition over H|Q as `a=Σ_r s_r A_r⊗e_r`, with s_r>=0, orthonormal A_r and at most two terms; complete A_r if necessary. Let `a0=(A_1⊗e_1+A_2⊗e_2)/sqrt2`. Then `a=(I_H⊗M)a0` for a possibly singular M on Q. Since Lambda acts only on H,

`(Lambda⊗id)(|a><a|)
 =(I⊗M) (Lambda⊗id)(|a0><a0|) (I⊗M†)`.

Thus positivity for all physical Stiefel a0 and all b is also sufficient for all Schmidt coefficients and rank-one boundaries. This explains why the source's maximally mixed a-marginal is no restriction despite the unrestricted input in the definition of 2-positivity.

## 2. Exact Choi matrix and its full spectrum

With unnormalized `Omega=Σ_(j=0)^3 |jj>`, the Choi matrix of Phi is

`J(Phi)=I_16−(1/2)|Omega><Omega|`.

Write `P=|Omega><Omega|/4`; then `J(Phi)=I−2P` is a Hermitian involution with eigenspaces of dimensions 15 (+1) and 1 (−1). Up to the fixed tensor-factor regrouping between input/output sites,

`J(Lambda)=J(Phi)^tensor3`.

Its exact +1 eigenspace dimension is `15³+3·15=3420`, its −1 eigenspace dimension is `3·15²+1=676`, and its ambient dimension is 4096. This is the actual fixed d4 original Choi operator, not a chosen matrix C.

Equation (1) and the standard vectorization identity can be checked directly: 2-positivity is equivalent to nonnegativity of this Choi form on **every** vector of Schmidt rank<=2 across the full H-output | H-input cut, i.e. exactly the original complex-rank domain. Merely knowing the signature, or that a particular subspace contains no low-rank vector, does NOT prove this global cone inequality. In particular the negative Choi eigenvalues show Lambda is not completely positive; they do not exhibit a prohibited rank-two counterexample.

## 3. Independent all-rank-one lower bound and why it does not settle rank two

Define `D(X)=Tr(X)I` and `A(X)=Tr(X)I−X^T`, where transpose is in the fixed standard basis. Both are completely positive. Explicitly,

`D(X)=Σ_(i,j) E_ij X E_ij†`,
`A(X)=Σ_(i<j) (E_ij−E_ji) X (E_ij−E_ji)†`.

Set `Psi=(D+A)/2`, so `Psi(X)=Tr(X)I−X^T/2` and `Phi=T∘Psi`, with T the whole matrix transpose. Consequently

`Lambda = T_H ∘ Psi^tensor3`.

Tensoring the displayed CP decomposition and keeping just the nonnegative `(D/2)^tensor3` summand gives, for every PSD X on H,

`Lambda(X) >= (1/8) Tr(X) I_H`.

Here T_H is a global transpose, an order-preserving map; it is not asserted completely positive. For every rank-one `C=x y†`, equation (1) with a=x, b=y therefore gives the exact uniform lower bound

`q3(C)>= (1/8)||x||²||y||²=(1/8)||C||HS²`.

This is a direct algebraic rank-one result, with no certificate or computation. It does **not** imply 2-positivity: a global transpose tensored with an auxiliary identity need not preserve PSD. The actual rank-two condition remains the independent q3 certificate obligation, not an automatic consequence of this rank-one proof or of complete copositivity.

## 4. Relation to the public d4 certificate and assurance

The physical lift, exact four-entry coupled-Gram source maps, source span, five original equalities, objective coefficients, independently checked 4675-orbit identity and saved-multiplier positivity are consolidated in `frontier-20261028-d4-consolidated-operator-certificate-proof-v1.md`, SHA256 `a6fb579592ffacd71cb0d8c115e5aea20209fc07395304be9b79651dbf1f646e`. If that full certificate route and its explicitly stated checker/runtime assumptions hold, then the same original d4 result is equivalently the 2-positivity of the fixed Lambda above. The Choi spectrum and rank-one result are separate unconditional elementary deductions, not independent confirmation of the rank-two certificate.

No all-d>=9 argument, general distillability implication, strict rank-two gap, chosen-state control, independent family/human review, formal Lean verification or parent adoption is claimed. The published source already made the full-target claim; no scientific priority is asserted.
