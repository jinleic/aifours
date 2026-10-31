# Exact two-column Schur interface for the original d4 target

**PhysicsResearch96h-2 / physics-1.** This is a **WRITTEN universal reformulation** of the original rank<=2 q3 target. It neither narrows to selected inputs/parameters nor gives a new rank-two proof. The precise unpaid analytic step is the single all-Stiefel contraction inequality in §3; the independent computer-assisted source certificate is one separately pinned way to support it. No novelty, human/family/kernel, operational or parent acceptance is claimed.

## 1. Fixed operators and original scope

Set `Phi(X)=Tr(X)I4−X/2` and `Lambda=Phi^tensor3` on H=(C⁴)^tensor3. The all-subset index derivation `frontier-20261028-d4-positive-map-all-subsets-addendum-v1.md`, SHA256 `8cd42f794b79fec63fd8d607b41554891b3b6409d75efb7278ac29c962cbf500`, gives for arbitrary `a,b∈H⊗C²`

`q3(C)=<b,(Lambda⊗id_2)(|a><a|)b>`,
`C_xy=Σ_(r=1)^2 a_(x,r) conjugate(b_(y,r))`.

Every complex rank<=2 C has such a factorization and vice versa. The original target is equivalent to 2-positivity of Lambda. This is the full literal q3 target, including all complex factors, rank0/1, and unnormalized partial traces.

For every unit `x∈H` we have the following uniform operator bound, proved in the pinned map interface using an explicit completely-positive Kraus decomposition:

`Lambda(|x><x|) >= I_H/8`.                                  (2)

This is a **rank-one input** bound; it is not a lower bound on `(Lambda⊗id_2)` or on rank-two q3.

## 2. Exact arbitrary Stiefel block

Let A1,A2∈H be **any** orthonormal pair, and define

`P=Lambda(|A1><A1|)`,
`Q=Lambda(|A2><A2|)`,
`B=Lambda(|A1><A2|)`.

By (2), both Hermitian P,Q are positive definite with `P,Q>=I/8`; consequently their inverse square roots exist even at all rank-deficient original-C boundaries. Lambda preserves adjoints, so `Lambda(|A2><A1|)=B†`.

For the Stiefel vector `a=(A1⊗e1+A2⊗e2)/sqrt2`, the **actual** positive-map output on H⊗C², in the Q-basis block order, is

`(Lambda⊗id_2)(|a><a|) = (1/2) [[P,B],[B†,Q]]`.             (3)

For an arbitrary `b=x⊗e1+y⊗e2`, equation (3) is exactly

`q3(C)=(1/2)[<x,Px>+<x,By>+<y,B†x>+<y,Qy>]`,
`C=(|A1><x|+|A2><y|)/sqrt2`.

Here x,y∈H are arbitrary complex vectors; the cross term B is the **actual** Lambda image of the common source columns, not an independently selectable matrix. Every original rank<=2 C can be put in this form by orthonormal completion of its range, with its corresponding x,y; no SVD inversion or limiting argument is needed.

## 3. Full universal equivalence and exact residual gap

Define the same-pair normalized cross operator

`K(A1,A2)=P^(−1/2) B Q^(−1/2)`.

Congruence of (3) by `diag(P^(−1/2),Q^(−1/2))` gives

`[[P,B],[B†,Q]]>=0`
`iff [[I,K],[K†,I]]>=0`
`iff I−K†K>=0`
`iff ||K||op<=1`.                                           (4)

Thus the original q3>=0 statement for **all** complex rank<=2 d4 operators is equivalent to

`||P^(−1/2) Lambda(|A1><A2|) Q^(−1/2)||op <= 1`

for **every** orthonormal pair A1,A2 in H, with P,Q defined from that SAME pair above. The square-root inverses in (4) are genuinely justified by the uniform bound (2). The statement cannot be replaced by an unrestricted bound on an unrelated B, by positivity of the diagonal blocks alone, or by a finite selection of pairs.

The unpaid all-variable analytic step, if one seeks a proof independent of the source certificate, is precisely (4), equivalently `B†P^(−1)B<=Q`, for every such pair. Nothing in the rank-one bound, mere Choi signature or norm inequality for a selected pair pays it. The earlier unrestricted-factor polynomial-SOS obstruction is not invoked as a premise here.

## 4. Connection to the checked source certificate

The pinned source/certificate proof in `frontier-20261028-d4-consolidated-operator-certificate-proof-v1.md`, SHA256 `a6fb579592ffacd71cb0d8c115e5aea20209fc07395304be9b79651dbf1f646e`, supports the original q3 statement conditional on its exact verifier/runtime and written physical-bridge assumptions. Under those same qualifications it supports the equivalent universal contraction (4). This reformulation is not another independent certificate check, another source theorem, or a derivation of the source's all-d>=9 claim. Its block B is an operator on the actual H, unrelated to an assumption that the source's d4 file contains a `gram2` multiplier.

No selected numerical state, finite parameter control, old held guidance or prior source outcome is used. No full elementary all-Stiefel contraction proof, exact strict gap, equality classification, physical distillability consequence or fresh discovery is asserted.
