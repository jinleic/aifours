# Original q1 four-family: unique nonfixed rays, no C5/C6, and sharp remaining C7/C8 span windows

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.** PhysicsMOQLS8-2. Actual native clock observed before writing: Thu Oct 29 13:52:24 PDT 2026. This packet changes representation from local coordinate pencils to the five actual net lines through repeated occurrences and their global projection-range gluing. Its sole adopted mathematical import is GAP3; every other used assertion is proved here. It does **not** decide the existence of a nonclassical four-family or establish a new numerical M(8).

## 1. Exact original family and results

Let Q,L1,L2,L3 be ANY ordinary four-MOQLS(8): all original rows and columns are ONBs in C^8, and all six same-cell tensor-product families are ONBs. For distinct cells y,z and distinct members M,N,

    <M_y,M_z><N_y,N_z>=0.                                          (1)

Assume L1,L2,L3 are classical in their respective, independently chosen global output ONBs. Unit phases and all complex output bases remain arbitrary. A ray is **fixed** if its component in Q's non-orthogonality graph has dimension one; every other ray is **nonfixed**. A component is intrinsic/irreducible by definition.

**Only imported theorem: GAP3.** Every nonfixed ray in any member of an ordinary four-MOQLS(8) has global cell multiplicity at most three. This is Gate 1 of `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`, SHA256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`. No earlier C4/C5/C6 span bound, f197/f211/f218 verdict, tested-qutrit theorem, catalogue, held route, solver result, or unreviewed candidate is a premise.

We prove the following consequences at the stated q1 interface:

1. Every nonfixed Q-ray occurs at exactly ONE original cell.
2. Every nontrivial Q component has dimension seven or eight. In particular, q1 intrinsic C5 and C6 are impossible, not merely subject to a span bound.
3. If its dimension is seven, its real projector span b lies in **17<=b<=21**. If its dimension is eight, **19<=b<=29**.

A classical Q has no nonfixed component and remains allowed. For a nonclassical Q there is at least one nontrivial component; two such components cannot fit in C^8, so exactly one C7 or C8 component remains. The intervals are necessary conditions, not realizability claims.

## 2. Five actual net classes and the physical star inequality

Label the rays of each classical L_i in its own ONB. Each classical array is Latin along rows and columns. For i!=j, (1) makes an ordered pair of L_i,L_j labels occur at most once, hence exactly once. The row, column and three symbol partitions are therefore five line classes: each line has eight cells, any two lines of different classes meet once, and two lines in the same class are disjoint.

Every Q-symbol line is an actual ONB: two cells on it have equal L_i ray, so their Q rays are orthogonal by (1); there are eight unit vectors. This also holds for ordinary rows and columns. The five lines through any cell share no other cell. Any two distinct cells lie on at most one net line. No affine net or common output unitary is assumed.

Let C be a Q component with complex span W of dimension r. Every actual Q line meets C in an r-ONB of W, different components being orthogonal, and

    sum_{z in C} P_z=8P_W,      P_z=|Q_z><Q_z|.                    (2)

For an actual component cell y with ray u, evaluate each Q-L_i tensor-ONB resolution along (L_i)_y. Off-diagonal mate weights are supported only on Q rays perpendicular to u, are pairwise disjoint across the three mates, and are at most one. Adding the actual row and column stars gives

    A_u := sum_{z in C, Q_z perpendicular to u} P_z
           >=5(P_W-P_u).                                            (STAR)

This is an operator inequality on actual original cells, not a supposed independent frame. It holds for every component dimension and does not use GAP3.

A ray occurring on all eight rows is fixed: its row occurrence is perpendicular to every different ray in that row, and the rows cover all cells. Conversely a fixed singleton ray appears once on each row, hence has multiplicity eight. A ray different from u but overlapping u is therefore nonfixed.

## 3. Net intersections force every nonfixed ray to occur once

Let u be nonfixed, with m occurrences. GAP3 gives m in {1,2,3}. Occurrences of the same ray cannot share a net line, because Q is an ONB on that line. Let y_1,...,y_m be those cells. For a cell z not carrying u, let k(z) be the number of the 5m net lines through these occurrences which contain z. Any z is collinear with a particular y_i in at most one class, so k(z)<=m. Every point on one of those lines, other than the y_i, is Q-orthogonal to u.

For two distinct occurrences y_i,y_j, the five lines through the first and five through the second have 20 intersections in different classes; lines in the same class are disjoint. No intersection is another u occurrence, because distinct occurrences cannot share a line. Counting incidences and pairs gives

    sum_z k(z)=35m,     sum_z binom(k(z),2)=20 binom(m,2).            (3)

If m=2, k is 0,1 or2, so exactly 20 cells have k=2 and 30 have k=1. At least 50 cells are perpendicular to u.

If m=3, write n_j=#{z:k(z)=j}. From (3),

    n_1+2n_2+3n_3=105,    n_2+3n_3=60,
    n_1=-15+3n_3>=0,      n_1+n_2+n_3=45+n_3>=50.

Again at least 50 cells are perpendicular to u. Hence the number L of **mixed** cells z with 0<|<u,Q_z>|^2<1 satisfies

    m=2: L<=12;        m=3: L<=11.                                  (4)

In each net class, the m lines containing u have no mixed cells. Each of the other 8-m lines has at least TWO mixed cells: their squared u-overlaps sum to one, and a single nonzero overlap would have modulus one and be another u occurrence. Thus L>=2(8-m).

We use an exact two-entry-line observation. If a net line has precisely two mixed cells x,z, the line-ONB expansion of u puts u in span(Q_x,Q_z), and Q_x perpendicular Q_z. Therefore Q_z is the UNIQUE in-plane orthogonal partner of Q_x in span(u,Q_x). If x lies on two such net lines, their partner cells are distinct but carry this SAME ray.

For m=2, (4) and the lower bound give L=12, so all six unused lines of each class have exactly two mixed cells. Each mixed x therefore has five distinct same-ray partners, contradicting GAP3. The partner is nonfixed because it overlaps u and differs from it.

For m=3, L is 10 or11. At L=10 every unused line is two-entry, giving the same contradiction. At L=11, each of the five classes has four two-entry lines and one three-entry line. The five three-entry lines contain 15 mixed-cell incidences in total. Some one of the 11 mixed cells lies on at most ONE of them, since otherwise there would be at least 22 incidences. It lies on at least FOUR two-entry lines, producing four occurrences of its same nonfixed partner, again contradicting GAP3.

Both m=2 and m=3 are impossible. Thus **every nonfixed Q-ray occurs exactly once**. This conclusion uses actual five-net intersections, not only the general four-family multiplicity bound.

## 4. A nonfixed ray has at least twenty mixed cells and cross rank at least five

Fix any nonfixed actual ray u, now known to have exactly one cell. In each of the five net classes there are seven lines not containing u; each has at least two mixed cells. Let L=14+s be the number of mixed cells, s>=0. In any class the sum of the excesses (number of mixed cells on a line minus two) is s, so at least 7-s of its seven lines have exactly two mixed cells.

The two-entry lines form a MATCHING on the mixed cells across ALL five classes. Indeed if a mixed cell x lay on two, the two distinct partner cells would carry the same nonfixed ray by Section 3, contrary to its now-proved multiplicity one. Hence, if T is the total number of two-entry lines in all five classes,

    5(7-s)<=T<=L/2=(14+s)/2,
    56<=11s,  so s>=6 and L>=20.                                  (5)

Let u lie in the intrinsic component C with span W of dimension r>=2, and put H=W intersect u-perp. All u-mixed rays lie in C. On H the mixed-cell projected covariance is

    F_u := sum_{z mixed} P_H P_z P_H =8I_H-A_u|_H <=3I_H.          (6)

The component resolution (2) evaluated at u gives sum_{z mixed}|<u,Q_z>|^2=7, because u itself occurs once. Taking traces in (6),

    tr F_u=sum_{z mixed}(1-|<u,Q_z>|^2)=L-7>=13.                  (7)

Let S=span_R{P_z:z in C}, b=dim_R S, and let L_u be the real cross-image defined by

    {P_u Z P_H:Z in S}={u chi*:chi in L_u}.

The complex span Pi=span_C L_u is exactly the complex span of the H-projections of the mixed rays: the cross-image is generated by their nonzero scalar multiples. Thus rank F_u=dim_C Pi=:p<=dim_R L_u. Since F_u<=3I_H, (7) yields

    13<=3p,        p>=5,        dim_R L_u>=5.                       (8)

The kernel of the cross map contains RP_u and the entire real projector span T_u of the u-star, in direct sum. If sigma_u=dim_R T_u,

    b>=1+sigma_u+dim_R L_u.                                        (9)

As p<=r-1, every nontrivial component has **r>=6**. This already excludes all intrinsic dimensions 2 through 5 at this q1 interface without importing a separate no-C4 or LOCAL5 verdict.

## 5. Exact ray capacities in subspaces

The capacities below are derived from STAR for actual component rays. They do not assume that a chosen subspace has its own QLS.

### 5.1 Two- and three-spaces

For a two-space B in W, total projection mass is 16. For each distinct actual Q ray v in B, STAR(v) evaluated at its unique B-orthogonal direction gives at least five units of mass on a cell set disjoint from those of every other tested ray. Thus B contains at most three distinct actual rays. If it contains three, they must contain an orthopair: otherwise the three ray-occurrence cells add at least three units outside the fifteen required target units. The third ray is nonorthogonal to that pair and has multiplicity one. In particular TWO different unordered actual two-ONBs cannot occur in B.

For a three-space D containing N distinct actual Q rays, STAR compressed to D gives trace at least 10 per tested ray. For each cell with nonzero D-projection, the tested rays perpendicular to it lie in a two-plane and number at most three. Since total D-projection mass is 24,

    10N<=3*24=72,  so N<=7.                                       (10)

Suppose N=7. Let d_i be each tested ray's number of orthogonal neighbors among the seven; d_i<=3. The slack in (10) is at most two. Each tested ray occurs at an actual cell of projection weight one, so sum_i(3-d_i)<=2. Since sum_i d_i is even and 21 is odd, the deficit is exactly one: six vertices have degree three and one degree two.

The three neighbors of a degree-three vertex are three rays in a two-plane, so they contain exactly one orthopair. That vertex lies in exactly one orthogonality triangle. A degree-two vertex also lies in at most one triangle, so triangles are disjoint. The six degree-three vertices must be covered by two disjoint triangles, leaving the degree-two vertex outside. Each triangle is an actual three-ONB. Their six vertices need six extra edge endpoints; the seventh vertex supplies at most two, so there must be at least TWO orthogonality edges between the two disjoint ONBs.

A 3-by-3 unitary with no shared basis ray has at most one zero. Two zeros in one row/column would give a singleton; with zeros in different rows/columns, those two rows have only one possible common nonzero position, forcing another zero and then a singleton. The two cross edges are impossible. Thus **a three-space contains at most SIX distinct actual Q rays**.

### 5.2 Four- and five-spaces

For a d-space D containing N distinct actual Q rays, compress STAR for each tested ray and take traces. Each contributes 5(d-1). At a cell with nonzero D-projection, the tested rays perpendicular to it lie in a (d-1)-space. If the latter capacity is c_(d-1), total D-projection mass 8d gives

    5(d-1)N<=8d c_(d-1).                                        (11)

With c_3=6, (11) gives c_4<=floor(8*4*6/15)=12 and then c_5<=floor(8*5*12/20)=24. These are bounds on DISTINCT actual rays; original cells remain separately counted in the mass sum.

## 6. No q1 intrinsic C6; hence only C7/C8 survive

Suppose a component had r=6. For an actual u in it, the five net lines through u meet the component in six-ONBs. Their 25 other component cells are pairwise distinct, all perpendicular to u, and all carry distinct rays by Section 3. They lie in the five-space W intersect u-perp. Section 5 permits at most 24 actual rays in that space. Contradiction.

Section 4 ruled out r<=5, so every nontrivial Q component has r=7 or8. Since two such orthogonal components cannot fit in C^8, a nonclassical Q has exactly one. The remaining Q rays, if r=7, are the one fixed singleton ray. No existence of either remaining case is asserted.

## 7. Lower projector-span bounds for C7 and C8

Let the remaining component have dimension r=7 or8, with b=dim_R S. Fix an actual cell y carrying u. The five net lines through y give five (r-1)-ONBs of H=W intersect u-perp. By Section 3 their rays are pairwise disjoint between different lines, because every ray in this nontrivial component has multiplicity one.

Choose two such star ONBs E,F. A connected component of their transition support of size one would give a common ray, impossible. A component of size two would give two different actual two-ONBs in one plane, also impossible by Section 5. Therefore the complete block partitions are

    r=7, dim H=6:       6  or  3+3;
    r=8, dim H=7:       7  or  4+3.                              (12)

For any pair of ONBs, the dimension of the intersection of their real diagonal algebras equals the number g of connected blocks: a common diagonal operator must have equal eigenvalues along every nonzero transition edge, and one scalar per block is possible. Hence

    dim_R(D_E+D_F)=2 dim(H)-g.                                   (13)

All these projectors lie in T_u, whose dimension is sigma_u. By (8)-(9), b>=1+sigma_u+5.

### 7.1 C7

Suppose b<=16. Then sigma_u<=10. A connected six-block has (13) equal to 11, impossible. The 3+3 case has dimension 10, so sigma_u=10 and T_u=D_E+D_F. Both diagonal algebras are block diagonal for an orthogonal decomposition H=A3 direct-sum B3. Every actual star projector belongs to this block-diagonal space, so rank-one purity puts every actual star ray in A or B.

By Section 5, A contains at most six distinct actual Q rays; by Section 3 they each occur once. The trace of A_u compressed to A is therefore at most six. STAR requires at least 5*3=15. Contradiction. Hence **b(C7)>=17**.

### 7.2 C8

Suppose b<=18. Then sigma_u<=12. A connected seven-block has (13) equal to 13, impossible. The 4+3 case has dimension 12, so sigma_u=12 and all star projectors are block diagonal for A4 direct-sum B3. Every actual star ray lies in one block. The B3 compression again has trace at most six by Sections 3 and 5, but STAR requires 15. Contradiction. Hence **b(C8)>=19**.

No reality, finite ray alphabet, chosen coordinate value or extra projector-span theorem was assumed in either case.

## 8. Self-contained upper spans from the actual five-net

Let G be Q's real 64-by-64 projector Gram matrix, G_xy=tr(P_x P_y). Its rank a is the real dimension of the full Q projector span. It satisfies G1=8*1, and for every net-line indicator h_l, Gh_l=1. Let J=11^T/64.

For each net class j let R_j be the orthogonal projection onto vectors constant on its eight lines. Distinct classes have R_i R_j=J, because their lines meet once. Thus

    E=I-sum_(j=1)^5 R_j+4J

is the orthogonal projection of rank 28 onto the complement of the constant and the five sets of seven line contrasts. G annihilates those contrasts and contains the constant in its range. Let R be the orthogonal projection onto range(G), and put P=R-J. Then P is a projection contained in E, of rank a-1, and

    Z=E-P

is a projection of rank 29-a. In particular **a<=29**. For C8 the component is the whole Q space, so b=a<=29.

Now suppose r=7. The one-dimensional complement is a fixed ray f, whose eight cells form a transversal of every net class. The component's 56 cells and the eight f-cells make G block diagonal; R is block diagonal as well. Let X be the corresponding off-diagonal block of Z. For a C-cell x and f-cell y, the R-block entry is zero, P_xy=-1/64, and the net projections give

    X_xy = 5/64 - (1/8)*1_{x,y share a net line}.

Thus X_xy is -3/64 for a collinear pair and 5/64 otherwise. Each x has five f-cells collinear with it, one on each net line through x, and these five cells are distinct; its other three f-cells are noncollinear. Therefore

    ||X||_F^2=56*[5*(3/64)^2+3*(5/64)^2]=105/64.                 (14)

For the orthogonal projection Z, its diagonal C-block B and cross block X satisfy XX*=B-B^2. Since 0<=B<=I, every singular square of X is at most 1/4; also rank X<=rank Z=29-a. Therefore

    105/64<= (29-a)/4,
    29-a>=105/16,  hence 29-a>=7 and a<=22.                       (15)

The full projector span is the orthogonal direct sum of S on W and the singleton span RP_f, so a=b+1. Hence **b(C7)<=21**. The bound uses the actual range projection R, not the unnormalized Gram G or an independently chosen relaxed projector.

## 9. Exact remaining gap and assurance

If a nonclassical ordinary four-MOQLS(8) with three actual classical members exists, its selected Q has exactly one nontrivial component, and the two remaining possibilities are

    C7 plus one fixed ray:  17<=b<=21;
    C8 with no fixed ray:   19<=b<=29.

These are the COMPLETE dimension/span residuals of this packet, not a proof that any point in either interval exists. Physical complex phases, the other cells' actual Q rays, and all five net-line ONBs must still glue in one object. In particular the original q1 witness-or-nonexistence alternative remains OPEN. The older adopted q1 C6>=13 theorem remains historically correct at its stated cut; this NEW no-C6 argument requires its own full review and does not retroactively change that disposition.

Main's separately dispositioned no-C4, LOCAL5 and q4 results are not mathematical inputs to this proof. This packet proves neither q2/q3, unrestricted four-family existence/classicality, M(8), maximum-three, A10 or A11, and it does not clear novelty or priority. A10 and A11 retain their separately recorded exact-input conditions.

Only exact WRITTEN mathematics and metadata clocks/hashes were used: no selected numerical state, scientific interpreter, solver, heavy/multi-GB run, external model CLI or nested agent. Full new review must reconstruct the net-incidence double count (including multi-intersections), uniqueness/partner matching, covariance rank, 3-space capacity, every star-basis block case, and the actual range-projection upper bound. No independent-review, parent, formal/kernel, human, configured-family, executable, priority or novelty acceptance is claimed. Prior fixed packets and all historical process/cadence findings remain unchanged.
