# Off-axis first orientation: the entire zero-leading-block family closes v1

PhysicsRQLS10, same primary. **Complete author-written candidate for the whole A1=-A0 second-core family**, not the whole all-P orientation. Stage observation2026-10-24T04:01:18-07:00; later actual working observation04:24:20-07:00. No scientific program, arithmetic runtime, enumeration, solver, compilation or CLI executed.

## 1. Exact family, all genuine literal cores

Use rho=(0,7,8,6,5,4,3,1,2), H={4,5}, J={3,6}, U={1,7}, V={2,8}, and the rank3 first mixed block from `off-axis-first-blocks-and-scope-v1.md`. The first A0 is the positive triangle with edges J-U=J-V=1,U-V=2 and H isolated.

Suppose a genuine second core has A1=-A0, so the entire first odd coefficient vanishes. The complete actual second-grid catalogue forces it to be a **negative off-axis all-rook triangle**: its triangle has negative cycle product, weights211, isolate H and distinguished light vertex J. No k2/paw/complete support has this shape; the positive all-rook211 triangle has positive cycle product.

The literal second-grid geometry then gives E1=-E0 and O1=-O0. Parallel relative root orientations are fixed by A1=-A0, leaving a simultaneous parallel sign and an independent horizontal H sign. These are the only remaining choices. In the mixed block this is

    B1=-B0*T,
    T=diag(t_H,t_P,t_P,t_P), t_H,t_P independently±1.

For completeness this follows by source-normalizing the off-axis raw matching to horizontal H={(1,1),(2,1)}, column0 pair J={(0,1),(0,2)}, and vertical leaves U={(1,0),(1,2)}, V={(2,0),(2,2)}. Its pair means are the fixed E0 data. The three parallel odd products prescribe their relative endpoint orientations; simultaneous reversal changes all three mixed columns by one sign. Reversing H changes its mixed column independently. Coordinate reflections/interchange in the source change no Q1 and introduce no further physical table. Both mixed parts are nonzero, so the four sign choices give four distinct literal cores.

They are all realized as

    C'_S=P_S*conjugate(C)*P_S,
    S∈{I,S_H,S_P,rho},
    S_H=(4 5), S_P=(3 6)(1 7)(2 8), rho=S_H*S_P.

Here S is an involution; the expression simply means C'_S(i,j)=conjugate(C_(S(i),S(j))). All are literal PC P^T cores because conjugate(C)=C_R for the nonsquare R. This is not a four-element phase ansatz: it exhausts the genuine second-core tables with A1=-A0 while their unknown compatibility phases stay arbitrary.

For each write

    (M_S)_(i,t)=conjugate(C_(t,i))*conjugate(C_(S(t),S(rho(i)))).

Each matrix below has actual rank5, with four-dimensional complex kernel; no rank8 shortcut is used.

## 2. S=I: genuinely complex paired-unit obstruction

The companion `off-axis-conjugate-core-phase-obstruction-v1.md` gives a complete full-unit-torus contradiction for M_I. It retains both reflection characters, derives an irreducible physical real-coordinate quadratic P, and a necessary paired-unit polynomial F. Its exact residue evaluation at5 has P(3)=0 but F(3)=2, disproving P|F; irreducibility then excludes a characteristic-zero common root. No restriction to projective K phases is made. The actual rank is5 by paired-row identity plus the rank5 reduction N.

## 3. S=rho: the transpose partner has a purely odd kernel

Symmetry of C and S*rho=rho*S give, for every S in the family,

    M_(rho*S)=M_S^T.                              (1)

Indeed M_(rho*S)(i,t)=conjugate(C_(t,i))*conjugate(C_(rho*S(t),S(i))), equal to M_S(t,i) after using symmetry. In particular M_rho=M_I^T. Since rows i,rho(i) of M_I coincide, columns t,rho(t) of M_rho coincide. Its right kernel contains the four-dimensional rho-odd subspace with fixed coordinate0 zero. N has rank5, so actual rank M_rho=5 and its whole kernel is exactly that subspace. The required coordinate |delta0|=1 is impossible. This reasoning works independently of the nontrivial torus proof for M_I.

## 4. S=S_H: exact reflection split and the actual low rank

Let g be the literal first x-reflection. It preserves C, commutes with rho,S_H,S_P, and hence M_(S_H) commutes with it. Its fixed/anti spaces have dimensions6 and3. On the fixed space N has rank4; on the anti space N has rank1.

The three parallel row pairs of M_(S_H) coincide: rows3/6,1/7,2/8. Outside the H columns this is the same paired product identity as for M_I. At H columns the cross-products are1 for each of these three parallel pairs, on either endpoint, so the identity remains exact. Thus in the g-fixed output, the J-odd row and the sum of the U/V odd rows vanish, bounding that image dimension by4. Together with N this gives actual fixed-block rank4.

Write the g-odd input as

    delta4=alpha,delta5=-alpha,
    delta1=beta,delta2=-beta,
    delta7=gamma,delta8=-gamma,

all fixed g-coordinates zero. The literal odd row is simply beta+gamma=0; alpha is unconstrained. Thus its rank is1, agreeing with N. The full actual rank is4+1=5. In particular no larger kernel can be omitted by the phase argument that follows.

