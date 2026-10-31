# info-6 frontier: complete one-flat search around published seed 1

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before this file was written: **2026-10-28T18:14:45-0700 PDT**. This is a **bounded executable search result, author-owned and not disjointly reviewed**. It is not an unrestricted exclusion, a claim about all possible starting functions, or a novelty claim.

## Scope and outcome

For the first published nine-variable peak-28 seed in `frontier-20261028-published-seeds.txt`, the program enumerated every affine 4-flat A in F₂⁹ once. On each A it fixed the other 496 truth values and considered **all 65,536** assignments on A; for every such assignment it applied exact Walsh-peak inequalities and tested for a zero at every frequency. A zero would allow an affine twist into a balanced function without changing the peak. The five contiguous native chunks below report **105,911,904 flats, 106,033,251 feasible flat/assignment incidences, and zero balanceable peak≤28 incidences**. Thus this implementation finds no target after an arbitrary replacement supported inside any one affine 4-flat, followed by any affine output twist. Complementing is also harmless for the conclusion. The incidences are not distinct functions: every flat admits at least the unchanged source assignment.

In particular, any set of at most five changed positions has affine span of dimension at most four and is contained in some enumerated flat. Subject to the executable-result boundary, this excludes a target obtained from seed 1 by **any five or fewer truth-bit flips and an arbitrary affine output twist**. The implication does not assume the changed positions were selected in advance.

This is not an exclusion outside the specified one-seed, one-flat neighborhood: six affinely independent truth-bit changes do not fit in any affine 4-flat. Search arithmetic and coverage have not been independently checked in full.

## Enumeration and finite solver

Every 4-dimensional linear subspace has a unique RREF basis with pivots in increasing coordinate order and free entries to their right. For each such subspace, the 32 representatives whose four pivot coordinates are zero select its cosets uniquely. The Gaussian-binomial count is `[9 choose 4]_2 = 3,309,747` subspaces, hence 105,911,904 flats.

For A=x₀+span(v₁,…,v₄), group the 512 Walsh frequencies by their 16 restrictions to the span. The fixed outside contribution, oriented by `(−1)^{a·x₀}`, gives the exact lower and upper admissible values of the 16-point local Walsh coefficient in each group. The program intersects exact bit masks of all 65,536 local assignments satisfying those 16 simultaneous bounds. It marks a local assignment balanceable exactly when some individual global frequency has zero Walsh value. Each visited flat asserts the unchanged seed restriction is feasible. No randomly sampled or relaxed histogram is counted as an actual witness.

An independently implemented Python control checked every affine 2-flat of F₂⁵ against brute-force set enumeration (155 subspaces, 1,240 flats, no duplicates/differences). Its first 1,000 nine-variable flats independently reproduced 1,000 feasible incidences and no target. This does **not** independently replay the other 105,910,904 flats, and the full result remains subject to independent review.

## Chronologically contiguous receipts

All filenames below are in this directory. Each is 17 LF and records zero target incidences, no timeout and no stopped witness. Durations are elapsed process times, not a claim of continuous owner work.

| Receipt | Zero-based interval | Feasible incidences | SHA-256 |
|---|---:|---:|---|
| `frontier-20261028-rref-flat-seed1-chunk00.json` | [0, 10,000,000) | 10,010,824 | `5854a4591322c58a1ba9bbc56ab663e51e8a70cf130c2756746ee9ce5fcc7c57` |
| `frontier-20261028-rref-flat-seed1-chunk01.json` | [10,000,000, 40,000,000) | 30,030,952 | `8f332178d315711b63ec4c7e57c14e7fe49937bdea74398befd5a41999cb6b73` |
| `frontier-20261028-rref-flat-seed1-chunk02.json` | [40,000,000, 70,000,000) | 30,031,244 | `b90015261907bfaa45ee88b26eed68cf0d8607e94166e1a4d643df478b8d086e` |
| `frontier-20261028-rref-flat-seed1-chunk03.json` | [70,000,000, 100,000,000) | 30,043,205 | `02cf1ca5a14b6a08afa8cb2253efba12cadee9b4d066c3d15ac2f79039ed11bb` |
| `frontier-20261028-rref-flat-seed1-chunk04.json` | [100,000,000, 105,911,904) | 5,917,026 | `49b46106772838fdfd3077ad3c27892d3b5a82c2d718a738eae35d0be56fdb9d` |

The final receipt records `complete_through_end=true`. Sum of recorded process durations is 384.6902 seconds; the receipts do not establish uninterrupted elapsed wall time across chunks.

## Pinned inputs and implementation

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-published-seeds.txt` | `116ab5a7709dd35d951ddc878af227e5e05ce269d8293e5c0c269e158bd051f2` | 6 |
| `frontier-20261028-core-outer-search.cpp` | `a1cd5207f2bcaf975998250002fb735717cd88625d5a304f4ae76d02d680652e` | 295 |
| `frontier-20261028-rref-flat-search.cpp` | `dbf65f97a7266b37173bd0f04d37b1cb79b21fbe950c26d94e901378e5a460de` | 153 |
| `frontier-20261028-rref-flat-search` executable | `23ba493a6388a21be8b027f0bcbac08361a8ecc865587e594bfc8ae89c20b7f8` | — |
| `frontier-20261028-check-rref.py` | `af173e41f7ba6fac3023ba24cfe8f97ceeab206d76b839bc9b6e5fbcec97ab19` | 149 |
| `frontier-20261028-independent-rref-smoke.json` | `f6bacdc0fba564e1b8676c8473771e8814ec61f5b0500bd276730ce09e9c84ca` | 18 |
| `frontier-20261028-affine-flat-search-report-v1.md` | `c4d52a9971c5420e207ff61be71776630df58ed6dbcfedca803a5b6f50f5db13` | 57 |

The prior report accurately described only the then-complete first ten-million prefix; this additive file records the subsequently completed remaining chunks. **END.**
