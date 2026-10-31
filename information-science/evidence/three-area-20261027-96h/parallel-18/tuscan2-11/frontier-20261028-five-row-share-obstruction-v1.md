# Candidate-specific five-row exclusion for unrestricted Tuscan-2(11)

Native `/bin/date` observed before writing: **Wed Oct 28 17:32:03 PDT 2026**. **EXACT INTEGER COMPUTATION, independently replayed:** for the eleven explicit row strings A below, no valid unrestricted T2(11) array on the same eleven labelled symbols can contain five or more of those row strings, even if its rows are reordered. Thus any actual T2(11) witness must use at least seven row strings not in A. This improves the earlier A-specific six-row exclusion in `frontier-20261028-candidate-share-bound-v1.md` (SHA-256 `a1329d4e6425130128afda024e53e54f1dbf6f1877342a8381845c41b599db4f`). It is **not** a global no-go, a witness, a statement after relabelling A, a formal/kernel proof, novelty clearance, or independent-model/human review.

The pinned source `frontier-20261028-row-dp-run-02.json` has SHA-256 `99ec9dc0b9970fbd282d07330cf03d3cc1d217fb3c2de2299759b9dfd3c69c29`. Its 1-based rows are:

```text
 1: 4 2 10 9 5 8 7 3 0 1 6
 2: 6 9 2 4 7 1 8 5 0 10 3
 3: 4 10 7 2 1 0 3 5 9 8 6
 4: 5 1 2 8 10 7 6 0 9 4 3
 5: 9 3 2 6 8 0 5 10 1 7 4
 6: 8 0 2 9 6 1 3 7 10 4 5
 7: 10 8 1 4 6 2 5 3 9 7 0
 8: 9 1 10 2 0 4 8 3 6 5 7
 9: 10 6 3 8 4 9 0 7 1 5 2
10: 2 3 1 8 9 10 5 4 0 6 7
11: 3 10 0 8 2 7 5 6 4 1 9
```

A itself is a nonwitness: its independently reconstructed linear D1/D2 event counts are 106/110 and 95/99, with eight pair collisions in total (`frontier-20261028-row-dp-run-02-check.json` SHA-256 `342f7b12914954d75621e5acddbd34c0ebfc4de91d4ab2d42b212f84020293c0`). The exclusion concerns only reuse of the strings above, not the original unrestricted problem.

## Complete finite reduction

There are C(11,5)=462 five-row subsets. A T2(11) array necessarily has no repeated linear D1 or D2 event and, because its 110 distinct D1 events exhaust every ordered pair of distinct symbols, each symbol starts exactly one row and ends exactly one row. Applying exactly these necessary checks directly to each five-subset leaves precisely the following 15 compatible sets; the other 447 are immediately impossible to retain:

| Fixed row IDs | Eligible additional rows | Exhaustive cover nodes |
|---|---:|---:|
| 1,2,5,7,11 | 436 | 37 |
| 1,2,7,8,11 | 300 | 4 |
| 1,5,7,10,11 | 329 | 23 |
| 1,5,9,10,11 | 649 | 45 |
| 2,3,5,7,11 | 387 | 15 |
| 2,3,6,7,8 | 427 | 36 |
| 2,3,6,7,11 | 320 | 35 |
| 2,3,6,8,11 | 711 | 13 |
| 2,3,7,8,11 | 568 | 21 |
| 2,6,7,8,11 | 334 | 14 |
| 3,5,7,10,11 | 722 | 61 |
| 3,5,9,10,11 | 580 | 7 |
| 3,6,7,8,11 | 481 | 29 |
| 3,6,7,10,11 | 609 | 58 |
| 3,6,9,10,11 | 549 | 45 |

For each fixed set, enumerate **all** permutation rows whose linear D1 and D2 events do not collide with the fixed rows and whose start and end are not used by those rows. Every row in a valid completion must appear in this finite list; this is a necessary filter only, not a claim that the listed rows are mutually compatible. The five rows use 50 distinct D1 arcs; all remaining 60 arcs must be covered exactly once by six additional rows, each contributing ten. Starting from the 60 missing arcs, choose any currently uncovered arc of minimum compatible-list size. Every valid completion contains exactly one eligible row covering that arc. Branch on every such row and remove from further consideration all rows sharing any D1 event, D2 event, start, or end with it. A branch with an uncovered arc and no eligible row is impossible. This is an exhaustive exact-cover tree: pivot choice changes speed, not coverage, and all pruning is by a necessary condition. The root-to-leaf depth is at most six. All 15 cases completed with no solution; no search cutoff or solver UNSAT claim is used. Hence no valid T2 can contain even one of the 15 compatible five-subsets, and a table containing more than five of A's strings would contain one of them.

The first implementation enumerates eligible rows by breadth-first prefix expansion and uses bitset conflict filtering for the cover tree. A separately written pre-existing exact completion program independently enumerates prefixes by depth-first recursion and uses explicit row lists and MRV branching. After independently reconstructing all 15 subset inputs, it completed every case and matched both the eligible-row counts and negative outcomes; the listed cover-node counts also coincided. Both implementations share the finite exact-cover characterization above; this is computational corroboration, not independent formal certification. They impose no Latin-column condition and no cyclic/wrap D1 or D2 events.

## Pinned computation and boundaries

- First source `frontier-20261028-five-share-exhaust-v1.py`, SHA-256 `2a31e418248fdbd8c64f45833b5f91b887d97fa954d5fb451665a68878df30ac`; result `frontier-20261028-five-share-exhaust-run-01.json`, SHA-256 `7c6e4edd98687ba9f9586e44fb7620528f17df15dbe7ba47d601819c236e458c`. All 15 cases completed; total observed 225 ms.
- Separate DFS case driver `frontier-20261028-five-share-secondary-v1.py`, SHA-256 `c39df8a4c898219f8ca9581abad8be54f096832f8fcb492087fd59c2c3a498b0`; aggregate `frontier-20261028-five-share-secondary-run-01.json`, SHA-256 `d2ad402a3c37dad049e5b56d23dd29807ba155791dc69bcdc0f7c61bf9919e81`. Its 15 separate case-output paths and SHA-256s are listed in the aggregate; total observed 314 ms. Independently written DFS helper `frontier-20261028-exact-partial-completion-v1.py` SHA-256 `1e7980a4e6c4fc1d930345628741f1a3796d5c91a596cb0928e1b2f437b0c6c`.
- These checks give a rigorously scoped row-reuse obstruction only. They do not fix any rows in the original target, prohibit arbitrary other choices of eleven rows, infer a universal upper bound, or promote a candidate to a witness. No held selected-graph consumer is used as a premise.
