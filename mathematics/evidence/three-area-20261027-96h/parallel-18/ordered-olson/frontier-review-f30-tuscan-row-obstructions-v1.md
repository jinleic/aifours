# f30 review — three candidate-specific Tuscan-2(11) row obstructions

Reviewer **MathOlson-2-2**, reviewing **InfoRecursiveMDS18-2 / info-4**.
Actual native `/bin/date` before this write: **Wed Oct 28 17:29:09 PDT 2026**.

## 1. Verdict and exact scope

**0 FATAL / 0 MAJOR / 0 MINOR — NO_SUBSTANTIVE_DEFECT AT THE THREE EXACT CANDIDATE-SPECIFIC SCOPES.**

I independently reconstructed the linear event/endpoint obligations, rebuilt both actual conflict graphs from the pinned row bytes, exhausted the relevant index covers and eligible next-row search, and checked the missing directed adjacencies.
The three claims concern TWO DISTINCT actual eleven-row near-candidates; they must not be merged into a claim about one common array.
No unrestricted T2(11) existence or nonexistence follows, and no SAT/Z3 result is promoted to an independently replayed proof certificate.

The 20-row finite exhaustion was independently programmed and run by me. It is an exact finite reproduction, not a formal/kernel proof or an independent-model-family review. No novelty judgment is required or made.

## 2. Complete read frontier, source pins and prior contacts

The complete f30 assignment was read FIRST. I then read all three candidate manuscripts completely through their endings, the full registered info-4 definitions, and the ACTUAL row arrays bound by the two source JSONs.
Live SHA256 values matched all supplied source pins:

| Input | SHA256 |
|---|---|
| A: row-repair manuscript,35LF | `6e510b87af2fdeb3f49de7c8df3c1843fcd80a35884a51ac4f85a2c7851f96cd` |
| B: six-row noncompletion manuscript,53LF | `2d8a43b008f5276dc15c85ab9e72d14844e63c591aa32101cd76974003331ea7` |
| C: row-share manuscript,54LF | `a1329d4e6425130128afda024e53e54f1dbf6f1877342a8381845c41b599db4f` |
| First underlying source, `frontier-20261028-search-run-02.json` | `5a941a6c3f6fa3b65a9f9d1972eb70e94c55b6cb11b72ee41baf7d3f4707be05` |
| Second underlying source, `frontier-20261028-row-dp-run-02.json` | `99ec9dc0b9970fbd282d07330cf03d3cc1d217fb3c2de2299759b9dfd3c69c29` |
| Registered `info-4-actual-rows-definitions-v1.md` | `37e2fcdd5df3e390b3ec4df73feda38344ea8ea9a35aae4d82be3b0e3afe8db4` |

The two source JSONs were read for their actual `rows` fields; my checker separately reads each whole source once as bytes and enforces the expected SHA before parsing.
I have substantial earlier Tuscan/linear-adjacency combinatorics and related-review exposure. This is not blind or an independent-model-family review. No old verdict, held result, author checker code, author output count or reported SAT result was used as a premise of my new checker.

## 3. Exact original definition and elementary endpoint consequences

The registered target is an11×11 array whose **each row is a permutation of the SAME labelled alphabet `{0,…,10}`**. For EVERY distinct ordered pair (a,b), exactly one row has b immediately to the right of a; for distance two, at most one row has b two positions to the right of a.
Both distances are LINEAR inside each row. There is no wraparound, Latin-column, cyclic/equivariant, symmetry-normalization or row-order requirement.

There are11·10=110 distinct possible ordered adjacency pairs. Each complete11-row table contributes11·10=110 linear adjacent positions. Thus a valid table has each possible directed adjacency exactly once, consistent with the registered exact-one clause.
For each symbol a, it occurs once in each of the11 permutation rows. It contributes an outgoing adjacency in all rows except those ending in a. Since its10 possible directed outgoing pairs occur exactly once, exactly one row ends in a. The incoming version shows exactly one row starts in a.
Consequently any two rows retained in a valid table must have different first symbols and different last symbols, in addition to no common D1 or D2 event.
This endpoint fact is a DERIVED necessary condition; no separate Latin-column condition has been inserted.

Rows can be arbitrarily reordered in the final table. A graph conflict between two row strings is independent of which final row slots they occupy. A proof about keeping a particular source slot is a narrower caller; the share theorem correctly permits arbitrary row-slot rearrangement.

## 4. First candidate: exact event graph and vertex-cover obstruction

Source A LF5–24 refers ONLY to the eleven rows in the first source JSON, SHA `5a941a6c…`.
My program checked all11 rows are actual permutations and rebuilt every linear D1/D2 event. Its actual counts are105 distinct D1 events out of110 and93 distinct D2 events out of99, so this near-candidate is NOT a witness.

