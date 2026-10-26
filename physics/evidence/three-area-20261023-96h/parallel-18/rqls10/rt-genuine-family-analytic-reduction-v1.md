# One analytic RT family dossier: genuine symbolic sources, new uniform obstructions, and the exact gaps

**PhysicsRQLS10 / physics-5.** Actual pre-write `/bin/date`: **Sun Oct 25 05:06:17 PDT 2026**. **WRITTEN CANDIDATE, PARTIAL: this is NOT a full RT proof.** No scientific eval, arithmetic interpreter, symbolic program, enumeration, finite-certificate replay or solver was used. Only written algebra/source reconstruction and metadata hashes/clocks. All earlier pinned files remain unchanged.

This is ONE consolidated analytic successor. It neither generates another per-core certificate table nor uses the earlier236/52 output identities as premises. It gives genuine symbolic representatives for every R0/R1/R2 source type; proves new uniform subfamily obstructions; and isolates the unproved parameter/phase steps. The generic Hermitian dual equivalence is NOT counted as closing RT.

## 1. Fixed literal data and named imports

Let s=i sqrt(7), K=Q(s), and label the F3-by-F3 grid by x+3y. Write

    q(z,w)=0 if z=w,
           +1 for distinct points sharing a grid row or column,
           -1 otherwise;
    Q0(i,j)=q(i,j), C=(J-I+sQ0)/sqrt(8),
    rho=(0,7,8,6,5,4,3,1,2),
    H=(4,5), J=(3,6), U=(1,7), V=(2,8).

The exact convention is physical row i, phase-coordinate column t:

    M_it=conjugate(C_ti)*C'_(t,rho(i)),
    (M delta)_i=sum_t M_it delta_t.

All nine coordinates of delta remain arbitrary complex unit phases, retaining independent arbitrary D/E. Endpoint orientation signs introduced below choose a literal permutation of the source POINTS, not an alphabet restriction on delta.

The following shared statements are imports from the consolidated manuscript and its now-integrated v28-A written boundary:

- The genuine source-grid shape catalogue and leading split, with the mandatory tag correction.
- Reduction of M modulo(s) has the same kernel as N=J-I-P_rho+Fix(rho): every reduced kernel vector has coordinate0 zero and every rho-pair sum zero.
- Five even unit pivots and r leading odd pivots give rank_K M>=5+r. Exact rank>=8 excludes all complex torus vectors by the fixed-point projective-K descent.
- For the actual nonsymmetric blocks, on a leading radical,

      S2=D2+(B1+B0)^T G_E N_E^(-1)(B1-B0)/128,
      y^T(feedback)y=(|O1 y|²-|O0 y|²)/128,
      16D2=E0 o O1-O0 o E1+B0 o B1^T-B0^T o B1.

  On pair rows the metrics are G_E=diag(1,2,2,2,2), G_O=2I. Products marked o are entrywise. Fixed-coordinate terms retain their separate formulas.

The first matrices used below are the actual ones, not a rank-one substitute:

    A0=[0 0 0 0; 0 0 1 1; 0 1 0 2; 0 1 2 0], O0=-I+A0;
    E0=[0 -2 2 0 0; -1 1 0 0 0; 1 0 1 -1 -1;
        0 0 -1 1 0; 0 0 -1 0 1];
    B0=[0 0 2 2; 0 2 0 0; 0 0 -1 -1;
        2 -1 0 0; -2 -1 0 0].

Only the old geometric source representatives are used from the central-rho papers. Their different-first-profile phase exclusions and any negative-core phase duality are NOT imported. Parent `wave-v28-v29-parent-written-dispositions-v1.md` supports the new shared/star/matching scope but explicitly leaves the RT finite data and all-P conclusion unaccepted. This note preserves that boundary.

## 2. New uniform lemma: one free physical pair suffices for ramified descent

For a rho pair a=(r_a,rho(r_a)), let e_a denote its literal physical odd vector: +1 at r_a, −1 at rho(r_a), zero elsewhere.

**One-free-pair lemma.** If rank_K M=7 and M e_a=0, then ker_C M contains no coordinate-unit vector. Here M is the actual literal coefficient matrix with the reduction described in Section1.

**Proof.** Suppose delta is a torus vector in its two-dimensional complex kernel. Subtract its odd part on this pair:

    omega=delta-[(delta_(r_a)-delta_(rho(r_a)))/2] e_a.

