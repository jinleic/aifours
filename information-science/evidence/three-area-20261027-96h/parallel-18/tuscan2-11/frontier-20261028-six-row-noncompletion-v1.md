# Exact, independently recomputed noncompletion of one actual six-row partial array

Owner **InfoRecursiveMDS18-2**, info-4. Native metadata clock before this record: **Wed Oct 28 17:14:49 PDT 2026**. This is a computationally checked, candidate-specific obstruction, NOT an unrestricted Tuscan-2(11) no-go.

## Scope and six actual rows

These are rows 2,3,6,7,8,11 from the independently checked `frontier-20261028-row-dp-run-02.json` (SHA256 `99ec9dc0b9970fbd282d07330cf03d3cc1d217fb3c2de2299759b9dfd3c69c29`):

```text
6  9  2  4  7  1  8  5  0 10  3
4 10  7  2  1  0  3  5  9  8  6
8  0  2  9  6  1  3  7 10  4  5
10 8  1  4  6  2  5  3  9  7  0
9  1 10  2  0  4  8  3  6  5  7
3 10  0  8  2  7  5  6  4  1  9
```

The six are actual permutations of 0..10, with distinct LINEAR distance-one events and distinct LINEAR distance-two events, and separately distinct first and last symbols. They are not a full table.

**Claim:** no unrestricted original T2(11) table can contain all six rows, irrespective of their order among the eleven row slots. In particular, freeing only rows 1,4,5,9,10 of the source candidate cannot produce a witness. Other six-row choices and all other arrays remain open.

## Reasoning

In any original array, each distinct ordered adjacency pair occurs exactly once. Every symbol occurs in all eleven rows and has ten distinct incoming and ten distinct outgoing adjacency events. Therefore each symbol is first in exactly one row and last in exactly one row. A new row compatible with the six fixed rows must:
1. be a full permutation of 0..10;
2. use none of their ordered events at the same respective linear distance1 or2;
3. start and end at symbols not already used as a start and end respectively.

These are NECESSARY, not assumed sufficient to extend. Under exactly these constraints, complete finite enumeration gives **20** possible additional rows; none contains adjacency `0→9` or `6→0`. Neither of those directed adjacency pairs is present in the six fixed rows. Original distance-one coverage would require each to occur in a remaining actual row, but no individually compatible remaining row can contain either. Thus completion is impossible. No same-distance event is interpreted with wraparound and no Latin-column condition is used.

## Independent computations and boundary

1. `frontier-20261028-exact-partial-completion-v1.py`, SHA256 `1e7980a4d344f3e66f222395bd1fbf1211ac158b7dd34840d5cfc991f75b0c6c`, was run as:

```text
python3 frontier-20261028-exact-partial-completion-v1.py frontier-20261028-row-dp-run-02.json frontier-20261028-partial-completion-01.json 2,3,6,7,8,11 30 5000000 300000
```

It completed the whole prefix-tree search: 2213 prefix nodes,20 eligible whole rows, no budget stop, and unsupported required adjacencies `[[0,9],[6,0]]`. Result SHA256 `788678567ae1dec2a3ed85ed27794ccc52a9eebef255e52ce7410f571b09f551`.

2. A separately written memoized suffix-state DP `frontier-20261028-partial-edge-dp-check-v1.py`, SHA256 `f1ec9a67cda3009cca6e638df69160a09530b76d5c9fd4389dd9910a76cbbc07`, was run independently on the same six actual rows:

```text
python3 frontier-20261028-partial-edge-dp-check-v1.py frontier-20261028-row-dp-run-02.json frontier-20261028-partial-edge-dp-01.json 2,3,6,7,8,11
```

It counted20 eligible rows and exactly the same unsupported adjacencies, visiting 2025 memoized states. Result SHA256 `779316f618876a104b18d8715c76382883d41369117bd84ab4aa45682465e5ee`.

The independent DP state is `(used-symbol mask, previous symbol, last symbol)`. For each allowed next symbol, it checks the corresponding unused distance1 and distance2 event and unions the adjacency masks of all COMPLETABLE suffixes. Its base accepts a full mask only when the last symbol has not already ended a fixed row; initial symbols already starting fixed rows are excluded. Induction on remaining symbols proves that its count and event union cover every possible additional actual row satisfying 1–3. This checker does not use the first enumerator's candidate list or its unsupported-pair output.

3. The separate SAT encoding reported UNSAT for these same fixed slots (`frontier-20261028-sat-repair-02.json`), whereas the independent Z3 model reached its30-second timeout with UNKNOWN. No SAT proof certificate was replayed; the argument above does not rely on either solver's verdict.

The associated eleven-row near-candidate has 106 distinct adjacency events of110 and95 distinct distance-two events of99; it is NOT a witness. An independent one-row best-response DP reported no strictly lower total pair-collision score by replacing any one row. Those are local computational facts only. Formal/kernel and independent-model verification were not performed; mathematical novelty is not claimed.
