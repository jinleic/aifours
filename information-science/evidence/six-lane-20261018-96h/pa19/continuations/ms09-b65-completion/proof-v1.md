# PA19 ms09 b65: full joint completion exclusion, written proof v1

Written after host clock 2026-10-19T17:00:50-0700 by ContinuePA19d. Scope: scope-v1.md, SHA256 edda4fc49fe722ae1e26cb36f095ac00d6d3f1b9ad996f2c30d920a577db77f5. Status: CANDIDATE_WRITTEN_PROOF, independently unreviewed. No scientific computation, enumeration, solver, encoder, test, model CLI, or Lean execution. Only input reads and metadata/hashes were used. All statements needed below are proved here; the earlier e7 candidate dossier and its reviews are not premises.

## Theorem and fixed case

There is no 19-by-8 array over six symbols with all the following properties:

1. Any two distinct rows agree in at most one column.
2. Five columns, called P0 and indexed 0,1,2,3,4, have profile (4,3,3,3,3,3). Their size-4 classes are Q_c = {r : c belongs to T(r)}.
3. The other three columns, called P1, each have profile (4,4,3,3,3,2).
4. The distinct rows and their T-sets are:
   - g: {0,1,2};
   - a_k: {k,3} and b_k: {k,4}, for k=0,1,2;
   - p_c: {c}, for c=0,1,2,3,4;
   - seven distinct rows with T empty, forming E.

Thus the theorem excludes the whole fixed-skeleton b65 class, not a first-P1 projection or a selected list of placements. It asserts no global nonexistence for PA(19,8,6).

This is the exact class specified by the zero-based b_index 65 entry of skeletons-b-ms09.json (whole-file SHA256 7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0): zero-based half-open bytes [4421,4503), entry SHA256 010b2b819f60b937e449a6af5ab88b711709fcae840ff226bb14af0895b28818,

    {"types": [[0, 1, 2], [0, 3], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4]], "empty": 7}

All listed-type degrees are 3, so the membership rule supplies exactly one private p_c per P0 column. The fixed quads are

    Q_k = {g,a_k,b_k,p_k} (k=0,1,2),
    Q_3 = {a_0,a_1,a_2,p_3},
    Q_4 = {b_0,b_1,b_2,p_4}.

Case identity is b_index plus this exact skeleton content and whole-file SHA, not the historical s-tag. The binding/interface map supplies the source excerpts; no claim about an encoder execution or completeness of a skeleton list is needed for the theorem.

Assume an array satisfying 1-4 exists. In a column, its six symbol classes are called blocks. For any block B let eps(B)=|B intersect E|. All rows named below are actual distinct rows, not anonymous occurrence slots.

## 1. Elementary identities and the one-unit excess

### 1.1 Every row pair agrees exactly once

The number of agreeing pairs, counted with multiplicity over all columns, is

    5*(C(4,2)+5*C(3,2)) + 3*(2*C(4,2)+3*C(3,2)+C(2,2))
      = 5*21 + 3*22 = 171 = C(19,2).

Assumption 1 therefore makes every pair agree exactly once. In particular, two rows whose T-sets intersect have already agreed in a P0 quad and cannot agree in any other block. Every block other than a P0 quad contains pairwise T-disjoint rows. Two blocks from different columns intersect in at most one row.

### 1.2 Row patterns

For a row r let t=|T(r)|, and let n_i count its P1 blocks of size i, i=2,3,4. Its P0 blocks account for 3t+2(5-t)=10+t partners. Its eighteen partners are all different by 1.1, so

    n_2+n_3+n_4=3,
    n_2+2*n_3+3*n_4=8-t,
    n_4-n_2=2-t.

The nonnegative solutions, in order (n_2,n_3,n_4), are

| t | possible patterns |
|---|---|
| 0 | (0,1,2) |
| 1 | (0,2,1) or (1,0,2) |
| 2 | (0,3,0) or (1,1,1) |
| 3 | (1,2,0) or (2,0,1) |

An empty row lies in five P0 triples, two P1 quads in different columns, one P1 triple and no pair. Each P1 pair consequently has two nonempty, T-disjoint endpoints. There are exactly three such pair blocks.

### 1.3 Exhaustive occupancy categories

Counting the 21 pairs within E in their unique agreeing block gives

    sum_B C(eps(B),2) = 21.

Each P0 column's five triples have total empty occupancy 7. The six P1 quads have total occupancy 14, and the nine P1 triples have total occupancy 7, by 1.2. P0 quads and P1 pairs have occupancy zero.

