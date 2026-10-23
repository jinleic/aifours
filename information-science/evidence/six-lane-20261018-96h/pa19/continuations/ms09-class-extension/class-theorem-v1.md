# PA19 ms09 skeleton-class theorem for the b65 mechanism: written proof v1

Written after host clock 2026-10-19T17:36:29-0700 by ContinuePA19d. Scope: scope-v1.md, SHA256 27b13a5c19b9bc7dc885d7fc52030796dcacc53bff8dcf707c1f1d232fa7b269. Status: CANDIDATE_WRITTEN_PROOF, independently unreviewed. Written only: no scientific computation, enumeration, script, assertion, solver, encoder, test, model CLI or Lean. Every step used from the earlier b65 candidate is re-derived below; that candidate is not a premise.

## 0. Setting, hypotheses and theorem

**Type data.** Let P={0,1,2,3,4}. A type list is a list of DISTINCT subsets of P, each of size at least 2, together with an integer e>=0, such that deg(c) (the number of listed types containing c) is at most 4 for every c, and

    (number of listed types) + sum_c (4-deg(c)) + e = 19.

Its rows are: one row for each listed type; 4-deg(c) distinct private rows of type {c} for each c; and e distinct empty rows (type empty). Write T(r) for the type of row r and t=|T(r)|.

**Arrays.** An array for the type data is a 19x8 array over six symbols on these rows in which any two distinct rows agree in at most one column; five columns, called P0 and indexed by P, have profile (4,3,3,3,3,3), and the size-4 symbol class of column c is exactly Q_c={r : c in T(r)}; the other three columns, called P1, have profile (4,4,3,3,3,2). Symbol classes are called blocks; eps(B) is the number of empty rows in a block B. This is exactly the ms09 skeleton semantics: each entry of skeletons-b-ms09.json supplies the listed types and e, and the pinned encoder lines 3-8 and 77-99 build these rows and quad memberships (see case-table-v1.md and the interface map for the bindings).

**Hypotheses H.**
- H1: e=7.
- H2: some listed type g has |g|=3, and its two-element complement P minus g is NOT a listed type.

**Theorem.** If the type data satisfy H1 and H2, no array exists.

The proof does not use any skeleton file, list, interval, solver, frontier status or prior acceptance. Sections 1-2 hold for the whole class; Section 2 proves that every hypothetical array forces the exact b65 type list, and Sections 3-4 exclude that list.

## 1. General facts for e=7

Fix an array for type data with e=7. Let E be its seven empty rows.

### 1.1 Exact pair cover
Counting agreeing pairs with multiplicity gives 5*(6+5*3)+3*(2*6+3*3+1)=5*21+3*22=171=C(19,2). Since no pair agrees twice, every pair of rows agrees EXACTLY once. Consequently: two rows whose types meet already agree in a common quad and agree nowhere else; two listed types share at most one index (otherwise their rows agree in two P0 columns); every block other than a P0 quad consists of pairwise T-disjoint rows; two blocks from different columns meet in at most one row.

### 1.2 Row patterns
For row r let n_i be the number of its P1 blocks of size i (i=2,3,4). Its P0 blocks give 3t+2(5-t)=10+t partners and its 18 partners are distinct, so n_2+n_3+n_4=3 and n_2+2n_3+3n_4=8-t, i.e. n_4-n_2=2-t. The nonnegative solutions (n_2,n_3,n_4) are: t=0: (0,1,2); t=1: (0,2,1),(1,0,2); t=2: (0,3,0),(1,1,1); t=3: (1,2,0),(2,0,1); t=4: (2,1,0); t=5: (3,0,0). In particular empty rows lie in two P1 quads of different columns, one P1 triple and no pair; every row with t>=4 lies in at least two P1 pairs; a private pair endpoint has pattern (1,0,2).

### 1.3 Occupancy categories
Counting the 21 pairs inside E in their unique agreeing block gives sum_B C(eps(B),2)=21. By 1.2 each P0 column has triple occupancies summing to 7, the six P1 quads sum to 14 and the nine P1 triples to 7; P0 quads and P1 pairs have occupancy 0. Moving a unit from x to y when x>=y+2 lowers the pair cost by x-y-1>0, so the minimum costs are 2 per P0 column (2,2,1,1,1), 10 for the quads (3,3,2,2,2,2) and 0 for the triples; the total excess is 21-20=1. Exactly one category holds, all non-exceptional parts being at their minimum lists:

