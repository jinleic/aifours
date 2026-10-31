# Exact optimum of the publisher's full three-branch copy LP

**Status: WRITTEN with separately checked exact rational primal and publisher dual.** The precise LP below has optimum `1847/276`, even after adding every stated disjoint original-variable `F_n` substitution for all positive integers `n`. This is an exact no-improvement result for that LP and those cuts, **not** an entropic realization, a new upper bound on guessing number, or a claim that additional copy structures or omitted cross-branch constraints cannot improve the bound. No proof-assistant, cross-model or novelty review was performed.

## Exact LP scope

Use the original R-minus graph, the normalization `h(v)<=1`, its ten graph FD equalities, and the eight-element original-variable automorphism group as recorded in `frontier-20261028-gurpinar-certificate-audit-v1.md` (SHA-256 `d0b494122660394b46d8ce647ed17e2f890c1f3ccf393cd4e44ccc48e87dcaf6`). Original variables `a,...,j` correspond to vertices `1,...,10`.

The publisher's Theorem 5.2 writes the full elemental Shannon inequalities separately on the following three variable sets, with a shared original entropy profile and the indicated copy equalities:

1. `a,b,c,d,e,f,g,h,i,j,b'0`: `b'0` copies `b` over `a,d,e,f,g,h,i,j`.
2. `a,b,c,d,e,f,g,h,i,j,d'1,e'1,g'2`: `(d'1,e'1)` copies `(d,e)` over `a,b,c,f,g,h,i`; then `g'2` copies `g` over `a,b,c,d,e'1,f,h,i`, independently of the rest of the previous branch given that conditioning set.
3. `a,b,c,d,e,f,g,h,i,j,f'3,g'3,h'4`: `(f'3,g'3)` copies `(f,g)` over `a,b,c,d,e,h,i,j`; then `h'4` copies `h` over `a,b,c,d,e,f,f'3,i,j`, independently of the rest of the previous branch given that conditioning set.

Each joint copy matches all required subset entropies with every subset of its conditioning set and satisfies its conditional-independence equality. The LP contains the **union** of nonempty entropy subsets of the three sets, hence `16,383` distinct coordinates. The sets overlap only on the 1,023 nonempty original-variable subsets. The pinned publisher text explicitly specifies these `11,13,13`-variable elemental sets in Theorem 5.2, and Remark 3.8 says that cross-branch Shannon inequalities such as one involving both `b'0` and `d'1` were not included. This result does not assert feasibility of a 17-variable polymatroid with every omitted cross-branch elemental inequality.

## Matching exact primal and dual

The common **original-variable** profile is the 1,023-coordinate base projection of `frontier-20261028-separator-bound-primal.json`, SHA-256 `aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651`. Its objective is `h(a,...,j)=1847/276`, all ten singleton values equal 1, and hence its entropy-balance expression is `h(V)-(2/3)sum_v h(v)=7/276`.

Three separately constructed exact rational auxiliary extensions of that same base profile are pinned:

| Branch | Exact auxiliary values | SHA-256 |
|---:|---|---|
| 1 | `frontier-20261028-affine-exact-branch-1.json` | `1898339bb4ba63c53dbda6dff9603f82414f29645543631bc21d82d752941e37` |
| 2 | `frontier-20261028-affine-exact-branch-2.json` | `09981982317f1659a9a291dbbc416f77d2ac8a91eac818191048cb0ac9cd7a87` |
| 3 | `frontier-20261028-affine-exact-branch-3.json` | `fd53af75dfa47e9eb03af60fb9704d89719ba8720ddf6aeb192533bcb44c4cd0` |

An independent exact integer/Fraction checker for each branch rebuilds the graph and automorphisms, all original caps and FDs, every elemental Shannon inequality on the whole branch, every subset copy equality and conditional-independence copy equality, and every applicable publisher source row. The counts are:

| Branch | Elemental Shannon | Copy equalities | Publisher rows checked tight |
|---:|---:|---:|---:|
| 1 | 28,171 | 257 | 623 |
| 2 | 159,757 | 642 | 933 |
| 3 | 159,757 | 1,282 | 1,372 |
| **Total** | **347,685** | **2,181** | Rows may repeat across branches |

The independent combined checker merges the three verified auxiliary assignments only through the identical original profile, checks that every one of the `1,920` publisher dual rows lies wholly in at least one of those branch sets, and verifies every such row is exactly tight. It revalidates the source dual: its nonzero signed multipliers combine the valid rows to `h(V)` and the caps to `1847/276`. Thus the primal gives the lower inequality and the publisher dual gives the matching upper inequality. The published three-branch LP optimum is exactly `1847/276`.

