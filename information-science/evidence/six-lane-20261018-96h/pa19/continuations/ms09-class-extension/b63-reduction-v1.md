# PA19 ms09 b63: written reduction v1 (NOT an exclusion; exact surviving obligation)

Written after host clock 2026-10-19T18:03:00-0700 by ContinuePA19d under scope-v1.md (SHA256 27b13a5c19b9bc7dc885d7fc52030796dcacc53bff8dcf707c1f1d232fa7b269), whose frozen rule selected b63. Status: CANDIDATE PARTIAL REDUCTION, unreviewed. **b63 is NOT excluded by this document.** Written only; no computation, enumeration, script, assertion, solver or model CLI. General facts are Section 1 (1.1-1.4, lemmas L1-L3) of class-theorem-v1.md in the same packet, proved there for every type list with e=7.

## 0. The case
S bytes [4256,4338), entry SHA256 6b03eb8ad5a5d05c6486cd04656e444f051a2a6677a136759c9cbf2e22149a6a:
{"types": [[0, 1, 2], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "empty": 7}
Degrees (2,3,3,3,4), so the rows are g={0,1,2}, 04, 13, 14, 23, 24, z=34, private rows p0,p0' (two distinct rows of type {0}), p1, p2, p3 (no p4), and seven empty rows E. Quads: Q0={g,04,p0,p0'}, Q1={g,13,14,p1}, Q2={g,23,24,p2}, Q3={13,23,z,p3}, Q4={04,14,24,z}. Symmetries used: 1<->2 (13<->23, 14<->24, p1<->p2), p0<->p0', P1 column names, empty-row names.

## 1. Proven reductions

**B1 (g is isolated in P0 columns 3 and 4).** The nonempty rows T-disjoint from g are exactly z and p3. If g has pattern (1,2,0), L2 forces T2 with equality, so both its P0 triples have occupancy 2; if (2,0,1), L3 gives the same. An occupancy-2 triple has one nonempty row, so g's P0 column-3 and column-4 triples are {g,e,e'} with two empty rows each.

**B2 (exhaustive split).**
- G1: g has (1,2,0). Category T2 (L2); by L1 no private is a pair endpoint, so g's pair partner is z (pair in column A). Equality in L2 puts g in the occupancy-2 P1 triple tau={g,eps1,eps2} (column B, by naming) and makes g's other P1 triple have occupancy 1; its nonempty partner is T-disjoint from g and not z, hence it is tau'={g,p3,eps3} (column C).
- G2: g has (2,0,1). Its two distinct pair partners are z and p3: pair(A)={g,p3}, pair(B)={g,z}; g's quad H_C={g}+U with |U|=3 (L3). p3 is a private endpoint, so the category is C0 or Q1 (L1).

**B3 (G1).** All three pairs have nonprivate endpoints. The 2-types other than z that are mutually T-disjoint form the path 24-13-04-23-14, so the B- and C-pairs are a two-edge matching of that path: {13-24,14-23} (04 unpaired), {13-24,04-23} (14 unpaired) or {04-13,14-23} (24 unpaired); the last two are exchanged by 1<->2. Every private has pattern (0,2,1). For p3, I(p3)=7 with tau' contributing 1, four P0 triples at least 4 and its quad at least 2 forces: quad occupancy 2, its other P1 triple occupancy 0, and all its P0 triples occupancy 1.

**B4 (G2 common facts).** p3 has pattern (1,0,2), quads in B and C; its C-quad is not H_C (full), call it L_C, and call its B-quad L_B. z has (1,1,1): its C-block is not H_C (full), not L_C (p3 and z share Q3), so it is a C-triple, and z's quad K_z is in A.

