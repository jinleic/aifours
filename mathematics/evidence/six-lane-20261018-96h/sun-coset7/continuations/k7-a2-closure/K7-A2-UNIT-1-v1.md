# K7-A2-UNIT-1-v1: local row/cell tools and a restricted-granularity Case-A closure [CANDIDATE_UNVERIFIED]

Written: 2026-10-19T13:43:32-0700 (`/bin/date` immediately before exclusive create). Owner SunM13MixedFibres. Written only; no scientific
computation/model call. Scope K7-A2-SCOPE-v1.md 4a9502ac1116a4a0f06a92ffa8fc95e00a60595fe051085ffb5fa17f0a2ee320.
This unit proves conditional-on-EXPLICIT-HYPOTHESES local lemmas, not (a2) closure alone. Units 2/3 verify their hypotheses.
Nothing from a pending unit or older pending candidate is a premise. Every new statement CANDIDATE_UNVERIFIED.

## 0. Common setting and notation
G finite; seven pairwise disjoint left cosets g_jU_j, V={z,t} disjoint-union W, |W|=5; n_j=6r_j with r_j pairwise coprime.
r_z=2^E w_z, r_t=3^A w_t, E,A>=1; r_u=rho_u for u in W, all rho_u odd, prime to3, pairwise coprime and coprime to r_z r_t.
At most one rho_u has a 5-part (that vertex is p); rho_p=5^B w_p, B>=1, while the other w's are prime to30. All w's pairwise
coprime. This is exactly the (a2) index arithmetic; no vertex is changed into an unmarked one.
Gamma^alpha=(g_jU_j), Gamma^alpha*=(g_j^-1 U*_j), U*_j=g_jU_jg_j^-1. INV makes both actual disjoint-coset configurations,
with the same labelled indices, and (Gamma*)*=Gamma. For x one family, x' is the other; Phi_j,h_j denote its subgroups and
representatives. T_x(Q)=[G:intersection_(j in Q) Phi_j]. In that configuration mu(Phi_jPhi_k)=x_jk/6, and at an apex u the LFC
labels are r_j x_uj; j meets n_u x_uj/6 left Phi_u-fibres, none u's own fibre. A set of labels is allowed if every subset of
size q>=2 has a pair with gcd>=q. Feasible y>=0 has sum<=1 on all allowed sets; val_x^u(y)=sum_(j!=u)y_j x_uj. LFC gives
val<6. Allowedness is hereditary; zero weights can always be omitted in feasibility checks.
After normalising h_a=1, X_j=Phi_aPhi_j, D_j=Phi_a h_j Phi_j: mu(D_j)=x'_aj/6, D_j disjoint from X_j, and each D_j is a union of
right Phi_a-cosets. Their pieces in a common right coset have indices d_j=r_j x'_aj and satisfy the same hereditary Sun
condition (VFC). Their union misses Phi_a, hence has measure<1. L_j^(u)=h_jPhi_jPhi_u is the union of left Phi_u-fibres meeting
j. Superscripts on L,D indicate apex when needed. mu=|.|/|G|.

## 1. Exact foundational interfaces and scope
Only accepted R0, L0.1-L0.3, Lagrange, LFC(a)-(d), INV(a)-(b)/E6/E7, VFC(V1)-(V4), and L1(T1)-(T3) are imported. Authorities:
O16/README.md 2a6d6d6e…3fd1 §§0-1; O16/rules-k7-v1.md 77b9afec…3cee §§0-2, written verdict 73a25ba6…9f35; S/K7-LFC-INV-v1.md
45be9162…726c §§1-2 with erratum 7af9acf0…75bd5 E1-E3/E6-E7, verdict 8621e744…cca18. Full paths/hashes/ranges in the manifest.
Sun(2), Sun(3), Sun(4) are used only inside LFC/VFC (or a subgroup in the cell lemma). Sun(5)/(6), computer-assisted, remain
transitive imports through the packages and class reduction. No Sun(7), K62-SG or arbitrary auxiliary-family theorem.
Older arguments below are attributed to K23/CELL with K23E, ecff R2.1-R2.4 and E1-E29 (R2 verdict 9b0f7df5), TC/A22 through OV1
then OV2 (A1/A2 verdict 2a7c5b6c), and pending TX/ZA/ZB through ZE1-ZE4/ecff. They are RE-DERIVED at the present explicit local
scope; no (a1) theorem is applied to an (a2) configuration and the accepted (a1) closure is not re-proved.

