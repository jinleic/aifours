# Actual T2(11): singleton transport and opposite-join constraints

**Status: AUTHOR WRITTEN CANDIDATE, not independently reviewed or parent-disposed.** The original T2(11) existence question remains open here. The strongest new proposed result is that, under the *simultaneous* hypotheses `M=C` and two distinct tripled odd-position supports, the T=14 branch has exactly two joins in each direction for **each** opposite-cell pair. In particular its previously surviving family-sum pair (7,7) is impossible. The proof uses the same labeled twelve-vertex Hamilton cycles and their directed squares, not separate schedule projections. For T=13, an extreme 4:1 opposite-join orientation forces a specific actual zero-full bridge row and a two-full minority-join row; consequently it cannot occur in the (4,0,0,0,0) full-count pattern. A further exact singleton-neighbor law holds in both branches.

## Scope, provenance, and method

This is conditional: assume an actual T2(11), equality of the original missing distance-two set with the actual last-to-first closing set, and two distinct six-symbol odd supports each used by three rows. We do not prove any of these assumptions and do not assert a witness or nonexistence in the unrestricted problem.

Before mathematical derivation I read the entire assigned manifest and freeze receipt, the parent predispatch metadata, the actual dispatch receipt, and all listed status-only controls through their endings. I sent the direct prebody ACK, then read the complete literal packet in ordered raw windows of at most 20 LF, including its last line. The three allowed source bodies are S1, S2 and S3 in that packet, with hashes and line ranges fixed by the manifest and freeze receipt. The packet's historical reviewer/run descriptions are source statements, not new verification by me. I did not follow its links, read sibling work, or import held science or its consumers. Fresh case analysis below is mine, not an independence or cognitive-isolation certification.

No child scientific executable, calculation program, solver, build, lint, test, or formatter was run. The finite source named below was **written but NOTRUN**. Its displayed hypothetical controls are definitions, not observed results. No external source or novelty search was used. Observed native clock before composition: 2026-10-30T15:16:49-0700 PDT.

## Imported interface and notation

Take the eleven actual rows, append the same infinity to each, and call the resulting connected directed twelve-cycles `P_i`. The 132 directed adjacency arcs are partitioned by these cycles. Only under `M=C`, their directed squares also partition the 132 directed arcs. A square arc of `P_i` is the ordered pair from a vertex to its second successor in the **same** `P_i`. All vertices are labeled and shared between cycles.

The S1/S2 conditional interface supplies the following necessary facts. For the two tripled supports the four cells `I,J,K,L` each have size three; `I,L` and `J,K` are the opposite pairs. Six alternating actual cycles leave five residual actual cycles. In the T=13 branch all five are regular; each cell has one length-three run and four length-two-plus-singleton occurrences. In T=14 one residual cycle `h` alternates among the cells in an `I,J,L,K` orientation repeated three times, and the other four are regular; each cell has two full length-three runs and two length-two-plus-singleton occurrences across those four. Each regular cycle has exactly one join between each opposite pair. Both endpoints of such a join belong to nontrivial runs in their own cells. The regular full-cell counts are `0,2,4`; a two-full mask consists of adjacent, not opposite, cells. In T=13 the global regular full-count patterns are `(4,0,0,0,0)` or `(2,2,0,0,0)`; in T=14 they are `(4,4,0,0)`, `(4,2,2,0)`, or `(2,2,2,2)`.

Every one of the six directed internal arcs of each three-vertex cell occurs in the residual cycles; in T=14 `h` has no internal-cell adjacency, so all six occur in the four regular cycles. Neither of the six alternating B/D cycles contributes a square arc in either direction between opposite cells. For each opposite pair, `h`, when present, contributes three square arcs in each direction. These are imported *necessary* facts, not an assertion that any surviving collection exists.

For any opposite pair write its cells `A,B` and the other pair `C,D`. If a regular cycle joins `A` to `B`, it has a physical segment

`A_p -> A_x -> B_y -> B_q`, with `p != x`, `y != q`.

Its two square arcs `A_p -> B_y` and `A_x -> B_q` are distinct and point in that same `A -> B` direction. A reverse join has the analogous segment `B_p -> B_y -> A_x -> A_q`. These are arcs of the actual cycle, not independent choices.

## Theorem 1: every regular singleton transports an opposite pair

**Claim.** In both T=13 and T=14, every vertex which is a singleton cell-run in a regular residual cycle has predecessor and successor in the *two opposite cells of the other pair*. Thus an I- or L-singleton is between a J and a K, in one order or the other, and a J- or K-singleton is between an I and an L.

