# First-order Schur test v1 — a concrete noncommuting case requires higher-order reasoning

PhysicsRQLS10. Written structural analysis; no creation clock estimate, scientific executable or enumeration. This is not a phase witness, an actual low-rank M certificate, or a full-target result. Read the noncommuting note with its explicit basis-metric erratum.

## 1. A useful test that closes some noncommuting cases

Fix rho(t)=-t, the first Et-Taoui core, and arbitrary relative character matrix Q'. Put s=i sqrt7. On positions where M is nonzero,

    1 maps to1,
    w²=1+s/4+s²/4,
    w^-2=1-s/4+s²/4.

Thus `M=N+sM1+s²M2` exactly in Z[1/2,s], with s²=-7. The even5×5 block is a unit modulo s; its mixed and odd blocks vanish modulo s. Consequently its Schur complement satisfies

    Schur(M)/s mod s = D1,

where D1 is the odd-to-odd block of M1. Products of the two mixed blocks only enter at order s². Inverting the even block is legitimate in the localization where its determinant, a unit modulo s, is inverted.

Choose representatives r1=1, r2=alpha, r3=1+alpha, r4=1-alpha in GF(9), alpha²=-1. For any real symmetric character matrix Q define a symmetric zero-diagonal4×4 matrix

    A(Q)_ab = [Q_(r_a,r_b)-Q_(r_a,-r_b)
                -Q_(-r_a,r_b)+Q_(-r_a,-r_b)]/2,   a!=b,
    A(Q)_aa=0.

A direct substitution into the odd projection gives

    D1=-(A(Q)+A(Q'))/8  modulo7.                          (L)

For the fixed first Q,

    A(Q)=2*[ 0  0  1  1 ]
             [ 0  0  1 -1 ]
             [ 1  1  0  0 ]
             [ 1 -1  0  0 ].

For example Q_(1,1+alpha)=+1 and Q_(1,-1-alpha)=-1, giving the (1,3) entry2. The (2,4) difference is-2. These are exact finite-field character values, not numerical approximations.

If the right side of (L) has rank at least3 over F7, the actual Schur matrix has rank at least3 over K, and therefore actual M has rank at least8. The written rank8 norm-descent theorem then excludes **all complex unit phases** for that case. This is a valid sufficient analytic test.

## 2. A legitimate noncommuting case where this first-order test is inconclusive

Use labels x+3y for x,y in F3. The representatives above have labels1,3,4,7. Let p, as a row-to-old-label permutation, be

    p=(0,3,5,1,7,2,4,8,6),
    Q'_(i,j)=Q_(p(i),p(j)).

It fixes0, but does not commute with inversion: p(-1)=p(2)=5, whereas -p(1)=-3=6.

The four rho-pairs map as follows:

| pair representative | image of r | image of -r | grid-coordinate difference |
|---|---|---|---|
|1| (0,1) | (2,1) | e_(x=0)-e_(x=2) |
|alpha| (1,0) | (1,1) | e_(y=0)-e_(y=1) |
|1+alpha| (1,2) | (0,2) | e_(x=1)-e_(x=0) |
|1-alpha| (2,2) | (2,0) | e_(y=2)-e_(y=0) |

In the3×3 rook description Q=2Adj-(J-I), the alternating combination defining A(Q') cancels the constant part. For two distinct pairs it equals the dot product of their displayed row/column difference vectors. This gives

    A(Q')=[ 0  0 -1  0 ]
           [ 0  0  0 -1 ]
           [-1  0  0  0 ]
           [ 0 -1  0  0 ].

Therefore

    A(Q)+A(Q') = [0 X; X^T 0],
    X=[1  2]
      [2 -3].

The ordinary integer determinant of X is-7. Over F7 its second row is twice its first and its rank is1, so (L) has rank2, not3. Hence this actual noncommuting p is **not closed by the first-order mod7 rank test**.

This is only a barrier to that argument. The actual M may still be nonsingular, rank8, or have another obstruction; **no claim rank(M)≤7 follows from a singular leading reduction**. In particular this example is not a compatible phase vector, torus point, ONB triple or QLS witness.

## 3. Exact remaining written step

A complete written supersession would need a higher-order Schur argument on the two-dimensional reduced kernel in cases like this, or another proof that every actual rank5–7 noncommuting kernel lacks unit phases. The commuting average and one-dimensional K-norm descent do not supply that missing step. Merely declaring the noncommuting first-order matrix nonsingular would be false for the concrete permutation above.

The prepared5040-core request has not run and is not authorized. Its possible scientific value is precisely to distinguish actual higher-order ranks/forced-coordinate certificates from leading-order artifacts, while keeping any remaining kernels UNKNOWN. This note records a concrete obstruction to overclaiming a first-order written closure, not a request to waive the parent's GO gate.
