# PA19 ms09 b63 residual family 5 excluded: written proof v1

Written after host clock 2026-10-19T18:30:39-0700 by ContinuePA19d. Scope: scope-v1.md SHA256 27b13a5c19b9bc7dc885d7fc52030796dcacc53bff8dcf707c1f1d232fa7b269. Status: CANDIDATE written proof, unreviewed. Claim: residual family 5 of b63-reduction-v1.md Section 2, G2-Q1-(a) with occupancy-3 K_B, contains no array. This does NOT close b63: families 1,2,3,6 remain open (family 4 is addressed separately by b63-family4-exclusion-v1.md). No computation, enumeration program, scientific script or assertion was used: the finite compatibility cases below are written proofs.

Dependencies supplied in the review packet: class-theorem-v1.md Section 1 (SHA256 6343c3da3ed6c8a29da6216d90d46db7f9f095ea3726bd8e4a1173f05c9b954c) and b63-reduction-v1.md B1-B8 (SHA256 6be58b9a82078ac9ed8df4fa4dc80d86ea91038b65885416087b05ef3a5c2aa9; timestamp erratum 68c1ddd04d699890efacca2e0e8210b27a2329759fbd27d623a4f112a58d46c9 retained). No earlier candidate acceptance is assumed.

## 1. Normalization and the two position types

Use B2/B4/B6/B7: pair(A)={g,p3}, pair(B)={g,z}, pair(C)={x,y}; H_C={g}+U (three empties), L_C={p3,r1,r2,e0}; L_B is p3's occupancy-2 B-quad and K_B the occupancy-3 B-quad. C-triples have occupancy 1. The A-quads have occupancies 3 and 2. The remaining four privates are r1,r2 (C-quads) and s1,s2 (A/B occupancy-2 quads; their non-C triples have occupancy 0 and all P0 triples occupancy 1, B7). Both s's cannot lie in the occupancy-2 A-quad: then both would also lie in the unique occupancy-0 B-triple and agree twice. Hence one, s_L, is the other nonempty row of L_B; the other, s_A, lies in the occupancy-2 A-quad.

Let xi be the C-pair row with an A-quad, and kappa the one in K_B. Exactly two position types are possible:
- Type I: occupancy-3 A-quad K_z contains z alone; occupancy-2 A-quad contains s_A,xi; K_B contains kappa alone.
- Type II: occupancy-2 A-quad contains z,s_A; occupancy-3 A-quad contains xi alone; K_B contains kappa alone.
These exhaust the positions because z's quad is in A, the other quad-bearing nonempty rows are precisely s_L,s_A and the two C-pair endpoints, and all free positions are full.

The other quad of e0 is neither L_B (it would meet p3 twice) nor the occupancy-2 A-quad: in the latter case the number f(e0) of occupancy-1 P0 triples through e0 would be 1+2-3=0 (its two quads' occupancies minus 3; no P1 triple has two empties), but s_L has all P0 triples of occupancy 1 and cannot meet e0 in P1 (L_B excludes it, its A-triple is empty-free, its C-block is a triple while e0's is L_C). Thus e0 is in the occupancy-3 A-quad or K_B, and f(e0)=1. Neither s_L nor s_A can meet e0 in P1 (s_A's B-triple is empty-free, its A-quad does not contain e0), so the unique occupancy-1 P0 triple through e0 is

    {s_L,s_A,e0}.                                                (E)

Consequently s_L,s_A have distinct singleton types. As r1,r2 also have distinct types (they share L_C), write

    {r1,r2}={O,p_a}, {s_L,s_A}={O',p_b}, {a,b}={1,2},

where O,O' are p0,p0' in either order. We shorten p1,p2 to 1,2 in all tables below; O,O',1,2 are private ROWS; 04,13,14,23,24 are two-type ROWS, not symbol or column names.

Let A0,B0 be the unique occupancy-0 triples of A,B. A0 contains s_L and B0 contains s_A. They cannot contain the other s (which met in (E)). The three two-types other than z,xi,kappa are called w's. A-triple rows, in both types, are {s_L,kappa,r1,r2,w's}; B-triple rows are {s_A,xi,r1,r2,w's}; C-triple rows are {z,s_L,s_A,w's}. All triple pairs must be T-disjoint and not already met. Each C-triple contains an empty and two nonempty rows; z's mate must be an s (every w meets z's type 34). The other s is paired with one w, and the remaining two w's form a T-disjoint C-pair.

The C-pair xi-kappa is an edge of 24-13-04-23-14. Up to 1<->2 symmetry, it is E1={04,13} or E3={13,24}, in either orientation. E1 leaves w's {14,23,24}, whose ONLY disjoint pair is 14-23; E3 leaves {04,14,23}, with disjoint pairs 04-23 or 14-23. The 1<->2 map fixes g,z,p3,O,O' and relabels privates 1,2; all values of a,b below are retained.

