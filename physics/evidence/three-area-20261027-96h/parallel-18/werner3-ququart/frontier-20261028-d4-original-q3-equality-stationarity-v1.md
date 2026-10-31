# Exact original-domain equality stationarity for the q3 functional

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN full-original-domain equality criterion, conditional only on global nonnegativity of the original q3 on rank<=2 operators. It does not itself prove that nonnegativity, produce a parameterization of all equalities, imply novelty, or confer physical operational, parent/f62, human/family or formal/Lean acceptance. No chosen physical target state/control or numerical q3 evaluation is used.

## 1. The actual original trace operator

For H=(C⁴)^tensor3 define `D_i(X)=I_i⊗Tr_i X` with the identity inserted at its original site and the partial trace unnormalized. Let

`W=(Id−D_1/2)(Id−D_2/2)(Id−D_3/2)`.

Each D_i is self-adjoint for the Hilbert–Schmidt pairing, D_i²=4D_i, and the D_i commute across sites. Thus W is a self-adjoint involution. For every complex C on H, direct expansion gives

`q3(C)=<C,W(C)>HS`.                                             (1)

Indeed `<C,D_S C>=||Tr_S C||HS²` for every subset S. This is the literal original coefficient/trace convention, not a weighted or normalized substitute.

## 2. No nonzero rank-one equality, independently of the certificate

If `C=x y†` has rank1, each partial-trace norm in q3 is the corresponding physical-swap expectation on `x⊗y`. Since the three site swaps commute and each `I−F_i/2 >= I/2`,

`q3(C)=<x⊗y, product_i(I−F_i/2)(x⊗y)>
       >= ||x||²||y||²/8 = ||C||HS²/8 >0`.

This is a universal written proof for every nonzero rank1 complex C, not a selected target/state test or full rank2 proof.

## 3. Rank-two equality iff stationarity, conditional on global nonnegativity

Assume as a premise that `q3(C)>=0` for **every** complex rank<=2 C. The separately audited public-source fixed-d4 certificate supports that premise subject to its source/code/runtime and review boundaries; the present argument does not silently adopt it.

Let C have **exact rank2** and factor `C=A B†` with A,B:H←C² both full column rank. Set `D=W(C)`. Then the following are equivalent:

1. `q3(C)=0`.
2. `D B=0`.
3. `A† D=0`.
4. Both matrix conditions in 2–3 hold.

For 1→2, for arbitrary complex H and every real t the matrix `(A+tH)B†` has rank<=2. Its q3 is therefore nonnegative and has a minimum at t=0. Differentiating the self-adjoint quadratic form gives

`0=2 Re Tr(H† D B)`.

The same argument with iH eliminates the imaginary part, so `D B=0`. For 1→3 vary B instead: `A(B+tK)†` has rank<=2, and arbitrary K and iK imply `A†D=0`.

Conversely, either condition 2 or condition 3 alone makes

`q3(C)=Tr(C†D)=Tr(B A† D)=Tr(A† D B)=0`,

where the traces are taken in the appropriate finite dimensions. This proves the equivalences. They hold for **every** full-column factorization: changing A→AS and B→B S^−† with invertible 2×2 S multiplies the left/right conditions by invertible factors and does not change their validity.

Thus, conditional on global q3 nonnegativity, the **complete original equality set** is C=0 or an exact-rank2 C satisfying either displayed matrix equation. This is an explicit necessary-and-sufficient **stationarity equation**, not a solution of that equation or a claim that the already derived product equality family exhausts it. The source-derived 1237-Gram-vanishing criterion remains a separate, equivalent conditional description.

## 4. Boundaries and provenance

The original public v4 paper already states a sharpness/equality clause. The independent product-class theorem `frontier-20261028-d4-original-q3-product-equality-v1.md`, SHA256 `b4d5f2673d9a2d605681f627e3ad2da943c68b010313c377d6d6fd4b6bd5fb1a`, confirms equality occurs and a universal strictly positive q3 gap is impossible. Nothing here asserts that these product cases are all solutions of the stationarity equations.

This theorem uses the original q3 definition, standard finite-dimensional differentiation/SVD and, for §3 only, a clearly declared global nonnegativity premise. It uses no content, conclusion or guide from the earlier elected HELD/ZERO/NONINPUT episode. Main actually read that disclosure and expressly allowed prospective work under contract-addendum-2; the previous 20/30-minute gaps, source review and runtime limits remain as recorded. No counterexample, selected target numerical probe, all-d/physical operational result, novelty, parent/f62, human/family or formal/Lean claim is made.
