# Uniform three-body projection separation for the whole low-rank cone

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN, source-independent all-operator corollary of the 2-local rank theorem. It gives an **unspecified qualitative projection separation**, not a numerical bound, selected physical state/control, q3 strict gap, residual-PPT proof, novelty, parent/f62, human/family or formal/Lean acceptance.

## 1. Exact statement and proof

On H=(C⁴)^tensor3, let

`E_i(C)=(I_i/4)⊗Tr_i C`, `T_i=Id−E_i`, `P=T_1T_2T_3`.

These are Hilbert–Schmidt orthogonal projections, and `ker P` is exactly the full two-local operator subspace. The theorem `frontier-20261028-d4-negative-space-rank-four-theorem-v1.md`, SHA256 `eb07a8ce4d5f3c121873e3d28f628b82a102698c5d8711225c82b81705904172`, proves that every nonzero operator in ker P has rank>=4.

There is therefore an **epsilon>0**, not specified numerically here, such that for every complex C on H with rank<=3,

`||P C||HS >= epsilon ||C||HS`.                                  (1)

To prove it, consider the rank<=3 Hilbert–Schmidt unit sphere K. It is closed because all 4×4 minors vanish, and compact because the finite-dimensional unit sphere is compact. The continuous function C↦||PC|| has no zero on K by the rank theorem, so it has a strictly positive minimum epsilon. Homogeneity gives (1), including C=0. The proof uses the **whole** low-rank set and does not select or evaluate any physical C, state, control, parameter or q3 value.

## 2. Precise relevance and nonimplication

Under the source's Choi regrouping, P is the projection to `Q_1⊗Q_2⊗Q_3`, the positive k=0 sector of the residual Choi partial transpose. Thus (1) gives a uniform nonzero **projection separation from the two-local space**, and in particular from the negative residual eigenspace contained in that space.

This is **not** a strict q3 gap, a numerical spectral/energy estimate, or proof of residual 2-positivity. The unspecified epsilon could be too small to dominate negative-sector contributions, and the full target still requires an actual all-rank<=2 mixed-sector energy inequality or the separately audited source certificate. The assertion is conditional on the unreviewed written rank theorem and standard finite-dimensional compactness; it carries no all-d/operational, novelty, human/model-family, formal/Lean, parent or f62 acceptance.

No old held result is a premise. The earlier cadence deviations and Main's actual prospective resumption remain as disclosed in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`.
