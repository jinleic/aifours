# Four-common-overgroup attack: exact residual and finite permutation image v1

Observed before creation: `2026-10-23T14:25:50-0700` (`/bin/date`). **CANDIDATE written reduction, not Sun8 or a realizable counterexample.** This is a consequential continuation of the prime-seven obstruction, not a replay of seven-coset marker enumeration. No scientific execution occurred.

## 1. Scope and added imports

P7 is the exact residual from `reduction-and-generation-v1.md`: eight pairwise disjoint LEFT cosets with indices n_i=7r_i, with pairwise-coprime positive r_i, in an arbitrary group. R8 proves, relative to the explicitly trusted internal Sun7 statement, that any Sun8 counterexample is P7. Its G5 theorem already rules out an index-seven overgroup containing five subgroup vertices.

Here assume an index-seven W contains four U_i. This is a ROUTE SUBCASE, not an added hypothesis on the full target. We derive its exact remaining necessary geometry and a finite quotient bound.

In addition to the earlier elementary and Zhu Sun3/4 interfaces, this manuscript imports:

1. **S5:** the literal all-group Sun(5) statement of `institute/runs/six-lane-2026-10-18-96h/review/sun56-S56W-parent-verdict-v1.md`, lines5–10, read with its parent errata1/2. The C5W gate is explicitly discharged there. Only that index-gcd theorem statement is used, on five disjoint fibre cosets inside W. This remains an internal written import, not formal/priority acceptance.
2. **MS45:** Margolis–Schnabel, *The Herzog–Schönheim conjecture for small groups and harmonic subgroups*, Proposition4.5, <https://arxiv.org/pdf/1803.03569>: if q_1,...,q_4 are pairwise coprime and q_1 is odd, then (2q_1,4q_2,4q_3,4q_4) is not G-harmonic for any group. The primary statement and local proof were read. This is a declared classical theorem interface.
3. **MSB:** the same primary source, TheoremB: every G-harmonic tuple of length at most4 is Z-harmonic. Only that bounded length is imported. The recent Menon counterexample beyond length4 is not contradicted or ignored. We do NOT import a general G-to-Z transfer.
4. Elementary finite permutation actions, Cauchy's theorem, and Lagrange's theorem; the new quotient-coset projection bridge is proved in `structural-addendum-v1.md`, LemmaQ, and recalled below.

All unrestricted/cofactor/valuation cases of P7 remain in force. No bounded group order is assumed before it is proved in the final residual branch.

## 2. Four baselines, three holes, and t≤4

Let U_1,...,U_4≤W. Their four cosets occupy different left W-cosets by coprimality of the indices r_1,...,r_4 inside W. Call those cells baselines; the other three W-cosets are holes. The other four vertices are outliers (t=1 remains allowed).

For each vertex let t_i=[U_i:U_i∩W] and λ_i=[W:U_i∩W]=r_i t_i. Its coset meets exactly t_i distinct W-cosets, and translated fibre pieces have index λ_i. Baselines have t=1. An outlier can meet at most ω(t_i) baseline cells because sharing the cell of baseline b requires gcd(r_b,t_i)>1; different baseline cofactors are coprime. Consequently

    1≤t_i≤7,        t_i≤3+ω(t_i).

For t=5,6,7 the right sides are4,5,4, so every outlier has t≤4. If t=4, the unique possible occupied baseline is the baseline2-carrier b (2 divides r_b), and the outlier meets that cell and ALL THREE holes. All outlier cofactors are then odd.

## 3. The t=4 branch is impossible

Suppose some outlier A has t_A=4. Its fibre index is4r_A, with r_A odd. A t=1 outlier has a coprime fibre index and cannot share any hole with A; it also cannot share a baseline. Thus t=1 is impossible.

A t=3 outlier C has index3r_C. This is coprime to4r_A unless3 divides r_A (all outlier cofactors are odd). If coprime, C could meet neither a hole nor the baseline2-cell, leaving at most the baseline3-cell, fewer than three cells. Hence every t=4 outlier coexisting with t=3 must carry the factor3. Cofactor coprimality permits at most one t=4 outlier in that situation.

