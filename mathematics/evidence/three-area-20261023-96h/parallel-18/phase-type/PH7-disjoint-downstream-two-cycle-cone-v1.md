# PH7 at 8/9: an exact cone with a vertex-disjoint downstream two-cycle

Actual `/bin/date` observation before this manuscript: **Sun Oct 25 23:38:03 PDT 2026**. Owner MathResearch96h-2, math-1. **WRITTEN AUTHOR CANDIDATE**, not independently reconstructed or parent-adopted. No interpreter, calculator, eval, CAS, solver, arithmetic program, replay, finite checker or scientific launch was used.

This is a new topology relative to the through-middle-cycle family: a cycle avoiding state 4 is now allowed, so disjoint-cycle products are retained. All earlier process findings and the ZERO-credit private-scout quarantine, including the v5 exactness addendum, remain permanent. The original unrestricted point question remains NOT_PROVED/minimum {7,8}.

## 1. Exact scope and the old property that breaks

Take the positive forward chain 1→2→⋯→7, with unit forward entries after positive diagonal scaling. Allow ALL fifteen backward edges whose forward-chain cycle contains state 4. In addition allow the edge 7→6, of weight sigma>=0. The holdings of the raw Metzler matrix G are

    (u,u,u,w,1,1,1),       u>=1, w>0.

Initial weights are on {1,2,3}; the raw exit is state 7. No through-middle feedback entry is dropped or identified with another entry. This is not claimed WLOG for arbitrary PH7 matrices.

The old argument used a cone of polynomials (y+u)^a(y+1)^b with nonnegative monomial expansions. That is NO LONGER the actual feedback cone. For example the actual middle→state-3 feedback generator becomes

    (y+u)^2[(y+1)^3−sigma(y+1)].

Put x=y+1 and delta=u−1. The old high functional [x^3]−delta[x^4]+delta^2[x^5] evaluates on this generator to **−sigma**. For sigma>0 the old separator is therefore invalid. This precise failure was identified before attempting the replacement cone below; no old no-go is merely copied to the new topology.

## 2. Actual common matrix, characteristic and numerator

Let X=y+u and x=y+1. In the R/o/S partition with sizes 3/1/3 set

    A=[−u,1,0; 0,−u,1; 0,0,−u],
    F=[−1,1,0; 0,−1,1; 0,sigma,−1],
    b=e3,        t=e1,
    G=[ A     b      0
        r^T  −w      t^T
        D     f      F ].

All three entries of r, all three entries of f and all nine entries of D are independently nonnegative. These are exactly the fifteen through-middle backward edges. Sigma is the new, additional backward entry.

Direct cofactors give

    a_R=X^3,              v=adj(yI−A)b=(1,X,X^2)^T,
    a_S=x^3−sigma x,      U=t^T adj(yI−F)=(x^2−sigma,x,1),
    t^T adj(yI−F)e3=1.

Eliminating the two principal blocks and clearing their determinants gives the FULL polynomial identity

    P(y)=det(yI−G)
        =(y+w)a_R a_S−a_S r^T v−a_R U f−U D v.       (CHAR)

Clearing denominators makes this valid even at roots of either principal polynomial. The backward cross-block D is present, including every product created by a disjoint cycle.

For Q(y)=y^2+py+q write

    B=p−2u,      C=Q(−u),      Q=X^2+B X+C.

Set the raw initial row beta=K(C,B,1,0,0,0,0), and gamma=e7. A necessary and sufficient condition for beta>=0 is B,C>=0. The same block elimination gives, without a feedback-independence assumption,

    beta adj(yI−G)gamma=KQ(y).                        (NUM)

The desired repeated-pole target uses

    D_z(y)=y[(y+1)^2+z]^2.

Its characteristic equation is P=D_z Q. Comparing the degree-six coefficient first forces

    w=p+1−3u.

Conversely, if this common matrix has P=D_z Q, Q has strictly left-half-plane roots, and B,C>=0, it gives an actual PH7 after the usual POSITIVE normalization, not merely a spectral factorization. For any physical c>0 choose K=D_z(c), put T0=G−cI and h=−T0^(−1)gamma. T0 is Hurwitz Metzler, and every state has a positive forward path to gamma, so h>0. Then

    T=diag(h)^(−1)T0 diag(h),
    alpha=beta diag(h),
    omega=diag(h)^(−1)gamma