Then omega remains in ker M, its a-pair entries are equal, and every other physical coordinate is unchanged, including the nonzero unit coordinate0. The equal-pair hyperplane meets the K-defined two-dimensional kernel in a ONE-dimensional K-defined space: the pair-difference functional is nonzero on e_a. Therefore omega is a common complex scalar times a K-vector v. This is a conclusion about the averaged vector only; the original delta has not been assumed projectively K-valued.

Clear denominators so all v_j=A_j+B_j s have integer coefficients. All coordinates outside pair a have a common positive integer norm c, because the corresponding omega coordinates have modulus one. The two omitted coordinates need not have that norm, but they are EQUAL.

If7 divides c, the norm equation A_j²+7B_j²=c makes every retained A_j divisible by7. The reduced kernel equation also makes the omitted equal pair sum zero, hence 2A_(r_a)=0 modulo7, so its real coefficient is divisible by7 too. Thus EVERY A_j is divisible by7 and division by s gives another integral kernel vector, since

    (A+B s)/s = B-(A/7)s.

The omitted pair stays equal and the common retained norm decreases to c/7. Repeat until that common positive integer is not divisible by7. But the reduced fixed-coordinate equation forces A0 divisible by7, making that retained coordinate's norm divisible by7, contradiction. QED.

This is not a claim that all rank-seven kernels descend, or that a partial average remains a torus vector. It uses precisely the equal omitted pair and the preserved unit coordinates. It is a closed symbolic argument, not a finite replay.

## 3. Genuine R0 normal form and analytic reduction

### 3.1 Source geometry and notation

A positive off-axis211 triangle with isolated H is, up to source grid coordinate signs/interchange, the matching

    H: ((1,1),(-1,1)),
    J: ((0,1),(0,-1)),
    U: ((1,0),(1,-1)),
    V: ((-1,0),(-1,-1)).                         (O)

The last three are parallel rook edges, with distinguished direction J and heavy edge U-V. This is exactly the first physical matching on the fixed grid. Any genuine same-isolate off-axis211 source is obtained by permuting J/U/V, orienting each of the four pairs independently, and optionally negating the source character matrix. This follows from the four-rook geometric classification: the unique transverse edge is in a nonzero row; normalizing that row and the two column signs gives(O). The negative class is the same literal source catalogue under nonsquare multiplication, not a phase-preserving duality argument.

For an explicit genuine realization of negation, multiplication by 1+alpha on F9 is

    (x,y) -> (x-y,x+y).

Its character is −1, so applying it to all source labels replaces q by −q. Consequently every sign epsilon=±1 below is realized by an actual point permutation fixing0.

Let S_a flip endpoints within physical pair a, and S_A be the product for a subset of pairs. Let T be a signed pair permutation fixing H as a pair and permuting J/U/V. Write

    Q1=epsilon*T Q0 T^T.

Its endpoint signs are sigma_H=h and sigma_J,sigma_U,sigma_V in {±1}. Its distinguished second-triangle vertex is K. Every R0 input is represented this way. The leading filter is exact: at least one first-triangle edge cancels, but not all three. No uniqueness or census of these representatives is needed.

The literal first-grid reflection g:(x,y)->(−x,y) preserves Q0 and commutes with rho. It swaps U,V and flips H's endpoints. It transports whole phase vectors and all equations; it never imposes g-invariance on a proposed phase vector.

### 3.2 Same distinguished vertex K=J: free-pair closures

Here T flips endpoints only. Thus E1=epsilon E0 and B1=epsilon B0 diag(sigma). Three uniform identities apply.

**Positive source with h=+1.** The two columns of M at the endpoints of H are identical, so M e_H=0. This can be seen directly: against J the H cross-block rows of C are equal, and against U/V its columns are equal; with H endpoints fixed in the second source, the two literal products agree. The fixed row products also agree, and both masked entries in H rows are zero. The one-free-pair lemma excludes every such rank-seven input.

**Negative source with h=−1.** Again M e_H=0, now for a different reason. Put R=rho T. Since T is an involution commuting with rho and C'=T conjugate(C) T,

    R M T=M, hence M T=R M.                       (I)

The input T-odd vector e_H can map only to the R-odd output space. On a pair b not flipped by T, its odd coefficient is, up to the harmless ordered-pair sign, the conjugate two-by-two determinant of the C cross-block between b and H. ALL those determinants vanish: the H-J block has equal rows, and H-U/H-V have equal columns. There is no fixed-coordinate component in an R-odd vector. Therefore M e_H=0 exactly, and the lemma applies.