### 3.1 Exactly one t=4 outlier and at least one t=3 outlier

Here3 divides r_A, so no baseline cofactor is divisible by3; every t=3 outlier meets all three holes. Each t=2 outlier has index2r_j, with r_j odd and not divisible by3. It is coprime to every t=3 outlier's index3r_C (since r_C is odd). Such a t=2 outlier could meet no hole, and only the single baseline2-cell, fewer than two cells. Thus t=2 is impossible as well. The other three outliers all have t=3. In each hole their three fibre indices together with4r_A have all pairwise gcds exactly3. Zhu Sun4 excludes these four pieces.

### 3.2 No t=3 outlier

All four outliers have t=2 or4. Put k=the number with t=4, so1≤k≤4.

- **k=1:** each of the four available cells (three holes plus baseline2-cell) already contains the t=4 piece. Two t=2 outliers in the same cell, together with it, would have all pairwise gcds2 and contradict Sun3. Each cell therefore admits at most one t=2 outlier. The three t=2 outliers require six incidences in only four such positions, impossible.
- **k=2:** the two t=4 outliers meet all four cells. Each cell admits at most one t=2 outlier by Sun3 with either t=4 piece. Neither t=2 outlier can meet the baseline2-cell: if v_2(r_b)=1, the baseline, one t=4 piece and that t=2 piece have all pairwise gcds2. If v_2(r_b)≥2, use the baseline and both t=4 pieces with the t=2 piece; their indices are (4(r_b/4),4r_A,4r_B,2r_C), with pairwise-coprime cofactors and r_C odd, so MS45 applies. Thus two t=2 outliers need four incidences in only three holes, each admitting at most one, impossible.
- **k=3:** any cell met by the t=2 outlier contains all three t=4 pieces. Their four fibre indices are exactly the MS45 pattern (2r_C,4r_A,4r_B,4r_D), with r_C odd; impossible.
- **k=4:** in the baseline2-cell, the baseline and four outliers have every pairwise index gcd at most4. S5 forbids these five disjoint pieces.

This exhausts t=4. Hence all four outliers have t∈{1,2,3}.

## 4. A six-residue fibre capacity, with exact arity control

For all eight vertices now t_i≤3. Every pairwise gcd of λ_i=r_i t_i divides6: any shared prime must come from one of t_i,t_j, and its common exponent is at most1 because the cofactors are pairwise coprime and t_i,t_j∈{1,2,3}.

Every hole contains at most the four outliers. Every baseline cell contains at most three pieces TOTAL. Indeed, an outlier sharing baseline b must have t=2 with2|r_b or t=3 with3|r_b. If both types occurred there, the two outlier indices would be coprime (the baseline owns both prime factors). If only t=2 occurs, Sun3 permits at most one outlier beside the baseline; if only t=3 occurs, Sun4 permits at most two. A t=1 outlier cannot share any baseline.

Thus EVERY cell contains at most4 pieces. MSB applies to its actual disjoint fibre cosets and gives disjoint integer congruence classes with these λ indices. Put

    d_i=gcd(λ_i,6).

For a fixed cell, enlarge each congruence class to its residue class modulo d_i. These enlarged classes remain pairwise disjoint: because gcd(λ_i,λ_j) divides6, it equals gcd(d_i,d_j); the original residue inequivalence modulo that gcd is unchanged. Counting in Z_6 gives the exact necessary inequality

    sum_{i meeting that cell} 1/d_i ≤1.                 (C6)

This is not an invocation of a general G-to-Z theorem. The length≤4 premise was verified above. Summing C6 over the seven W-cosets yields

    sum_{i=1}^8 t_i/d_i ≤7.                            (GLOBAL)

## 5. Only two distinct exceptional owners can survive GLOBAL

A vertex whose r_i is coprime to6 contributes t_i/gcd(t_i,6)=1 to GLOBAL. At most one cofactor carries2 and at most one carries3.

