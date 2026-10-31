# info-6 frontier: a certified-size bounded swap component around one NL240 table

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T18:21:48-0700 PDT**. This is an executable finite search with a separately implemented local replay, **not yet disjointly reviewed**. It concerns one explicit actual table and a restricted path class; it is not an unrestricted no-go or novelty claim.

## Scope and conclusion

The source `frontier-20261028-balanced-anneal-a-candidate.json` is an actual balanced 512-bit function. Independent direct-character-sum, FWHT, inverse and Parseval checks gave weight 256, W(0)=0, peak 32, nonlinearity 240, exactly 27 coefficients of absolute Walsh magnitude 32, and five Walsh zeros. It is not an NL242 witness.

Define a graph whose vertices are actual balanced Boolean tables with peak at most 32 and at most 31 coefficients of magnitude 32. Connect two vertices when one is obtained from the other by swapping a one-position and a zero-position. The source's connected component has **5,731 vertices**, all with at least 27 magnitude-32 coefficients. The native breadth-first search and the independently implemented Python bitset traversal each report the same 5,731 expanded/visited vertices, 375,586,816 candidate directed swaps, 4,956,872 peak≤32 directed neighbors, and 129,220 directed neighbors within the 31-peak cap; both queues drained without reaching the node or time cap.

Consequently, subject to this finite executable certificate, a balanced peak≤28 table cannot be reached from this source by a sequence of balanced swaps all of whose intermediate tables have peak≤32 **and** at most 31 magnitude-32 coefficients. Any such path, if one exists, must at some point exceed one of those two bounds. This conclusion is not an assertion about other starting functions, arbitrary transformations, or paths that exceed the cap.

## Two independent neighborhood algorithms

For a swap x∈f⁻¹(1), y∈f⁻¹(0), balance is preserved and `Δ(W(a)/4)` is `χ_a(x)` when `χ_a(x)≠χ_a(y)`, otherwise zero. The C++ implementation enumerates all 256×256 swaps and rejects immediately if any changed coefficient would exceed absolute value 32. The Python implementation instead intersects 512-bit coordinate masks for the current peak frequencies, then uses character masks and integer popcounts to update the peak count. Each constructs and deduplicates actual truth tables and exhausts the resulting queue.

The Python replay independently recomputed the source's complete spectrum by direct character sums and checked four encountered neighbors by fresh direct sums, including rejection of a deliberately changed expected coefficient. Its sorted vertex-set digest is `33c55f4c707546e2526ac5f2af7597b83795229aa5eb8e1594a39ced3c060b30`. The two implementations are same-owner computational cross-checks, not an independent-model, human, or formal verification.

A separate cap-32 run timed out after 11,004 expansions and 13,943 discoveries, without finding a better table; its queue did **not** drain. It supports no complete cap-32 conclusion.

## Pinned evidence

All paths are in this directory. SHA-256 values are from the actual artifact bytes.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-balanced-anneal-a-candidate.json` | `5d2dd87f5c77ea6b3767e57f73816f7fb881172d189db354c426ecf1115efcdc` | 8 |
| `frontier-20261028-balanced-anneal-a-audit.json` | `37f7e9309574bf73e9008565b0415966d3b634d0f91bbb7bd2ad96f46740fbeb` | 559 |
| `frontier-20261028-balanced-descent.cpp` | `a6cdbb31414a65184d572659ee2ef352a5e623171b9f2a1c4e560dcb4e8b9b10` | 128 |
| `frontier-20261028-balanced-bfs.cpp` | `8a52187f8095091ec623757395a9ff8bc9a80eaea4755ac89367d24773ee1519` | 75 |
| `frontier-20261028-balanced-bfs-independent.py` | `617061c3cbf99d125c847fe780fb3275b620b1b2087b9dc2a7c33f20b91e8fc3` | 116 |
| `frontier-20261028-balanced-bfs-c-result.json` | `8cf7568dde5eb45074ea896e587c91d6885201b4331f6ec3a2d2c6645d839bcd` | 17 |
| `frontier-20261028-balanced-bfs-c-independent.json` | `554071b07b878251a34bc91eb81b5fce4eed7ee4e36eb998bea815d6987e813e` | 39 |
| `frontier-20261028-balanced-bfs-d-result.json` | `f8c0063fda6d237d4037c1973e70d86238c8521c9122e3a9191acfcdbf73e354` | 17 |

The original witness-or-unrestricted-exclusion gap remains. **END.**