**Positive source flipping exactly three pairs.** Let a be the sole unflipped pair, so T=rho S_a. For either endpoint t of a and every row i outside a,

    C'_(t,rho(i))=C_(t,i),

hence both M columns equal1 there; they are both zero in a rows. Thus M e_a=0 and the lemma applies. This holds for any choice of unflipped pair, not just H.

### 3.3 Reflection identities closing the common endpoint patterns

Write u=(−3+s)/4, v=(−3−s)/4, so uv=1 and u+v=−3/2. The following are direct row identities of the actual literal M; no actual kernel table is used.

For a g-fixed vector use physical coordinates

    (delta0,delta1=delta2,delta3,delta4=delta5,delta6,delta7=delta8)
      =(x,y,z,w,t,f).

Averaging any proposed phase vector over g preserves coordinates0,3,6. The other four means are NOT assumed unit.

**Positive T=S_J with optional H flip.** Let h=+1 or−1 and T act by endpoint signs `(h,-1,+1,+1)`. Put A=(1+7h)/4 and B=(1−7h)/4. The distinct g-fixed row equations are

    2y+z+2w+t+2f=0,
    x+2y+2w+2f=0,
    v x+v y+u z+A w+t+u f=0,
    u x+u y+z+A w+v t+v f=0,
    x+B(y+f)+v z+u t=0.

Set Y=y+f. The first two give t=x−z and w=−x/2−Y. Adding the third and fourth, and using the fifth, gives

    (5+7h)x+7(1+3h)Y=0,
    Y=−(2+h)x/7,
    z=[1/2−(12+13h)s/98]x.                       (R+)

The squared modulus of this last coefficient is

    1/4+(12+13h)^2/1372 < 1,

because the possible squares are at most625, smaller than1029. But x and z are BOTH unchanged unit physical coordinates of the averaged phase vector. Contradiction. This closes in particular the positive two-pair flip S_H S_J without using the earlier computed exceptional kernel.

**Negative T=S_J.** The g-fixed equations force w=f and z=t. The remaining equations reduce to

    v x+2u y−3w=0,
    x+y+(1+u)z−w/2=0,
    u x+2y+2z+2w=0,
    v(y+z)+2u w=0.

The last three give

    x=(4u−2v)w,
    z=−9(1+v/2)w,
    y=(17/4−3u/2)w.

Substitution in the first gives `(3/2+10u)w=0`. Its coefficient is nonzero because u is not rational. All six g-fixed coordinates vanish. Thus averaging preserves a nonzero coordinate0 but would land in the zero kernel, impossible.

**Negative T=S_U S_V.** Here the g-fixed equations first give y=f and then

    4y+v(z+t)+2u w=0,
    v x+2(1+u)y+2w=0,
    v x+2y+u(z+t)+(u+v)w=0,
    u x+2y+u z+v t+(u+v)w=0,
    u x+4y+v z+u t=0.

The third minus fourth gives t=x. Combining the first and fifth gives `2u w=(2u−v)x`; combining the second and third gives `u x=15w`. Hence

    (2u^2−30u+15v)x=0,
    (96u+49)x=0.

Again the coefficient is nonzero. Therefore x=0 (indeed every g-fixed coordinate is zero), excluding a phase vector. No transpose-torus equivalence was assumed in either negative argument.

### 3.4 Different distinguished vertex K: uniform curvature and an involution closure

By g-transport it suffices to take K=U and let pi swap J,U in the source matching(O). Then

    E1=epsilon*P_E^T E0 P_E,
    B1=epsilon*P_E^T B0 P_O diag(sigma).

Here P_E/P_O are the same literal pair swap in the even/odd frames. The only cancellable first edge is J-U, so

    epsilon*sigma_J*sigma_U=−1.

Put t=epsilon*sigma_J*sigma_V and

    a=1+2t, b=2−epsilon*t,
    y=b e_J−a e_U.

The leading radical is span(e_H,y). On it A1 y=−A0 y exactly. Since D1=epsilon I,

    |O1 y|²−|O0 y|²=−4ab(1+epsilon).

The symmetric direct scalar is `−ab(1+epsilon)/8`; the feedback scalar is `−ab(1+epsilon)/32`. Thus

    y^T S2 y=−5ab(1+epsilon)/32 modulo(s).        (C1)

For epsilon=+1, a and b are7-units, so(C1) is nonzero and gives actual rank at least eight. This excludes EVERY positive R0 source with K different from J, independently of all endpoint signs.