## 5. S_H: unit phases force an impossible equal-mean-norm condition

Normalize only delta0=1. As before set a=delta3,b=delta6, and c,d,e the g-means on H, the row0 heavy pair and the row2 heavy pair. All |a|=|b|=1; none of c,d,e is assumed unit. The full even raw equations are now

    v(a+b)+2u*c+2v*d+2u*e=0,
    u+v*a+u*b+(u+v)(d+e)=0,
    v+2c+2u*d+2e=0,
    1+u*a+b+2c+d+e=0,                             (2)

where u=(-3+s)/4,v=(-3-s)/4. The g-odd equation is beta+gamma=0. Unit norms of the row0 and row2 physical pairs therefore give

    |d|²+|beta|²=1, |e|²+|gamma|²=1,
    G:=|d|²-|e|²=0.                               (3)

This uses the entire odd freedom rather than assuming delta invariant.

Eliminating(2) gives

    v+(6+u)a+(6+8u)b=0.                           (4)

Let r=6+8u. For explicit rational substitution, all means are determined by

    b=-[v+(6+u)a]/r,
    S=d+e=(2/3)[u+v*a+u*b],
    c=-[1+u*a+b+S]/2,
    d=[-v/2-c-S]/(u-1), e=S-d.                    (5)

The norm values in(4) are1,28,28. Since |a|=|b|=1,

    Re[((-35+9s)/8)*a]=-1/2.

Writing a=x+(z/7)s, x=Re a,z=sqrt7*Im a, this is35x+9z=4. The additional |a|=1 therefore gives

    P_H(x)=1792x²-280x-551=0.                     (6)

Its discriminant is72²*777, and27²<777<28², so P_H is irreducible over Q. After substituting z=(4-35x)/9 and(5), G is a rational polynomial in x with only constant denominators. They are units at13: |r|²=28, |u-1|²=7/2 and2,3,7,9 introduce no factor13. The leading coefficient of P_H is11 modulo13, also a unit. Existence of a physical phase vector would force P_H to divide G over Q.

The following exact residue certificate disproves that divisibility. Work over F13[s]/(s²-6), conjugation s→-s;6 is a nonsquare. At x=-1=12,

    P_H(x)=11x²+6x+8=0 (mod13),
    z=0, a=-1,
    u=9+10s, v=9+3s, r=2s, r^-1=-s.

Substitution into(5) gives

    b=10+7s, S=2+5s, c=11-s,
    d=6+4s, e=9+s.

Their two norm residues are

    |d|²=36-6*16=5,
    |e|²=81-6=10,
    G=5-10=8 (mod13),

nonzero. As in the companion proof, reduction commutes with polynomial division because the constant denominators and leading coefficient are local units. Irreducibility makes every characteristic-zero common root imply P_H|G, contradicted by this residue value. Therefore M_(S_H) has no all-unit vector anywhere in its full complex kernel.

## 6. S=S_P: the other transpose partner forces fixed coordinate0 zero

By(1), M_(S_P)=M_(S_H)^T. It commutes with g. In its g-fixed kernel lie the two independent vectors

    e3-e6,
    (e1-e7)+(e2-e8),

because the corresponding parallel rows of M_(S_H) are identical. They are g-fixed, have coordinate0 zero, and are independent. The transpose's fixed-block rank is4 on its six-dimensional fixed space, by section4, so these two vectors span its entire fixed kernel.

If an arbitrary phase delta lay in ker M_(S_P), averaging over g would keep its actual nonzero coordinate0 and yield a vector in that two-dimensional fixed kernel. Every vector there has coordinate0 zero: contradiction. No unit norm of the other averaged coordinates is needed. Its anti space also has rank1; the entire complex kernel is accounted for, not a restricted real subspace.

## 7. Consequential all-P reduction, and honest remaining scope

The four distinct cores with A1=-A0 are now all excluded for the genuinely new off-axis rho, including their actual rank5/four-dimensional kernels. This closes the entire rank-zero leading odd case, not merely a selected floating seed.

For EVERY other genuine second core, the symmetric zero-diagonal matrix L=A0+A1 is nonzero. Such a matrix cannot have rank1 in characteristic7: a nonzero rank1 symmetric matrix would be a scalar vv^T and its zero diagonal would force all v_i²=0. Thus its rank is at least2. If rank_F7 L>=3, the usual even5 plus odd3 argument gives actual rank M>=8 and excludes all phases. Only rank2 L can remain, with actual rank M>=7; an actual rank>=8 there also closes. Consequently the only remaining possible phase-gluing cores for this orientation have **actual rank7, complex-kernel dimension2 and rank_F7 L=2**. This is a restriction on the full all-P obligation, not a claim that those kernels contain phases or that all such cores have been classified.

All results here remain author-written candidates pending their own actual reconstruction. The all5040-second-core orientation theorem is NOT yet closed. Zero equations are only necessary for a true local conference triple, still less a global100-ray QLS. No exact or numerical executable was run, no novelty/formal/human acceptance is asserted, and unrestricted maximal1-RQLS10 remains UNKNOWN.