**Proof.** For a square arc from A to B whose intermediate vertex lies in A, the second edge is an actual A-to-B join, and the square is the first of the two arcs displayed above. If its intermediate vertex lies in B, it is the second displayed arc. All other A-to-B square arcs have intermediate vertex in C or D; that vertex is a singleton of its own cell. The same statement holds with directions and opposite pairs reversed. One singleton occurrence has exactly one predecessor and successor and therefore can supply at most one such opposite-pair square arc.

For T=13, each opposite pair has 18 directed square arcs in total, all on the five residual cycles. Their five joins supply ten, leaving eight singleton-centered arcs per pair, 16 over the two pairs. There are exactly `4*4=16` singleton occurrences. For T=14, subtract h's six square arcs per pair: the four regular cycles supply 12 square arcs per pair. Their four joins supply eight, leaving four singleton-centered arcs per pair, eight total. There are exactly `4*2=8` regular singleton occurrences. All square arcs mentioned are distinct on the same decomposition. Hence the injection from the required centered arcs into the singleton occurrences is a bijection. For a singleton of A or B, the opposite endpoints cannot include its own cell and must consequently be one in C and one in D. The other case is symmetric. ∎

### Consequent actual cell-word grammar

Join each pair of nontrivial opposite-cell runs into its physical block. In a regular cycle with four, two, or zero full cells the two blocks have lengths `(6,6)`, `(5,5)`, or `(4,4)` respectively. Let their cell words be `A...A B...B` and `C...C D...D`, where `A,B` and `C,D` are opposite and the written orders are the directed join orientations.

The singleton-neighbor law gives, with cyclic gaps between the blocks:

* With **two** full cells, the two singleton vertices are consecutive in one gap, the other gap is empty. If they occupy the A/B-to-C/D gap their cell word is `D,A`; if the other gap, it is `B,C`. Their two centered opposite square arcs both point **opposite** the corresponding opposite joins.
* With **zero** full cells, either all four singleton vertices are consecutive in one gap, or each gap contains two consecutive singleton vertices. Call these **grouped** and **split**, respectively. In the grouped case their centered arcs give one in each direction for each opposite pair. In the split case they give two in the direction opposite the corresponding join for each pair.

To see this without enumeration of labeled cycles, follow a singleton chain: its neighbors must be opposite. Starting immediately after a block ending in B, if the first singleton has cell S, the successive cell labels are `B,S,A,opposite(S),B,S,...`; the other block starts in C, which lies in the other opposite pair. Therefore one or three singletons in a gap are impossible; two give `D,A`, and four give `C,A,D,B`. The reverse gap is symmetric. The two/full-cell case has exactly two singletons, and the zero/full-cell case has four. All these statements concern the cell words of the same actual cycles.

## Theorem 2: T=14 forces 2:2 directed joins

**Claim.** In T=14 each opposite pair has exactly two regular joins in each direction. In S1's notation, if `x,y` are the two I/L directed join totals of the B-family and `u,v` those of the D-family, then

`x=y`, `u=v`, `x+u=7`, and the family run-sum pair is `(6,8)` or `(8,6)`; `(7,7)` is excluded.

**Proof.** Fix an opposite pair A,B. Write the three h-square arcs from A to B as a bijection `F:A -> B`, and the three in reverse as `G:B -> A`. Because h is one twelve-cycle with cell word `A,C,B,D` repeated, `G F` is a three-cycle on A. Identify A_i with B_i=F(A_i), for i=1,2,3. Then G is one of the two three-cycles on those indices.

The imported square budget says the numbers of regular A-to-B and B-to-A joins are each in `{1,2,3}` and sum to four. Suppose three joins point A-to-B and one in reverse. The three high-direction joins contribute six different A-to-B squares, necessarily exactly the six entries of the `3 x 3` matrix outside F. Each high join pairs two such entries with different source vertices and different target vertices. Their A-internal arcs are distinct, as are their B-internal arcs. Since each vertex occurs in exactly two of the six off-F entries, these three internal arcs form a tournament on each three-vertex cell: they contain exactly one arc from each unordered pair.

Neither tournament can be cyclic. In a cyclic tournament, extending any of its edges to a directed three-vertex path needs one of the other two tournament edges. Those edges already belong to different high-join cycles. Thus no high-join cycle could contain a full run of that cell; but the cell has two full runs and there is only one low-join cycle. Both tournaments are therefore transitive.

Partition the six off-F matrix entries into the three two-entry square pairs. The row pairs and column pairs must each be the three different unordered pairs. There are exactly four partitions. Indeed, the pair involving source rows 1 and 2 can be `(12,21)`, `(12,23)`, or `(13,21)`; the first has two completions and each of the others one. One partition is the three reciprocal pairs `(12,21),(13,31),(23,32)`. There each high adjacency is a matching edge `A_i -> B_i`. These three adjacencies must be distinct; every i is used once, so the A-internal tournament has indegree one at each vertex and is cyclic, contradiction.

