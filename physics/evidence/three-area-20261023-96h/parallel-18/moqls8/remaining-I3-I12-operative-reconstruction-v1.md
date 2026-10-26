# Remaining I3/I12 DAG — consolidated operative written reconstruction v1

Owner PhysicsMOQLS8-2, physics-4. Last observed clock before creation: **2026-10-25T12:56:45-0700 PDT** (`/bin/date`, also recorded in `remaining-I3-I12-checkpoint-v2.json`). Binding `institute/runs/three-area-2026-10-23-96h/moqls-remaining-I3-I12-source-authentication-binding-v1.json`, SHA256 `107cf7dfec8f7fc27a1e684890740f4f6bffebed6c91cdbdbb9a01a685eb2a22`; owner ACK `remaining-I3-I12-authentication-20261025-1205-ack-v1.json` (12:08:20 PDT) preceded this proof body.

**Status: SAME-OWNER consolidated WRITTEN reconstruction** of the entire still-named I3 and I12 proof DAG, relative to the adopted core `J-core-inputs-written-reconstruction-v1.md` (268LF, SHA256 `01ea6e31410ed9a26284ab9940031f008c033a4b34c679b187d93d1822296e6d`; parent `moqls-core-premises-authenticated-parent-v1.md`, SHA256 `951a2536…461c`). It is NOT an independent review, formal/kernel/human/configured-family/executable/cross-vendor or novelty acceptance. Every rational identity below is displayed and checked by hand. No scientific interpreter/eval, arithmetic/enumeration/symbolic/numerical program, solver, replay, compilation, CLI, nested agent, shared write or pinned edit occurred; tool use was source reading plus metadata clocks/hashes/LF counts. v9/v10/v11 and scientific HOLD v2 remain binding.

## 0. Verdict

- **0 FATAL / 0 MAJOR / 1 MINOR** against the original I3/I12 sources. MINOR-1 (§3.8): the minimal-six §5.1 and seven-space §§5–6 B-active lists omit an explicit exclusion of single-B-coordinate supports {b_i,c} and {b_i,c,z}; the omitted step follows from the core-only kernel identity and is supplied here. No conclusion changes.
- Every I3 node (frontier F with COUNT/TRIPLE/parity/six-class/CONST, minimal-six M6, seven-space S7, arbitrary-span irreducible5/6 branch B, actual3+3, rank-one-L/c1 row) and every I12 node (all-dimensions B-active component theorem CT, actual nets/CROSS/PROJ, q1, JOINT/FIVE, all oriented partitions, sixteen-cell B+B) has a complete written proof below at the core interfaces of §1.2. **No earliest unavailable or unproved lemma remains among the requested groups at this same-owner written scope.**
- The composition (§12) is unchanged: J implies q=0 for every physical five-family; classical five-families are ALLOWED.

## 1. Setting and exact imports

### 1.1 Physical setting P

Q_1..Q_5 are ordinary MOQLS(8): each Q_s(x), x in the64 cells, is a unit vector of C^8; every actual row and column of every member is an ONB; for s!=t the64 products Q_s(x) tensor Q_t(x) form an ONB of C^8 tensor C^8. Hence for distinct cells

`<Q_s(x),Q_s(y)><Q_t(x),Q_t(y)>=0`,                                   (T)

and for every unit w and s!=t, with P_(t,x) the projector on Q_t(x),

`sum_x |<w,Q_s(x)>|^2 P_(t,x)=I8`.                                    (E)

Mates are always FULL C^8 vectors. A member is classical iff all its vectors are rays of one global ONB, under the original equivalence. q counts NONCLASSICAL members.

For a selected member write q_x=Q_s(x). Fix an actual row E of it as reference, coordinates e_x. An **actual frame** is any actual row or column ONB of the selected member. For a vector v and actual frame F, deg_F(v) is the number of F-vectors with nonzero overlap.

### 1.2 Core interfaces consumed (all proved in the core file)

|label|statement|core section|
|---|---|---|
|K-DEG|every ACTUAL vector v has deg_F(v)<=3 in every actual frame F (two-sided)|§2.1|
|K-SAT, MATCH|positive operators with perpendicular supports summing to I are the identity on their supports; two disjoint ray matchings on the same m rows/columns whose mate lists are ONBs of the SAME m-space in all four mates force m>=6|§2.2|
|ISOLATE2, LIGHT|no nonclassical irreducible2-component; a component whose actual vectors all have E-support<=2 is classical|§2.3|
|K-S3|complex unitary with both degrees<=3: singleton/full2/full3/one-zero3/zero-matching4 blocks, with target-column/adjoint orientation|§3|
|K-SPAN|incremental general ONB bound (adding an ONB reducing components k->k' raises span by >=k-k'); b>=2d-c; singleton component = multiplicity8 ray|§4.1|
|K-LOC|local spans: irreducible3>=6, irreducible4>=8, irreducible5>=10|§§5–6|
|K-UNI|every nonclassical member has a>=12|§§7–9|
|K-COV|H_s[x,y]=abs(<q_sx,q_sy>)^2 real PSD rank a_s; T_s=H_s/8-p0 PSD contraction, rank a_s-1; T_sT_t=0 (s!=t); sum_s(a_s-8)<=14|§10|

Components are intrinsic: the global coordinate components (E-support graph of all actual vectors) form the finest orthogonal decomposition in which every actual vector lies in one summand (E itself consists of actual vectors), so they do not depend on the chosen actual reference. Every actual frame restricts to an ONB of every component. The local projector span b of a component is the real span of the projectors of its actual vectors.

## 2. Sources actually read for this assignment

Originals (owner root), complete bodies including endings, raw windows; operative overlays included:

