# Finite review: AME maximal-coefficient forbidden matchings

Review-write clock observed immediately before creation: `2026-10-28T19:29:41-0700 PDT`. This is not an exact file-completion time.

## Verdict and scope

**Finite-scope PASS; no FATAL, MAJOR or MINOR finding in the enumerated matching/cube assertions or the sampled P-only diagnostic.** This is a separately authored same-harness computational review, not a human review, independent-model-family review, formal/kernel verification, or novelty assessment. The all-state `t ≤ 29` theorem is **not established by this enumeration** and is out of scope for this finite verdict. In particular, no conclusion about attained minimum support, existence at 29, or an automatic ≥45/≥46 bound is asserted. The `t ≤ 30`/residual-incidence argument and no-OLS(6) are named premises, not re-proved here.

The exact finite object checked is a four-vertex graph on coordinates A,B,C,D with a forbidden perfect matching on each 3-symbol coordinate pair. Relabel B,C,D independently so that AB, AC and AD are identity; this leaves all `6³ = 216` ordered triples of BC, BD, CD permutations. The relabeling is a bijection and entails no symmetry assumption on the E support. The checker tests all `3⁴ = 81` possible tuples for each triple against all six forbidden pair sets. It records every surviving tuple per triple in the receipt. The 216 normalized cases represent all `6⁶ = 46,656` labelled six-matching choices, but no complex AME tensors are enumerated.

## Exact enumeration

There were **216 triples**, **648 A-fibers**, **17,496** all-tuple/triple visits, **5,184** candidate visits after the three A-matching constraints, and **1,536** surviving tuple/triple visits. Repeated tuples in different triples are counted separately. The exact histograms are:

| Surviving tuples per complete triple | 0 | 4 | 6 | 7 | 8 | 10 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Number of triples | 1 | 18 | 98 | 18 | 36 | 39 | 6 |

| Surviving tuples per A-fiber | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Number of fibers | 12 | 72 | 324 | 144 | 96 |

Maximum four per fiber and 12 in total agree with the author receipt. The complete ordered-fiber-vector histogram and each individual triple's tuple list are in `finite-counts-v2.json`, not inferred from a maximum alone.

There are six triples with exactly 12 survivors, each with fiber sizes `(4,4,4)`. In every one, all six pair-projection sizes are six, but **four** of the six projections have extension-multiplicity histogram `{1: 3, 3: 3}` and only two have `{2: 6}`. Thus none of these six 12-tuple supports satisfies the separate residual condition that each of the six projections has exactly two extensions per projected value. Since 12 is the maximum matching-avoiding set size, no 12-tuple subset has that degree property in this finite matching model. This is an additional finite control, not a replacement for the general AME-to-model argument.

## Cube-edge and weakened-constraint controls

The cube has 8 vertices and 12 edges. Exhausting all `C(12,3) = 220` distinct edge triples gives union-size histogram `{4: 56, 5: 120, 6: 44}`. The 64 triples with one edge parallel to each axis have histogram `{4: 32, 5: 24, 6: 8}`. Exactly eight triples have all three edge pairs intersecting; all eight share a vertex, and none forms a triangle. Thus the minimum union is four. Equivalently, three distinct simple edges contained in three vertices would form a triangle, impossible in the bipartite cube.

The matching enumeration also checked the actual cube bad sets in all 648 fibers: a leaf matching fixing the A symbol excludes four cube vertices; a matching not fixing it excludes exactly two vertices forming an edge, with the bad-set complement equal to the directly enumerated survivors. Zero bad-set construction errors occurred. The histogram for the number of interleaf matchings fixing the fiber's A symbol is `{0: 192, 1: 288, 2: 144, 3: 24}`.

Dropping each of the **six** pair constraints separately changes the maximum from 12 to **15**. For every omitted pair the total histogram is `{6: 6, 8: 36, 9: 24, 10: 36, 12: 102, 15: 12}`. If the omitted pair is incident to A, the fiber histogram is `{2: 108, 3: 144, 4: 324, 5: 72}`; if it is a leaf pair, it is `{2: 72, 3: 288, 4: 144, 5: 144}`. As a concrete positive weakened control, omit CD and use BC=BD=`(1,2,0)` and CD=`(0,1,2)` (the latter is ignored). There are 15 admitted tuples, five in each A fiber; `(0,1,1,1)` is one such tuple, admitted only because its CD constraint was dropped. All six maximal examples and their full admitted tuple lists are in the receipt.

## P-only diagnostic

The exact bound source JSON was parseable. Independent parsing found 30 distinct records, active-count histogram `{1: 12, 2: 18}`, valid active metadata, 30 distinct projected P pairs on each of the six coordinate pairs, and two-regular six-element residual pair complements. Each coordinate symbol 0,1,2 occurs four times and 3,4,5 occurs six times. The occupied active-active P pairs are exactly the identity matching on **each** pair, and the six supplied direct-pair summaries match the reconstructed records.

