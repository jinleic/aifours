# A candidate global 42-support lower bound for AME(4,6)

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:42:51 PDT 2026`; not an exact completion clock. **WRITTEN author candidate**, elementary except for the explicitly named classical no-OLS(6) theorem. The finite checks below are controls, not the proof. Independent scientific review is required before acceptance; this is not a formal proof or a novelty determination.

## 1. Claim

For every normalized complex AME(4,6) state ψ and **every** choice of product basis,

`support(ψ) ≥ 42`.                                                     (1)

The explicit 60-term state of [Pandya, arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673#S2.T1) gives a known upper bound 60, so this candidate would narrow the minimum to `42 ≤ m ≤ 60`. The cited paper states a lower bound 38 in its discussion, based on classical-code constraints; if independently accepted, (1) would improve that stated bound by four. This comparison is to that source, not a completed priority or novelty audit.

The proof below establishes the stronger structural necessary condition that **at most 30 coefficients can have modulus 1/6**. It does not claim existence of a 42-term state or determine the minimum.

## 2. Isolated maximal coefficients and the residual support

Fix an arbitrary product basis. For any pair of parties, its reduced density matrix is `I_36/36`. Thus a 2|2 flattening `U=6ψ` is a 36×36 unitary matrix, and each row of ψ has squared norm 1/36. A coefficient is *maximal* if its modulus is 1/6. Any such coefficient is the sole nonzero entry in every 2|2 row or column containing it, because its squared modulus already exhausts the row/column norm. Conversely, a singleton row contains a maximal coefficient.

Let P be the set of maximal coefficient positions, `t=|P|`, and E the remaining nonzero coefficient positions. In every 2|2 cut the P entries occupy t distinct singleton rows and columns; deleting them leaves an `n×n` unitary submatrix, where `n=36−t`. Every residual row and column is nonempty and has at least **two** E entries: a singleton in a residual row would itself have modulus 1/6 and belong to P. Consequently, for every pair of distinct coordinate positions i,j,

`|π_ij(E)|=n`, and every pair in `π_ij(E)` has at least two extensions in E.  (2)

Also

`support(ψ) = t+|E| ≥ t+2n = 72−t`.                                (3)

The maximal entries form a length-4, distance-at-least-3 code: no two share any two coordinates. Thus `t≤36`. If `t=36`, every two-coordinate projection is a bijection, which is equivalent to a pair of orthogonal Latin squares of order 6. **Named external import:** such a pair does not exist, the classical solution of Euler's 36 officers problem, proved by Tarry; see also the discussion and references in the cited Pandya paper. If `t=35`, the 1×1 residual unitary is a singleton and would be maximal, contradicting its definition. Hence `n≥2`. We now rule out n=2,3,4,5.

## 3. Incidence lemma for residual coordinates

Fix one of the four coordinates i. Let r be the number of values it takes in E and write its nonempty fibers as `E_v`. Every fiber must vary in **at least two distinct** other coordinates. If it varied in none it would be a singleton; if it varied only in coordinate j, then fixing its i-value and a j-value would specify the whole tuple, contradicting the two-extension condition (2).

For each other coordinate j,

`Σ_v (|π_j(E_v)|−1) = |π_ij(E)|−r = n−r`.

Every fiber which varies in j contributes at least 1 to this sum, so j can vary in at most n−r fibers. Summing the three coordinates j and counting fiber/coordinate incidences in both ways gives

`2r ≤ 3(n−r)`, hence `r ≤ floor(3n/5)`.                           (4)

This statement is purely combinatorial; it uses only (2), not coefficients, orthogonality phases, or a selected tensor.

For n=2 or n=3, (4) gives r≤1 for **each** coordinate. Then each two-coordinate projection has size at most 1, contrary to (2). These cases are impossible.

## 4. n=4 would give an AME(4,2), which cannot exist

For n=4, (4) gives r≤2 for each coordinate. If one coordinate were constant on E, its pair projection with any other coordinate would have cardinality at most 2, not 4. Thus every coordinate has exactly two values. Since each two-coordinate projection has four values, it is the full product of those local two-element alphabets.

In each 2|2 cut the residual 4×4 submatrix `U_E` is unitary and its four rows and columns are exactly these binary coordinate pairs. The residual state has norm squared `n/36=1/9`; after multiplying it by 3, the resulting normalized four-qubit state has flattening `U_E/2` in each cut and is therefore AME(4,2).

For completeness, here is a short self-contained contradiction for such a state. Expand its pure density matrix as

`ρ=2^(-4) Σ_{P∈{I,X,Y,Z}^4} r_P P`,  `r_P=Tr(ρP)∈R`.

Two-uniformity makes all nonidentity Pauli expectations of weight 1 or 2 vanish. Purity gives `Σ_P r_P²=16`. For each triple of qubits, the reduced state has purity 1/2, equal to the purity of its complementary single qubit. Its only possible nonidentity Pauli expectations have weight 3, so

`(1 + Σ_{weight-3 on that triple} r_P²)/8 = 1/2`.

Each triple therefore contributes 3, and the total weight-3 squared sum is 12. The weight-4 squared sum is `16−1−12=3`. Let `\widetildeρ=Y^{⊗4}\overlineρ Y^{⊗4}`. It is positive semidefinite, and spin flip sends every weight-w Pauli term to `(-1)^w` times itself. Therefore

`Tr(ρ \widetildeρ) = (1−12+3)/16 = −1/2`,

contradicting positivity. Hence n=4 is impossible.

## 5. n=5 is excluded by a three-fiber parity obstruction

For n=5, (4) gives at most three values per coordinate. At least one coordinate must take exactly three values: if every coordinate took at most two values, every two-coordinate projection would have at most four values, contradicting (2).

Fix a three-valued coordinate i. In (4), `2r=3(n−r)=6`, so equality holds throughout the incidence count:

- each of its three fibers varies in exactly two of the other three coordinates;
- each of the other three coordinates varies in exactly two fibers;
- each such variation uses exactly two values, since the two available excess incidences in a projection cannot be spent on a third value in one fiber.

Thus each fiber has one fixed other coordinate, and the three fixed-coordinate choices are distinct. After relabeling the i-values, call the other coordinates 0,1,2 and arrange that fiber j fixes coordinate j. Each fiber varies the other two coordinates in two values each. The two-extension rule (2) makes its support the **full 2×2 Cartesian product**: for each of the two values of either varying coordinate, both values of the other varying coordinate must occur.

For each coordinate j, let `S_{j,k}` and `S_{j,l}` be its two-element value sets in the other two fibers, and define the Boolean flag

`e_j = [S_{j,k}=S_{j,l}]`, where `{j,k,l}={0,1,2}`.

Consider the projection onto coordinates j,k. In the remaining fiber l both vary, producing a 2×2 base rectangle with four points. In fiber j, coordinate j is a singleton and k varies, producing a two-point edge; in fiber k the roles reverse. The projection must have exactly five points.

First, each fixed singleton must belong to the corresponding base two-set: otherwise its two-point edge adds at least two points outside the rectangle. Since a local coordinate has at most three values, any two distinct two-element sets differ by exactly one value. Therefore each of the two extra edges adds either zero points (its varying two-set agrees with the base) or one point (it differs). If **both** edges add one, their added points are distinct: one is inside the base on the j coordinate and outside on k, while the other is outside on j and inside on k. Thus exactly one edge must add a point. Equivalently,

`|π_jk(E)|=5  ⇒  e_j ≠ e_k`.                                       (5)

All three pairs j,k must have projection cardinality 5, so (5) would make three Boolean flags pairwise distinct. This is impossible. Hence n=5 is impossible.

## 6. Conclusion and exact controls

Sections 2–5 show that n cannot be 0,1,2,3,4,5. Thus `n≥6` and `t≤30`. The row count (3) then gives `support(ψ)≥72−30=42`, proving the candidate claim conditional only on the named classical no-OLS(6) theorem and independent review of the written argument.

Three separately structured exact finite controls exercise the n=5 argument:

- `frontier-20261028-five-projection-xor-controls-v1.py`, SHA-256 `ed1624509435de960f40816de5f8e4a9dbd37fd46d14125402323b0133f76ce4`; receipt SHA-256 `a3787da565a2d45757857deddf654f387b6616704ae0aa2ac1ef29dd9c8b7570`. It checks the full two-coordinate projection/XOR characterization in `3·27²=2187` cases, with 432 projection-5 cases and zero discrepancies; replacing XOR by OR is rejected in 432 cases.
- `frontier-20261028-five-projection-direct-v1.py`, SHA-256 `b3430b4b49d9660715976fdb7bb1467253767a821d09e40132057b7c108d7180`; receipt SHA-256 `3e86e8f7164d4a8986199124e78c7f86f872b99e6dcf157a7332d744362c856f`. It builds all `27³=19683` three-fiber supports and finds none with the three remaining projection sizes `(5,5,5)`; the relaxed `(5,5,6)` target has 648 witnesses.
- `frontier-20261028-five-projection-bitgraph-v1.py`, SHA-256 `0364d35d908e44db9e061c9bdd24044a6a3006838bb30a64a3c8382c16fbaecc`; receipt SHA-256 `8de5dd28dc01f80564e6ba16256f5fe1270e448b265a0903c5d4527b38150401`. An independent 9-bit projection representation has 144 compatibility edges in each of three vertex-pair classes, 1080 two-edge wedges, and zero triangles. Its edge masks are included in the receipt.

All these are exact same-harness combinatorial checks; they neither establish independent scientific review nor replace the written incidence, spin-flip, or rectangle proof. No unreviewed orbit result is a premise of (1). The explicit 60-support witness and the 38 lower bound are prior published source material; the current work makes no priority claim.