## 2. Type I is impossible

z's A-quad has occupancy 3 and its C-triple occupancy 1, so I(z)=7 forces all its P0 triples to have occupancy 1. If e0 were in K_B, z would not meet it in P1 and would have to lie in the unique triple (E), impossible. Thus e0 lies in K_z. The high C-pair row kappa cannot meet e0 in P1; it is not in (E), so it meets e0 as the nonempty single of an occupancy-2 P0 triple. For a t=2 row whose quad has occupancy 3, the count of its occupancy-2 P0 triples is 1 minus the occupancy of its other P1 triple (I=7). Therefore kappa's A-triple has occupancy 0, so

    A0={s_L,kappa,m}.                                            (A)

By B8, precisely one U row has an A-quad and two have B-quads (A-quads contain 5 empties: V, e0 and one U row). Call their missing-column triple empties u_A and the two u_B's. B's nonzero triples are Be (carrying e0) and Bu (carrying u_A). Neither r is in Be (they met e0 in L_C); the r's are in different B-triples. xi is not in B0 (it met s_A in their A-quad). Thus B0={s_A,r_i,w0}, Bu={r_j,t,u_A}, and Be contains e0 and a compatible pair of {xi,w's}. Below B0 entries omit no row, while Be/Bu list their two nonempty rows. All possibilities are checked by the following hand case analysis; its small pair-partition checks are stated explicitly.

### 2.1 E1 orientations
E1's C w-pair is 14-23, so Be cannot use that pair.

**xi=04,kappa=13.** T-disjointness of s_A from 04 forces s_A=p_b, s_L=O'. Be must be 04-23 (04 meets 14 and 24). B0/Bu are forced:
- a=1,b=2: B0={2,O,14}, Bu=1-24. The other C-triple besides z's and the 14-23 one has the row 24. Its s cannot be 2, so it is O', and O'-24 already meet in C. But in (A), the only m compatible with O' and 13 among the A-rows is 24, impossible.
- a=2,b=1: B0={1,O,24}, Bu=2-14. The s paired with 24 in C is O' (1 already met 24 in B0). In (A) m is 24 or 2, so it must be 2. The four remaining A-rows are {O,14,23,24}; their only T-disjoint partition into two pairs is O-24 | 14-23, both already met (B0,C).

