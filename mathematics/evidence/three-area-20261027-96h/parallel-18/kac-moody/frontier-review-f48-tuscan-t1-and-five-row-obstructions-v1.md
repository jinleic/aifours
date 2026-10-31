# f48 Tuscan review — universal T1 row rigidity and two exact candidate-specific exclusions

Reviewer **MathKacMoody-2**, original math-3; author **InfoRecursiveMDS18-2**, original info-4. Actual native `/bin/date` BEFORE this new review write: **Wed Oct 28 17:38:43 PDT 2026**. Precreation observation only.

## 0. Verdict and exact limits

**NO NEW MATHEMATICAL FATAL, MAJOR OR MINOR at the stated scopes.** The universal one-row T1 rigidity proof is reconstructed below. For the two named, distinct11-row candidates I independently replayed the COMPLETE finite enumerations—not only a subset—using new code that does not import any author program or result.

- For candidate A (the T1/15-collision array), every T1 array changing at most three of its exact row strings has distance-two pair-collision score at least15. Thus no T2(11) can share eight or more of those strings, up to row reordering.
- For the DIFFERENT candidate B (the score-8 array), no T2(11) on the same labelled symbols can contain five or more of its exact row strings. Any such T2 must have at least seven new row strings relative to B.

These are candidate-specific negative results, NOT an unrestricted T2(11) no-go, an actual T2 witness, a theorem after arbitrary symbol relabeling, or a global distance-two lower bound. The universal lemma concerns T1 arrays themselves, not arbitrary non-T1 arrays.

**One previously disclosed DOCUMENTARY MINOR is carried, not a new mathematical defect:** the five-row report's helper SHA was incorrectly expanded. Its additive erratum `d432daea706e7fff3333aaf1d8d1314de3bd2f26d99f5c8a02d2c418b8111089` gives the corrected `1e7980a4d344f3e66f222395bd1fbf1211ac158b7dd34840d5cfc991f75b0c6c`; my live metadata hash matches the correction. The author's frozen report is unchanged. My scientific replay did not run or import that helper.

## 1. Actual inputs, prior familiarity and exact independent replay

I read the COMPLETE `f48-tuscan-t1-and-five-row-obstructions/assignment-v1.json` FIRST, then both complete candidate bodies:43LF `f55aeffec2579fee4e43a829c1c200802df882bef8a44643f97d576a4e3e36ec` and53LF `7a60a10c843bf900665a99875e14c1e471a6a8473d304594a89adf24f64f8890`, and the complete13LF mandatory SHA erratum `d432daea...`. All three live hashes matched.

I also read the COMPLETE registered info-4 definition `info-4-actual-rows-definitions-v1.md`, SHA256 `37e2fcdd5df3e390b3ec4df73feda38344ea8ea9a35aae4d82be3b0e3afe8db4`. Its literal definition requires11 permutation rows; each ordered distinct-symbol pair appears exactly once at LINEAR distance1 and at most once at LINEAR distance2. It does NOT impose wrap, Latin columns, a cyclic/equivariant ansatz or a preselected row set. The supplied modern primary-source transcription is not a fresh book-page or current-openness certification.

I have earlier same-harness Tuscan/source and other research exposure. This is a serial disjoint review, not a blind/independent-model-family review or a cognitive-unaffectedness certificate. No author contact, old quarantined/held graph guide, author search result or candidate code was used as a proof premise. Candidate row strings themselves are the literal objects under review, not inferred from old held material.

### Actual newly executed verification

I wrote an independent standard-library exact-integer program `frontier-review-f48-independent-replay.py`,212LF/8898B, SHA256 `c8fbbb5f8f1a5493ce6784ebae718c2b9147dec9a6c9e2afacb55c73d04575d2`. It hard-codes ONLY the two source-specified row arrays, independently validates the full event counts, enumerates residual sentinel Hamilton paths directly for all row pairs/triples, and builds a separate bitset MRV exact-cover tree for every compatible five-subset. It does not import an author helper, source program, output JSON, optimizer or finite solver.

Actual command/output from my exclusive root:

    python3 frontier-review-f48-independent-replay.py
    PASS: A D1/D2 110/84, B D1/D2 106/95; all 55 pairs/165 triples; 15 compatible five-subsets exhausted; no completion
    pair decompositions 65 triple first cycles 6404 triple decompositions 534 min D2 15
    frontier-review-f48-independent-replay-v1.json

The process exited0; reported wall time2.34 seconds, actual post-run clock **17:38:06 PDT**. The new2371LF/45093B output JSON has SHA256 `42c2b12bc980fb72d9b71e2751500dc800888d9fd548584679d10a50c42a43d1`. It retains all165 triple cases and every fixed-five result. Independent replay is separate implementation of the same finite mathematics, not a formal proof certificate or external-model review.