For epsilon=−1, set tau=sigma_J=sigma_U. The symmetric form on the radical vanishes, but its actual nonsymmetric cross coefficient is

    e_H^T S2 y
      =epsilon*[(17b+a)h+17a sigma_U+b sigma_J]/64
      =−[(35+19t)h+(19+35t)tau]/64
      =−5(th+tau)/64 modulo(s).                  (C2)

For transparency, the direct term before combination is `epsilon*(b h+a sigma_U)/4`; the feedback term is `epsilon*[a(h+sigma_U)+b(sigma_J+h)]/64`. The latter follows by applying the actual even inverse to `(B1+B0)e_H`, whose fixed component is zero. Its pair dot product with `(B1−B0)y` is `−2epsilon*[a(h+sigma_U)+b(sigma_J+h)]`. These formulas use the full B0, not an arbitrary mixed-block ansatz.

If h differs from −t tau, (C2) is nonzero and supplies an additional genuine pivot, excluding actual rank seven. In the remaining branch

    h=−t tau=sigma_V,

the full source permutation is an INVOLUTION T: it swaps J,U with common orientation tau and fixes H,V as pairs, orienting both by h. Therefore identity(I) still holds.

If h=−1, T has four physical transpositions while rho T has two. Its T-odd input space has dimension four and its (rho T)-odd output space dimension two. Thus M has at least a two-dimensional kernel inside the T-odd space. Under the actual RT rank-seven hypothesis its entire kernel is exactly that two-dimensional space, which has coordinate0 zero because T fixes0. This excludes this WHOLE branch, for both tau signs, without constructing any kernel basis.

If h=+1 the dimension argument reverses and does NOT exclude phases. That remaining parameter step is retained below, not declared solved by a zero curvature coefficient.

### 3.5 Exact still-unproved R0 representatives after these written lemmas

Up to the legitimate first g-transport, the R0 phase step is not yet proved for the following symbolic sources:

- **P:** `Q1=(S_H S_U) Q0 (S_H S_U)`; the S_H S_V partner is its g-image.
- **N1:** `Q1=−S_U Q0 S_U`; include the g-image S_V.
- **N2:** `Q1=−(S_J S_U) Q0 (S_J S_U)`; include the g-image S_J S_V.
- **N3(tau):** `Q1=−T_tau Q0 T_tau`, tau=±1, where T_tau fixes the ordered H,V endpoints and swaps the ordered J,U pairs with common endpoint sign tau; also include the g-transport to distinguished vertex V.

These are unproved parameter/phase obligations, NOT asserted feasible cores, actual rank-seven certificates or norm-span-three examples. For each, retain the hypotheses actual rank_K M=7 and norm-span<=3 if invoking RT in its original form. The exact missing step is to exclude its FULL complex right-kernel torus, or prove one of those actual-rank/norm-span hypotheses impossible, by a closed identity. No old per-core list is used to decide which alternative occurs.

To see the reduction is exhaustive for K=J, note that positive leading cancellation means the JUV endpoint signs are not all equal. If H is fixed, use the free-pair lemma; if three pairs flip, use its third positive identity. The remaining positive two-pair flips are S_H times one JUV flip: S_H S_J is(R+), while S_H S_U/V is P. For negative K=J, H-flipped inputs use the negative free-pair identity. With H fixed, the nonconstant JUV signs give single or double B flips: S_J and S_U S_V are handled above, while the other two g-types are N1/N2. For K different from J, (C1)/(C2) and the involution argument leave precisely N3(tau). This is symbolic case logic, not an executed census.

## 4. Genuine R1 family: explicit paw sources and exact remaining sign step

The genuine paw source has three rook pairs and one diagonal pair, or its negative. Source coordinate signs/interchange normalize it to one of the following TWO symbolic raw matchings, indexed by u=0 or1:

    Pendant P: ((0,1),(1,1)),
    Hub D:     ((0,-1),(-1,u)),
    Leaf A:    ((1,0),(1,-1)),
    Leaf B:    ((-1,v),(-1,w)), {v,w}=F3 without{u}.    (P_u)

Fix (v,w)=(1,-1) for u=0 and (v,w)=(0,-1) for u=1; reversal is included by the independent endpoint signs. The four pairs cover all eight nonzero points. The three-pair source geometry proves exhaustion: the horizontal rook and diagonal pair both use column0; their remaining endpoints use opposite nonzero columns; the diagonal's second row level is0 or1 after normalizing the horizontal row to1.

