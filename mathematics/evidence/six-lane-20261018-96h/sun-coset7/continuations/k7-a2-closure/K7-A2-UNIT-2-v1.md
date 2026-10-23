# K7-A2-UNIT-2-v1: normalised z-t-five prerequisites, re-derived in small form [CANDIDATE_UNVERIFIED]

Written 2026-10-19T13:46:04-0700 (`/bin/date` immediately before exclusive create). Owner SunM13MixedFibres. Written only. Frozen scope
4a9502ac…e320. This unit has NO dependency on Unit1 or Unit3. The B-row test used here is proved in section4. All new results
CANDIDATE_UNVERIFIED. ZA/ZE1-ZE4/ecff's R3 repairs are argument origins, NOT premises; no NO_VERDICT is counted as approval.

## 0. Exact setting and accepted interfaces
Finite G, seven disjoint left cosets, n_j=6r_j, V={z,t} disjoint-union W, W=W' cup {p}, |W'|=4;
r_z=2^E w_z,r_t=3^A w_t,r_p=5^B w_p,E,A,B>=1; r_u=w_u (u in W'); all w's prime to30,pairwise coprime. Put rho_u=r_u for u in W:
odd, prime3, pairwise coprime. Actual inversion Gamma*=(g_j^-1 U*_j), U*_j=g_jU_jg_j^-1, swaps alpha,alpha* and keeps the labelled
indices/markers (INV/E6). T_x(Q) denotes subgroup-intersection index in the actual x-configuration. At u, labels r_j x_uj,
val=sum y_j x_uj; LFC val<6. VFC sets D_j at a normalised apex have measures x'_aj/6, local indices r_j x'_aj, union<1.
Foundational imports only: R0,L0.1-L0.3,Lagrange,LFC(a)-(d),INV(a)-(b),VFC(V1)-(V4),L1(T1)-(T3), Sun(2)-Sun(4). Authorities:
written verdict73a25ba6, LFC verdict8621e744 through E1-E3/E6-E7. Sun5/6 remain computer-assisted transitive imports.
Normalised **S-data**, imported from accepted A2-FIVE Lemma F / D23-a2 / Proposition ZT5 (S1)-(S5), read through OV1 then OV2
(A1/A2 verdict2a7c5b6c, RICH/D23P verdict1167bc4f):
 alpha_zt=5, alpha*_zt=1; alpha_zu=3 (u in W); alpha*_zu in{1,2,3}; T*={u in W:alpha*_zu=3}, |T*|>=3;
 alpha_tu in{2,4} (u in W'), alpha_tp in{1,2,4}; all other entries in either matrix<=4; E>=2.
Accepted FG-a2 interface: for an actual subgroup family beta (either actual alpha-matrix),
(a) at u in W', gcd(n_u,T_beta(V\{u}))=6 if 5 does not divide beta_zt OR 3 does not divide beta_zp OR beta_tp is odd;
(b) at p, gcd(n_p,T_beta(V\{p}))=6 if beta_zt!=5 and beta_zu<=3 on W'.
Only beta=alpha*, whose zt=1 and zu<=3, is used for FULL gcd6 here. No arbitrary auxiliary beta<=5 theorem is assumed.
The manifest includes the literal accepted statements and applicable mandatory overlays; their long ancestor proofs are not
repeated. The S-data imply gcd label formulas used below even when a named W-vertex is p (retain its rho_p=5^B w_p).

## 1. Light sets for arbitrary subsets, and the exact granularity map
**Light lemma.** In an actual configuration at v, for Q excluding v, let H=intersection_(j in Q) g_jU_jg_j^-1. The fibres
contained in H g_v U_v avoid each j-piece with j in Q and number at least n_v/gcd(n_v,[G:H]); proof: they number
[H:H cap g_vU_vg_v^-1]=[G:H cap g_vU_vg_v^-1]/[G:H], and the numerator is divisible by both indices. If hg_vu belonged to
g_jU_j, h=g_jag_j^-1 gives g_vu in g_jU_j, contradiction. If feasible y is supported in Q and gcd=6, double-counting LFC gives
val<=5; at val5 EVERY fibre meeting at least one Q-piece has weight1 (all inequalities in the light-fibre bound are equal).
In the x-configuration [G:H]=T_x'(Q) (common normalising conjugation changes no index).
VFC form: W_Q=intersection of OWN subgroups Phi_j (j in Q); Phi_vW_Q lies in all Phi_vPhi_j, outside all D_j (j in Q), with
measure>=1/gcd(n_v,T_x(Q)) by L0.1/Lagrange. Thus own gcd6 implies mu(union_Q D_j)<=5/6.

**Omitted-marker chain (FG-zf, re-proved).** For u in W, x either family, put Q_z=V\{u,z}, Q_t=V\{u,t}.
Then gcd(n_u,T_x(Q_z))=gcd(n_u,T_x(Q_t))=6.
Proof: Q_z ordered t,p,then W' (omit u if it is one of them); base factor x_tp<=4. When p is omitted (u=p), only t then
unmarked vertices enter and no index or factor has a5. Otherwise p second has gcd6 with t, and every subsequent e is
unmarked: gcd(n_e,T)=6 and multiplier k=6mu(Phi_eW)<=x_ej<=4. Thus no prime>3 enters except the prescribed w_j, and v5T=B if
p included,0 otherwise. Q_t is identical with z,p first (base x_zp<=3); then W'. At a singleton start the same step formula
applies, and at u=p no5 enters. For u in W', n_u=6w_u; for u=p the5-part is absent from T. Both give gcd6. This proof uses
only the actual K7 arithmetic and S-data, not K62-SG.
Consequences, in each orientation at each u in W:
(L_z)/(L_t): feasible vectors with y_z=0 / y_t=0 have val<=5, with weight1 on every fibre whose S is not contained in the
omitted singleton when val=5;
(V_z)/(V_t): unions of D_j excluding z / t have measure<=5/6.
Moreover FULL gcd6 holds for the alpha*-family over V\{u}, by accepted FG-a2(a)/(b) above: hence all feasible alpha-rows at
u have val<=5 and full occupied-fibre equality, and the full VFC union in Gamma^alpha* at u is<=5/6.
Full alpha*-LFC granularity, or full VFC in Gamma^alpha, is NOT asserted. In particular the z/t odd label parts share3;
z may share5 with p when its coefficient is5. These collisions are retained.

## 2. Alpha has no W-three (RICH local proof re-run, not imported outside (a1))
At u in Gamma^alpha, c=alpha_uz=3, e=alpha_ut in{1,2,4}. Assume a W-entry3 and let k be the number of W-threes. W-three
labels3rho_j are coprime to every W-nonthree (rho prime3, no entry5); their pairwise gcd is3. For a two/four class the
standard weights are one1, two1/2, four1/4 when there are<=2 fours (value=its size), or all1/3 on three fours (value4),
or1/4 on four fours (value4); singleton-class refinements give the two-entry values below. These weights are used on at
most four W-neighbours, so Sun2-4 suffice. FULL val<=5 from section1 applies.
W-only tests: k=1 gives value>=3+3=6. For k=2, pair-values on the remaining entries (11,12,14,22,24,44) are (2,3,5,2,3,4),
with feasible weights respectively (1,1),(1,1),(1,1),(1/2,1/2),(1/2,1/2),(1/2,1/2); only11,22 survive after adding3 from
the threes. k=3 leaves a single1 or2 (4 would give7). k=4 has no remainder. In particular any row with a three has NO W-four.
All other e-values are excluded by this short table (unlisted weights0):
* e=1: third-weights on the W-threes,z,t, plus remainder ones1 / twos1/2, except for remainder single2 use2/3. For k=2
  (11 or22), k=3 (1 or2), k=4 these give respectively16/3,16/3,16/3,17/3,16/3, all>5. Feasible: threes,z,t pairwise gcd3,
  so at most3; t odd is coprime to twos; z+two weight<=1; no three coexists with a nonthree.
* e=4,k=2,11: t1,ones1 gives6. k=2,22: threes1/4 each,t1/2,twos1/2 each gives11/2 (two twos with t form a forbidden
  gcd2 triple). k=3,1: threes1/3,t1/3,one1 gives16/3. k=3,2: threes1/3,z1/3,t0,two2/3 gives16/3. k=4: threes1/3,t1/3 gives16/3.
* e=2,k=3,remainder2: threes1/3,z1/3,two2/3 gives16/3, so this case also dies.
The only local survivors (NOT realisability claims) are e=2 and W-parts3333,3331,3311,3322. Each has a feasible value5
vector forcing every weight1 set through t to contain z:
3333: W-threes1/3,z1/3,t0; 3331: same plus one1; 3311: z1,ones1,threes/t0; 3322: threes1/4 each,z1/2,twos1/2 each,t0.
For the first two, sets through t with weight1 must be4-sets containing z,t and two W-threes (all other gcds3, z/t gcd6).
For3311, t is coprime to ones, so weight1 needs z. For3322, the possible weight1 sets through t are {z,t,three,three'}
or {z,t,two}; two twos with z or t are forbidden gcd2 triples. Thus full equality implies L_t^(u) subset L_z^(u).

Suppose alpha_uv=3 in W. For any other w in W, if neither alpha_uw nor alpha_vw is3, both are1,2,4; L1 on the triangle
(3,a,b) forces a=b=4: tau is divisible by3*max(a,b), at most3min(a,b) and at most a*min(3,a). This contradicts the
no-W-four conclusion at u. So every vertex of W has a W-three. Normalise g_z=1. For each such u, L_t^(u) subset L_z^(u)=U_zU_u implies
D_t=U_zg_tU_t subset U_zU_zU_u=U_zU_u; V1 makes D_u disjoint from this set. Thus D_t cap D_u=empty at z for each u in T*
(indeed for all W). At z, VFC labels are alpha*_zu rho_u on W and3^A w_t for t:
T* labels3rho have gcd3, incompatible with O*=W\T* entries1/2; t's label shares3 with T* but is disjoint from their D_u by
hypothesis. Put weight1/3 on T*, weight1 on O* ones and t,1/2 on O* twos. Every actually occupied right fibre has weight<=1:
inside T* at most3 (Sun4), outside it ones isolated (Sun2), at most two twos (Sun3). Weighted mass is
(|T*|+|O*|+1)/6=1, against V4 union<1. Contradiction. Thus **alpha has no W-three**. Its W-W entries are1,2,4; W-t already
are1,2,4 by S-data. The p marker causes no extra pair gcd (no coefficient5).

## 3. Connected-graph t-row bounds, ZT and ZTR (both re-proved)
For x one family, if Gamma_x={uv in W:x_uv<=2} is connected, order W along a spanning tree. Actual intersection index
T_x(W)=6(product rho_u)*2^h: first pair factor1 or2 and every later k<=2 by comparison with its earlier tree neighbour;
gcd at entering p is6 because no earlier index/factor has5. Hence gcd(n_t,T_x(W))=6 (r_t=3^A w_t has no5).
At t in Gamma^x the W-VFC union has measure<=5/6. Every feasible W-weight vector has sum y_u x'_tu<=5, with equality
saturation on the W-union. In an equality case the light product has measure1/6 and contains Phi_t; D_z, of measure
x'_tz/6>=1/6 and avoiding Phi_t, therefore meets the W-union in a right coset (its intersection with the light product is
at most1/6-1/n_t). On that coset the W-part has weight1 and is allowed together with z. This is a direct spanning-tree
argument in K7, not an unrestricted auxiliary FG assumption.

**ZT.** If Gamma_alpha is connected, b_u=alpha*_tu lies in{1,2,4} for every u in W and at least two b_u equal4.
Proof: initially b_u in{1,2,3,4} by Lemma F (no other5); d_u=b_u rho_u have entry gcds, while d_z=2^E w_z is coprime to
ones/threes and has gcd2 with twos. Let k count W-threes. Weights1/min(3,k) on them (at most3, Sun4), with standard
weights on the rest, yield>5 for k=1,2. For k=3, only remainders11,22 have pair-value2 (the other pair-values3,5,3,4 above
exceed2); vector threes1/3 plus ones1 or twos1/2 has value5. Its weight1 W-sets are a triple of threes, a singleton one or
a pair of twos, none allowed with z (Sun2/3). The equality witness of the preceding paragraph is impossible. k=4: the
remaining entry must1 and the same equality vector gives only a triple of threes or one; k=5: weight1/3 gives only triples
of threes. Both fail with z. Thus k=0. With one four, ones1,twos/four1/2 give6 (or onefour1 and fourones1 give8). With no
four, one two gives6 by singleton weights; otherwise ones1,twos1/2 yield value5 and only singleton ones/pairs of twos,
again impossible with z. So there are>=2 fours. No assumption that the t-row already avoids3 was used.

**ZTR.** If Gamma_alpha* is connected, at least two alpha_tu (u in W) equal4.
Proof: b_u=alpha_tu in{2,4} on W', b_p in{1,2,4}; extra z-index=5*2^E w_z and its mass5/6. The same spanning-tree bound in
Gamma^alpha* gives W-value<=5/equality saturation. One four: ones1,twos/four1/2 yields6 (there are at least3 twos). Zero
fours: W' all twos, p1 or2; ones1/twos1/2 gives value5, so W-union Q has measure5/6 and saturated W-sets are one p (if p1)
or two twos. A right coset in D_z cap Q omitting p would contain z and two W' twos, pairwise gcd2, impossible. Hence
D_z cap Q subset D_p; but mu(D_z cap Q)>=5/6+5/6-1=4/6 while mu(D_p)<=2/6. This explicitly retains the z-p5 collision. QED.

## 4. Two short local consequences: B-test and the exact T* split
**B-test** (re-derived for the alpha-rows needed here). At c=3, W-W/W-t entries1,2,4 and the omitted z/t bounds of section1,
at least three W-entries<=2 force exactly one four, e=4 and E>=2.
Proof: nofour: ones1,twos/z1/2,t0 gives11/2 (allones plusz1 gives7); 1114/1124 have W-value>=7,6. In1224/2224,E=1:
ones1,twos/four/z1/2,t0 gives13/2. E>=2,e=1: W-value5 (one1/four1, or allW1/2) plus t1 gives6; e=2: ones1,twos/four/t1/2,z0
gives6. Each uses an omitted-marker bound with the other marker weight0. QED.
**ZS.** Either T*=W, or |T*|=3 and W\T*={v1,v2} with alpha_v1v2=alpha_tv1=alpha_tv2=4 and alpha_va=2 for a in T*.
Proof: for a in T*,v outside, the starred z-a-v triangle has entries3,s<=2,b<=4. T1 makes tau divisible by3s (rho_a,rho_v
prime6), while T3 bounds tau<=bs, so b>=3: alpha*_av in{3,4}. Thus alpha_av<=3; section2 removes3, leaving1/2. Each
outside vertex has>=3 such small W-entries; B-test forces a W-four outside T* and t-entry4. Therefore the outside size is
not1, is<=2 (|T*|>=3), hence is0 or2. In size2, triangle(4,alpha_v1a,alpha_v2a) forces both cross entries2. This covers the
otherwise missed |T*|=4 case explicitly (impossible). E>=2 was already S5; no p placement in T* or its complement is excluded.

## 5. ZW: starred entry types in the T*=W branch
Assume T*=W, so c*=3 at every W-vertex. At u in Gamma^alpha*, let k count W-threes. W-only vectors as in section2 (using
L_z, not full granularity) show: k=1 impossible; k=2 permits only3311/3322; k=3 only3331/3332; k=4 gives3333. No W-four
coexists with a W-three. For3311/3322 the vector(threes1/3,t1/3,ones1 or twos1/2,z0) has value4+alpha*_ut/3; feasible for
ALL e*=1,2,3,4 (two twos with even t are a forbidden gcd2 triple; odd t is coprime to twos). Thus e*<=3 in these rows.
Suppose Theta*={uv in W:alpha*_uv=3} is nonempty. Every edge dominates all other vertices, since otherwise the (3,a,b)
triangle forces344 (section2's triangle computation), forbidden by the local row test. Hence every vertex is incident to
an edge and then has Theta*-degree>=2 by the same test. Degree4 would make all four alpha-W entries<=2 (section2 excludes
alpha3), against B-test. Nonadjacency in Theta* is transitive: if uv is an edge no third w is nonadjacent to both. Its
complement is thus a union of cliques; degrees2..3 make their sizes2 or3, so on5 vertices the complement is K3+K2 and
Theta*=K(A,B), |A|=3,B={d,e}. Each B-row has three small alpha cross-entries; B-test gives alpha_de=alpha_td=alpha_te=4;
triangles with that4 give alpha=2 on A x B. Gamma_alpha is connected, so ZT gives two starred t-fours. They cannot lie in B
(alpha_tB=4); they cannot lie in A either (each A-row is3311 or3322, e*<=3). Contradiction. So no starred W-three.
Finally if alpha*_ut=3, the t-label3^(A+1)w_t is coprime to all four starred W-labels (powers2 times rho), so t1 plus
standard four-neighbour weights (value>=4),z0 gives>=7>5 via L_z. Thus no starred W-t-three either. We have proved:
**ZW:** in T*=W, both families' W-W and W-t entries are in{1,2,4}; no use of the obsolete full Cor L on unresolved threes.

## 6. Exported interfaces, attribution and limits
Exports (only for the normalised S-setting, not general K7): both omitted-marker bounds G_z/G_t at W in both orientations;
full alpha-row/equality and full Gamma^alpha* VFC bound; alpha has no W-three; ZT, ZTR under their OWN connectedness
hypotheses; ZS with precisely the two branches; ZW only when T*=W. Each proof is contained in this unit; no Unit1/3 premise.
Origins: ZA FG-zf/ZS, ZE2 ZW, ZE3 ZT, ZE4 ZTR, with ecff items5-9 (retained p-factor, explicit pair vectors, odd-t/two gcd)
and RICH c=3 row/centre arguments. All are re-derived, not accepted merely from old Codex or repair-only reviews.
No unchanged failed packet retry. No fullK7/Sun7/novelty/Lean/human claim. Unit3 must separately close BOTH ZS branches and
join the no5 component; this unit does not claim (a2) is empty.
