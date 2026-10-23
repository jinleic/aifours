# P0 rainbow and actual-empty constraints v1

Written after host clock 2026-10-19T14:00:53-0700. These exclude only the explicitly described branches, not a whole named case.

## 1. Empty incidence graph (all four cases)
Represent the six P1 quads by six vertices, in three parts of size2 (one part per P1 column). Each empty row belongs to exactly two P1 quads in different columns, so represent it by an edge between those two vertices. Two empty rows cannot give the same edge: that would make the two rows agree in both columns. Thus this is a SIMPLE tripartite graph on six vertices with seven labelled edges (the actual empty rows). Its vertex degrees are precisely the six quad-eps values in the occupancy classification. An edge's unique missing P1 column determines the P1 triple in which its empty row must appear. This construction is necessary; not every such graph gives an array.

If a nonempty row r lies in a P1 quad H with eps3 and its remaining empty partners must occur in exactly two P0 triples, then E minus H (four rows) must have a perfect matching of pairs NOT already agreeing in any P1 block. Indeed its two P0 triples contain r and two empties each; they partition its remaining four empty partners by exactness. Two empties already agreeing in P1 cannot agree again in a P0 triple. This is a test on the ACTUAL seven empty rows, not merely on numbers of empty positions.

## 2. b65: at least one high-quad row must be in a zero-empty P1 triple
Use reductions-v1's normal form: C-quads H_C={g}+U, |U|=3, and L_C={p0,p3,p4,e0}. The remaining empties V=E minus (U union {e0}) have size3. The other P1 columns A,B each have an eps3 high quad and eps2 low quad, with p4 in the low A-quad and p3 in the low B-quad.

First, the high A/B nonempty rows cannot be p1 or p2. Such a private row has pattern (0,2,1), its quad would contribute3 to I, its C-triple contributes1 (all C-triples have eps1), and its four P0 triples contribute at least4, giving I>=8. Therefore the high rows are exactly x,y (the two-type endpoints of the C-pair), one per high quad. The low A/B additional rows are p1,p2, one each.

The row e0 lies in another quad besides L_C. It cannot lie in the low A-quad: p4 would then agree with it in A and C. Similarly it cannot lie in the low B-quad (p3). It therefore lies in a high quad. Interchange the names of A,B for this paragraph if necessary, and suppose e0 is in H_A. (This interchange does not assert any unproved skeleton symmetry or decide which of x,y lies there.)

Every v in V already belongs to a C-triple, so it belongs to one A-quad and one B-quad. The A-quads contain5 empties, of which V contributes3 and e0 contributes1. Exactly one row u in U has its other quad in A; the other two have it in B. Thus E minus (H_B union L_B)={e0,u}: these are exactly the two empties appearing in B-triples.

If u were in L_A, H_A would contain e0 and two members of V. These three members of E minus U already agree pairwise in H_A. On four vertices, any partition into two pairs has one pair within a given set of three vertices. Hence E minus U has no perfect matching avoiding P1 agreement. But g has its eps3 quad H_C and its two eps2 P0 triples (reductions R3), so the matching requirement in Section1 forbids this. Therefore u lies in H_A.

Both empties appearing in B-triples (e0,u) now belong to H_A. Its unique nonempty row r has no B-quad (x and y each have only one P1 quad), and is not in the B-pair (that contains g and a private). Thus r is in a B-triple. If that triple contained an empty, it would be e0 or u, already agreeing with r in H_A. Therefore r's B-triple must have eps0.

Conclusion: whichever high A/B quad contains e0 has its two-type nonempty row in the OTHER column's unique zero-empty P1 triple. This is a new necessary relation between the actual empty graph and the nonempty projection; it is not implied by eps counts alone. It leaves written branches open.

