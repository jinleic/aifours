# b63 family 1, part 4: B/C configuration lemmas and option (3,3,4) partial elimination v1

Written after host clock 2026-10-19T22:04:49-0700 by ContinuePA19d. Uses parts 1-3 (same directory) only. "Compatible" = T-disjoint and not yet agreed. All blocks below are P1 blocks other than the three pairs, tau and tau'. Quad sizes count nonempty rows (occupancy-3 quad: 1, occupancy-2: 2); triple sizes count nonempty rows (3 minus occupancy).

## L1. Column B when h_B=3 and Fq has occupancy 2
The nine nonempty rows z,14,23,04,p0,p0',p1,p2,p3 fill four blocks of sizes 1 (quad), 2 (quad), 3, 3 (triples of occupancy 0). z,14,23 lie in different blocks (W incompatible); call the fourth block B4. 04 is in a triple, compatible in B only with 23,p1,p2,p3, so 04 is in 23's block or in B4. p0,p0' never share a block or sit with 04. The size-1 block is a W row alone (Fq has occupancy 2). Exhausting compatibilities gives exactly:
- (i) 23's block {23,04,p1} (p1 is the only row compatible with both), and
 (i-a1) {z}; {14,p0*,p2}; B4={p0*',p3} (quad);
 (i-a2) {z}; {14,p0*,p3}; B4={p0*',p2} (quad);
 (i-a3) {z}; {14,p0*} (quad); B4={p0*',p2,p3};
 (i-b1) {14}; {z,p0*,p2}; B4={p0*',p3} (quad);
 (i-b2) {14}; {z,p0*} (quad); B4={p0*',p2,p3};
- (ii) B4={04,a,b} with {a,b,r*}={p1,p2,p3}; the blocks of z,14,23 are {W} (quad), {W',p0*'} (quad), {W'',p0*,r*} (triple) with {W,W',W''}={z,14,23} and W'' compatible with r* (z: p1,p2; 14: p2,p3; 23: p1).
Here {p0*,p0*'}={p0,p0'} in either order. (In (i-a), B14 cannot be {14,p2,p3}: B4 would be {p0,p0'}; a size-2 B14 must take p0* so that B4 is a valid triple; similarly in (i-b).)

## L2. Column C when h_C=4
The eight rows z,13,24,04,p0,p0',p1,p2 fill four blocks of size 2 (two quads of occupancy 2, two triples of occupancy 1); z,13,24 are in different blocks; 04 (compatible in C only with 13,p1,p2) is in a triple. Hence either
- (C4a) {13,04} is a triple and the blocks {z,a}, {24,b}, {c,d} hold the four privates, two of these three blocks being quads; or
- (C4b) the fourth block is the triple {04,p_k} (k in {1,2}) and z,13,24 each have one of the other three privates, two of their blocks being quads.

## L3. Option (3,3,4): configurations (i-a1)-(i-b2) and (ii) with r*=p3 are impossible
In (3,3,4): h_A=3 (one A-quad with a single W row, one of occupancy 2), h_B=3, h_C=4, Fq has occupancy 2 (Q5). A row whose quad is in column X has triples in the other two columns; p3's quad is in A or B and has occupancy 2, and p3's other P1 triple has occupancy 0 (N3).
- (i-a1): B-quads are {z} and Fq={p0*',p3}, so 14,23 have A-quads, filling A; 13,24 then have C-quads and z a C-triple, so L2 gives (C4b); 04 already met p1 (in B), so the C-triple is {04,p2}. p2 has triples in B and C, hence an A-quad, which must be the occupancy-2 A-quad with 14 or 23: 23 shares index 2 and 14 already met p2 in B. Contradiction.
- (i-a2): as before 14,23 fill A and C uses (C4b) with {04,p2}. p3's B-block is a triple, so its quad is in A, with 14 (met in B) or 23 (shares 3). Contradiction.
- (i-a3): B-quads {z},{14,p0*}; 23 has an A-quad; p3 (in the B-triple B4) has an A-quad, whose partner cannot be 13 or 23 (index 3). (C4a): the C-quads are 24's and Fq, so A's quads are 23's and 13's, leaving no place for p3. (C4b): 04 met p1, so the triple is {04,p2}; C-quads are 13's and 24's, so A holds 23's quad and Fq, which must contain p3 and p2 (p2's B- and C-blocks are triples); but p2,p3 met in B4. Contradiction.
- (i-b1): B-quads {14}, Fq={p0*',p3}; z has a C-quad, 23 an A-quad; p0*' and p3 have A-triples; p3's A-triple must have occupancy 0. In (C4a) 13 has an A-quad and the C-quads are z's and 24's; z's partner avoids p0*,p2 (met in B) and p0*' (which needs a C-triple), so it is p1; then 24's C-quad partner is p0* and {p0*',p2} is a C-triple, so p2 has an A-quad, which must be {13,p2}. In (C4b) 04 met p1, so the triple is {04,p2}; z's C-quad partner is again p1, and p2 (triples in B and C) needs an A-quad, which must be with 13. In both cases 04's A-triple can contain none of 13,23,p2 (quads), p1 (met in B); only p3 remains, so 04's A-triple is {04,p3}, of occupancy 1, contradicting occupancy 0 for p3's A-triple.
- (i-b2): B-quads {14},{z,p0*}; z has a C-triple; 23 an A-quad; p3 (B-triple) an A-quad. (C4a): C-quads are 24's and Fq, so A's quads are 23's and 13's, no place for p3. (C4b): the C-triple is {04,p2}; p0* (B-quad) needs a C-triple, so it is z's C-partner, but z met p0* in B. Contradiction.
- (ii) with r*=p3 (W''=14): B={14,p0*,p3}, B4={04,p1,p2}; 14 has an A-quad and p3 (B-triple) an A-quad whose partner is 24 or Fq (14 met p3; 13 shares 3). (C4b) is impossible because 04 already met p1 and p2. (C4a): z has a C-triple, so the C-quads are 24's and Fq; then A's quads are 14's and 13's, leaving no place for p3. Contradiction.

## L4. Option (3,3,4), configuration (ii) with r*=p1, W''=z: partial
B-blocks: {z,p0*,p1}, B4={04,p2,p3} (triples of occupancy 0), and {W},{W',p0*'} quads with {W,W'}={14,23}. z has a C-quad; p3 an A-quad; p0*' (B-quad) needs triples in A and C.
- (C4a) with C-quads z's and 24's: A's only W-quad is 13's, so A-quads are {13} and Fq={p3,q}; q and p0*' both need C-triples, so {p0*',q} is the C-triple besides {13,04}; z's C-partner avoids p0*,p1 (met), so it is p2, forcing q=p1 and 24's C-partner p0*. In A, 04's triple must be {23,04} (p1 is in a quad, p2 met 04); then 14's and 24's triples are {14,p2,p0*} and {24,p0*'} (24 met p0* in C). Now p0*' has quad occupancy 2 and two triples of occupancy 1, so x(p0*')=3-2-1-1<0. Contradiction.
- (C4a) with C-quads z's and Fq: 24's C-block is the triple {24,b} with b=p0*' (the only private needing a C-triple there); z's C-partner is p2; then Fq_C={p0*,p1}, but p0*,p1 met in B. Contradiction.
- (C4b): the triple is {04,p1} (04 met p2,p3 in B). If z's and 13's blocks are the C-quads: forced C={04,p1},{z,p2},{13,p0*},{24,p0*'}; A-quads {24} (alone) and Fq={p1,p3}; x(p0*')=0 forces p0*' into the occupancy-0 A-triple. Exactly two A-arrangements exist: S1: {13,04},{14,p2,p0*'},{23,p0*} (then W'=23, W=14); S2: {23,04},{13,p0*',p2},{14,p0*}.
  S1 is impossible: x(p1)=0 (quad 2, B-triple 0, C-triple 1). p0*' (x=0) has already met 23,24,14,p2 and must meet 13,z,p1,p3 in its four P0 triples; in column 3 its menu is {14,24,p1,p2}, so it meets p1 there. Then p1's column-2 menu {04,z,p0,p0',p3} is exhausted (04 in C, z and p0* in B, p3 in A, p0*' in column 3), so p1 is alone in a column-2 triple, contradicting x(p1)=0.
  S2 and the C-quad choice {z's, 24's} remain open (see residual-v1.md).
