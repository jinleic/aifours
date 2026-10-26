# Rank-two completion — consolidated spectral rigidity and both Gold-support exclusions

Owner InfoBalancedNL242, info-6. Actual precreation clock: `Sun Oct 25 05:22:27 PDT 2026`.

**WRITTEN CANDIDATE, NOT INDEPENDENTLY RECONSTRUCTED.** No scientific eval/interpreter, arithmetic/enumeration program, symbolic program, certificate replay or solver was used for this continuation. Source/metadata tools and written reasoning only. Parent v7 and the global scientific HOLD remain binding. Formal, human, cross-model and novelty acceptance are not claimed.

This is ONE successor consolidation after returning the v37-B Shor review. It integrates the exact full-system interfaces, proves new universal S-side spectral rigidity across the retained L16/L20 cases, and strengthens the116-site Gold residual to a written subclass exclusion. Both explicit Gold S supports are now excluded at the written-candidate level. **Neither entire L16 case, L20 nor universal U2 is excluded.**

## 1. Immutable provenance and exact remaining scope

Retained source chain:

- `rank2-two-spectrum-completion-v1.md`, SHA-256 `2a0d363458746f20e9c226db71c8460869386ebc95381fc6c62e51dca8612f6e`, at the named parent-written boundary in `wave-v19-nl242-completion-parent-v1.md`, SHA-256 `8783a156c3fa4a15f3cb5730d1e28f601e2e977c47b1dcbd856baf63548d7f08`.
- `rank2-half-design-and-gold-barrier-v1.md`, SHA-256 `07bfc5d42ad7d65751f555f82387f090b1f066c76ee68a5882f3dbd90a7d135b`, with its mandatory admission/written-Gold overlay `rank2-half-design-admission-and-written-gold-addendum-v1.md`, SHA-256 `9482f1df4dd79354250b96b9b75a756b895182a2a111022dea1dc3f58b1a5e60`.
- `rank2-four-stream-block-grammar-v1.md`, SHA-256 `3d6a62d03911d9648e4e4cb151fc6bec0b47fc94c2ba01f40e68ee66addd4a15`.
- Immediate consolidated predecessor `rank2-completion-consolidated-v1.md`, SHA-256 `be9eb0e071d0de3f61238cb05ca7351f7f7dd55bae362311a8561490813de366`.

All earlier files remain unchanged. The earlier eval arrays, numerical histograms and finite searches remain unadmitted observations and are NOT proof premises. Existing frozen reviews of earlier packets do not automatically review these new bytes or the new theorems.

The retained parent-supported global pruning is: every genuine normalized rank-two target has E empty and necessary (L,u) among(16,24),(16,32),(20,24). This manuscript imports that frontier, not a classification of all surviving delta supports. Its new proofs below are ordinary written algebra. In particular the stronger116-site exclusion supersedes the predecessor's residual ONLY as a new written candidate; that residual was a true necessary condition, not an error being erased.

## 2. Full unpruned system and exact completion maps

On G=F2^8 let H be unnormalized Walsh, H²=256I. Fix a six-space W and put

    D=1−1_W, chi=1−2D, U=W-perp, q=2e0−1_U.

For ternary delta,beta define phi as the odd representative modulo3 and DEFINE

    b=phi(Hdelta), a=phi(Hbeta),
    E={x in U:b(x)=−q(x)}, P=H(q1_E),
    B=phi(q−b)=q−b−3q1_E, C=Hb, C_R=Ha.

The exact S condition is C+3P=4delta on supp(delta), magnitude12 elsewhere. The exact R condition is C_R=−8beta on W, C_R=4beta off W at beta!=0, |C_R|=12 off W at beta=0, and beta(0)=0. The N convolution is

    beta star beta+delta star delta+chi star delta+1_W=e0 over F3.

It is exactly the integer norm a²+B²=1: Walsh over F3 gives that congruence, and ternary squares make0,1,2 the only possible integer sums. No Boolean lifting relaxation is used.

Set p=Ha/4. R is precisely

    p in {0,±2} on W, p in {±1,±3} off W, p(0)=0.   (1)

Then Hp=64a, beta=phi(p), and phi(Hbeta)=a. With S=2HB, R=2Ha=8p, both signs B+a,B−a are Boolean. Both canonical spectra H(B+a),H(B−a) are2 modulo8, because HB=2+4D modulo8 and Ha=4D modulo8. Their absolute-sum cap is max(|S|,|R|)<=28.

The literal512-bit map is

    F(x,0)=(1−B(x)−a(x))/2,
    F(x,1)=(1+B(x)−a(x))/2.                         (2)