The other three partitions are equivalent by a common relabeling of A and B. Take

`Q0=(12,21), Q1=(13,32), Q2=(23,31)`,

where `ij` means the square arc `A_i -> B_j`. For a pair, its two entries can be assigned to the two squares of the join in either order. Label those choices 0 and 1 by the following four-vertex segments:

| pair | choice 0 | choice 1 |
|---|---|---|
| Q0 | `A2 A1 B1 B2` | `A1 A2 B2 B1` |
| Q1 | `A3 A1 B2 B3` | `A1 A3 B3 B2` |
| Q2 | `A3 A2 B1 B3` | `A2 A3 B3 B1` |

If Q1 and Q2 both use choice 1, both joins are the same adjacency `A3 -> B3`, impossible. With at most one of them using choice 1, direct reading of the three internal arcs gives:

| choices `(Q0,Q1,Q2)` | obstruction |
|---|---|
| `(0,1,0)` | A tournament cyclic |
| `(1,1,0)` | B tournament cyclic |
| `(0,0,1)` | B tournament cyclic |
| `(1,0,1)` | A tournament cyclic |

The remaining `(0,0,0)` and `(1,0,0)` are interchanged by swapping indices 1 and 2, with Q1 and Q2 exchanged. Hence assume the three high segments are

`r0: A2 A1 B1 B2;  r1: A3 A1 B2 B3;  r2: A3 A2 B1 B3.`

The fourth regular cycle joins B to A. Physical full runs now force its A-internal edge to be `A1 -> A2`: the remaining A edges are `1->2,1->3,2->3`. Row r0 cannot be A-full, since its needed predecessor edge `3->2` already occurs in r2. If the low edge is `1->3`, r2 cannot be A-full and the low row cannot be A-full (it would need `3->2`); only r1 could be full. If the low edge is `2->3`, r1 cannot be full and the low row cannot be full (it would need `3->1`, already in r1); only r2 could be full. Both contradict the two actual A-full runs.

Similarly the low B-internal edge must be `B2 -> B1`. The remaining B edges are `2->1,3->1,3->2`; r0 cannot be B-full because `2->3` occurs in r1. If the low edge is `3->1`, r1 cannot be B-full and the low row cannot be B-full because it would need `2->3`; if it is `3->2`, r2 cannot be B-full and the low row cannot be B-full because it would need `1->3`. Each leaves at most one B-full row.

The low join is therefore the physical segment `B2 B1 A1 A2`. Its B-to-A square arcs are `B2 -> A1` and `B1 -> A2`. One is already in G whether `GF` is `(1 2 3)` or `(1 3 2)`. This repeats a directed square arc on two actual cycles, contradiction. Reversing A and B excludes the 1:3 case. Thus only 2:2 remains. ∎

For the stated family consequence, the four regular directed join counts are, in S1's notation, `9-x-u, 9-y-v, 9-x-v, 9-y-u`. Each is now 2. Thus all four cross sums are 7, implying `x=y`, `u=v`, and `x+u=7`. Each family run sum `x+y` or `u+v` is even. S1's T=14 permitted pairs `(6,8),(7,7),(8,6)` therefore reduce to `(6,8),(8,6)`.

### T=14 joint cell-word consequences

These are simultaneous requirements on the four physical regular cycles, in addition to 2:2:

* For `(4,4,0,0)`, the two zero-full cycles are either **both grouped** or **both split**. If split, their joins are oppositely directed to one another in both opposite pairs, and so are the joins of the two four-full cycles. A grouped/split mixture would give odd singleton-square totals in each direction, whereas the exact 2:2 budget requires two in each.
* For `(4,2,2,0)`, if the zero-full cycle is grouped, the two two-full cycles have opposite join directions in each pair and the four-full and zero-full cycles also have opposite directions. If it is split, the two two-full cycles have the same join directions, opposite to the zero-full cycle, and the four-full cycle has the same join directions as the zero-full cycle. Both pairs are constrained in the same named cycles.
* For `(2,2,2,2)`, put signs `s=+` for I-to-L and `t=+` for J-to-K. The actual two-full mask is one of `{J,L},{I,K}` when `s=t`, and one of `{I,J},{L,K}` when `s!=t`. If each of the first two opposite masks occurs `x` times, `x` is 0, 1, or 2 and the numbers of rows with sign pairs `++`,`--`,`+-`,`-+` are respectively `x,x,2-x,2-x`.

