# RQLS10 v85 — Dense local frames: one cell per transversal, projection trails, and NO single-dense-vertex sector frame

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 18:32:08 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written unitary-zero/projection/graph-trail/counting arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Domain: ALL mixed sparse/dense local frames of the v76 graph

Use the ENTIRE v76 actual five-row-type trueE4 graph G: a connected loopless 4-regular multigraph on the five actual row-pair vertices, with the ten actual columns as edges. At each vertex v the two actual row ONBs e_i,f_i of E4 are indexed by the four incident columns, and the column plane is P_(v,i)=span(e_i,f_i). By v76, across every column e={u,v} the endpoint planes are complementary: P_(v,e)=I-P_(u,e). By v77, EVERY vertex is either SPARSE (transition [[0,U],[V,0]] with full-support 2-by-2 unitaries, unique complement pairing) or DENSE (all twelve off-diagonal transition entries nonzero, canonical weights a,b,c>0). Let d be the number of DENSE vertices. The all-sparse case d=0 is the domain of v77-v84; this manuscript treats ALL d.

No complex frame, weight, phase, angle or row/column labeling is chosen. Ordinary 100-ray maximality (MAX) is assumed where stated; a full TEN-class resolution is assumed ONLY where stated.

## 2. Lemma D1: a quantum transversal contains at most ONE cell at any dense vertex

Two cells at one vertex lying in distinct rows and distinct columns are e_i and f_j with i not equal to j. Their overlap is the transition entry W_ij. In the DENSE branch every off-diagonal entry is nonzero, so they are NEVER orthogonal. Cells in the same row or column are excluded from a transversal by definition. Hence every quantum transversal, and in particular every class of a full resolution, contains at most ONE cell at each dense vertex.

At a SPARSE vertex the same reasoning allows at most TWO cells, and two cells occur only as e_i,f_j with W_ij=0, i.e. a complementary pair of planes of ONE local pair, with opposite orientations.

## 3. Projection trails through sparse vertices

Start at any vertex along a column e. Whenever the far endpoint is SPARSE, continue along its unique complement partner of e. Stop when a DENSE vertex is reached, or when the starting column recurs. This decomposes the ten columns into CLOSED CIRCUITS, which meet only sparse vertices, and OPEN TRAILS, which start and end at dense vertices and pass only through sparse vertices. Every dense vertex is the end of exactly four trail ends.

Along a trail e_1,...,e_L with vertices u_1,...,u_(L+1), the v76 column complement and the sparse complement pairing give, exactly as in v77,

    P_(u_k,e_k) = Q    for every k,
    P_(u_(k+1),e_k) = I-Q    for every k,

for ONE fixed rank-two projection Q, the TAIL plane. This is the actual propagation P_(v,f)=I-P_(v,e)=P_(u,e), not a chosen orientation. A trail cannot use both local pairs of one sparse vertex: then all four planes there would be Q or I-Q, contradicting v77's strict sparse cross-pair traces between 0 and 2. So trails are vertex-simple through sparse vertices.

ORIENTED-PLANE BOUND. Under MAX, a quantum transversal contains at most one cell in Q and at most one in I-Q along a trail. Two cells in the same oriented plane at one vertex share a column. At different vertices they belong to two actual ONBs of the same two-dimensional plane, and orthogonality would make one of them equal to the column-mate ray of the other: a duplicate ray. This is the C80_PLANE1 argument verbatim, valid for trails and circuits alike.

## 4. Theorem D2: no trail returns to its starting dense vertex; d=1 is impossible

Suppose a trail starts at dense D along e_1 and ends at the same D along e_L. Since G is loopless, L is at least two and e_1,e_L are distinct columns at D. By section3 their planes at D are Q and I-Q, which are COMPLEMENTARY. In the DENSE canonical form every pair of incident planes has trace tr(P_iP_j) in {2a^2,2b^2,2c^2}, strictly between 0 and 2, so no two incident planes are complementary. Contradiction.

