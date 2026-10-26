# All96 negative-axis-triangle second cores: axial first orientation v1

Observed before creation: **2026-10-23T16:56:30-07:00**. PhysicsRQLS10; exact written author candidate, no program, arithmetic runtime, solver or execution. Same literal first C and rho_ax as `selection-v2-axial-orientation-v1.md`; all independent complex diagonal phases retained. This is a complete finite **family** closure, not yet the complete axial orientation or QLS10.

## 1. Parameterization, with no unproved WLOG on the first orientation

Use H=first horizontal pair{1,2}; b=V0={3,6}; d=V1={4,7}; e=V2={5,8}. The first B0 mixed column is b0=(0;0,0,2,-2). A negative-axis second core is the negative of a relabeled axis all-rook grid core. It is determined by:

- an isolated second odd vertex K, four choices;
- a distinguished parallel J≠K, three choices;
- three parallel-root orientation signs sigma modulo simultaneous reversal, four choices;
- the horizontal-root/mixed-column sign, two choices.

Its blocks are

    D1=-I, O1=I+A1;
    A1_ab=-2*sigma_a*sigma_b among the three parallels, zero at K;
    (E1)_pair=-I+2(e_K e_J^T+e_J e_K^T);
    B1=b1 e_K^T,

where b1 has entries±2 with opposite signs at the two parallel pair means other than J, and0 elsewhere including coordinate0. The full even fixed row is-2 on K,J and+2 on the other two pair columns, with the corresponding half-sized pair-to-fixed column.

These data reconstruct the full Q1, hence are unique. All are realized by permuting the three column pairs and choosing endpoint orientations of the axis rook matching. There are4*3*4*2=96 literal cores. Equivalently, the two raw axis matchings contribute2*384/8=96. This is a parameterization of this family, not a claim that all5040 cores are axis triangles.

If K=H, every such second core shares the literal y-reflection g(x,y)=(x,-y). `axial-partial-symmetry-descent-v1.md` excludes its arbitrary complex phase kernel, including actual rank5 cases. This closes24 cores.

Suppose K≠H, and call the other two first vertical labels i,j. If sigma_i≠sigma_j, then A1_ij=+2 so L=A0+A1 has an H-based nonzero triangle. Rank L>=3 and the rank8 norm descent excludes all phases. This closes36 cores.

It remains that sigma_i=sigma_j. Normalize them to1 and write t=sigma_H=±1. Then A1_Hi=A1_Hj=-2t, A1_ij=-2, and

    ker L=span(u,v), u=e_H+t e_K, v=e_i-e_j.

## 2. A single second-order formula closes24 of the remaining36

Use the exact nonsymmetric mixed algebra of `axial-mixed-block-closures-v1.md`. Both B0 and B1 annihilate v. On the leading radical, O1=-O0, so the symmetric feedback difference vanishes modulo(s), and all feedback cross terms with v vanish. The direct curvature's two cross coefficients are equal:

    S2_uv=S2_vu=(t/4)*(v_b-v_J),
    S2_uu=S2_vv=0.                                (1)

For(1), the first even edge H-b gives the t*v_b/4 term; the second even edge K-J gives-t*v_J/4. The direct mixed skew term is supported only on H-K, and thus has zero restriction on u,v. No global P_rho M symmetry is assumed.

The coefficient is nonzero except in exactly two role types:

    R: K=b, J=H;
    S: K∈{d,e}, J=b.

Indeed when K=b, v_b=0 and only J=H makes v_J=0. When K is a first diagonal, v_b=±1; equality v_J=v_b requires J=b. All other choices give difference±1 or±2, nonzero modulo7, hence an additional pivot and rank M>=8. These nonexceptional six(K,J) roles contribute6*4=24 critical-orientation cores and are closed by(1).

The R type has4 critical cores; S has8. The next sections reconstruct all of them, without dropping a phase freedom.

## 3. Literal convention for the prototypes and the only normalization symmetries

Here a permutation tuple p means precisely

    Q1_(x,y)=-Q0_(p(x),p(y)),
    M_(i,t)=conjugate(C_(t,i))*conjugate(C_(p(t),p(rho(i)))).

Thus a **source** automorphism g replaces p by g∘p and leaves Q1 unchanged. Replacing it by p∘g instead would in general change the physical second core. This order matters below.

Set u=w²=(-3+s)/4, v=w^-²=(-3-s)/4. Thus uv=1, u+v=-3/2, u-v=s/2 and u²+(3/2)u+1=0. Every displayed raw M entry is0,1,u or v.

