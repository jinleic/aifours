# info-6 frontier: exact local search on sampled and canonical affine four-flats

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T18:05:51-0700 PDT**. This is a bounded search for an actual balanced nine-variable NL≥242 function. **No witness was found in the reported draws or prefix.** Neither result is an unrestricted nonexistence proof, a claim that all affine flats have been searched, a confidence estimate, novelty or formal/kernel acceptance.

## Exact operation on each drawn flat

For a fixed actual 512-bit source f and an affine 4-flat A=x₀+U, the program keeps all 496 outside bits fixed and considers **every one of the 2¹⁶ local truth assignments**. In each of the 16 restricted-character classes it computes exact outside Walsh minima/maxima, then intersects precomputed 65,536-bit masks of all local truth vectors satisfying the full peak≤28 inequalities. It separately identifies every local vector with a zero at any of the 512 global frequencies; such a zero would give an actual balanced candidate by affine twisting. The original local restriction is checked as a positive control on every draw. Counts below are **draw/assignment incidences**, not counts of distinct functions.

## Six bounded deterministic pseudorandom samples

The native SplitMix64 program drew 1,000,000 ordered-basis/origin representations per row, with replacement. The three published inputs and their source/bit convention are in `frontier-20261028-two-flip-report.md` SHA-256 `375d9034c03b6b469878a4cd74435dc37e8a6f7ba450ff12d71ee0853d04314d`, 74 LF. The first three seed-1 core-family inputs are from a separately generated 448-table family: each member's complete spectrum was independently recomputed and confirmed zero-free with peak 28. **Only three of the 448** were used in this sample.

| Input | RNG seed | Flat draws | Feasible draw/local-assignment incidences | Draws with a balanceable peak≤28 local table |
|---|---:|---:|---:|---:|
| Published seed 1 | 20261028 | 1,000,000 | 1,001,064 | 0 |
| Published seed 2 | 20261029 | 1,000,000 | 1,001,129 | 0 |
| Published seed 3 | 20261030 | 1,000,000 | 1,001,120 | 0 |
| Core-family index 1 | 20261101 | 1,000,000 | 1,001,130 | 0 |
| Core-family index 2 | 20261102 | 1,000,000 | 1,001,093 | 0 |
| Core-family index 3 | 20261103 | 1,000,000 | 1,001,135 | 0 |

Each draw has at least the unchanged source assignment, so the feasible counts mostly repeat that same source; they are not a six-million-function construction. Draws can repeat, and no IID, uniformity or global prevalence claim is made. Each row completed its stated bound without timeout; native reported time was approximately 3.76–3.84 s per row. The first 10,000 draws of the first published-seed sequence were independently replayed: direct 512×512 character sums and a Python local-mask implementation reproduced 10,013 feasible incidences and zero targets; a corrupted expected summary was rejected for its intended mismatch. The remaining draws are not independently replayed.

## Canonical no-duplicate enumeration: completed prefix only

The RREF enumerator generates every 4-dimensional linear subspace of F₂⁹ once, with one canonical representative for each of its 32 cosets. There are exactly 3,309,747 subspaces and **105,911,904** affine four-flats. For seed 1 the first zero-based indices `[0,10,000,000)` were exhaustively searched by the exact local solver: 10,000,000 flats, 10,010,824 feasible flat/local incidences, and **0** balanceable peak≤28 local tables. The receipt explicitly records `complete_through_end=false`, `next_index=10000000`; the other 95,911,904 flats are not covered by that receipt.

The count follows from the Gaussian binomial coefficient; the algorithm's RREF basis has one pivot per row, zeroes in the other pivot columns and free entries only to the right of each pivot. Coset representatives have all pivot coordinates zero, so each flat is generated once. An independent Python control compared **all** RREF affine 2-flats of F₂⁵ with brute force: 155 subspaces, 1,240 affine flats, zero duplicates or set differences. Its independently replayed first 1,000 nine-variable flats exactly matched the native result: 1,000 feasible incidences, zero targets. It does not independently replay the full ten-million prefix. A later chunk may be in progress; no result from it is implied here.