| category | unique exceptional part | other parts |
|---|---|---|
| C3 | one P0 column (3,1,1,1,1) | other P0 (2,2,1,1,1); quads (3,3,2,2,2,2); P1 triples <=1 |
| C0 | one P0 column (2,2,2,1,0) | as C3 |
| Q4 | quads (4,2,2,2,2,2) | every P0 (2,2,1,1,1); P1 triples <=1 |
| Q1 | quads (3,3,3,2,2,1) | every P0 (2,2,1,1,1); P1 triples <=1 |
| T2 | one P1 triple has 2, others <=1 | every P0 (2,2,1,1,1); quads (3,3,2,2,2,2) |

Exhaustiveness: in a P0 column with occupancy counts m_j, cost 3 means m_2+3m_3=3 with sum j*m_j=7 and sum m_j=5, giving exactly the C3 and C0 lists, and cost 2 gives only the normal list. For quads write d_j=y_j-2; then sum d_j=2 and sum C(y_j,2)=9+(1/2)sum d_j^2, so cost 10 means two deviations +1 (normal list) and cost 11 means one deviation +2 (Q4) or four deviations of absolute value 1, necessarily three +1 and one -1 (Q1). Triple cost 0 means all occupancies <=1; cost 1 means exactly one 2 and no 3. No placement is assumed.

### 1.4 Incidence lemmas
For every nonempty row r, I(r):=sum over blocks B containing r of eps(B) equals 7, because r agrees once with each empty row. A triple containing a nonempty row has eps<=2 and a quad containing one has eps<=3.

