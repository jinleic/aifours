# Exact repair obstruction for one checked Tuscan-2(11) near-candidate

**Scope:** only the actual eleven rows in `frontier-20261028-search-run-02.json`, SHA256 `5a941a6c3f6fa3b65a9f9d1972eb70e94c55b6cb11b72ee41baf7d3f4707be05`. Row slots below are numbered1–11. This is NOT a global obstruction or a claim that any particular row-repair neighborhood has a solution.

## Statement

Any array that retains at least eight of these eleven rows in the SAME row slots necessarily contains a repeated ordered event at linear distance1 or linear distance2. Equivalently, at least FOUR original row slots must change to obtain a Tuscan-2(11) witness from this candidate. The four-slot sets that remove all pre-existing conflicts among unchanged rows are exactly

`{1,3,5,10}`, `{1,3,5,11}`, `{1,5,10,11}`.

Choosing any one of these sets for free rows is necessary to keep seven candidate rows fixed, but does NOT imply a valid completion of those seven exists.

## Proof from the actual event incidence

For this candidate, connect row indices when the two rows repeat an ordered pair at the SAME linear distance. Independently rebuilding all110 adjacency events and99 distance-two events gives exactly the following row pairs:

`(1,2), (1,4), (1,10), (3,5), (3,10), (3,11), (5,9), (5,10), (5,11), (10,11)`.

Both occurrences of a repeated event survive if both of its rows are unchanged. Therefore every changed-row set must meet every listed pair.

No set of at most three can do that:
- If row1 is unchanged, rows2 and4 must both change to hit `(1,2)` and `(1,4)`. At least two further rows are needed for the disjoint pairs `(3,10)` and `(5,9)`.
- If row1 changes, at most two further changes remain. The triangle on rows3,5,10 requires at least two of them. If neither of those two is5, the pair `(5,9)` remains. If one is5, exactly one of3 or10 remains unchanged and its pair with11 remains. Either way at least a third additional row is necessary.

The set `{1,3,5,10}` meets every listed pair, so four is the exact minimum for eliminating current frozen-row conflicts. Checking all row-index subsets of sizes0 through4 found exactly the three minimum sets stated above; the script additionally rebuilt both event layers on each frozen complement and confirmed that each complement is collision-free. This exhausts the 562 subsets through size4, not the space of possible new rows.

## Actual bounded search/check status

The source candidate was independently inspected with `frontier-20261028-tuscan-check-v1.py`, SHA256 `8a46ce0fd0a97663ea5117ad234a36a2b80ad0c12d91bce22e597678e42f6320`, producing `frontier-20261028-search-run-02-check.json`, SHA256 `4637a22bb6a1cb72375fc3d0149909ceab26681ddffa915b7c9ebfe1176fb7d7`: 105/110 distinct D1 and93/99 distinct D2 events, not a witness.

`frontier-20261028-row-conflict-cover-v1.py` (SHA256 `06ce9e503d18d38e4c186946a93fef597b87751f9b0bd476e6566a968e284ab4`) produced the reproducible event-to-row lists and all minimum covers in `frontier-20261028-row-conflict-cover-02.json` (SHA256 `830b9273db209ba5f9ed22b80b6ffb2893856f5494b61d55458da675154b5597`). The elementary lower-bound argument above is separate from reliance on the subset enumeration.

A bounded Z3 attempt left rows2,4,6,7,8,9,11 fixed and freed `{1,3,5,10}`. It returned **UNKNOWN, reason timeout** after a requested30-second solver limit; it did not return SAT or UNSAT. Full-model run with first row normalized by a common symbol relabel also returned **UNKNOWN, timeout** under a separate30-second limit. Neither is evidence of nonexistence, and the frozen-row result applies only to that one neighborhood. Exact model/input/result pins are recorded in the accompanying JSON outputs.

The target remains the unrestricted original: arbitrary actual permutation rows, distinct linear adjacency events and distinct linear distance-two events. No Latin-column or wraparound condition is introduced. A fresh candidate or witness must be independently checked from its rows. This record establishes only a local obstruction around the named candidate; it is not a mathematical lower bound for all arrays, a proof of T2(11) nonexistence, a formal certificate or a novelty claim.
