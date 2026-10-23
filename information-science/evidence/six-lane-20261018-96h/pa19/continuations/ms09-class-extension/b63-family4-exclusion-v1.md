# PA19 ms09 b63 residual family 4 excluded: written proof v1

Written after host clock 2026-10-19T18:21:03-0700 by ContinuePA19d (info-1, scope-v1.md SHA256 27b13a5c19b9bc7dc885d7fc52030796dcacc53bff8dcf707c1f1d232fa7b269). Status: CANDIDATE written proof, unreviewed. It closes ONE of the six residual families listed in b63-reduction-v1.md Section 2 (SHA256 6be58b9a82078ac9ed8df4fa4dc80d86ea91038b65885416087b05ef3a5c2aa9; header-clock erratum 68c1ddd04d699890efacca2e0e8210b27a2329759fbd27d623a4f112a58d46c9 retained): family 4 = G2-Q1-(a) with occupancy-2 K_B, for both choices of L_B and every identity. **b63 as a whole remains UNDECIDED** (families 1,2,3,5,6 open). Written only; no computation, enumeration, script or assertion.

Premises: Section 1 of class-theorem-v1.md (SHA256 6343c3da3ed6c8a29da6216d90d46db7f9f095ea3726bd8e4a1173f05c9b954c) and lemmas B2, B4, B6, B7, B9 of b63-reduction-v1.md, used as stated there. "Compatible" means T-disjoint and not yet agreeing in any block; every P1 triple consists of pairwise compatible rows (exact pair cover).

## 1. The family-4 normal form (from B9) and three general consequences

Notation of B9: pair(A)={g,p3}, pair(B)={g,z}, pair(C)={x,y} (two 2-types, pattern (1,1,1)); K_z={z,e0,u1,va} and K'_A={x,u2,vb,vc} are the occupancy-3 A-quads; the B-quads are {s_L,p3,.,.} = L_B and {s_K,y,.,.} = K_B with empty sets {va,vb} and {vc,u3} in either assignment; H_C={g,u1,u2,u3}, L_C={p3,r1,r2,e0}; {s_L,s_K,e0} is a P0 triple; e0's B-triple contains x. The three 2-types other than z,x,y are called w's (pattern (0,3,0)). Both assignments of L_B are treated at once: nothing below depends on it.

**1a (triple empties).** An empty row's triple lies in the column without its quads: e0,u1,u2 have quads in A and C, so their triples are the three B-triples (each of occupancy 1); u3 has quads in B and C, so the only nonzero A-triple is the occupancy-1 "u3-triple"; va,vb,vc carry the three C-triples (each occupancy 1). The other two A-triples have occupancy 0 and three nonempty rows each.

**1b (row distribution).** A-triples contain exactly s_L,s_K,r1,r2,y and the three w's (g,p3 are in pair(A); z,x in A-quads). By B7 s_L,s_K have occupancy-0 A-triples, and they agree in a P0 triple, so they lie in the two different occupancy-0 A-triples T_L,T_K; the u3-triple holds u3 and two rows of {r1,r2,y,w's}. B-triples contain exactly x,r1,r2 and the w's: e0's B-triple is {x,w_e,e0} with w_e a w (its third row is compatible with x and is not r1,r2, which met e0 in L_C); the other two B-triples each contain one of r1,r2 (they agree in L_C) and one of the two other w's. C-triples contain exactly z,s_L,s_K and the w's: z's only compatible nonempty rows are privates, so z's C-triple partner is s_L or s_K; the other s (call it s_o) shares a C-triple with one w, and the remaining two w's share the third C-triple, hence are T-disjoint.