Its weight is256 by p(0)=0, and the entire Walsh sectors are8p and2HB. Conversely the named canonical/balanced foundation recovers this exact system from every normalized target. Both transforms and every coefficient remain present.

Two exact coordinate systems for the missing completion are retained, with proofs included here:

**Half-design.** For an unpruned S-consistent delta put T={B=0}, n=|T|, H_v={x:v dot x=1}, M_v=|T intersect H_v|. Expanding HB=2+4D modulo8 gives n even, XOR(T)=0, and second moments of T equal the quadratic coefficients d_ij of D modulo2. A completion is exactly V subset T with

    |V|=n/2,
    XOR(V)_i=M_(e_i)/2+D(e_i) mod2,
    ||V intersect H_v|−M_v/2|<=3 for ALL v.          (3)

Indeed a=1−2*1_V on T gives Ha(v)=4[|V intersect H_v|−M_v/2]; the XOR condition sets its quadratic parity to D, and the slabs give(1). Conversely every actual a has exactly that form. The integer norm follows from complementary supports, hence N. All quantities are integral since XOR(T)=0. The full B lift retains E and3P.

**Four streams.** Choose G=C0 direct-sum U. For each actual T intersection with c+U choose a_c=±1 there and0 at its missing sites, then d_r(c)=sum_u (−1)^(r dot u)a_c(u). The exact inverse local condition is that the four-point inverse is0 at the actual missing sites and±1 at the occupied sites. Splitting characters gives H8a(y,r)=H6d_r(y). Therefore full completion is iff

    H6d_0 in {0,±8}, H6d_0(0)=0;
    H6d_r in {±4,±12} for every r!=0.               (4)

No independent choice of stream spectra is licensed. Locally occupancy0,1,2,3,4 gives respectively all0; four units; two zeros/two magnitudes2; one magnitude3/three units; or one magnitude4 versus four magnitudes2. The actual sites and signs are fixed by the inverse local test. It is not a magnitude-only relaxation.

## 3. NEW universal S spectral rigidity on ALL retained L16/L20 supports

Assume E empty, as forced for every full surviving target. Put A=supp(delta), |A|=L in{16,20}, h=Hdelta and b=phi(h). S now says

    C=Hb=4delta on A, |C|=12 off A.                 (5)

Consequently

    m=sum b²=144−L/2,
    sum h²=256L,
    sum h*b=4L.                                    (6)

These are exact inner-product/Parseval identities on the shared arrays, not independently chosen scalar profiles.

### 3.1 The support XOR is zero

From C²=144−128*1_A and H(C²)=256(b star b),

    H1_A=288e0−2(b star b).                         (7)

At a nonzero shift the convolution b star b is even, since its summands pair under x -> x+shift. Thus H1_A is divisible by4 there; it is L, also divisible by4, at0. Hence all first moments of A are even and XOR(A)=0. Therefore h has one constant residue modulo4; as L is even, that residue is0 or2.

### 3.2 The residue2 alternative is impossible below L32

For every integer t=2 modulo4,

    t²−8t*phi(t) >=36−16phi(t)².                    (8)

If phi(t)=0, |t|>=6. If the sign of t agrees with phi(t), the smallest possible |t| is10 and t²−8|t|>=20. With opposite sign, |t|>=2 and t²+8|t|>=20. These are exactly the zero/nonzero right-hand values36 and20.

If h were always2 modulo4, summing(8) and using(6) would give

    224L >=36*256−16(144−L/2)=6912+8L,

hence L>=32. Both retained L values are smaller. Therefore

    Hdelta is pointwise divisible by4.              (9)

This is universal for the surviving L16/L20 class, not an assumption that the defects form a Gold graph.

### 3.3 An exact positive dual identity

For a multiple of4 with |t|<=20 define

    F(t)=t²+4t*phi(t)−32phi(t)².

Its values at absolute magnitudes0,4,8,12,16,20 are respectively0,0,0,144,288,288. All are nonnegative. By(6),

    sum F(h)=288(L−16).                             (10)

For L16 this sum is0. Therefore **every** such S-consistent delta has

    Hdelta in {0,±4,±8},
    #{|Hdelta|=4}=96,
    #{|Hdelta|=8}=40,
    #{Hdelta=0}=120.                                (11)

The counts follow from m136 and Parseval once the full alphabet is proved; they are not computational enumerations. More strongly, on that alphabet phi(h)=(48h−h³)/128. Applying H gives C=96delta−2delta star delta star delta. Thus ALL surviving L16 S data satisfy the full signed-triple identity

    delta star delta star delta=46delta on A,
    |delta star delta star delta|=6 off A.           (12)