## 2. Omitted-marker bounds: the exact hypotheses used later
At u in W, for each family x, write G_z(u,x) for both following properties:
(L_z) if feasible y_z=0 then val<=5; if val=5, every left fibre with S_F not contained in {z} has y(S_F)=1;
(V_z) in Gamma^x at u, mu(union_(j notin {u,z}) D_j)<=5/6.
Define G_t(u,x) by replacing z with t. In this unit these are HYPOTHESES whenever invoked, not blanket claims about K7.
Full row granularity gcd(n_u,T_x'(V\{u}))=6 supplies L_z,L_t; the own-family gcd supplies V_z,V_t. A subset gcd6 supplies
only the corresponding omitted-marker properties. Unit 2 proves the needed subset gcds directly for K7(a2-zt5).

**TC (any actual configuration, no granularity).** For three distinct u,a,j,
L_j^(u) subset L_a^(u) iff D_j^(a) subset X_u^(a); consequently D_j^(a) cap D_u^(a)=empty.
Proof: normalise h_a=1. L_a^(u)=Phi_aPhi_u. If h_jPhi_jPhi_u subset Phi_aPhi_u, then Phi_a h_jPhi_j subset Phi_aPhi_u; conversely
this latter containment implies h_jPhi_jPhi_u subset Phi_aPhi_u. V1 makes D_u disjoint from X_u. QED.
**K3 (distinct u,a,j; j,a!=z).** If a row at u forces L_j subset L_a, then x'_aj+x'_au<=5.
Proof: TC makes D_j,D_u disjoint at a. Their measures sum (x'_aj+x'_au)/6<1 by V4; integrality gives <=5. Thus the familiar
4+2 kill needs NO FG union bound, only V4. (The old K23 proof used V_z<=5/6; this sharper import accounting is deliberate.)

## 3. Row tools (all proofs local; p may be any positive- or zero-weight vertex)
Fix u in W with c=x_uz=3. In sections 3-6 assume its W-entries and e=x_ut lie in {1,2,4}, and G_z,G_t hold for this row.
Labels: a_j rho_j (j in W\{u}), 3*2^E w_z, e*3^A w_t. On the five non-z labels odd parts are pairwise coprime whenever all
a_j,e are powers of2; the z/t odd parts share3, and are NEVER asserted coprime. All 5's occur only in rho_p.
A two/four class has pair gcd2 except between fours (gcd4): triples need two fours, four-sets need three fours; isolated
ones share no positive label. These facts, via Sun(2)-Sun(4), verify all vectors below. Extra zero-weight labels do not affect
feasibility. A displayed value5 vector uses L_z or L_t at the stated omitted marker.

**B (single-four rows).** If at least three W-entries are<=2, then the row is (2,2,2,4|e=4) or (1,2,2,4|e=4), and E>=2.
Proof: if no W-four, weights1 on ones and1/2 on twos,z (t0) give4+3/2>5 (if all ones, z1 gives7): L_t. W-parts1114 and1124
have W-only value>=7,6. In1224/2224 with E=1, half on twos,four,z and1 on the one gives13/2: L_t. For E>=2,e=1, W-only value5
(one1,four1 for1224; half on2224) plus t1 gives6: L_z. For e=2, one1 and half on twos,four,t (z0) gives6: L_z. Thus e=4. QED.
**Rigid row list.** A row is its W-multiset followed by e; fours f, twos s, one o.
R1: (2,2,4,4|2), any E>=1: y_A=(f1/2,s1/2,s2/2,t/2), y_B=(f2/2,s1/2,s2/2,t/2) have value5, vanish on z, and are feasible:
three positive labels have pair gcd2, so at most two occur. Equality subtracts to give L_f1=L_f2.
R1minus: (2,2,4,4|1): y_A=(f1/2,f2/2,t1), y_B=(f1/4,f2/4,s1/2,s2/2,t1), value5, z0. t is coprime to all W-labels;
for weight1 under both, #fours=2#twos unless t is present, forcing both fours or neither. Thus L_f1=L_f2.
R3/R3prime: (2,2,2,4|4) / (1,2,2,4|4), E>=2 (B). y_A: half on f and all twos,1 on o if present; y_B: replace f/2 by t/2.
Both value5, z0; no positive triple containing two twos and f or t is allowed. Equality on fibres meeting f or t gives
L_f=L_t. We shall not import an L_z-containment from this z-free equality clause.
R4/R5: (1,4,4,4|e)/(1,2,4,4|e), e=2 or4, any E>=1. For every four f the vector (o1,f1) has value5 and vanishes on both z,t.
The one is coprime to all other labels (e,c not5). Using L_z or L_t as necessary, every occupied fibre not containing o
contains every four: L_j subset L_f for j!=u,o, including j=z. In particular all four L_f coincide.
R6: (2,4,4,4|1). Vectors (f_i1,t1), value5,z0, are feasible (f_i and t coprime). Any fibre meeting the two-label s or a four
cannot contain t (coprime); hence L_s subset L_fi for each i, and all L_fi coincide. No claim on a z-only fibre.
Rows (1,2,4,4|1) and (1,4,4,4|1) are impossible: o1, fours1/2 or1/3, t1 (z0), value6>5.
Every row has a W-four (B); at most one W-one (two ones plus any one four at weight1 give6>5). These include every R2 repair
of the row list; R3prime's t weight is1/2, NOT1; R4 is proved here at c=3; R6's equal-four conclusion is explicit.

**Twins.** For a triangle in W cup {t} whose entries are powers1,2,4, L1 gives tau_min=largest, tau_max=product of the two
smaller entries (ell-divisors are odd). Thus (1,a,b) forces a=b. If x_uv=1, the two endpoints have equal x-four
neighbourhoods and equal t-entries. This is only a necessary triangle rule, not a group-realisation statement.

## 4. Conditional Case-A classification, all degree branches
Assume, for BOTH families at EVERY W-vertex: c=3; W-W/W-t entries in {1,2,4}; G_z,G_t. Also assume:
(CL) if Gamma_x={uv in W:x_uv<=2} is connected, at least two t-entries of x' on W equal4.
These are the complete hypotheses H_A. Unit 2/3 establishes them where used.
F={alpha=4 on W}, F'={alpha*=4}, disjoint; d,d' their degrees; P={alpha_t=4}, P'={alpha*_t=4}, disjoint.
By B/row list d,d'>=1 and d+d'<=4. A degree1 vertex in F lies in P and E>=2; degree1 in F' lies in P'. No type(1,1).
So types are12,13,21,31,22. A four-vertex graph cut complement on five vertices is disconnected only when F contains a
K1,4 or K2,3; maxdegree3 excludes K1,4. Thus CL is applicable unless F contains K2,3 (and dually).

**K2.** There is no a single-x-four and s single-x'-four whose x'-four is a.
Proof: s's row R3/R3prime in x' gives L'_a=L'_t. a's single-x-four gives x_at=4; x_as<=2 since x'_as=4. If x_as=1, twins make
s single-x-four too: forbidden type11; hence x_as=2. At apex a of Gamma^x', TC/K3 gives 4+2 impossible. QED.

**Type list.** If a vertex v has type31 with unique F'-neighbour g, no vertex has F-degree1: g cannot have degree1 by K2;
if any F-neighbour a of v had degree1, K2 with roles reversed would kill(v,a). Thus n12=n13=0. The inverse statement holds.
If no degree3 occurs, parity makes n12,n21 even; apart from all22, up to actual inversion their counts are
(n12,n21,n22)=(4,0,1),(2,0,3),(2,2,1).
If degree3 occurs, normalise its direction to31; n31 is even by the F-degree sum and n31+n21 even by the F'-degree sum;
the possibilities are (n31,n21,n22)=(4,0,1),(2,2,1),(2,0,3). No orientation branch is dropped: inversions are actual Gamma*.
Four degree1 vertices in EITHER family are impossible: they give >=4 entries4 in its P, leaving <=1 in opposite P; that
family's four-graph has degree sequence11112 (three edges), hence connected complement, and CL gives >=2 opposite fours.
This kills the (4,0,1) no3 case and both (4,0,1),(2,2,1) degree3 cases, replacing the long old S-f argument entirely.
The remaining cases are exactly:
(a) no3, (2,0,3). F' is a5-cycle; F lies in its complementary5-cycle with four edges: path u0-a-b-c-u1. F'={u0b,u0c,ac,au1,bu1}.
All F/F' neighbourhoods differ; twins give no W-ones. Endpoints' alpha-rows R3 give alpha_tu0=alpha_tu1=4. The triangle
(t,u1,a) has (4,2,alpha_ta), so alpha_ta!=1. At a, its starred fours are c,u1: if alpha*_ta<=2, R1/R1minus gives L'_c=L'_u1;
at apex u1, alpha_u1c=4,alpha_u1a=2: K3. Therefore alpha*_ta=4,alpha_ta=2; a's alpha-row R1 gives L_u0=L_b, and at b,
alpha*_bu0=4,alpha*_ba=2: K3. Contradiction.
(b) no3, (2,2,1). Name A1,A2 type12, B1,B2 type21, C type22. F has degree11222, so triangle+edge or a path with ends A1,A2.
The full possibilities (up to A/B endpoint relabelling/reversal) and their K2 violations are:
* triangle B1B2C plus A1A2: F'={A1C,A2C,A1B1,A2B2}, and (a=A1,s=B1) is forbidden;
* path A1-B1-C-B2-A2: F' either {A1C,A2C,A1A2,B1B2}, killed by K2 with roles reversed on(A1,B1), or
  {A1C,A2C,A1B2,A2B1}, killed on(A1,B2);
* path A1-C-B1-B2-A2: F'={CB2,CA2,A1B1,A1A2}, killed on(A1,B1).
Completeness: the degree2 vertices of a connected path are B1,B2,C, so C is middle or adjacent to an endpoint; otherwise
F is its only possible cycle (B1B2C) plus A1A2. The listed F' follow its prescribed degrees and disjointness from F.
(c) degree3, (2,0,3). F' again has degree11222: either path v1-x-y-w-v2 or triangle xyw plus v1v2. N (neither four) is empty.
For the path, all neighbourhoods differ, so no W-ones. At x its alpha-fours w,v2 form an R1/R1minus unless alpha_tx=4;
if rigid, at apex w the masses alpha*_wv2=4,alpha*_wx=2 give K3. Thus alpha_tx=4; its starred row R1/R1minus has fours v1,y;
at apex y, alpha_yv1=4,alpha_yx=2 give K3. The only remaining possibility is triangle+edge: F=K2,3 on {v1,v2}|{x,y,w},
F'={xy,xw,yw,v1v2}. This proves the classification except for the still possible all22 case treated next.

## 5. The all22 case is impossible under H_A (shortened A22 count)
F,F' are complementary5-cycles. Different neighbourhoods and twins exclude all W-ones, so alpha/alpha* are2 or4 on all W.
For a row2244 with e<=2, R1/R1minus gives equality of its two four-fibres. Both complement graphs are connected, so CL
implies |P|,|P'|>=2; they are disjoint. If |P|=2, a5-cycle has a vertex u whose F-neighbours w1,w2 avoid P (adjacent endpoints:
use the opposite vertex; nonadjacent: use an endpoint). If |P|>=3, then |P'|=2 and invert first. At w1 its two four-fibres
u,w1' are equal. TC at u gives D_w1' disjoint D_w1, of masses alpha*_uw1'/6=4/6 and alpha*_uw1/6=2/6. Their sum is1,
contradicting V4's union<1. No elaborate overlap estimate, no full FG at u and no Sun(5) are needed for this final count.

