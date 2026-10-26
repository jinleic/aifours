# Off-axis all-P remainder: complete leading-rank2 shape reduction v1

PhysicsRQLS10, same primary. Author-written working CANDIDATE, not a complete new orientation closure. Actual working clock observed before creation:2026-10-24T04:41:07-07:00. No scientific executable, arithmetic interpreter, enumeration or solver ran.

The literal first rho=(0,7,8,6,5,4,3,1,2) has pair order(H,J,U,V), first A0_JU=A0_JV=1,A0_UV=2, H isolated. Keep every genuine second Q1=P Q0 P^T and every arbitrary complex D/E. Define L=A0+A1. The four-core A1=-A0 family has a complete separate author-written candidate; its support is not silently promoted while awaiting actual reconstruction. This file classifies the nonzero rank2 reduction needed after that family.

## 1. Exact support logic over F7

All entries of L lie between-2 and4 as integers. Thus an individual entry vanishes modulo7 iff it vanishes exactly. A nonzero triangle gives a nonzero3×3 principal determinant2abc modulo7. Therefore rank_F7 L≤2 forces the actual nonzero-edge support to be triangle-free.

A nonzero symmetric zero-diagonal rank1 matrix over F7 is impossible. A four-vertex triangle-free graph with rank at most2 must be a weighted star, possibly with isolated vertices, or a4-cycle whose2×2 cross block has determinant0 modulo7. A disjoint pair of nonzero edges has rank4; a four-vertex path has determinant equal to the product of its two squared endpoint weights and also has rank4. These observations give the following exhaustive split by H degree.

**Important modulus caution:** a4-cycle's determinant must vanish modulo7, not necessarily as an integer. Here a zero determinant modulo7 may come from a nonzero integer multiple±7 or±14. Such a case cannot be deleted by the old axial small-determinant shortcut or declared actual rank2 over K.

## 2. H degree3: exactly prescribed cancellation of the entire first triangle

Every H-based triangle must disappear, so ALL three B={J,U,V} edges cancel:

    A1_JU=-1, A1_JV=-1, A1_UV=-2.

L is then a star at H, with all three incident second edges nonzero. The actual second-root catalogue admits only two complete-support magnitude possibilities compatible with those cancellations:

- a complete K4 with its unique heavy edge U-V;
- a complete K4 with two heavy edges forming the perfect matching U-V,H-J.

The all-light K4 cannot cancel U-V. Every degree3-H diamond or paw has a missing B edge, so cannot cancel that first edge. Other catalogue shapes do not have degree3 H.

There is a further genuine cycle/tag restriction. The B triangle just specified has negative product. In the one-heavy complete family, a positive three-rook core has positive product on every triangle containing its heavy edge, because its heavy roots have parallel y-components and the third root sees correlated signs. Thus only its negative, one-rook counterpart can occur here; its sole rook-positive pair is one endpoint of U-V, not H or J.

For the two-heavy complete family, the heavy rook-rook edge has positive triangle product with a third vertex. The heavy diagonal-diagonal edge has negative triangle product: in the actual parallel canonical roots its x and y contributions add to2 while a vertical rook has opposite-signed inner products with those two diagonal y-roots. Hence U-V must be the diagonal-diagonal heavy edge and H-J the rook-rook edge. The pair tags are+1 on H,J and-1 on U,V. These tag conclusions come from the actual root catalogue, not an arbitrary signed K4.

No higher-order or phase closure of these degree3-H stars is asserted in this file.

## 3. H degree2: a precise cross-determinant congruence

Let i,j be its two neighbours and k its non-neighbour in B. To avoid the H-i-j triangle one must have

    A1_ij=-(A0)_ij.

Write b_i=A1_Hi,b_j=A1_Hj, both nonzero, and

    c_i=(A0)_ki+A1_ki,
    c_j=(A0)_kj+A1_kj.

Then the whole L is bipartite between{H,k} and{i,j}, with cross block

    [b_i b_j; c_i c_j].

Its rank over F7 is twice the cross rank. Thus the exact necessary-and-sufficient leading-rank2 condition for this genuine second A1 is

    b_i*c_j-b_j*c_i=0 (mod7).                    (1)

Equation(1) includes a zero lower row (a two-leaf star at H) and a partially zero row if it really satisfies the congruence. It is NOT a claim that every signed choice satisfying(1) is a realizable second core. The source A1 still comes from the actual triangle/paw/diamond/K2,2 root catalogue, and its E1/B1/D1 are not frozen by this test.

If the cancelled i-j edge is the first heavy U-V edge, its second value must be-2. If it is one of the two first light edges, its second value must instead be-1. This new light cancellation is precisely why the old first-all-heavy triangle argument does not transfer unchanged.

## 4. H degree1: only an opposite-edge cancellation can survive

Let its unique neighbour be k and let{i,j}=B\{k}. If L_ij were nonzero, the nonzero disjoint edges H-k and i-j would already have a rank4 determinant, or a remaining connection would give a four-vertex path, still rank4. Therefore rank2 requires

    A1_ij=-(A0)_ij.                               (2)

Conversely(2) makes L a star at k, with leaf H and the other two possible leaves i,j, so it has rank2 because H-k remains nonzero. No extra determinant condition is needed.

Only two actual second support classes have degree1 H:

- the signed matching of two unit edges: (2) is possible only when i-j is one of the first LIGHT edges, so k=U orV. Its opposite unit edge must be-1. Both all-rook and all-nonrook matching classes stay in scope.
- a paw with H pendant: its opposite triangle edge may cancel a first light edge via-1 or the first heavy edge via-2. The paw's actual heavy position and cycle signs still constrain what is genuine.

This is broader than the old axial P family; requiring the cancelled edge always be heavy here would silently omit real cases.

## 5. H degree0: same-isolate triangles with any one actual cancellation

The genuine second catalogue permits only a triangle-plus-isolate with H isolated. L is a3×3 zero-diagonal B block. It has rank2 iff at least one B edge cancels and not all three cancel. Thus

    A1_ab=-(A0)_ab for at least one B edge,
    A1≠-A0.

Both axis222 and off-axis211 second triangles, positive and negative cycle classes, remain represented. A second heavy edge can cancel the first heavy edge, while a second light edge can cancel either first light edge. The all-three cancellation is exactly the separate four-core family, not another unhandled rank2 case.

## 6. Consequence, current boundary and next bounded target

Every genuine second input has H degree0,1,2 or3. The alternatives above exhaust rank_F7 L=2 without a scientific enumeration. Every input outside them and the separate L=0 family has leading rank>=3 and is excluded by actual rank>=8/common-norm descent. Within them, only actual rank7 kernels can still matter after the four-core family candidate and the general rank8 theorem; no reduced singularity is a physical phase witness.

The next written work must retain the actual first rank3 B0 and the genuine second mixed blocks. In particular it can attack the same-isolate axis triangles or the degree3-H stars with their exact tags, rather than repeat the already closed symmetry orbit or assume an old rank-one first mixed profile. This is an exhaustive shape reduction, not a completed higher-order closure or a claim that surviving rank2 profiles are realizable on the unit torus. The all-P off-axis orientation and full QLS10 remain UNKNOWN.
