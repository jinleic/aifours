# Addendum 11 — actual coprime-Sylow coupling and a sharp obstruction to two-sided noncrossing grids

Owner **MathOlson-2-2**, successor math-2.
Actual `/bin/date` before writing: **Tue Oct 27 16:25:05 PDT 2026**.
**NEW WRITTEN all-variable conditional coupling / exact bridge obstruction. Not an unrestricted solution, avoiding word or novelty claim.**

## 1. Current scope, source separation and timely substantive publication

Main's latest direction is to continue the actual mixed-prime bridge, such as ordered transport across coprime Sylow factors, using ONLY S1 definitions and the current written chain. No new paper/algebra method was released.
This proof uses the original S1/S2 finite-group word definition, elementary group quotients, noncrossing ordered partitions, finite integer coprimality and elementary PLANAR GRAPH counting. Every load-bearing specialized step is proved below.
There is NO p-group existence theorem, finite-field zero count, group algebra, augmentation ideal, public-paper bound or external source in this derivation.

The source statement-only status remains: all-p-group existence is PRIOR/REPRODUCTION; mixed-prime ordered status is UNCERTIFIED-OPEN, not proved open. Main's Han/Qu/Dimitrov screen is a STATUS boundary, not a theorem input here. I opened none of those papers for this step.
The affected Dimitrov proof/method and prospective algebra branch remain STOPPED; extra displayed context and all consuming method/selection/confidence are NONINPUT.
Prior cross-domain partition/incidence exposure is disclosed, not erased. No quantum Gram, Latin-basis, spectral or QLS theorem is an input; the ordinary group/planar proof is complete here. This is not a clean-cognition/noninfluence certificate.

The actual substantive result and its complete short proof were already published in checkpoint012 at observed prewrite16:24:19 PDT, before this expanded body. Previous substantive checkpoint observation was16:05:22; the returned-observation interval was18m57, not an exact native-write/runtime claim.
All earlier candidates remain immutable and unadopted at their own scopes.

## 2. Exact original target and the new actual-object coupling

For a finite group G of order n, O(G) is the assertion that EVERY actual word of length2n−1 contains EXACTLY n ORIGINAL occurrence indices in increasing order with product identity.
The original ALL-finite-group problem is not restricted to Sylow/direct-product groups by this paper.
We address a candidate bridge in the genuinely mixed-prime direct-factor setting.

Let G=P×Q with |P|=k, |Q|=l, gcd(k,l)=1 and n=kl.
Equivalently one may be given actual normal P,Q with P∩Q={1} and G=PQ; their commutators lie in both normal subgroups, so they commute and give this direct product.
No arbitrary finite group is declared to have such normal Sylow factors.

Fix ANY original word of length2n−1 and ANY selected set U of EXACTLY n actual indices, in inherited original order.
Suppose U has TWO packet partitions:

- rows R_1,…,R_k, each of size l, each ACTUAL inherited-order product lying in P×{1};
- columns C_1,…,C_l, each of size k, each ACTUAL inherited-order product lying in {1}×Q.

For this coupling assume each partition is NONCROSSING in U: two blocks of the SAME partition never alternate at four indices.
The two different partitions may cross one another. They are representations of the SAME actual selected indices, not independent copies of a word.
No aggregate product-one condition on row products or column products is assumed.

**Theorem A — genuine two-sided actual coupling.** Under exactly these hypotheses, the chronological product over U is identity. Thus U is an actual original-order n-occurrence selector.

**Proof.** Project the actual selected word to Q. Every row packet individually has quotient product1.
A noncrossing partition has an interval block: choose one with minimal endpoint span; an intervening different block must lie fully inside without crossing and would have smaller span, a contradiction.
Remove that interval's identity factor in the projected chronological word. Induction removes ALL row packets and proves its Q-product1. Thus the ACTUAL G-product lies in P×{1}.
The SAME proof applied to the columns and projection to P puts the SAME chronological product in {1}×Q.
Their intersection is trivial, so that product is1. ∎

This pays the actual coupling, with no permutation of selected letters, centrality assumption, separate kernel zero choice or unproved cancellation of commutators.
The existence of such two coupled partitions for EVERY original word is NOT supplied.
A valid original selector is NOT asserted to admit these partitions, so no converse/WLOG certificate is smuggled in.

## 3. The tempting independent-grid strengthening

A particularly natural stronger bridge would make the two uniform partitions orthogonal:

`|R_i∩C_j|=1 for EVERY i,j`.

