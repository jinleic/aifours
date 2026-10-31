# RQLS10 v82 — ALL remaining sparse mechanisms: complete ribbon topologies and an exact quadratic-projector reconstruction

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 17:55:14 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written graph/operator/row-column/ONB equivalences only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen physical parameter/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict transfer.

## 1. Exact domain: not a selected graph or original WLOG

Use ENTIRE v76 actual five-row-type trueE4 graph, v77 unique sparse local pairing, v79 circuit-intersection graph H, and v81's entire two/three-circuit exclusion. For an original MAX1 array in THIS graph family with ALL local frames sparse, there are exactly FOUR or FIVE actual vertex-simple projection circuits. H has five edges, one for each actual row-pair vertex, no loops, is connected, has every degree at least two and has edge multiplicity at most two. Circuit lengths are its degrees.

This manuscript does NOT assume every original4+6 array has this placement or sparse frames. It provides a COMPLETE two-sided representation of all remaining sparse SECTOR row/column frames, plus an exact sector interface for the SAME original TEN-class resolution. No existence or full original witness is asserted.

## 2. ALL abstract H topologies: four four-circuit cases, one five-circuit case

With FIVE circuit vertices, the degree sum is ten and every degree is at least two, so every degree is two. Connectedness forces H to be the SIMPLE FIVE-CYCLE: a two-edge parallel cycle would already form a separate component. No other five-circuit topology occurs.

With FOUR circuit vertices, the degree excess over two sums to TWO. Thus degrees are either 4,2,2,2 or 3,3,2,2. The exhaustive possibilities, with all parallel edges retained, are:

* FIGURE-EIGHT: a three-cycle and a two-edge parallel cycle sharing ONE circuit vertex. Degrees4,2,2,2.
* THETA(1,1,3): two length-one parallel paths and one internally disjoint length-three path between the degree-three vertices. Degrees3,3,2,2.
* THETA(1,2,2): one length-one path and two internally disjoint length-two paths between the degree-three vertices; equivalently K4 with ONE edge removed. Degrees3,3,2,2.
* BARBELL(2,1,2): two disjoint two-edge parallel cycles, joined by ONE bridge between their degree-three vertices. Degrees3,3,2,2.

Proof of completeness: for one degree-four vertex, suppress the other degree-two vertices. The resulting two loops at that vertex lift to two cycles, each of length at least two; their five total edges force lengths two and three. For two degree-three vertices, suppression produces either THREE paths joining them, or ONE joining path and ONE loop at each. Three paths have total length five and two internal degree-two vertices, so their positive lengths are 1,1,3 or1,2,2. In the loop case, looplessness before suppression forces both cycles to have length at least two; five total edges then force 2,1,2. A disconnected degree-two cycle is forbidden by connectedness. This accounts for every case, not a computer enumeration.

The repeated pairs in FIGURE-EIGHT and THETA(1,1,3) are interior-isoclinic by v79; BARBELL has two such disjoint repeated pairs. THETA(1,2,2) and the FIVE-CYCLE have no repeated pair and inherit NO isoclinicity assertion from that argument. Other pairs in any topology remain fully arbitrary subject to actual frame equations below.

## 3. H alone is NOT the original column placement: retain ALL rotation data

For EACH circuit vertex C of H, retain a CYCLIC ORDER of its incident H-edges, with every incident edge occurring once. An H-edge is an actual original row-pair vertex v. If the order at C is v1,...,v_d, its original edge-columns join v_i to v_(i+1), cyclically, and are labeled by circuit C. For d=two, there are TWO distinct original columns between the two vertices. Opposite directions reverse the orientation of that entire circuit, never erase a column.

These cyclic orders are part of the data, not WLOG-equivalent choices silently dropped. Their construction yields the original connected loopless four-regular multigraph G on the FIVE H-edges, with TEN distinct edge-columns. Each row-pair vertex lies on exactly its two incident H-circuits, supplying two edges from each. Connectivity follows from H connectivity and connectedness of each circuit cycle.

Conversely every actual sparse G supplies exactly these H incidences and cyclic orders by following its UNIQUE actual complement pairings. This is the full ribbon/rotation representation; an abstract topology list without these orders would lose operative original column data.

## 4. Only k+five rank2 projector variables reconstruct ALL forty actual rays

Fix ANY one of the five abstract H types, ALL cyclic orders and ALL labels of the actual two rows per G vertex and ten columns. Work in an arbitrary H4. For every circuit C choose a Hermitian rank2 projection P_C; its complement is I-P_C. Orient each circuit once so its outgoing edge plane at a vertex is P_C and its incoming edge plane is I-P_C. Across an edge these are opposite, as required for its two endpoint contributions to a column ONB.

At every original row-pair vertex v, order its two incident circuit labels as (C,D), an arbitrary discrete convention retained in the data. Introduce a Hermitian rank2 projection S_v satisfying EXACTLY

    [S_v,P_C]=[S_v,P_D]=0,
    tr(S_v P_C)=tr(S_v P_D)=1.

Because the projections commute and both have rank two, these conditions also give rank1 products with both S_v and I-S_v, for both P_C and I-P_C and for both P_D and I-P_D. All equations are finite exact operator equalities; no spectral genericity, invertibility or choice of eigenvectors is assumed.

For a column incident at v, let P_C^epsilon be its oriented C-plane there, either P_C or I-P_C. The two actual rank1 cell projectors in that column's row-pair are defined by

    first row, C-column:   P_C^epsilon S_v,
    second row, C-column:  P_C^epsilon (I-S_v).

For its D-columns reverse the S_v assignment:

    first row, D-column:   P_D^epsilon (I-S_v),
    second row, D-column:  P_D^epsilon S_v.

