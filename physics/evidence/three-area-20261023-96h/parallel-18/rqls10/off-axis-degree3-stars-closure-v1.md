# Off-axis first orientation: every degree3-H leading star closes v1

PhysicsRQLS10, same primary. Author-written CANDIDATE, not yet independently reconstructed. Actual clock before creation:2026-10-24T05:08:40-07:00. No scientific program, arithmetic interpreter, enumeration, solver, compilation or CLI ran.

This consumes the working leading classification **WITH** `off-axis-leading-rank2-tag-erratum-v1.md`. The old assertion that the one-heavy family's sole rook must lie on its heavy edge is false; ALL FOUR rook positions are explicitly treated here. No original source is rewritten.

## 1. Fixed first, exact star profiles and retained phase freedoms

First rho=(0,7,8,6,5,4,3,1,2), pair order(H,J,U,V), and the actual rank3 first mixed block remain those in `off-axis-first-blocks-and-scope-v1.md`. First A0_JU=A0_JV=1,A0_UV=2,H isolated. Every second core is genuine PC P^T with arbitrary independent complex D/E.

For H degree3 and leading rank2, the entire B={J,U,V} triangle must cancel:

    A1_JU=A1_JV=-1, A1_UV=-2.

Only two genuine complete support classes are possible:

(A) negative one-rook K4 with unique heavy U-V;
(B) k2 K4 with heavy edges U-V and H-J, the former joining diagonal pairs and the latter rook pairs.

Other degree3-H shapes leave a first-triangle edge uncancelled and a nonzero principal triangle modulo7. This file excludes both(A),(B), not merely some signs.

Write Q blocks as[E B; B^T G_E/2 O], and operator M blocks as[A Bop; Cop D]. The second Schur quadratic on a leading radical y is, modulo(s),

    y^T S2 y=y^T D^(2)y
                +[|O1 y|²-|O0 y|²]/128.          (1)

This follows from the actual nonsymmetric mixed feedback: the two cross terms cancel only in its scalar quadratic, the even inverse is metric-self-adjoint, and regular mixed columns satisfy the previously derived inverse-norm identity. It does NOT assert that the full Schur matrix is symmetric.

On these star radicals y_H=0 and A1 y=-A0 y. Since D0=I,

    O1 y=-O0 y-2*P_R y,
    |O1y|²-|O0y|²=4*sum_(r in R) y_r*(A0y)_r,   (2)

where R consists of the second rook-positive vertices among B. The direct symmetric curvature is

    -[A0 o(E0+E1)]/16

on B, with E0_JU=E0_JV=-1,E0_UV=0. Direct skew terms contribute0 to a scalar y-y evaluation. Actual E1 entries, not a frozen first-profile surrogate, will be used below.

## 2. One-heavy class: all tag positions and exact parameters

Every off-diagonal A1 product in the one-heavy class comes from four A2 y-roots, with U,V parallel. Their signs force

    A1_HU=A1_HV=h, A1_HJ=-h, h=±1.

Thus L is the star at H with weights h*(-1,1,1), and its radical is

    y_H=0, y_J=y_U+y_V.                           (3)

Let r∈{H,J,U,V} be the unique second rook-positive vertex. Before negation it is the extra diagonal pair among three parallel rook pairs. If r is H orJ, the heavy endpoints U,V are the two source rook pairs sharing their y-root, one of them in source column0. There are two choices sigma for which heavy endpoint has column0, and a simultaneous odd sign lambda=±1. If r is U orV, its heavy partner must be the source column0 pair, so that choice is fixed; lambda remains free. Together with h, these give

    r=H:8, r=J:8, r=U:4, r=V:4, total24.

These parameters exhaust the actual source geometry: the positive parallel construction has two leftover row levels a≠b. If neither is0, the diagonal pair forms the heavy edge with the column0 rook. If one is0, two rook pairs form the heavy edge instead. Source coordinate signs/interchange normalize those raw cases; the relative odd signs are prescribed by the displayed A1, leaving only the global lambda. This is the corrected geometry behind the mandatory tag erratum.

The even B-triangle entries are:

- r=H: E1_JU=E1_JV=+1,E1_UV=0;
- r=J: E1_J,R0=+1,E1_J,other=-1,E1_UV=0, where R0 is the heavy endpoint in source column0;
- r=U: E1_JU=-1,E1_JV=+1,E1_UV=0;
- r=V: E1_JU=+1,E1_JV=-1,E1_UV=0.

They follow by averaging the actual rook/diagonal endpoint coordinates. A diagonal pair against a nonzero-column rook has negative-core mean-1; against the column0 rook it has mean+1 in the one-zero-leftover geometry and0 when that is its heavy partner. Two distinct nonparallel source rooks have negative-core mean+1, while parallel ones have mean0.

## 3. All sixteen cases with the sole rook in B close at second order