The only first-core equivalences used are the literal x and y reflections g_x,g_y. They commute with rho_ax and preserve the first C exactly. For R, both act on the two remaining signs(t,epsilon) by simultaneous reversal. The two epsilon choices at t=+1 therefore represent its four critical cores. For S, define epsilon=(b1)_H/2. Then

    g_y:(K,t,epsilon)→(K,-t,-epsilon),
    g_x:(d,t,epsilon)→(e,-t,epsilon), and conversely.

The two epsilon choices at K=d,t=+1 have disjoint four-element orbits and represent all eight critical S cores. These sign actions follow directly from pair endpoint permutations and the printed B1 column; they do not fix the complex delta to be symmetric.

## 4. Type R, first prototype: exact rank7 and a forbidden norm ratio

Take

    p_R=(0,3,6,1,4,5,2,7,8).

It swaps the two first axis pairs and leaves all diagonal points unchanged. Q1 is the negative core above. Both literal cores preserve g_n(x,y)=(-x,-y), and g_n commutes with rho_ax, so M commutes with g_n.

For the g_n-even part use coordinates

    z0; a on{1,2}; b on{3,6}; c on{4,8}; d0 on{7,5}.

Its five equations, after division of the fixed row by2, are

    v(a+b)+u(c+d0)=0,
    v*z0+2u*b+2c+(u+v)d0=0,
    v*z0+2u*a+2c+(u+v)d0=0,
    u*z0+2a+(u+v)b+c+d0=0,
    u*z0+(u+v)a+2b+c+d0=0.

They give uniquely in terms of z0

    a=b=(3+s)z0/8,
    c=(83-7s)z0/112,
    d0=(-5-7s)z0/28.                              (2)

In the g_n-odd coordinates with representatives1,3,4,7, the actual block is, writing q=s/2,

    [ 0   0   0  -q]
    [ 0   0   0   q]
    [ 0  -q  -1  -1]
    [-q   0  -1  -1].

Its kernel is span(1,1,-q,0). In particular the entire odd kernel vanishes on the last pair{7,5}. For any full kernel vector the two coordinates7,5 must therefore equal the value d0 in(2), while its coordinate0 is z0. If all physical coordinates had modulus1, |z0|=1 would imply

    |delta7|²=|delta5|²=|(-5-7s)/28|²=23/49,

not1. This excludes arbitrary complex phases, not merely K-valued or g_n-symmetric phases. The actual two blocks have ranks4 and3, so this is a genuinely rank7 exception to a rank-only argument.

## 5. Type R, horizontal-orientation reversal

Take

    p_R'=(0,3,6,2,4,5,1,7,8).

This reverses only the second isolated horizontal orientation relative to the preceding core. It still commutes with g_n as a label permutation, so both cores and M preserve g_n. The necessary even equations from the fixed, beta and gamma rows are now

    v(a+b)+u(c+d0)=0,
    u*z0+2(a+b)+c+d0=0,
    u*z0+(u+v)(a+b)+c+d0=0.

The last two imply(7/2)(a+b)=0. The first then gives c+d0=0, and the second gives z0=0. Averaging any hypothetical phase vector over g_n would preserve its nonzero coordinate0, contradiction. This treats the other sign orbit; no assumption about the averaged other coordinates' moduli was made. Together sections4–5 close all four R critical cores.

## 6. Type S, first prototype: unit norms force a forbidden K vector

Take

    p_S=(0,4,7,3,1,5,6,2,8).

It is the involution(1 4)(2 7), fixes0, and commutes with rho_ax. Because Q1=-Q0∘(p_S,p_S), direct multiplication of the two scalar factors gives

    M_(p_S(i),p_S(t))=M_(rho(i),t).

Thus ker M is invariant under the right permutation p_S, even though M need not commute with p_S. Its anti-invariant vector has coordinates delta1=x,delta4=-x,delta2=y,delta7=-y, all others0. Rows1,2,3 of M applied to it give

    -v*x-y=0, -x-u*y=0, (u-1)(x-y)=0.

The first gives y=-v*x, and the third becomes(u-v)x=0. Hence this anti-invariant kernel is zero. Every kernel vector is genuinely p_S-even, not just an averaged vector.

Normalize a hypothetical phase vector so delta0=1 and write

    delta1=delta4=a, delta2=delta7=b,
    delta3=c,delta6=d0,delta5=e0,delta8=f.