obey T1=−omega, alpha1=beta h=K/D_z(c)=1, and the required transfer K/D_z(s+c). This normalization is CONDITIONAL on the coefficient match; none is claimed to exist.

## 3. A replacement six-ray cone, exact for all fifteen feedback entries

Put delta=u−1>=0, x=y+1, P2=p−2 and Q0=Q(−1). Define

    R=(y+w)X^3(x^3−sigma x)−D_z Q.

After the trace tie it has degree at most five. Its actual feedback generators in (CHAR) are

    X^j(x^3−sigma x)            (j=0,1,2),
    X^3(x^2−sigma), X^3 x, X^3,
    X^j(x^2−sigma), X^j x, X^j (j=0,1,2).

Use the following SIX actual generators:

    g5=X^2(x^3−sigma x),
    g4=X(x^3−sigma x),
    g3=x^3−sigma x,
    g2=x^2−sigma,
    g1=x,
    g0=1.

Every other actual generator is a nonnegative combination of these for delta,sigma>=0. Here is the complete nontrivial list; the remaining six generators are g5 through g0 themselves:

    X^3(x^2−sigma)=g5+delta g4+delta^2 g3+delta^3 g2,
    X^3 x=g4+2delta g3+(3delta^2+sigma)g2
                 +(delta^3+3delta sigma)g1+sigma(3delta^2+sigma)g0,
    X^3=g3+3delta g2+(3delta^2+sigma)g1
                 +(delta^3+3delta sigma)g0,
    X(x^2−sigma)=g3+delta g2,
    X^2(x^2−sigma)=g4+delta g3+delta^2 g2,
    Xx=g2+delta g1+sigma g0,
    X^2x=g3+2delta g2+(delta^2+sigma)g1+2delta sigma g0,
    X=g1+delta g0,
    X^2=g2+2delta g1+(delta^2+sigma)g0.             (GEN)

These are written polynomial identities, not sampled coefficient checks. They include zero sigma and zero feedback boundaries. Since the six basis rays themselves correspond to actual independent entries, they prove equality of cones, not just a necessary relaxation.

If R_j=[x^j]R, the unique basis coefficients are

    a5=R5,
    a4=R4−2delta R5,
    a3=R3−delta R4+(delta^2+sigma)R5,
    a2=R2+sigma R4,
    a1=R1+sigma R3+sigma^2 R5,
    a0=R0+sigma R2+sigma^2 R4.                   (CONE)

Indeed subtract the leading terms of g5,g4,g3,g2 successively; the displayed residual coefficients follow. Thus the actual coefficient system is feasible iff all six a_j are nonnegative, with the separate numerator/stability/normalization requirements retained.

## 4. Exact relation to an effective visible parameter

Let O_j be coefficients of the OLD no-sigma residual

    (y+w)X^3 x^3−D_z Q.

They are

    O5=3delta(P2−1)−6delta^2−Q0+P2−2z,
    O4=3delta^2(P2−1)−8delta^3+Q0−2zP2+2z,
    O3=delta^3(P2−1)−3delta^4−2zQ0+2zP2−z^2,
    O2=2zQ0−z^2 P2+z^2,
    O1=z^2(P2−Q0),       O0=z^2 Q0.

Since R=O−sigma(y+w)X^3 x, its three high coefficients are

    R5=O5−sigma,
    R4=O4−sigma(P2−1),
    R3=O3−sigma[3delta(P2−1)−6delta^2].          (HIGH)

For any Z define the OLD three functionals

    L5(Z)=O5(Z),
    L4(Z)=O4(Z)−2delta O5(Z),
    L3(Z)=O3(Z)−delta O4(Z)+delta^2 O5(Z).

Here O_j(Z) means the displayed polynomial with z replaced by Z, holding delta,P2,Q0 fixed. Set

    Z=z+sigma/2.

