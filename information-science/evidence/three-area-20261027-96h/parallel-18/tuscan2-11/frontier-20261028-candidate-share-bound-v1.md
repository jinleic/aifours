# A checked near-candidate cannot share six rows with any Tuscan-2(11) witness

Owner **InfoRecursiveMDS18-2**, info-4. Native clock before writing: **Wed Oct 28 17:21:47 PDT 2026**. This is a finite, candidate-specific obstruction; it does NOT exclude an unrestricted Tuscan-2(11) array and does not imply a global lower bound.

## Exact statement

Let A be the actual eleven-row array in `frontier-20261028-row-dp-run-02.json` (SHA256 `99ec9dc0b9970fbd282d07330cf03d3cc1d217fb3c2de2299759b9dfd3c69c29`). **No original Tuscan-2(11) array on the same labelled alphabet contains six or more of A's rows**, even after arbitrarily reordering row slots. In particular any repair of this particular A keeping rows in their original slots must change at least six whole row slots.

The original rows are permutations; its separately checked event layers contain106 distinct ordered linear adjacency pairs out of110 and95 distinct ordered linear distance-two pairs out of99. A itself is not a witness. No column condition or wraparound rule is imposed.

## 1. Necessary event and endpoint conflicts

Every original T2(11) has all ten incoming and all ten outgoing ordered adjacency pairs of each symbol exactly once. As the symbol appears in eleven rows, it begins exactly one row and ends exactly one row. Hence no original array can contain BOTH rows of a pair that either:
- repeat an ordered adjacency or distance-two event at the same distance; or
- have the same first symbol or the same last symbol.

For the actual A, independently recomputed conflicts include five PAIRWISE DISJOINT row pairs:

- `(1,3)` share the first symbol4 (and also share the last symbol6);
- `(2,4)` share the last symbol3;
- `(5,6)` share a linear distance-one event;
- `(7,9)` share the first symbol10;
- `(8,10)` share the last symbol7.

Therefore any witness retaining rows from A can retain at most one endpoint from each pair, i.e. must discard at least five A rows. It cannot retain more than six.

## 2. The only possible six-row subset

The conflict list additionally includes `(4,11)`, `(2,9)`, `(2,10)`, `(5,8)` and `(1,6)`.

Suppose exactly five A rows are discarded. They must comprise exactly one endpoint from each of the five disjoint pairs above, leaving no room to discard row11. Consequently:
1. `(4,11)` forces row4 discarded, so row2 is retained.
2. Since row2 is retained, `(2,9)` and `(2,10)` force rows9 and10 discarded, so rows7 and8 are retained.
3. Since row8 is retained, `(5,8)` forces row5 discarded, so row6 is retained.
4. Since row6 is retained, `(1,6)` forces row1 discarded, so row3 is retained.

Thus the ONLY conflict-free six-row subset is exactly `{2,3,6,7,8,11}`, whose full rows are recorded in `frontier-20261028-six-row-noncompletion-v1.md`. The independent cover analyzer `frontier-20261028-endpoint-cover-dp-02.json` (SHA256 `51fb4b31757b303d7368e041486269247ce536b98dd27619cd40b933f6c84215`) confirms this uniqueness by checking every one of the 1024 index subsets of size at most5; it also independently rebuilds both event layers and endpoints on the six retained rows.

## 3. Even that six-row subset has no completion

Two independently implemented exact checks exhaust all individually admissible next rows for this concrete six-row subset. Each requires an actual permutation, no repeat of any fixed row's D1 or D2 event at the same distance, and a start/end distinct from the six fixed starts/ends. These are necessary conditions of any full witness.

- Prefix-tree enumeration examined2213 prefix nodes and found exactly20 eligible next rows; neither needed adjacency `0→9` nor `6→0` occurs in any of them. Output `frontier-20261028-partial-completion-01.json`, SHA256 `788678567ae1dec2a3ed85ed27794ccc52a9eebef255e52ce7410f571b09f551`.
- A separate suffix-state dynamic program examined2025 memoized states, counted exactly20 eligible rows and independently found the same two unsupported adjacency pairs. Output `frontier-20261028-partial-edge-dp-01.json`, SHA256 `779316f618876a104b18d8715c76382883d41369117bd84ab4aa45682465e5ee`.

Both `0→9` and `6→0` are absent from the six fixed rows, so a full original array would need a remaining row carrying each. No such individually compatible row exists. Thus the sole possible six-row subset cannot extend, establishing the claim. Exact method, input rows, commands and source hashes are provided in `frontier-20261028-six-row-noncompletion-v1.md`, SHA256 `2d8a43b008f5276dc15c85ab9e72d14844e63c591aa32101cd76974003331ea7`.

The separate SAT solver also returned UNSAT on this fixed-six neighborhood, but no SAT proof replay was performed and the present argument does not depend on that result. An independent Z3 attempt timed out UNKNOWN. The finite checks are independent implementations and locally executed, not a formal proof assistant or independent-model review.

## 4. Why this changes the repair strategy, not the global problem

A simple conflict-cover prefilter would leave the unique six-row subset as apparently viable; actual compatible-row exhaustion shows it cannot be completed. Hence a solver-guided search must replace at least six of A's eleven rows, or leave this candidate's fixed-row neighborhood entirely. This claim is limited to this concrete A with its actual symbols. A fresh array, a changed choice of six rows, or another global method is not excluded.

**Open:** the unrestricted original T2(11) existence/no-go. This local finite result is not a witness, universal obstruction, source-status verification or novelty claim.