For nonnegative integers of fixed sum, moving a unit from x to y when x>=y+2 decreases the sum of binomial pair costs by x-y-1>0. Thus the minimum costs are 2 for each P0 column (occupancies 2,2,1,1,1), 10 for the six P1 quads (3,3,2,2,2,2), and 0 for the nine P1 triples. Their nonnegative integral excesses have total

    21 - (5*2+10+0) = 1.

Exactly one of the following categories occurs; all nonexceptional parts have their minimum-cost occupancies:

| category | unique exceptional occupancy part | other parts |
|---|---|---|
| C3 | one P0 column has (3,1,1,1,1) | other P0 columns (2,2,1,1,1); quads (3,3,2,2,2,2); P1 triples <=1 |
| C0 | one P0 column has (2,2,2,1,0) | same other parts as C3 |
| Q4 | P1 quads have (4,2,2,2,2,2) | every P0 column (2,2,1,1,1); P1 triples <=1 |
| Q1 | P1 quads have (3,3,3,2,2,1) | every P0 column (2,2,1,1,1); P1 triples <=1 |
| T2 | one P1 triple has occupancy 2, all others <=1 | every P0 column (2,2,1,1,1); quads (3,3,2,2,2,2) |

Here is explicit numerical exhaustiveness. For a P0 column with cost 3, let m_j count the occupancies j. Then m_2+3*m_3=3, sum j*m_j=7 and sum m_j=5 give precisely the two exceptional lists C3,C0; cost 2 gives only the normal list. For quad occupancies y_j, set d_j=y_j-2, so sum d_j=2 and

    sum_j C(y_j,2) = 9 + (1/2)*sum_j d_j^2.

Cost 10 requires exactly two deviations +1, yielding the normal list. Cost 11 requires either one deviation +2 or four deviations of absolute value 1. In the latter case sum d_j=2 forces three +1 and one -1, giving Q1; the former gives Q4. The remaining deviations are zero. Triple cost 0 means all occupancies <=1; cost 1 means exactly one occupancy 2 and none 3. This proves the table, without any placement or realization assumption.

### 1.4 Per-row empty incidence; private endpoint rescue

For any nonempty r,

    I(r) := sum_{B containing r} eps(B) = 7,

because r agrees once with each of the seven empty rows. A triple containing a nonempty row has occupancy at most 2; a quad containing one has occupancy at most 3.

A private pair endpoint has pattern (1,0,2). Unless it is in C0's unique occupancy-0 P0 triple or Q1's unique occupancy-1 P1 quad, its four P0 triples contribute at least 4 and its two P1 quads contribute at least 4, contradicting I=7. These are the only possible rescue blocks. This statement includes C3: its exceptional occupancy-3 triple is all-empty and cannot contain a private row.

## 2. Forced b65 normal form

### 2.1 The pairs containing g

The only nonempty rows T-disjoint from g are p_3,p_4. If g has pattern (1,2,0), its two P0 triples contribute at most 4 to I(g), and its two P1 triples contribute at most 2 unless the category is T2. Thus T2 is required. But g's pair partner is private, and T2 provides no private-endpoint rescue by 1.4. This is impossible.

Consequently g has pattern (2,0,1). Its two pair partners must be distinct, so they are p_3,p_4. Name the equal-profile P1 columns A,B,C so that

    pair(A)={g,p_3}, pair(B)={g,p_4},

and g's quad is H_C. The only empty contributions to I(g) come from its P0-column-3 and P0-column-4 triples and H_C. Their upper bounds are 2,2,3, so all are attained. Thus H_C={g}+U_E with |U_E|=3, and each of those two P0 triples contains g and two empties.

### 2.2 Q1 and the distinguished low quads

Rows p_3,p_4 both have pattern (1,0,2): p_3 is in quads in B,C, and p_4 in quads in A,C. Neither can enter H_C, which already consists of g and three empties, so they share the other C-quad, L_C.

Categories C3,Q4,T2 have no private rescue and are impossible. In C0 both p_3 and p_4 would have to be in the unique occupancy-0 P0 triple. They would then agree both in that triple and in L_C, impossible by 1.1. Hence the category is Q1, and both private endpoints must lie in its sole occupancy-1 quad. Since they already share L_C, that quad is L_C.