Conversely(11)'s alphabet and(12), with the actual E-empty q/b relation retained, give(5). This is an exact common-coordinate signed-set reformulation, not a Parseval-only test.

For L20 let n_j=#{|h|=j}. Equation(10) gives the exact exceptional-magnitude budget

    n_12+2n_16+2n_20=8.                             (13)

In particular at most four coefficients have magnitude16 or20. Equations(9),(13) remain necessary, not a construction or exclusion. Nothing promotes these spectral constraints to an R completion.

## 4. A written Gold construction and its two column profiles

Let V=F16=F2[alpha]/(alpha^4+alpha+1). The graph A0={(t,t³)} in V x V has16 points. On the six-dimensional exterior square define mu(u wedge v)=uv²+u²v. It is never0 on a nonzero decomposable bivector. The Pluecker quadratic z_01z_23+z_02z_13+z_03z_12 vanishes exactly on decomposables. Hence every nonzero vector of K=ker(mu) has Pluecker value1. A quadratic polynomial cannot be1 at all seven nonzero vectors of a three-space (its total parity there is0), so dim K<=2. Rank-nullity gives dim K>=2, hence mu is onto and dim K=2.

For q0(t)=t0t1 let lambda be its polar functional. The bivector kappa=e0 wedge e1+e0 wedge e2+e0 wedge e3+e1 wedge e2 is in K: its four images are alpha+alpha²,1+alpha+alpha²,alpha²,1+alpha², whose sum is0. But lambda(kappa)=1. Therefore lambda|K is nonzero.

Define delta(t,t³)=−(−1)^q0(t), zero elsewhere. Each Hdelta slice is the transform of q0(t)+L(t³), whose nonzero polar lambda+L composed with mu has rank2 or4. Its Walsh values are0,±8 or±4. Thus C=96delta−2delta³_convolution as above.

At a graph point the signed triple convolution is46delta, from repeated triples; an all-distinct triple would give a nonzero decomposable member of K. Off the graph, write c=y+s³!=0. Triples are parameterized by s+u,s+v,s+u+v; each plane with mu(u wedge v)=c contributes six ordered bases, with sign delta(s,s³)(−1)^lambda(u wedge v). The four-element fiber mu^{-1}(c) has one or three decomposable members, because Pluecker restricted to K is anisotropic. Its full lambda character sum is0, so the sum over those one/three members is±1. The triple convolution off the graph is±6. This proves(5) in writing.

Its support has affine rank8: an affine relation ell(t)+L(t³)+c=0 has c=0; polarization gives L composed with mu=0, so L=0 and then ell=0. Parseval gives wt(b)=136.

Write the b-domain as (a,L) in V* x V*. For the first normal form U={0,4,8,12} in the first factor, b|U=(1,0,0,0), directly from the transform of −(−1)^(t0t1). Thus E empty, alpha1, wt(B)=138 and |T|=118. For the character modulation (−1)^t2 with U'={0,1,2,3}, b|U'=0, so E empty, alpha0, wt(B)=140 and |T|=116.

There are six rank4 and ten rank2 slices: if N4 is the former count then16N4+4(16−N4)=136, giving N4=6. Their six rank4 labels M affinely span V*: the indicator is the Pfaffian of lambda+L composed with mu, a degree-at-most2 Boolean function of weight6. If its support lay in an affine hyperplane, the function would factor the hyperplane indicator times an affine three-variable function, having weight0,4 or8 instead. This is impossible.

Every M column of T is empty. Each rank2 slice has a four-point affine Walsh support P_L, so before q correction its zero support is the size12 complement of P_L. These complements have XOR0. The first q correction toggles the four U sites in column L=0, changing its size12 to10 and preserving XOR0. The second correction removes four U' sites in its column L=0, changing size12 to8 and again preserving XOR0. Therefore the exact written column data are

    first Gold: six empty, nine size12/XOR0, one size10/XOR0;
    second Gold: six empty, nine size12/XOR0, one size8/XOR0,  (14)

with the six empty labels full affine rank4. No earlier computed histogram is used.

## 5. Common four-by-four slice lemmas

For a ternary sign completion A(a,L) supported exactly on T put

    f_t(L)=sum_a (−1)^(t dot a)A(a,L).

Then H8A(t,s)=H4_L f_t(s)=4p_t(s), and H4 p_t=4f_t. The four t in X=ann(U) are W rows; the other twelve are outer rows. Every f_t(L) is even because every column in(14) has even cardinality.

### 5.1 Positive low-row count is at least four

