# b63 family 1, part 2: normal form v1

Written after host clock 2026-10-19T21:47:21-0700 by ContinuePA19d. Uses only part1-ingredients-v1.md (same directory) and the family definition frozen in scope-v1.md.

## N1. Columns, pairs, category
Let an array of family 1 be given. g={0,1,2} has pattern (1,2,0), so by L2 the category is T2, g lies in the unique occupancy-2 P1 triple tau, both P0 triples of g (columns 3 and 4; g is in Q0,Q1,Q2) have occupancy 2, and g's other P1 triple tau' has occupancy 1. g's pair partner is T-disjoint from g, so it is z=34 or p3; p3 would be a private pair endpoint, impossible in T2 by L1. Name the P1 columns A,B,C by g's blocks: pair(A)={g,z}, tau={g,e1,e2} in B (one nonempty row, as eps=2), tau' in C. The nonempty member of tau' other than g is T-disjoint from g and not z (met in A), so tau'={g,p3,e3}. By the family definition the pairs of B and C are {13,24} and {14,23}. The map 1<->2 (13<->23, 14<->24, p1<->p2; g,04,z,p0,p0',p3 fixed) preserves the type list, profiles and Q-sets, fixes g and therefore the names A,B,C, and exchanges the two pairs. So assume
pair(A)={g,z}, pair(B)={13,24}, pair(C)={14,23}.
04 lies in no pair.

## N2. Patterns
z,13,24,14,23 have pattern (1,1,1): z has its quad and triple in B,C; 13,24 in A,C; 14,23 in A,B. 04 has (0,3,0). Every private has (0,2,1) (all pairs are used). Empties have (0,1,2).

## N3. Incidence equalities
In T2 every P0 column is (2,2,1,1,1) and every quad is >=2. Write x(r) for the number of P0 triples of r with occupancy 2.
- p3: I=7 with four P0 triples (>=4), tau' (1), its quad (>=2): so its quad has occupancy 2, its other P1 triple occupancy 0, and x(p3)=0. Its quad and other triple are in A,B.
- A private q other than p3 (q is not in tau or tau'): x(q)+eps(quad)+eps(triple1)+eps(triple2)=3 with eps(quad) in {2,3}.
- A (1,1,1) row r: x(r)+eps(quad)+eps(triple)=4 (three P0 triples; its triple is not tau).
- 04: x(04)+(sum of its three P1 triple occupancies)=4.

## N4. Quad/triple position counts
Let h_X be the number of nonempty positions in the two quads of column X (a quad of occupancy 3 has one nonempty row, of occupancy 2 two). As quads are (3,3,2,2,2,2), h_A+h_B+h_C=10 and each h_X in {2,3,4}. Let n_XY be the number of empty rows with quads in X and Y (triple in the third column). Counting nonempty positions in each column:
- A: 10 nonempty rows besides g,z, so the A-triples hold 10-h_A nonempty and n_BC=h_A-1 empties.
- B: 9 nonempty rows besides 13,24,g, so n_AC=2+(occupancy of the two B-triples other than tau)=h_B-1.
- C: 8 nonempty rows besides 14,23,g,p3, so n_AB=1+(occupancy of the two C-triples other than tau')=h_C-1.
Since e1,e2 have triples in B, n_AC>=2 and h_B>=3; e3 gives n_AB>=1. e1,e2 already agree in tau, so their A-quads differ and their C-quads differ.

## N5. Compatibility table
Two-type rows: the only T-disjoint pairs are 04-13, 04-23, 13-24, 14-23; z is T-disjoint from no two-type. 13-24 and 14-23 have already agreed. Private compatibility by type: p0,p0' with 13,14,23,24,z,p1,p2,p3 (p0-p0' share Q0); p1 with 04,23,24,z,p0,p0',p2,p3; p2 with 04,13,14,z,p0,p0',p1,p3; p3 with 04,14,24,p0,p0',p1,p2.

## N6. P0 column 0
Outside Q0 the nonempty rows are 13,14,23,24,z,p1,p2,p3. No two of 13,14,23,24,z can share a column-0 triple (N5), so each of the five column-0 triples contains exactly one of them. The (2,2,1,1,1) pattern means two triples have one nonempty row and three have two; hence p1,p2,p3 lie in the three occupancy-1 triples, one each, each with one of 13,14,23,24,z, and the remaining two of these five rows are the nonempty members of the two occupancy-2 column-0 triples. p3's partner there is 14 or 24 (T-disjoint from {3}); p1's is 23, 24 or z; p2's is 13, 14 or z.

## N7. P0 columns 3 and 4
Column 3: outside Q3 the nonempty rows are g,04,14,24,p0,p0',p1,p2; g is alone in an occupancy-2 triple (N1), so the other seven form three compatible pairs and one single. Column 4: outside Q4 they are g,13,23,p0,p0',p1,p2,p3; again g is alone and the other seven form three pairs and one single.