The pendant-to-hub edge is unit. For u=0 the heavy edge joins hub D to leaf A and the A-B edge is unit; for u=1 the heavy edge is A-B. These assertions follow directly from the y-roots: A has root e0−e_(−1); at u=0 D has its negative, while at u=1 B has that same root. The endpoint-independent A-B source signs in the displayed orders are positive.

For R1 put physical H on P, physical hub k on D, and physical i,j on A,B in either order. Orient every pair independently by sigma and multiply the source character by epsilon=±1. The leading cancellation gives the exact retained possibilities:

- u=0: k is U or V, {i,j} the opposite first LIGHT edge;
- u=1: k is J, {i,j}={U,V}, the opposite first HEAVY edge;
- in either case, with the displayed source leaf orders, `epsilon*sigma_i*sigma_j=−1`.

Every sigma_H and sigma_k remains independent, as do the remaining endpoint signs subject to that single equation and every physical delta phase. These are all actual source tables; no arbitrary paw B1 is manufactured.

**Unproved R1 step:** for BOTH u strata, BOTH leaf assignments, every indicated hub and every retained epsilon/sigma choice, derive a uniform actual-rank obstruction or a diagonal norm-annihilator identity under rank_K M=7/norm-span<=3. No such uniform identity is supplied here. In particular the heavy-at-hub/light-cancellation u=0 branch is not discarded, and the whole R1 family is not claimed closed.

## 5. Genuine R2 family: source templates with no integer-determinant shortcut

All ordered pairs below may receive arbitrary physical pair labels and independent endpoint orientations. Normalize p(0)=0, take the resulting literal source q, and optionally negate q by the genuine nonsquare map above. Retain only assignments with H-degree two and the stated leading filter. These source normal forms are not numerical phase samples.

### 5.1 Triangle sources

Use the off-axis source(O), or the axis source

    I: ((1,0),(-1,0)),
    A: ((0,1),(0,-1)),
    B: ((1,1),(1,-1)),
    C: ((-1,1),(-1,-1)).                           (A222)

For R2 the isolated pair I is not H; H lies in the triangle. These exhaust the positive four-rook triangle shapes by the transverse-edge row0/nonzero-row split; their negatives cover the zero-rook counterparts.

### 5.2 Paw sources

Use(P_u) for both u, putting H on one of its degree-two leaves, not on the pendant or hub. Every raw heavy placement remains. Negation covers the one-rook counterparts.

### 5.3 Parallel diamonds

For exactly one of a,b equal to zero, with

    a in{0,-1}, b in{0,1},

take vertical rook pairs in columns1 and−1 omitting levels a and b respectively, together with

    D1: ((0,1),(1,a)),
    D2: ((0,-1),(-1,b)).                           (D_parallel)

The other two a/b alternatives give complete graphs, whose H-degree is three and so are not R2. Both mixed choices remain; their endpoint and label assignments are not collapsed.

### 5.4 Perpendicular diamond

A genuine normalized source is

    R1: ((0,1),(-1,1)),
    R2: ((1,1),(1,-1)),
    D1: ((1,0),(-1,-1)),
    D2: ((-1,0),(0,-1)).                           (D_perp)

Source coordinate interchange includes its dual placement. H must occupy an actual degree-two vertex. This is a source-grid symmetry, not a symmetry imposed on delta.

### 5.5 The three K2,2 templates

The central all-heavy source is the four opposite pairs

    ((1,0),(-1,0)), ((0,1),(0,-1)),
    ((1,1),(-1,-1)), ((1,-1),(-1,1)).              (K_central)

A weighted K2,2 with a heavy ROOK vertex has source

    ((1,0),(-1,0)), ((1,1),(1,-1)),
    ((0,1),(-1,-1)), ((0,-1),(-1,1)).              (K_A)

A weighted K2,2 with a heavy DIAGONAL vertex has source

    ((0,1),(-1,1)), ((1,0),(1,-1)),
    ((0,-1),(-1,0)), ((-1,-1),(1,1)).              (K_B)

All cover the eight nonzero cells exactly. The two-rook source geometry exhausts these perpendicular possibilities: either the two rook edges use row0/column0, exactly one does, or both are in nonzero levels. In the latter case disjointness forces one omitted intersection coordinate; both omitted yields K_B, one zero omitted yields D_perp, and the other alternatives leave three unpaired points in one line. The parallel possibilities are exactly Section5.3 and its complete-graph alternatives. Thus these templates, the triangles and paws cover every genuine H-degree-two source shape at the named catalogue import; no central-rho phase exclusion is transferred.