## 6. Case-A refined matrix and its cell exclusion
In the remaining K2,3 orientation x=alpha, F as above: v1,v2 single starred-four force alpha*_tv=4,E>=2, alpha_tv<=2.
The distinct F'-neighbourhoods give alpha*=2 on F. For each a in {x,y,w}, unless its alpha-row is R2=(2,2,4,4|4), row rigidity
(R1/R1minus/R5; 1144 and1244|1 excluded) gives L_v1=L_v2; at apex v1 the masses alpha*_v1v2=4,alpha*_v1a=2 give K3. Thus
alpha_ta=4 and alpha=2 inside {x,y,w}. Suppose alpha_v1v2=1. Then the v-rows R4 have e<=2 and not1, so L_z subset L_a at both
v_i. TC at apex a=x gives D_z disjoint D_v1,D_v2; their measures3/6,2/6,2/6. The t-free union (V_t) has measure<=5/6 and
contains these three sets and D_y (4/6). Thus D_v1=D_v2=:R (measure2/6), outside D_z; and D_y must meet R (their sum1 exceeds
5/6 in that same union). A common right coset carries y,v1,v2 with indices4rho_y,2rho_v1,2rho_v2 of pairwise gcd2: Sun(3).
So alpha_v1v2=2. The t-row44411 is impossible by ordinary LFC at t: fours1/3,ones1,z0 feasible of value6 (ones coprime to
fours; no five-index Sun instance). Hence alpha_tv1,alpha_tv2 are1 or2, not both1. This is the complete matrix M_A below.

