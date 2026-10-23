# b63 family 1, part 3: quad placement lemmas v1

Written after host clock 2026-10-19T21:56:22-0700 by ContinuePA19d. Uses part1 and part2 (same directory) only.

Let W={z,13,14,23,24}. Every two rows of W are incompatible (N5: they share an index, except 13-24 and 14-23, which already agreed in pair(B), pair(C)).

## Q1. One privates-only quad
Each W row has exactly one P1 quad (pattern (1,1,1)); g and 04 have none; each private has one. The six quads have 10 nonempty positions (quads (3,3,2,2,2,2)), filled by the 5 W rows and 5 privates. No quad holds two W rows, so the W rows lie in five distinct quads and exactly one quad, Fq, holds no W row (it holds one private if it has occupancy 3, two if occupancy 2). If Fq has occupancy 3, exactly one W row is alone in a quad and the other four share their quads with one private each; if Fq has occupancy 2, two W rows are alone and three share with a private. The quad column of z is B or C, of 13 and 24 is A or C, of 14 and 23 is A or B (N2); each column has two quads, so the numbers of W-quads in (A,B,C) form a permutation of (2,2,1), and Fq lies in the column with one W-quad.

## Q2. Single-row quads
Let a quad have occupancy 3, so it contains exactly one nonempty row r.
- r is not p3 (p3's quad has occupancy 2, N3).
- If r is a private, I(r)=7 forces x(r)=0 and BOTH P1 triples of r to have occupancy 0 (four P0 triples >=4, quad 3).
- If r is in W, x(r)+eps(triple of r)=1 (N3).

## Q3. Triple occupancies by h
From N4 and T2 (every P1 triple other than tau has occupancy <=1): the three A-triples have total occupancy h_A-1; the two B-triples other than tau total h_B-3; the two C-triples other than tau' total h_C-2. Hence: h_A=4 gives all A-triples occupancy 1; h_C=4 gives both such C-triples occupancy 1; h_B=3 gives both such B-triples occupancy 0. With h_B>=3 and h_C>=2 (N4), (h_A,h_B,h_C) is one of (4,4,2), (4,3,3), (3,4,3), (3,3,4), (2,4,4). The occupancy-3 quads lie in the columns with h<4.

## Q4. (4,4,2) is impossible
Both C-quads have occupancy 3 and one nonempty row each; the two C-triples other than tau' have occupancy 0 and three nonempty rows each. The eight nonempty rows of C outside pair(C) and tau' are z,13,24,04,p0,p0',p1,p2 (p3 is in tau'). If both C-quads held W rows, the two triples would contain the third W row w, 04, p0, p0', p1, p2. p0 and p0' cannot share a block (Q0) and neither can be with 04 (index 0), so 04's triple is {04, two of p1,p2,w} and the other triple holds p0 and p0' together unless 04's triple contains w; then w=13 (only 13 in W is compatible with 04), 04's triple is {13,04,p2} and the other triple again contains both p0,p0' (with p1). Either way p0,p0' share a block, impossible. So some C-quad is Fq with a single private q, and by Q2 q's A-triple has occupancy 0, contradicting h_A=4 (Q3).

## Q5. Fq has occupancy 2 in (4,3,3), (3,3,4) and (2,4,4)
If Fq had occupancy 3 with private q in column X, Q2 requires occupancy-0 triples of q in both other columns. In (4,3,3) the high quads are in B and C and h_A=4 leaves no occupancy-0 A-triple. In (3,3,4) the high quads are in A and B and h_C=4 leaves no occupancy-0 C-triple. In (2,4,4) the high quads are in A and h_C=4 again leaves none. Hence in these three options Fq has occupancy 2, and each occupancy-3 quad contains exactly one W row: in (4,3,3) one in B and one in C; in (3,3,4) one in A and one in B; in (2,4,4) both in A. In (3,4,3) both possibilities for Fq remain.