Write L_A for the A-quad containing p_4, and L_B for the B-quad containing p_3. The equality I(p_3)=7 has contributions from four P0 triples of occupancy at least 1, L_C of occupancy 1, and L_B of occupancy at least 2. Hence every one of p_3's P0 triples has occupancy 1 and eps(L_B)=2. Similarly every P0 triple through p_4 has occupancy 1 and eps(L_A)=2.

The third nonempty row in L_C is T-disjoint from {3} and {4}. Among our listed rows it must therefore be one of p_0,p_1,p_2; g is in H_C and all a_k,b_k contain 3 or 4. Permuting indices 0,1,2 together with a_k,b_k,p_k is an automorphism of the exact skeleton and profiles. Use this explicit symmetry to name that row p_0. Thus

    L_C={p_0,p_3,p_4,e_0}, eps(L_C)=1.

The remaining A- and B-quads, H_A,H_B, each have occupancy 3, since the full quad list is (3,3,3,2,2,1). All P0 columns now have occupancies (2,2,1,1,1). Every C-triple has exactly one empty row: there are three empties outside H_C and L_C, and three C-triples with occupancy at most 1.

### 2.3 The low A/B rows and their incidence equalities

Rows p_1,p_2 cannot be in a P1 pair. Only C's pair remains available, and a private endpoint there would need Q1's rescue quad in C, although its two quads would have to be in A and B. Thus each has pattern (0,2,1). Its quad is in A or B, since both C-quads' nonempty positions are already full. It cannot be H_A or H_B: the high quad would contribute 3, its C-triple 1 and its four P0 triples at least 4, giving I>=8. Each must occupy the sole extra nonempty position in L_A or L_B. Name their indices i,j so that {i,j}={1,2} and

    L_A contains p_4,p_i; L_B contains p_3,p_j.

No choice between i=1 and i=2 is made or discarded.

For p_i, the contributions from L_A, its C-triple, its B-triple and four P0 triples give

    7 = 2 + 1 + eps(B-triple through p_i) + sum(P0 contributions),

where the last sum is at least 4. Therefore its B-triple has occupancy 0 and all four P0 triples have occupancy 1. Similarly p_j's A-triple has occupancy 0 and all four of its P0 triples have occupancy 1. We have proved that all four private rows p_3,p_4,p_i,p_j lie only in occupancy-1 P0 triples outside their fixed quads.

## 3. The forced graph on the seven actual empty rows

Every empty row is an edge between its two P1 quads, which lie in different columns. The edge graph is simple: two empty rows on the same two quads would agree twice. Its six vertex degrees are the six quad occupancies. The edge determines only the missing P1 column, not which particular triple contains the empty row. All particular-triple uses below are explicitly justified by occupancy and uniqueness.

The three rows of U_E are in H_C. Put V=E minus (U_E union {e_0}), so |V|=3. Each row of V has its two quads in A,B and its triple in C.

The other quad of e_0 cannot be L_A or L_B, since e_0 would then agree with p_4 or p_3 twice, respectively. It is H_A or H_B. The exact skeleton automorphism

    P0 index 3<->4; a_k<->b_k; p_3<->p_4;
    P1 column A<->B; g,p_0,p_1,p_2 fixed

preserves the already normalized pairs and L_C. Therefore we may assume e_0 lies in H_A. (The previous permutation of indices 0,1,2 leaves this symmetry available.)

The A-quads contain five empties, three from V and e_0, so exactly one member u of U_E has its other quad in A; the other two have their other quads in B. If u were in L_A, H_A would contain e_0 and two rows of V. Those three already agree pairwise in A. But g's two P0 triples must partition the four rows E minus U_E={e_0}+V into two pairs, neither of which may already agree in P1. Any partition into two pairs of a four-element set puts two of a specified three-element subset together, impossible. Hence u is in H_A.

