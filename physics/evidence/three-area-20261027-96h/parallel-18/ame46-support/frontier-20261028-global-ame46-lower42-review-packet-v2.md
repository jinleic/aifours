# Complete review packet: candidate global AME(4,6) support lower bound 42

Owner: **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:47:22 PDT 2026`; this is not an exact completion time. This is a **WRITTEN scientific candidate**, not a formal or independently accepted proof. The only named mathematical import is the classical theorem that there is no pair of orthogonal Latin squares of order six. No earlier unreviewed orbit candidate is a premise.

## Claim and boundary

Every normalized complex AME(4,6) state, in every product basis, has at least **42** nonzero coefficients. More precisely, at most 30 coefficients can have the maximal possible modulus `1/6`.

The published 60-term AME state supplies an upper bound 60. [Pandya arXiv:2610.16673v1 §VI](https://arxiv.org/html/2610.16673#S6) reports the lower bound 38; if the present argument withstands review, it would give 42 instead. This is a comparison with that cited statement only: priority and novelty have not been independently audited. We do not claim a 42-term example, the exact global minimum, formal proof, or independent acceptance.

## 1. Saturated coefficients and residual projections

Fix any product basis. For every pair ij of the four parties, 2-uniformity gives `ρ_ij=I_36/36`; equivalently every 2|2 flattening `U=6ψ` is a 36×36 unitary matrix. Each row and column of the ψ flattening therefore has squared norm `1/36`.

Call a coefficient *maximal* if its modulus is `1/6`. In **every** 2|2 cut, a maximal coefficient is the only nonzero entry in its row and its column: its square `1/36` exhausts each norm. Conversely, any singleton row or column has its unique entry of modulus `1/6`. Distinct maximal coefficients cannot share any two coordinates.

Let P be the maximal positions, `t=|P|`, let E be all other nonzero positions, and put `n=36−t`. In every cut, the P entries occupy t distinct singleton rows and columns. Deleting those matched rows and columns leaves an n×n unitary submatrix: after permuting rows and columns the full unitary is the direct sum of t one-dimensional unitary blocks and that residual block. Its rows and columns are nonempty. None is a singleton, because a singleton in a unitary row or column would again have coefficient modulus `1/6` and would belong to P.

Consequently, with `π_ij` denoting projection onto any **one of the six** coordinate pairs ij,

`|π_ij(E)|=n`, and every pair value in `π_ij(E)` has at least two E extensions.  (1)

This quantifier applies to all six projections: each is a row or column projection in one of the three complementary 2|2 cuts. Counting E entries in any residual flattening gives

`N:=support(ψ) = t+|E| ≥ t+2n = 72−t`.                            (2)

There are at most 36 maximal entries since they occupy different rows. If t=36, every two-coordinate projection of P is a bijection. Label the 36 cells by the first two coordinates: the third and fourth coordinates are then orthogonal Latin squares of order six. Such a pair does not exist by Tarry's classical no-OLS(6) theorem, the only external mathematical import. If t=35, the 1×1 residual unitary would be a singleton and hence maximal, contradicting its removal. Thus `n≥2`.

## 2. Fiber/variation incidence lemma

Fix a coordinate i. Write `r=|π_i(E)|`, and for each value v in that projection write `E_v={x∈E:x_i=v}`. Say that fiber `E_v` *varies in coordinate j* when `|π_j(E_v)|≥2`.

Every fiber varies in at least two distinct other coordinates. If it varied in none, it would contain one tuple. If it varied only in j, then fixing the i-value and any j-value would uniquely determine all four coordinates, violating the two-extension condition in (1).

For any of the three other coordinates j, projection pairs with different i-values are disjoint, so

`Σ_v (|π_j(E_v)|−1) = |π_ij(E)|−r = n−r`.

Each fiber varying in j contributes at least one to this sum. Therefore at most n−r fibers vary in j. Counting all fiber/coordinate variation incidences gives

`2r ≤ 3(n−r)`, equivalently `r≤floor(3n/5)`.                     (3)

For n=2 or 3, this gives r≤1 for **every** coordinate. All pair projections would then have size at most one, contradicting (1). Thus n=2 and n=3 are impossible.

## 3. n=4: residual four-qubit AME contradiction

For n=4, (3) gives at most two values per coordinate. No coordinate can be constant: if i were constant, `|π_ij(E)|` would be at most the number of values of j, at most two, not four. Hence every coordinate has exactly two values, and each size-4 two-coordinate projection is the full product of those two local alphabets.

In each of the three cuts the residual 4×4 block of `U=6ψ` is unitary, and its rows and columns are exactly the four binary coordinate pairs just identified. Let ψ_E be the state consisting only of E entries. Its norm squared is `4/36=1/9`, because the residual block of U has four unit-norm rows. Therefore `φ=3ψ_E` is normalized. In each of the three cuts its 4×4 flattening is the residual unitary divided by 2; each two-qubit reduction is `I_4/4`. Thus φ would be an AME(4,2) state.

A self-contained Pauli proof rules that out. Expand the pure four-qubit density matrix as

`ρ=2^(−4) Σ_{P∈{I,X,Y,Z}^4} r_P P`, with real `r_P=Tr(ρP)`.

All nonidentity expectations of weight 1 or 2 vanish by two-uniformity. Purity `Tr(ρ²)=1` gives `Σ_P r_P²=16`. A three-qubit marginal has purity 1/2, equal to the purity of its complementary one-qubit marginal. Its only possible nonidentity Pauli expectations have weight 3, hence

`(1+Σ_{weight-3 on that triple} r_P²)/8=1/2`.

Each of the four triples contributes 3, so the total weight-3 squared sum is 12; the weight-4 squared sum is `16−1−12=3`. The spin-flipped matrix `ρ̃=Y^{⊗4} \barρ Y^{⊗4}` is positive semidefinite. Spin flip multiplies a Pauli of weight w by `(−1)^w`; consequently

`Tr(ρρ̃)=(1−12+3)/16=−1/2`,

which is impossible for positive semidefinite ρ and ρ̃. Hence n=4 is impossible.

## 4. n=5: full three-fiber normal form

For n=5, every coordinate takes at most three values by (3). At least one coordinate must take three values: if all took at most two, every pair projection would have at most four values, contrary to (1).

Fix a three-valued coordinate i. Both sides of the incidence inequality (3) equal 6. Thus:

- each of the three i-fibers varies in exactly two of the remaining three coordinates;
- each remaining coordinate varies in exactly two of the three fibers;
- each such variation uses exactly two values, since the total excess `n−r=2` for that coordinate must be spent as one extra value in each of two fibers.

Each fiber therefore fixes precisely one of the three other coordinates, and each other coordinate is fixed in exactly one fiber. Relabel the i-values and the other coordinates so that fiber j fixes coordinate j, j=0,1,2. In each fiber the other two coordinates vary in two values. The two-extension rule forces the **complete four-point 2×2 product** in that fiber: for each value of one varying coordinate, there must be two extensions, and only the two values of the other varying coordinate are available. Hence E is exactly the union of three such four-point fibers.

## 5. Analytic n=5 projection/XOR contradiction

For each coordinate j∈{0,1,2}, let `S_{j,k}` and `S_{j,l}` be its two-element value sets in the other two fibers, where `{j,k,l}={0,1,2}`. Define the Boolean flag

`e_j=[S_{j,k}=S_{j,l}]`.

Consider the projection onto two coordinates j,k. In the remaining fiber l both coordinates vary, giving a four-point base rectangle. Fiber j contributes a two-point edge with j fixed and k varying; fiber k contributes a two-point edge with k fixed and j varying. By (1) their union must have exactly five points.

Each fixed singleton must lie in the corresponding base two-set; otherwise its edge alone contributes two new points. Since each local coordinate has at most three values, a varying two-set either equals the base two-set and adds zero points, or differs by exactly one value and adds exactly one point. If both edges add one, their new points are different: one is inside the base in coordinate j and outside it in k, while the other is outside in j and inside in k. Therefore a five-point projection requires exactly one edge to add a point, which is equivalent to

`e_j ≠ e_k`.                                                        (4)

All three pair projections among j=0,1,2 must have size five, so (4) would make three Boolean values pairwise distinct. This is impossible. Thus n=5 is impossible.

## 6. Final case split and global support count

The classical no-OLS(6) theorem rules out n=0, the residual-unitary singleton rule rules out n=1, the incidence lemma rules out n=2 and n=3, §3 rules out n=4, and §5 rules out n=5. Therefore `n≥6` and `t=36−n≤30`. Substituting in (2) gives

`N≥72−t≥42`,

for every AME(4,6) state and every product basis. This completes the written candidate subject to independent review and the named no-OLS(6) import.

## 7. Independent exact controls and reproducibility

The analytic XOR proof is the proof; the following finite checks are independent controls. The exhaustive n=5 normal form is finite: each of the three remaining coordinates chooses a singleton in its fixed fiber (3 choices) and a two-element subset of a three-symbol alphabet in each other fiber (3 choices each), for `3·3·3=27` options per coordinate. Padding any smaller local alphabet with an unused third symbol loses no case.

1. **Direct set construction.** `frontier-20261028-five-projection-direct-v1.py`, SHA-256 `b3430b4b49d9660715976fdb7bb1467253767a821d09e40132057b7c108d7180`, directly builds all `27³=19683` three-fiber supports. Receipt `frontier-20261028-five-projection-direct-v1.json`, SHA-256 `3e86e8f7164d4a8986199124e78c7f86f872b99e6dcf157a7332d744362c856f`, reports zero with remaining pair projection sizes `(5,5,5)` and 648 with the relaxed target `(5,5,6)`.
2. **Independent 9-bit compatibility graph.** `frontier-20261028-five-projection-bitgraph-v1.py`, SHA-256 `0364d35d908e44db9e061c9bdd24044a6a3006838bb30a64a3c8382c16fbaecc`, represents each pair projection as a 9-bit set. Receipt `frontier-20261028-five-projection-bitgraph-v1.json`, SHA-256 `8de5dd28dc01f80564e6ba16256f5fe1270e448b265a0903c5d4527b38150401`, records 144 compatibility edges in each of the three graph bipartitions, 1080 two-edge wedges, zero triangles, and all edge masks.
3. **XOR lemma control.** `frontier-20261028-five-projection-xor-controls-v1.py`, SHA-256 `ed1624509435de960f40816de5f8e4a9dbd37fd46d14125402323b0133f76ce4`; receipt SHA-256 `a3787da565a2d45757857deddf654f387b6616704ae0aa2ac1ef29dd9c8b7570`. It checks all `3·27²=2187` coordinate-option pairs, finds 432 five-point projections with zero XOR-characterization failures, and rejects a weakened OR condition in 432 cases.

Run each source with `python3 -B <checker.py> <new-output.json>`; the output path must not already exist. These are exact finite computations, not formal proof, cross-model review, or priority clearance.
