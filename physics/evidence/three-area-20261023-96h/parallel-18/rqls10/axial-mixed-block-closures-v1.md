# Axial mixed-block closures v1

PhysicsRQLS10; author-written candidate, not independently reconstructed. Last clock observed before this working file: **2026-10-23T16:44:56-07:00**; no exact creation clock inferred. Same first C, rho_ax=(0,2,1,6,7,8,3,4,5), all literal second PC P^T and arbitrary independent complex D/E. Written exact algebra only; no program, control, compilation or scientific execution. This supplies family-wide closures in the T0/T1/P split, not yet a complete axial packet.

## 1. Pair-coordinate algebra, including the nonsymmetric terms

Use s=i sqrt7, K=Q(s), and the local ring R localized at the prime(s), with2 invertible and7=-s². Write the paired even basis as the fixed coordinate0 followed by four pair means, and odd basis as four pair differences. Their metrics are G_E=diag(1,2,2,2,2) and G_O=2I. First pair order is(H,b,d,e)=(horizontal,V0,V1,V2), with b the first distinguished vertical axis. The two Q matrices are real symmetric, Q_j 1=0, Q_j²=9I-J. Define their coordinate blocks

    Q_j=[E_j B_j; C_j O_j],   C_j=B_j^T G_E/2,
    O_j=-D_j+A_j,             D_j=diag(Q_j(r_a,rho r_a)).

In a pair-to-pair4×4 subblock C_j=B_j^T. The first core has

    D0=I,  O0=-I+A0,
    (A0)_ab=2 for distinct a,b in{b,d,e}, zero otherwise;
    B0=b0 e_H^T,  b0=(0;0,0,2,-2);
    (E0)_pair=I-2(e_H e_b^T+e_b e_H^T).

All references to B0 in this file mean this Q0 mixed block, not the Schur coefficient called B^(1) below.

The exact gluing matrix is

    M_(i,t)=conjugate(C_(t,i))*C'_(t,rho i)
           =N+sM1+s²M2,
    N=J-I-P_rho+Fix(rho),
    M1=(P_rho Q1-Q0-D1+D0 P_rho)/8,
    M2=(N-Q0 o(P_rho Q1))/8.

Here o denotes entrywise product; rows of P_rho Q1 are permuted. In the even/odd split, let A=M_EE, B=M_EO, C=M_OE and D=M_OO. Then

    A=A^(0)+s A^(1)+s² A^(2),
    B=s B^(1)+s² B^(2),    B^(1)=(B1-B0)/8,
    C=s C^(1)+s² C^(2),    C^(1)=-(B1+B0)^T G_E/16,
    D=s D^(1)+s² D^(2),    D^(1)=-(A0+A1)/8.

The leading even block is invertible modulo(s). For h=(h0;h1,...,h4),

    (A^(0)^-1 h)_0=(sum(hpair)-3h0)/4,
    (A^(0)^-1 h)_a=(sum(hpair)+h0-4h_a)/8.

In particular A^(0)^-1 e0=(-3/4;1/8,1/8,1/8,1/8). If h is any Qj mixed column or linear combination thereof, regularity gives h0+2sum(hpair)=0. Therefore

    e0^T A^(0)^-1 h = -7h0/8,
    h^T G_E A^(0)^-1 e0 = -7h0/8,                    (1)
    h^T G_E A^(0)^-1 h = -h^T G_E h/2-7h0²/16.    (2)

The mod(s) Schur matrix is obtained from

    S=D-C A^-1 B
      =s D^(1)+s²[D^(2)+(B1+B0)^T G_E A^(0)^-1(B1-B0)/128]+O(s³).

It is generally **not symmetric**. All row/column mixed terms must remain.

For later calculations, its direct odd curvature is

    D^(2)=[E0 o O1-O0 o E1+B0 o C1-C0 o B1]/16.    (3)

The pair-to-pair E/O/B/C blocks are meant on the right of(3). The other direct curvature blocks are

    B^(2)_pair=[O0 o C1-E0 o B1-B0 o E1+C0 o O1]/16,
    C^(2)_pair=[E0 o C1-O0 o B1+B0 o O1-C0 o E1]/16. (4)

Fixed-row/column entries are evaluated separately below; their factors differ because the fixed even basis vector has norm1 rather than2. These formulas follow by multiplying a literal2×2 pair block in sum/difference coordinates, not by assuming P_rho M symmetric.

