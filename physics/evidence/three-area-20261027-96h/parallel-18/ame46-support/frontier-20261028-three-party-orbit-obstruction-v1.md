# Exact three-party support minimum for a published 60-term AME(4,6) tensor

Owner **PhysicsAME46-2**. Native prewrite observation **`Wed Oct 28 17:13:31 PDT 2026`**; not an exact write/completion/runtime clock. **WRITTEN + exact finite support checks; author candidate, not yet independently peer-reviewed, formally verified or novelty-cleared.** The preceding two-party bound and public source/witness validation are in `frontier-20261028-two-party-orbit-obstruction-v1.md`, SHA256 `94f85389567b2a3ea8e8f1a418af58977f4fdc3670f4a696fa6512703b7a9f75`.

## 1. Exact claim, quantifiers and limitations

Let `T` be the explicit real 60-term tensor transcribed from [Pandya, arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673#S2.T1), with coefficient table `frontier-20261028-pandya-table-v1.txt` SHA256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38` and normalization `sqrt(72)`.

For **each** choice of a spectator party, **every** triple of arbitrary invertible complex local `6×6` matrices acting on the other three parties leaves the tensor with at least **60** nonzero coefficients in the product basis where the spectator is fixed. The identity triple attains60. In particular this holds for arbitrary physical unitaries; a monomial unitary on the spectator may also be included. Therefore any product unitary taking THIS tensor to support below60 must be nonmonomial on **all four parties**.

The statement is specific to the published witness's local orbit. It is NOT a lower bound for every AME(4,6) state, a proof that 60 is the global minimum, or an exclusion of four-party cancellations. The published source reports 38–60; its source lower-bound import was not independently re-proved here. An exact sub-60 witness remains unconstructed.

## 2. A general matrix-pencil rank lemma

Let `T∈A⊗B⊗C` and write `T=sum_(j=1)^d e_j⊗M_j` for a chosen basis of A. Assume the matrices `M_j` are linearly independent. Let

`L={x∈C^d : rank(sum_j x_j M_j)≤1}`.

Suppose L is contained in a linear subspace `W` of dimension w. Under arbitrary invertible maps on A,B,C, the coefficient support of the transformed tensor is at least

`w + 2(d-w) = 2d-w`.                                                            (1)

**Proof.** An invertible change of the A basis makes the d output pencil vectors `x_1,…,x_d` a basis of `C^d`. Invertible changes of B,C send each matrix to `U (sum_j x_{tj} M_j) V^T`, preserving its rank. Since `M_j` are independent, each nonzero `x_t` gives a nonzero matrix, rank at least1. At most w of the basis vectors can lie in W, so at least d-w output matrices have rank at least2. Each output matrix has at least rank-many nonzero entries, and their disjoint A-index slices partition the full tensor support. Summing gives (1). ∎

Nothing in this lemma assumes orthogonality, real matrices, a chosen optimizer, or an AME condition. A smaller w or a stronger lower rank on `L^c` would strengthen it. The proof only needs a subspace **containing** the rank-at-most-one vectors; those vectors need not fill W.

## 3. What the exact finite certificate establishes

Fix ANY spectator party `s`, ANY original spectator level `t`, and ANY one of the remaining three parties as pencil axis A; choose the other two as matrix row/column axes. This gives **72** distinct matrix pencils (4 spectators ×6 levels ×3 active axes).

From the explicit table, the independently checked facts are:

1. Each of the six pencil generators has nonzero coefficients, and their matrix-cell supports are pairwise disjoint. Thus the six are linearly independent and every matrix cell of the pencil is a nonzero fixed scalar times at most one variable `x_j`.
2. For each of the **24** pencils arising from 12-entry spectator slices, no nonempty subset of the six variables has a support union equal to a row-set × column-set rectangle. Consequently **no nonzero pencil matrix has rank1**: a nonzero rank-one complex matrix has exactly a rectangular nonzero support.
3. For each of the **48** pencils arising from 9-entry spectator slices, the ONLY variable-support masks whose cell union is rectangular are three singleton masks. Thus every rank-one pencil vector is contained in the coordinate subspace spanned by those three variables, of dimension3. The matrices associated with these singleton masks are themselves nonzero one-entry matrices; no additional rank-one possibilities are claimed.

These statements cover ALL `2^6−1=63` nonempty masks per pencil. They are support/finite-combinatorial facts, not a trial over numerical values of complex variables. Because each cell is owned by at most one variable and its scalar is nonzero, the support for a given variable mask is exactly the union of the corresponding generator supports; no cancellation between different variables can create or destroy a cell. Rectangular support is used only as a NECESSARY condition for rank1.

## 4. Derivation of the three-party 60 bound

The pencil generators are independent by §3. For a 12-entry spectator slice, §3(2) lets us use `w=0` in (1), giving support at least12 after ANY three local invertible transformations. For a 9-entry slice, §3(3) gives `w=3`, hence support at least9. At each spectator party the verified original levels have counts `(9,12,12,9,9,9)`, so summing these SIX spectator-level bounds gives

`9+12+12+9+9+9 = 60`.

The same three active-party matrices must act on all six slices; the proof remains valid because each individual lower bound holds for **every** such triple. It does NOT choose different local maps per slice. The identity maps give exactly60, so60 is the exact minimum for that restricted local orbit. A spectator monomial simply permutes/rescales the fixed slices; it cannot alter the support sum. Consequently any candidate below60 in this tensor's product-unitary orbit has all four party factors nonmonomial. ∎

## 5. Compact graph interpretation and reproducible checks

A second exact support checker established an equivalent graph structure for ALL72 pencils:

- every 12-entry pencil's bipartite row/column support graph is ONE **12-cycle**, with each of its six variables owning two vertex-disjoint edges;
- every 9-entry pencil's graph is ONE **6-cycle plus three isolated edges**; three variables own two disjoint cycle edges each, and the other three own one isolated edge each.

A rectangle with at least two rows and two columns contains a bipartite 4-cycle, absent from both structures. In a 12-cycle every nonzero variable contributes two edges with different row and column, so any nonempty variable mask meets at least two rows/columns and cannot be rectangular. In a 6-cycle-plus-three-isolated-edges graph, a rectangle cannot meet different connected components; any cycle variable contributes two vertex-disjoint edges and cannot form a rectangle inside the 6-cycle; among isolated edges, only a SINGLE edge is a rectangle. This is a shorter human-readable explanation of the exhaustive mask result, not a separate numerical optimizer.

Exact artifacts, all in this exclusive root:

| Artifact | SHA256 | Scope / observed result |
| --- | --- | --- |
| `frontier-20261028-pencil-rectangle-filter-v1.py` | `8428273905521c0aa198b4a161c1c61e0b42ea3d6b4c02c3f0819ebe95a78ee8` | Strict support parser via companion; exhausts 63 masks for every pencil. |
| `frontier-20261028-pencil-rectangle-filter-v1.json` | `5e50c55b9fca24414633554c1278a569d989cca72bc0265c4d2bec40ed46e103` | Full per-pencil masks, permitted-coordinate unions, four spectator totals60. |
| `frontier-20261028-rectangle-independent-verifier-v1.py` | `1e48a75444e1a80701288de30776870ed07d513c56c6b9d115144774e21c2cb2` | Different support parser and independent 72-pencil mask enumeration. |
| `frontier-20261028-rectangle-independent-verifier-v1.json` | `83c7a5772100e115d863769069d25dc750b40691a549b42687b734f2c58b21ff` | All72 mask lists match; deleting one support coordinate rejected with the intended mask-mismatch reason. |
| `frontier-20261028-rectangle-coverage-audit-v1.py` | `7d8a60ef838d45e3763b9d0e6bed0f97c8422ed6d3b843251aa962520f03d170` | Checks exact spectator/level/pencil universe and arithmetic aggregation. |
| `frontier-20261028-rectangle-coverage-audit-v1.json` | `04ad734545015e75f631acf3aa4bfc747e9a4817025ac57647e37c2f9cdcc539` | 24 slices/72 pencils; 24 have w=0 and48 have w=3; all144 surviving masks are singleton; duplicate-slice mutation rejected. |
| `frontier-20261028-pencil-graph-certificates-v1.py` | `16c10327049a10f05e05633cbec90dc63f34d8dd714fe0bfb985e087251ee79e` | Independent graph-structure classification and parameter-matching checks. |
| `frontier-20261028-pencil-graph-certificates-v1.json` | `9759443a2631cd739ca4fc762c6ea91c5fa44130f8e66d51126dfe1cdf312fb2` | Lists all72 graph edge/parameter certificates; deletion mutation rejected. |

Commands were `python3 -B` with the named source table, checker or candidate receipt and a new exclusive output path; all completed successfully. They used exact support sets and integers, no floating-point thresholds. The graph checker shares the dense table parser, while the independent rectangle verifier has its own support parser; this is **same-harness implementation diversity**, not independent-family or formal proof. Their deletion/duplicate controls validate selected failure paths, not completeness of every possible mutation.

The earlier independently structured dense and sparse Q(sqrt2) checkers separately verified the SAME table's normalization and all six 36×36 two-party marginals; explicit code/receipt hashes and controls are in the cited prior report. Their coefficient-vector agreement is recorded there. The source's published table remains PRIOR; no construction priority is asserted.

## 6. Remaining frontier

This bound improves the prior restricted-orbit result from “at least three parties must move” to “all four must move” and supersedes the separate weaker 44 lower bound for three moving parties. It still leaves the actual global AME minimum and ANY four-nonmonomial local move open. The next productive step is to analyze or search coordinated four-party changes on this tensor and to seek independent review of the finite support certificate and written rank lemma. No claim of failure for all four-party unitaries, all AME states, or support≤59 follows.