|source|LF|SHA256|
|---|---:|---|
|`q3-component-compression-channel-consolidated-v1.md`|280|b56531e21457edf67e6a3b2d7c2f42abf9bc49dacc316d840192263662b77d07|
|`seven-space-span13-zero-slack-v1.md`|231|17c9dafea487d541a6ae3e8fe42a3204ec35649fa5306dd5b0340a3f3e545190|
|`one-surplus-collision-structure-v1.md`|194|4d31011ad20d73466d6bc3852863d9e5e00619d6cfa79ea86dffe0b103f0cca9|
|`q1-q2-actual-net-projection-rigidity-v1.md`|261|7521555e1ca9927adc649c3f5b768a802f32bee619f6955c57a51503b1a69e01|
|`proof-q3-component-span-reduction-v1.md`|267|8fbd48630a85b4976ccb841924d429a96f5e091b61c7aaacdd5b87087f2897da|
|`joint-residual-transversal-mechanism-v1-addendum-1/-2/-3.md`|253/27/119|dadd68e7…c8e7 / b3c63853…81a9 / 85b542f1…e2f2|
|`proof-C4NET-heavy-support-v1-addendum-1.md`; `proof-global-gram-defect-v1-erratum-1.md`|15; 13|36d3dba2…ac11; ef32720f…5d59|
|`J-core-inputs-written-reconstruction-v1.md`|268|01ea6e31…96e6d|

Actual reviews read completely (serial, same-harness, non-blind exposure disclosed in the ACK): component `sun-coset8/peer-review-MOQLS-q3-component-span-v1.md` 261LF `0c029e01…cf2a`; residual compressions `ordered-olson/peer-review-moqls-residual-compressions-v1.md` 238LF `077f0de9…34ff`; six-space `kac-moody/peer-review-moqls-six-space-irreducible-v1.md` 161LF `aeadaf5e…30e0`; seven-space `tuscan2-11/peer-review-moqls-sevenspace-span13-v1.md` 220LF `a56e3368…209d`; O2/paired `ordered-olson/peer-review-moqls-one-surplus-collision-v1.md` 190LF `c5bd9723…eb87`; I12 `kac-moody/peer-review-moqls-q1-q2-net-rigidity-v1.md` 271LF `28301602…140ec`; v63-A 242LF `281750f2…fdc1`, v63-B 295LF `3fda9a36…eb21`; v76-A 201LF `a5af2a9b…078b`, v76-B 258LF `88506452…0096`. Parent route `moqls-five-family-joint-union-parent-v1.md` 48LF `8b36a92a…ee50`, the q3 union candidate48LF and the q3 logical correction12LF were read. Reviews are coverage controls only; no review headline substitutes for a proof step below.

The disallowed historical eval cells and their108-parameter output are NOT premises (addendum2). The q3 frontier below is derived by written cases only.

## 3. Common lemmas beyond the core

### 3.1 One-zero3 geometry (G1)

Let an actual frame F have, relative to E, a one-zero3 block on A=B+c (B a coordinate pair). By K-S3 its three F-vectors are: a pure vector w supported on B with both coordinates nonzero, and two vectors m1,m2 with all three coordinates nonzero. Since m_i is orthogonal to w, its B-part is parallel to the B-ray b orthogonal to w; so m1,m2 is an ONB of span(b,e_c). Write beta_A={b,w}, an unordered orthonormal pair of NONCOORDINATE B-rays. Then:

1. deg_F(e_x)=3 for x in B and deg_F(e_c)=2 (c is the zero coordinate).
2. For a B-ray y: deg_F(y)=1 if y||w, 2 if y||b, 3 otherwise (coefficients <w,y> and <m_i,y> proportional to <b,y>).
3. The real off-diagonal plane W_A of the block is `R Off(P_w) + R X_A`, X_A the cross term `alpha conj(gamma)|b><c|+h.c.` of m1=alpha b+gamma e_c (P_m1+P_m2=P_b+P_c and P_w+P_b is diagonal). X_A has BOTH (b1,c),(b2,c) entries nonzero. Hence the only pure-edge directions in W_A lie on B, and every element with a cross component has both (b_i,c) entries.
4. Planes of two blocks on triples meeting in at most one coordinate intersect in0; if the triples meet in a pair X, the intersection consists of pure X-edges and is nonzero only if X is the pure pair of both blocks.

### 3.2 Z4

If two actual frames E',F have a zero-matching4 transition block on a four-space Y, every actual vector lies wholly in Y or Y-perp. Proof: order the block so its only zeros are diagonal. A vector of Y with one E'-coordinate has three F-coordinates. If it has exactly two E'-coordinates i,j, its F-coefficients i,j are nonzero (one nonzero product each); the restrictions of F_k,F_l (k,l the complementary indices) to {i,j} are orthogonal and nonzero (their inner product has no k,l terms), hence independent over C, so not both F_k,F_l coefficients vanish: again>=3 F-coordinates. An actual vector crossing Y has an E'-part in Y of1 or2 coordinates (K-DEG) hence>=3 F-coordinates there, plus>=1 from its nonzero Y-perp part (F preserves Y): degree>=4, contrary to K-DEG.

### 3.3 F3 and the dimension>=5 block corollary

