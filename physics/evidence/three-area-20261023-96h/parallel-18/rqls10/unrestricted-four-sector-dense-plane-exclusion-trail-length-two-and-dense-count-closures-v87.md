# RQLS10 v87 — Dense plane exclusion: every trail has length at most two; d=2 with four long trails and d=3 with four long trails are impossible

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 18:56:43 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written unitary-entry/projection/graph/counting arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Domain

Use the ENTIRE v76 actual graph, the v77 SPARSE/DENSE classification, v85's trails (Lemma D1, Theorem D2: trails join distinct dense vertices) and v86's GLX. Let d >= 2 be the number of dense vertices. Assume ordinary MAX and ONE full TEN-class resolution wherever counts of classes are used. Nothing is chosen.

## 2. Theorem DX: dense plane exclusion

Let D be dense with row ONBs e_1,...,e_4 and f_1,...,f_4 and column planes A_i = span(e_i,f_i); W_ij = <e_i,f_j> has all off-diagonal entries nonzero and zero diagonal. Let x be a cell at ANY other vertex with x in A_i for some i. Then x is non-orthogonal to EVERY one of the eight cells at D.

Proof. Write x = alpha e_i + beta f_i. Then <e_i,x> = alpha and <f_i,x> = beta, while for j not equal to i

    <e_j,x> = beta W_ji,      <f_j,x> = alpha conj(W_ij),

because rows are orthonormal. Every vanishing case forces alpha=0 or beta=0, i.e. x proportional to f_i or e_i, the ray of an actual cell at D. That is a duplicate ray at another vertex, contradicting MAX.

Which cells lie in A_i structurally: if column i at D is an end of trail tau, then by v85 every sparse cell of tau carrying the SAME oriented plane as tau has at D lies in A_i. There are two such cells at each interior sparse vertex of tau: the tail cells when tau leaves D, the head cells when tau enters D. Call them the D-side cells of tau.

## 3. Theorem TL: in a full resolution every trail has length at most two

By D1, the eight cells of a dense vertex D lie in eight distinct classes, so EXACTLY TWO classes miss D. By DX, every D-side cell of every trail ending at D lies in a class missing D. The 2(L-1) D-side cells of one trail of length L share one oriented plane, so v85's oriented-plane bound puts them in distinct classes. Therefore

    2(L-1) <= 2,   i.e.   L <= 2,

for EVERY trail, for every d >= 2. Moreover the two classes missing D contain ALL D-side cells of ALL trails at D, at most one per trail-end plane in each class.

## 4. Consequences for each dense count

Let m be the number of length-two trails. Each sparse vertex has two local pairs; a length-two trail occupies one pair at its unique sparse vertex, and circuits among sparse vertices are vertex-simple. Every component must reach a dense vertex.

d=2 (dense D,D'; three sparse vertices; four trails D-D').
* m=4 is IMPOSSIBLE. The eight D-side cells fill the two D-missing classes with four sparse cells each. These classes contain no dense cell, so they are ALSO the two D'-missing classes. They must then also contain the eight D'-side cells, which is impossible.
* m=0 is impossible: all sparse vertices would lie on circuits only and be disconnected from D,D'.
* m=3: the remaining three pair-slots carry ONE three-circuit C through all sparse vertices; each sparse vertex carries one length-two trail; the fourth trail is a direct D-D' edge. The six D-side cells split three per D-missing class, and likewise the six D'-side cells. A class missing BOTH would need six sparse cells, so the four classes are distinct. Each D-missing class is {one D'-cell, three D-side cells, one per long trail}, and each D'-missing class is {one D-cell, three D'-side cells}. Counting the 24 sparse cells then forces the other SIX classes to be exactly {one D-cell, one D'-cell, one C+ cell, one C- cell}. By GLX, a C-cell at sparse s_k excludes, in its class, the dense cells of trail tau_k's columns.
* m=2: the two circuits are two-circuits sharing one sparse vertex; m=1: a three-circuit plus a two-circuit. Both remain OPEN.

d=3 (three dense, two sparse, four pair-slots, six trails with exactly two between each dense pair).
* (m,c)=(0,2) with two two-circuits is disconnected, hence impossible.
* m=4 is IMPOSSIBLE. The eight length-two trail ends are distributed over the three dense vertices. A dense vertex with FOUR such ends fills its two missing classes with four D-side sparse cells each; those classes then miss ALL dense vertices, so every other dense vertex with a long-trail end would need its D-side cells in these already full classes. With at most three ends per vertex the only distribution is (3,3,2), say at D1,D2,D3. Each D1-missing class holds exactly three D1-side cells (three distinct trail planes) plus ONE further cell, so it misses D1 and at least one of D2,D3. Missing D2 would require three more D2-side cells; missing D3 would require two more D3-side cells (four D3-side cells in two classes, at most two per class). Either overflows a four-cell class. Contradiction. D-side cells of different dense vertices are distinct cells, so no overlap rescues the count.
* Hence d=3 forces EXACTLY two length-two trails, one through each sparse vertex, and one two-circuit between the sparse vertices. Existence remains OPEN.

d=4 (one sparse vertex s). Both trails through s have length two: tau from D_a to D_b and tau' from D_c to D_d. Two cells at s in one class must belong to one route. If D_a were an end of tau' as well, the two D_a-missing classes would need both tau's and tau''s D_a-side cells, i.e. four distinct classes. Hence {D_a,D_b} and {D_c,D_d} are DISJOINT: the two long trails join COMPLEMENTARY pairs of dense vertices. Each class misses exactly as many dense vertices as it has cells at s. Existence remains OPEN.

d=5. No sparse vertex exists, DX is vacuous and the case remains OPEN.

## 5. THETA(1,2,2) forced isoclinicity (all-sparse addendum)

By v86 route avoidance, X-cells at v2 (partner a) can lie only in {X,Y} or {X,b} classes, and X-cells at v4 only in {X,Y} or {X,a} classes. Similarly Y-cells at v3 lie only in {X,Y} or {Y,b}, and Y-cells at v5 only in {X,Y} or {Y,a}. Every adjacent 2+2 class forces its pair interior-isoclinic (v86). Hence a full resolution requires

    X/Y interior-isoclinic, OR all four of X/a, X/b, Y/a, Y/b interior-isoclinic.

If X/Y is the ONLY isoclinic adjacent pair, the eight X-cells at v2,v4 and the eight Y-cells at v3,v5 fill EXACTLY four {X,Y} classes. X-cells at v1 then lie only in {X,a,b} classes, and Y-cells at v1 only in {Y,a,b} classes.

## 6. Exact frontier and imports

New paid results: Theorem DX; Theorem TL (all trails have length at most two in any full resolution); impossibility of d=2 with m=4 and of d=3 with m=4; the exact rigid d=2,m=3 class pattern; the exact d=3 and d=4 residual structures; and THETA(1,2,2) forced isoclinicity. The v76-graph frontier is now: all-sparse residuals (BARBELL, THETA(1,1,3) three cases, THETA(1,2,2), C5); d=2 with m in {1,2,3}; d=3 with m=2; d=4 with complementary long trails; and d=5. Other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution remain unpaid. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: ENTIRE v76/v77 graph and local frames, v80 oriented-plane bound, v85 D1/D2/trails, v86 GLX/route avoidance/vertex form, and the actual primary TEN-transversal/CLASSICAL-mate interface. No NR/classifier/Butson/Gaussian/code premise, measure genericity, chosen frame or global tensor WLOG. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S87, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the disclosed v29 parallel-intent minor and the v30 dangling-reference defect. Frozen Mainv17/S72/input map/proofs/live151 stay immutable.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