Using only common events at the SAME distance, the independently recomputed row-index graph is exactly

`(1,2), (1,4), (1,10), (3,5), (3,10), (3,11), (5,9), (5,10), (5,11), (10,11)`.

If two endpoints remain unchanged in a repair, their shared actual event remains duplicated. Therefore any valid repair's changed-slot set must hit EVERY graph edge.

The author's lower bound can be independently reconstructed without trusting its subset loop:

- If slot1 is not changed, edges(1,2) and(1,4) force changes2 and4, while disjoint edges(3,10) and(5,9) require two more. Thus at least4 change.
- If slot1 changes, the triangle on3,5,10 needs at least two more changes. Choosing3 and10 leaves(5,9), requiring a fourth. Choosing3 and5 leaves(10,11); choosing5 and10 leaves(3,11). Either also requires a fourth.

I independently enumerated all562 index subsets of sizes0 through4. Exactly three size4 covers occur:

`{1,3,5,10}`, `{1,3,5,11}`, `{1,5,10,11}`.

The program also rebuilt both event layers on each complement and found no collision among its seven unchanged rows. Therefore those are EXACTLY the four-slot sets removing the **pre-existing frozen-row conflicts**, not proofs that the seven rows admit a completion.
A table retaining eight rows would change at most three slots, contradicting the lower bound. Other row sets/new arrays are not excluded.

## 5. Second candidate: endpoint/event conflicts and the unique six-row survivor

Sources B/C use ONLY the different second JSON, SHA `99ec9dc0…`.
My program checked all11 rows are permutations and directly obtained106 distinct D1 events and95 distinct D2 events. Thus this near-candidate is also NOT a witness.

From the full independent event+endpoint graph, the five pairwise-disjoint conflict edges are verified:

- (1,3): same first symbol4 and same last symbol6;
- (2,4): same last symbol3;
- (5,6): common D1 event `8→0`;
- (7,9): same first symbol10;
- (8,10): same last symbol7.

A valid table sharing candidate row strings cannot keep both endpoints of any such edge, so it must discard at least five of A's rows. If it keeps SIX, it discards exactly one from each pair and keeps row11.

The additional edges needed in source C are also independently present: (4,11) shares D2 `8→7`; (2,9) shares D1 `7→1`; (2,10) shares D1 `1→8`; (5,8) shares first symbol9; (1,6) shares D2 `10→5`.
Thus keeping11 forces discarding4/keeping2; keeping2 forces discarding9 and10/keeping7 and8; keeping8 forces discarding5/keeping6; keeping6 forces discarding1/keeping3.
The ONLY possible retained six-row set is

`{2,3,6,7,8,11}`.

Independently, I checked ALL1,024 changed-index subsets of sizes0 through5. The unique size-five cover is `{1,4,5,9,10}`; the complementary six-row set is the same. I separately checked all462 six-subsets for conflict-freeness, again yielding exactly that set.
These are explicit finite graph exhaustions, not assumptions that an independent set of six extends to a valid array.

## 6. The actual six rows and complete compatible-row exhaustion

The six rows in source B LF7–19 match the ACTUAL row strings at those one-based indices in the pinned second JSON exactly:

```text
6  9  2  4  7  1  8  5  0 10  3
4 10  7  2  1  0  3  5  9  8  6
8  0  2  9  6  1  3  7 10  4  5
10 8  1  4  6  2  5  3  9  7  0
9  1 10  2  0  4  8  3  6  5  7
3 10  0  8  2  7  5  6  4  1  9
```

I checked that these six have60 distinct linear D1 events,54 distinct linear D2 events, and six distinct starting and ending symbols.
The complete fixed start set is `{3,4,6,8,9,10}` and end set `{0,3,5,6,7,9}`.

A further actual row in ANY completion must be a permutation; must avoid the fixed rows' D1 and D2 event sets at their respective distances; and must start/end outside those two sets. These conditions are NECESSARY even though they are not by themselves sufficient for a full completion.

My independent prefix backtracker tries every unused symbol in each prefix, rejecting EXACTLY when a necessary fixed D1/D2 conflict or forbidden first/last symbol occurs. A full-length surviving prefix is an actual permutation satisfying all these necessary individual-row conditions.
Induction on prefix length proves completeness: any eligible row's first symbol passes the same test; at each later symbol its actual D1/D2 events are not fixed conflicts, and its final symbol is allowed. Therefore its unique prefix path is never pruned and is reported.

The independent run reports **20** eligible actual rows, saved explicitly in its result JSON. None contains `0→9` or `6→0`; neither of those events occurs among the six fixed rows.
The original EXACT-one adjacency requirement would force each missing directed pair to occur in one of the five remaining rows, yet every remaining row would belong to the exhausted 20-row list. Thus no full original T2(11) can contain those six.
Either missing pair alone is sufficient for this contradiction; both were checked.