Then every selected occurrence would be one independent row-column cell, suggesting a k×l grid of simultaneous quotient-packet constraints.
**This is an ADDITIONAL premise, not part of O(G), not implied by coprimality and not needed by TheoremA.**
The next theorem shows that its simultaneous NONCROSSING requirement is impossible for both factor orders at least3, whatever the group letters are.
This is an obstruction to that precise proposed bridge, not a no-go for the original group problem.

## 4. Planarity of the ACTUAL incidence graph

Let U be ANY finite linearly ordered set with two noncrossing partitions R and C.
Form its bipartite incidence MULTIGRAPH: a row vertex for each R block, a column vertex for each C block, and ONE EDGE for EACH ACTUAL occurrence u joining its two containing blocks.
Parallel edges encode multiple actual indices in one intersection; they are not merged occurrences or duplicated labels.

**Lemma B.** This incidence multigraph is planar. Therefore the simple graph obtained by retaining one edge for every NONEMPTY intersection is also planar.

**Proof.** Above the actual index line, connect consecutive members of each row block by arcs; below it do the same for columns.
Arcs within a partition have disjoint or nested endpoint intervals: a pair of alternating intervals from different blocks would violate noncrossing, and consecutive-member arcs of one block do not alternate.
They can be drawn without intersections in their respective halfplanes. For example, semicircle arcs with disjoint or strictly nested diameters do not cross; arcs of the same path may share their own endpoints.
At each actual index split the point into an upper row copy and a lower column copy connected by a short vertical edge. Local rerouting at finitely many endpoints keeps all other arcs disjoint.
Each row block is now one connected upper path-tree; each column block is one lower path-tree.
Contract each of these disjoint path-trees to its corresponding block vertex. Edge contraction preserves a plane embedding; the vertical edges become exactly the one-per-occurrence bipartite edges.
No row vertex is identified with a column vertex, so no vertical loop is created.
This is the required planar incidence multigraph. Deleting all but one parallel edge preserves planarity. ∎

This geometric construction does NOT reorder U or assert any new actual-word identity; it proves a combinatorial constraint on a proposed certificate on those fixed indices.

## 5. Exact sharp obstruction to an orthogonal noncrossing grid

**Theorem C.** On a linearly ordered set of k l points, an orthogonal pair of uniform k-row/l-column partitions can BOTH be noncrossing IFF min(k,l)≤2.
This statement is purely incidence-theoretic and does not need coprimality.

**Necessity when k,l≥2.** Orthogonality makes the simple incidence graph EXACTLY the complete bipartite graph K_(k,l), with V=k+l vertices and E=kl edges. It is connected.
A connected simple planar bipartite graph with V≥3 has

`E≤2V−4`.

For completeness, Euler's identity V−E+F=2 follows by deleting nonbridge cycle edges, reducing E and F together, until a tree with E=V−1,F=1 remains.
Every facial boundary walk has length at least4 for a connected simple bipartite graph with at least3 vertices; a bridge is counted twice in the face walk, and the sole two-step single-edge exception has only2 vertices. Thus2E≥4F.
Combining gives the displayed edge bound.

Hence

`kl≤2(k+l)−4`, equivalently `(k−2)(l−2)≤0`.

If both k,l≥3 this is impossible. No group assignment, overlap tuning or quotient theorem can make that incidence pattern exist.

**Sufficiency and sharpness.** For k=2, order the first row's l cells by column1,…,l and the second row's cells by column l,…,1.
The rows are separated intervals. Column j is the pair at positions j and2l+1−j, so all column pairs are nested and noncrossing. Every row-column intersection is one cell.
For l=2 interchange the names of the partitions. If one factor is1, one partition has a single block and the other only singletons, which is immediate.
These cases prove the full iff, including the trivial k=l=1 case separately from the planar edge formula. ∎

Even when min(k,l)≤2 permits the incidence, this does NOT guarantee the actual quotient products required by TheoremA.
The result is sharp for geometric certificate existence, not a group theorem for those factor sizes.

## 6. Coprimality gives CONNECTEDNESS without orthogonality

Return to uniform row blocks of size l, column blocks of size k, with exactly k and l blocks respectively, and gcd(k,l)=1.
Do NOT assume orthogonality.
Let E be the number of NONEMPTY row-column intersections, i.e. the edge count of the SIMPLE incidence graph.

**Lemma D.** The incidence graph is connected.

**Proof.** A component has, say, a row vertices and b column vertices. Every selected occurrence of any of its row blocks has its column in the same component, so its actual occurrence count is a l.
Counting instead by its columns gives b k. Thus a l=b k.
Every block is nonempty, so a,b≥1 in each component. Coprimality forces k|a and l|b.
As a≤k,b≤l, it follows that a=k,b=l. Thus any component already contains ALL vertices. ∎