**1c (private identities).** {r1,r2,s_L,s_K}={p0,p0',p1,p2}. r1,r2 share L_C and s_L,s_K share a P0 triple, so neither pair is {p0,p0'}. Write r1=p0*, r2=p_a, and {s_L,s_K}={p0*',p_b}, where {p0*,p0*'}={p0,p0'} and {a,b}={1,2}. y and s_K share K_B, so s_K is T-disjoint from y.

**1d (P0 partners of p3).** p3's P1 partners are g (pair), s_L (L_B), r1,r2 (L_C). Its T-disjoint rows are g,04,14,24,p0,p0',p1,p2, so its P0 partners are exactly 04,14,24,s_K, one in each of its occupancy-1 P0 triples (columns 0,1,2,4; B6). 04,14,24 lie in Q_4, so s_K is p3's column-4 partner: s_K's column-4 triple is {p3,s_K,.} with occupancy 1.

## 2. Orientations of the C-pair
The C-pair is one of 04-13, 04-23, 13-24, 14-23 (B7), and e0's B-triple needs a w compatible with x. Using the symmetry 1<->2 (13<->23, 14<->24, p1<->p2; it fixes g,z,p3,04,p0,p0' and every block named in B9), all orientations reduce to:
- (i) x=04, y=13, w's {14,23,24}, w_e=23;
- (ii) x=13, y=04, w's {14,23,24}, w_e=24;
- (iii) x=13, y=24, w's {04,14,23}, w_e=04.
The orientations x=24 (pair 13-24) and x=14 (pair 14-23) are impossible: no w is T-disjoint from x. The other orientations are the 1<->2 images of (i)-(iii).
In (i),(ii) the only T-disjoint pair of w's is 14-23, so {14,23,.} is a C-triple. In all three, the B-triples of the two w's other than w_e pair them with r's as forced by T-disjointness: 14 can only meet p0*,p2 and 23 only p0*,p1; 24 only p0*,p1. Hence

| case | a=1 (r's p0*,p1) | a=2 (r's p0*,p2) |
|---|---|---|
| (i) | 14-p0*, 24-p1 | 14-p2, 24-p0* |
| (ii),(iii) | 14-p0*, 23-p1 | 14-p2, 23-p0* |

## 3. Exclusion of every case

**(i), a=1.** s's are {p0*',p2}. The A-triple rows compatible with 14={1,4} are among p0*,p0*',p2,23; p0* met 14 in B and 23 met it in C. The remaining two are both s's, which already agree; so 14's A-triple has at most one other nonempty row, i.e. it is the u3-triple, whose other row must then be compatible with 14 and not an s. None exists.

**(i), a=2.** s's are {p0*',p1}; s_K is T-disjoint from y=13, so s_K=p0*', s_L=p1. 14's compatible A-rows are p0*,p0*' (p2 met in B, 23 in C), which share Q_0; so 14 is in the u3-triple with p0*. Then T_L needs two compatible partners of p1 among p0*',p2,13,23,24: p0*' met p1 in P0 and 13 shares index 1; p2,23,24 pairwise share index 2. Impossible.

**(ii), a=1.** s_K is T-disjoint from y=04, so s_K is p1 or p2; with s's {p0*',p2}, s_K=p2, s_L=p0*'. 14's compatible A-rows: p0*,p0*',p2,23 minus p0* (B) and 23 (C) leaves the two s's. Impossible as in (i), a=1.

**(ii), a=2.** s's {p0*',p1}, so s_K=p1, s_L=p0*'. 14's compatible A-rows are p0*,p0*' (p2 B, 23 C), so the u3-triple is {14,p0*,u3}. T_K needs two compatible partners of p1 among p0*',p2,04,23,24: p0*' (P0) and 04 (K_B) are excluded and p2,23,24 pairwise share index 2. Impossible.

**(iii), a=2.** s's {p0*',p1}, both T-disjoint from y=24. If s_K=p0*': its A-partners must avoid p1 (P0), 24 (K_B), 04,p0* (index 0), so they lie in {p2,14,23}; p2-14 met in B and p2,23 share index 2, so T_K={p0*',14,23}. If s_K=p1: T_L contains p0*', whose compatible rows are p2,14,23,24, and the only compatible pair among them is 14-23, so T_L={p0*',14,23}. Either way 14 and 23 meet in A, so the C-triple pair of w's is 04-23 and the C-triple {s_o,14,.} needs s_o in {p0*',p1} compatible with 14: p0*' met 14 in A and p1 shares index 1. Impossible.