**Crucial coordinate boundary.** The base-profile file also contains older partial auxiliary coordinates. They are **not** held fixed in this primal: only its 1,023 original-variable values are imported. Comparing the new branch values with old shared auxiliary coordinates gives `4/302`, `243/1070`, and `460/2002` differences in branches 1,2,3 respectively. In particular this is not claimed to extend the old complete 4,397-coordinate partial assignment. The earlier saved-point nonextension corrections remain valid for their own specified profiles.

## Adding the all-order original-variable family

For pairwise disjoint blocks `A,B,C,D,Z` of the original ten variables, with `A,B,C,D` nonempty and `Z` possibly empty, define

\[
a=I(A;B\mid C,Z),\quad
\delta=I(A;B\mid Z)-I(A;B\mid D,Z)-I(C;D\mid Z),\quad
d=I(A;C\mid B,Z)+I(B;C\mid A,Z).
\]

The universally valid all-positive-integer copy family is

\[
F_n=(n+1)a-n\delta+\frac{n(n+1)}2d\ge0\qquad(n\ge1),
\]

with its written proof and named imports in `frontier-20261028-all-order-copy-obstruction-v1.md` (SHA-256 `76d83e14a011baaa2de3a17d8f6d8a28474094bf8a8a4bd5829f14bb5c40230b`). The separately pinned original-profile checker examined all `13,729,980` disjoint substitutions modulo `A/B` exchange and proved the inequality for every positive integer `n` by exact integer quadratic-minimum checks. These `F_n` use original variables only, so the verified branch extensions retain them. Consequently **even this infinite family of added constraints leaves the published LP optimum exactly `1847/276`**. This does not cover overlapping block substitutions, other information inequalities, new copy protocols, or mixed cross-branch Shannon rows.

## Reproducibility and provenance

* Publisher source/certificate: exact original ZIP/PDF/TXT extraction and `1,920`-row signed dual are pinned and independently parsed in `frontier-20261028-gurpinar-certificate-audit-v1.md`. The upper proof remains the already-published result, not a new bound.
* Primal producer: floating IPM supplied proposals on the source-optimal face, followed by exact affine-equality reconstruction; the float status is **not** evidence of feasibility. The shared rational projection helper `frontier-20261028-exact-affine-reconstruction.py` has SHA-256 `3fd72a62776a49b105bd6fad29f5d56158950a1c356fd49d5750c7d477b53c97`.
* Separate branch-1 verifier `frontier-20261028-branch1-exact-independent-check.py` SHA-256 `ad8428be36fadc3b7338136fb0782b81a62cacf0e74a43add708c918225d8145`; receipt SHA-256 `a6c8e46fb679a8638d31cb6d76b6ef091aca89c5147bf84ee77fe5893261204e`. It rejected four intended mutations.
* Separate branch-2/3 verifier `frontier-20261028-branch23-exact-independent-check.py` SHA-256 `dbed7ff9de6cd8c3693b0086509540eb06df3cc60c21f7e5549cbc4cfa4be78e`; receipt SHA-256 `24632017c2defe3aea5debb8f4a1b8541bbe38a87804ce3e1d708bed31373ea2`. It rejected five intended mutations in each branch.
* Combined source/primal checker `frontier-20261028-full-source-exact-combined-check.py` SHA-256 `ce96cd7148526942125c01875a749c6b6bf93e863f7ad8e4a851022a29aeaf3d`; receipt SHA-256 `4ebec6e24ed8a33f4ded8e558b678fab89ebd9ae911ebd8cd66269fa0b572b8c`. It binds all input hashes and branch receipts, checks all publisher rows tight, source-dual identity and row coverage, and rejects an original-joint and one auxiliary mutation per branch.
* All-order base checker `frontier-20261028-separator-primal-independent.py` SHA-256 `92627e854b17b4971a430eac14d8c13fbd05988a28025e592e12b183feb62b68`, using `frontier-20261028-all-order-primal-independent.py` SHA-256 `d4268fd6db3b4573462f04b19253b345d94e81295405a7acf7d1e3f68976210a`; receipt SHA-256 `dac76b954fbd166eac73ce461d2bca641420991ebceb721093f49db6df54284d`.

All verifier evidence is internal to this harness; the earlier publisher extraction and the written `F_n` proof still have the review boundaries noted in their packets. The positive balance gap belongs to an LP point, not to an actual probability distribution. The original guessing-number interval and all genuinely new copy-structure opportunities remain open.