If rank_F7(A0+A1)>=3, actual rank_K M>=8. Such a matrix has no all-unit complex kernel vector by the primitive equal-norm K-line descent. If an additional nonzero Schur pivot is found after the even5 and leading odd2 pivots, the same rank>=8 consequence applies. Only this necessary local condition is being excluded.

## 2. Positive off-axis T0 and positive paw-star P

These two families share exactly the data needed here. Label the two heavy leaves i,j and their triangle hub k, all in the first vertical set{b,d,e}; first H is either the same second isolate(T0) or the second paw pendant(P). The heavy edge is A1_ij=-2, the hub-light edges are opposite, A1_ki=a, A1_kj=-a, a=±1. All leaf Q1 pair tags are+1. The leading radical contains

    v=e_i-3e_j for a=+1,
    v=3e_i-e_j for a=-1.

It satisfies v_H=v_k=0 and B0 v=0. Its norm-square is10. The O1 action has squared norm42: for a=+1 its(i,j,k) values are(5,1,4); for a=-1 they are(-1,-5,-4). The extra pendant contribution is zero because v_k=0. Thus Q1² gives

    (B1 v)^T G_E(B1 v)/2=9*10-42=48.               (5)

The direct v-v curvature from(3) is zero. Indeed the first even pair block has no off-diagonal edge on these leaves; the second even leaf cross-entry is also zero, since these are parallel vertical pairs in distinct columns with the same two row labels. The diagonal products cancel because the two leaf tags are+1. Both entrywise mixed products in(3) vanish on v-v because B0 is supported in column H and C0 in row H.

By(2), the feedback term in the v-v Schur coefficient is

    (B1v)^T G_E A^(0)^-1(B1v)/128
       = -48/128 = -3/8 (mod s),

nonzero in F7. Hence an additional odd pivot exists and actual rank M>=8, for **every genuine second core in either of these positive families**, independently of all phases, first-label roles and unused mixed entries. No phase alphabet was assumed. This closes positive off-axis T0 and positive paw-star P.

## 3. Negative off-axis T1

Now the second heavy triangle contains first H, its isolated vertex K lies in{b,d,e}, and its heavy opposite pair i,j are the other two first vertical labels. The light entries A1_Hi=A1_Hj=a, a=±1, and A1_ij=-2. The second core is the negative of an all-rook off-axis grid matching. In that grid the first H is the parallel column0 pair, i,j are the other parallel columns, and K is the off-axis horizontal pair. The even pair block is

    (E1)_diag=-I,
    (E1)_Hi=(E1)_Hj=+1,
    all other off-diagonal entries zero.

The leading radical has basis

    u=2e_H-a e_K,  v=e_i-e_j.

Both Q mixed blocks annihilate v exactly, because O0 v=-3v and O1 v=3v and Q_j²=9I-J. On the whole leading radical, O1 y=-O0 y; thus the symmetric mixed-feedback difference has zero reduction by(2). The feedback cross terms with v vanish since both mixed blocks annihilate it. It remains to calculate(3).

Let h=(B1)_H i=(B1)_H j, which is±1: the parallel column0 mean meets each other parallel difference in exactly half a coordinate. Let b0_i,b0_j be the fixed first mixed column entries from(0,0,2,-2). In basis(u,v), the direct reduced2×2 curvature has zero diagonal and cross terms

    S2_uv=c+z,  S2_vu=c-z,
    c=-a*v_b/4,
    z=-h*(b0_i-b0_j)/8.                             (6)

The symmetric c comes only from the first even edge H-b of weight-2. The antisymmetric z comes from B0 o C1-C0 o B1 in(3); discarding it would be the invalid old-symmetry move.

If K=b, then v_b=0, while b0_i-b0_j=±4. Thus c=0 and z=±1/2, and both cross entries are nonzero modulo7. If K is one of d,e, the pair{i,j} contains b and the other diagonal, so c=±1/4 and z=±1/4. At least one cross entry is nonzero. Consequently this second Schur form always has rank>=1 and actual rank M>=8. This closes **all negative off-axis T1**, not merely a selected relabeling or coordinate phase set.

## 4. Negative off-axis T0: two role branches

The second isolate is again H. Its heavy leaves i,j have A1_ij=-2; the third vertical k has equal light entries A1_ki=A1_kj=a=±1. Put v=e_i-e_j. Both mixed Q blocks annihilate v, and the entire odd blocks satisfy

    D^(1)v=0,  v^T D^(1)=0,
    D^(2)v=0,  v^T D^(2)=0.                        (7)

