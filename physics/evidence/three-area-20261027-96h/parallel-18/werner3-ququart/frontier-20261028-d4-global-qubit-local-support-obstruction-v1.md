# Why the local qubit-corner lemma does not automatically tensor

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN structural proof of the exact gap in `frontier-20261028-d4-local-qubit-corner-eb-analytic-v1.md`, SHA256 `3589a59a3dc019da87169a63844995c63e2016167dbcf1e863a048815a96eee8`. It evaluates **no chosen physical state, control, boundary, numerical parameter or q3 instance**. It is not a counterexample to the original theorem, an analytic q3 proof, a novelty claim or a parent/reviewer/formal result.

## Global encoded dimension does not bound a local support by two

Write H=A⊗B with `dim A=4`, `dim B=16`; here A is any one of the three actual local C⁴ sites and B is the other two. For an isometry `V:C²→H`, define the local support operator

`L_A(V) = Tr_B(VV†) >= 0`.

Although `rank(VV†)=2` globally, the condition `rank(L_A(V))<=2` is **not** automatic: full local rank4 is possible. This is an abstract linear-algebra existence statement, not an evaluated target instance:

1. The tensor/matrix identification `A⊗B ≅ Hom(B*,A)` maps a vector u to a 4×16 linear map X_u. Full-row-rank maps exist because `dim B>=dim A`; equivalently the vanishing of all 4×4 minors describes a proper determinantal subset. Normalize any such u. No particular entries or target parameters are specified.
2. Since `dim H=64>1`, every unit u extends to an orthonormal pair (u,v), giving a global isometry V with those columns.
3. `Tr_B |u><u| = X_u X_u†` has rank4, while

   `L_A(V) = Tr_B |u><u| + Tr_B |v><v| >= Tr_B |u><u|`.

   Therefore `L_A(V)` has rank4. This proves that two-dimensional global encoded range alone does not supply the local two-dimensional corner hypothesis.

The same argument applies to any of the three sites by permutation. It does not assert that every V has full local support, evaluate the Werner functional or demonstrate any failure of the original q3 inequality.

## Consequence for the exact analytic route

The local lemma proves `Psi∘iota_W` entanglement breaking for every **local** isometry W:C²→C⁴. To infer the original three-copy target by separately applying that lemma at the three local sites, one would need additional mathematics ensuring the relevant local inputs/correlations factor through valid two-dimensional corners or otherwise establishing a global tensor/PPT theorem. The global isometry condition alone does not give that factorization. No claim is made that such a global proof is impossible; this note records the precise unclosed step rather than converting the local lemma into a full-target assertion.

No held historical result is a premise. The separate public-source computer-assisted d4 certificate and all of its trust/review boundaries are unchanged. The earlier 20/30-minute cadence gaps remain disclosed in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`; no parent/f62, formal/Lean, independent human/family, all-d, operational or novelty claim follows.