If r=J, choose y_J=1, y_R0=1 and the other heavy coordinate0. Equation(3) holds. The only active direct edge has E0+E1=-1+1=0, so direct curvature is0. Equation(2) gives norm difference4, and(1) gives1/32 modulo7, nonzero. This closes all8 such cores.

If r=U, choose y_J=y_U=1,y_V=0. Direct curvature is1/4 from E0_JU+E1_JU=-2. The norm difference is4, so the full scalar is

    1/4+1/32=9/32≠0 (mod7).

For r=V use the exchanged vector. Thus all4+4 cases close. The additional actual odd pivot proves rank M>=8; every arbitrary complex phase vector is excluded. No mixed orientation or physical phase was fixed to obtain these scalar certificates.

## 4. r=H: exact fourth-order computation retains all eight cases

Let sigma=+1 when U is the source column0 rook and-1 when V is. For the canonical sigma=+1,h=lambda=+1 source geometry, the full second mixed block is

    B1=[-2 -2  0  0;
         0 -1 -1 -1;
         1  0  1  1;
         1  1  0  0;
        -1  1  0  0],

in even order(0,H,J,U,V), odd order(H,J,U,V). Reversing h reverses only its H column; lambda multiplies the full B1 by lambda; exchanging sigma swaps physical U,V means/odd labels. In particular for every case

    B1_J=lambda*q, q=(-2;-1,0,1,1).

Let v=e_U-e_V. Both first Q mixed blocks kill v. The odd operator is an exact star at H, with

    D_HJ=(s*h/8)*(1+s*lambda),
    D_JH=(s*h/8)*(1-s*lambda),
    D_Hv=s²*lambda/4, v^T D e_H=-s²*lambda/4.

The corrected right/left odd vectors

    v_R=v+beta_R*e_J, beta_R=-2s*lambda*h/(1+s*lambda),
    v_L^T=v^T+beta_L*e_J^T, beta_L=+2s*lambda*h/(1-s*lambda)

kill D exactly on their sides. The denominators are local units; beta itself has valuation1 and is NOT a unit. These independent unipotent changes do not divide by beta.

Direct fixed/pair curvature gives

    r=B^(2)v=(sigma/2; h/4,0,0,0),
    l=v^T C^(2)=(1/2)*r^T G_E.

The leading corrected mixed vectors have the form

    rhat=x+y, lhat=(1/2)(x-y)^T G_E,
    x=r-(lambda*h/4)B1_J,
    y=(lambda*h/4)B0_J.

Their actual entries simplify to

    x0=(sigma+h)/2,
    x_pair=(h/2)e_H-(h/4)(e_U+e_V),
    y0=0, y_pair=lambda*x_pair.

Both pair sums vanish and each pair squared norm is3/8. The exact universal even inverse and its self-adjointness therefore give the fourth-order scalar

    -lhat*A^(0)^-1*rhat=3*x0²/8.                  (4)

All cross entries to the two leading odd pivots begin at s3, so their feedback begins at s5 and cannot cancel a nonzero s4 coefficient. When sigma=h, x0=±1 and(4) is nonzero modulo7. This closes four of the eight r=H cores.

The remaining four have sigma=-h. They are NOT declared excluded by the zero scalar. The literal first x-reflection exchanges sigma,h simultaneously and keeps lambda, so it suffices to treat sigma=+1,h=-1 with lambda=±1. It preserves the first C/rho and merely transports arbitrary unknown phases.

## 5. First exceptional rank7 prototype: two exact purely odd kernel vectors

Take sigma=+1,h=-1,lambda=-1. Let w=e_J+e_U, v=e_U-e_V and

    z=(1-s)*v-2s*e_J.

The exact star D kills w and z. Direct mixed-block substitution gives

    Bop(s)w=0,
    B^(1)v=0, B^(2)v=r,
    B^(1)e_J=r/2, B^(2)e_J=-r/2,
    r=(1/2;-1/4,0,0,0).

Consequently Bop(s)z=(1-s)s²r-2s*[s(1-s)r/2]=0 as well. Thus w,z are actual full M-kernel vectors, not just leading-kernel vectors. They are independent and purely rho-odd, with coordinate0 zero.

The universal even5 plus leading odd2 pivots prove rank M>=7. Two independent kernel vectors prove rank M<=7; hence actual rank7 and the entire complex kernel is their span. Every vector in it has coordinate0 zero. This excludes arbitrary complex phase vectors without any modulus restriction elsewhere.

## 6. The transpose prototype: four physical norms force projective K phases

Changing lambda is conjugation of the second core by rho, so for this pair the matrices are transposes. The remaining lambda=+1 matrix has actual rank7 as well; left-kernel information alone is NOT used as a right-phase obstruction. Its literal negative-core source tuple is

    p=(0,3,4,2,5,1,8,6,7),
    Q1_xy=-Q0_(p(x),p(y)).