All six variables have modulus1. Five necessary raw row equations(0,1,2,3,5) are

    2a+2b+v(c+d0)+u(e0+f)=0,
    1+u*c+v*a+u*e0+d0+b+f=0,
    1+c+a+v*e0+u*d0+u*b+f=0,
    v+(u+1)(a+b)+e0+f=0,
    u+(u+1)a+(v+1)b+c+d0=0.

Eliminating sums gives

    (19+3s)a+26b=16,                               (3)
    e0=(381+49s)/364+(7-9s)a/52.                    (4)

The other coordinates are also K-affine in a, by those same sums and the two nonsingular difference equations. Since |a|=|b|=1 and |19+3s|²=424, equation(3) yields

    Re[(19+3s)a]=1/8.                              (5)

The additional |e0|=1 condition in(4) implies Re(beta*a)∈Q, where

    beta=conjugate((381+49s)/364)*(7-9s)/52
        =(-105-943s)/4732.

The coefficient vectors(19,3) and(-105,-943) have determinant-17602≠0. Thus these two real-linear equations in Re a and sqrt7*Im a force a∈K. Equations(3),(4) and the remaining linear rows then force the entire normalized delta into K.

Such a projective K-valued all-unit kernel vector is impossible at this rho. To recall the actual argument rather than import a scope claim: clear its rational denominators into Z[s]; all nine norms are the same positive integer. Reduction modulo(s) of M is N, whose kernel is rho-odd and whose fixed coordinate0 is0. If the common norm is divisible by7, all constant coefficients are divisible by7, so divide every entry by s, retaining integral coefficients and reducing the common norm by7. At the first common norm not divisible by7, the fixed-coordinate norm is nevertheless0 modulo7 because N still kills the reduction: contradiction. Complex phases were unrestricted before equations(3)–(5) forced K. Hence this prototype has no unit kernel vector.

## 7. Type S, horizontal-orientation reversal: fixed coordinate vanishes linearly

Take

    p_S'=(0,4,7,3,2,5,6,1,8).

Use the source automorphism g_y to replace it by the **same-core** permutation q=g_y∘p_S':

    q=(0,7,4,6,2,8,3,1,5)
      =(1 7)(2 4)(3 6)(5 8).

This is an involution commuting with rho_ax. The factor-exchange identity of section6 therefore makes ker M invariant under q. Average any hypothetical phase vector over q; coordinate0 remains a nonzero z0. The resulting even vector has

    delta1=delta7=a, delta2=delta4=b,
    delta3=delta6=c, delta5=delta8=d0.

No unit assumption is made about a,b,c,d0. The raw rows0,1,2,3,5 give

    a+b+v*c+u*d0=0,
    z0+v*a+b+(u+1)(c+d0)=0,
    z0+a+u*b+(u+1)c+(v+1)d0=0,
    v*z0+2u*a+2b+2d0=0,
    u*z0+2u*a+2v*b+2c=0.

The last two give

    c=-(u/2)z0-u*a-v*b,
    d0=-(v/2)z0-u*a-b.

Substituting these into the second and third equations gives

    a+b=-(7+3u)z0/2,
    b=(1+3v)z0/4,
    a=-(21+6u)z0/8.

The first equation then becomes

    -(133+110u)z0/32=0.

Its coefficient is nonzero because u is nonreal. Therefore z0=0, contradicting the preserved fixed phase. This is a purely linear exclusion of all complex phases, not a rounded residual or a field restriction. Section3's literal reflection orbits now cover all eight S critical cores.

## 8. Complete family accounting and exact remaining larger problem

The disjoint accounting is24 same-isolate cores,36 noncritical-sign cores,24 nonexceptional critical-role cores,4 type R and8 type S: total96. Every one is excluded at the necessary local phase-zero bridge, with arbitrary D/E. The rank7 and symmetry exceptions were actually treated, not incorrectly forced into a rank8 assertion.

Combined with the other new axial lemmas, the presently isolated remaining larger-orientation branch is the sixteen exceptional negative parallel-leaf paw cores specified in `axial-negative-paw-fourth-order-v1.md` **with** `axial-negative-paw-count-erratum-v1.md`. This family closure alone does not prove the whole axial no-go, all orientations, all complex H0 lifts, or maximal1-RQLS10 impossibility. No scientific source has been run; all new family arguments still require their own complete pinned reconstruction before acceptance.
