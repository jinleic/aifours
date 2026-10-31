# Addendum 12 — collision-paying coprime tree certificates, and a full actual-word obstruction to fixed windows

Owner **MathOlson-2-2**, successor math-2.
Actual `/bin/date` before writing: **Tue Oct 27 16:37:17 PDT 2026**.
**NEW complete WRITTEN collision/actual-value coupling candidate. Not an original solution, avoiding word or novelty claim.**

## 1. Exact current task and source boundary

Main directed the next step to a certificate paying A11's forced overlap collisions, or an exact obstruction to that, using S1 inputs and the current written chain.
This manuscript supplies: positive collision patterns for EVERY coprime pair; a sharp cut criterion for any tree template; an exact actual-product completion criterion; and a universal full-length word family where every local leaf check passes but ANY selection respecting fixed source windows fails.
It is not merely a picture/coordinate encoding: the positive incidence construction and the actual fixed-window incompleteness theorem are both proved.

Only the admitted S1/S2 original word definition, elementary group quotients, finite tree/order counting and integer coprimality are used. The needed noncrossing arguments and actual-product caller are proved inline.
There is no p-group theorem, public-paper bound/proof, finite-field zero-count, group algebra/augmentation, quantum Gram theorem, old held guide or additional source in this proof.
Prior partition/source exposure is not erased; no blind/clean-cognition/noninfluence certificate.
Affected Dimitrov proof/method and augmentation branch remain STOPPED, extra displayed method/selection/confidence NONINPUT; A5/A6 existence PRIOR/REPRODUCTION.

The original problem still asks for EVERY length2n−1 word in EVERY finite group of order n, an ORIGINAL-order identity subsequence of EXACTLY n actual occurrences.
Here G=P×Q, |P|=k, |Q|=l, gcd(k,l)=1 and k,l≥2, n=kl. This is the actual coprime direct-Sylow-factor setting, not WLOG for all finite groups.

## 2. What must be paid on the SAME selected occurrences

On an n-occurrence selected set, rows are k packets of size l with product in P×{1}, and columns are l packets of size k with product in {1}×Q.
Both partitions must be noncrossing in the inherited ORIGINAL order.
Projecting to Q and removing noncrossing interval row packets of identity, then projecting to P and removing the columns, proves the SAME chronological product lies in both direct factors and is1.
This proof requires no aggregate kernel product or commuting selected letters.
The existence of the TWO actual-value partitions is a separate hypothesis, not guaranteed by their incidence alone.

A11 proves that one-cell orthogonal intersections cannot have both partitions noncrossing when both factor sizes exceed2.
Repeated intersections therefore have to be genuine groups of DISTINCT actual indices. They may not be erased, duplicated or independently assigned P/Q products.
We now construct and control such collisions exactly.

## 3. A collision-paying tree template exists for EVERY coprime k,l

Temporarily use ordered labels1,…,n, not assigned group values.
Take k CONSECUTIVE row blocks of length l and l CONSECUTIVE column blocks of length k.
Both partitions are separated, hence noncrossing.
Their internal cut positions are

`l,2l,…,(k−1)l`, and `k,2k,…,(l−1)k`.

There is no common internal cut: i l=j k with0<i<k,0<j<l contradicts coprimality.
The common refinement therefore has EXACTLY

`E=(k−1)+(l−1)+1=k+l−1`

nonempty interval intersections. Each has a positive integer size m_e.
The row weighted degrees are l, the column weighted degrees k, and sum_e m_e=n.

The simple incidence graph is connected: any component with a rows and b columns contains a l=b k actual labels, and coprimality forces it to contain all vertices.
A connected graph with k+l vertices and k+l−1 edges is a TREE, since deleting any cycle edge would leave a connected graph with fewer than V−1 edges.
Thus this is an explicit universally available NONORTHOGONAL collision-paying tree pattern.
Its exact repeated-intersection excess is

`sum_e(m_e−1)=n−E=(k−1)(l−1)`.

This exceeds or meets the necessary A11 planar bound and really pays it; it is not a fictitious orthogonal grid.
It is NOT claimed to minimize overlap among all planar certificates.
No ACTUAL group word has been replaced by these labels; a separate order-preserving binding to original indices is mandatory below.

## 4. Exact cut test for EVERY proposed weighted tree

More generally let T be ANY bipartite TREE with k row vertices and l column vertices.
Seek positive integer edge weights m_e with each row sum l and each column sum k.
Orient each edge from row to column. Remove e and let S_e be the component containing its ROW endpoint, with a_e rows and b_e columns.

**Theorem A.** There is AT MOST ONE weight solution, and necessarily

`m_e=a_e l−b_e k`.

Those cut values always solve the signed degree equations; therefore a positive solution exists IFF EVERY displayed cut value is positive.
Under coprimality none of the cut values is zero.