Proof: apply the cell-word grammar. In a two-full row each pair's singleton contribution is one opposite its join; in a split zero-full row it is two opposite; in a grouped row it is one in each direction. The exact 2:2 join result makes each direction's required singleton total two. The last mask assertion follows because the two singleton cells are either `D,A` or `B,C` for the actual join orientations; the sign-pair counts then use both 2:2 margins. These statements do not imply compatible vertex labels or a full array.

## Theorem 3: actual 4:1 rigidity in T=13

**Claim.** Fix an opposite pair A,B in T=13. If four regular joins point A-to-B and the fifth points B-to-A, then:

1. The unique square arc A-to-B not supplied by the eight squares of the four high joins is `z_A -> z_B`, where `z_A` is the common endpoint of the low row's A-internal join edge and the other, unassigned A-internal edge, and `z_B` is defined analogously. These two internal edges in each cell cannot be reversals of one another.
2. The cycle containing `z_A -> t -> z_B` has a **high** A-to-B join, has no full cells, and has all four singleton vertices consecutive. It is uniquely identified among the high rows by the requirement that both its selected internal edges omit `z_A,z_B`.
3. The low B-to-A join cycle has exactly one of A,B full. Consequently it has exactly two full cells, and its other full cell lies in the other opposite pair.

**Proof.** In each of A,B the five joins use one distinct internal arc in each residual cycle; the only sixth internal arc is the other edge of that cell's unique full run. Call the selected internal edge of the low join `ell` and the sixth edge `e`. The eight high-join squares are distinct. Their number with a specified A source vertex equals that vertex's undirected incidence among the four high selected A-internal arcs and is at most three. The complete directed three-vertex graph has incidence four at every vertex, so `ell` and `e` cannot be the two reversals of one unordered edge: their absent third vertex would have high incidence four. They use different unordered edges and share exactly one vertex `z_A`. Hence the eight squares have A-source degrees `(2,3,3)`, the degree-two vertex being `z_A`. The same argument gives `z_B` on the B side. The sole missing A-to-B square is therefore `z_A -> z_B`.

No alternating-family cycle supplies this square. Its intermediate vertex t cannot lie in A or B, since such a square would be one of the two squares of an A-to-B join. It is thus a C- or D-singleton on one of the five residual cycles. Suppose that cycle is the low join `B_p -> B_y -> A_x -> A_q`. Because `z_A` is incident to the low A edge, but cannot be x (x has successor q rather than t), `z_A=q`. Likewise `z_B=p`. The cycle would contain the closed five-cycle `B_p -> B_y -> A_x -> A_q -> t -> B_p`, impossible inside a connected twelve-cycle. Thus the bridge row is one of the four high rows.

In that high row `A_p -> A_x -> B_y -> B_q`, neither `p` nor `x` can equal `z_A`, and neither `y` nor `q` can equal `z_B`, because `z_A -> t -> z_B` has different actual neighbors. They are the third vertices of their cells. They are singleton runs: if A were full its third vertex would precede p and could not also precede t; if B were full its third would follow q and could not also follow t. Cell t is also nonfull. Since full counts are 0, 2, or 4 and two-full masks cannot be the remaining opposite pair C,D, the bridge row is zero-full. It has three consecutive singletons `z_A,t,z_B`; by Theorem 1's grammar it is grouped, with all four singletons consecutive.

Exactly two high A-internal edges omit `z_A`, and exactly two high B-internal edges omit `z_B`. The bridge row is in their intersection. If two high rows lay in that intersection, their A-internal edges would be reversals and their B-internal edges also reversals; their two contributed square arcs would be identical, contrary to square uniqueness. Hence the intersection has exactly one row, the bridge row.

It remains to locate the full cells. Label `z_A=A3`, `z_B=B3`, and relabel the other vertices so the bridge row is `r0: A2 A1 B2 B1`. Its square entries are 11 and 22, and the only missing matrix entry is 33. Let r1 be the other high row whose A-internal edge omits A3, and r2 the other whose B-internal edge omits B3; they are distinct. Partitioning the remaining six matrix entries into their two-square contributions forces exactly one of the following four cases, where juxtaposition is an actual directed segment:

| case | r1 | r2 | fourth high row r3 | cell full in the low row | possible row of the other full cell |
|---|---|---|---|---|---|
| X1 | `A1 A2 B2 B3` | `A2 A3 B1 B2` | `A3 A1 B1 B3` | A | B in r1 or r3 |
| X2 | `A1 A2 B2 B3` | `A2 A3 B1 B2` | `A1 A3 B3 B1` | B | A in r1 |
| Y1 | `A1 A2 B3 B1` | `A3 A1 B1 B2` | `A3 A2 B2 B3` | B | A in r2 or r3 |
| Y2 | `A1 A2 B3 B1` | `A3 A1 B1 B2` | `A2 A3 B3 B2` | A | B in r2 |