Consequently every open trail joins TWO DISTINCT dense vertices. If d=1, the four trail ends at the unique dense vertex must pair among themselves, which is impossible. Hence:

    NO ordinary MAX sector frame in the ENTIRE v76 graph family has exactly ONE dense vertex.

This uses ONLY the v76 column complements, v77 local classification and MAX through v77's no-shared-ray condition. It needs NO quantum transversal, full resolution, CS angle, isoclinicity or v15 ceiling. It is therefore stronger than a resolution obstruction: it excludes the d=1 mechanism at ordinary sector level.

## 5. Exact dense-trail graph for d at least two

Contract each open trail to a single edge between its two distinct dense end vertices. The result is a LOOPLESS 4-regular multigraph on the d dense vertices, with 2d edges. At each dense vertex the four trail-end planes are pairwise neither equal nor complementary, satisfy sum = 2I, and carry the DENSE weights in the v77 trace pattern. Hence ANY two trails ending at a common dense vertex have tail projections Q,Q' with Q' outside {Q,I-Q}, whatever their orientations.

* d=2: all FOUR trails join the two dense vertices.
* d=3: every pair of dense vertices is joined by EXACTLY TWO trails, since m12+m13=m12+m23=m13+m23=4.
* d=4: a loopless 4-regular multigraph with eight trail edges on four vertices. The single sparse vertex has two local pairs, each used by a trail of length two; no circuit fits on one sparse vertex. Hence exactly two trails have length two and six have length one.
* d=5: no sparse vertex; every column is its own trail and the trail graph is G itself.

Any closed circuits lie on the sparse vertices only: for d=2 they have length two or three, for d=3 length two, and for d=4,5 none exist. Lengths obey sum of trail lengths plus sum of circuit lengths = 10. These are exact graph facts, not an enumeration of candidate frames.

## 6. Full-resolution counting interface with dense vertices

Assume ONE full TEN-class resolution. By Lemma D1 each dense vertex has its eight E4 cells in EIGHT distinct classes and is missed by exactly two classes. Each class has exactly four E4 cells, at most one per dense vertex, and at most two per sparse vertex; two only as an opposite-orientation pair. Every oriented trail or circuit plane carrying n cells is used by exactly n classes.

* d=5: every class has its four E4 cells at FOUR DISTINCT vertices, and every vertex is missed by exactly two classes.
* d=2: with n_2,n_1,n_0 the numbers of classes containing two, one or no dense cells, 2n_2+n_1=16 and n_2+n_1+n_0=10. Hence n_2=6+n_0 and at least SIX classes contain one cell at EACH dense vertex.

A class containing a cell x in trail plane A_i at one dense end and a cell y in the complementary plane at the other end of the SAME trail is automatically orthogonal; it uses distinct columns iff that trail has length at least two. Every other combination requires a coupled orthogonality. These are necessary conditions only.

## 7. Exact frontier and imports

New paid results: Lemma D1 (one dense cell per transversal); the complete projection-trail decomposition with the oriented-plane bound; Theorem D2, excluding EVERY sector frame with exactly one dense vertex; the exact trail graphs for d=2,3,4,5; and the dense resolution-counting interface. Together with v81 (two/three circuits), v84 (FIGURE-EIGHT) and the open v82-v84 residuals, the v76 graph frontier is now: d=0 residual sparse topologies BARBELL/THETA(1,1,3)/THETA(1,2,2)/C5, OR d in {2,3,4,5} with the trail structure above. Other sector placements, minimal-rank-3 physical and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution remain unpaid. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: ENTIRE v76 actual graph/column complements, v77 complete local SPARSE/DENSE classification and strict traces, v80 oriented-plane argument, and the actual primary TEN-transversal/CLASSICAL-mate interface for section6. No NR/classifier/Butson/Gaussian/code premise, measure genericity, chosen trail orientation or global tensor WLOG. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S85, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history. Frozen Mainv17/S72/input map/proofs/live151 stay immutable.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