**Proof.** Inside S_e the total row weight is a_e l and column weight b_e k. Internal edges cancel in the difference; the sole boundary edge contributes +m_e, proving necessity.
For sufficiency, give each row signed demand+l and each column−k. The total demand is0.
For a row vertex, components on the far side of its incident edges partition all OTHER vertices, so summing the negative of their demands gives exactly its own demand+l. The cut formula therefore gives its required row sum.
For a column vertex, the row-end components of its incident edges partition all OTHER vertices, so their demands sum to−(−k)=k, giving the required column sum.
Uniqueness follows from the cut values. They are integers, so positivity is the only further requirement.
If a proper nonempty cut component had a_e l=b_e k, coprimality would force a_e=k t,b_e=l t. The allowed counts leave only t=0 (empty) or t=1 (all vertices), both impossible for that component. Thus no zero cut occurs. ∎

This provides a precise obstruction to a proposed collision tree: any negative cut value forbids positive uniform overlaps. No tree enumeration, numerical input or program is performed.

## 5. Any positive weighted tree can be realized with BOTH partitions noncrossing

Root such a tree at a row vertex, order its children arbitrarily, and list edges in depth-first PREORDER.
Replace each edge e in that list by m_e consecutive DISTINCT occurrence labels carrying its row/column endpoint labels.
The total number is n, and the weighted degree equations give the required uniform block sizes.
Each row-column intersection is exactly its edge cluster of size m_e, or empty if there is no edge.

To verify noncrossing, consider two vertices in the SAME bipartition.
If neither is an ancestor of the other, their depth-first subtrees are disjoint intervals.
If A is an ancestor of B, B lies in one branch after an A-incident edge. Its incident clusters all occur before the next A-child edge, if one exists; otherwise after A's last incident cluster.
Thus the B-interval is wholly nested between consecutive A-incidences or wholly after A's last incidence. Four alternating A/B labels cannot occur.
Repeating a single edge label in an adjacent cluster cannot create an alternating pattern absent from the original edge list.
Both row and column partitions are therefore noncrossing.

This is a COMPLETE positive geometric certificate paying arbitrary admissible tree collisions, not an actual group-value assignment or an assertion that every original selector has this tree form.
The canonical consecutive template of §3 is one concrete option; no optimization or WLOG selection is asserted.

## 6. Bind collision clusters to the ACTUAL original word without changing it

Fix ANY such ordered weighted tree template and an ACTUAL original word w of length2n−1 in P×Q.
Choose pairwise disjoint source windows I_e, chronologically ordered as the template edge clusters, of size2m_e−1 each.
This fits inside the ORIGINAL length because

`sum_e(2m_e−1)=2n−E≤2n−1`.

For example use consecutive windows in the initial2n−E positions; the remaining E−1 positions are unused. Other prescribed separated windows are also allowed.
Each cluster must select EXACTLY m_e ORIGINAL occurrences from its own window.
Define the ACTUAL product list

`A_e={ chronological products of m_e-occurrence subsequences of w restricted to I_e } ⊆ P×Q`.

These are paired P/Q products of the SAME actual subsequence, not independent component projections or arbitrary edge variables.
No set is computed, enumerated or generated by a program here; this is a universally quantified mathematical definition.
The windows' separation means independently witnessed choices g_e∈A_e can be concatenated into an order-preserving n-occurrence binding of the whole template.
Each actual occurrence appears once, although it is viewed in both its row and column certificate.

The row quotient condition is the ordered product of π_Q(g_e) over its incident edge clusters, in their actual order, equal1.
The column quotient condition is the corresponding ordered product of π_P(g_e) equal1.
These are the exact common-value coupling conditions, with ALL m_e collisions retained.

## 7. Exact tree-message certificate, necessity AND actual-object sufficiency

For a vertex v let π_v=π_Q for a row and π_P for a column.
Root the tree and orient edges away from the root. For a nonroot vertex v with parent edge e, define a message M_(v→e)⊆A_e recursively:

A pair g∈A_e belongs to this message IFF one can choose g_f from each child's message on its edge f so that the product of their π_v-values, WITH π_v(g) inserted at e's ACTUAL incident-edge position, is1.
No commutativity or arbitrary reordering of those incident products is permitted.
For a leaf this is simply `M_(v→e)={g∈A_e:π_v(g)=1}`.
At the root require choices from all incoming child messages making its incident-edge product1 in the same actual order.

**Theorem B.** Root acceptance is EQUIVALENT to the existence of an ACTUAL original n-occurrence subsequence respecting the chosen windows/template and satisfying ALL row and column quotient conditions.
Hence root acceptance SUFFICES for a genuine original ordered identity selector.

**Proof, necessity.** Such an actual selection gives a single actual g_e∈A_e on every edge. Starting at leaves and restricting it to each subtree verifies every message membership, and finally the root condition.
**Proof, sufficiency.** Choose witnesses for root acceptance and recursively for each message. Distinct child subtrees have no other shared edges/vertices, so their choices combine without conflicting edge assignments.
This gives ONE actual paired g_e∈A_e per edge satisfying ALL vertex equations.
Choose its witnessing m_e-occurrence subsequence in I_e. Disjoint chronological windows make these witnesses simultaneously compatible; their total cardinality is sum m_e=n and their order is the template order.
Sections2/5 then prove the chronological G-product is identity. ∎

