# Off-axis first profile: all96 negative two-edge-matching second cores v1

PhysicsRQLS10, same primary. Complete author-written CANDIDATE for this second-core family, not the full off-axis orientation. Actual working clock observed before creation:2026-10-24T05:29:00-07:00. No scientific program, arithmetic interpreter, enumeration, solver, compilation, checker or CLI ran. Coefficient reductions below are written determinant certificates, never reductions of unknown physical phases.

## 1. Exact critical family and exhaustive parameterization

First rho=(0,7,8,6,5,4,3,1,2), paired H,J,U,V and actual rank3 B0 stay fixed. First A0_JU=A0_JV=1,A0_UV=2,H isolated. The second family is the negative all-rook two-edge-matching class, hence D1=-I. Its96 literal cores have A1 supported on two disjoint unit edges.

Exactly as a support argument (not a phase duality),64 cases have a nonzero leading triangle and close at actual rank>=8. Only the following32 can have leading rank2:

    H-neighbour k in{U,V}, other heavy leaf l,
    A1_Hk=p=±1, A1_Jl=-1.

Then L=A0+A1 is a star at k with leaf weights p on H,1 on J and2 on l. A literal first x-reflection transports k=U to k=V, changing p,mu signs as below and retaining all arbitrary phases. It suffices to print all16 k=U cases explicitly.

For k=U,l=V choose p,mu,nu independently±1 and epsilon∈{0,1}. Every E1 has fixed row/column0 zero, pair diagonal-I and off-diagonal+1 only at H-U,J-V. Its odd block is O1=I+A1. The complete B1 tables are, in even order(0,H,J,U,V) and odd order(H,J,U,V):

    epsilon0:
    [ 2mu  2nu -2p*mu  2nu;
       0    0   -p*mu -2nu;
      -2mu  0     0     nu;
       mu -2nu    0      0;
       0    nu  2p*mu    0 ],

    epsilon1:
    [ 2mu  2nu -2p*mu  2nu;
       0  -2nu  -p*mu    0;
       0    0   2p*mu   nu;
       mu   0     0   -2nu;
      -2mu  nu    0      0 ].

These are the entire family, not arbitrary mixed-block choices. Before negation, source-normalize the horizontal pair group to

    A={(0,1),(1,1)}, B={(0,2),(2,2)},

and the vertical group to

    C={(1,0),(1,2)}, D={(2,0),(2,1)}.

The physical group H,k can be normalized horizontal by source interchange, and J,l vertical. The two assignments of C,D give the two cross-patterns epsilon. Endpoint orientations are exactly the column multipliers(-mu,-nu,p*mu,-nu) relative to the printed canonical negative table. The edge signs then become p and-1 and the fixed-row differences become the stated values. Source signs/interchange exhaust the two raw matchings; no other even pattern remains. Distinct p changes A1, distinct mu/nu changes fixed differences, and distinct epsilon changes a zero versus a nonzero cross-entry. Thus2*4*2=16 distinct k=U tables, and32 with k=V included.

## 2. The actual second Schur form is skew on the leading radical

Use the leading radical basis

    u=e_H-p e_J, v=2e_J-e_V.

First D0=I and second D1=-I imply O1=-O0 on that radical. The symmetric mixed-feedback difference therefore vanishes modulo(s). The direct symmetric curvature also restricts to0: its only possible active B edge J-V has E0_JV=-1,O1_JV=-1,O0_JV=1,E1_JV=+1, giving cancellation; all H off-diagonal terms vanish and diagonals cancel. Thus the reduced2×2 second Schur form is skew.

For clarity, with T_A=G_E A^(0)^-1, its skew feedback cross coefficient is

    -[(B0u)^T G_E(B1v)-(B1u)^T G_E(B0v)]/256

modulo(s), because regular mixed columns replace T_A by-G_E/2 there. Its direct skew cross coefficient is

    u^T[B0_pair o B1_pair^T-B0_pair^T o B1_pair]v/16.

Both asymmetric pieces are retained. Substituting the COMPLETE tables gives

    epsilon0 direct =-mu/2+nu/4,
    epsilon0 feedback =-3[mu-(p+2)nu]/64,
    epsilon0 total kappa=[-35mu+(22+3p)nu]/64.

Modulo7 this is4nu/64 for p=+1 or5nu/64 for p=-1, always nonzero. Hence all16 epsilon0 cases over both k choices have an actual further odd pivot (indeed the skew2×2 form has rank2). Their matrices are nonsingular and have no complex phase kernel.

For epsilon1 both cross pieces cancel. That zero is NOT called a phase witness. The remaining16 cases require actual phase geometry, supplied next.

## 3. A first-order certificate for full Hermitian norm-span

The following is a conditional structural argument, not an assumption about the phase field. Any possible phase in the critical class must have actual rank7: leading rank2 gives rank>=7 and the general rank8 norm theorem excludes rank>=8.

Under that rank7 hypothesis, choose a K-basis V(s) of the full kernel integral in the local ring at(s), s²=-7, whose leading odd part is the displayed real basis(u,v). Such a lift exists: eliminate the even unit block and the two order-s odd pivots; after factoring s their pivot block is a unit, the remaining2×2 Schur block is exactly0 because total rank is7, and the two radical coordinates remain free. The odd part is Y0+sY1+..., Y0=(u,v); the even part is

    x=s X1+O(s²),
    X1=-A^(0)^-1*(B1-B0)Y0/8.                    (1)

All congruences are in that exact local ring, not a numerical small-s approximation.

For each physical coordinate j, let F_j=V_j^* V_j be its2×2 Hermitian norm matrix. Its entries are in K. Take rational coefficient vectors of the form

    [r11,r22,Re r12, coefficient_of_s(r12)].