For reproducibility all consumed raw rows are listed. Write t=delta0 and z_j=delta_j:

    R0: v*z1+z2+v*z3+u*z4+z5+z6+z7+u*z8=0,
    R1: v*t+z2+u*z3+z4+u*z5+z6+z8=0,
    R7: t+z2+u*z3+v*z4+u*z5+z6+z8=0,
    R2: t+z1+u*z3+u*z4+v*z5+z6+z7=0,
    R8: u*t+z1+u*z3+z4+v*z5+z6+z7=0,
    R3: t+u*z1+u*z2+v*z4+z5+z7+z8=0,
    R6: v*t+u*z1+u*z2+z4+z5+z7+z8=0,
    R4: t+z1+z2+v*z3+u*z6+z7+z8=0,
    R5: u*t+z1+v*z2+v*z3+z6+u*z7+z8=0,

where u=(-3+s)/4,v=(-3-s)/4. The symbol v in these equations is the scalar w^-2, not the preceding odd vector. Entries follow from the literal character-neighbour rule, with the two required zero columns per row omitted.

R8-R2 forces z4=t. A phase vector has |t|=1, so normalize t=1. Put b=z2,a=z1,d=z5 and T=34+40u, with |T|²=716. Ordinary K-linear elimination of the displayed rows gives

    d=[22+16u+21(2u-1)b]/T,
    a=[32(u+4)+35(2u-7)b]/(7T).                  (5)

For checking the elimination, two intermediate equations are

    14a+(6u-1)d=-3(2u+1)-7(4+3v)b,
    -7(u+2)a+(21+19u)d=11(u+1)+(7/2)(4u-1)b.

All denominators here are nonzero complex/K numbers; factors7 are used in ordinary characteristic-zero algebra and are not called local-ring units.

The actual physical entries a,b,d all have modulus1. For each affine expression A+B*b in(5), its unit norm therefore gives a rational real-linear condition on b with cross coefficient conjugate(A)*B. The two coefficients, up to nonzero rational factors, are

    beta_d ∝ -11+15s,
    beta_a ∝ -107+15s.

Explicitly their numerator products are21(-11+15s) and280(-107+15s), with rational norm denominators716 and49*716. Their coefficient-vector determinant is

    (-11)*15-15*(-107)=1440≠0.

Thus Re b and sqrt7*Im b are rational, so b∈K. Equation(5) gives a,d∈K. All other normalized entries are also K-linear in them: with c=z3,f=z7,g=z8,e=z6, the raw rows give

    c=a-v-(5/2)v*b-(1-v)d,
    f=(1-v)a-v²*c+v*d+v²-1+b,
    g=-(v+1)-u*b-u*a-d-f,
    e=1+f-v*b.

Together with z4=1 these force the entire normalized phase vector into K. Only AFTER those unrestricted physical unit equations is the general fixed-coordinate norm descent applied, contradicting a projective-K unit vector. This is an actual rank7 Hermitian norm-span4 instance, not a mere request to test such a criterion. It excludes the second exceptional prototype and, by the literal first reflection, all four sigma=-h cores.

## 7. Two-heavy class: all eight cases close by one scalar

For the other degree3-H support, U,V are diagonal pairs and H,J are rook pairs. The parallel rook relation forces

    A1_HJ=2t, A1_HU=A1_HV=-t, t=±1.

The radical condition is y_H=0, 2y_J=y_U+y_V. The actual even U-V entry is0; among E1_JU,E1_JV one is+1 and the other-1, according to which diagonal shares the nonzero source column of J.

Choose y_J=1 and set the diagonal coordinate with E1=+1 to2, the other to0. This satisfies the radical equation. Its only active edge has E0+E1=0, so direct curvature is0. The only rook in B is J, and(2) gives norm difference8. Therefore(1) gives

    8/128=1/16≠0 (mod7),

uniformly over all signs and geometry. Actual rank M>=8 excludes every complex phase. The two choices t, the two global odd signs and the two even-column geometries give eight literal cores; all are retained.

## 8. Composition and precise remaining scope

The one-heavy class has24 actual cores:16 close at second order,4 at fourth order and4 by the two exceptional rank7 prototypes. The two-heavy class has8 and closes at second order. Thus EVERY genuine degree3-H leading star in this off-axis first orientation is excluded, all32 literal second cores, with arbitrary independent complex D/E.

This is disjoint from the earlier same-isolate families (H-degree0). The original four-core cancellation and48-axis family proofs remain separate candidates with their original pins. These counts are second-core tables, not new scientific problems or executed cases.

The all-P off-axis orientation is still incomplete: remaining rank2-leading supports with H degree0,1 or2 and actual rank7 require actual analysis. Neither a degenerate Hermitian norm span nor a leading singularity is a phase witness. All proofs here await their own actual reconstruction. No all-first-orientation, all-H0,100-ray, unrestricted QLS10, novelty or formal/kernel claim is made; full primary UNKNOWN and no scientific execution permission inferred.
