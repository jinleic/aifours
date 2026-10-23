# New P1-triple and case reductions v1

Written after host clock 2026-10-19T13:56:35-0700. Imports are rederived in imports-v1.md; no prior acceptance assumed. These are necessary conditions, not case closures.

## 1. Five all-triple two-types are impossible
Call a row an all-triple two-type if |T|=2 and its P1 pattern is (n2,n3,n4)=(0,3,0). Listed two-types are distinct two-element subsets of the five P0 indices. Their T-disjointness graph is an induced subgraph of the graph on the ten two-subsets, adjacent iff disjoint.

That ten-vertex graph has degree3 and no triangles or 4-cycles. A triangle would require three disjoint two-subsets of five elements. A 4-cycle would give two distinct vertices with two common neighbours: if two two-subsets meet, their union has size3 and there is exactly one possible two-subset in its complement; if they are disjoint, there is none. Thus two distinct vertices have at most one common neighbour.

Every induced subgraph on five vertices has at most five edges. If its maximum degree is at most2 this follows by summing degrees. Otherwise choose a degree3 vertex v. Its three neighbours are independent (no triangles). The remaining fifth vertex is not adjacent to v (degree in the full graph is3), and can be adjacent to at most one of those three neighbours (otherwise a 4-cycle). So in this case the subgraph has at most4 edges.

Suppose five all-triple two-types existed in an ms09 array. In each P1 column they lie among its three triples. A triple contains at most two of these rows (three disjoint two-types would require six indices). Hence at least two pairs of these five rows agree in each P1 column. Across three columns these are at least six distinct T-disjoint pairs, since no pair agrees twice. Their graph has at most five edges, contradiction.

**AT2 theorem:** At most FOUR distinct two-type rows can be all-triple in the three P1 columns. This proof uses the whole array quantifiers, not a selected placement.

**Equality for four:** Four such rows distributed among three triples require at least one agreeing pair per column. Their induced graph has at most3 edges (no triangle or4-cycle); therefore it must be a tree with exactly3 edges (a path or a star). Each P1 column contains exactly one of those three edges, all three edges are used once, and no P0 triple can contain either endpoint of any of those three edges together. Each P1 column's distribution of those four rows is exactly (2,1,1) across its triples.

## 2. b65: only category Q1 survives, with forced path structure
Name its t3 row g={0,1,2}, two-type rows a_i={i,3}, b_i={i,4} for i=0,1,2, and private rows p_i={i}, one each. Seven rows are empty.

R4 forces g to pattern (2,0,1), with pair partners p3,p4. Relabel P1 columns A,B,C so pairs in A and B are {g,p3} and {g,p4}; g is in a C-quad. R3 forces that quad to have eps3, hence it contains only g and three empties. Private rows p3,p4 have pattern (1,0,2), so both are in the other C-quad and agree there.

They both require the unique rescue block. It cannot be a P0 eps0 triple (category C0), because both would then also agree in that triple. C3,Q4,T2 provide no private rescue. Therefore the category is Q1. The other C-quad has eps1 and nonempty rows p3,p4,p_a, for some a in {0,1,2}: its third nonempty row must have type contained in {0,1,2}, cannot be g in the other C-quad, and every other listed type contains3 or4. Permuting indices0,1,2 allows a=0 without restricting the original array problem (explicit skeleton automorphism).

No private other than p3,p4 can be a pair endpoint. R1 would put it in the exceptional C-quad; the only candidate p0 cannot be in the C-pair and A/B pairs are already full. So the C-pair {x,y} consists of two disjoint two-types. Exactly x,y have P1 pattern (1,1,1); the other four two-types form a set U of all-triple rows.

The remaining A/B quads have eps multiset (3,3,2,2). The A-quad containing p4 and the B-quad containing p3 must each have eps2: their four P0 triples contribute at least4 and their C-quad contributes1; I=7 forces the other quad to contribute2, with all their P0 triples having eps1. Thus each of A/B has one eps3 quad and one eps2 quad. Their four additional nonempty quad positions contain p1,p2,x,y each once. The low A-quad contains p4 plus a row T-disjoint from {4}; the low B-quad contains p3 plus a row T-disjoint from {3}. This completely describes the P1 pair/quad NONEMPTY POSITION COUNTS; actual row assignment and all empty placements remain to be solved.

After fixing p0 in the exceptional quad, the C-pair has two orbits under the skeleton stabilizer (permutations1<->2 and3<->4, and swap A/B):
- I: {x,y}={a0,b1}={{0,3},{1,4}};
- II: {x,y}={a1,b2}={{1,3},{2,4}}.
This follows because any disjoint pair is {a_i,b_j}, i!=j, and either one of i,j is0 or neither is0.