## Pinned evidence

All paths are in this exclusive `balanced-nl242` root; filename prefix `frontier-20261028-` is omitted. SHA-256 values were taken from actual bytes.

| Artifact | SHA-256 | LF |
|---|---|---:|
| `random-flat-search.cpp` | `5304421be5ede6fa223b6bdd28fa8b5071aeb9f64cbec74da15831f5b934aebb` | 130 |
| `random-flat-search` executable | `6967246dc31767739c02e8872016891dc4af84c6aef1d512bacb6cebcfbecb4f` | — |
| `random-flat-seed1-b.json` | `0793551483c4d2ef7c812c55ad389b4769451e524d8caf3f3c537c1e11d4cb6c` | 14 |
| `random-flat-seed2-b.json` | `ab713d9dcc2d630fe91da0ef3cf6ed480ec2e5d4b4fd7811bc47952e223a5cc0` | 14 |
| `random-flat-seed3-b.json` | `f3008fac3d5f4c04ee534d50fad0c144d0bc487294b7a9cc44a632ae6301c3d2` | 14 |
| `generate-core-family.py` | `77f070749240bd0f573ffc235c75873140fa358b683c578725396fc876d2fd68` | 93 |
| `seed1-core448.txt` | `ea10f8b358316e32f1533daf91d48e2820172e9474b56eba3e3da65ccf23312d` | 448 |
| `seed1-core448-receipt.json` | `0dbaab11a1385b60bfcd90b35be86ce6dacf164c913be685f4cac83edfde07ea` | 5,385 |
| `check-core-family.py` | `692bcc345c9c10e769d5b73bb2270cf249b1dbb527b2dd844724d9b2d0d2c80a` | 63 |
| `independent-core448-audit.json` | `c8876d8d55c19812fd3d205780d2f02b4545cefd58c3694900b40a6d471d2a94` | 14 |
| `random-flat-core448-index1.json` | `51eafff6cb4aeecb670171c081436592c9dc67d8346a10c686395083dd148381` | 14 |
| `random-flat-core448-index2.json` | `2362e5194d999dc3334232cf7462393aefb790d7e195c9c805aa9a9332316cbf` | 14 |
| `random-flat-core448-index3.json` | `17bcdfc9cf2bf25ebdc432ff9cf4cd95b646bd9ac8c91447131b0a7575c9cab5` | 14 |
| `check-random-flat.py` | `d68698ecfd7cc504edd1a7290f84babb976ac3ce4b79dbabd2e2b9c92194b282` | 138 |
| `independent-random-flat-prefix10000.json` | `495d67b8d02868715ef0cffbc203688ad12b636c066b6b4a7eb236a77c36509f` | 14 |
| `rref-flat-search.cpp` | `dbf65f97a7266b37173bd0f04d37b1cb79b21fbe950c26d94e901378e5a460de` | 153 |
| `rref-flat-search` executable | `23ba493a6388a21be8b027f0bcbac08361a8ecc865587e594bfc8ae89c20b7f8` | — |
| `rref-flat-seed1-chunk00.json` | `5854a4591322c58a1ba9bbc56ab663e51e8a70cf130c2756746ee9ce5fcc7c57` | 17 |
| `check-rref.py` | `af173e41f7ba6fac3023ba24cfe8f97ceeab206d76b839bc9b6e5fbcec97ab19` | 149 |
| `independent-rref-smoke.json` | `f6bacdc0fba564e1b8676c8473771e8814ec61f5b0500bd276730ce09e9c84ca` | 18 |

All reported seeds are explicit Boolean truth tables; no relaxed histogram was treated as a witness. The current original gap remains an actual balanced peak≤28 table or an unrestricted exclusion. **END.**