For an outer row define beta_t=phi(p_t), supported at c_t=#{s:|p_t(s)|=1}. At every empty column L in M,

    H4 beta_t(L)=0 modulo3.                         (15)

A one-point beta has transform±1 everywhere. A two-point beta has zeros on only one affine hyperplane. A three-point beta is divisible by3 only when its three signed characters agree, at an affine two-plane of four points. None can vanish on the six full-affine-rank labels M. Hence c_t=0 or c_t>=4.

For c_t=4, affine rank3 support has a transform-zero set contained in an affine hyperplane: gauge the four signs/points to1+chi1+chi2+chi3 and its zeros have even parity in those three coordinates. It cannot contain M. An affine-plane support with sign product−1 has transform magnitude2 and no zeros. Thus the only possibility is a character-signed affine two-plane, whose transform is supported on a four-site affine plane K_t disjoint from M. This is a necessary exact structure, not a sufficient completion.

### 5.2 All3 rows and column capacity

If c_t=0, write p_t=3epsilon. Since f is even and3H4epsilon=4f, H4epsilon is divisible by8. Parseval forces either one coefficient±16 or four coefficients±8. Thus f_t is either one spike±12 or four coefficients±6. In the latter case its four support labels are an affine two-plane: the inverse signed four-point support must have transform magnitude2 everywhere, impossible for four affine-independent points.

For a column S_L of XOR0,

    f_t(L)=sum_a A(a,L) modulo4 for EVERY t.          (16)

Its change from t=0 is−2 times a signed halfspace count whose parity is t dot XOR(S_L)=0. Also sum_t f_t(L)²=16|S_L|.

A spike12 uses a size12 column; different spikes use different columns since2*144>192. A spike column has no6 by(16) and no8 because144+64>192. In any other column containing6 all16 entries are2 modulo4, so the minimum squared total is64. Each6 consumes32 above that minimum. The maximum counts of6 are4 for size12,3 for size10,2 for size8.

### 5.3 Actual zero lower bound

For the116 argument we need z>=8, with no enumeration. Since Hp and HD are divisible by64, the integer function(p−D)/2 has Walsh transform divisible by32. An integer function on n bits with Walsh transform divisible by2^j has parity degree at most n−j: Fourier inversion makes every coordinate face of dimension n−j+1 have even sum. Thus the next bit has degree at most3.

On W, the nonempty zero indicator is1+(p−D)/2 modulo2, a degree-at-most3 Boolean function on six bits. A nonzero degree-d function on n bits has weight at least2^(n−d), by splitting on one coordinate and induction. Therefore z>=8. The normalization p(0)=0 supplies nonemptiness.

## 6. Structural118-site exclusion — retained written proof

**E118.** No full R sign completion exists for the first column profile of(14), with six empty full-affine-rank labels, the rank-two row alphabets and an actual W zero.

The support size is118, so sum p²=16*118=1888. The R alphabet gives sum p²=1984−4(z+2c), with c=sum c_t. Therefore z+2c=24. Since z>=1, c<=11. Each positive c_t costs at least4, so at least TEN of twelve outer rows are all3.

Let s be spike rows and k four-coefficient6 rows among them. Their s columns cannot contain6. The others require4k sixes, while the remaining nine−s normal columns and the size10 exception supply at most4(9−s)+3. Thus4(s+k)<=39 and s+k<=9, contradiction.

This excludes the entire displayed first Gold S support and every support satisfying these exact structural hypotheses. It does not classify all L16/alpha1 supports.

## 7. NEW structural116-site exclusion

**E116.** No full R sign completion exists for the second column profile of(14), with six empty full-affine-rank labels and the rank-two row alphabets/actual zero.

### 7.1 Forced residual before the final contradiction

Now sum p²=16*116 gives z+2c=32. The zero bound z>=8 gives c<=12. Hence at least nine outer rows are all3. The column capacity with one size8 exception gives4(s+k)<=38, so at most nine are all3. Therefore exactly nine are all3, exactly three other rows have c_t=4, and

    z=8, c=12.                                     (17)

Let s of the nine all3 rows be spikes and k be four-coefficient6 rows, so s+k=9. The s spikes occupy distinct size12 columns. The remaining k normal columns can each supply at most4 sixes; the exception supplies at most2. The k all3 planar rows ALREADY require4k sixes.

If one remaining normal column had residue0 modulo4, it supplied0 sixes and the total capacity would fall to4k−2, impossible. If it had a coefficient10, then, by its192 energy and common residue2, its six count would be1 rather than4; total capacity would be at most4k−1, also impossible. Thus EVERY nonspike normal column has residue2, exactly four coefficients6 and twelve coefficients2. In particular no column anywhere contains10: spike columns have residue0, nonspike columns have no10, and the exception has size8.

