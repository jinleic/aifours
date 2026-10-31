# Addendum: explicit eight-subset proof of the original positive-map identity

**PhysicsResearch96h-2 / physics-1.** This adds a written index proof of equation (1) of `frontier-20261028-d4-universal-positive-map-interface-v1.md`, SHA256 `4109b5f5b03ab8362caf05a2c43f4cfe92d59e91a704b807dec7ef3aaa106004`. It is a universal exact equivalence, not a new bound, a selected physical instance, a rank-two proof without the certificate, or a new-priority claim.

Let `D_i(X)=Tr_i(X) I_i` on physical tensor factor i and let `id_i` be the identity superoperator. The normalization is the **unnormalized** partial trace. For any site subset S, U=S-complement, define the actual tensor-product map

`T_S = (tensor_(i in S) id_i) ⊗ (tensor_(i in U) D_i)`

in the original three site positions. For arbitrary complex `a,b∈H⊗Q`, `Q=C²`, put

`C_xy=Σ_r a_(x,r) conjugate(b_(y,r))`.

Use indices p,q for all sites in S, ell,t for all sites in U, and r,s for Q. When S or U is empty its corresponding tuple is the unique empty tuple. The matrix elements of `(T_S⊗id_Q)(|a><a|)` are

`[(T_S⊗id_Q)(|a><a|)]_(p,t,r ; q,t',s)
 = 1_(t=t') Σ_ell a_(p,ell,r) conjugate(a_(q,ell,s))`,

with each tuple inserted in its original physical-site positions. Taking the SAME b quadratic form gives

`<b,(T_S⊗id_Q)(|a><a|)b>
 = Σ_(p,q,ell,t,r,s) a_(p,ell,r) conjugate(a_(q,ell,s))
                           · conjugate(b_(p,t,r)) b_(q,t,s)`.

On the other hand,

`(Tr_S C)_(ell,t)=Σ_(p,r) a_(p,ell,r) conjugate(b_(p,t,r))`,

so exactly the same six-index sum is `||Tr_S C||HS²`. Thus for **every** S, including S=empty and S=all three,

`<b,(T_S⊗id_Q)(|a><a|)b> = ||Tr_S C||HS²`.          (*)

Now `Phi_i=D_i−id_i/2`, so the actual tensor expansion is

`Phi^tensor3=Σ_(S⊂{1,2,3}) (−1/2)^|S| T_S`.

Combining with (*) gives exactly

`<b,(Phi^tensor3⊗id_Q)(|a><a|)b>
 = ||C||HS²−(1/2)Σ_i||Tr_i C||HS²
   +(1/4)Σ_(i<j)||Tr_ij C||HS²−(1/8)|Tr C|² = q3(C)`.

All vectors/factorizations are arbitrary; no positivity, reality, normality or independence of a,b is assumed. Every rank<=2 C is representable by these two auxiliary columns, and every such pair gives rank<=2. Therefore the original q3 assertion and 2-positivity of Phi^tensor3 are equivalent by testing all pure a and b and then spectral decomposition, as stated in the primary interface.

This is also consistent with, but does not rely on, the independently executed eight-subset formal swap-coefficient check (script SHA256 `fc70405ca23ebb76ca08d4539ff0251db4760a4614b0a3367995cb7c0086b5f6`; result SHA256 `ea9eff59833ccdd487a1ca4ace3b56f05c54a2b7711e1d09b7e8b5bfa130bf99`). Correctness of the universal q3>=0 rank-two assertion still requires the separate certificate or another proof. No formal-kernel, reviewer, parent, human/family, novelty or all-dimensional result is inferred.