**(iii), a=1.** s's {p0*',p2}; s_K must be T-disjoint from y=24, so s_K=p0*', s_L=p2. y=24's compatible A-rows are p0*,p0*',p1 minus p0*' (K_B); p0*,p1 share L_C, so 24 is in the u3-triple with p0* or p1.
- u3-triple {24,p1,u3}: T_L needs two compatible partners of p2 among p0*,04,14,23: 23 shares index 2, and p0*-04 (index 0), p0*-14 (B), 04-14 (index 4) are incompatible pairs. Impossible.
- u3-triple {24,p0*,u3}: T_L and T_K split {p1,04,14,23}; p2's only compatible pair there is {p1,04} (23 shares index 2; p1-14 index 1; 04-14 index 4). So T_L={p2,p1,04}, T_K={p0*',14,23}. As 14,23 meet in A, the C pair of w's is 04-23 and {s_o,14,.} is a C-triple with s_o compatible with 14: not p0*' (met in A), so s_o=p2 and z's C-partner is p0*'. Now use P0 partner lists (each row named below has all P0 triples of occupancy 1, so exactly one nonempty partner per P0 column):
 1. x=13 has occupancy-1 P0 triples (B9) in columns 0,2,4. Its T-disjoint rows are 04,24,p0,p0',p2; it met 24 (C-pair) and 04 (e0's B-triple), so its P0 partners are p0*,p0*',p2. Its column-0 options are 24 and p2, so p2 is in column 0. By 1d p0*''s column-4 triple contains p3, which shares Q_3 with 13; hence 13 meets p0*' in column 2 and p0* in column 4.
 2. p0* lies in the u3-triple, so its P1 contributions are 1 (L_C) + 1 (u3-triple) + 1 (B-triple), and I(p0*)=7 forces occupancy 1 in all four P0 triples (columns 1-4). Its T-disjoint rows are 13,14,23,24,z,p1,p2,p3; it met p3,p1 (L_C), 14 (B) and 24 (A). So its P0 partners are 13 (column 4 by step 1), 23 (23's P0 columns are 0,1,4: column 1), and z,p2 in columns 2,3; z lies in Q_3, so z is column 2 and p2 column 3.
 3. s_L=p2 has occupancy-1 P0 triples (B7) in columns 0,1,3,4. Its T-disjoint rows are 04,13,14,z,p0,p0',p1,p3; it met p3 (L_B), 14 (C-triple), p1 and 04 (T_L). So its P0 partners are 13 (column 0), p0* (column 3), z and p0*'. z's P0 columns are 0,1,2, so z is column 1 and p0*' is p2's column-4 partner.
 By 1d, p0*''s column-4 triple is {p3,p0*',.} with occupancy 1, so it has no room for p2 (and p0*' lies in only one column-4 triple). Contradiction.

Every orientation, both values of a and both choices of s_K are impossible, and the 1<->2 images follow by symmetry. Hence **residual family 4 contains no array.**

## 4. Boundary
The proof uses only block memberships, row patterns, the occupancy-1 P0 facts of B6/B7/B9 and T-disjointness; it does not use the empty-row labels of the two B-quads, so it covers both L_B assignments named in b63-reduction-v1.md family 4. Families 1 (G1, {13-24,14-23}), 2 (G1, {13-24,04-23}), 3 (G2-C0), 5 (G2-Q1-(a), occupancy-3 K_B) and 6 (G2-Q1-(b)) remain open. No ledger or count change; PA(19,8,6) UNDECIDED; candidate pending independent parent check and both-family review.
