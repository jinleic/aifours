# info-6 frontier: exact six-flip neighborhood of three published seeds

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T18:27:14-0700 PDT**. This is an author-owned finite executable search, not yet disjointly reviewed. It does not resolve the unrestricted balanced NL242 problem.

## Result and immediate scope

For each of the three pinned published peak-28 Boolean tables, the native program enumerated every 6-position flip set implicitly, subject to an exact necessary condition at the original peak frequencies. It examined every surviving set against **all 512** Walsh values and found no peak≤28 table with any zero coefficient; hence an affine output twist cannot make one balanced. There are `C(512,6)=24,295,061,050,624` possible six-sets, but the program prunes them exactly rather than visiting them all: each source has 210 original peak frequencies, and precisely **195** six-sets survive their necessary peak inequalities.

For seed 1, a separately written Python big-integer implementation replayed the entire enumeration and independently computed all 512 character sums for each of the 195 surviving actual flipped tables. It found:

| Peak | Number of zero Walsh coefficients | Affine dimension of six flip positions | Number of six-sets |
|---:|---:|---:|---:|
| 28 | 0 | 4 | 120 |
| 32 | 0 | 3 | 15 |
| 32 | 4 | 3 | 24 |
| 32 | 5 | 3 | 36 |

Thus **all** 195 peak-compatible six-sets for seed 1 are contained in some affine 4-flat, including the 120 true peak-28 tables. This is a finite computational observation for this seed, not a universal statement about arbitrary Boolean functions. The independently checked seed-1 six-set list and classification are pinned below. Seeds 2 and 3 have the same native 195-survivor count and no target, but this file does **not** claim their complete independent replay.

Combining the new six-flip result with the previously independently checked 0-, 2- and 4-flip searches yields the following bounded exclusion, subject to the evidence boundaries just stated: **none of the three sources can reach a balanced peak≤28 table by at most seven truth-bit flips and an arbitrary affine output twist**. The 0-flip sources have no Walsh zero. For every odd flip count the conclusion is elementary: the sources have even truth-table weight, every affine function on nine variables has even weight, and the parity of the output weight after those XOR operations is the parity of the flip count, whereas a balanced table has even weight 256. The native six-flip scan for seeds 2 and 3 has not yet received the independent full replay used for seed 1.

## Exact pruning rule

At an original peak a with W(a)=±28, call an input position bad when flipping it moves W(a) away from zero. Of six flipped positions, more than three bad positions necessarily make the final magnitude exceed 28. Therefore an eligible six-set cannot contain **any** four positions all bad at the same original peak. For every increasing triple, the solver intersects its three bad-frequency masks; each common bad frequency rules out its bad points as a fourth position. The corresponding rule is intersected over every triple of a valid four-set when extending to five positions, and every triple of a valid five-set when extending to six. This enumerates every six-set satisfying all necessary peak constraints; there is no randomness or assumption that peak compatibility alone suffices for a target. The final full-spectrum computation checks the remaining nonpeak constraints and every potential zero.

For each source the outer three positions have `C(509,3)=21,849,334` enumerated combinations; the native receipts show complete first-position range `[0,507)`, no timeout, and no target. Seed 1's Python replay agrees on all intermediate counts: 21,849,334 triples, 2,978,536 compatible four-prefixes, 23,607 compatible five-prefixes, and 195 checked six-sets. Its full direct-character-sum evaluation uses 512-bit integer population counts and a mutation control. These are same-owner independently implemented computational cross-checks, not a disjoint review or formal verification.

## Pinned evidence

All files are in this directory. SHA-256 values refer to observed artifact bytes.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-published-seeds.txt` | `116ab5a7709dd35d951ddc878af227e5e05ce269d8293e5c0c269e158bd051f2` | 6 |
| `frontier-20261028-core-outer-search.cpp` | `a1cd5207f2bcaf975998250002fb735717cd88625d5a304f4ae76d02d680652e` | 295 |
| `frontier-20261028-six-flip-search.cpp` | `f696e60ad31b04b36880ca4d86f2a8d05d035a378911cfd1ece0e6a59c4ffb5d` | 125 |
| `frontier-20261028-six-flip-search` executable | `38a0d2d307efe05fab65f9f6ef9d536b06f98fec217e7ee30a47c2c427f812dd` | — |
| `frontier-20261028-six-flip-independent.py` | `53f67691dd440dc12dee6916dc03a157d601f959c0a25c40a4ca6c3284b99ad4` | 107 |
| `frontier-20261028-six-flip-seed1-all-result.json` | `3de2293101dab06de3ea5a17b5a7be1720b88bb3cac28674b048682b1e6e4e01` | 15 |
| `frontier-20261028-six-flip-seed1-independent.json` | `a9a998270920637eaafe8c3e971dcd1680035d4023581f37ee9cb6abb28cb176` | 2,355 |
| `frontier-20261028-six-flip-seed2-all-result.json` | `50fddc921b3278ee8596eef9715e0187bcb4aeff6a8d72f39b3292e9da0fa7f5` | 15 |
| `frontier-20261028-six-flip-seed3-all-result.json` | `af0cc0fb457553aeae7acb4f69ac162aefe4bb6467f64e0395eb28e69a55724d` | 15 |
| `frontier-20261028-six-flip-classify.py` | `f93bcc5e47481614554268457a63785c7559446f2f2548288dca68dee1e7f330` | 42 |
| `frontier-20261028-six-flip-seed1-classes.json` | `21a985382b8ec9d9561acbd75faaec94af80a65cc313f4bca04e446123530334` | 31 |
| `frontier-20261028-two-flip-report.md` | `375d9034c03b6b469878a4cd74435dc37e8a6f7ba450ff12d71ee0853d04314d` | 74 |
| `frontier-20261028-four-flip-span-report.md` | `377a569c10b60d79fd367b263b800afad376e0516d4911f3afe28b86d4e47fc7` | 78 |

No actual balanced NL242 witness has been found. **END.**