For completeness, the two possible partitions after r0 are

`(12,23),(21,32),(13,31)` and `(13,21),(12,31),(23,32)`.

The first pair is assigned to r1, the second to r2, and the last to r3. Distinct internal arcs force the r1 and r2 orientations shown; r3 has the two shown orientations. The final two columns follow by using all six internal arcs once, requiring exactly one full run per cell, respecting the join's directed endpoint, and remembering that r0's A and B vertices A3,B3 are singletons. For example, in X1 the A edges left after the high rows are `1->3,3->2`; no high row other than r0 can extend to a full A-run and r0 cannot, so the low row uses `1->3->2`. The other three cases follow by the same explicit edge check. The table lists necessary possibilities only, not claimed realizations. In every case exactly one of A,B is full in the low row. Since the full-cell count is 0,2,4 and the other opposite cell is nonfull, it is exactly 2. ∎

**Consequence.** In the T=13 `(4,0,0,0,0)` pattern no regular row has two full cells, so neither opposite pair can have a 4:1 directional split. The imported `1..4` bounds then force both opposite pairs to have directed counts 2:3 or 3:2. In the `(2,2,0,0,0)` pattern, a 4:1 pair's unique low row is one of the two two-full rows, and its uniquely determined high bridge row is a grouped zero-full row. This is not a contradiction for every T=13 pattern.

A further exact cell-word constraint in the `(4,0,0,0,0)` case follows from Theorem 1. Let `s_F` denote the sign of the four-full row's join in one opposite pair, and sum the signs of the grouped zero-full rows for that pair. Equality of the nine square arcs in each direction gives `s_F + sum(grouped signs) = 0`. Thus the number of grouped zero-full rows is odd, namely one or three. This holds separately for the two opposite pairs on the same row classification.

## Prospective local checker, not run

`t14-opposite-join-local-enumerator-v1.py` is a complete, standard-library, no-file/no-network finite source prepared for possible **parent** audit and a named one-shot GO; it has NOT been run or syntax-checked by the child. It constructs two actual connected h cycles realizing the two orientations of `GF`, enumerates the three high `A_p A_x B_y B_q` segments and one low segment on shared labels, checks all six off-F A-to-B squares, the low squares against h, all internal arc uniqueness, and exactly two physically extendable three-vertex runs per cell. It fixes F by simultaneous relabeling and treats the three high rows as an unordered combination; those symmetries do not drop any putative actual configuration. It deliberately omits the other six cycles, global adjacent/square budgets, and most other-cell arcs: this is a **necessary local relaxation**, never an array enumerator.

The source includes an explicit locally positive fixture when the h reverse-square exclusion is dropped, and requires that this fixture collide with both possible h reverse matchings. It reports counts, not a claimed result, and prints `INCOMPLETE` if its cooperative 40-second limit is reached. The parent must inspect the entire source, its symmetry/completeness argument and controls, freeze its exact bytes and resource/receipt requirements, and decide whether to authorize execution. Zero, a positive count, a timeout, or any output is not asserted here. The written proofs stand or fall on independent review, not on an unobserved execution.

## Exact unpaid frontier and gates

* T=14 still has `(6,8)` and `(8,6)` family-sum branches and all three stated full-count patterns, subject to the new 2:2 and synchronized word constraints. No complete labeled packing of the eleven cycles and their two decompositions is constructed or excluded here.
* T=13 still has both full-count patterns. The four-directional-count 2:3 case, the 4:1 cases compatible with two-full rows, and all their simultaneous labeled adjacency and square budgets remain unpaid. The local four-case table is a necessary opposite-pair interface, not an extension theorem.
* A single tripled support, no tripled support, `M != C`, and any other original-row case remain entirely open. The 132-square decomposition, h matchings, and all results in this candidate must **not** be imported into `M != C` without separate proof. S3's closing-pair derangements are an unconditional structural reformulation, not a proof that all are derangements.
* A complete answer requires either all original actual eleven rows and direct verification of all 110 adjacency and 99 linear distance-two events, or a contradiction covering **every** original branch. No projected schedule, individual cell ledger, or local-model zero can by itself pay that frontier.
* This author proof and optional source require separate prospective independent checks and a parent disposition; no independent-family, human, formal/kernel, novelty, or priority claim is made. All held episodes and all their consumers remain NONINPUT.
