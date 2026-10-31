# Independent same-harness review: maximal 1-RQLS(10) commutant trichotomy

**Disposition: 0 FATAL / 0 MAJOR / 1 MINOR. INCONCLUSIVE:** existence or impossibility of each of the three branches and of the original 100-ray object; novelty and priority. The separate 95- and 90-ray candidate bounds mentioned in the target are outside the frozen scope and were not reviewed. The stated trichotomy and the general 3D-sector count are reconstructed below for the resolution-Latin-square definition fixed by the manifest.

Native clock observed with `/bin/date` before writing this review: **2026-10-29T13:16:54-0700 PDT**. This is an observation before writing, not an asserted file-creation time.

## Frozen inputs and actual sequence

The first research artifact opened was the manifest. Its measured SHA-256 was `c9d58a44beccaf30bc4193979c6797148b85faf3abf43eefade460822850add6`, matching the assigned prefix `c9d58a44becc`. After reading the manifest and before reading either input body, I measured both complete input files by SHA-256 and `wc -cl`. All three recorded properties matched the manifest:

| Order | Input | Measured SHA-256 | Bytes | LF | Actual complete raw windows |
|---|---|---|---:|---:|---|
| 1 | `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-5-quantum-mann-k333-no-k555-exact-core-parent-v1.md` | `3d18e1fcadf5346b58b72cfb0cd18f15526514fad0bf4cf10006c3c729c022c4` | 7280 | 25 | 1–5, 6–10, 11–15, 16–20, 21–25 |
| 2 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10/frontier-20261029-maximal-1rqls10-commutant-trichotomy-v1.md` | `37b62f6eefc4b5d0e4ac57c91f9c521473b13deb0465468e24a3daad98c982bc` | 5251 | 55 | 1–10, 11–20, 21–30, 31–40, 41–55 |

Each range is a displayed `:raw:a-b` read, including each file's final line. The inputs were read completely in manifest order before mathematical reconstruction or the independent control. A mistyped attempt to open the target's final window returned `path not found`; the next attempt used the correct frozen path and displayed lines 41–55. It opened no other body and did not change the successful read sequence.

## Per-claim findings

`0F/0M/0m` below means no finding on that claim, not a claim of external verification. The one minor is counted only once.

| Claim in scope | Verdict | Reason |
|---|---|---|
| Definition and the pairwise context-intersection property used at target lines 33 and 37 | **m1; 0F/0M** | The self-contained statement lists ONBs but does not explicitly spell out that the resolution classes partition the cells into transversals: one cell in every row and column. This property is essential to the degree-six argument and the rank-two argument. The manifest fixes the intended resolution-Latin-square scope, under which the proof is valid. State the condition explicitly. |
| Nonzero-overlap components have mutually orthogonal spans, span the entire space, and yield commutant `C^k`; its orthogonal projections are unions of components | **0F/0M/0m** | Reconstructed for arbitrary complex linear operators, without assuming they are Hermitian. |
| A union of components of dimension `d` has `d` rays in each of the 30 contexts and `10d` distinct rays overall | **0F/0M/0m** | Orthogonally split each ONB and count cells by rows. |
| Sectors of dimension 1 or 2 are impossible | **0F/0M/0m** | One-dimensional uniqueness and the unique 2D orthogonal partner, respectively, contradict pairwise distinct rays. |
| In a hypothetical 3D sector there are 30 vertices, each of degree 6, and the auxiliary graph is C4-free | **0F/0M/0m** | The three contexts meet pairwise only at the given cell; a four-cycle forces two distinct rays into one common 1D complement. |
| `30 * binom(6,2) = 450 > binom(30,2) = 435`, excluding the 3D sector | **0F/0M/0m** | Every unordered endpoint pair has at most one common neighbor in a C4-free graph; the count is exact. |
| For arbitrary order `n`, a 3D sector requires `3n-1 >= 30`, hence `n >= 11` | **0F/0M/0m** | The same 3n-vertex degree-six argument applies to a maximal 1-RQLS(n) with a resolution Latin square. |
| Exact three-way classification, including 40+60 and 50+50 ray counts and `C` or `C⊕C` commutants | **0F/0M/0m** | Complements exclude dimensions 7, 8, 9; the remaining component dimensions partition 10 and are at least 4. |
| Feasibility of the irreducible, 4+6, or 5+5 branches; unrestricted 100-ray existence/no-go | **INCONCLUSIVE** | These are not decided by the trichotomy or by this review. No branch construction or exclusion is inferred. |
| Separate 95- and 90-ray quantitative candidates, novelty and priority | **OUT OF SCOPE / INCONCLUSIVE** | The linked candidate bodies were not inputs or opened; no literature or novelty search was performed. |

## Definitions and independent reconstruction

For clarity, take an order-`n` array of cells `(r,c)` with one nonzero ray in each cell, all `n²` cell rays pairwise non-parallel. Every row and every column is an ONB of `C^n`. A **resolution Latin square** `L` assigns one of `n` labels to each cell, with each label appearing exactly once in every row and in every column; its label classes are also ONBs. Thus each cell lies in exactly one row, one column and one resolution class, and any two of these three contexts meet exactly at that cell. These definitions give the intended maximal 1-resolvable scope; the conclusions do not assert that such an array exists.

### 1. Overlap components and their commutant

Normalize representatives and let `P_x = |x><x|`. Form the graph `G` whose vertices are the cell rays and whose edges mean **nonzero** inner product. If two vertices are in different components, their inner product is zero, so the component spans `H_1,...,H_k` are mutually orthogonal. A row is a basis, so their orthogonal sum is all of `C^n`.

Let a complex linear operator `X` commute with every `P_x`. Since `P_x` has rank one, commutation implies both `X P_x = lambda_x P_x` and `P_x X = lambda_x P_x`. If `<x,y> != 0`, then `P_x P_y != 0` and

`lambda_x P_x P_y = P_x X P_y = lambda_y P_x P_y`.

Hence `lambda_x=lambda_y` along an edge and therefore throughout each component. Since the component's rays span `H_j`, `X` equals a scalar on all of `H_j`. Conversely, `X = sum_j lambda_j Pi_j`, where `Pi_j` is the orthogonal projector onto `H_j`, commutes with every ray projector. Thus the full, not merely Hermitian, commutant is isomorphic to `C^k`. An orthogonal projector in it has scalar coefficients each satisfying `lambda_j²=lambda_j`, hence 0 or 1; these are exactly the projectors onto unions of components.

### 2. Sector and cell counts

Let `H` be a union of component spans and `dim H=d`. Every cell ray lies either in `H` or in `H^perp`. Project any context ONB onto `H`: the vectors belonging to `H` remain and the others vanish. They therefore form an orthonormal spanning set of `H`, so there are exactly `d` of them. This holds for each row, column, and resolution class. The `n` rows partition the cells, and distinct cells are distinct rays, so there are exactly `nd` sector rays. For `n=10` this is `10d`.

### 3. Exclusion of dimensions 1 and 2

For `d=1`, every sector ray is the same one-dimensional ray, whereas each of the ten rows contains one and different cells must be non-parallel. Contradiction.

For `d=2`, choose a sector cell `x`. Each of its three contexts contains exactly one other sector cell. All three companion rays are orthogonal to `x` in `H`, and `H ∩ x^perp` is one-dimensional; hence they are the same ray. The row, column, and resolution class through `x` meet pairwise only at `x`, so these three companion cells are distinct. This violates pairwise non-parallelness. The explicit transversal condition in m1 is what guarantees the distinctness of the companion cells.

### 4. Exclusion of dimension 3 by an independent C4 count

Now suppose `d=3` and `n=10`. There are `10*3=30` distinct sector rays. Construct a **different** graph `A` on these 30 rays: connect two vertices when their cells share a row, column, or resolution class. These edges mean orthogonality, unlike the nonzero-overlap edges in `G`; `A` need not include all orthogonal pairs.

In each of the three contexts through a vertex there are exactly two other sector cells. The three two-element sets are disjoint by the resolution-Latin-square intersection property. Thus `A` is a simple graph, every vertex has degree `2+2+2=6`, and every edge joins orthogonal rays.

If distinct vertices `a,b,c,d` formed a four-cycle `a-b-c-d-a`, then `b` and `d` would both be orthogonal to `a` and `c`. The rays `a,c` are distinct and non-parallel, so their representatives span a two-dimensional subspace of `H`. Its orthogonal complement in the 3D space `H` is one-dimensional. Thus `b,d` would be parallel, contradicting distinctness. The cycle need not be induced: extra chords do not change this argument. Therefore `A` is C4-free.

In any simple C4-free graph, two distinct vertices have at most one common neighbor: two different common neighbors would themselves form a four-cycle with the pair. Count triples consisting of a center and an unordered pair of its distinct neighbors. The center count is

`sum_v binom(deg(v),2) = 30 * binom(6,2) = 30 * 15 = 450`.

The endpoint-pair count is at most `binom(30,2)=435`. This would require `450 <= 435`, a contradiction by 15. No graph census, solver output, or author code is used for the exclusion.

For general order `n`, the same argument has `3n` vertices, each of degree 6. Since `n>0`,

`3n * 15 <= binom(3n,2)` implies `30 <= 3n-1`, hence `n >= 11`.

This is only a necessary condition for a 3D sector, not a construction for any `n >= 11`.

### 5. Exhaustive classification at order 10

For any proper sector of dimension 7, 8 or 9, its orthogonal complement is also a union of components and has dimension 3, 2 or 1, respectively, already excluded. In particular, every individual component has dimension at least 4. Three components would require dimension at least 12, so there are at most two.

If there is one component, it spans `C^10`, and the commutant is `C I`. If there are two, their positive integer dimensions add to 10 and are each at least 4, leaving precisely `4+6` or `5+5`. The sector count gives 40 and 60 rays in the former case, or 50 and 50 in the latter, and the commutant is `C⊕C`. The alternatives are disjoint because they have different component counts or dimension multisets. This establishes necessity and exhaustiveness, not realizability.

## Independent exact controls and receipts

I wrote and ran only my own reviewer-prefixed script, `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f210-rqls10-maximal-commutant-trichotomy/reviewer-f210-exact-control.py`; no author code was run, imported, or compiled. The command was `/usr/bin/env python3 <that-script>`, with a subprocess timeout of 120 seconds. Native `/bin/date` observations immediately before and after the run were both `2026-10-29T13:16:01-0700 PDT`; the recorded script SHA-256 was `104d0b4d63291840c0ee2b2576ea94fa7e717577f3552d5b1effdf0173d690f8`; exit code was **0**, and stderr was empty. The run did not time out. Its complete stdout was:

```text
SYNTHETIC_30: vertices=30 contexts=30 context_size=3 max_context_intersection=1 degree=6
SYNTHETIC_30: wedges=450 pair_capacity=435 excess=15
NEG_30_C4_FREE: rejected_for_common_neighbors witness_indices=(0, 2, 4, 26) witness_cells=((0, 0, 0), (0, 2, 6), (1, 2, 4), (8, 0, 4))
POS_C4_FREE: PG(2,5) incidence vertices=62 degree=6 wedges=930 pair_capacity=1891 witness=none
NEG_DUPLICATED_CELL: rejected_for_duplicate_position_and_context_intersection distinct=29 max_intersection=2
NEG_MISSING_EDGE: rejected_for_degree vertices=(0, 1) degrees=(5, 5)
GEOMETRY: all_four_C4_orthogonalities_hold_implies_sample_parallel
NEG_NONPARALLEL_VECTOR: rejected_for_broken_c_d_orthogonality dot=1
CONTROL_COMPLETED
```

The synthetic 30-cell incidence uses triples `(r, r+t mod 10, r+3t mod 10)` for `r=0,...,9`, `t=0,1,2`. It verifies the local context/degree and counting arithmetic and explicitly finds a four-cycle. Its extension to a complete Latin square or realization by rays is **not** claimed. The C4-free positive control is a separately generated finite-field projective incidence graph: normalized nonzero triples over `F_5`, with point/line incidence determined by zero dot product. The duplicate-position and missing-edge controls are rejected for the intended intersection and degree reasons, respectively. The vector control uses `a=e1`, `c=e2`, `b=e3`, `d=2e3`: all four cycle orthogonalities hold but `b,d` are parallel; replacing `d` by `(0,1,2)` makes it nonparallel and deliberately breaks the `c-d` orthogonality. These examples do not replace the general written proof.

## Imports, gaps, and deviations

**Imports:** The definition and scope in the manifest, including a resolution Latin square and pairwise non-parallel cell rays, plus elementary finite-dimensional complex linear algebra and counting, explicitly reconstructed above. I did not need to import any theorem, finite object, census, or commutant result from the adopted context; reading that context does not grant linked bodies as premises. Author PASS/receipts, searches, solver outcomes, literature, external models, sibling reviews, held material, and author contact were not used as evidence.

**Remaining gap:** The proof neither produces nor rules out a maximal 1-RQLS(10), nor settles the existence of any of its three possible structural branches. It does not decide the separate quantitative candidates or novelty/priority. The definition clarification m1 remains to be made in the author-facing statement.

**Contract deviations:** No substantive deviation. The unsuccessful mistyped final-window read and its immediate correction are disclosed in the sequence above. No input, Git state, infrastructure, or non-review-wave file was edited; no build, lint, formatter, or unrelated test was run.

This is a **same-harness** scientific review; it is **not** human review, independent-model-family review, formal/kernel verification, or novelty verification.