Substituting (HIGH) into (CONE) yields the exact identities

    a5=L5(Z),
    a4=L4(Z),
    a3=L3(Z)−z sigma−3sigma^2/4.                 (SHIFT)

In particular a5,a4,a3>=0 force L5(Z),L4(Z),L3(Z)>=0. This is the NEW valid separator relation. It compensates for the earlier −sigma failure instead of assuming that failure away.

## 5. The entire new family is impossible for z>=8/9, u>=1

For completeness the required high-coefficient contradiction is written here. It uses no decimal estimates from the separate 4/5 table.

For delta=0, L5,L4>=0 require

    Q0<=P2−2Z,       Q0>=2Z(P2−1).

They imply (1−2Z)P2>=0. But P2=w>0 and Z>=8/9, a contradiction.

For delta>0, w=P2−3delta>0 gives P2>0. Eliminating Q0 from L5,L4>=0, and then from L4,L3>=0, gives

    P2 L >= N,
    P2 A <= H,

where

    L=3delta^2+3delta+1−2Z,
    N=delta(3+9delta+8delta^2)>0,
    A=delta^4+2delta^3+(4Z+1)delta^2+2Z(2Z−1)>0,
    H=2delta^5+4delta^4+(8Z+2)delta^3
          +6Zdelta^2+6Z^2delta+3Z^2.

These eliminations multiply only the positive factors 1+2delta and delta^2+delta+2Z. If L<=0 the first inequality is already impossible. If L>0 the two require Delta=N A−H L<=0. Written expansion gives

    Delta=2delta^7+7delta^6+(12Z+9)delta^5+(2Z+5)delta^4
       +(30Z^2−26Z+1)delta^3+(21Z^2−24Z)delta^2
       +(12Z^3−3Z^2−6Z)delta+3Z^2(2Z−1).

At Z=8/9 this is

    2delta^7+7delta^6+(59/3)delta^5+(61/9)delta^4
       +(43/27)delta^3−(128/27)delta^2
       +(176/243)delta+448/243.

The block (61/9)delta^4−(128/27)delta^2+448/243 is strictly positive: as a quadratic in delta^2 its discriminant is negative, since

    (128/27)^2=49152/2187 <109312/2187
              =4(61/9)(448/243).

Every remaining coefficient is positive for delta>0. Hence Delta(delta;8/9)>0. Moreover

    dDelta/dZ=12delta^5+2delta^4+(60Z−26)delta^3
          +(42Z−24)delta^2+(36Z^2−6Z−6)delta+18Z^2−6Z.

For Z>=8/9 the last four coefficients are respectively at least

    82/3,       40/3,       154/9,       80/9,

all strictly positive. Thus Delta(delta;Z)>0 for every Z>=8/9 and delta>0, contradicting the required Delta<=0.

Together with (SHIFT) this proves: **for every z>=8/9, every u>=1, every sigma>=0, every w>0, and all fifteen nonnegative through-middle feedback entries, the actual characteristic/numerator coefficient system has no solution.** In particular adding the stated downstream two-cycle to the band's natural closure cannot produce an 8/9 witness.

## 6. Lineage, remaining gap and assurance

The no-sigma cone/source lineage is `PH7-band-closure-through-mid-cycles-v1.md`, SHA256 `9a6dad309d82b68e448e7a50ae9d5f143e24ac7ee248885ad3a59d41fde3cdc5`; its Addendum 1 is SHA256 `1248612d563f0eb9032661c5e06a20752abb98457dddb166b10dc30c033a8c1a`. Both bodies were read. The new common-matrix system, replacement six-ray cone and effective-Z comparison are supplied in full above; no old review accepts them automatically.

NOT settled: u<1 for this new sigma topology, other unequal holdings, additional cycles avoiding the middle state, other initial/exit/degree arrangements, and the two unrestricted dominator strata. The positivity proof of (GEN) specifically uses delta>=0; it must not be transferred to delta<0. The original PH7 question at 8/9 is still NOT_PROVED and minimum {7,8}. This is a larger actual-family obstruction, not a topology-unrestricted no-go or a terminal park. No machine/kernel/formal/configured-family/human/novelty acceptance, new GO, source edit, deadline reset or continuous-runtime assertion is made.