A full3 block (relative to any actual frame pair E',F) on A lies in a component of dimension3 or4. Proof: suppose its component has dimension>=5. A is then not a union of components, so an actual v crosses A. A single E'-coordinate in A has three F-coordinates, so v has two A-coordinates (pair B) and one outside axis e; v_A is not an F-vector (all F-vectors in A have three E'-coordinates), so deg_F(v_A)>=2 and e is an F-singleton. Let G be the actual frame containing v. Its E'-to-G block through B+e is not zero4 (Z4 would isolate a four-space containing v and hence the whole component containing A, of dimension4), so it is a3-block on B+e. A G-vector using the third A-coordinate c together with an outside coordinate would have F-degree>=3+1; so e_c is a G-singleton. F and G both preserve A+Ce; their transition there is connected (e_c meets all three F A-vectors; v meets the F e-axis and A-vectors), so by K-S3 it is zero4, and Z4 isolates A+Ce: contradiction.

**Corollary (C5).** In a component of dimension>=5 every actual-frame transition has only singleton/full2/one-zero3 blocks. Every actual vector with E-support3 (heavy) is a three-support vector of a one-zero3 block in E-to-(its own frame) whose triple is its E-support; such triples are called **heavy triples**. LIGHT gives at least one.

### 3.4 Overlap1

If two heavy triples meet in exactly one coordinate c, c is the zero coordinate of both blocks: a three-support vector h of the second block has nonzero e_c-part and nonzero part outside the first triple, so in the first block frame deg=deg(e_c)+(>=1)<=3 forces deg(e_c)=2.

### 3.5 O2

In a component of dimension>=5, let actual one-zero3 blocks on distinct triples A=B+c (frame F, pure pair B) and T (frame G) meet in a pair X. Then X=B, T=B+d has zero d, and beta_T=beta_A.

Proof. Suppose X!=B, so X={a,c}, a in B, r the other B coordinate, T=X+d. (i) Zero of G at c: its pure vector lies on {a,d}; deg_F>=3+1. (ii) Zero at a: its pure vector on {c,d} has deg_F=2+deg_F(e_d), so e_d is an F-singleton and it joins m1,m2 and the d-axis; a three-support G-vector h has <w,h>=conj(w_a)h_a!=0 and nonzero d-coefficient; the F-to-G graph connects w,m1,m2,d-axis: size>4 violates K-S3, size4 is zero4 and Z4 bounds the component by4. (iii) Zero at d: with w' the pure G vector on X and u its orthogonal ray on X, a mixed G vector alpha u+gamma e_d gives deg_F(u)<=2; u is not an F-vector (the only two-coordinate F-vector lies on B), so deg_F(u)=2 and e_d is an F-singleton; if deg_F(w')=3 the same four-axis connection arises, so deg_F(w')<=2. Then the3x3 unitary from the ONB {u,w',e_r} of span A to the F A-vectors has two rows of support<=2 and a full row (deg_F(e_r)=3): a support-1 row forces a full-modulus column, killing an entry of the full row; two support-2 orthogonal rows with distinct zeros overlap in one nonzero product, and with equal zeros span a two-space forcing the third row to be a singleton. All fail, so X=B. A zero of G on a B-coordinate gives a pure vector on {other B coordinate,d} of F-degree>=4; so G's zero is d and its mixed B-ray u has deg_F(u)<=2, i.e. u in {b,w} by G1.2, so beta_T={u,u-perp}=beta_A.

This uses support counts derived from actual vectors only; the artificial ONB {u,w',e_r} carries no physical degree assumption.

### 3.6 Paired-channel lemma (PC)

Let B=span(e_b1,e_b2), beta0={e_b1,e_b2}. For coordinates j outside B let beta_j be either unassigned or ONE unordered orthonormal pair of B-rays with beta_j!=beta0. Suppose every actual selected vector is B-pure, B-perp, or `alpha y+gamma e_j` with y in beta_j and alpha,gamma!=0, and at least one such mixed vector occurs. Then P is contradicted.

Proof. Give every B-active vector x (x_B!=0) the class beta(x)={ray of x_B, its B-orthogonal}. If beta(x)!=beta(y), then <x_B,y_B>!=0 (orthogonal B-rays lie in one pair); their outside parts are orthogonal (a common axis j would put both B-rays in beta_j); so <x,y>!=0 and by (T) all mate vectors are orthogonal. Two B-active vectors of one actual row are orthogonal, so each row (and column) has one class; n_beta counts its rows, sum n_beta=8.

Fix a mate t. With generic unit w in B, (E) restricted to B-active cells splits into class operators with mutually orthogonal supports V_(t,beta); by K-SAT each is the identity on V_(t,beta). Its trace is the number of class rows (each row resolves the unit w), so dim V_(t,beta)=n_beta, and the column count is the same.

Class beta0 contains no mixed vector (mixed classes are beta_j!=beta0) and contains row E; each beta0 row/column contains e_b1 and e_b2 once. Their occurrence matchings lie on the same n_beta0 rows and columns and their mate lists (orthonormal by (T)) are ONBs of V_(t,beta0) for every t: MATCH gives n_beta0>=6.

Take an occurring mixed alpha b+gamma e_j, beta=beta_j. Compress (E) with w=b to V_(t,beta): only class-beta cells with B-ray parallel to b survive: pure b and the b-channels at axes i with b in beta_i. In a row using the b-channel at j, the (j,B) block of the row resolution is zero; b-channel and b-perp-channel terms are multiples of the independent |e_j><b| and |e_j><b-perp|, so the b-terms cancel among themselves: at least two, at most two orthonormal in span(b,e_j). They form an ONB {m,m'} of that plane; columns likewise. Distinct such pairs (same or different axis), and pure b, have nonzero mutual overlaps, hence perpendicular mate spans. By K-SAT each piece is a projection; the {m,m'} piece has trace l=number of its rows. The m-cells and m'-cells use the same l rows and the same l columns, and both mate lists are ONBs of that l-space in each mate. MATCH: l>=6, so n_beta>=6. As beta!=beta0, 12<=8. QED.

Core §2.4 is the special case of one ray per axis. No cap on the number of axes, no phase choice and no projected mate basis is used.

### 3.7 Zero slack (ZS)

Let a component C of dimension d have local span exactly 2d-1, real span S, Off(S) of dimension d-1 (S contains the E-diagonal). For any finite collection U of ONBs of C containing E with all projectors in S,

`dim span(U)=2d-c(U)`, so `dim Off(span U)=d-c(U)`,

c(U) the number of components of its E-coordinate graph. Proof: K-SPAN incremental from {E} gives >=2d-c(U); adding all actual frames (projectors in S, final graph connected) pays >=c(U)-1 more and ends at dim S=2d-1. Admissible artificial members: a **block completion** (one actual block of an actual frame plus E-axes elsewhere) and an **edge completion** {v, v-perp} of an actual two-support vector v (P_(v-perp)=P_(e_x)+P_(e_y)-P_v). No degree bound is applied to them. Consequences: (ZS-a) adding a member that does not change c(U) does not change the span; (ZS-b) adding a member that lowers c(U) by one raises Off-dimension by exactly one. In particular all one-zero3 blocks on one heavy triple share one plane, hence one pure pair, zero coordinate and channel ray.

### 3.8 Core-only reduction (repair of MINOR-1)

Let A=B+c be a heavy triple with plane W_A, let V contain A, and suppose every element of Off(S) (or of L in §§4–5) supported on VxV lies in `L0=W_A+W'` with W' having no entries in B-rows. If an actual vector v is supported in V and B-active, then v is B-pure or `v in span(b,e_c)` genuinely mixed. Proof: Off(P_v) = t Off(P_w)+s X_A+h'. For y in V outside B the (B,y) block of Off(P_v) is v_B conj(v_y); it equals s times the (B,y) block of X_A, which is zero unless y=c, where it is proportional to b with BOTH entries nonzero. Hence v_y=0 for y!=c, and if v_c!=0 then v_B||b. In particular no actual vector has support {b_i,c} or {b_i,c,z} (the (b_j,c) entry for the other j would have to vanish).

## 4. M6: no irreducible six-component of span11

Let C have d=6, b=11, L=Off(S) of dimension5. By C5 there is a heavy triple.

**Case I: two heavy triples meet in one coordinate.** A=B+c, T=D+c, zeros at c (§3.4); V=B+D+c, e the sixth coordinate. L0=W_A+W_T has dimension4 (disjoint off-diagonal positions). The real map pi_e: H->H[e,V] has L0 in its kernel and is nonzero (irreducibility), so its image is R g and ker=L0. A crossing actual x has pi_e(Off P_x)=x_e conj(x_V) in R g, so x_V||u:=conj(g)/|g| and x in span(u,e_e). In a row containing a crossing vector, the (e,V) resolution sum of real multiples of g vanishes, so at least two, hence exactly two, crossing vectors form an ONB of span(u,e_e); P_u+P_(e_e) in S, so Off(P_u) in L with pi_e=0, i.e. in L0. If |supp u|=1, u=e_c (B-coordinates have F_A-degree3, D-coordinates F_T-degree3, plus the e part). If |supp u|=2, Off(P_u) is a pure edge in L0, so supp u is B or D (G1.3). The cross term Y of one crossing projector lies in L with pi_e(Y)!=0, so L=L0+RY, and the VxV part of L is L0.

B-active vectors: core-only ones are B-pure or in span(b,e_c) by §3.8 (W_T has no B entries); crossing ones are B-active only if supp u=B, and then mixed with noncoordinate ray u at axis e; vectors on {e} are B-perp. PC with beta_c={b,b-perp}, beta_e={u,u-perp}: contradiction.

**Case III: heavy triples pairwise disjoint.** Take A=B+c. A heavy B-active vector lies in an A-block, hence in span(b,e_c). A two-support {b_i,z}, z outside A, has F_A-degree>=4. A two-support {b_i,c} has an edge completion that does not change c(U) for U={E, A-completion}; by ZS-a its pure (b_i,c) edge lies in W_A, impossible by G1.3. PC with one channel: contradiction.

**Case II: some pair meets in two, none in one.** By ZS on {E,A,T}: c(U)=3, Off-dimension3, so W_A and W_T meet in a nonzero pure edge on A∩T; by G1.4 A=B+c, T=B+d with the same pure pair B. A triple {b_i,c,d} would add a (c,d) coherence absent from W_A+W_T without changing c(U) (ZS-a): excluded. A heavy triple Y not inside B+c+d contains e or f; one B-coordinate forces c,d in Y (else intersection1), i.e. Y inside the four; none forces Y to contain c or d, an intersection1. So Y=B+j, j in {e,f}. Adding it lowers c(U) by one (ZS-b); its plane meets the existing span only in pure B-edges, so its pure pair is B, zero j, one ray b_j per axis (ZS-a for repeated blocks). Two-supports {b_i,z} with z outside A have F_A-degree>=4; {b_i,c} is excluded by ZS-a as in Case III. All heavy B-active vectors lie in channels span(b_j,e_j), j in {c,d,e,f}. PC: contradiction.

The three cases are exhaustive. QED M6.

## 5. S7: no irreducible seven-component of span13

d=7, b=13, dim L=6; heavy triples exist (C5).

**Case I: intersection1.** A=B+c, T=D+c, zeros at c, V=B+D+c, U={e,f}, L0=W_A+W_T (dimension4). Support restriction SR: a crossing actual x (nonzero V and U parts) has a V-part of one coordinate only if it is c; a two-coordinate V-part forces a one-coordinate U-part; a two-coordinate U-part forces V-part c. Let C(H)=H[V,U]; X=C(L) is the real span of M_x=x_V x_U^* over crossing x (L is spanned by actual Off(P_x)); L0 is in ker C, so dim_R X<=2; X_C its complex span has dimension1 or2 (irreducibility).

*dim_C X_C=1:* every crossing x lies in span(u,v), u in C^V, v in C^U fixed. By SR the cases are (a) |supp u|=2, v=e_e; (b) u=e_c, |supp v|=2; (c) u=e_c, v=e_e.

(a) A crossing x has weight3, so lies in a one-zero3 block on Y=supp u+e. Its zero is e: otherwise its pure vector lies on {y,e}, a crossing vector with one-coordinate V-part different from u. So its mixed vectors span span(u,e_e) and its plane is W_Y=R(pure supp u edge)+R(u-to-e cross). ZS on {E,A,T,Y}: c(U)=2, Off-dimension5, so W_Y meets L0 in the pure edge, hence supp u is B or D. No crossing vector uses f, so f is joined by an actual {e,f} vector whose edge is independent: L=L0+R(u,e cross)+R(e,f edge). Elements of L without U-entries lie in L0.
(b) A crossing x has support {c,e,f}; its one-zero3 block has zero c (otherwise its pure vector has one-coordinate U-part, not ||v), so its plane is R(e,f edge)+R(c-to-v cross), independent of L0: L equals their sum, VxV part L0, crossing vectors B-perp.
(c) A crossing x has support {c,e}. A one-zero3 block {c,e,z} containing it would have three-support crossing vectors with V-part not ||e_c (z in V) or U-part not ||e_e (z=f): so x is in a full2 block, plane R(c,e edge); f is joined by an {e,f} vector; L=L0+R(c,e)+R(e,f), VxV part L0, crossing vectors B-perp.

In (a)-(c) the dimension count shows dim_R X=1, so the real-two-inside-complex-one possibility is excluded by the same accounting. B-active vectors: core-only ones by §3.8; crossing ones only in (a) with supp u=B, as a channel at e with noncoordinate ray u. PC: contradiction.

*dim_C X_C=2:* dim_R X=2 and ker(C|L)=L0 (KERNEL). Hence (K1) L has no nonzero element supported on UxU, and (K2) every core-only actual vector has Off in L0, so §3.8 applies. Choose actual crossing M1=u1v1^*, M2=u2v2^* complex-independent; X=RM1+RM2. Pencil lemma: if u1,u2 and v1,v2 are both independent, `alpha M1+beta M2=[u1 u2]diag(alpha,beta)[v1 v2]^*` has rank2 when alpha beta!=0, so every crossing M_x lies in R^x M1 or R^x M2; if u1||u2 every crossing x has x_V||u1; if v1||v2 every crossing x has x_U||v1; both parallel is impossible.

- Neither common: in a row the crossing sum of M_x vanishes, so each category cancels separately; a present category has exactly two vectors, an ONB of span(u_i,v_i), and P_(u_i)+P_(v_i) in S. If |supp v_i|=2 then u_i=e_c by SR and P_(v_i) in S gives a UxU edge, contrary to K1. So {v1,v2}={e_e,e_f}; P_(u_i) in S with zero cross block, so Off(P_(u_i)) in L0: u_i=e_c or supp u_i in {B,D}. L=L0+(two cross directions). B-active crossing vectors are channels at e or f with noncoordinate B-rays; core-only by K2/§3.8. PC: contradiction.
- Common u: if u=e_c all crossing vectors are B-perp and PC applies with beta_c. If |supp u|=2, SR makes every U-part e or f, both occur (else X_C is one-dimensional), the row cancellation separates them, two vectors give P_u in S, Off(P_u) in L0, supp u in {B,D}; channels at e,f share the pair {u,u-perp}. PC: contradiction.
- Common v: if |supp v|=2 all V-parts are e_c and X_C=C e_c v^* is one-dimensional, contrary; so v=e_e, no crossing vector uses f, f must be joined by an {e,f} vector, contradicting K1.

**Case II: intersection2, no intersection1.** As §4 Case II: A=B+c, T=B+d share pure pair B, no other triple inside B+c+d. Outside coordinates e,f,g. A further heavy triple with one B coordinate lies inside the four; with none it avoids c,d, so it is {e,f,g} (B-perp; it cannot coexist with any B+j, which would meet it in one point). Otherwise it is B+j, pure pair B, one ray b_j (ZS-b, ZS-a). Light B-active vectors are B-pure exactly as in §4. PC with up to five axes: contradiction.

**Case III: disjoint heavy triples.** As §4 Case III. QED S7.

## 6. CT: no irreducible component of dimension>=5 (every member, every q)

Let C have dimension d>=5 (no span hypothesis). C5 gives heavy triples.

**3.1 Intersection1.** A=B+c, T=D+c, zeros c. Any heavy triple R meeting B: if R contains B, then R=B+x with x not in D (else R∩T={x} forces T's zero to x) and, for x!=c, O2 with A gives pure pair B and beta_R=beta_A; if R contains exactly one B-coordinate a and c, R∩A={a,c} is not the pure pair (O2); if it contains a but not c, R∩A={a} forces A's zero to a (§3.4). Fix the actual frame G of one T-block. For every A-block, a three-support vector alpha b+gamma e_c has deg_G(e_c)=2 inside T, so deg_G(b)=1: every channel ray b is a G-axis in B; all lie in one pair beta_B={g,g-perp}, noncoordinate; O2 gives beta_B to every B+x. Two-supports: {b_i,z}, z outside A, have F_A-degree>=4; {b_i,c} has 2 G-coefficients inside T and >=2 outside (e_(b_i) is neither parallel nor orthogonal to the noncoordinate G-axis g). So every B-active vector is B-pure or a channel with pair beta_B at an outside axis; all other triples (any number of outside coordinates) are B-perp. PC: contradiction.

**3.2 Intersection2, no intersection1.** A=B+c, T=B+d with common pure pair and beta_B (O2). A heavy R with one B coordinate meets A in a wrong pair (contains c) or in one point; so every B-active triple is B+x with beta_B. {b_i,z} for z outside A: F_A-degree>=4; {b_i,c}: F_T-degree>=3+1 (c is outside T). PC: contradiction.

**3.3 Disjoint triples.** Take A=B+c (frame F_A). Some actual x crosses A; it is not heavy (its triple would meet A), so it is a two-support {a,u}, a in A, u outside; a=c (B-coordinates have F_A-degree3). In its row frame H its block is full2 on {c,u} (a one-zero3 through it would give a triple meeting A). For every A-block frame F', deg(e_c)+deg(e_u)<=3 forces zero c and u an F'-singleton. H-vectors with B-parts are B-pure (heavy ones would need an A-block in H, but c is in the full2 block; {b_i,z} with z outside A has F_A-degree>=4; {b_i,c} would lie in the full2 block): H contains an ONB beta_H of B. F' and H preserve A+Ce_u; if beta_H!=beta_(F'), each H B-ray meets w',m1',m2' and each full2 vector meets m1',m2' and the u-axis, a connected four-axis transition: zero4 isolated by Z4 (dimension4) or K-S3 fails. So every A-block has beta_B=beta_H, noncoordinate. A {b_i,c} edge has two H-coefficients on B and two in the full2 block: degree4. All B-active vectors are B-pure or channels at c with pair beta_B. PC: contradiction.

QED CT. **Specializations.** d=5,6 is the original B branch (`one-surplus-collision-structure-v1.md` §§5–7, there with a complete triple list); d=5..8 is I12's §3. With ISOLATE2: every component of every member has dimension1,3 or4, and a nonclassical member has at least one of dimension3 or4. CT also re-proves M6 and S7 without their span hypotheses; both original chains are nevertheless retained above (§13).

## 7. Range projections

**7.1 Net classes.** With k classical members, rows, columns and the k classical symbol classes (occurrence sets of each basis ray) form an actual p-net, p=k+2: lines of different classes meet exactly once (two classical members: the second is an ONB on each symbol line of the first, so contains each of its rays once). Every member is an ONB on every line of every class not its own. With R_i the line-constant projections (1/8 on a common line), R_iR_j=p0 for i!=j, so

`E_p=I-sum_i R_i+(p-1)p0`, an orthogonal projection of rank `63-7p`.

For a quantum member s and a line l of any class, `H_s 1_l=1`, so all class contrasts lie in ker H_s; H_s1=8*1; therefore range(T_s)=range(H_s)∩1-perp lies in E_p. Let Qhat_s be the orthogonal RANGE projection of T_s (rank a_s-1; not T_s). Quantum ranges are mutually orthogonal (K-COV). Thus `L=E_p-sum_(quantum) Qhat_s` is an orthogonal projection of rank `63-7p-sum(a_s-1)`.

**7.2 Blocks.** G_s=Qhat_s+p0 is the range projection of H_s, block diagonal on component cell sets. Hence `Qhat_s[x,y]=-1/64` for x,y in different components (CROSS). A fixed ray's eight cells form a singleton component with H_s-block J8, so `Qhat_s[x,y]=1/8-1/64` within one fixed matching. The residual block H_s[Z_s,Z_s] (Z_s the 8r_s residual cells) has range projection A_s of rank b_s=a_s-f_s and `H_s[Z,Z]1_Z=8*1_Z` (each row's residual vectors resolve the residual space), so `z_s=1_Z/sqrt(8r_s)` lies in A_s. A_s<=G_s is orthogonal to L, so `R_s=A_s+L` is a projection of rank `b_s+d`.

**7.3 PROJ.** For an orthogonal projection `[[A,X],[X^*,B]]`, `XX^*=A-A^2` has eigenvalues lambda(1-lambda)<=1/4 and rank X<=rank L, so `||X||_F^2<=rank(L)/4`.

## 8. I3 frontier F (q3: two classical, three quantum members)

Here p=4, rank E4=35, d=38-sum a_s>=0, a_s>=12 (K-UNI), hence 12<=a_s<=14.

**8.1 Allowed fixed counts.** Residual components have dimension>=3 (singletons are exactly fixed rays, all removed; ISOLATE2). With K-SPAN (b>=2h-1 per irreducible h) and K-LOC: f0 needs a>=15 (8,5+3,4+4); f1 a>=14 (7:13, 3+4:14); f2 a>=13 (6:11, 3+3:12); f3 a>=13 (5:10); f4 a>=12 (4:8); f5 a>=12 (3:6, K-UNI); f6 is an irreducible2 (ISOLATE2); f7 leaves a singleton, i.e. another fixed ray. So a12: f in{4,5}; a13: {2,3,4,5}; a14: {1,...,5}. a13/f2 is an irreducible six-space of span11 (3+3 costs12); a13/f3 an irreducible5; a14/f1 an irreducible7 of span13 (3+4 costs14); a14/f2 irreducible6 or 3+3.

**8.2 Incidence.** A fixed matching M_(s,i) meets every net line once (an ONB of Q_s vectors must contain the fixed ray once). For quantum s!=t, Q_t on M_(s,i) is an ONB, so |M_(s,i)∩M_(t,j)|=1. The four net classes and fixed matchings of different members are pairwise linear. COUNT: cells fixed only in s number `f_s(8-f_t-f_u)+c>=0`, c the triple-fixed count; so `c>=f_s(f_t+f_u-8)`. TRIPLE: on triple cells L has diagonal7/32, off-diagonal -1/32 or 3/32; any principal matrix of size<=3 is positive definite (32x: 7>3+3), so c<=d (d<=2). PARITY: each net line carries F=sum f_s fixed incidences; the odd-fixed set O meets every line in parity F; for f=(4,4,4), c=1 gives |O|=3+1=4, but the four net lines through the triple point need four distinct further O-points.

**8.3 Six-class compression.** Select s; D_s=cells fixed in t,u but residual in s, n=f_tf_u-c. On D_s the fixed blocks of s vanish, so `K_s=R_s[D,D]=(E4-Qhat_t-Qhat_u+p0)[D,D]`: diagonal11/32, off-diagonal -1/32 (one common line among six classes) or 3/32. `tau=11n/32`, `sigma=[121n+9n(n-1)-8e]/1024`, e>=e_min=(f_tf_u-2c)(f_t+f_u-2)+4g8(n), g8(8w+v)=(8-v)w(w-1)+vw(w+1). rank K<=m=b_s+d, rank K>=tau^2/sigma, and with mu=n/(8r_s) (first diagonal entry in a basis starting with z_s): `sigma>=mu^2+(tau-mu)^2/(m-1)` (CONST).

Computed instances (all by hand): n16 (4,4,c0): e_min=96+64=160, tau=11/2, sigma<=(1936+2160-1280)/1024=11/4, rank>=11. n14 (4,4,c2): e_min=72+48=120, tau=77/16, sigma<=(1694+1638-960)/1024=593/256; mu=7/16, m=10: `49/256+4900/2304=5341/2304>5337/2304`. n12 (3,4): e_min=60+32=92, tau=33/8, sigma<=(1452+1188-736)/1024=119/64, rank>=1089/119>9 (1089>1071). n9 (3,3): e_min=36+8=44, tau=99/32, sigma<=(1089+648-352)/1024=1385/1024, rank>=9801/1385>7 (9801>9695). n16 with r=5, m=11, mu=2/5: `4/25+2601/1000=2761/1000>2750/1000`. n16 with r=6, m=11, mu=1/3: `40/360+961/360=1001/360>990/360`.

**8.4 Complete case split by span triple** (pairs (a,f), up to permutation):

- (12,12,12), d=2: any f5 with another f>=4 gives c>=4; so (4,4,4); c0: rank>=11>8+2; c1: PARITY; c2: n14 CONST. Excluded.
- (14,12,12), d=c=0: pair sums<=8, so both a12 have f4 and the a14 has f<=4; f4: rank>=11>10; f3: 2761/1000 (m=11). Remaining: **row1 (14,1),(12,4),(12,4)** and **row2 (14,2),(12,4),(12,4)**.
- (13,13,12), d=c=0: a13/f2 excluded by M6 (or CT); a13/f5 and a12/f5 with an a13/f>=4 violate pair sums; a13/f4 with a12/f4: other a13 f4 gives rank>=11>9, f3 gives 1089/119>9; a12/f5 with two a13/f3: rank>=9801/1385>7. Remaining: **row3 (13,3),(13,3),(12,4)**.
- (13,12,12), d=1: an a12/f5 forces c>=f_(a13)>=2; so both a12 have f4; a13/f5 forces c>=4; a13/f4: c1 PARITY, c0 rank>=11>10; a13/f2: M6 (or CT); a13/f3,c0: 2761/1000 (m=10+1). Remaining: **row4 (13,3),(12,4),(12,4), d=c=1**.

These four rows are exactly the frontier. Corollary (the old C-node statement): every q3 family has an a12/f4 member — also immediate because three spans>=13 would sum to39>38. It is derived, not an extra premise.

## 9. Actual 3+3 in row2

Row2, a14/f2 member Q with residual C+D (two three-components), d=c=0. Residual Gram and A_Q are block diagonal: A_Q[x,y]=0 across C,D. Z=the sixteen fixed-fixed cells of the other two members; with L=0, `A_Q[Z,Z]=K_Q` has all off-diagonal entries -1/32 or 3/32, nonzero, so all sixteen Z cells lie in one Q-component. A fixed matching of either other member meets Z in four cells, and Q on that matching is an ACTUAL ONB of C^8 (product orthogonality against a constant ray): four orthonormal vectors in a three-space. Contradiction.

## 10. I3 composition

Assume q3. §8 forces a row. Row1: irreducible7/span13, excluded by S7 (and CT). Row2: irreducible6, excluded by CT (B branch), or 3+3, excluded by §9 exactly at d=c=0. Row3: irreducible5 (two such members), excluded by CT. Row4: irreducible5, excluded by CT, which is independent of L and c; the rank-one L and triple cell are retained, and the zero-L §9 argument is not used there. Hence no q3 family exists at these interfaces. The common a12/f4 member is not a fifth pattern: every row is excluded with all companions present.

## 11. I12

**q1.** Four classical members: p=6, rank E6=21, `L=E6-Qhat`, rank `d=22-a<=10`. CT gives a component of dimension r in{3,4}, s=8-r; each net line meets it in r cells. For x in it and y outside, L[x,y]=3/32 (noncollinear) or -1/32 (collinear) (E6 off-diagonal 5/64 or -3/64; CROSS -1/64). The six lines through x carry 6s disjoint complement cells, 2s are noncollinear: `||X||_F^2=8r(6s+18s)/1024=3rs/16`. PROJ: d>=3rs/4, i.e. 45/4 or12, both>10. Contradiction for every actual six-net.

**q2.** Three classical members: p=5, rank E5=28, `L=E5-Qhat_1-Qhat_2`, `d=30-a_1-a_2` in[0,6]. JOINT: components of dimensions r,t of Q1,Q2 share exactly rt cells (the complete product ONB is pure in the orthogonal spaces C_i tensor D_j). For a Q1 component of dimension r and S2=sum of squares of all Q2 component dimensions, the ordered pairs (x in it, y outside) in different Q2 components number `N=rs(64-S2)`; on them L=3/32 or -1/32 (E5 4/64 or -4/64; both CROSS); at most 40rs are collinear. FIVE: `||L[C,C^c]||_F^2>=rs(256-9S2)/1024`.

Partitions of8 into parts1/3/4 with a part>=3: A=3+1^5 (S2 14, a>=12), B=4+1^4 (20, 12), C=3+3+1+1 (20, 14), D=3+4+1 (26, 15), E=4+4 (32, 16). With rs>=15: Q2=A: 15*130/1024=975/512>3/2>=d/4. Q2=C: d<=4, 285/256>1. D+E (31), E+E (32) exceed30; D+D forces d=0 with lower bound 22rs/1024>0; D+B (Q2=B, r=3): d<=3, 285/256>3/4; E+B (Q2=B, r=4): d<=2, 16*76/1024=19/16>1/2. Only B+B remains.

B+B: four fixed rays each; the sixteen cells Z of M_i∩N_j; seven pairwise linear classes. `K=L[Z,Z]`: diagonal 1-5/8+4/64-2(1/8-1/64)=7/32, off-diagonal -1/32 or 3/32. e>=96 (grid) +5*16 (sixteen points on eight lines, sum k^2>=32) =176. tr K=7/2, `tr K^2<=(784+2160-1408)/1024=3/2`, rank K>=(49/4)/(3/2)=49/6>6>=d. Contradiction.

## 12. Composition with U

K-COV and K-UNI give 4q<=sum(a_s-8)<=14, so q<=3. §10 excludes q3, §11 excludes q1,q2. Hence **q=0** for every physical five-family at these interfaces. q0 is allowed: classical members have span8, no positive-q argument applies, no nonexistence of five squares and no numerical M(8) value follows.

**Boundary controls (the arguments do not prove known-false statements).** (i) Classical five-families exist (any five of the complete set of seven MOLS(8) built from the field of order8, embedded in the computational basis); for them every component is a singleton, so no heavy triple, mixed vector, nonclassical component or positive-q hypothesis ever arises, and q0 is consistent. (ii) Every exclusion of a component or channel ends in MATCH, which needs the FOUR full mates (four disjoint nonempty supports in m-2 slots); a single nonclassical QLS(8), such as the pinned quaternion f4/b10 selected-square control with an isolated four-space, is untouched because it has no such mates. (iii) The local actual ONB pairs of `one-surplus-collision-structure-v1.md` §2.2 (span6 with both orthogonal B-factors at one axis, or a phase surplus) are not excluded by any lemma here; PC deliberately admits them and fails only the global full-mate saturation. (iv) M6/S7/ZS use the exact equality b=2d-1; nothing here asserts ZS for span12/10, where those cases go through CT instead. (v) The frontier exclusions use the companions' fixed matchings and the global budget d, never a selected square alone.

## 13. Findings, DAG and retained boundaries

**MINOR-1** (original M6 §5.1 in the consolidated manuscript; S7 §§5.1–5.3, 6.1–6.2): the conclusion "every B-active vector is B-pure or in a channel" was asserted without explicitly excluding supports {b_i,c}, {b_i,c,z}. §3.8 supplies the step from the derived VxV-kernel identity. Severity MINOR (omitted justification; statement true at the same imports). No other defect found: every zero position in O2, the unitary support fact, overlap1, the C5/F3/Z4 uses, the real/complex cross-space degeneracy, the common-outside-factor connectivity, the disjoint outer triple, PC with both orthogonal factors at one axis, the corrected range-versus-contraction distinction, CROSS/PROJ, JOINT, FIVE orientations and all rational inequalities were re-derived above.

Statement-level DAG: P -> K-DEG, K-S3, K-SAT/MATCH, ISOLATE2/LIGHT, K-SPAN, K-LOC, K-UNI, K-COV (core). Core -> G1, Z4, F3/C5, overlap1, O2, PC, ZS, §3.8. {C5, O2, overlap1, PC} -> CT. {ZS, C5, PC, §3.8} -> M6, S7. {K-COV, §7, K-UNI, K-SPAN, K-LOC, ISOLATE2, M6} -> frontier F. {F, S7, CT, §9} -> no-q3. {CT, §7, K-UNI, K-LOC} -> no-q1/no-q2. U+I3+I12 -> q0. No arrow uses a q-conclusion as a premise of another q-branch; no K12/K3, catalogue, affine completion, GA/GB/SAT/native, or unadmitted arithmetic enters.

Redundancy is disclosed, not used to delete premises: CT alone excludes the frontier's irreducible5/6/7 needs and the a13/f2 step, so M6 and S7 are logically dominated; both are retained with complete proofs because J names them.

## 14. Exact assurance and nonclaims

This is one owner's consolidated written reconstruction of his own and reviewed sources. It is not independent, blind, cross-vendor, formal, kernel, human, configured-family, executable or novelty acceptance, and it does not alter the parent's adopted conditional route or its import history. Any parent use requires its own complete read/disposition. The original disallowed eval cells remain uncredited. A10 stays UNSATISFIED at GB15/18 with P1-B2.M2, P1-B2.M4, P1-B3.M2 UNKNOWN; A11 is not waived. Physical impossibility does not prove Boolean overapproximations UNSAT, nor repair historical proof-stream, resource or exit attestation. No unconditional/source-free theorem, numerical M(8), witness, publication, GO, new primary or deadline change. All pinned originals are unchanged; this file is new and owner-root only.