These coefficients are integral at7. A basis change of the complex kernel acts by invertible real-linear Hermitian congruence, so the dimension of their real span is intrinsic.

For pair a, the two rows are even x_a plus/minus odd y_a. The sum F_ra+F_rhoa has leading real-symmetric part2Y0_a^T Y0_a. Its fourth coefficient may have a leading term, but the first three coefficient columns from H,J,V are independent modulo7, since their Y0 rows are(1,0),(-p,2),(0,-1). The cross coefficient-4p is a unit.

The pair DIFFERENCE cancels every first-order correction Y1. Its leading matrix is

    2s*(Y0_a^T X1_a-X1_a^T Y0_a).

The first three rational coefficients are divisible by7, while its fourth coefficient modulo7 is, up to sign,2det(Y0_a,X1_a). Therefore if this determinant is nonzero at even one physical pair, these three sums plus that difference have an actual nonzero4×4 coefficient determinant. The Hermitian norm-span then has rank4 over Q and R. No unknown phase was reduced modulo7; only coefficient determinants were.

A rank4 span excludes a full coordinate-unit vector: the equations diag(V X V*)=1 uniquely reconstruct the four real coordinates of X in rational arithmetic. For a physical vector X=z z* is rank1; its diagonal entries are rational and off-diagonal is in K, so z1/z2∈K (or one z-coordinate vanishes). The entire physical delta is projectively K-valued, contradicting the general fixed-coordinate equal-norm descent. A full-rank mixed positive X is not a physical rank1 vector and is not ruled out by this argument. Thus no universally feasible relaxation is mistaken for a phase construction.

## 4. Fourteen epsilon1 cases have the displayed full-span certificate

For a regular raw mixed difference g=(B1-B0)y, formula(1) gives at a pair coordinate

    X1_a(y)=g_a/16-g0/128.                       (2)

The first inverse formula uses sum(g_pair)=-g0/2; its fixed-coordinate component is not silently treated as a norm2 pair.

For epsilon1, on v=2J-V,

    g_v=(nu+1)*(2;-4,-1,2,2),
    X1_H(v)=-17(nu+1)/64.

If nu=+1, this is a unit modulo7. Since Y0_H=(1,0), the pair-H determinant certificate in section3 is nonzero, uniformly over p and mu.

If nu=-1, g_v=0. On u=H-pJ, the pair-V coefficient is

    X1_V(u)=(8-9mu-p)/64.

Its possible integer numerators are-2,0,16,18. The only zero is mu=+1,p=-1; all other values are nonzero modulo7. Since Y0_V=(0,-1), its pair-V determinant certificate is nonzero in those cases. Thus, over both k choices,14 of the16 epsilon1 cases close: either actual rank>=8 already excludes phases, or the rank7 hypothesis supplies full Hermitian norm-span and forces forbidden projective K phases. No actual rank or phase was guessed from a small residual.

## 5. The two exceptional tables have whole purely odd kernels

The only remaining canonical k=U case is epsilon1,nu=-1,mu=+1,p=-1. Its leading star is centred at U. Let

    a=(2;0,0,-1,0)

be an even vector in order(0,H,J,U,V). Actual subtraction gives

    (B1-B0)e_H=a,
    (B1-B0)e_J=-a,
    (B1-B0)e_V=-2a.

The direct EO curvature has exactly

    B^(2)e_H=B^(2)e_J=a/8,
    B^(2)e_V=0.

For example the two fixed entries are1/4 and the two U-pair entries-1/8; all other entries of those columns vanish. These are direct fixed/pair formula identities from the printed matrices, not executed checks.

The entire odd operator is

    D(s)=(s/8)*[0 0  1-s  0;
                 0 0 -1-s  0;
                1+s -1+s 0 -2;
                 0 0  -2   0].

It kills the two independent purely odd vectors

    w1=(1-s)e_H+(1+s)e_J,
    w2=2e_J-(1-s)e_V.

Their raw mixed differences are both-2s*a, while B^(2)w1=B^(2)w2=a/4. Hence

    Bop(s)w_i=(s/8)*(-2s*a)+s²*(a/4)=0

exactly for i=1,2. Thus they are actual full-kernel vectors. Leading rank2 gives actual rank>=7; these two independent kernel vectors give rank<=7. The entire complex kernel is therefore their span, whose fixed coordinate0 is0. An all-unit vector is impossible.

The literal first x-reflection sends k=U to k=V and(p,mu,nu) to(-p,-mu,nu), with the same epsilon pattern. It preserves first C/rho and transports the full arbitrary phase torus. Thus the other exceptional table is covered without imposing reflection symmetry on an unknown phase vector.

## 6. Complete family accounting and exact remaining problem

There are64 noncritical inputs with leading rank>=3,16 critical epsilon0 inputs with a nonzero second skew form,14 epsilon1 inputs excluded by the first-order Hermitian norm-span certificate, and2 exceptional actual-rank7 inputs with purely odd whole kernels. Total96, all negative two-edge-matching second cores, with arbitrary independent D/E.

This is NOT deduced by transporting the positive matching scalar: that scalar cancels for these negative tags. The negative proof keeps its own full B1 tables, actual Hermitian coefficient determinants and exceptional full kernels. The count is mathematical, not an executed96-case enumeration, and every finite sign split is printed.

Together with the earlier positive matching candidate this treats the whole192-core two-edge support class at this first orientation. All such claims still require their own actual reconstruction. Other H-degree0/1/2 rank2-leading families remain; the full all-P off-axis orientation, all complex H0 lifts and unrestricted maximal1-RQLS10 remain UNKNOWN. No novelty, formal/kernel/human acceptance or scientific execution is asserted.