## 3. A P0 rainbow/capacity obstruction
For b65, Q3={a0,a1,a2,p3} and Q4={b0,b1,b2,p4} are disjoint. Row g lies in an eps2 triple of each P0 column3 and4. Fix column4. Its four Q3 rows must be in four distinct triples: they already agree with each other in P0 column3. The fifth triple contains g and two empties. Thus every remaining nonempty row outside Q4 and distinct from g must share its column4 triple with one Q3 row. If it has already agreed with all four Q3 rows elsewhere, this is impossible. The column3 statement with Q3/Q4 interchanged is identical.

For example the following b65 P1 NONEMPTY projection is excluded for EVERY filling of its E slots. The displayed eps values only specify the number of missing empty rows; they are NOT names of actual empty rows, and this is NOT a valid array or a full extension witness. Short labels ij mean the two-type row {i,j}.

| column | two quads: nonempty rows (eps) | three triples: nonempty rows (eps) | pair |
|---|---|---|---|
| A | {14}(3), {p4,p1}(2) | {13,p0,p2}(0), {04,23}(1), {24,03}(1) | {g,p3} |
| B | {03}(3), {p3,p2}(2) | {14,23,p0}(0), {04,13}(1), {24,p1}(1) | {g,p4} |
| C | {g}(3), {p0,p3,p4}(1) | {13,24}(1), {04,p2}(1), {23,p1}(1) | {03,14} |

Proof of exclusion: p0 has already agreed with a0=03 in Q0; with a1=13 in A's first triple; with a2=23 in B's first triple; and with p3 in C's second quad. This exhausts Q3. But p0 is outside Q4, is not g, and must share its P0-column4 triple with a Q3 row by the preceding capacity argument. Contradiction. No assertion that every remaining b65 projection has this form is made.

## 4. Exact unresolved extension obligations (not an obstruction theorem)
The scalar five-category classification is exhaustive. It does NOT enumerate all compatible assignments of named rows or actual empty edges. A complete exclusion would still need to refute EVERY remaining choice below.

| case | exhaustive remaining top-level split | genuinely unresolved choices |
|---|---|---|
| b63 | G1/T2 (two unmatched-type orbits), or G2/C0,Q1 | G1: placement of the two remaining matching edges into P1 columns; all quads/triples and actual empty rows. G2: rescue block location/members, remaining pair (two types or private+type), quads/triples and empties. Both branches still need all five P0 triple partitions. |
| b65 | Q1 only; two C-pair orbits and the C-projection branches in reductions-v1 | Allocate x,y to high A/B quads and p1,p2 to low A/B quads; complete A/B triples with all-triple path edges assigned once each; impose the high-quad/zero-triple relation in Section2 for either location of e0; fill the seven actual empty rows; complete P0 triples. Section3 removes only its displayed branch. |
| b66 | C3,C0,Q4,Q1,T2; l<=2 private pair endpoints | In C3,Q4,T2, l=0. In C0,Q1, choose l=0,1,2 and the unique rescue block, which cannot contain both p0,p0'. If l=2, the four all-triple two-types must induce a path/star and its three edges are forced once each into P1. All remaining actual block and empty-row choices, including P0, are unresolved. |
| b68 | same five categories and l<=2 | Same obligations, with private rows p0,p1,p2,p3 (all distinct types). No l=0/1/2 branch is certified feasible or impossible in general. |

Exact completion criterion: choose the six blocks of each P1 column with the stipulated sizes, row patterns, T-disjointness and no repeated pair; choose the five triples partitioning the complement of each fixed Q_c. Every row is used once per column; every pair is used at most once over ALL eight columns. Together with the fixed quads and profiles these conditions are equivalent to a valid original array: assigning a distinct symbol to each of a column's six blocks produces the array, and every valid array produces those blocks. No compatibility condition between the chosen P0 and P1 parts may be dropped. The new necessary reductions merely restrict this equivalent completion problem; no solution/non-solution to a weaker projection is promoted to a whole-case verdict.

**Disposition:** zero whole cases closed by this continuation. New written partial results are AT2, its equality path/star forcing, l<=2 for b66/b68, the refined b63 matching split, b65 high/low-quad placement and zero-triple condition, and the explicit P0-incompatible branch. All four current cases remain UNDECIDED. No e2 expansion.