**xi=13,kappa=04.** T-disjointness of s_L from 04 forces s_L=p_b, s_A=O'. Be must be 13-24. Since O' and O share type 0, B0 uses r_i=p_a:
- a=1,b=2: B0={O',1,23}, Bu=O-14. In (A) m=1. Remaining A-rows {O,14,23,24} have only pair partition O-24 | 14-23, blocked by the C w-pair.
- a=2,b=1: B0={O',2,14}, Bu=O-23. In (A), m=2 or 23. If m=2, the same four-row partition is blocked by C. If m=23, remaining A-rows {O,2,14,24} have only T-disjoint pair partition O-24 | 2-14, blocked by B0.

### 2.2 E3 orientations
**xi=13,kappa=24.** The requirements s_A disjoint 13 and s_L disjoint 24 force s_A=2,s_L=O' when a=1, or s_A=O',s_L=1 when a=2.
- a=1: (A) forces m=1. Remaining A-rows {O,04,14,23} have only T-disjoint pair partition O-14 | 04-23. Hence C's w-pair must be 14-23, and Be cannot be either already-met w-pair, so Be=13-04. This forces B0={2,O,14}, repeating O-14 from A.
- a=2: (A) forces m=O. Remaining A-rows {2,04,14,23} have exactly the two T-disjoint pair partitions P=2-04 | 14-23 and Q=2-14 | 04-23. Be is one of 13-04,04-23,14-23. If Be=13-04, B0={O',2,14}; C's w-pair cannot be 04-23, since its leftover w=14 would have to meet an s in {O',1}, neither compatible (O' met 14 in B0; 1 meets 14's type). Thus C's pair is 14-23, blocking P, while B0 blocks Q. If Be=04-23, C's pair is 14-23 and Be/C block Q/P. If Be=14-23, C's pair is 04-23 and Be/C block P/Q.

**xi=24,kappa=13.** The requirements force s_A=1,s_L=O' (a=2) or s_A=O',s_L=2 (a=1). Since 24 meets every w, it is in Bu; Be is 04-23 or 14-23.
- a=2: Bu must be O-24; B0={1,2,04}, so Be=14-23. In (A) m=2, leaving {O,04,14,23}, whose only pair partition O-14 | 04-23 is blocked by C's w-pair 04-23.
- a=1: B0 containing O' cannot use r_i=O, so r_i=1 and Bu=O-24. Its only possible w0 is 23 (04 meets O',14 meets 1), leaving Be=04-14, not T-disjoint.

Thus all Type-I arrays are impossible.

## 3. Type II: e0 in the high A-quad xi

Here the occupancy-2 A-quad is {z,s_A,. , .}. Thus z's C-mate is s_L (it already met s_A in A), and the remaining C-triples consist of s_A plus a w and the other two w's. As above kappa cannot meet e0 in P1 and is not in (E), so kappa belongs to A0, giving (A). Let Be be e0's B-triple. xi already met e0 in its A-quad and r's met it in L_C, so Be's two nonempty rows are w's. Its pair differs from C's w-pair, hence E1 (only one w-pair) is impossible. Normalize to E3 with w's {04,14,23}.

Write U=04-23 and V=14-23. If Be=U, C uses V and its s_A-w triple uses w=04; if Be=V, C uses U and that triple uses w=14. B0 and the other nonzero B-triple split r1,r2 and the remaining {xi,w} between them.

**xi=13,kappa=24.**
- Be=U: s_A must be p_b (disjoint 04), s_L=O'. In (A) only m=1 works, so a=1. Remaining A-rows {O,04,14,23} have only pair partition O-14 | 04-23, repeating Be.
- Be=V: s_A disjoint 14 and s_L disjoint 24 allow only (s_A,s_L)=(2,O') (a=1), or (O',1) (a=2). In the first, (A) has m=1, leaving the same four-row set whose partition repeats C's U. In the second, m=O, leaving {2,04,14,23}; its two pair partitions P,Q (Section 2.2) repeat respectively Be's V and C's U.

**xi=24,kappa=13.**
- Be=U: s_A=p_b,s_L=O'; (A) needs m=2, forcing a=2. The remaining four-row set {O,04,14,23} repeats Be's U.
- Be=V: s_A disjoint 14 and s_L disjoint 13 force {s_A,s_L}={O',2}, a=1. If s_A=2,s_L=O', no m in (A) is compatible with O' and 13. If s_A=O',s_L=2, B0 must use r_i=1 (O meets O') and w0=24 (04 meets O'); the other B-triple is O-04, not T-disjoint.

Type II with e0 in A is impossible.

## 4. Type II: e0 in K_B

Now xi cannot meet e0 in P1 and is not in (E), so the same incidence count forces its B-triple to be B0:

    B0={s_A,xi,m_B}.                                            (B)

kappa already met e0 in K_B; r's met it in L_C, and s_L is in A0. Hence e0's A-triple Ae contains two w's. It differs from the C w-pair; E1 is impossible, and again normalize to E3 with U=04-23, V=14-23. If Ae=U then C uses V and s_A's C-mate is 04; if Ae=V then C uses U and s_A's C-mate is 14. A0 and the other nonzero A-triple Au split {kappa,r1,r2,remaining w} with A0 also containing s_L.

**xi=13,kappa=24.**
- Ae=U: s_A must be disjoint both 13 and 04, so s_A=2, a=1, s_L=O'. (B) allows m_B=O or 04. A0 is forced to {O',1,24}, Au=O-14. If m_B=O, the remaining B-rows {1,04,14,23} have only pair partition 1-04 | 14-23, blocked by C's V. If m_B=04, remaining B-rows {O,1,14,23} cannot use O-1 (met L_C) and their only remaining T-disjoint partition is O-14 | 1-23, blocked by Au.
- Ae=V: s_A disjoint 13,14 is 2 or O'. If s_A=2 (a=1), s_L=O'; A0={O',1,24}, Au=O-04, impossible. If s_A=O', (B) needs m_B=2 (a=2,b=1). Remaining B-rows {O,04,14,23} have only partition O-14 | 04-23, blocked by C's U; a=1 provides no m_B.

**xi=24,kappa=13.**
- Ae=U: s_A disjoint 24,04 must be 1 (a=2), s_L=O'. (B) forces m_B=O. Remaining B-rows {2,04,14,23} have partitions P and Q, blocked respectively by C's V and Ae's U.
- Ae=V: s_A disjoint 24,14 must be O', so s_L=p_b. (B) needs m_B=1 (a=1), leaving B-rows {O,04,14,23}, whose only pair partition O-14 | 04-23 is blocked by C's U; a=2 provides no m_B.

This excludes the final Type-II subcase. Every position type, orientation, private identity and e0 location was included, so **residual family 5 contains no array**.

## 5. Boundary
This is a whole-family exclusion, not a selected nonempty projection: all asserted partitions are necessary for every completion of the family, and the contradictions are within actual P1 blocks and already-forced P0 pair meetings. Empty placements not fixed above remain arbitrary; none is assumed feasible. No inference to b63 outside family 5. Together with the separately proved family-4 exclusion, G2-Q1-(a) is excluded as a candidate written result; families 1,2,3,6 of b63-reduction-v1.md remain open. Parent checking and both-family review remain required; no count or ledger change.
