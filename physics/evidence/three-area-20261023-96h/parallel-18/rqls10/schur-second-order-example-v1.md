# Second-order Schur closure v1 — the concrete noncommuting barrier permutation is nonsingular

PhysicsRQLS10. Written exact calculation, no scientific executable, enumeration, numerical test or creation-clock estimate. This closes the **specific actual permutation** in `schur-first-order-barrier-v1.md`, and its literal first-core automorphism images. It does not close all5040 relative cores or all cyclic orientations.

**CANDIDATE WRITTEN PARTIAL.** No local phase solution exists for the displayed core pair, even with arbitrary complex compatibility phases: its actual9×9 coefficient matrix is nonsingular. The previous note's first-order reduction was correctly inconclusive; the second-order term supplies the missing step.

## 1. Fix the same actual matrix, not a simplified ansatz

Use labels x+3y for GF(9), rho(i)=-i, s=i sqrt7 and

    p=(0,3,5,1,7,2,4,8,6),
    Q'_(i,j)=Q_(p(i),p(j)).

M is the exact fixed-coefficient matrix from the conference-gluing manuscripts. Let P denote the involution matrix of rho, and put H=PM. This H is complex symmetric, since C and C' are symmetric and the first C commutes with rho. P is invertible, so it is enough to prove H nonsingular.

The exact expansion in the ring R=Z[1/2,s], s²=-7, is

    H=N+sH1+s²H2,
    N=J-I-P+Fix(rho).

Let D=diag(Q_(i,-i)) and D'=diag(Q'_(i,-i)). The character entries at a fixed point are zero. Directly removing the two masked positions of each row gives

    H1=(Q'-PQ-D'P+D)/8.                                  (1)

Also H2 has zero entries at t=i or t=-i, and elsewhere

    H2_(i,t)=[1-Q'_(i,t) Q_(-i,t)]/8.                    (2)

This is0 when the signs agree and1/4 when they disagree. Formula (2) follows by noting that the coefficient of s² in w² and w^-2 is1/4.

## 2. The first odd block and its reduced kernel

Let even/odd refer to rho. N has invertible even block of dimension5 and zero odd block. The first odd coefficient is

    (A(Q)+A(Q'))/8,

up to the harmless fixed odd sign between H and M. The previous note computed

    A(Q)+A(Q')=[0 X; X^T 0],
    X=[1  2]
      [2 -3].

Over F7, X has rank1. The odd first-order block therefore has rank2. Its two-dimensional reduced kernel has basis u,v with physical nine-coordinate values

    u=(0,-2, 2, 1, 0, 0,-1, 0, 0),
    v=(0, 0, 0, 0,-2,-1, 0, 1, 2).

In the four pair representatives (1,alpha,1+alpha,1-alpha), these are respectively(-2,1,0,0) and(0,0,-2,1). They really are in the reduced kernel: X and X^T annihilate(-2,1) modulo7.

After eliminating the even block, the second-order form on this reduced kernel is

    B2(a,b)=a^T H2 b - h_a^T (N|even)^-1 h_b,
    h_a=even projection of H1 a,                         (3)

computed modulo7. Mixed first-order/even coupling gives the second term. Since u,v are in the reduced odd kernel, their first-order odd parts are zero modulo7 and do not contribute at this order.

## 3. Reconstruct the even-coupling term directly

For this p, every nonfixed pair of Q' is a rook edge, so D' equals1 on the eight nonfixed coordinates. The fixed first Q has Q_(i,-i)=chi(i). From (1), for an odd a,

    H1 a=(Q'a+Qa+D'a+Da)/8.

All following vectors are in label order0,...,8. Computing the rook row/column sums gives, modulo7,

    h_u=(-2,-2,-2,0,-2,-2,0,-2,-2),
    h_v=( 2, 2, 2,2, 2, 0,2, 0, 2).

A directly checkable pair of even solutions to Nz=h is

    z_u=(0,0,0,-1,0,0,-1,0,0),
    z_v=(0,0,0, 0,0,1, 0,1,0).

For example z_u has total sum-2, so its fixed row is-2, its pair{3,6} equation is-2-(-2)=0, and every other pair equation is-2. This is exactly h_u. Similarly z_v has sum2 and only pair{5,7} sum2, giving h_v. Thus these are the actual inverse-even-block products, not guessed inverses.

Their pairings are

    h_u^T z_u=0,       h_v^T z_v=0,
    h_u^T z_v=h_v^T z_u=-4    modulo7.                    (4)

The equality of the cross terms is also consistent with symmetry of N.

## 4. Reconstruct the direct second-order term

Within u's support the only nonzero cross-pair H2 entries are at(1,6),(2,6) and their transposes, each1/4. Their contributions cancel because u1+u2=0. Hence u^T H2u=0.

Within v's support the only nonzero cross-pair entries are at(4,5),(8,5) and their transposes, each1/4. Again v4+v8=0, so v^T H2v=0.

For the cross term, use rows i=(1,2,3,6) and columns t=(4,8,7,5). The exact sign products `Q'_(i,t)Q_(-i,t)` are

    [ 1  1  1 -1 ]
    [-1  1  1 -1 ]
    [-1 -1 -1 -1 ]
    [ 1  1  1 -1 ].

Weights u on the rows are(-2,2,1,-1); weights v on the columns are(-2,2,1,-1). The weighted sum of this table is6. The constant part of (2) contributes zero because both weight sums are zero. Therefore

    u^T H2 v=-6/8=-3/4.                                  (5)

This gives a second, explicit character-table route to the cross term rather than inferring it from the first-order rank.

Combining (3)–(5), the reduced second-order form on span{u,v} is

    [ 0       13/4 ]
    [13/4       0  ]
       = [0 5;5 0]   in F7.

Its determinant is-25=3 modulo7, nonzero.

## 5. Why this proves actual nonsingularity

The even block is a unit modulo s, so it can be eliminated over K while preserving a well-defined reduction in the localization at s. The odd Schur block has first-order rank2 modulo s. Choose a lifted odd basis separating its rank-two complement and reduced kernel span{u,v}. Eliminate the two nonzero first-order pivots after factoring their nonzero s factors. On the remaining two-dimensional kernel, its next term is exactly the second-order form above: mixed correction from this latter elimination only appears at higher order because the first-order cross blocks vanish modulo s.

Factoring the two remaining nonzero s² factors leaves an invertible reduction, since [0,5;5,0] is nonsingular over F7. Therefore an equivalent scaled matrix has nonzero determinant modulo s. It follows that det H, hence det M, is nonzero in K and C. This is an exact algebraic nonsingularity proof, not a finite numerical sample.

Consequently M delta=0 has no nonzero complex solution for this actual noncommuting p. In particular no independent phase gluing exists. The same conclusion transports under literal first-core automorphisms preserving rho, because they merely permute the local equations and phase coordinates.

## 6. Unchanged broader boundary

This closes the explicit first-order barrier example, not a class-coverage theorem for every other relative permutation. A universal written closure would need the analogous leading/second-order obstruction or another argument for every genuine residual low-rank configuration. Rank8 cases are already excluded universally by the separate common-norm descent; possible rank5–7 cases elsewhere are not declared absent.

The prepared assay and its controls remain unexecuted, with no GO. This note does not authorize execution or alter raw prospective output semantics. All mathematical claims are author-written CANDIDATE pending independent reconstruction and parent check. No new target, witness, formal verification, novelty clearance or unrestricted1-RQLS10 result is claimed.