**Five-index EQ (local, NO six-index coprimality).** At an apex a in W assume five NON-z sets D_j have measures4/6 twice,
2/6 three times, with respective local indices4 times odd,2 times odd and pairwise coprime odd parts. If their union has
measure<=5/6, the two4/6 sets coincide. Proof: let B their large-set union (measure b>=4/6), Q the five-set union. A right
coset in B contains at most one small index (three with two small indices would have pairwise gcd2), and outside B at most
two small indices (Sun3). Small total mass1<=b+2(mu(Q)-b)<=10/6-b gives b<=4/6; equality of both large sets. The z-index,
which may share3 with t, is not used. This supplies exactly the repaired R2/R3 EQ interface.
**SUB (general).** At a, D_j=D_k=G\X_j and x_jk=x_aj=2 imply K=Phi_aPhi_j=Phi_jPhi_k is an index3 subgroup containing all
three. Proof: X_j=G\D_k is right-invariant under Phi_k and Phi_j; their generated subgroup lies in X_j, whereas Phi_jPhi_k
already has its measure1/3. Thus all equal. L0.2 gives h_aK!=h_jK,h_jK!=h_kK; if x_ak=2 also h_aK!=h_kK.
**IN (general, i!=j).** If K index3 contains Phi_j and i's coset meets h_jK, then x_ji<2m_i^K, m_i^K=[Phi_i:Phi_i cap K]<=3.
Proof: its LFC fibres at j distribute equally among its m_i^K occupied K-cosets (left multiplication by h_iPhi_i h_i^-1 is
transitive on them and preserves the j-fibre partition). Within h_jK there are n_j/3 fibres, one j's own, so
n_j x_ji/(6m_i^K)<=n_j/3-1. If x_ji=4, m_i^K=3. Also Phi_l subset K and x_il/6>1/3 imply m_i^K>=2 by Phi_iPhi_l subset Phi_iK.
**CELL (vertex-wise, general).** K,L index3 and LK=G imply H=K cap L index9; intersections of a K-coset and an L-coset are
the nine H-cells. If Phi_v subset K and m_v^L=3, its coset meets each cell of its K-column, in an H-coset of Phi_v cap L of
index n_v/3=2r_v. Likewise Phi_a subset L,m_a^K=3. This needs no assumption that qualifying vertices occupy distinct
columns. For any other j, a nonempty cell-piece has index N_j=[G:Phi_j cap K cap L]/9=n_j ab/9 with integers a,b<=3, so only
prime factors2,3 or from r_j. Three distinct vertices' pieces in one cell are disjoint subgroup cosets in H; pairwise index
gcd<=2 is impossible by Sun3. Proof: L0.1 gives [G:H]=9; inject the nine H-cosets into the nine K/L pairs to get bijection;
LFC splitting inside each cell gives n_vm_v^L/9; the successive index brackets a,b are<=3. This re-proves the accepted
vertex-wise form with its LK=G hypothesis, not the false K!=L shortcut.