This is where the coprime Sylow-factor sizes make a load-bearing difference; connectedness is not assumed from a generic picture.

## 7. Quantitative overlap that ANY such coprime dual certificate must retain

By LemmaB the simple incidence graph is planar, and by LemmaD it is connected.
For k,l≥2 its vertex count is at least4, so the same bipartite bound gives

`E≤2(k+l)−4`.

Let m_(ij)=|R_i∩C_j|, counting ACTUAL original indices.
Their total is kl=n, and exactly E of them are nonzero. Therefore the exact repeated-intersection excess is

`sum_(i,j) max(m_(ij)−1,0)=kl−E`.

Consequently

`sum_(i,j) max(m_(ij)−1,0) ≥ (k−2)(l−2)`.

For coprime factor orders both at least3 this forces POSITIVE overlap excess.
Thus any viable simultaneous two-sided noncrossing quotient certificate must accommodate at least this many repeated row-column incidences beyond one occurrence per nonempty intersection.
It cannot be assembled as independent single-cell constraints on an orthogonal grid.
Those repeats are real shared original positions, not permission to duplicate a selected occurrence in the group product.
The bound is necessary, not claimed optimal for every prescribed k,l, and not by itself a contradiction to a nonorthogonal certificate.

## 8. BOTH caller directions and exactly what is ruled out

**Paid positive caller:** if a given selected n-occurrence set in the actual direct-product group has the two stated NC quotient-packet partitions, its original product is identity by TheoremA. No kernel aggregate theorem is missing from THAT conditional implication.

**Exact failed strengthening:** demanding in addition a one-cell orthogonal grid is impossible when k,l≥3. This is independent of group values, so no later scalar/phase/value choice can rescue THAT particular certificate pattern.

**What remains possible:** nonorthogonal NC dual partitions with the forced overlap, a certificate with one family crossing but its actual correction paid, a joint construction not based on a grid, or a completely different original selector. None is excluded by the planar argument.
No theorem that every original selector admits two NC partitions is supplied or used.

If G has two distinct ODD Sylow factors, both sizes are at least3, so the orthogonal NC grid cannot be the unrestricted bridge across them.
If a2-Sylow has order at least4 and the other factor order at least3, the same obstruction applies.
A factor of order2 merely avoids this incidence obstruction; it does not prove the ordered statement, and the old order2p residual is not closed.
These are exact consequences of the factor sizes, not selected numerical examples or a purported classification of original counterexamples.

The full mixed-prime/nilpotent ordered2n−1/n problem remains unresolved by this conditional lemma and bridge obstruction. The status is UNCERTIFIED-OPEN under the allowed primary screen, not a proof of worldwide openness.
No actual avoiding word, all-group theorem or novelty/SOTA/priority claim is made.

## 9. Dependency/application and controls

Ordinary inputs are group quotients/direct products, noncrossing finite partitions, finite incidence graphs, elementary plane-edge contraction, Euler's identity and face counting, and coprime integer divisibility. Every specialized application and degeneracy is proved above.
No graph classification theorem, public-paper proof, p-group theorem, polynomial bound, quantum partition theorem, old guide or source confidence is imported.
This needs its own separately frozen full mathematics AND original-object/dependency/source-separation review before adoption; no already frozen w42/w45/w51 scope is enlarged.
Those allocations and reported no-defect returns are not scientific inputs or parent adoption.

All prior bytes remain immutable. A5/A6 existence remains PRIOR/REPRODUCTION; count/short-threshold/proof novelty and A7/A8 mixed-prime gates are separate unreviewed questions.
Affected Dimitrov proof/method and prospective augmentation/group-algebra branch remain STOPPED; extra displayed source/method/selection/confidence NONINPUT. All other STOP/HOLD/ZERO outside S1, nine held formulas/consumers, v214-A/threshold/v227, N4UNKNOWN historical actual child exitUNESTABLISHED, aux214STOP and findings persist.
No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/state/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infrastructure action or timer/heartbeat loop.
WRITTEN/same harness, not formal/kernel/human/configured-family/executable/novelty acceptance. Same18/new exclusive append-only root/actual20min substantive target with honest gaps/science ends2026-10-31T21:23:27.000Z.

**END OF COMPLETE COPRIME DUAL-PACKET COUPLING AND PLANAR BRIDGE OBSTRUCTION.**