If one vertex carries both2 and3, its maximum possible saving below1 is5/6 (at t=1); all other vertices contribute1. Total is at least43/6>7. If only one prime carrier exists, or one carrier's t does not reduce its contribution, total is also strictly greater than7.

Therefore there must be two DISTINCT exceptional vertices E_2,E_3, with2|r_{E_2},3∤r_{E_2},3|r_{E_3},2∤r_{E_3}, and

    x:=t_{E_2}∈{1,3},        y:=t_{E_3}∈{1,2}.

Each E_2 contribution is1/2 (saving1/2); each E_3 contribution is1/3 (saving2/3). Other cofactors are coprime to6. For C6 their denominators are:

    E_2: d=2 if x=1, d=6 if x=3;
    E_3: d=3 if y=1, d=6 if y=2;
    ordinary t=1,2,3: d=1,2,3 respectively.

## 6. Vacancy argument: the exact surviving outsider pattern

Each ordinary t=1 vertex occupies a cell alone, because its fibre index is coprime to every other fibre index. Remove these q vertices and their q different cells. Let b be the number of ordinary t=2 vertices and c the number of ordinary t=3 vertices. Remaining vertices number b+c+2, and remaining cells number b+c+1.

Call a remaining cell a2-cell if it contains at least one ordinary t=2 vertex, a3-cell if it contains at least one ordinary t=3 vertex, and a0-cell otherwise. A2- and3-cells are disjoint classes because ordinary2 and ordinary3 indices are coprime. Let their counts be h2,h3,h0. Since each2-cell holds at most two ordinary2 pieces and each3-cell at most three ordinary3 pieces, incidence counting gives h2≥b and h3≥c. Hence h0≤1.

### 6.1 h0=1 is impossible

Then h2=b and h3=c. All2-cells are full with two ordinary2 pieces; all3-cells are full with three ordinary3 pieces. C6 leaves no room for an exceptional piece in these cells. Both exceptionals must therefore occupy the unique0-cell. This is impossible if x>1 or y>1; if x=y=1 their denominators2 and3 are coprime and their fibre cosets cannot share a cell. Thus h0=0.

### 6.2 The extra cell cannot be a2-cell

If h2=b+1,h3=c, all3-cells are full. Both exceptionals must occur in2-cells. E_3 cannot have y=1 (denominator3 is incompatible with an ordinary2 piece), so y=2 and E_3 has d=6. Its two distinct cells can hold at most one ordinary2 piece each by C6; it forces at least two ordinary2 vacancies. There are exactly2h2−2b=2 vacancies total. Consequently precisely those two E_3 cells have one ordinary2 piece each, and all other2-cells are full.

If x=1, E_2 has d=2 and cannot fit either E_3 cell (C6 sum1/2+1/6+1/2=7/6) or any full cell. If x=3, it needs three distinct nonfull cells but only the two E_3 cells are available. Contradiction.

### 6.3 The unique remaining configuration

Thus h2=b,h3=c+1. All2-cells are full. E_2 must have x=3 and d=6, because x=1 would put denominator2 in a3-cell. Its three cells each have at most two ordinary3 pieces; this forces at least three ordinary3 vacancies. Total vacancies equal3h3−3c=3, so exactly those three cells have two ordinary3 pieces, and all other3-cells are full.

E_3 cannot have y=1: its d=3 piece would exceed C6 in an E_2 cell (2/3+1/6+1/3=7/6), and no other3-cell has space. Thus y=2 and d=6. Its two cells must be two of E_2's three cells, each then saturating C6 at2/3+1/6+1/6=1. The third E_2 cell has C6 weight5/6.

Since x=3,y=2, neither exceptional is a baseline. All four original baselines are therefore ordinary t=1 vertices removed earlier. At most two ordinary vertices remain among the original four outliers, so b+c≤2. But E_2 uses three3-cells, so c+1=h3≥3 and c≥2. Therefore

    b=0, c=2, q=4.

