# Negative paw-star: fourth-order closure and the exact residual v1

PhysicsRQLS10, author-written CANDIDATE; no independent reconstruction or execution. This is the negative P branch left open by `axial-mixed-block-closures-v1.md`. It preserves every second P and every independent complex diagonal phase. No guessed creation clock is attached; last observed clock was2026-10-23T16:50:55-07:00.

## 1. Literal geometry and signs

First pair labels are H, b=V0, d=V1, e=V2. H is the first isolated odd vertex; the fixed first mixed column b0 has values+2 on d,-2 on e, and0 on H,b and the fixed coordinate.

In the second negative paw, H is the pendant; k is its hub; i,j are the heavy leaves. Define i geometrically as the vertical column also occupied by the horizontal H pair, and j as the other nonzero vertical column. This removes a sign ambiguity in the even means. One positive-grid representative, before negation, has

    H={(0,r),(a,r)},
    k={(0,-r),(b,r)},
    i={(a,0),(a,-r)},
    j={(b,0),(b,-r)},

where r=±1, a,b are the two distinct nonzero column labels. The negative-core odd entries are

    A1_Hk=p, A1_ki=A1_kj=a0, A1_ij=-2,

with p,a0=±1. The negative Q1 pair tags are-1 on H,i,j and+1 on k. Every pair mean of its fixed row is0. Its even pair off-diagonal entries are

    E1_Hk=-1, E1_Hi=0, E1_Hj=+2,
    E1_ki=+1, E1_kj=-1, E1_ij=0.

Let d0=±1 denote the chosen hub diagonal-root orientation, h=±1 the common heavy-leaf orientation, and e0=±1 the H horizontal orientation. Actual geometry enforces

    a0=h*d0,  p=-e0*d0.

The mixed block of the negative Q1 is exactly

    B1_H-column: fixed -2e0; pair k -e0, i 2e0, all others0;
    B1_k-column: fixed 0; pair H d0, i -d0, j +d0, k0;
    B1_i-column=B1_j-column: fixed -2h; pair k h, all others0.

These columns obey h_fixed+2sum(h_pair)=0. They are direct root/mean products, not numerical data.

## 2. Correcting the leaf radical inside the exact odd block

Put c=2+a0∈{1,3}, v=e_i-e_j. The leading odd L=A0+A1 is a star centred at k, with leaf weights p on H and c on both i,j. Its rank is2. The leading radical is two-dimensional.

The direct odd curvature D^(2) is also a star at k. Its symmetric H-k entry is n/16, with

    n=-2p if b=k, otherwise n=0;

its skew H-k coefficient is b0_k*d0/16; and its k-i,k-j entries are-2/16,+2/16. Thus D^(2)v=-(1/4)e_k on both sides; unlike off-axis T0, it would be false to assert that this curvature kills v.

Set q=b0_k*d0 and define local-ring units

    beta_R(s)=4s/[-2p+s(n+q)],
    beta_L(s)=4s/[-2p+s(n-q)].

The exact odd vectors

    v_R=v+beta_R(s)e_H,
    v_L^T=v^T+beta_L(s)e_H^T

satisfy D(s)v_R=0 and v_L^T D(s)=0. Both beta functions start-2p*s. This is an algebraic basis change, not a statement that phase vectors have this symmetry.

Write r=B^(2)v and l=v^T C^(2), using the operator blocks of the mixed-closure paper. A direct fixed-row/column calculation gives

    r_fixed=h*(eta_i-eta_j)/4,  r_pair=-(d0/4)e_k;
    l_fixed=-h*(eta_i-eta_j)/8, l_pair=+(d0/4)e_k^T,

where eta is the fixed first Q0 row's pair mean: eta_H=eta_b=+1, eta_d=eta_e=-1. In particular l=-(1/2)r^T G_E.

The corrected mixed couplings have leading terms

    B(s)v_R=s²*rhat+O(s³),
    v_L^T C(s)=s²*lhat+O(s³),
    rhat=r-(p/4)(B1_H-b0),
    lhat=l+(p/8)(B1_H+b0)^T G_E.

