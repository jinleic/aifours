# Adjacency-complete candidate: universal one-row rigidity and exact three-row obstruction

Observed native `/bin/date` before writing: **Wed Oct 28 17:28:53 PDT 2026**. Scope labels: the one-row statement below is **WRITTEN** for every order n; the candidate-specific statements are **EXACT INTEGER COMPUTATION, INDEPENDENTLY REPLAYED**, not a formal/kernel proof, external review, novelty claim, Tuscan-2 witness or unrestricted no-go. Only ordinary finite graph/matching facts derived below are used.

## Universal one-row rigidity

For every n≥1, let a T1(n) array consist of n permutations of the n symbols, with every directed **linear** adjacent event distinct. Its n(n−1) events are then exactly all ordered pairs of distinct symbols. If all rows except one are fixed in a second T1(n) array, the missing set of n−1 adjacency arcs is forced to equal the first array's removed row arcs. For n≥2 those arcs are a single directed spanning path and determine its unique order by their unique indegree-zero vertex and the unique outgoing continuation at each vertex; n=1 is trivial. Hence **no one-row replacement can change a T1 array while preserving T1**. No column-Latin or cyclic-row condition is imposed. In particular a repair search that remains adjacency-complete must modify at least two rows at once.

## Concrete candidate and exact scope

The following actual 11 rows, labelled 0–10, are the independently checked output `frontier-20261028-row-dp-run-04.json`, SHA-256 `9aa7377f3f9655bdc146d57315d5e704f6383bf345e6822c9cd032411362c9dc`:

```text
6 5 1 4 2 8 3 7 9 0 10
2 4 7 6 9 10 1 3 8 5 0
10 2 1 0 7 3 5 8 6 4 9
4 3 2 0 8 10 5 7 1 9 6
9 3 0 2 6 10 8 4 1 7 5
3 6 1 10 0 4 8 9 5 2 7
1 2 5 6 8 0 3 10 9 7 4
7 8 2 9 4 6 0 1 5 10 3
8 1 6 3 4 10 7 0 5 9 2
5 4 0 9 8 7 10 6 2 3 1
0 6 7 2 10 4 5 3 9 1 8
```

Rebuilding all actual linear events independently gave 110/110 distinct distance-one events and 84/99 distinct distance-two events, with 15 distance-two pair collisions. The 15 is a score of **this actual nonwitness**, not a global bound. Independent event-check JSON `frontier-20261028-row-dp-run-04-check.json` SHA-256 `fd549f96883faf8b660124e2b0e3ad267f0d29093410047b5a1e54804cb3aa4f`.

**Exact local conclusion.** Among all T1(11) arrays obtained from these particular rows by replacing at most three row strings while leaving the other row strings unchanged, the minimum distance-two pair-collision count is 15. Consequently no T2(11) array on these same labels can contain eight or more of these eleven exact row strings, even after an arbitrary permutation of row order. Indeed such a T2 array could be reordered to keep at least eight rows in place and would be a T1 array with zero distance-two collisions, contradicting the exhaustive ≤3-row calculation. This does not rule out T2 arrays sharing at most seven strings, arbitrary relabellings, or any unrestricted solution.

## Why the enumeration is complete

T1 completeness also forces each symbol to be the start of exactly one row and the end of exactly one row: count its n−1 outgoing and incoming arcs. Add a fresh sentinel to each row by the two arcs sentinel→first and last→sentinel. Each augmented row is a directed Hamilton cycle on 12 vertices; the augmented cycles' arcs are disjoint. Removing a chosen pair or triple of rows leaves exactly the union of their augmented arcs; any replacement preserving the other rows and T1 must partition this same residual arc set into Hamilton cycles. Conversely, any such partition yields admissible adjacency-complete linear rows. This is merely a sentinel representation of endpoints; **distance-two is always scored inside the linear rows only**, with no wrap events.

For a pair, the producer splits its residual 2-regular bipartite tail-to-head graph into two matchings. In a 2-regular bipartite graph every component is an even alternating cycle, and every perfect matching picks one of its two alternating orientations. It checks all orientation choices up to interchanging the two replacement rows and retains precisely Hamilton-cycle pairs. It found **65** unordered Hamilton decompositions across all **55** row pairs; none improved the score 15. The separately written verifier avoids matching components entirely: it depth-first enumerates every Hamilton path in the residual graph, checks that the unique remaining arcs form a Hamilton cycle, quotients only row interchange, and agrees pair by pair.

For a triple, the producer enumerates every possible first Hamilton cycle from the residual 3-regular graph, then enumerates the complete bipartite matching-component splits of the remaining 2-regular graph; it keeps only three Hamilton cycles and canonicalizes their row order. It checked all **165** triples, **6,404** first cycles, and **534** unordered Hamilton decompositions; no score is below 15. The separate verifier instead uses nested Hamilton-path depth-first enumeration of the first and second cycles, checks that the unique third complement is a Hamilton cycle, and removes only permutation duplicates by lexicographic row order. It independently matches all 165 first-cycle counts, decomposition counts, and per-triple minima. This also includes every one-/two-row replacement because its unchanged rows can be included among the three selected slots.

## Pinned evidence

- Pair producer/source `frontier-20261028-two-row-trade-v1.py` SHA-256 `1501a8dc18f152be34f64dbefe74353abe2ff1f867bde70f28a62584f2b72d85`; output `frontier-20261028-two-row-trade-run-01.json` SHA-256 `495f218a39a418b33f84d4d158f9d2f072f8c59130a62a630d5287d052619cc0`. Direct-DFS independent verifier/source `frontier-20261028-two-row-trade-independent-v1.py` SHA-256 `73dc35dd26cec796642d5c5e2292ba3a829d58c570d0766dec2331d2d9bd1a1c`; output `frontier-20261028-two-row-trade-run-01-independent.json` SHA-256 `03523adc75ba2d1d0bb5c4d0a4e4f046c502aa8f66a2591488f18c9c85ed496e`.
- Triple producer/source `frontier-20261028-three-row-trade-v1.py` SHA-256 `d53fdea62a25967ee1805780223c6ddfd92e66415513383d76e9e4c01c2bd581`; output `frontier-20261028-three-row-trade-run-01.json` SHA-256 `b47621abaaceb575c6d0c808b153bd074360bdf363580909c3617486bee1294b`. Nested-DFS independent verifier/source `frontier-20261028-three-row-trade-independent-v1.py` SHA-256 `da1acb77493ed319783169fe8173d6eb708d908ed8a64bd29ebc706cde006ebd`; output `frontier-20261028-three-row-trade-run-01-independent.json` SHA-256 `10198af3e696e71dca204421ca9ae12697bdb38a5435cedc93ddb306d5638ee7`.
- Computations share the independently explained residual-arc characterization and actual input rows; they are not a formal proof certificate or substitute for external review. No scientific conclusion from the predecessor selected-graph held episode is used.