This certificate is not permission to run a tree program or to replace A_e by separately fitted P and Q lists.
An arbitrary original selector need not respect these fixed windows or template; NO converse to unrestricted O(G) is claimed.

## 8. Universal ACTUAL obstruction: fixed windows are not a complete all-word bridge

**Theorem C.** For EVERY nontrivial coprime k,l, EVERY positive uniform weighted tree template above, and EVERY prescribed disjoint windows of lengths2m_e−1 fixed before the word values, the resulting certificate scheme fails on SOME actual full-length word — even one with at least n identity letters and with every local leaf check satisfied.

**Proof.** Coprimality with k,l≥2 means they are unequal. Interchange the two factor names if necessary so k<l.
Use the ACTUAL group `G=C_k×C_l`, with q a generator of C_l.
Choose ANY template edge e0, of positive weight m=m_(e0).
Because its column weighted sum is k, `1≤m≤k<l`.
Fill EVERY original position of I_(e0) with `(1,q)` and EVERY OTHER original position with identity.
This is an actual word of EXACT length2n−1; no arithmetic example or table is tested.

ANY admissible m-occurrence choice inside that window has product `(1,q^m)`, which has NONIDENTITY Q-coordinate since0<m<l.
Every other A_e is the singleton identity. Therefore the row vertex incident to e0 has Q-product exactly q^m≠1, no matter which actual occurrences are chosen inside any window.
No root-accepted certificate or window-respecting selector of this template can exist.

This is NOT merely a failed leaf: e0 cannot meet a row leaf, because a row leaf would require m=l>k. A column leaf checks only P, where the bad edge has value1. Every other leaf sees identity.
Thus ALL actual leaf conditions are feasible, but the internal row coupling fails. Quotient/kernel leaf existence alone cannot fill this gap.

There are2m−1 nonidentity original letters. The number of identities is

`2n−1−(2m−1)=2n−2m≥n`,

because n=kl≥2k≥2m.
Selecting n identity occurrences is a correct original ordered selector.
Hence the ambient word is NOT avoiding and the failure is of the FIXED collision-window scheme, not of O(G).
The proof works for EVERY template/window choice fixed independently of word values; it does not rule out an adaptive choice after seeing the original word. ∎

If factor orders are distinct prime powers, these are actual coprime Sylow-factor examples. Their abelian character does not make the certificate failure less valid; it explicitly prevents confusing a restricted-certificate no-go with failure of the original ordered theorem.
No new group-family existence discovery is claimed.

## 9. What has been paid, what is obstructed, and the exact remaining mixed-prime premise

Paid in full:

- positive noncrossing overlap patterns for EVERY coprime k,l, with exact collision excess;
- the unique signed-cut weights and complete positivity criterion for any proposed tree;
- realization of EVERY positive weighted tree as two uniform noncrossing partitions;
- an EXACT paired-value tree certificate on ACTUAL original windows, with both lifting directions;
- an all-template/all-fixed-window actual-word counterfamily showing leaf feasibility and original-length budgets do NOT force the internal coupling.

Thus A11's forced overlap collisions can be represented and accounted for exactly. They are not a geometric impossibility once orthogonality is abandoned.
But geometric accounting and even every feasible leaf are not an all-word selector theorem. The remaining premise is an ADAPTIVE actual-window/tree/selection result or another transport paying the shared component products, not independent per-edge completion or a fixed template imposed WLOG.
The theorem does not eliminate all adaptive collision certificates, all noncrossing transport or the original mixed-prime/nilpotent question.
Original all-finite-group O(G), mixed-prime unrestricted existence and the old odd-prime dihedral actual-word gap remain unresolved by this packet.
The public primary status is UNCERTIFIED-OPEN, not proof of worldwide openness.

All results here are universally quantified written proofs, not selected-word computation, encoding-only progress or a claim of current novelty.
They need a NEW frozen full mathematics AND actual-object/dependency/source-separation review; no existing w42/w45/w51/A11 wave is enlarged.

## 10. Controls

Only original S1/S2 definitions, elementary finite groups/trees, depth-first order as a written construction, coprime integer counting and inductive actual-product logic are inputs. No old proof/held guide, paper formula, p-group theorem, quantum result or source confidence is imported.
No tree messages or product lists were executed/enumerated. A mathematical recursion with its induction proof is not a scientific program run.
Prior exposure is not erased or certified uninfluential. A5/A6 existence PRIOR/REPRODUCTION; affected Dimitrov source/proof/method and augmentation/group-algebra branch STOPPED; extra displayed method/selection/confidence NONINPUT.
Every other STOP/HOLD/ZERO outside S1, held9/v126/v150/v214A/threshold/v227, N4UNKNOWN historical actual child exitUNESTABLISHED, aux214STOP and process findings persist.
No interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numerical/control/state/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infrastructure action or heartbeat/timer loop.
Same18/new exclusive append-only root/actual20min substantive target and honest gaps/science ends2026-10-31T21:23:27.000Z. WRITTEN/same harness, not Main adoption/formal/kernel/human/configured-family/executable/novelty acceptance.

**END OF COMPLETE COLLISION-TREE CERTIFICATE AND FIXED-WINDOW OBSTRUCTION.**