Write q for the total number of sixes in the three low rows, and w for the number in the four W rows. The all3 planar rows supply exactly4k; normal columns supply exactly4k. The size8 exception either has residue0 and no6, or residue2 and exactly two6. Consequently

    q+w=0 OR q+w=2,                                 (18)

according to its residue. No W-row classification is assumed; only w>=0 is needed.

### 7.2 The three low rows have only four possible magnitude patterns

For each c_t=4 row, beta_t is the character-signed affine plane from §5.1. Its transform is±4 on a four-site plane K_t and0 elsewhere. Since H p_t=4f_t,

    f_t modulo3 = H beta_t modulo3.

Hence inside K_t the even f magnitudes can only be2,4,8,10; outside K_t nonzero f values can only have magnitude6. A magnitude12 is impossible because this row's squared norm is

    sum_L f_t(L)²=144−8c_t=112.

Let q_t count its outside sixes. The four inside squares are at least16, so q_t<=2. Subtracting that minimum, the available per-site excesses are0,12,60,96 for magnitudes2,4,8,10. The exact possibilities are:

    q_t=0: inside magnitudes(10,2,2,2) OR(8,4,4,4);
    q_t=1: inside magnitudes(8,2,2,2);
    q_t=2: inside magnitudes(4,4,2,2).                (19)

This follows from sum_inside f²=112−36q_t: respectively the excess is96,60,24. It is a written four-square calculation, not a program or sign enumeration. Signs, planes and actual column supports remain coupled.

### 7.3 Both exceptional-column residues are impossible

If the size8 exception has residue2, all its entries have magnitude2 or6. Nonspike normal columns also have only2 or6. Spike columns have a12 and cannot contain8; no column contains10. Thus NO8 or10 exists anywhere. By(19), each of the three low rows must have q_t>=1, giving q>=3. This contradicts q+w=2 in(18).

If the exception has residue0, (18) gives q=w=0. Every low row is the q_t=0 case of(19). No10 exists, so each has the pattern(8,4,4,4). Its8 cannot lie in a nonspike residue2 column or a spike column, so all three distinct low rows must place their8 in the one exceptional column. But its full squared norm is16*8=128, whereas three such entries already contribute3*64=192. Contradiction.

Both cases fail. This proves E116 in writing, without requiring the earlier special radical-direction incidence argument or a computation.

**Corollary:** the explicit second Gold S construction also has no complete S/R/N solution. The stronger structural theorem applies to ANY support meeting the exact six-empty/nine12/one8 and XOR/full-affine-rank hypotheses. This is not a classification of all L16/alpha0 supports.

## 8. Current frontier and ONE next attack

| Necessary case | Written result now available | Exact remaining universal gap |
|---|---|---|
| (16,24) | E118 excludes the first explicit Gold S support and the full stated118-site slice class. Universal S rigidity(9),(11),(12) applies to EVERY surviving L16 delta. | No theorem places every such signed16-point S support into the excluded slicing class; other supports and U placements remain. |
| (16,32) | E116 excludes the second explicit Gold S support and the full stated116-site slice class. The predecessor's structured residual is now contradicted, not merely recounted. | No classification/covers-all theorem for all L16/alpha0 supports. |
| (20,24) | Every S-consistent surviving delta has Hdelta divisible by4 and the exact exceptional budget(13). The original half-design/four-stream iff remains intact. | No actual S construction or universal S exclusion, and no corresponding global R noncompletion. |
| U2 | Exact original ternary, half-design and block formulations all retain both Boolean transforms, balance and every512 coefficient. | No contradiction covering EVERY S-consistent delta and no full witness. |

The one consolidated next attack is now an **intrinsic signed-set classification**, not another selected Gold profile: for L16 classify all signed16-point full-affine-rank arrays with the five-level Walsh alphabet(11) and exact triple-convolution(12), retaining the actual four-point q restriction. Prove they admit one of the excluded slice structures, or exhibit and analyze a genuine outside class while keeping the coupled R completion. L20 must retain its sparse exceptional Fourier sites and the same full completion interface. A count-compatible signed spectrum is not an actual Boolean pair.

All three entire cases, the rank-two residue type, seven entire types and unrestricted balanced NL242 remain unresolved. No new scientific execution, executable verification, proof-assistant check, independent-model review, novelty clearance, publication, deadline reset or round closeout accompanies this manuscript. New written results require a separately frozen reconstruction; prior reviews do not transfer automatically.