**Theorem R4 (necessary exact subcase reduction).** If an index-seven W contains four subgroup vertices of P7, then after renaming, exactly four baseline cells are exclusive and the other three cells are holes. Four outliers A,B,C,D satisfy:

    t_A=3, 2|r_A, 3∤r_A;
    t_B=2, 3|r_B, 2∤r_B;
    t_C=t_D=3, gcd(r_C r_D,6)=1;
    gcd(r_b,6)=1 for every baseline b.

A,C,D meet ALL THREE holes. B meets exactly two of them. No outlier meets a baseline cell. In the two holes met by B, there are four pieces of respective core denominators(6,6,3,3); the third hole has core denominators(6,3,3). This is an actual necessary fibre-incidence statement, NOT a construction or proof that those pieces/globally consistent subgroups exist.

## 7. A rigorous finite permutation-image bridge for R4

Let N=core_G(W), and Q=G/N with its faithful transitive degree-seven action on the left W-cosets. It is finite and Q≤S7, even when the original G was infinite. Put V_i=U_iN/N, c_i=[N:N∩U_i], and D_i=[Q:V_i]. Then n_i=c_iD_i and the orbit of W/N under V_i has the SAME size t_i=[U_i:U_i∩W].

The group Q has exactly one factor7 in its order (7 divides its order by transitivity and 7^2 does not divide7!). If7 did not divide D_i, then7 would divide |V_i|. By Cauchy's theorem V_i would contain an element of order7, which in S7 is a7-cycle. Such a subgroup is transitive on all seven points, contrary to t_i≤3. Hence7|D_i for EVERY i.

It follows that the c_i are pairwise coprime: their prime factors other than7 lie in the private r_i, and7 can divide at most one c_i because at most one r_i is divisible by7 and each D_i has a factor7. LemmaQ of `structural-addendum-v1.md` applies: overlap of projected cosets would create two disjoint pieces of coprime indices c_i,c_j in the same N-coset. Therefore the eight projected LEFT cosets in Q remain pairwise disjoint. Their pairwise index gcds are again exactly7.

The six ordinary vertices (four baselines and C,D) have r_i coprime to6. Their D_i/7 can therefore only have prime factor5, because D_i divides |Q| and |Q| divides7!. At most one of C,D can have that factor, so at least one has D_i=7. Call its subgroup K≤Q. It has an orbit of size3 on Q/(W/N). Its remaining four points form an invariant complement; thus K embeds in S3×S4 and

    |Q|=7|K| divides 7·3!·4!=1008.

In particular5 does NOT divide |Q|. Therefore ALL SIX ordinary projected subgroup indices equal7. Their four baseline subgroup images are exactly H=W/N, since they lie in H and have the same index7. The remaining two projected indices have the form

    D_A=7·2^a,        D_B=7·3^b,
    1≤a≤4,           1≤b≤2.

The exponents must be positive: if either exceptional index were7, seven of the projected cosets would have index7 and cover all of Q, leaving no room for the eighth. The upper bounds follow from |Q| dividing1008=2^4·3^2·7. No classification of finite permutation groups or enumeration is being assumed.

**Finite-image residual.** Any surviving R4 configuration produces an actual transitive subgroup Q≤S7 of order dividing1008, six disjoint cosets of index7 (four are distinct H-cosets), and two further disjoint cosets of indices7·2^a and7·3^b, with the SAME exact three-hole incidence above. K of index7 has an orbit3 on Q/H. A local tuple of these numbers is not an example.

## 8. Honest endpoint

The G4 route is not closed. The residual in section7 has not been excluded or realized. A rigorous exclusion of that finite permutation-image geometry would prove that every four subgroup vertices generate G, improving G5. Even that would NOT prove unrestricted Sun8 without a further argument excluding P7 with all such joins equal to G.

No native group enumeration, old checker, new script, solver, executable scientific check or modelCLI has run. All arguments above are written. Parent and separate-agent reconstruction of this new snapshot are not yet performed; earlier review assignments to `reduction-and-generation-v1.md` do NOT cover this file or its additional imports.