In orbit I, U={b0,a1,a2,b2}={{0,4},{1,3},{2,3},{2,4}} and its disjointness graph is exactly the path a2--b0--a1--b2. In orbit II, U={a0,b0,b1,a2}={{0,3},{0,4},{1,4},{2,3}} and its graph is exactly b0--a2--b1--a0. The AT2 equality theorem forces one path edge in each P1 column, all three used once; the same edges can never agree in P0.

In C, g,p3,p4,p0 occupy the two quads and x,y the pair. Its triples contain U plus p1,p2, with one empty in each triple. Thus there is one U-edge and the remaining two U rows are paired with p1,p2.
- Orbit I: the middle edge b0--a1 is impossible in C: the remaining rows a2,b2 both contain2, so neither can be paired with p2. The C-edge is a2--b0 (then p1--b2,p2--a1) or a1--b2 (then p2--b0,p1--a2).
- Orbit II: the C-edge may be either outer edge or the middle edge at this reduction level. If it is b0--a2, the other pairs are p1--a0,p2--b1. If it is b1--a0, the other pairs are p2--b0,p1--a2. If it is a2--b1, the other pairs match p1,p2 bijectively with a0,b0 (both bijections T-disjoint).

These are exhaustive C-column NONEMPTY projection branches, not complete columns/arrays. No exclusion of b65 is claimed. Outstanding: assign the A/B quad positions and triples without repeating any N-N agreement; place actual E rows with their two-quad/one-triple pattern; and simultaneously complete all five P0 triple partitions. The original quantifiers are retained.

## 3. b63: three excess categories, two main branches
Name g={0,1,2}, z={3,4}; private rows p0,p0',p1,p2,p3; and other two-types {0,4},{1,3},{1,4},{2,3},{2,4}. There is no p4.

The only possible pair partners of g are p3 and z. There are two exhaustive cases:

**G1:** g has (1,2,0). R2 forces T2. No private pair endpoint exists in T2 by R1, so its pair partner is z. All other pair endpoints are two-types. Of the other five two-types exactly four are pair endpoints and one is all-triple. The two remaining pairs form a matching of size2 in the path
{2,4}--{1,3}--{0,4}--{2,3}--{1,4}.
The unmatched vertex is one of the three alternating vertices {2,4},{0,4},{1,4}. Indeed in a path of five vertices, deleting an even-position vertex leaves an odd component and cannot leave a perfect matching; deleting any odd-position vertex leaves even path components. Up to the exact skeleton symmetry1<->2 there are two unmatched-type branches: {0,4} or {1,4}. The eps2 P1 triple contains g as its ONLY nonempty row. The other P1 triple of g has eps1 and must contain p3 (the only remaining nonempty T-disjoint partner of g), with one empty. Both P0 triples of g have eps2.

**G2:** g has (2,0,1), with pairs {g,p3},{g,z} in distinct P1 columns A,B. Its C-quad has eps3. Private p3 requires C0 or Q1. Thus C3,Q4,T2 are impossible in this branch. Row z has (1,1,1). It is in the B-pair and cannot be in either C-quad: one contains g and three empties, the other contains p3 which shares Q3 with z. Therefore z's quad is in A and its triple in C. Row p3 has quads in B,C. The third pair cannot have two private endpoints: together with g's pair to z, this would leave only one of six two-types paired and FIVE all-triple two-types, contradicting AT2. Hence the third pair is two two-types, or one additional private plus one two-type.

No exclusion of G1 or G2 is claimed. In G2 the rescue block's actual members/location and the remaining pair still matter. No artificial first-column choice is imposed.

## 4. b66 and b68: private-pair bound and equality cases
Both have eight distinct two-types, four private rows and seven empty rows, with no t3 row. Let l be the number of private pair endpoints. Each private and two-type row has n2<=1 by the row-pattern identities, so all three pair blocks are disjoint as row sets. There are 6-l paired two-types and therefore 2+l all-triple two-types. AT2 implies l<=2, strengthening the crude rescue capacity l<=3.

In C3,Q4,T2, R1 gives l=0. In C0,Q1, l can only be0,1,2 at this reduction level; all l private pair endpoints must lie in the unique rescue block. Two private pair endpoints cannot form a pair with each other, since they already agree in that rescue block. If l=2 there are exactly four all-triple two-types: their induced disjointness graph must be a path or star with exactly three edges, one forced into each P1 column; none can occur in P0. If l=1 the three all-triple rows must still be distributed across the P1 triples but AT2 equality gives no forced edge. If l=0 only two all-triple rows are forced.

For b66 the private rows are p0,p0',p1,p2, so l=2 cannot use both p0,p0' (they share Q0 and could not both lie in the rescue block). For b68 the private rows are p0,p1,p2,p3. All these assertions preserve whole-case quantifiers; none is an array realization or a case exclusion.
