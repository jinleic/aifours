# b63 family 1, part 1: re-derived general ingredients v1

Written after host clock 2026-10-19T21:45:31-0700 by ContinuePA19d under scope-v1.md (SHA256 e741e635262057612799190fdc151527e2967dda9ca76fc013bfbdbe963613ad). Self-contained; nothing from earlier candidate files is cited as a fact.

## 0. The b63 row model
Rows: g={0,1,2}; two-type rows 04,13,14,23,24 and z=34; private rows p0,p0' (two distinct rows of type {0}), p1,p2,p3; seven distinct empty rows forming E. (Degrees of the listed types at 0..4 are 2,3,3,3,4, so the number of type-{c} private rows is 4-deg(c) = 2,1,1,1,0.) An array is a 19x8 array over six symbols in which two distinct rows agree in at most one column; five columns P0 (indexed 0..4) have profile (4,3,3,3,3,3) with the size-4 class of column c equal to Q_c = {rows whose type contains c}:
Q0={g,04,p0,p0'}, Q1={g,13,14,p1}, Q2={g,23,24,p2}, Q3={13,23,z,p3}, Q4={04,14,24,z};
three columns P1 have profile (4,4,3,3,3,2). Symbol classes are blocks; eps(B) is the number of empty rows in block B; T(r) is the type of row r and t=|T(r)|.

## 1. Exact pair cover
Agreeing pairs counted with multiplicity: 5(C(4,2)+5C(3,2)) + 3(2C(4,2)+3C(3,2)+C(2,2)) = 5*21+3*22 = 171 = C(19,2). As no pair agrees twice, EVERY pair of rows agrees in exactly one column. Hence: rows with intersecting types agree in their common quad and nowhere else; every block other than a P0 quad consists of pairwise T-disjoint rows; two blocks of different columns share at most one row. Call two rows compatible if they are T-disjoint and have not yet agreed.

## 2. Row patterns
Let n_i be the number of P1 blocks of size i containing r. Its P0 blocks give 3t+2(5-t)=10+t distinct partners, so n2+n3+n4=3 and n2+2n3+3n4=8-t, i.e. n4-n2=2-t:
t=0: (n2,n3,n4)=(0,1,2); t=1: (0,2,1) or (1,0,2); t=2: (0,3,0) or (1,1,1); t=3: (1,2,0) or (2,0,1).
Empty rows lie in two P1 quads (different columns), one P1 triple and no pair; pair endpoints are nonempty.

## 3. Occupancy categories
Counting the 21 pairs inside E in their unique agreeing block: sum_B C(eps(B),2)=21. Each P0 column's five triples have occupancies summing to 7; the six P1 quads sum to 14; the nine P1 triples sum to 7 (Section 2); P0 quads and P1 pairs have occupancy 0. Moving one unit from x to y with x>=y+2 lowers sum C(.,2) by x-y-1>0, so the minimum costs are 2 per P0 column (2,2,1,1,1), 10 for the quads (3,3,2,2,2,2), 0 for the triples; total excess 21-20=1. Exactly one category holds (all other parts at their minimum lists):
- C3: one P0 column (3,1,1,1,1); C0: one P0 column (2,2,2,1,0);
- Q4: quads (4,2,2,2,2,2); Q1: quads (3,3,3,2,2,1);
- T2: one P1 triple has occupancy 2, all other P1 triples <=1.
(Exhaustiveness: a P0 column of cost 3 has m2+3m3=3, sum j m_j=7, sum m_j=5, giving only the C3/C0 lists; for quads, d_j=y_j-2 gives sum d_j=2 and sum C(y_j,2)=9+(1/2)sum d_j^2, so cost 11 means one +2 (Q4) or three +1 and one -1 (Q1); triple cost 1 means exactly one 2.)

## 4. Incidence
For nonempty r, I(r) := sum over blocks B containing r of eps(B) = 7 (r agrees once with each empty row). A triple containing a nonempty row has eps<=2; a quad containing one has eps<=3.
- (L1) A private pair endpoint has pattern (1,0,2) and lies in C0's occupancy-0 P0 triple or Q1's occupancy-1 quad; otherwise its four P0 triples and two quads give I>=4+4=8.
- (L2) A t=3 row with pattern (1,2,0): its two P0 triples give at most 2+2 and its two P1 triples at most 1+1 unless the category is T2 and the row lies in the occupancy-2 P1 triple. Hence the category is T2, the row lies in that triple, and I=7 forces: both its P0 triples have occupancy 2 and its other P1 triple occupancy 1.