(L1) Private rescue. A private pair endpoint (pattern (1,0,2)) lies in C0's unique occupancy-0 P0 triple or in Q1's unique occupancy-1 quad: otherwise its four P0 triples contribute at least 4 and its two quads at least 4, contradicting I=7. (C3's occupancy-3 triple is all-empty.) Each rescue block has exactly three nonempty rows, and no rescue block exists in C3, Q4 or T2.

(L2) A t=3 row with pattern (1,2,0) forces category T2 and lies in the occupancy-2 P1 triple: otherwise its two P0 triples give at most 4 and its two P1 triples at most 2, so I<=6.

(L3) A t=3 row with pattern (2,0,1) has both P0 triples of occupancy 2 and its quad of occupancy 3: these three blocks are its only empty contributions and their bounds 2,2,3 sum to 7.

## 2. Reduction of H1-H2 to the b65 normal form

Assume an array exists for type data satisfying H1 and H2. A permutation of P applied simultaneously to P0 column indices, listed types and private types preserves every defining condition, so assume g={0,1,2} and {3,4} is not listed.

**Step A (pairs of g).** A row T-disjoint from g has type inside {3,4}. A listed one would be {3,4}, excluded; so only privates of types {3},{4} qualify. If g had pattern (1,2,0), L2 gives T2, while its pair partner is a private endpoint, impossible in T2 by L1. Hence g has (2,0,1): two distinct private pair partners in two P1 columns. Both are private endpoints, so both lie in the unique rescue block (L1). Two privates of the same type {c} already agree in Q_c, so they cannot share that block: the partners are a row p_3 of type {3} and a row p_4 of type {4} (in particular deg(3),deg(4)<=3). Name the P1 columns A,B,C so that pair(A)={g,p_3}, pair(B)={g,p_4}, and g's quad H_C is in C. By L3 its P0 triples in columns 3 and 4 have occupancy 2, and H_C={g}+U_E with |U_E|=3.

**Step B (Q1 and L_C).** p_3 has quads in B and C, p_4 in A and C. Neither can enter the full quad H_C, so both lie in the other C-quad L_C. Categories C3,Q4,T2 provide no rescue. In C0 both would lie in the occupancy-0 P0 triple and agree twice with L_C. Hence the category is Q1; the rescue quad contains p_3 and p_4; their only common quad is L_C, so eps(L_C)=1.

**Step C (third row of L_C).** Its third nonempty row r_3 is T-disjoint from {3} and {4}, so T(r_3) is a nonempty subset of {0,1,2}. It is not g (in H_C) and not a listed type (a listed subset of {0,1,2} of size >=2 is g or meets g twice, contrary to 1.1). Thus r_3=p_k is a private row of type {k}, k in {0,1,2}. Write L_C={p_3,p_4,p_k,e_0}.

**Step D (occupancies).** In Q1 every P0 column is (2,2,1,1,1), so every P0 triple through a nonempty row has eps>=1, and every quad other than L_C has eps>=2. Let L_A be p_4's A-quad and L_B p_3's B-quad. Then 7=I(p_4)>=4+eps(L_A)+1 gives eps(L_A)=2 and all four P0 triples of p_4 have eps 1; likewise eps(L_B)=2 and all P0 triples of p_3 have eps 1. The remaining quads H_A,H_B have eps 3 (the list is (3,3,3,2,2,1)). Three empties lie outside the C-quads, so each C-triple has eps exactly 1.

**Step E (patterns of the other rows).**
- E1. If p_k were a pair endpoint, its pair would lie in A or B (its C-block is L_C), but those pairs are full. So p_k has (0,2,1) and its A- and B-blocks are triples.
- E2. Any other private q: if it were a pair endpoint, only the C-pair is free, so its quads are in A and B, while L1 requires the rescue quad L_C; impossible. So q has (0,2,1). Its quad is not in C (H_C and L_C are full). If it were H_A or H_B, then I(q)>=4+3+1=8 (its C-block is an eps-1 triple). Hence q lies in L_A or L_B; each has exactly one nonempty position besides p_4 or p_3.
- E3. A listed type h other than g with |h|>=4 needs two P1 pairs (1.2), but only the C-pair is free. If |h|=3, pattern (2,0,1) needs two pairs, and pattern (1,2,0) needs T2 by L2, while the category is Q1. So every listed type other than g has size 2.
- E4. The C-pair's endpoints are not g, p_3, p_4, p_k (their C-blocks are quads) nor other privates (E2). They are two listed 2-types with pattern (1,1,1), each having exactly one quad, which lies in A or B. Every other 2-type is a pair endpoint of no free pair, hence has (0,3,0) and no quad.

**Step F (the type list is forced).** Besides p_3 and p_4, the A/B quads have exactly four nonempty positions: one in each of H_A,H_B,L_A,L_B. Exactly the following nonempty rows occupy A/B quads: p_3, p_4, the two C-pair 2-types (one quad each, E4) and the m privates of E2 (one quad each, only L_A/L_B); g and p_k have C-quads and the (0,3,0) rows none. Hence 2+m=4, m=2, and there are exactly five private rows. So sum_c deg(c)=20-5=15. All listed types other than g have size 2 (E3), so 15=3+2(n-1) and there are n=7 listed types. Each of the six 2-types meets g in at most one index (1.1) and is not {3,4}; a 2-type disjoint from g would be {3,4}. So each is {k,w} with k in {0,1,2} and w in {3,4}; there are exactly six such sets. Therefore the listed types are exactly

    g={0,1,2}, a_k={k,3}, b_k={k,4} (k=0,1,2),

every index has degree 3, and there is exactly one private row p_c of each type {c}. This is precisely the b65 list. The quads are Q_k={g,a_k,b_k,p_k} (k=0,1,2), Q_3={a_0,a_1,a_2,p_3}, Q_4={b_0,b_1,b_2,p_4}.

Permuting {0,1,2} (simultaneously a_k,b_k,p_k) preserves this list and the normal form, so assume p_k=p_0. The two remaining privates are p_1,p_2; by E2 and the position count they occupy the free positions of L_A and L_B, one each. Name them so that

    L_A contains p_4,p_i; L_B contains p_3,p_j; {i,j}={1,2}.

Both choices of i remain in the proof. The two C-pair 2-types occupy the positions of H_A and H_B.

**Step G (incidence of p_i,p_j).** p_i has quad L_A (eps 2), its C-block is an eps-1 triple and its B-block a triple: 7=I(p_i)=2+1+eps(B-triple of p_i)+(four P0 terms, each >=1). So its B-triple has eps 0 and all its P0 triples eps 1. Likewise p_j's A-triple has eps 0 and all its P0 triples eps 1. Thus p_3,p_4,p_i,p_j lie only in occupancy-1 P0 triples outside their quads.

## 3. The forced graph of the seven actual empty rows

Each empty row is an edge between its two P1 quads (different columns); the graph is simple since two empties on the same two quads would agree twice; vertex degrees are quad occupancies. An edge determines only the column of its triple, not which triple; every particular-triple statement below is separately justified.

The three rows of U_E lie in H_C. Put V=E minus (U_E union {e_0}); each row of V has its quads in A and B and its triple in C. The other quad of e_0 is not L_A (it would meet p_4 twice) nor L_B (p_3); it is H_A or H_B. The automorphism

    P0 index 3<->4, a_k<->b_k, p_3<->p_4, P1 column A<->B (g,p_0,p_1,p_2 fixed)

preserves the b65 list and the normal form (it exchanges the roles of i and j, both of which are retained), so assume e_0 lies in H_A.

The A-quads hold 5 empties: the three of V and e_0, so exactly one u in U_E has its other quad in A, the other two in B. If u were in L_A, then H_A would contain e_0 and two rows of V, which pairwise agree in A. But g's two occupancy-2 P0 triples (columns 3 and 4) must split the four empty partners E minus U_E={e_0}+V into two pairs that do not already agree in P1, and every split of four elements into two pairs puts two members of a given three-element subset together. Hence u is in H_A. Name its third empty v in V and the other rows of V v',v''. The two other U_E rows lie in different B-quads (they share H_C) and so do v',v'' (they share L_A); since H_B has three empties it contains v and one of each pair; call them u',v'. The table is

| quad | empty rows |
|---|---|
| H_A | e_0,u,v |
| L_A | v',v'' |
| H_B | u',v,v' |
| L_B | u'',v'' |
| H_C | u,u',u'' |
| L_C | e_0 |

These seven labels are distinct rows. e_0,u have their triples in B; u',u'' in A; v,v',v'' in C. In Q1 no P1 triple holds two empties, so two empties agree in P1 iff they share a quad above. Let M be the graph of empty pairs NOT agreeing in P1; its edges are exactly

    e_0u', e_0u'', e_0v', e_0v'', uv', uv'', u'v'', u''v, u''v', vv''.

Each M-edge agrees in exactly one P0 occupancy-2 triple. g's two P0 triples contain exactly e_0,v,v',v'' and the only perfect matching of these in M is {e_0v',vv''}, so they are, in some order,

    {g,e_0,v'} and {g,v,v''}.                                   (G)

## 4. P0 bookkeeping and the contradiction

### 4.1 Occupancy-1 counts
Every P0 column has two occupancy-2 and three occupancy-1 triples. An empty w lies in exactly deg_M(w) occupancy-2 P0 triples (each realizes exactly one incident M-edge, and each incident M-edge is realized once) and in f(w)=5-deg_M(w) occupancy-1 triples:

| w | e_0 | u | u' | u'' | v | v' | v'' |
|---|---|---|---|---|---|---|---|
| deg_M | 4 | 2 | 2 | 3 | 2 | 3 | 4 |
| f | 1 | 3 | 3 | 2 | 3 | 2 | 1 |

For r in {p_3,p_4,p_i,p_j} (four occupancy-1 P0 triples each) let S(r) be its four P0 empty partners, one per triple. From the quad table and Step G:

    S(p_3)={u,u',v,v'}, S(p_4)={u,u',u'',v}, S(p_i)={e_0,u,u',u''}.     (S)

(For p_i: its C-triple holds one of v,v',v'' and it already met v',v'' in L_A, so that empty is v; its B-triple is empty-free.) Let c_j be the empty in p_j's C-triple; c_j is v or v' since p_j met v'' in L_B. Its A-triple is empty-free and L_B gives u'',v'', so S(p_j)=E minus {u'',v'',c_j}, which contains e_0.

### 4.2 The O-to-E bijection
Let T_3, T_4 be the four occupancy-1 P0 triples through p_3, respectively p_4; they are disjoint (p_3,p_4 agree in L_C). Let O be the other seven of the fifteen occupancy-1 P0 triples. Subtracting gives, for every w, f(w)-[w in S(p_3)]-[w in S(p_4)]=1 (values 1-0-0, 3-1-1, 3-1-1, 2-0-1, 3-1-1, 2-1-0, 1-0-0 in table order). So each O triple carries a different empty and every empty labels exactly one O triple.

### 4.3 Shared triples
p_3's T-disjoint nonempty rows are g,b_0,b_1,b_2,p_0,p_i,p_j,p_4. In P1 it already met g (A-pair), p_j (L_B), p_0,p_4 (L_C), so its four P0 triples contain b_0,b_1,b_2,p_i once each. In column 4 the b_k lie in Q_4, so

    tau_1={p_3,p_i,w_4}, w_4 in S(p_3) intersect S(p_i)={u,u'}.        (4)

Symmetrically p_4 meets a_0,a_1,a_2,p_j in its P0 triples and its column-3 triple is {p_4,p_j,w_3} with w_3 in S(p_4), so w_3 != e_0. p_i lies in exactly one T_3 triple (4) and no T_4 triple (it met p_4 in L_A); its other three P0 triples are in O. p_j lies in exactly one T_4 triple and no T_3 triple (it met p_3 in L_B). Both S(p_i) and S(p_j) contain e_0, and neither w_4 nor w_3 is e_0, so p_i and p_j both lie in the unique O triple carrying e_0, which is exactly {p_i,p_j,e_0}. Then p_i,p_j cannot also share a C-triple; p_i's C-triple holds v, so c_j=v', S(p_j)={e_0,u,u',v} and w_3 is in {u,u',v}. The other two O triples of p_i and of p_j are four distinct triples (p_i,p_j already agreed), so by the bijection

    ({u,u',u''} minus {w_4}) intersect ({u,u',v} minus {w_3}) = empty.

With bar(w_4) the other member of {u,u'}, the first set contains bar(w_4), forcing w_3=bar(w_4). Thus {w_3,w_4}={u,u'}; p_i's O empties are {e_0,u'',w_3} and p_j's are {e_0,v,w_4}.                                         (6)

### 4.4 Column 4 is impossible
Column 4 contains Q_4={b_0,b_1,b_2,p_4}. Its occupancy-1 triples include tau_1 (empty w_4). p_j's column-4 triple tau_2 has occupancy 1 and is in O (p_j met p_3 in L_B; p_4 is in Q_4). By (6) its empty is e_0, v or w_4. It is not e_0 (that O triple contains p_i, whose column-4 triple is tau_1) and not w_4 (already in column 4), so it is v. The third occupancy-1 triple tau_3 contains none of p_3,p_4,p_i,p_j, so it is an O triple different from those through p_i and p_j, which carry {e_0,u,u',u'',v}; hence its empty is v' or v''. By (G) g's column-4 triple is {g,e_0,v'} or {g,v,v''}; the latter repeats v in column 4, so it is {g,e_0,v'}, and tau_3 carries v''. Column 4 has now used w_4,v,v'',e_0,v', so its other occupancy-2 triple contains the two remaining rows {u,u',u''} minus {w_4}. Both lie in H_C and would agree twice. Contradiction; the theorem is proved.

## 5. Consequences and boundary

Section 2 proves more than needed: for type data with e=7 and a 3-type g whose complement is unlisted, either an immediate contradiction occurs (missing p_3 or p_4, a second 3-type, a type of size >=4, or a wrong number of privates) or the list is exactly b65's, which Sections 3-4 exclude. Among the 59 v10-undecided ms09 cases only b65 satisfies H (case-table-v1.md); b59, outside that list and already parent-closed, also satisfies H (with g={0,1,2}; it is excluded at E3 by its second 3-type {0,3,4}), giving independent corroboration only. The theorem therefore yields no new frontier closure beyond the pending b65 candidate. Normalizations used: P0 index permutations (any), P1 column naming, the permutation of {0,1,2} placing p_k=p_0, and the 3<->4/A<->B automorphism. Both i=1 and i=2 are retained. Candidate only: independent parent checking and both-family hostile review are required; no ledger change; PA(19,8,6) remains UNDECIDED; no Lean, solver, novelty or priority claim.