The checker directly tested **all 1,296 tuples in `0..5` to the fourth power** for avoidance of the P pair projections. Counts after AB, AC, AD, BC, BD, CD respectively are `216, 72, 24, 12, 6, 0`; a separately expressed all-pairs test gives the same empty final set. Hence this **specific** P code has **zero compatible E tuples**, not just zero compatible tuples within a purported AME support. Dropping any one P-pair compatibility constraint gives exactly six surviving tuples, listed in the receipt. Conceptually, all six occupied active-active matchings are identity, so a compatible active tuple would require four mutually distinct symbols from a three-symbol alphabet.

Five targeted mutations were rejected for the intended reasons: removed word → `word_count`; duplicated word → `duplicate_word`; out-of-range coordinate → `invalid_coordinate`; inconsistent active metadata → `active_metadata`; same-class coordinate change causing a pair collision → `pair_collision`. The receipt binds the canonical mutated-record hashes. The input is a P-code necessary-condition diagnostic only; the `sat` field is source metadata, not an independently rerun solver verdict. With no compatible E and no amplitudes, it is **not an AME witness** and says nothing about every other 30-word P code.

## Source binding, execution and provenance

The manifest was read first and its complete SHA-256 matched `13e3696bd685bd9ee36ed655a53591706a409dfb77e764e85cf04a1024af139b`. All seven declared inputs were hash-, byte- and LF-checked in order and their mathematical bodies read completely in that order; the source directory is `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/`:

| Basename | SHA-256 | Bytes / LF |
|---|---|---:|
| `frontier-20261028-global-ame46-lower42-review-packet-v2.md` | `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf` | 11168 / 107 |
| `frontier-20261028-global-ame46-maximal-coefficients29-v1.md` | `2520967103592e125423a5a22c0ed5e86236582f149fb9375cb0c6f2070b476c` | 7902 / 54 |
| `frontier-20261028-signed-k4-matching-bound-v1.py` | `2e54209c76a277818a702c6c51049119b221d0c666dbfbce1a5b4e7da8ef67b5` | 2286 / 42 |
| `frontier-20261028-signed-k4-matching-bound-v1.json` | `a81641c7129f790aef937efb2c914d08f0590b31c693dadfabdde000d6dda65a` | 699 / 46 |
| `frontier-20261028-n6-maximal-code-z3-v1.json` | `516cba122e2a7fbd252ccf06267e66410ab8e393089e0fe91c4d8b0f5690c083` | 5547 / 460 |
| `frontier-20261028-n6-maximal-code-independent-v1.py` | `b3d3d4e1b422f038edcfc6a9b3a9cae07c962ffa623a364b9f3053860a4937ec` | 3424 / 71 |
| `frontier-20261028-n6-maximal-code-independent-v1.json` | `9c71a81344dc094491cb082b8ba375c626ec76a7010266fac414149f4549a421` | 2657 / 195 |

The reviewer's standard-library program was independently written; it did **not** import or execute the author's code. From this review directory the actual command was:

```text
python3 -B finite-enumeration-v2.py finite-counts-v2.json
```

The observed run began `2026-10-28T19:29:08-0700 PDT`, the last clock before writing the receipt was `2026-10-28T19:29:09-0700 PDT`, and a subsequent clock was `2026-10-28T19:29:12-0700 PDT`. The process returned success and printed these hashes:

- `finite-enumeration-v2.py`: `4d4affe1c9f7219fc675737ae1f13f341164e2f3749895f4591b157ad6d03e17`.
- `finite-counts-v2.json`: `122ad92ed595d2c0dfb8930dcd3f23c1cc5d984fa891e71e32533d853b70d6fd`.

**Preserved correction history.** The first independently written run, `finite-enumeration-v1.py` / `finite-counts-v1.json`, started `19:28:31` and observed `19:28:32 PDT` before writing. It computed the same matching histograms, cube histogram and empty compatible-E set, but mistakenly compared tuple-valued calculated matchings with list-valued JSON metadata, reporting false for the identity and metadata-equality flags. That was a reviewer-checker representation bug, not an author finding. V2 explicitly converts each calculated pair to a list before those comparisons; its actual run reports all six comparisons and the identity flag true. V1 is retained without alteration: script SHA-256 `fd217040a02451d903bdad3d9ceeab9e8573853d41dc75cac291bb253e26d79f`; receipt SHA-256 `447dba174c60ef35bb033e4dcc2a0da7e565ab3f54ac59c04c0c7fd365183e39`. V2 is the disposition-bearing receipt.
