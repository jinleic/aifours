# Four-party active-sector support barrier and exact equality criterion

Owner **PhysicsAME46-2**. Actual native prewrite observation **`Wed Oct 28 17:31:47 PDT 2026`**, not exact creation/completion/runtime. **WRITTEN proof + exact finite data checks, author candidate; unreviewed, not novelty-cleared or global minimum acceptance.** This continues the exact verification of Pandya's [published 60-term tensor](https://arxiv.org/html/2610.16673#S2.T1) in `frontier-20261028-two-party-orbit-obstruction-v1.md` (SHA256 `94f85389567b2a3ea8e8f1a418af58977f4fdc3670f4a696fa6512703b7a9f75`) and the arbitrary-three-party obstruction in `frontier-20261028-three-party-orbit-obstruction-v1.md` (SHA256 `81d66a899197064107351d703fda6fbedb7ec7842766c39d1168af27dd8fc07d`).

## 1. Exact statement

In the published tensor's reference product basis, let `H=span{|1>,|2>}` and `K=span{|0>,|3>,|4>,|5>}`. For EACH of the four parties choose an arbitrary unitary

`V_i = U_i ⊕ D_i` on `H⊕K`,

where `U_i∈U(2)` is completely arbitrary and `D_i∈U(4)` is monomial in the displayed K basis (a permutation with phases). Then

`support((V_1⊗V_2⊗V_3⊗V_4) T) ≥ 60`,

with equality at the identity and at nonmonomial examples on ALL FOUR parties. Thus even fully coordinated continuous U(2)^4 changes in this invariant sector cannot improve this particular 60-term witness. This is NOT a proof for arbitrary U(6)^4, another state, or the global AME minimum.

Write `Mon(2)` for the group of 2×2 monomial unitaries and

`X=[[0,1],[1,0]]`, `Z=[[1,0],[0,−1]]`, `Y=[[0,−i],[i,0]]`.

Equality **support=60** holds IF AND ONLY IF BOTH conditions hold:

1. `U_i U_j^T∈Mon(2)` for every distinct party pair i,j;
2. `U_i† Z U_i ∈ {±X,±Y,±Z}` for every party i.                              (E)

The transpose in condition1 is essential: it is the coefficient-matrix action of the second active local unitary, not an adjoint. This is an exact complex-unitary equality criterion; no finite sampling is used to establish the stated iff.

## 2. Independently checked input decomposition