For(7), the even negative off-axis pair block has off-diagonal entries+1 only on k-i,k-j; the symmetric part of(3) is their equal star. The mixed skew part has an H-k edge only, since(B1)_H i=(B1)_H j=0. Both kill v on the relevant side. The leading L=A0+A1 has rank2 and radical span(e_H,v).

### 4.1 k=b: common reflection, no phase can keep its fixed coordinate

The literal first x-reflection g(x,y)=(-x,y) fixes0 and both b endpoints. In the second off-axis grid, the same permutation is the column reflection: it swaps the horizontal H endpoints, interchanges the two equally oriented heavy parallel pairs i,j, and fixes the column0 pair k=b pointwise. Thus it preserves both actual unphased C matrices and commutes with rho, so M commutes with g. This is an actual shared permutation, not an asserted phase symmetry of delta.

The fixed subspace has dimension6. N on it has rank4; its reduced kernel is spanned by the b-odd direction and the sum of the i,j odd directions. L on this reduced kernel has matrix

    [0  2(2+a); 2+a  0],

of nonzero determinant modulo7. Therefore M restricted to Fix(g) is invertible. Averaging any hypothetical unit delta over g would retain its nonzero coordinate0 and lie in this zero kernel, contradiction. This closes every k=b core in this family.

### 4.2 k is a first diagonal: a fourth-order scalar survives

Choose i=b, and j the other first diagonal, so k is the remaining first diagonal. Give the common second heavy vertical difference orientation h=±1. The actual negative off-axis geometry gives the following mixed entries (the free horizontal orientation does not enter):

    (B1)_0i=(B1)_0j=-2h,
    (B1)_ki=(B1)_kj=h,
    (B1)_Hi=(B1)_Hj=0,
    (B1)_ik=(B1)_jk=-a*h.

All leaf-to-leaf mixed entries vanish. Pair-row formula(4) cancels on v. Its fixed row/column, which must not be silently treated as norm2 pair coordinates, instead give the exact identities

    B^(2)v=(h/2)e0=:r,
    v^T C^(2)=-(h/4)e0^T=:l.                      (8)

For example the first fixed-row pair averages are eta_i=+1,eta_j=-1; hence its odd-column difference is -(eta_i-eta_j)*(-2h)/8=h/2. Projecting the odd output against the fixed column gives the separate factor1/16 and value-h/4.

Using(7),(8), the exact even-eliminated v-v entry is

    S_vv=-s^4*l*A(s)^-1*r.

Its leading coefficient is

    -l*A^(0)^-1*r=-3/32,                            (9)

nonzero modulo7. It remains necessary to check that eliminating the two first-order odd pivots does not cancel(9). This follows from regularity rather than an informal truncation. By(1),

    C^(1) A^(0)^-1 e0 is divisible by7,
    e0^T A^(0)^-1 B^(1) is divisible by7.

Thus every cross entry S_(w,v),S_(v,w) starts at order at least s^4: its nominal s^3 coefficient is divisible by7=-s². The two leading odd pivot inverses have order s^-1, so their correction to S_vv starts at order s^7, not s^4. It cannot cancel(9). One additional odd pivot is therefore present and actual rank M>=8.

All inverses and divisibility statements occur in the local ring at(s), where the leading even determinant and the nonzero first-order odd2×2 determinant are units. This is finite exact algebra modulo powers of(s), not a floating asymptotic experiment. This closes every k=diagonal core in negative off-axis T0.

## 5. Scope after these lemmas

Together with the existing common-y-reflection descent for same-isolate **axis** triangles, sections2 and4 close **all T0**. Section3 closes all off-axis T1. Section2 closes the positive paw-star P branch. No direct scientific execution was used, and all diagonal phase freedoms are still present as arbitrary complex unit entries in ker M.

Two author-written tasks remain before a complete new-orientation packet: consolidate the negative-axis T1 family, whose exceptional role cases have explicit literal calculations, and close the **negative paw-star P** family. The latter is not covered by the off-axis T0 fourth-order calculation: its odd curvature has a nonzero hub component, and claiming(7) there would be false. Parent support for the earlier central-negation route is not being imported as acceptance of these new nonsymmetric lemmas. All this remains CANDIDATE until complete pinned reconstruction. Full maximal1-RQLS10 remains UNKNOWN even if the entire present first orientation ultimately closes.