Name its third empty row v, and name the other two V rows v',v''. Then the A-quad empty sets are

    H_A: {e_0,u,v}, L_A: {v',v''}.

The other H_C empties must be in different B-quads because they already share H_C. Likewise v',v'' must be in different B-quads because they already share L_A. Since H_B has three empties, it contains v and one row of each of those two pairs. Name them u',v', respectively; the low B-quad contains u'',v''. The complete table is

| quad | actual empty rows |
|---|---|
| H_A | e_0,u,v |
| L_A | v',v'' |
| H_B | u',v,v' |
| L_B | u'',v'' |
| H_C | u,u',u'' |
| L_C | e_0 |

These seven labels denote distinct rows. The rows e_0,u have their triple in B; u',u'' have it in A; v,v',v'' have it in C. In Q1 no P1 triple has two empties. Thus two empty rows agree in P1 if and only if they share one of the quads in this table.

Let M be the graph on E whose edges are pairs not agreeing in P1. Its edges, written with juxtaposition for an unordered pair, are exactly

    e_0u', e_0u'', e_0v', e_0v'',
    uv', uv'', u'v'', u''v, u''v', vv''.

They must each agree in exactly one P0 triple. In particular g's two P0 triples contain precisely the four empty partners e_0,v,v',v''. The only perfect matching of those four using M-edges is {e_0v',vv''}. Hence its P0-column-3 and P0-column-4 triples are, in some order,

    {g,e_0,v'} and {g,v,v''}.                         (G)

## 4. Global P0 bookkeeping closes the joint completion

### 4.1 The occupancy-1 triple counts

Every P0 column has two occupancy-2 triples and three occupancy-1 triples. An empty row w lies in five P0 triples. Every occupancy-2 occurrence pairs w with one other empty row, accounting for exactly one incident M-edge. Distinct such occurrences cannot repeat a partner, and every incident M-edge must be accounted for. Therefore w occurs in exactly deg_M(w) occupancy-2 triples and in

    f(w)=5-deg_M(w)

occupancy-1 triples. The edge list above gives

| w | e_0 | u | u' | u'' | v | v' | v'' |
|---|---|---|---|---|---|---|---|
| deg_M(w) | 4 | 2 | 2 | 3 | 2 | 3 | 4 |
| f(w) | 1 | 3 | 3 | 2 | 3 | 2 | 1 |

Let S(r) be the set of empty partners met by r in P0 triples, for r in {p_3,p_4,p_i,p_j}. Each of these rows has four occupancy-1 P0 triples, so its four distinct P0 empty partners occur once each. Its other empty partners are determined by the P1 quad table and 2.3:

    S(p_3)={u,u',v,v'},
    S(p_4)={u,u',u'',v},
    S(p_i)={e_0,u,u',u''}.                            (S)

For the last equality, p_i's C-triple must contain v: it has one of v,v',v'', but p_i already agrees with v',v'' in L_A. Its B-triple has no empty row.

Let c_j be the empty row of p_j's C-triple. Since p_j already agrees with v'' in L_B, c_j belongs to {v,v'}. Its A-triple has no empty row, and its L_B empty partners are u'',v''. Thus

    S(p_j)=E minus {u'',v'',c_j}.                    (J)

In particular S(p_j) always contains e_0.

### 4.2 Exactly one remaining triple per empty row

Let T_3 be the four occupancy-1 P0 triples through p_3 and T_4 the four through p_4. These are disjoint families of blocks, since p_3 and p_4 already agree in L_C. Among the fifteen occupancy-1 P0 triples, let O be the other seven, containing neither p_3 nor p_4.

The T_3 triples carry the empties S(p_3) once each; the T_4 triples carry S(p_4) once each. Subtracting their indicators from f(w), using (S), gives

    f(w) - 1_{w in S(p_3)} - 1_{w in S(p_4)} = 1

for EVERY w in E (respectively 1-0-0, 3-1-1, 3-1-1, 2-0-1, 3-1-1, 2-1-0, 1-0-0 in the table order). Consequently each of the seven O triples carries a different empty row, and every empty row labels exactly one O triple. This is a bijection between O and the seven actual rows of E.

### 4.3 The exceptional shared triples and the e_0 constraint

The nonempty rows T-disjoint from p_3 are g,b_0,b_1,b_2,p_0,p_i,p_j,p_4. Of these, its P1 agreements already account for g in A's pair, p_j in L_B, and p_0,p_4 in L_C. Its four occupancy-1 P0 triples therefore have exactly b_0,b_1,b_2,p_i as their other nonempty rows, once each. In column 4 none of b_0,b_1,b_2 can accompany p_3, because they belong to Q_4. Hence the column-4 triple through p_3 is

    tau_1={p_3,p_i,w_4}, w_4 in S(p_3) intersect S(p_i)={u,u'}.       (4)

Likewise p_4's four other nonempty P0 partners are a_0,a_1,a_2,p_j; in column 3 it must accompany p_j. Call that triple {p_4,p_j,w_3}. Its empty w_3 is in S(p_4), in particular w_3 is not e_0.

Row p_i is in exactly one T_3 triple, namely (4), and no T_4 triple, since it already agrees with p_4 in L_A. Its other three P0 triples are in O. Row p_j is in exactly one T_4 triple, namely the column-3 triple just described, and no T_3 triple, since it already agrees with p_3 in L_B; its other three P0 triples are in O.

Both S(p_i) and S(p_j) contain e_0, and neither w_4 nor w_3 is e_0. Thus both p_i and p_j belong to the unique O triple carrying e_0. That triple is exactly {p_i,p_j,e_0}, since it has occupancy 1. They agree in this P0 triple, so they cannot agree in C. As p_i's C-triple contains v, c_j cannot be v (there is only one C-triple containing that actual empty row). Hence

    c_j=v', S(p_j)={e_0,u,u',v},
    w_3 in {u,u',v}.                                (5)

The other two O triples through p_i and the other two O triples through p_j are all different, because the pair p_i,p_j has already agreed in their e_0 triple. Their empty-row sets must therefore be disjoint by the O-to-E bijection:

    ({u,u',u''} minus {w_4})
      intersect ({u,u',v} minus {w_3}) = empty.

Let bar(w_4) be the other member of {u,u'}. The first set contains bar(w_4); the second would also contain it unless w_3=bar(w_4). Thus

    {w_3,w_4}={u,u'},
    O-empty rows through p_i: {e_0,u'',w_3},
    O-empty rows through p_j: {e_0,v,w_4}.            (6)

This deduction did not select i versus j, a C-pair orbit, an all-triple projection, or a particular P1 triple for an empty edge.

### 4.4 Column 4 is impossible

Column 4 contains Q_4={b_0,b_1,b_2,p_4}. Its three occupancy-1 triples include tau_1 from (4), carrying w_4. Row p_j belongs to a different occupancy-1 triple tau_2. This triple is in O: p_j already agrees with p_3 in L_B, and p_4 belongs to Q_4. By (6), tau_2's empty row is one of e_0,v,w_4.

It is not e_0: the unique O triple carrying e_0 contains p_i and p_j, but p_i is already in tau_1 in this column. It is not w_4, already used in tau_1. Therefore tau_2 carries v.

Call the third occupancy-1 triple tau_3. It contains none of p_3,p_4,p_i,p_j (their column-4 blocks were already identified), so it is an O triple different from all the O triples through p_i and p_j. By (6) their combined empty set is {e_0,u,u',u'',v}. The O-to-E bijection forces tau_3's empty to be v' or v''.

By (G), g's column-4 occupancy-2 triple is either {g,e_0,v'} or {g,v,v''}. The latter is impossible because v already lies in tau_2 in column 4. Thus g's triple is {g,e_0,v'}. Tau_3 cannot also use v', so it carries v''.

The empty rows now used in column 4 are w_4,v,v'' in its three occupancy-1 triples and e_0,v' in g's occupancy-2 triple. Its other occupancy-2 triple must contain the two remaining empty rows,

    {u,u',u''} minus {w_4}.

These two distinct rows both lie in H_C. They already agree in P1 column C, and would agree again in this P0-column-4 triple. This contradicts assumption 1.

The assumed full array therefore does not exist, proving the theorem.

## 5. Scope and verification boundary

The contradiction covers every assignment of the P1 nonempty rows, all seven actual empty rows, and all five P0 triple partitions in the exact b65 class. It does not infer a full-array result from a nonempty projection. The only normalizations were equal-profile P1 column naming, the explicit S3 action on indices 0,1,2 naming L_C's private row p_0, and the explicit simultaneous 3<->4/A<->B automorphism. Both i=1,j=2 and i=2,j=1 remain in the proof. Arbitrary empty-row labels were chosen only to name positions that were proved forced.

No AT2 theorem, Petersen-graph result, C-pair orbit enumeration, earlier displayed P0 obstruction, solver receipt, placement-list completeness, or accepted structural Theorem A/B is used. They are unnecessary for this exclusion. All e7-type facts actually used are re-proved in Sections 1-3.

Candidate consequence only, pending independent parent checking and both-family hostile review: b65 can be closed as a whole fixed-skeleton mathematical case. No ledger is changed by this worker. Parent frontier v10 (SHA256 29c7cbe8e22cdad3bb1d196f9df12d9336652cb4942dc9538ac6d22225ebd90a) is the pre-result snapshot with ms06=70, ms09=59, total=129; any new count decision belongs to the parent. All historical UNKNOWNs, native HOLDs, STOP markers and runtime gates remain. PA(19,8,6) remains UNDECIDED; no Lean, solver-checked, novelty or priority claim is made.
