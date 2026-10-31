# info-6 frontier: seed-2 and seed-3 independent six-flip replays

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T18:29:16-0700 PDT**. Additive to the unchanged `frontier-20261028-six-flip-obstruction-v1.md`, SHA-256 `b3a863f3816c42ffbc18e10fef1e47ff789d2dcccb47a4246d7b3872f74a71f0`, 48 LF. This is a same-owner independent computational implementation, not a disjoint review or unrestricted nonexistence claim.

The Python big-integer replay has now also completed for published seeds 2 and 3. For each, it independently computed the source's 512 direct Walsh character sums, traversed the full six-position pruning enumeration, and directly recomputed all 512 Walsh values of each surviving six-flip table. Both traversals completed without timeout and found **zero** balanceable peak≤28 tables. Intermediate counts exactly match the earlier native C++ receipts:

| Seed | Triple prefixes | Compatible four-prefixes | Compatible five-prefixes | Surviving six-sets | Targets |
|---|---:|---:|---:|---:|---:|
| 1 | 21,849,334 | 2,978,536 | 23,607 | 195 | 0 |
| 2 | 21,849,334 | 2,971,717 | 23,607 | 195 | 0 |
| 3 | 21,849,334 | 2,983,930 | 23,607 | 195 | 0 |

For each seed, a separate rank classifier finds all 195 peak-compatible flip sets contained in an affine 4-flat. Exactly 120 of the 195 have peak 28, no Walsh zeros, and affine dimension 4; the remaining 75 have peak 32 and affine dimension 3. The numbers of zeros among the 75 differ by seed; the class receipts give the precise distributions. Together with the previously checked 0/2/4-flip cases and odd-flip parity, the original ≤7-flip-plus-affine-twist exclusion now has the independent full six-flip replay for **all three** sources. It remains a narrowly bounded local result.

| New artifact | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-six-flip-seed2-independent.json` | `5fc7354d2adf85098b26a9b371b5d2ac7c1a505acf7f40d53da8f0eaa14c1f86` | 2,355 |
| `frontier-20261028-six-flip-seed2-classes.json` | `9dbe74702f2ceb554ecff5532d9352d4e7f09c6fd6e594980046d572e9be277a` | 49 |
| `frontier-20261028-six-flip-seed3-independent.json` | `f3851b6749f59d7e6e79fa3a651aed5a0555fbe18e0d2f2a8e5ef82414ed0956` | 2,355 |
| `frontier-20261028-six-flip-seed3-classes.json` | `cee2dde8aeec6da2a00911018faba85245d6566d1d6fa173a87ceb2845a07a56` | 31 |

No candidate Boolean witness was found. **END.**