The explicit table `frontier-20261028-pandya-table-v1.txt` has SHA256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`. Every nonzero coefficient belongs to exactly one of two disjoint types:

- **12 P terms:** no coordinate lies in `{1,2}`; each coefficient has numerator `sqrt(2)` in the paper's `1/sqrt(72)` normalization.
- **48 E terms:** exactly two of the four coordinates lie in `{1,2}`. Fix those two party positions i,j and the two K-valued spectator indices. The active 2×2 coefficient matrix is one of `±I,±J,±X,±Z`, where `J=ZX=[[0,1],[−1,0]]`.

For EACH of the six active-party pairs, there are exactly four distinct spectator assignments, one for each type I,J,X,Z up to sign. Thus E comprises **24 disjoint invertible 2×2 blocks**, each with exactly two source nonzeros. Every possible active-party pair/type is actually represented; the equality proof uses this stronger fact, not merely the aggregate counts.

This is an exact finite table property independently checked with a separate parser in `frontier-20261028-sector-block-independent-v1.py`, SHA256 `e47cb9a50800f7206f8c179b03e464c8e97521815b749657b290be51ca410ecf`; its receipt `frontier-20261028-sector-block-independent-v1.json`, SHA256 `4007e9706486fff67b2ce28c73127a171eefda83ea072afdeed3deffa9115d65`, records each block and determinant. A deliberate one-coefficient sign flip was rejected for the intended per-pair type imbalance. A separately structured earlier checker also obtained six of each block type; both are same-harness evidence, not an independent scientific referee.

## 3. Four-party lower bound

The decomposition `H⊕K` is preserved separately at every party. Each P term is sent by the four monomial K-actions to a distinct nonzero P term. Each E block is sent, up to nonzero spectator phases and a spectator-index permutation, to

`U_i M U_j^T`,

where M is its original signed I/J/X/Z matrix. Different active-party pairs and different spectator assignments remain in disjoint output coordinate groups: the K permutations are bijections, and no operation converts an H index into K or vice versa. Thus there is no cancellation between P and E or between two different E blocks.

Every such 2×2 matrix is invertible, so has at least two nonzero entries. Hence the actual full tensor support is at least

`12 + 24·2 = 60`.

The proof also holds for invertible complex U_i and invertible monomial D_i, though nonunitary maps need not preserve AME. For physical unitaries all six marginals remain exactly maximally mixed because the transformation is a product of actual local unitaries. Identity achieves60, so60 is the exact sector-orbit minimum.

## 4. Proof of the equality criterion

An invertible 2×2 matrix with exactly two nonzeros is monomial. Thus equality above is equivalent to every one of the24 transformed blocks being monomial. Let `B_ij=U_i U_j^T`.

**Necessity.** For any i≠j, the actual I-block gives `B_ij∈Mon(2)`. The actual X- and Z-blocks give monomial `U_i X U_j^T` and `U_i Z U_j^T`. Multiplying each on the right by `B_ij^{-1}` gives `U_i X U_i†` and `U_i Z U_i†`, which must be monomial. If i is the second index in our displayed pair ordering, transpose the same argument: `{I,X,Z,J}^T={I,X,Z,−J}`, so it applies to i as well. Every i has a partner.

**Sufficiency.** If all `B_ij` and each `U_i X U_i†`, `U_i Z U_i†` are monomial, then for M=I,X,Z, or J=ZX,

`U_i M U_j^T = (U_i M U_i†) B_ij`

is a product of monomial matrices. Signed source blocks have the same support. Every one has exactly two nonzeros, giving equality.

It remains to rewrite the single-party condition. The traceless Hermitian unitary `N=U† Z U` has a Pauli expansion `n_x X+n_y Y+n_z Z` with real `n_x,n_y,n_z` and `n_x²+n_y²+n_z²=1`. For `M=X` or Z, the coefficient of Z in `U M U†` is `(1/2)Tr(N M)`, namely `n_x` or `n_z`. A traceless Hermitian 2×2 unitary is monomial exactly when that diagonal coefficient is 0 or ±1: if zero it is off-diagonal; if ±1 its off-diagonal entries vanish.

Thus both conjugated X and Z are monomial iff `n_x,n_z∈{0,±1}`. With the unit-length condition this holds iff `N∈{±X,±Y,±Z}`. This proves condition2 of (E), including all phase and degenerate-label choices, with no assumption that the U_i are real. Together with the pair condition it is necessary and sufficient.

## 5. Two explicit nonmonomial equality mechanisms and continuous paths

For common real rotations on all four parties,

`R_θ=[[cosθ,sinθ],[−sinθ,cosθ]]` on H and identity on K,

one has `R I R^T=I`, `R J R^T=J`,

`R Z R^T=cos(2θ) Z−sin(2θ) X`,

`R X R^T=sin(2θ) Z+cos(2θ) X`.

There are six blocks of each type. Therefore the actual support is **60** if either `sin(2θ)=0` or `cos(2θ)=0`, and **84** otherwise. At θ=π/4 all four parties are nonmonomial, X/Z blocks exchange diagonal/off-diagonal support and the new 60-support set intersects the old in **36** coordinates; the 36 common coefficients are unchanged. This is an LU-equivalent witness, not a new orbit or a support improvement.

A second common complex path uses `Q_θ=[[cosθ,i sinθ],[i sinθ,cosθ]]`. Here `Q Z Q^T=Z`, `Q J Q^T=J`, while I and X mix as `I→cos(2θ)I+i sin(2θ)X`, `X→cos(2θ)X+i sin(2θ)I`. Its support has the same 60/84 classification. At θ=π/4 the all-complex endpoint also has support60, overlaps the original in36 coordinates, and its support intersects the real-rotation endpoint in36 coordinates. All three are the SAME LU orbit.

For the rational-angle real example `cosθ=3/5, sinθ=4/5`, a Q(sqrt2)-integer calculation gave actual support84 and verified normalization and all six 36×36 physical marginals exactly. The 45-degree real and complex endpoints were also materialized and all six marginals verified exactly over Q(sqrt2,i). These are checks of specific constructed states in addition to the written continuous proof, not a replacement for its universal argument.

## 6. Four-party discrete search and exact artifacts

A separate bounded search applied, independently at every party, one equal-angle 2×2 gate on any of15 coordinate pairs and relative phase `z∈{1,i}`:

`(1/sqrt2)[[1,z],[−conjugate(z),1]]`, identity on the other levels.

All `15^4·2^4=810000` combinations were evaluated exactly in Z[sqrt2,i]. Relative phases `−1,−i` are redundant up to output row phases/permutation for a single equal-angle gate, so these results also cover that fourth-root phase set for support. The search reported minimum60, with TWO gate representatives attaining it: all parties acting on pair(1,2), with all z=1 or all z=i. It found no sub-60 support in this FINITE gate alphabet; it does not cover arbitrary angles, general U(6)^4 or all AME orbits.

| Artifact | SHA256 | Observed scope |
| --- | --- | --- |
| `frontier-20261028-sector-block-independent-v1.py` | `e47cb9a50800f7206f8c179b03e464c8e97521815b749657b290be51ca410ecf` | Separate exact table parser and per-pair block-type checker. |
| `frontier-20261028-sector-block-independent-v1.json` | `4007e9706486fff67b2ce28c73127a171eefda83ea072afdeed3deffa9115d65` | 12 P terms; each of six pairs has one I,J,X,Z; sign mutation rejected. |
| `frontier-20261028-common-rotation-structure-v1.py` | `b90c2f969770a6910a34eea990afb2952279a9cabf2f2f60048ca7b9681460b3` | Exact 24-block classification and rational-angle/real-endpoint checks. |
| `frontier-20261028-common-rotation-structure-v1.json` | `aeda757d43da2c7470dfa334d11c40b5edec4fd3731dce1bfc456f462cd9ebef` | Six I,J,X,Z each; 84 rational-angle and60 real endpoint, all six marginals checked. |
| `frontier-20261028-four-party-phase-search-v1.py` | `b9ef00f599868fd1624a818a8b75bdf60c0c95ba5ed3387b0d131e2e8b737403` | Exact sparse search code and direct best-state partial traces. |
| `frontier-20261028-four-party-phase-search-v1.json` | `cc346b975eaf7f08ada1ee54863c0de5762796950f82138b6e57b556ae5f56f4` | 810000 combinations, full histogram, best exact tensor; wall time9.16s. |
| `frontier-20261028-common-complex-endpoint-v1.py` | `4f883996133ffbc41dc4f9a6c508f3308daeba92e58414bb74a58bb7a5faeff2` | Materializes both exact endpoints and compares to search receipt. |
| `frontier-20261028-common-complex-endpoint-v1.json` | `900849868577fad0af77ec7e9ce85f8d46657c327a9546cde9ef7c4ade3c8858` | Both endpoints60, all six marginals; pairwise support intersections36. |

All commands ran as single local `python3 -B` processes with exact integers/rationals; no floating-point zero threshold or scientific program was used as a substitute for the written equality proof. These checks are same-harness, not a third-family/formal verification. The state and its 60-term upper bound are prior source material; no priority claim is made.

## 7. Remaining original-target gap

The theorem settles an entire **continuous four-party sector** of one LU orbit but does not preclude sub-60 support when one or more local transformations mix H with K or mix K nonmonomially, and it says nothing about other AME states. The 810000-gate search adds a bounded exact obstruction outside that sector but is not exhaustive over general unitaries. The original minimum, strict universal lower-bound improvement and an actual sub-60 witness remain open in this work. Independent scientific review of the source table, block classification and (E) proof is still required before adoption.
