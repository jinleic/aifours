# Complete two-syndrome difference screen and reconstruction-method boundary

**Status: WRITTEN with independently replayed exact difference masks and exact fractional-cover certificates; conditional on the pinned proper-subgraph inequality; scientific review pending.** In the fixed q=8 triangle encoding, consider original-neighbour FD laws whose syndrome support is contained in two points `s,t`. Of the **1,023** possible nonzero difference masks `J=s xor t`:

* **603** do not cover all graph vertices with their corresponding triangles, so the syndrome-cover entropy gate gives `Delta<=0`.
* Of the remaining 420 covers, **325** have an exact universal three-coloring of every nonconfusable mixed-block difference with syndrome zero or `J`, so their laws also have `Delta<=0` for arbitrary probabilities.
* The other **95** are the complete residual list for this particular argument. For each of them, the fractional universal-reconstruction cover optimum is strictly larger than 3, so even a fractional mixture of those reconstruction inequalities cannot prove the two-thirds bound.

Thus a strict-gap q=8 law supported on two syndrome values must have its difference mask among those 95 pinned cases. **No** conclusion of gain or impossibility is drawn for any residual case; other entropy inequalities, support-specific reconstruction sets or different representations may succeed. The result is restricted to two syndrome values and the fixed q=8 factor encoding, not the unrestricted guessing-number question.

## Counts by difference weight

| Weight `|J|` | Noncover: ruled out | Cover with universal color: ruled out | Residual cover |
|---:|---:|---:|---:|
| 1 | 10 | 0 | 0 |
| 2 | 45 | 0 | 0 |
| 3 | 120 | 0 | 0 |
| 4 | 191 | 19 | 0 |
| 5 | 162 | 90 | 0 |
| 6 | 65 | 138 | 7 |
| 7 | 10 | 68 | 42 |
| 8 | 0 | 10 | 35 |
| 9 | 0 | 0 | 10 |
| 10 | 0 | 0 | 1 |

The entropy lifting is the same as `frontier-20261028-two-syndrome-distance5-v1.md` SHA-256 `606e74ea5d7ede9580c217091e240663641d23d43141ac9db49c5b753b0a38df`: condition on full fixed-factor tuples, use the universal mixed-block coloring or the pinned proper-subgraph inequality, and tensorize the fixed affine-XOR factors. For each covering `J`, the allowed vertex-difference masks are computed exactly for syndrome zero or all-one on `J` and checked against all original-neighbour FDs.

## Exact boundary of the universal fractional method

For a covering `J`, call a vertex set `I` safe if it contains no allowed nonconfusable difference support. Then its complement reconstructs every possible two-coset FD support. The minimum nonnegative weight `sum_I w_I` with vertex coverage `sum_{I containing v}w_I>=1` is the universal fractional reconstruction-cover number. At most 3 would yield the desired `2/3` entropy bound by averaging. For every colored case the optimum is exactly 3: the coloring gives an upper bound, and the three edge differences of any selected triangle give a matching dual lower bound.

For the 95 residual covers, exact primal/dual certificates give:

| Weight | Optimum `13/4` | Optimum `10/3` | Optimum `7/2` |
|---:|---:|---:|---:|
| 6 | 0 | 3 | 4 |
| 7 | 2 | 8 | 32 |
| 8 | 1 | 8 | 26 |
| 9 | 0 | 2 | 8 |
| 10 | 0 | 0 | 1 |

All values exceed 3. This exactly rules out only the stated **universal fractional reconstruction-set** route; it does not exclude support-dependent inequalities, other Shannon arguments or non-Shannon cuts.

## Evidence

The complete Möbius census `frontier-20261028-two-syndrome-full-census.py` SHA-256 `f33444fede8de0966207c5bbe6206b434acc04ad1558c5787d22951efff72c20`, receipt SHA-256 `c36f2adbf02f6dc926693c29d991f8d9c4c58536c64159c132f8f14fc559f47c`, records all 420 cover cases, their attainable difference masks and the 325 colorings. Separately written direct inclusion-exclusion replay `frontier-20261028-two-syndrome-full-independent.py` SHA-256 `17a45d4e2527ca28a50d689beadfe7ddcce364713fdc467c11319243bc08dffc`, receipt SHA-256 `190959f0b121a69fe2e2fe97bc24457702a081c73efe5540706a3b0469ab12bd`, verifies all 420 mask lists and all supplied colors.

The 95 fractional certificates `frontier-20261028-full-fractional-cover-certificates-v1.json` have SHA-256 `9f549e01128dd5a207742d1acf6040ae766058026df15709ba97f7f63ad1b148`; checker `frontier-20261028-full-fractional-cover-check.py` SHA-256 `022556fe4c2cbe9c1f88fd465f902d2debc529259c182f110e6813d4f49649be`, receipt SHA-256 `eeaef6ca59ac2a907f3b6e1403af27e3f6518d31f5b9d1f3bf7829f80e2e447d`, verifies every rational primal/dual equality and all 1,024 vertex subsets per case, with a changed-dual control. The underlying graph-FD inequality, conditional lifting and finite enumeration interpretations remain subject to scientific review; no proof-assistant or novelty claim is made.