## 2. Registered object and universal T1(n) rigidity

For n>=1, take n rows, each a permutation of the SAME n labelled symbols. A T1(n) array has no repeated directed adjacent pair at LINEAR distance1. Each row contributes n−1 events; total events are n(n−1), equal to the number of ordered pairs of distinct symbols. Thus every such pair occurs EXACTLY once. No end-to-start edge is included in this counting.

Suppose two T1 arrays agree in every row position except one. The unchanged rows have the same event set; because both full arrays use the entire directed-pair universe exactly once, the missing row must have exactly the same set of n−1 directed arcs in each array. For n>=2 those arcs form a directed Hamilton path: one vertex has indegree0 within the path, each nonterminal vertex has a unique outgoing arc, and following those arcs uniquely recovers the row string. For n=1 the sole permutation is unique. Therefore a one-row replacement is necessarily identical.

This proves the author's universal lemma at its exact scope, independently of either candidate, an optimization run, column constraints, or a cyclic interpretation. The statement is about one changed row position; arbitrary row-order changes are addressed separately by matching retained strings.

## 3. Candidate A: actual starting table and complete sentinel reduction

I copied the eleven source-specified candidate-A rows into the new verifier and verified that each is a permutation of0,...,10. Recomputing ONLY linear events gives:

    distance1: 110 events, 110 distinct, 0 pair collisions;
    distance2:  99 events,  84 distinct, 15 pair collisions.

The pair-collision score is sum over directed events of binomial(multiplicity,2), not a wrap score. This agrees with candidate A and establishes it is T1 but not T2.

In EVERY T1(n), each symbol starts exactly one row and ends exactly one row. For a fixed symbol, all n−1 distinct outgoing directed arcs are used. Across n permutation rows the number of outgoing occurrences equals n minus the number of rows ending at that symbol, so there is exactly one ending row. The incoming count similarly gives one starting row.

Add a fresh sentinel vertex to each row with sentinel→first and last→sentinel. Each augmented row is a directed Hamilton cycle on n+1 vertices. Its other edges are EXACTLY the original linear adjacent edges. The cycles are edge-disjoint, including sentinel edges, because starts and ends are unique. Conversely, any partition of a chosen residual augmented arc set into Hamilton cycles gives the SAME number of replacement permutation rows with exactly the required linear distance1 arcs and endpoints. The sentinel is a bookkeeping device: distance2 is ALWAYS scored only inside the original linear rows, with no boundary/wrap events.

For a specified pair of removed rows, the residual is two-in/two-out at every vertex. My code enumerates EVERY Hamilton cycle rooted at sentinel by direct depth-first path recursion; after removing it, it checks that the unique one-outgoing complement is ONE Hamilton cycle, visiting all12 vertices. The two cycles are sorted to discard only row interchange. This direct DFS is independent of the author's alternating-bipartite-cycle matching implementation. Across all55 pairs it found exactly65 unordered Hamilton decompositions and minimum D2 collision score15.

For a specified triple, my code enumerates EVERY first residual Hamilton cycle, then EVERY second Hamilton cycle of its remaining arcs, and tests the unique last complement as above. Lexicographic row ordering removes ONLY the six permutations of the same unordered triple. Across all165 triples it found6404 first-cycle enumerations and534 unordered full decompositions. Recomputing the complete same-table linear D2 score for each gives minimum15. The output retains per-triple counts/minima, not merely the aggregate.

The original array itself attains15. Cases changing zero, one or two rows are also included by selecting enough unchanged slots among a triple; the one-row universal lemma gives an independent special check. Therefore the exact minimum in the at-most-three-row T1 neighborhood is15. Any T2 sharing at least eight of A's eleven exact strings may be row-reordered to keep those eight positions, hence would be such a T1 neighbor with D2 score0, a contradiction. This does not rule out an array sharing at most seven strings or one whose labels are first changed.

## 4. Candidate B: original five-string constraints and exhaustive completion

For the separate source-specified candidate B, independent row-permutation and linear-event reconstruction gives106 distinct D1 events out of110, 95 distinct D2 events out of99 and **eight pair collisions in total**. It is a nonwitness. Nothing from A's T1 trade exhaustion is assumed to apply to B.

There are C(11,5)=462 five-subsets of B's exact labelled row strings. A prospective T2 containing any chosen five must satisfy, within those five, no duplicate D1 event, no duplicate D2 event, and no duplicated start or end symbol. The start/end requirement follows from the T1 universe count proved above; it is a NECESSARY condition for a completion, not an added Latin condition. My independent program checks ALL462 subsets and obtains exactly the15 compatible sets listed in the author's table; the other447 fail at least one necessary condition.

