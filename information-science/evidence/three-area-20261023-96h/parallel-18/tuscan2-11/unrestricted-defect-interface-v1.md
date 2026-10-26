# Unrestricted Tuscan11 defect interface and finite certificate proposal v1

Clock observed before creation: **2026-10-23T14:55:07-0700**. Full primary target remains `selection-v1.md`. The group-source deletion route is closed only at the written-candidate level described by the three obstruction documents plus notation erratum. Both old assay proposals remain superseded/HOLD and were never run.

This record does **not** claim a new Tuscan theorem or a solved encoding. It fixes a literal unrestricted finite certificate experiment, derived from the actual endpoint/defect identities, after the narrower deletion route was exhausted in writing. No scientific source below has been imported, compiled, typechecked, tested or executed.

## 1. What the unrestricted defect identities do and do not allow

For any candidate square A of order n, adjacency coverage makes each symbol occur first and last exactly once. Its n(n−2) distance2 events are distinct in an n(n−1)-pair universe, so exactly n pairs are missing. Their directed missing graph M has

`outdeg_M(a) = #{rows with penultimate symbol a}`,

`indeg_M(a) = #{rows with second symbol a}`.

At n=11 this is an11-arc digraph, with degrees not assumed1. It need not be the endpoint-matching graph. None of the columns2through10 is assumed a permutation. An attempted proof or finite search that imposes those extra constraints would solve a restricted Roman-2 problem, not the active Tuscan-2 target.

The identities provide two legitimate propagation facts: first/last columns are permutations, and the full adjacent-pair coverage follows already from row permutations plus adjacent-pair noncollision. They do **not** prove that all possible defect graphs are impossible. The remaining mathematical obstacle is coupling a valid defect graph to11 actual Hamilton paths whose two-step events are all different, rather than constructing a graph satisfying necessary degree counts alone.

## 2. Exact unrestricted Boolean model

For general n≥3, use cell variables

`x_(r,c,a) ⇔ A[r,c]=a`, with `0≤r,c,a<n`.

For every cell require exactly one a; for every row and symbol require exactly one column. Thus rows are arbitrary permutations, not necessarily translates, group tables or Latin columns.

For each d∈{1,2}, each valid starting position `(r,c)` with `c+d<n`, and a≠b, introduce

`y_(d,r,c,a,b) ⇔ x_(r,c,a) ∧ x_(r,c+d,b)`.

Encode the equivalence with three clauses:

`¬y∨x_left`, `¬y∨x_right`, `y∨¬x_left∨¬x_right`.

For each fixed `(d,a,b)` require at most one y over all valid row/position events. Uniqueness is separate at the two distances. There is no wraparound, no merged-distance prohibition and no condition at distances≥3.

At d=1, n rows each provide n−1 events, all on distinct-symbol pairs. Therefore noncollision yields exactly n(n−1) different pairs, the whole universe. At d=2 only at-most-one is required. Consequently this model is equivalent to the FULL Tuscan-2 definition, before the safe normalizations below.

### Safe normalization and endpoint propagation

Choose any row of a solution and globally relabel symbols in its left-to-right order, making it `(0,...,n−1)`. Every symbol occurs first once, so sorting rows by their first symbol makes column0 natural and retains that chosen row as row0. This justifies the unit clauses

`x_(0,c,c)` and `x_(r,0,r)`.

By the independent endpoint count, the last column is a permutation, so explicitly requiring that is redundant and sound propagation. **No other column is constrained.** This is the standard-form normalization used in the classical Tuscan literature, not a new symmetry theorem claimed by this slot. Arbitrary column permutations and independent row reversals are not used.

### Sequential at-most-one correctness

For literals `p_0,...,p_(k−1)`, auxiliary prefix variables `s_0,...,s_(k−2)` are constrained by

- `¬p_0∨s_0`;
- for `1≤i≤k−2`: `¬p_i∨s_i`, `¬s_(i−1)∨s_i`, `¬p_i∨¬s_(i−1)`;
- `¬p_(k−1)∨¬s_(k−2)`.

If two p are true, the earlier one's prefix truth propagates forward and contradicts the later one's exclusion of the preceding prefix. Conversely if at most one p is true, set each s_i to the OR of the preceding p through i; all clauses hold. This establishes exact existential equivalence, not merely one implication or an intuition about counters.

## 3. Expected finite sizes — written formulas, not observed outputs

The frozen generator uses pairwise exactly-one for cells, row/symbol occurrences and last-column symbols, plus the sequential counters above for pair events. Its exact counts should be:

