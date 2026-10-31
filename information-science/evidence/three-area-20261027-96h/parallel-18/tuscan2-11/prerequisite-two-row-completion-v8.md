# Definition-first common selection VIII: sentinel completion, exact affine D2 coupling for the last two rows, and a Hamilton parity obstruction

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:17:54 PDT 2026**.

**NEW author-WRITTEN, unreviewed completion bridge.** This is universally quantified over actual partial row systems, not a chosen numerical state or support stratum. At original order11 it applies to EVERY nine-row subsystem of a putative original array. It gives exact distance-two constraints on the remaining two cycle covers as affine equations over the two-element field, while retaining the indispensable Hamilton-cycle realization conditions. A parity obstruction and a missing-pair capacity obstruction follow. No original table or all-array contradiction is delivered.

## 0. Inputs and separation

Only the current S1/S2 literal packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c` (complete LF1-37), the prospective controls/pre-body ACK, and named elementary facts are inputs. Needed facts: actual permutation-row counting, directed graph degrees/paths, alternating cycles in a degree-two bipartite graph, elementary binary equations, and signs of finite permutations. Proofs are below.

No old turn/converse/support/Latin-sign theorem, source, private type8 or author/reviewer material is imported. The sentinel graph is defined afresh directly from literal rows; it is NOT an old split/turn construction. The Olson packet remains review-only. Prior exposure survives without a clean-cognition or independent-reconstruction claim.

No interpreter/calculator/Eval/CAS, row/graph enumeration, selected numeric/control/boundary probe, program, solver, replay, modelCLI or new GO. Component orientations below are mathematical variables for ALL possibilities, not an executed branch search.

## 1. Exact full-array sentinel equivalence

Let X have n≥3 symbols, and adjoin a NEW formal vertex ∞ not in X. For a genuine linear row

`a1,…,a_n`,

form the directed cycle

`∞→a1→a2→…→a_n→∞`.

This is a Hamilton cycle on N=n+1 vertices. The sentinel is bookkeeping only: no original row is given wraparound events.

### Lemma 1 — whole-array forward/converse

An original n-row array is equivalent to a decomposition of the complete loopless directed graph on X∪{∞} into n Hamilton cycles, with the extra condition that all directed two-step paths whose THREE vertices lie in X have distinct ordered outer pairs across the cycles.

**Proof.** In an original array each symbol is first once and last once: n occurrences minus n−1 outgoing/incoming adjacency events leaves one terminal/initial occurrence respectively. Thus the n augmented cycles use each ∞→x arc and x→∞ arc once, as well as each x→y adjacency arc once. They decompose the complete directed graph.

Conversely, deleting ∞ from each Hamilton cycle gives n actual linear permutations of X. Every x→y arc with x,y∈X is used exactly once, proving original adjacency coverage. The extra two-step condition applies precisely to the internal consecutive triples of those linear rows. It deliberately ignores paths using ∞ in ANY of their three positions. Hence it is exactly original distance-two noncollision, not a stronger cyclic requirement. ∎

This equivalence by itself is a representation. The following completion results supply additional common-selection constraints and exact remaining realization gaps.

## 2. Arbitrary n−2-row partial system and residual degree-two graph

Take ANY n−2 actual rows with pairwise distinct distance1 and distance2 events at the respective distances. A full extension must have distinct starting symbols and distinct ending symbols among these rows, by the endpoint count above. If either fails, there is no extension.

Assume these distinctness conditions. Their augmented cycles are edge-disjoint in the complete directed graph on N vertices. Delete those n−2 cycles; call the residual directed graph D.

Every vertex has indegree2 and outdegree2 in D, since the complete graph degree is n and n−2 Hamilton cycles have been removed. D is loopless and has no parallel directed arcs. A two-row adjacency completion is precisely a partition of D into TWO Hamilton cycles. This degree-two conclusion is derived for the augmented residual, not imposed on an original missing-distance2 graph.

Construct the bipartite graph B with a left and right copy of every vertex in X∪{∞}; the directed arc u→v in D becomes the edge u_L v_R. All degrees are2. Consequently each connected component of B is an even cycle, with exactly TWO alternating edge-colourings by colours0,1.

Choose a reference alternating colouring τ(e) symbolically on each component. If B has c components, every proper two-colouring of its edges is

`χ(e)=τ(e) xor x_j`, where e belongs to component j, with `x_j∈{0,1}`.

Each colour has one incoming/outgoing arc at every vertex, so it is a permutation/cycle cover. It need NOT be a Hamilton cycle; that condition is retained below.

## 3. Distance-two restrictions become exact affine equations

Let U be the set of ordered outer pairs already used at distance2 by the n−2 fixed rows. These are `(n−2)^2` distinct pairs. For each distinct a,c∈X, consider ALL residual two-step paths

`a→b→c`, with b∈X,

whose arcs lie in D. There are at most two such paths, because D has outdegree2 at a. In a proper colour splitting, such a path is an added original D2 event exactly when its two arcs have the SAME colour.

### Lemma 2 — exact local constraints for both added rows

All distance2 noncollision requirements for the two added cycle covers, relative to U, hold exactly under the following constraints:

1. If (a,c)∈U, EVERY available path a→b→c must have its two arcs differently coloured.
2. If (a,c)∉U and there are TWO available paths, it is necessary and sufficient that the two arcs of EITHER ONE of them be differently coloured. Then the other path is differently coloured as well.
3. If (a,c)∉U and there is only one available path (or none), there is no extra distance2 constraint for that outer pair.

**Proof.** A used outer pair allows no new occurrence, giving1.

For2, let the two paths have distinct middles b,d. The outgoing arcs a→b,a→d have opposite colours, and the incoming arcs b→c,d→c have opposite colours. If the first path's colours are u,v, the second path's are 1−u,1−v. Thus both paths are monochromatic exactly when u=v; in that case they lie in different colours and duplicate the outer pair across the two added rows. Otherwise neither is monochromatic, and there is no new event. This proves both necessity and sufficiency.

For3, one available path can occur in at most one colour, so an unused pair cannot be duplicated. These are all paths and all distinct original outer pairs, proving the complete claim. ∎

For each required differently-coloured pair of arcs e,f, the component variables satisfy

`x_j xor x_k = 1 xor τ(e) xor τ(f)`.                              (D2-XOR)

So the exact original D2 coupling of the TWO cycle covers is an affine binary system, not an unverified packet/row-margin assumption. If j=k, a right side1 is an immediate contradiction and right side0 is a tautology. For different components, the labelled constraint graph is consistent exactly when its edge labels xor to0 on every cycle: necessity follows by cancelling each variable twice; conversely, assign one variable per connected component and propagate labels along a path, with cycle consistency making the result path-independent. This is a written equivalence, not an executed linear solver.

Diagonal outer pairs a=c are not silently admitted as valid row triples. Hamilton cycles of length N≥4 below exclude every repeated vertex in a linear row. One may additionally impose opposite colours on all such original-symbol two-step returns as an early necessary condition; Lemma2 addresses exactly the distinct outer-pair D2 requirement from the literal definition, with Hamilton realization still explicit.

## 4. A genuine missing-pair capacity obstruction

Let T be the set of UNUSED outer pairs (a,c)∉U with TWO residual internal-middle paths. Under Lemma2 neither path may be monochromatic, so every pair in T is missing from the final original D2 event set.

A complete original array has exactly n missing directed pairs: n(n−1) possible pairs minus n(n−2) distinct D2 events. Therefore

`|T|≤n`                                                          (CAP)

is necessary for extension. More than n such double-path unused pairs is an exact no-extension certificate, independent of whether the affine system can be solved or the cycle covers made Hamilton.

No particular partial row system or outer pair is chosen or counted here. This is a universal implication for EVERY admissible partial system and hence for every n−2-row deletion of a hypothetical original array.

## 5. Hamilton realization is NOT removed: an independent parity obstruction

Let B's c alternating-cycle components have lengths `2l_1,…,2l_c`. Then `Σ_j l_j=N`. Splitting B into two perfect matchings gives permutations P,Q on the N augmented vertices. On component j their relative permutation is a cycle of length l_j, up to inversion/conjugation, so

`sgn(P)sgn(Q)=Π_j (-1)^(l_j−1)=(-1)^(N−c)`.

For completeness, following first a Q matching edge and then a reversed P matching edge runs once around the component's l_j left vertices. Hence the relative bijection on those vertices is one l_j-cycle. This proves the sign factor directly, without a Latin-square sign theorem.

If BOTH P and Q were Hamilton cycles on N vertices, each would have sign `(-1)^(N−1)`, so their product would be+1. Thus

`N−c is EVEN`                                                    (HP)

is necessary, independent of every component orientation variable.

At original n=11 (N=12), B must have an EVEN number of components. An odd component count is a rigorous two-row noncompletion certificate. It is not a contradiction for all original arrays: any genuine two-row remainder already obeys it.

This parity condition is NOT sufficient for Hamiltonicity. Nor are affine D2 consistency or the degree equations. They remain necessary constraints alongside the actual requirement that both permutations be single N-cycles.

## 6. Complete forward/converse two-row caller

Given the fixed n−2 partial rows, a full original extension exists IF AND ONLY IF:
- their starting symbols and ending symbols are separately distinct;
- some component orientation vector x in §2 satisfies every (D2-XOR) equation;
- BOTH resulting colour permutations are Hamilton cycles of length N.

**Forward:** an original completion supplies exactly those two cycles, their proper colouring, component vector and D2 constraints.

**Converse:** such a vector partitions every residual arc once into the two actual Hamilton cycles. Delete ∞ from them. The result is two actual linear permutation rows; with the fixed rows their adjacencies cover every directed original pair exactly once, and Lemma2 checks every distinct outer-pair D2 event, with no sentinel-wrap event included. Hamiltonicity rules out repeated-symbol rows and diagonal two-step returns. Thus the same constructed rows satisfy the literal original definition.

(CAP) and (HP) are proved necessary certificates for this exact caller, not substitutes for its remaining Hamilton conditions.

## 7. Original target and next genuine gap

This applies without assuming any maximal cross-layer overlap, any old support census or a selected construction family. It exposes a concrete common-row selection interface after an arbitrary n−2-row partial system: local D2 coupling is affine, but the two single-cycle conditions are still global.

No nine-row input at n=11 is supplied or evaluated, and no proof is given that every possible such input violates (CAP), (HP), affine consistency or Hamiltonicity. Thus the original problem is still OPEN. Conversely no satisfiable local system is promoted to an actual completion without both Hamilton-cycle witnesses.

**Next admitted mathematical step:** retain this exact residual common-row system and determine whether stronger universal Hamilton/affine compatibility or an original all-row extension theorem follows. A degree-two cycle cover or a feasible fractional mixture alone does not pay that step. No old theorem/source, solver or selected probe is requested by implication.

All prior exposure/STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist. Author-written, unreviewed, same harness; no parent adoption, formal/kernel, executable, human, configured-family, priority or novelty claim. Deadline unchanged.
