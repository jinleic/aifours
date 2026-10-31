# Finite review: BH(10,5) half-frame obstruction

Native `/bin/date` observation before preparing this report: **2026-10-28T21:01:21-0700 PDT**.

## Disposition and limits

**FATAL 0; MAJOR 0; MINOR 0 in the assigned BH(10,5) finite replay, normalization, inclusion, and physical-caller scope.** The finite verification is **complete** for the normalized half-frame superset described below. Every eligible triangle is represented exactly once by the pinned certificate; every supplied witness was checked against its independently regenerated graph; an independently written exact matching recurrence also rejected every eligible graph.

Together with the separate handwritten reduction below, this supports the no-transversal conclusion for Fourier10 products of BH(10,5) matrices and their stated phase-equivalent versions. The finite result by itself is not that conclusion: it depends on the normalization, necessary-extension inclusion, and physical opposite-row argument below. **This review does not establish or assess the all-odd-q theorem, resolve general QLS10, establish priority or novelty, classify BH matrices, or give a formal-kernel proof.** It is a same-harness scientific review, not a human review or an independent-model-family review. The prior same-harness review was a declared, read input, so this review is not blinded to that review's written findings. No author or prior-review code was read, imported, or executed.

## Frozen inputs and source identity

Manifest `manifest-v1.json`: 3,897 bytes, 57 LF, SHA-256 `18c99ee567c62fce537563f4fde06bebb1308b4549e5417191bfcecf7d331d02`. Its five declared inputs were read completely **in the declared order**, each full SHA-256/byte/LF triple verified before interpretation. The 612,365-byte certificate was UTF-8 decoded and parsed in full with duplicate object keys and non-JSON constants rejected; every record was subsequently validated. The following paths are absolute.