## 3. A scalar fourth-order certificate

Let x=r-(p/4)B1_H and y=(p/4)b0. Then

    rhat=x+y, lhat=-(1/2)(x-y)^T G_E.

Since p*e0=-d0, the entries simplify to

    x_fixed=xi=h*(eta_i-eta_j)/4-d0/2,
    x_pair=(d0/2)(e_i-e_k),
    y_fixed=0, y_pair=(p/4)b0_pair.

Both pair sums vanish; each pair squared norm is1/2. The explicit A^(0) inverse from the mixed-closure paper therefore gives

    x^T G_E A^(0)^-1 x=-3xi²/4-1/2,
    y^T G_E A^(0)^-1 y=-1/2.

Its self-adjointness cancels both cross terms. The leading corrected v-v Schur coefficient is consequently

    -lhat*A^(0)^-1*rhat=-3xi²/8.                   (1)

Eliminating the two leading odd pivots cannot alter this fourth-order coefficient: the corrected vectors kill D exactly, so each of their cross entries to those pivots starts at s³. The odd pivot inverse has order s^-1, and its correction thus starts at s^5, later than s^4. Hence any xi nonzero modulo7 supplies one additional pivot and actual rank M>=8, excluding every arbitrary complex phase vector.

Because h=a0*d0,

    xi=d0*[a0*(eta_i-eta_j)-2]/4.

The complete role disposition is:

- b=k: eta_i-eta_j=0, xi=-d0/2; all p and d0 close.
- b=i: eta_i-eta_j=2; a0=-1 gives xi=-d0, so closes. The a0=+1 cases remain.
- b=j: eta_i-eta_j=-2; a0=+1 gives xi=-d0, so closes. The a0=-1 cases remain.

No equality case has been silently declared no-go: when xi=0, certificate(1) is zero.

## 4. Exactly sixteen remaining literal cores in this branch

The negative paw has8 raw matching embeddings in a9-point rook grid, and384 literal fixed-point-zero cores after quotienting the eight point-stabilizer automorphisms. Requiring its pendant to be first H leaves96; requiring its heavy edge to be-2 leaves48. This can also be counted without the quotient: choose hub k among three first vertical labels; choose which of the other two vertical leaves is geometrically i (two choices); choose three independent pair-orientation signs e0,h,d0 (eight choices), giving48.

The residual xi=0 consists exactly of

    (b=i AND a0=+1) OR (b=j AND a0=-1),

with pendant p and diagonal-root sign d0 arbitrary. Each alternative has two possible hub labels and four(p,d0) choices:8+8=16. All other32 negative paw-star cores have been excluded by the nonzero scalar(1). This is a count of **literal unphased second cores**, not phase witnesses or QLS constructions.

A source-explicit way to generate the16 without searching is to choose b=i or b=j, choose k among the two first diagonals, let the other diagonal fill the other leaf, choose p,d0 independently, set a0=+1 or-1 respectively, h=a0*d0 and e0=-p*d0, and use the E/O/B/C blocks printed above. Each block specification reconstructs a unique genuine Q1: it is the negative of the displayed rook-grid geometry with those pair orientations. No execution has been used to produce a table.

## 5. What does not close them

Expanding the corrected odd Schur matrix one order further does not immediately repair the xi=0 case. In the b=i,a0=+1 branch, the nominal fifth-order diagonal term1/32 cancels the1/32 feedback from the two first-order odd pivots. Treating the diagonal term alone as a fifth-order certificate would therefore be wrong. This cancellation was found in written algebra and is a reason to retain the16 as unresolved, not claim completion.

The exact remaining obligation is to exclude or construct an arbitrary-unit complex kernel vector for these16 genuine cores (and, if one survives the zero conditions, to check the remaining cross-conference magnitudes and global QLS compatibility). A rank>=8 certificate would suffice; for a rank7 survivor, a complete diagonal Hermitian-norm reconstruction may suffice instead, but it has not yet been evaluated on these16. No old executable, scientific execution, phase alphabet restriction, or full axial/QLS10 conclusion is implied.
