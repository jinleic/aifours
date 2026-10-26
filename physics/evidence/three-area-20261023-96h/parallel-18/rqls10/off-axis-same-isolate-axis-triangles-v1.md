# Off-axis first profile: all48 same-isolate axis-triangle second cores v1

PhysicsRQLS10, same primary. Author-written CANDIDATE; no scientific executable, interpreter, solver, enumeration or CLI. Last actual working clock before this artifact:2026-10-24T04:41:07-07:00; no exact creation clock inferred. This is an additional family closure, not the all5040-second-core orientation theorem.

## 1. Fixed first and the exact family

First rho=(0,7,8,6,5,4,3,1,2), paired H,J,U,V and rank3 B0 are exactly those in `off-axis-first-blocks-and-scope-v1.md`. In particular first A0_JU=A0_JV=1,A0_UV=2 and H is isolated. Use the exact nonsymmetric block formulas from the prior packet, with this actual rank3 B0, not the old first rank1 profile.

The second Q1 is an **axis triangle with isolate H**: its three parallel vertices are J,U,V, all off-diagonal magnitudes2. Its distinguished parallel K can be any of J,U,V. Axis second cores have24 literal choices per sign class at fixed isolate: three choices K, four parallel sign patterns modulo global reversal, two independent horizontal/mixed signs. Positive and negative families therefore total48. Every one is a genuine PC P^T table.

If A1_UV=+2, all three entries of the leading L=A0+A1 triangle are nonzero: U-V becomes4, while J-U/J-V are1±2 and cannot vanish modulo7. Thus leading rank>=3, actual rank M>=8 and the general all-complex-phase norm theorem closes these cases. Only A1_UV=-2 needs the calculations below.

## 2. Positive axis triangles: a second-order scalar with the actual rank3 B0

Positive cycle product forces A1_JU=a,A1_JV=-a with a=±2. Thus L has J-leaf weights3,-1 in some order and no U-V edge. Its radical contains v with leaf coordinates(1,3) or(3,1), zero on H,J.

The first block is not frozen away: v^T v=10 and |O0 v|²=42, so

    (B0v)^T G_E(B0v)/2=90-42=48.

For the second positive-axis O1, the same v has |O1v|²=90 and hence B1v=0 exactly. The direct v-v curvature is0: first E0_UV=0, second E1_UV=0 because its only even off-diagonal pair edge is H-K, and the matching positive leaf tags make diagonal products cancel. The direct skew mixed products vanish in any v-v quadratic form.

Let A^(0) be the universal invertible even block of N. For any regular Q mixed column h,

    h^T G_E A^(0)^-1 h=-h^T G_E h/2-7h0²/16.

The actual second Schur coefficient on v is therefore

    -(B0v)^T G_E A^(0)^-1(B0v)/128
        =+48/128=3/8 (mod s),

nonzero modulo7. This supplies an additional odd pivot after the leading rank2 pair and proves actual rank M>=8, uniformly for every K, mixed sign and arbitrary complex compatibility phase.

## 3. Negative axis triangles: correct radical and mixed entries

Negative cycle product forces

    A1_JU=A1_JV=a, a=±2, A1_UV=-2.

The leading L is the star at J with equal leaf weights c0=1+a, either3 or-1, so it has rank2. Let v=e_U-e_V. Both Q mixed blocks kill v: B0 has equal U,V columns and B1 has only the H column. The full odd curvature kills v on BOTH sides. To see this directly, E0 o O1 contributes equal J-U/J-V weights; O0 o E1 has no such edge because the second even off-diagonal edge is H-K and first O0 has isolate H. The direct skew mixed terms are supported only on H-J, since the first mixed H-row is nonzero only at J. Thus D(s)v=v^T D(s)=0 exactly.

Write the second mixed block B1=b1 e_H^T. It has fixed row0, value0 at H and at the distinguished K, and opposite±2 at the other two parallels. Its fixed-row pair means f_a are-1 at H,K and+1 at the other two parallels, because this is a negative axis core.

The exact curvature on v has

    r=B^(2)v=r0*e0+rH*e_H,
    l=v^T C^(2)=l0*e0^T,
    r0=-(f_U-f_V)/4,
    rH=-(b1_U-b1_V)/16,
    l0=-(f_U-f_V)/8=r0/2.                        (1)

All other pair components cancel by the actual first rank3 mixed table. For example the first U,V fixed differences are both2; the fixed EO coefficient is-(f_a*2)/8. The fixed OE coefficient is-(f_a*2)/16, giving the separate norm1/norm2 factor. In the pair formula the only surviving EO row is H, from O0_HH=-1 and the second mixed H-row of its transpose. These details are not the old profile's pure-fixed-coordinate curvature.

## 4. K=J: a literal common reflection gives an invertible fixed block

The negative-axis second grid's x-reflection fixes its distinguished parallel J endpoints pointwise, swaps horizontal H endpoints, and interchanges its equally oriented heavy parallels U,V. This is exactly the first literal x-reflection g, since critical A1_UV=-2 means the physical U,V orientations agree in that source grid. Therefore it preserves both cores and commutes with rho; M commutes with g.

The g-fixed subspace has dimension6, with reduced N-rank4. Its reduced kernel is spanned by J-odd and U-odd+V-odd. The leading L on that two-space is

    [0 2c0; c0 0], c0=1+a∈{3,-1},

invertible modulo7. Thus the actual M on Fix(g) is invertible. Averaging an arbitrary phase delta over g preserves its nonzero fixed coordinate0 and would give a vector in that zero kernel: contradiction. No other averaged entry needs modulus1.

## 5. K=U orV: a nonzero fourth-order scalar

Now f_U-f_V=±2, so r0=±1/2 and l0=r0/2. Exactly one of b1_U,b1_V is0 and the other±2, giving rH=±1/8. The universal inverse has

    (A^(0)^-1 e0)_0=-3/4,
    (A^(0)^-1 e_H)_0=1/4.

Since both first mixed radical couplings vanish and D kills v, the exact self-Schur entry is-s^4*l*A(s)^-1*r. Its leading coefficient is

    -l0*(-3r0+rH)/4
       =-r0*(-3r0+rH)/8.                         (2)

It is nonzero modulo7: r0=±1/2 is a unit and(-3r0+rH) is one of±11/8,±13/8, all nonzero there. The values rH=±1/8 cannot be silently dropped or replaced by the old pure-e0 profile.

Every cross entry from v to the leading odd pivot space starts at s3, because its mixed coupling is s² and the other side is at least s. Feedback through an order-s odd inverse starts at s5, later than the nonzero s4 scalar(2). Hence one additional actual pivot survives, rank M>=8, and all complex phase vectors are excluded. The two sign freedoms in(1) were kept independent, so no special physical phases were fixed to obtain the scalar.

## 6. Scope and next remainder

This closes every positive/negative axis triangle with second isolate H:48 literal second cores, including all mixed signs and all distinguished-parallel roles. The count is not an executed enumeration and does not multiply primary problems. These are disjoint from the four off-axis A1=-A0 cores in the separate family packet.

The new first orientation remains genuinely uncovered by the old accepted symmetry union; this lemma does not replace it with the old axial first core. The remaining second cores with rank2 leading L and actual rank7 still need actual phase analysis. Every result here is a written candidate pending its own actual reconstruction; no all-P orientation, global H0, unrestricted QLS10, novelty or formal/kernel verdict follows.