**M_A exclusion.** Suppose W={v1,v2} cup {x,y,w}, alpha has a-v and a-t=4, aa'=2, v1v2=2, z-W=3; alpha* has av=2, aa'=4,
v1v2=4,tv=4; alpha_tvi in {1,2}, not both1, alpha*_ta in {1,2}. Assume V_z at W in Gamma^alpha. Then no such configuration.
Proof: choose i' with alpha_tvi'=2, i the other. At v_i the five non-z masses are v_i',t:4/6, x,y,w:2/6; all non-z odd parts
coprime. EQ gives D_vi'=D_t, and alpha_vivi'=2 gives D_vi'=G\X_vi'. SUB produces K index3 containing v1,v2,t, with v1,v2 in
DISTINCT K-cosets. At t in Gamma^alpha*, ordinary LFC excludes two a's having alpha*_ta=1: weights1 on those ones and1/2
on v1,v2 (entries4) give6. Choose x with alpha*_tx=2. At x in Gamma^alpha, EQ gives D_y=D_w; SUB makes L index3 containing
x,y,w, in its three distinct cosets. For each a in{x,y,w}, mu(Phi_aPhi_v1)=4/6 yields m_a^K>=2; any two K-cosets include
v1's or v2's distinct column, and IN at that v forces m_a^K=3. Each j in{v1,v2,t} has m_j^L=3 by the three L-cosets and
IN (all alpha_aj=4). Thus Phi_xK=G and Phi_x subset L, so LK=G BEFORE any assertion about t's K-position.
If t shared v1's column, the vertex-wise CELL gives in each cell pieces v1,t,a with indices2rho_v1,2*3^A w_t,2rho_a,
pairwise gcd2; impossible. Hence v1,v2,t occupy distinct columns. A cell in either v-column already has v,a pieces;
any z-piece has index with primes2,3,w_z, hence gcd with the two distinct W-pieces<=2 (including p's unique5). Thus z misses
both columns, lies in t's column and Phi_z subset K. But Phi_zPhi_v1 subset K has measure<=1/3 while alpha_zv1/6=1/2. QED.

**M_B exclusion (explicit data, no Case-B label assumed outside its scope).** Work in Gamma^alpha*. W={a1,a2,a3,v1,v2};
alpha: aa'=4,av=2,v1v2=4,tv=4,ta=2,za=3; alpha*: aa'=2,av=4,v1v2=2,ta=4,tv in{1,2},za=3. Assume V_z at W in Gamma^alpha*.
Then no such configuration, regardless of alpha_zv and the z-t entries (only the displayed data are used).
Proof: at a1, non-z masses a2,a3:4/6, v1,v2,t:2/6. EQ+SUB give H index3 containing all a's, each in a distinct H-coset.
At t in Gamma^alpha*, LFC forbids both starred tv=1: a-entries4 at weight1/3 and the two ones at weight1 give6.
Choose i' with alpha*_tvi'=2. At v_i, EQ+SUB give K index3 containing v1,v2,t, with the two v-columns distinct. Products
mu(Phi_aPhi_v)=mu(Phi_aPhi_t)=4/6 and IN give m_v^H=m_t^H=3; m_a^K>=2 and the two distinct v-columns with IN give m_a^K=3.
Hence Phi_aK=G,Phi_a subset H =>HK=G before t-placement. Vertex-wise CELL rules out t sharing a v-column by the v,t,a
pieces (indices2rho_v,2*3^A w_t,2rho_a). z misses every cell in both v-columns (v,a,z indices gcd<=2), so Phi_z subset K and
z lies in t's column. Its cell index is N_z=[K cap H:Phi_z cap H]=n_z m_z^H/9. Since v3(n_z)=1 and1<=m_z^H<=3, integrality
forces m_z^H=3, N_z=2^(E+1)w_z. In t's column pieces t,a,z have indices2*3^A w_t,2rho_a,2^(E+1)w_z, pairwise gcd2. z has no
cell, contradiction. The p-factor is unique and does not occur in N_z or r_t. QED.

## 7. Export contract and provenance
Exports are TC,K3; B and the rigid-row rules at c=3 under the indicated L_z/L_t hypotheses; Twins; the H_A Case-A theorem
(no configuration if BOTH families have c=3, W-W/W-t entries1,2,4, G_z/G_t and CL); the explicit M_A/M_B exclusions requiring
only their displayed matrices and V_z. The Case-A conclusion follows sections4-6 (all degree possibilities, all22, K23
refinement, M_A); the inverse K23 orientation is Gamma*, not an assumed relabelling. No unconditional (a2) claim in this unit.
Old arguments: row list and degree classification = K23 through all29 repairs, with simplified four-single-degree and A22
kills; EQ/SUB/IN/CELL/M_A/M_B = CELL through the vertex-wise repairs, re-proved here. The role of these proofs is exactly
the wider-scope transfer, not a fresh proof of the accepted (a1) closure. Unit3 must verify H_A or M_B, not merely cite their
headings. No dependency on Unit2/3. No novelty, Lean, human or fullK7/Sun7 claim.