**B5 (G2-C0).** The rescue block is the occupancy-0 triple R* of the exceptional column c*, and contains p3, so c* is not 3. I(p3)=7 with three P0 triples of occupancy at least 1 and two quads of occupancy at least 2 forces eps(L_B)=eps(L_C)=2 and occupancy 1 in p3's other three P0 triples. R* is p3 plus two T-disjoint rows outside Q_{c*} and T-disjoint from p3:
- c*=0: {p3,14,p2}, {p3,24,p1}, {p3,p1,p2};
- c*=1: {p3,04,p2}, {p3,24,p0}, {p3,24,p0'}, {p3,p0,p2}, {p3,p0',p2};
- c*=2: the 1<->2 images of the c*=1 list;
- c*=4: {p3,a,b} with {a,b} one of p0p1, p0p2, p0'p1, p0'p2, p1p2 (g's column-4 triple has occupancy 2).

**B6 (G2-Q1 split).** p3 lies in the occupancy-1 quad and I(p3)=7 forces {eps(L_B),eps(L_C)}={1,2} and occupancy 1 in all p3's P0 triples. Write (a) eps(L_C)=1, eps(L_B)=2 and (b) eps(L_B)=1, eps(L_C)=2.

**B7 (G2-Q1-(a)).** Every C-triple has occupancy 1 (four empties lie in C-quads). A private C-pair endpoint would need the rescue quad L_C while its quads are in A,B, so the C-pair is two T-disjoint 2-types x,y with pattern (1,1,1) and quads in A or B. L_C={p3,r1,r2,e0}: a row with a C-quad other than g,p3 cannot be a 2-type (its pair would be in A or B, both full) nor a private endpoint (same reason), so r1,r2 are privates of different types with pattern (0,2,1). The other two privates s1,s2 have (0,2,1), quads in A or B, and I(s)=7 with an occupancy-1 C-triple and four P0 triples forces quad occupancy 2, occupancy 0 in their non-C triple and occupancy 1 in all their P0 triples. The remaining quads K_B (in B), K_z and K'_A (in A) have occupancies {3,3,2}.

**B8 (spread lemma).** The three empties of U already agree in H_C, so their other quads (one each, in A or B) are pairwise different; hence at most two have A-quads and at most two B-quads. The same holds for any three empties sharing one block.

**B9 (G2-Q1-(a), K_B occupancy 2: normal form).** Then K_z and K'_A have occupancy 3, contain z and one C-pair row x alone, and the B-quads hold p3's partner and s1,s2,y. The A-quads hold V (the three empties with quads in A and B) plus e0's other quad (if in A) plus U's A-quads; by B8 exactly two U rows have A-quads, so e0's other quad is in A (the alternative e0 in K_B is impossible) and f(e0)=1, where f(w)=eps(Q_w)+eps(Q'_w)-3 counts the occupancy-1 P0 triples through w (as in class-theorem-v1.md 4.1, since no P1 triple holds two empties in Q1). Neither s meets e0 in P1, so both meet it in the unique occupancy-1 P0 triple through e0: {s1,s2,e0} is a P0 triple. Hence s1,s2 are T-disjoint and lie in different B-quads; y is in K_B. z and x have all P0 triples of occupancy 1 (their quads have occupancy 3 and their other P1 triple occupancy 1), so each must meet e0 in P1: e0 is in K_z and x's B-triple contains e0. With B8 the empty-row table is forced up to naming: K_z={z,e0,u1,va}, K'_A={x,u2,vb,vc}, B-quads {va,vb} and {vc,u3} (one of them is L_B), and g's P0 triples are {g,e0,vb} and {g,va,vc}. If L_B holds va,vb, counting the two occupancy-1 P0 triples through u3 forces the P0 triples {p3,x,u3} and {s_L,z,u3} (s_L the private in L_B), so x is one of 04,14,24.

## 2. Exact surviving obligation for b63
A complete exclusion must still refute every array in each of the following exhaustive residual branches (the reductions above hold in each):
1. G1 with B/C pairs {13-24,14-23}; 2. G1 with {13-24,04-23} (its 1<->2 image {04-13,14-23} is equivalent).
3. G2-C0, for every c* and R* listed in B5.
4. G2-Q1-(a) with occupancy-2 K_B, in the B9 normal form with L_B={p3,s_L,va,vb} or L_B={p3,s_L,vc,u3}, for every admissible identity of x,y (C-pair), r1,r2 and s_L,s_K.
5. G2-Q1-(a) with occupancy-3 K_B: e0's other quad in A with one U row in A, or e0 in K_B with two U rows in A.
6. G2-Q1-(b) (eps(L_B)=1, eps(L_C)=2).
No branch above is claimed infeasible; no branch is claimed to extend to an array. This document closes no case and changes no count.