Thus every one of the FORTY actual cell-ray projectors is an explicit product of commuting rank2 projections, a quadratic polynomial in only k+five projector variables. Swapping the discrete circuit ordering at v is absorbed by S_v to I-S_v; swapping original rows is also retained, not a physical restriction.

## 5. Forward proof: these data give EXACT sector row/column ONBs

Each product is Hermitian and idempotent with trace ONE, hence a rank1 orthogonal projector. The two C-planes sum to I, so the two first-row C projectors sum to S_v; the D pair sums to I-S_v. They are mutually orthogonal inside each pair and across S_v/S_v-perp. Hence the FOUR first-row projectors are an ONB of H4. The same argument works for the second row.

In an original column of circuit C, its two endpoint row-pairs carry complementary planes P_C and I-P_C. The two projectors at either endpoint sum to its whole rank2 plane and are orthogonal. Their union is therefore a FOUR-ray column ONB. This uses the actual cyclic-order/orientation placement, not an arbitrary rearrangement of cells.

Impose additionally that ALL forty rank1 projectors just defined are pairwise DISTINCT. This is an exact ray condition, expressible for normalized rank1 projectors X,Y as tr(XY) not equal to ONE. It is not a finite test performed here. Distinctness forbids every local zero/unit principal-angle endpoint and every accidental inter-vertex repeat, including coincidences between different circuit labels. No claim is made that the full parameter class satisfying all these conditions has been shown nonempty.

The transition between the two original row ONBs has the sparse off-diagonal two-by-two block form automatically: same-circuit cross-row overlaps vanish because of S_v versus its complement. The other two unitary blocks have full support once all actual cell rays are distinct; a zero entry in a two-by-two unitary forces a modulus-one entry and a repeated ray. Therefore the constructed local transition is ACTUALLY SPARSE with the stipulated unique complement pairing, not an unnoticed dense case.

## 6. Converse proof: EVERY remaining sparse sector frame has exactly these data

Start from ANY actual all-SPARSE sector array in the domain. v77 constructs its unique circuits and fixed projection pairs, hence the abstract H, all cyclic orders, oriented P_C and actual labels above. At v, its sparse local form supplies S_v as the span of the first-row C-pair. This projection commutes with both circuit projections and has both displayed trace-one restrictions. The first-row D-pair lies in S_v-perp; the second row reverses those spans.

Each actual cell ray is then the ONE-dimensional intersection of its actual edge plane with the appropriate S_v or S_v-perp. Its projector is EXACTLY the corresponding displayed product. Hence there is no additional hidden factorization, flatness, product-state ansatz or missing complex phase. Individual ray phases are physically irrelevant in the registered complex-projective model; every complex ray is recovered by its rank1 projector.

Thus the construction is a TWO-SIDED equivalence for the COMPLETE remaining sparse SECTOR row/column/maximality problem, including ALL degenerate pair spectra allowed by the equations and all exact cyclic placements. It is not an equivalence to solving the full original100-ray problem without its remaining conditions.

## 7. Exact SAME-resolution interface: quadratic sector identities, not an automatic mate

Let L be ANY actual classical Latin labeling of the FULL ten-by-ten cells by ten class labels: every original row and column contains each label once. Retain its full placement, not merely a separate matching of the E4 cells. For each label r require exactly FOUR E4 cells and the exact equation

    sum of the FOUR reconstructed projectors X_cell with L_cell=r = I_H4.

Four unit rank1 projectors in dimension four sum to I if and only if their rays form an ONB: for their square unit-column matrix U, UU*=I implies U*U=I. Thus these are NECESSARY AND SUFFICIENT for the E4 portions of those SAME ten Latin classes to be quantum transversal ONBs. They are quadratic equations in the P_C,S_v variables once L is specified, with ALL L still quantified. No enumeration, candidate labeling or numerical viability test is selected or executed.

For the ORIGINAL full witness one must ALSO fill the complementary sixty cells in H6 with row/column ONBs and SIX-ray ONBs for THESE SAME ten labels, keep all sixty complement rays distinct, and preserve the original full cell layout. The E4 and H6 rays are automatically distinct across sectors, but no H6 construction or actual solution of the quadratic E4 equations is delivered. The full original classical-mate requirement is therefore visible and still unpaid, not silently replaced by ordinary forty-ray sector existence or one quantum transversal.

## 8. Meaningful new representation and remaining original gap

The progress is the EXACT all-variable reconstruction and converse, reducing forty unknown rays to k+five rank2 projectors with explicit quadratic cell formulas and SAME-resolution equations, while retaining the missing cyclic column data and ALL four/five-circuit topologies. The topology list alone is NOT offered as scientific progress. This provides a complete smaller representation for the actual remaining sparse problem without choosing a control or claiming a nonempty full-resolution family.

Unpaid: solving those complete projection/Latin equations and complementH6 in any surviving topology, dense local frames, other sector placements/minimalrank3 physical/higher-rank families and actual100 distinct rays/SAME allowed TEN-class resolution. All original irreducible10,4+6,5+5 branches remain OPEN. No all-sparse/global no-go/original witness/formal/kernel/family/vendor/human/checker/priority/current-openness/novelty promotion.

Imports are ENTIRE v76 actual graph/frame placement, v77 unique sparse local frames/circuit projections, v79 H/multiplicity/isoclinicity facts, v81 exact two/three-circuit frontier, elementary finite-dimensional commuting projection identities, and the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, flat factorization assumption or hidden local-to-global common2-sector inference.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S82, preserving ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history. Frozen Mainv17/S72/input map/proofs/live151 stay immutable; no automatic admission/read/adoption.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only, not permission to open111/newscope/coauditorproof; none accessed from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