For each of the15 fixed sets, I independently generate every possible permutation row by depth-first prefix extension. An extension is pruned ONLY when a newly formed linear D1 or D2 event conflicts with the FIXED rows or its starting/ending symbol is already used. Each surviving row records exact bitsets of its D1/D2 events and start/end. These filters do not require pairwise compatibility with other prospective rows; that is enforced later. Every row of a valid completion appears in the generated list.

The fixed rows occupy50 distinct D1 arcs. Exactly60 directed nonloop arcs are missing. My solver chooses an uncovered arc with the fewest currently compatible candidate rows, and branches over EVERY row containing that arc. It rejects a row only for a D1/D2 collision or a repeated start/end with a previously chosen row. Every valid completion must contain one branch row for the selected arc; after a row is chosen the same argument recurses. If the missing set is empty, exactly six extra rows have been chosen because each contributes ten disjoint D1 arcs. If an uncovered arc has no compatible row, that branch is impossible. The finite tree has no time cutoff and no unexamined branch in the reported result.

All15 trees exhausted with NO completion. My independently generated eligible-row and search-node counts match every row of the author's table (for example436/37 for IDs1,2,5,7,11 and711/13 for2,3,6,8,11); the other rows are explicitly in the pinned JSON. Consequently no T2 can contain even five B strings, since any larger shared set contains a forbidden five-subset. At least7 of its11 row strings must be new relative to B. No unique-symbol relabeling invariance, extra column rule or arbitrary five-row universal theorem is inferred.

## 5. Separate verdict and import ledger

|Claim|Verdict|Exact dependence / limit|
|---|---|---|
|T1(n) one-row rigidity|SUPPORTED WRITTEN|All n>=1, linear D1, row permutations; n=1 handled separately|
|Candidate A actual T1 and D2=15|SUPPORTED BY INDEPENDENT EXACT REPLAY|Literal A rows; 110/110 D1 and84/99 D2, pair-collision definition|
|All <=3-row T1 neighbors of A score>=15|SUPPORTED BY INDEPENDENT EXACT REPLAY|All55 pairs and165 triples, full sentinel arc partitions; no wrap|
|No T2 sharing >=8 A strings|SUPPORTED conditional on the replayed finite enumeration|Same labelled strings, arbitrary row order; no unrestricted no-go|
|Candidate B actual D1/D2 score8|SUPPORTED BY INDEPENDENT EXACT REPLAY|Different literal B rows; 106/110 and95/99, not T1|
|15 compatible 5-subsets out of462|SUPPORTED BY INDEPENDENT EXACT REPLAY|D1/D2/start/end are necessary conditions, all subsets examined|
|No T2 sharing >=5 B strings|SUPPORTED BY INDEPENDENT EXACT REPLAY|Every compatible five-subset; independent eligible-row DFS + full exact-cover tree, no cutoff|
|Author helper SHA citation|PRIOR DOCUMENTARY MINOR, ADDITIVELY CORRECTED|Corrected actual helper SHA `1e7980a4d344...`; my program did not import or run it|
|Original T2(11) existence/nonexistence, symbol-relabelled neighborhoods, novelty|OPEN / NOT CLAIMED|No fixed candidate-row exclusion becomes an unrestricted theorem|

Every finite claim above relies on the actual literal candidate rows, the shown enumeration-completeness argument and the newly run program. The bounded computation is reproducible but is not a formal/kernel certificate; reviewer and author share the elementary exact-cover mathematical characterization even though their implementations are separate. Main must read the complete source/review and assess the actual program/output scope before adopting.

No FATAL/MAJOR/MINOR mathematical finding was identified. The existing corrected helper-SHA documentary error remains recorded separately, not silently edited or counted as new evidence of a theorem error. Source-wide novelty, independent human/configured-family/executable certification beyond the exercised runs and the original target remain unclaimed.

## 6. Process, scope and return

The earlier source-policy, STOP/quarantine and owner/reviewer findings remain historical; no held result is promoted, no prior process incident is cured and no clean-private-cognition census is asserted. This review used ordinary exact integer computation as prospectively authorized, with no external model/paid API, author contact, Git push/publication, deletion, infrastructure mutation or secrets. I did not resume my own Kac primary during this priority review. After ACTUAL RETURN I continue that primary under the current frontier direction; no continuous-service claim follows.

**END OF COMPLETE f48 REVIEW — BOTH ROW-REUSE RESULTS ARE CANDIDATE-SPECIFIC.**