The author's first enumerator reports2213 prefix nodes; mine reports2198. These are implementation-specific visited-prefix counts, not a scientific discrepancy: my implementation rejects a forbidden last symbol BEFORE recursively entering the terminal prefix, while the source's count convention is not a shared metric. The independently checked set of20 eligible rows and the two unsupported events are the load-bearing results. I did not rerun either author program or infer its exit code from mine.

## 7. Complete row-share conclusion, with both callers

If a valid full T2(11) contained six or more of the SECOND candidate's row strings, choose any six of them. They must be conflict-free under the necessary event+endpoint graph, so by §5 they would be the unique set `{2,3,6,7,8,11}`.
Section6 proves that exact set cannot occur in ANY full T2(11), independently of their eventual row order. Contradiction.
Therefore a full witness shares at most FIVE of those eleven actual labelled row strings.
If one additionally demands the original slots be kept, at least six slots must change. This slot-specific statement is a correct corollary, not a stronger global lower bound.

A different near-candidate, any array sharing at most five of these rows, a nonlocal repair or an unrestricted new construction is not excluded. The result does not require rows to be Latin in the columns or adjacency to wrap from the end back to the start.

## 8. Exact independent computation and mutation controls

I wrote `frontier-20261028-tuscan-independent-review-check.py` from the registered definition and the two pinned input paths. It imports NO author checker/solver code and reads each source file once as bytes, checking its exact SHA before parsing.
It validates all11 row lengths, integer ranges, permutation status and source-row distinctness, then separately recomputes events, conflict graphs, covers, six-subsets and the complete prefix search described above.

Actual command, with the two exact source paths given explicitly:

```text
python3 -B frontier-20261028-tuscan-independent-review-check.py \
  /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/frontier-20261028-search-run-02.json \
  /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/tuscan2-11/frontier-20261028-row-dp-run-02.json \
  --output frontier-20261028-tuscan-independent-review-results.json
```

Actual output: `INDEPENDENT_FINITE_RECONSTRUCTION`, first distinct `[105,93]`, first minimum cover4 with the three exact sets, second distinct `[106,95]`, 1024 cover subsets, one conflict-free six set,20 compatible rows,2198 independently visited prefix nodes, and unsupported adjacencies `[[0,9],[6,0]]`.
Three in-memory targeted corruptions were rejected for their intended reasons: duplicate symbol in a row, out-of-range symbol, and duplicate source rows.

Checker SHA256 `982060803ff52fa40373ad1d237191753050c259f97e216f5a85207d37d49134`; complete result SHA256 `dc548e8be586bc3b68fd650fa82f5b098ce934e50325c7ab4e981166304b8b12`.
The saved result lists all20 eligible rows, complete conflict edges, actual six-row input and mutation outcomes. The program's input bindings agree with the source manifests. All arithmetic and event checks are exact integers/sets.

I did NOT run or replay the author's SAT model, Z3, or SAT certificate. The author's UNKNOWN timeout remains UNKNOWN; SAT UNSAT without proof replay is not the basis of my verdict. My distinct backtracker independently verifies the finite combinatorial obstruction.

## 9. Separate judgments, limits and return

| Claim | Judgment | Boundary |
|---|---|---|
| First candidate event graph / minimum four changes | Supported by independent graph rebuild, analytic lower bound, and all562 subsets | Original slots; eliminating existing collisions is only necessary for completion |
| Three exact minimum four-slot sets | Supported by exhaustive finite cover check | Not an existence claim for the corresponding repairs |
| Six specific rows and20 eligible next rows | Supported by direct source-byte binding and complete independent prefix exhaustion | D1/D2 linear and endpoint checks; no symmetry/column/wraparound assumption |
| Missing `0→9`, `6→0` | Both verified absent from fixed rows and every eligible next row | Proves ONLY that specified six cannot extend |
| At most five shared second-candidate rows | Supported by actual conflict graph/unique six set and six-row obstruction | Row order arbitrary, same labelled alphabet; not a global T2(11) no-go |
| Original unrestricted T2(11) | **NOT_ESTABLISHED** | No actual full witness or universal impossibility proof supplied |

All prior source/failure/quarantine records retain their historical states; this review does not retrospectively validate them. It uses the newer authorized bounded checks and factual source definitions, not stopped assessments as accepted premises.
No external model/paid API, author contact, nested agent, Git push, deletion, publication, secret or infrastructure mutation was used. Novelty and independent-model/human/formal acceptance remain unassessed.

**FINAL: 0 FATAL / 0 MAJOR / 0 MINOR — NO_SUBSTANTIVE_DEFECT AT THE THREE LOCAL SCOPES.**

**END OF COMPLETE f30 REVIEW.**