### 5.6 Exact retained parameter condition and unproved step

For any of these source assignments let i,j be H's neighbours and k its non-neighbour in B={J,U,V}. Compute the ACTUAL odd entries from the source endpoints, not an arbitrary graph:

    A1_ab=[Q1(r_a,r_b)-Q1(r_a,rho(r_b))
           -Q1(rho(r_a),r_b)+Q1(rho(r_a),rho(r_b))]/2.

The exact leading R2 predicate is

    A1_ij=−A0_ij,
    b_i=A1_Hi, b_j=A1_Hj,
    c_i=A0_ki+A1_ki, c_j=A0_kj+A1_kj,
    b_i*c_j-b_j*c_i=0 modulo7.

The determinant is NOT replaced by integer zero; nonzero multiples ±7 or ±14 remain if genuine. This filter retains the actual E1/B1/D1 automatically through its source coordinates.

**Unproved R2 step:** uniformly over every source template, label assignment, endpoint sign and epsilon surviving these explicit equations, exclude the full right-kernel torus under actual rank seven/norm-span<=3, or show those rank/norm hypotheses impossible. The templates specify the missing parameter problem completely; no such uniform phase or diagonal-dual proof is supplied here.

## 6. One precise remaining algebraic obligation, without a hidden finite replay

For every retained endpoint template let p be its literal point permutation, and put

    q1=epsilon*q(p(t),p(rho(i))), q0=q(t,i),
    B_it=4M_it=0 if t=i or t=rho(i),
    B_it=(1+7q0q1)/2+s(q1−q0)/2 otherwise.

This is a closed symbolic representative for the actual operator of every remaining R0/R1/R2 input. It is not another computed table.

A physical-dual route to closing one of the remaining families would need a CLOSED family expression lambda,Z with rational diagonal Lambda=diag(lambda),

    Lambda=M* Z+Z* M, trace(Lambda)!=0,

or an independently written rank/phase alternative covering all that family's parameters. The previously proved generic dual lift says how an established norm annihilator lifts; it does not produce lambda from these literal sources. That production/identity is the unproved load-bearing step for P/N1/N2/N3 and for the R1/R2 parameter regions above. No claim that such a dual exists is made for an arbitrary torus-empty matrix with a feasible affine norm relaxation.

Accordingly this packet supplies **new analytic subfamily theorems and an exact consolidated symbolic remainder**, not the full requested analytic RT theorem. It does not use a selected core as a substitute for the all-input quantifier, claim any remaining stratum feasible, or use the unadmitted finite list to label a parameter impossible. Independent reconstruction of the new written identities is still required.

## 7. Provenance and non-claims

Fresh metadata pins observed with the pre-write clock:

- Parent current disposition: `wave-v28-v29-parent-written-dispositions-v1.md`, SHA `5553f19e3f503764b02566536bfa3a079daa2d10b8d75b2c31246c57178a1f0a`.
- `rook-positive-pairs-closure-v1.md`, SHA `aa0c4966efa8009d4e8dcd7afb8c4a0f76498b1c492c93dedf55887babbfe743`, ONLY source geometry LF30–38.
- `rook-three-pairs-closure-v1.md`, SHA `3ca0eb7adb0de03cc0a5103fcab4fb11535766811ca5ae7abf7979022d3a86b4`, ONLY source geometry LF20–45.
- `rook-two-pairs-full-closure-v1.md`, SHA `71626e32c1d4b5fbc45a7e7ff89bcf65942aa27a940aa2c180d9d3f49871e734`, ONLY source geometry LF61–105.
- Actual off-axis shared matrices/Schur formulas: `off-axis-consolidated-orientation-v1.md`, SHA `9f1c469002abb6cc0c7bf5cb8bf9a7ca664773b6c4b70276516a565e6a3750c7`; mandatory current tag/curvature errata and original failure history preserved.

No old central-profile phase result is imported by geometric reuse. No new literal census, certificate table, scientific computation or GO is requested. Parent erratum v7 remains mandatory; earlier unadmitted outputs receive no executable-verification or retroactive-admission credit. RT, the whole fixed-profile all-P orientation claim and unrestricted maximal1-RQLS10 remain unaccepted/open at their stated distinct boundaries. No all-first-profile WLOG, all-conference-class, global100-ray, formal, human, cross-vendor or novelty claim follows.