| Order | Input | Bytes | LF | SHA-256 |
|---:|---|---:|---:|---|
| 1 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10/frontier-20261028-all-odd-fourier-product-no-transversal-v1.md` | 6,254 | 54 | `d9422ffac608ddd9b128e979dc105b20c6ca94ad06f4a63af4e086a42e6e9490` |
| 2 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10/frontier-20261028-all-bh10-5-product-obstruction-v1.md` | 11,149 | 105 | `44776a4da92b9b50cc9b8710bdd7b7dc7b2119dbb7c3beebf4aa909969885678` |
| 3 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10/frontier-20261028-bh10-structural-cert-v1.json` | 612,365 | 1 | `67bc6f39a6d2bbd6a3c181dc4a7e5baaa7e5406b4ad8a50eb997b44e41197eb2` |
| 4 | `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f72-all-bh10-5-product-obstruction/review-v1.md` | 11,197 | 75 | `1fb094152763cf0785f08b80affa5c9ad24fa1ffb2c3e3940b8f6250477757e3` |
| 5 | `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f72-all-bh10-5-product-obstruction/receipt-v1.json` | 5,612 | 222 | `e131fa267ed4edf0992064dc8d493923a1e8a1d217f82a29a37d38175123a011` |

The prior review and its reported counts agree with this replay; that agreement is not a substitute for this replay. Its sample matrix was used **as data only**, then checked directly for all 45 row-pair and 45 column-pair conditions before use in controls. No historical checker execution or output is taken as evidence for the finite enumeration.

The candidate names [Lam–Leung, *On Vanishing Sums of Roots of Unity*, arXiv:math/9511209v1](https://arxiv.org/pdf/math/9511209v1). I directly fetched that named PDF: 201,910 bytes, SHA-256 `b010546db8230a39741997807a1110402c4f24fb7e897441e66fc355284ce1ab`, retained as `finite-lam-leung-math9511209v1.pdf`. I rendered and visually inspected its first page: title, authors T. Y. Lam and K. H. Leung, and arXiv identifier/version appear there. The page image `finite-lam-leung-page1.png` has SHA-256 `7c084694f5cf69016e9931185d96e0918461027deac77165a2784bc4ed3676c6`. This identity inspection is **not** a disposition of the general root-sum theorem or the odd-q reduction; the q=5 argument here needs only the elementary cyclotomic fact stated below.

## Independent construction and exhaustive certificate binding

`finite-check-v1.py` uses only the Python standard library. It starts with the sorted nine-entry multiset `0,1,1,2,2,3,3,4,4`, iterates its distinct lexicographic successors, prefixes a zero, checks strict increasing order, and therefore generates the full dephased balanced-row universe without importing producer or prior-review code. It selects rows balanced in their difference with `(0,0,1,1,2,2,3,3,4,4)`, builds all pairwise compatibility edges, and enumerates each unordered triangle once. Candidate indices are fixed by the resulting lexicographic row order.

| Object, exhaustively regenerated | Result |
|---|---:|
| Balanced tails before the second-row filter | 22,680 |
| Candidate rows | 1,075 |
| Candidate-compatibility edges | 26,715 |
| Unordered triangles | 53,065 |
| Triangles with at least five common candidate neighbors | 16,064 |
| Certificate records bound to that exact eligible set, no duplicate or omitted triple | 16,064 |
| Fresh half-graphs checked by the separate matching recurrence | 16,064, all without a perfect matching |

The sorted candidate rows have canonical-JSON SHA-256 `34460b30195aa50be87a23739213595fd9a6edfeeab734177997af3a63673053`; the sorted eligible triples have canonical-JSON SHA-256 `796d4b4530a1c72685d3a2b7183b29861227d0288af71733581d5594aa774aee`. The complete certificate schema is checked: exact top-level and per-record keys, integral strictly increasing in-range triple indices (booleans rejected), eligibility, uniqueness, and set equality. No unrecognized field, duplicate JSON object key, extra triple, or absent eligible triple is accepted.

For each triple `(i,j,k)`, I reconstructed the five-row frame `[0, second, row_i, row_j, row_k]` and independently rebuilt its ten-column graph from all 45 pairs: an edge occurs exactly when the five coordinate differences represent all five residues. For the supplied witnesses:

* 16,000 isolated-vertex records were verified directly. Among all eligible graphs, 12,800 have exactly one isolate, 3,200 have exactly two, and 64 have none.
* Each of the remaining 64 records supplies a proper nonempty odd set of five vertices. Every crossing edge from that set to its complement was checked to be absent. An odd set with no crossing edge cannot be perfectly matched, regardless of whether the set is internally connected.

Separately, the checker computes an exact subset recurrence on each freshly built graph: choose the least vertex `u` in a remaining even set `S` and recurse over every neighbor `v` in `S` on `S \\ {u,v}`, with the empty set successful. All 16,064 return no perfect matching. This is a second no-matching check on the same independently reconstructed graphs, not a second independently authored graph generator or a separate model-family review.

## Mathematical caller, normalization, and inclusion

Let `omega` be a primitive fifth root. For a sum of five or ten fifth roots, the polynomial of residue multiplicities has degree at most four. Since the minimal polynomial of `omega` is `1+X+X^2+X^3+X^4`, the sum vanishes exactly when its five multiplicities are equal: all one for five terms, all two for ten. This supplies both the half-graph edge predicate and the full-row compatibility predicate with no numerical tolerance.

First remove any arbitrary unit-modulus row and column phases used to obtain a fifth-root matrix. A K-row phase is a common diagonal unitary on all physical vectors; a K-column phase is a cell phase for that physical column. Both preserve orthogonality and transversals. Common unitaries, cell phases, and relabeling of physical rows or columns also preserve the property. Write the resulting K entries as `omega^a[t,c]`.

Choose any five K-coordinate rows `E`, two distinct members `p,q` of `E`, and any pivot column `c0`. Define

`b[t,c] = a[t,c] - a[t,c0] - a[p,c] + a[p,c0] (mod 5)`.

Then row `p` and column `c0` are zero. Since K has orthogonal rows, `q` contains each residue twice; with `c0` first, permuting the other columns brings it to `second=(0,0,1,1,2,2,3,3,4,4)`. For any pair of columns, this dephasing shifts all five differences by the same column-pair-dependent residue, so it preserves balanced half-sums; the column permutation merely relabels the half-graph. Rearranging rows within `E` is a relabeling used for this graph computation, not a claim that an arbitrary coordinate permutation fixes the original Fourier formula.

Every other dephased K row starts with zero and is balanced relative to both the zero row and `second`, so it is in the 1,075-row list. The three other rows of `E` are distinct and pairwise compatible, hence form one enumerated triangle. The five actual rows outside `E` are five further **distinct** candidate rows, each compatible with all three of those vertices, and hence are five common candidate neighbors. They are necessarily also mutually compatible, but the finite filter does not require that: every extendible frame lies in the larger checked set with at least five common neighbors. In particular, the calculation does not assume a classification or that all retained frames extend to a full BH matrix. The direct checks above show that none of those retained frames has a half-graph perfect matching. Therefore no BH(10,5) matrix has a perfect matching in its half-graph for any five-row set `E`.

For the physical caller, put `psi_(r,c)(t)=zeta10^(rt) K[t,c]/sqrt(10)` and take any hypothetical orthogonal transversal. Its ten distinct physical row labels contain five opposite pairs `(r,r+5)`; because its ten physical column labels are distinct, these give five disjoint pairs of K columns. For one such pair `c,d`, let `S_E` and `S_O` be the sums of `conjugate(K[t,c]) K[t,d]` over even and odd coordinates. K-column orthogonality gives `S_E+S_O=0`. The physical inner product of the opposite-row cells gives `S_E-S_O=0` because `zeta10^(5t)=(-1)^t`. Thus `S_E=0`, and the column pair is an edge in the half-graph. All five pairs would form a perfect matching, contradicting the preceding result. This argument does not assume that the 100 rays are globally distinct; it only assumes the hypothetical transversal is orthogonal. A matching is necessary, not asserted sufficient.

## Actual positive, negative, and normalization controls

* The matching positive is the five-row frame `0000000000 / 0121230434 / 0242410313 / 0313140242 / 0434320121`. All ten row pairs are balanced; exact matching returns `(0,1),(2,3),(4,5),(6,7),(8,9)`. Its normalized candidate triple is `(0,25,50)` with **zero** common candidate neighbors and five doubled half-column signatures. It demonstrates a real matching outside the five-outside-row filter, not a full BH completion or a transversal.
* Four full altered-certificate fixtures were retained, re-parsed, and replayed through the checker. Each was rejected for its intended reason: one removed record → `missing_triangles`; duplicated record → `duplicate_triple`; changing the actual isolated column of `(57,208,429)` from 1 to nonisolated 0 → `isolate_not_isolated`; changing the five-set of `(75,163,634)` from `[0,3,4,6,8]` to crossing set `[1,3,4,6,8]` → `odd_cut_crosses`. Their full-file hashes appear below. Additional in-memory tests rejected a boolean triple index, an extra record field, a duplicate JSON key, and an even cut for their respective intended reasons. The receipt records exact reasons and mutation hashes; arbitrary exceptions do not count as passes.
* In one directly revalidated BH(10,5) sample from the frozen prior receipt, all 252 five-row halves and all 50,400 choices of ordered first/second rows and pivot column were normalized. In every case the five actual outside rows were distinct common neighbors, the normalized graph was the column-relabelled original graph, and a deterministic fifth-root row/column gauge produced the same dephasing. This is **one K and one gauge pattern**, not a substitute for the universal algebra above.
* For that same sample, 11,340 half/column-pair cases checked the sign distinction exactly via fifth-root coefficient counts. In particular, for `E=(0,1,2,3,4)` and columns `(0,1)`, the plus counts are `[2,2,2,2,2]` (zero) whereas minus counts are `[2,-2,-2,0,2]` (nonzero). This rejects replacing the required physical minus by the automatically vanishing column-orthogonality plus.

## Commands, clocks, and retained hashes

All paths in this section are relative to this review directory. Both commands used `/opt/homebrew/opt/python@3.14/bin/python3.14 -B`, standard-library code, and `stdin=DEVNULL`. The exact command, clock observations, stdout/stderr, elapsed time, observed process exit, and hashes are retained in the two run-attempt receipts.

| Run | Actual command | Observed start → process return | Exit |
|---|---|---|---:|
| Complete replay | `python3.14 -B finite-check-v1.py` | 2026-10-28T20:59:17-0700 PDT → 2026-10-28T20:59:21-0700 PDT; 3.418 s monotonic | 0 |
| Materialize/replay retained controls | `python3.14 -B finite-fixture-check-v1.py` | 2026-10-28T21:00:44-0700 PDT → 2026-10-28T21:00:45-0700 PDT; 0.751 s monotonic | 0 |

The fixture script verifies the SHA of **this review's own checker** before importing that checker; it does not import author or prior-review code. It persists four full mutated JSON files and checks their rejection from the persisted bytes. The substantive original finite replay does not import any checker.

| Retained artifact | Bytes | SHA-256 |
|---|---:|---|
| `finite-check-v1.py` | 22,027 | `35a89a1504832fee220c56a09af5e64fe28d1152b49c44d00529d92633e12ca1` |
| `finite-receipt-v1.json` | 7,877 | `6b62ebed978c649785f215ac7cb20472c2b38176463edf59e026ec7ebc4e49c7` |
| `finite-run-attempt-1.json` | 1,090 | `0135f9bfee2b7688a27b09416a14eb76a546715eb82c93b83e9e464c97f1c250` |
| `finite-fixture-check-v1.py` | 6,160 | `ad9107c8a003c89882f0eb6797bb98e1b0ff3d4d248611833360e851158f7d14` |
| `finite-fixture-receipt-v1.json` | 5,478 | `6c254543703c869c30c38003468458d7ed92db4ce03d6d2c0da26b7c3502c98b` |
| `finite-fixture-run-attempt-1.json` | 1,116 | `bb4b5f526b0a7a5d0715edf347176967f67076be11cd0eb32dee25e706ce6df6` |
| `finite-fixture-removed-v1.json` | 612,326 | `5d31bd35b6ea60d6ddd03900d8ebc914691a01dc1d12844bebd8520827a94939` |
| `finite-fixture-duplicated-v1.json` | 612,401 | `81ff69b8035911f2c189ce3ab5271422106094dc4f687eb301704de0d366c065` |
| `finite-fixture-wrong-isolate-v1.json` | 612,364 | `64917f70b0c9d99b21236ee6bc306e676818326241c0bf5610a6bf6f45edbfd0` |
| `finite-fixture-wrong-cut-v1.json` | 612,364 | `4a5998e6e97a8fd5e1d74c5958b531b82681885c606d072b723a11394eebd0de` |

The successful checks are exact finite computations plus the written argument above. They are not a claim of independent human or cross-family verification, kernel checking, odd-q theorem acceptance, or resolution of arbitrary QLS10.