- cell variables: `n³`;
- event variables: `n²(n−1)(2n−3)`;
- counter variables: `n(n−1)(2n²−3n−2)`;
- small exactly-one clauses: `(2n²+n)(1+n(n−1)/2)`;
- normalization unit clauses: `2n` (including a duplicate corner unit, harmless);
- channel clauses: `3n²(n−1)(2n−3)`;
- event-counter clauses: `n(n−1)(3n(2n−3)−8)`.

Thus the expected `(variables,clauses)` are:

| Order | Expected variables | Expected clauses | Intended role |
|---:|---:|---:|---|
|3|123|366|known negative encoding control|
|4|520|1604|known positive encoding/control decode|
|11|47091|151250|unrestricted target, not a symmetry subclass|

These figures were derived in writing from the loop ranges. **They are not receipts from a generated CNF or solver execution.** Any actual generator mismatch is HOLD pending inspection/new source version, not permission to silently repair and rerun.

## 4. Definition-level controls calibrated in writing

A concrete T2(4) is

`0 1 2 3`

`1 3 0 2`

`2 0 3 1`

`3 2 1 0`.

Its adjacent ordered pairs, by row, are

`01,12,23; 13,30,02; 20,03,31; 32,21,10`,

exactly all12 distinct pairs. Its distance2 pairs are

`02,13; 10,32; 23,01; 31,20`,

eight distinct pairs. This manually checks the positive calibration against the literal definition before asking a program to validate itself.

No Tuscan-1 square of order3 exists. In the sound standard form, the first row is012. Since starts and ends are permutations and no row has equal start/end, the other rows would have to be120and201. Then the adjacent pair12 is repeated. Therefore the full order3 encoding must be UNSAT. This negative statement is an elementary written proof, not an external solver report.

The checker also has intended-reason mutations: a duplicate symbol, an out-of-range value, a row-permutation mutation repeating an adjacent pair, a malformed shape, and the developed Z6 Walecki starter `(0,1,5,2,4,3)` whose adjacent quotients are1,4,3,2,5 but whose distance2 quotients repeat5and1. The latter is a genuine Tuscan-1/non-Tuscan-2 control rather than a malformed array accidentally rejected earlier.

## 5. Frozen proposed code and source-trust boundary

New source: `unrestricted-tuscan-sat-v1.py`, SHA-256 **`ae060379381e7700d298fd22b7d35e8e41f0e6d6b812bb011a6602bd2c2e5904`**.

It has separate finite CLI operations:

- `controls`: author definition-checker positives/mutations;
- `encode N DIR`: create an exclusive new directory and deterministic DIMACS/manifest for the exact model;
- `decode N DIR LOG OUT`: require the pinned CNF/expected order, a complete SAT assignment, reconstruct the literal array and check its full definition; exclusive new output only;
- `check-table N FILE`: literal array predicate only.

It launches no solver or subprocess, uses only the Python standard library, reads/writes only the owned root for runtime file arguments, and does not impose group/deletion assumptions. A decoder acceptance would still be the author's own implementation, not independent certification. UNSAT output is not accepted by the decoder and must not be promoted without a checked proof and completeness/normalization review.

Available local metadata, observed only (not solving): Python3.14.3 at `/opt/homebrew/bin/python3`, SHA-256 `cbf84109626aa1013bbe408fbb9590bd0f1c1548f038b2221c6b8b87de26ca43`; Kissat4.0.4 at `/opt/homebrew/bin/kissat`, SHA-256 `05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848`. Its actual `--help` documents the internal `--time=<seconds>` limit and full assignments by default. Only version/help/hash metadata calls were made, not any CNF generation, check or solve.

## 6. Proposed admission sequencing and scientific limits

A successor request may admit ONLY encoding/controls first: fixed source/interpreter pins, literal inputs3/4/11, exclusive fresh output root, fresh resources and receipts. It must then bind actual generated CNF byte hashes and compare the counts above before requesting a separate exact native-solver admission. No unpinned input file can be launched just because a generator source was once approved.

A later solver assay, if parent admits it, should run known-positive4 and known-negative3 controls before one short internally time-limited order11 solve using a pinned solver and exact CNF. If SAT, save the literal121-entry array and obtain actual independent and parent definition-first checks. If UNSAT, preserve the proof trace and require independent proof checking and scope review before a full-target claim. If no decision within the internal limit, report UNKNOWN; no automatic retry, longer run or model change is authorized.

This finite experiment proposal is not mathematical progress by itself. The substantive completed written candidate in this lane is the group-source deletion barrier, still awaiting review and with novelty separate. The unrestricted defect problem remains scientifically open here; no reduced model or empty encoding is counted as its solution.
