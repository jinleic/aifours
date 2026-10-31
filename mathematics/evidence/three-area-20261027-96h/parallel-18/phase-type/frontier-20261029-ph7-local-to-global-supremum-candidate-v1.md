# PH7 local-to-global candidate: the attained supremum is the adopted algebraic z_*

**FULL-TARGET CANDIDATE — NOT_PROVED pending the exact GLOBAL certificate gate.** This is the ONE consolidated local-to-global packet, not a nearby-threshold variant of f180. MathResearch96h-2 / math-1. Native clock observed before writing: **Thu Oct 29 10:28:08 PDT 2026**. The new mathematical reductions are written below. Only the LOCAL stage has an exact certificate; all GLOBAL covers listed in Section 10 have closed only in floating arithmetic at one rational parameter center. No exact global checker has been launched. Independent hostile review, definition-first verification, hardening and parent executable GO are prerequisites to promotion. No formal/kernel, novelty, human or independent-model-family claim.

## 1. Quantified target, success and first unproved step

Let c,d>0, a=c+d, b>0, z=b²/d², and

    H(s)=c(a²+b²)² / [(s+c)((s+a)²+b²)²].

Let `(U,V,z_*)` be the ADOPTED f50 algebraic endpoint; its construction realizes H with seven states for every `7/9<=z<=z_*`, and `0.820420341<z_*<0.820420541`.

**Candidate theorem.** No PH representation with at most seven states exists for ANY `z>z_*`. Consequently the supremum of PH7-realizable ratios is EXACTLY z_*, and it is attained. This upper theorem is conditional on the adopted irreducibility caller and on the new lemmas and uniform certificate obligations below. It does not assume the PH-realizable set is downward closed. The already adopted construction supplies attainment, not a new construction above z_*.

Success means the whole quantified theorem above, with every finite-cover obligation below fully and independently exact-verified on the SAME frozen inputs, plus a parent disposition. Otherwise this packet remains NOT_PROVED. **First unproved step: exact uniform verification of the GLOBAL covers over J and the algebraic-dual parameter enclosures.** Fixed-center floating closure is not that verification.

## 2. Pinned mathematical inputs and exact parameter domain

Adopted context: f50 construction/root, f159/f160 symmetrization/coefficient lemmas and spectral shift, f180 no-PH<=7 for z>=83/100. They are used only at their stated same-harness scopes. No reviewer return outside those dispositions is a premise. New candidate input `frontier-20261029-ph7-joint-interlacing-y1-v1.md`, 90LF/6695B, SHA256 `0221e6c73440f921f127db0130038f8ab733fae65d5585f4227ba06b9fef8310`, supplies the joint y¹ bound; it is not adopted.

Exact LOCAL stage: `frontier-20261029-ph7-local-global-dual-check.py`, 180LF/9057B, SHA256 `cb2b9ede94c117ea44b6c100ee7dbfa4cb46d38531aea9de1bd3582892e085d8`, and `frontier-20261029-ph7-local-global-local-certificate-v1.json`, 188LF/15085B, SHA256 `8f5f9b85b1211c36114500fc61c1a35b23646e9e1cb65e6697fd0663d1b15fce`. They refine the SAME adopted root to the radius `r=10^-16` box centered at

    U0=334696976789746519/250000000000000000,
    V0=208405938226799943/200000000000000000,
    z0=410210220392063003/500000000000000000.

A rational preconditioned contraction maps that box into itself, has norm<10^-8, and the box lies inside the adopted old uniqueness box, so its root is the same `(U,V,z_*)`. Root existence/uniqueness in the original box is an adopted import. The certificate stores the exact interval enclosures `I_a,I_b` for the two algebraic dual constants defined in Section 5.

**Frozen prospective GLOBAL parameter domain:**

    epsilon=r=10^-16,
    J=[z0-r,z0+r+epsilon],     a_dual in I_a, b_dual in I_b.

Every GLOBAL sign obligation is UNIFORM on J (and independently on I_a,I_b when dual constants occur), not sampled at z0. The actual application is `z_*<=z<=z_*+epsilon`, a subset of J. The LOCAL proof uses the linked algebraic constants at the root, not arbitrary independent interval values. All root/dual enclosures are rational exact data in the local certificate; no decimal approximation substitutes for them.

## 3. Spectral reduction and full canonical definitions

For z>1/2 the adopted caller gives exactly seven states and an irreducible Metzler `G=(T+cI)/d` with s(G)=0 and

    det(yI-G)=y((y+1)²+z)²(y²+py+q),    p,q>0.

Geometric symmetrization S has `S_ii=G_ii`, `S_ij=sqrt(G_ij G_ji)`. The adopted strict Perron argument makes `𝒜=-S` positive definite because G is irreducible, s(G)=0 and has a nonreal eigenvalue. Write its eigenvalues `0<v1<=...<=v7`, elementary sums e_k, and set

    p=e1-4, q=e2-4e1+10-2z,
    W=e3-4e2+(10-2z)e1+12z-20,
    E3=e4-(6+2z)e2+(20+4z)e1+3z²+6z-45,
    E2=e5-(1+z)²p-(4+4z)q, E1=e6-(1+z)²q,
    s=v1+v2, S3=v1+v2+v3, S4=v1+v2+v3+v4, L4=v4+v5+v6+v7,
    K=E3-S4*W,
    Y2=E2-W*e2(v1,v2,v3,v4)-S3*(E3-W*L4),
    alpha=e3(v1,v2,v3,v4)-s*e2(v4,v5,v6,v7), B_joint=v1*v2-s²,
    Z=E1-s*E2, Y_joint=Z-W*alpha-K*B_joint+W²/2.

Every realization has `W>=0,K>=0,Y2>=0,Y_joint>=0`. The first three are adopted coefficient/interlacing relations. The last is the new joint lemma: for a three-state principal minor with ordered eigenvalues nu_i>=v_i, `e2(nu)-s*sum(nu)>=v1*v2-s²` because its coordinate derivatives are nonnegative; hence the four-cycle contribution is bounded jointly, not by incompatible separate extrema. The pair of disjoint extra three-cycles contributes at most W²/2 to the y¹ coefficient. These facts give the displayed Y_joint by collecting the y¹ minus s times y² coefficients.

For x=v7 and f_k the elementary sums of the six others define

    A=f2-4f1+10-2z, B=f3-4f2+(10-2z)f1+12z-20,
    h1=f3-(6+2z)f1+20+4z,
    h0=f4-(6+2z)f2+(20+4z)f1+3z²+6z-45,
    D=h1-A*S4, E=h0-B*S4,
    Q=A²-(f1-4)*B, Hpol=-(h0*A-h1*B).

Thus `q=A+(f1-4)x`, `W=Ax+B`, `K=E+Dx`, and `EA-BD=h0*A-h1*B`. Q and Hpol are UNSCALED here; certificate integerization may multiply them only by positive constants.

## 4. New y⁰ necessary inequality and adaptive cubic selector

Extra cycles in the adopted cover identity have nonnegative weights omega. Let Wj be the sum of length-j extra-cycle weights. Its constant coefficient, using det(-G)=0, gives

    e7 = a4+b3+c2+d1+W7-P33v-P34.

Here a4 sums `omega*det(𝒜_U)` over length3 cycles (|U|=4), b3 sums the analogous determinant over length4 cycles (|U|=3), c2,d1 are the corresponding nonnegative terms for lengths5,6. Pair terms are unordered disjoint 3+3 cycles times the remaining diagonal entry, and disjoint 3+4 cycles, respectively. Interlacing gives `a4>=W*e4(v1..v4)`, `b3>=W4*v1*v2*v3`; the remaining diagonal is at most v7, so `P33v<=W²*v7/2`, and `P34<=W*W4`. Therefore, with `g=v1*v2*v3-W`,

    base:=e7-W*e4(v1..v4)+W²*x/2 >= W4*g.

Also `W4>=max(0,E3-W*L4)`. Whenever g>=0,

    Y0:=base-g*(E3-W*L4)>=0.                                      (C0)

For fixed six rates Y0 is a cubic in x,

    Y0(x)=c0+c1*x+c2*x²+c3*x³,      c3=-A²/2,
    g(x)=g0-A*x, g0=v1*v2*v3-B.                                  (C1)

The leading-coefficient identity was exactly expanded in the owner kernel; the other reasoning is written, unreviewed. In case A<0, if a rational anchor t satisfies `0<=t<=x`, `g(t)>0`, `Y0(t)<0`, `Y0'(t)<=0`, `Y0''(t)<=0`, then g stays positive and the strictly negative third derivative makes Y0(x)<0 for every x>=t, contradicting (C0). This is a uniform tail argument, not a check of one selected instance.

## 5. Algebraic dual and exact LOCAL stage

Evaluate W,E3,Z at `(v,v,u,u,u,u,u)` to obtain Wg,Eg,Zg. At `(U,V,z_*)`, choose CONSTANTS a_dual,b_dual solving

    [Wg_u Eg_u; Wg_v Eg_v] [a_dual;b_dual]=-[Zg_u;Zg_v].           (D0)

The exact local checker bounds this determinant away from zero. Define

    F(v,z)=Z+a_dual*W+b_dual*E3-E3²,
    lambda=a_dual+alpha+b_dual*S4-W/2-S4*E3,
    mu=b_dual+B_joint-E3.

The exact identity is `F=Y_joint+lambda*W+mu*K`. The root equations give `F(v_*,z_*)=0`, `grad_v F(v_*,z_*)=0`, with `v_*=(V,V,U,U,U,U,U)`; grouped stationarity implies all seven derivatives vanish by within-block symmetry. This is exact, not a small numerical residual.

The exact LOCAL certificate proves lambda,mu>0, partial_z F<0 and strict negative definiteness of Hessian_v F on a rational superset of

    |v1,2-V|<=rho, |v3..7-U|<=rho, z in [z_*,z_*+rho], rho=1/500.

It uses centered exact derivative polynomials, a rational upper-unit-triangular congruence, and strict interval diagonal dominance (minimum margin>3). Consequently `F(v,z_*)<=0` in this spectral box, with equality only at v_*, and `F(v,z)<0` there whenever z>z_*. This local inequality holds without assuming spectral feasibility at the comparison point. This is the ONLY already exact-checked stage of the prospective global proof.

## 6. New blockwise Schur-barrier reduction to two variables

Use the fixed rational box

    B7=[1,11/10]² x [127/100,29/20]^5.

F is symmetric within the first2 and within the last5 coordinates. Put `c=s*(4+4z)-(1+z)²`. For i,j in the SAME block, with elementary sums e'_k of the five coordinates excluding i,j, differentiation gives

    F_i-F_j=-(v_i-v_j)*Phi_ij,
    Phi_ij=e'_4-s*e'_3+(b_dual-2E3)*e'_2+a_dual*e'_1
           +c-4a_dual-(6+2z)*(b_dual-2E3).                        (S)

**Uniform barrier obligation SB:** throughout B7 and the parameter domain, either `F<0`, or BOTH `Phi_12>0` and `Phi_34>0`. By within-block permutation invariance this implies every same-block Phi_ij is positive wherever F>=0.

If SB holds, any point of B7 with F>=0 can be continuously averaged within each block without decreasing F: along `v_i(t)=mean+exp(-t)*(v_i(0)-mean)`,

    dF/dt=(1/m)*sum_{i<j in block} Phi_ij*(v_i-v_j)²>=0.

As long as F>=0 the derivative is strictly positive unless that block is already constant, so a first exit into F<0 is impossible. The path stays in B7. Its limit is the grouped spectrum `(vbar,vbar,ubar,ubar,ubar,ubar,ubar)`, where `vbar in[1,11/10]`, `ubar in[127/100,29/20]`; its F value is at least the original one, strictly greater if the original spectrum was not block-constant.

**Uniform mean-plane obligation MP:** cover that two-dimensional rectangle by cells on which `F_group<0`, or cells contained in the rational INNER local rectangle

    |ubar-U0|<=rho-r, |vbar-V0|<=rho-r.

For the latter cells the exact LOCAL stage applies to the actual root and actual z>=z_* (not to arbitrary unlinked interval values). Thus MP implies `F_group<0` throughout the mean rectangle for z>z_*. With SB, **F>=0 is impossible anywhere in B7** for z>z_*. At z=z_*, only the exact grouped root can have F>=0. No assumption that W,K or Y_joint persist along averaging is needed; SB is conditional on F>=0 alone.

## 7. Six-rate case partition and critical-block routing

The following finite obligations cover every positive spectrum for every actual `z in(z_*,z_*+epsilon]`.

- Case(a), f1<4: p>0 gives x>4-f1, so `q<A-(4-f1)²<=6/7-2z-(7/12)(f1-24/7)²<0`, contradiction. All J has z>3/7.
- Case(b), f1>=4,A<=0: Q>0 is contradictory (if f1=4 then q=A<=0 already). **Outer obligation QO** proves Q>0 unless all six rates lie in `N6=[5/11,37/27]^6`. Inside N6, **NB** is the sorted cover of Section 8.
- Case(c), f1>=4,A>0,D<=0: `-Hpol=EA-BD=A*K-D*W>=0`, hence Hpol>0 is contradictory. **Outer obligation HO** proves Hpol>0 unless all six lie in `M6=[7/9,5/3]^6`. Inside M6, **MC** is the sorted cover below.
- Case(d), f1>=4,A>0,D>0: **Residual obligation R3** is the same three-parameter reduction as the adopted core, at every z in J. With y=alpha1, alpha2=(3/8)tau*y², beta1=y/2+gamma,

      Abar=alpha2-4y+10-2z+beta1*(y-4)+beta1²/4,
      Dbar=4y²-16y+20+4z-(5/6)y*alpha2+beta1*(alpha2-y²+4y-6-2z),
      f1=y+beta1.

  The elementary bounds give Abar>=A>0 and Dbar>=D>0, tau in[0,1], y,gamma>=0. R3 excludes the triple `Abar>0,Dbar>0,f1>=4`.

**MC leaf rules on sorted M6:** mA (A<0), D (D>0), H (Hpol>0), jointEnd, SchurBlock, or no sorted point. The first three contradict case(c). Write `Y_joint(x)=d2*x²+d1*x+d0`. jointEnd requires A>0,D<0,d2>0 and

    A²*Y_joint(-B/A)<0, D²*Y_joint(-E/D)<0.

W,K>=0 confine x to `[-B/A,-E/D]`; a convex quadratic negative at both ends is negative on that whole segment.

SchurBlock requires that v1,v2 in[1,11/10], v3..v6 in[127/100,29/20], A>0,D<0,

    -B-(127/100)A>=0,    -E-(29/20)D>=0,

so the WHOLE crude x interval lies in[127/100,29/20]. Both lambda(x) and mu(x) are linear in x. If L0,L1 and M0,M1 are their literal coefficients, require

    A*L0-B*L1>0, -D*L0+E*L1>0,
    A*M0-B*M1>0, -D*M0+E*M1>0.

These are their endpoint values with denominators cleared in the correct directions. Hence lambda,mu>0 on the crude interval; feasibility gives F>=0, while SB+MP exclude every such point of B7. This completes case(c), conditional on the exact covers.

## 8. Sorted small-q cover NB with correlation-preserving cubic tails

NB covers sorted N6 by: F (f1<4), A (A>0), Q (Q>0), E4v6, Y2v6, Disc, adaptiveY0, or no sorted point. These definitions are canonical:

- E4v6: A<0 and `A*v6+B<0`; then W(x)<0 for every x>=v6.
- Y2v6: A<0, Y2(v6)<0, Y2'(v6)<=0. Y2 is concave in x with leading coefficient `(v1+v2+v3)A`, so Y2(x)<0 for every x>=v6.
- Disc: A<0 and the discriminant of the quadratic Y2(x) is negative.
- adaptiveY0: A<0, Fm=f1-4>0, and one nonnegative rational anchor t<=x with the four cubic/g predicates of Section 4.

For a certificate cell in the affine N6 cube, put -A and Fm in a common degree-one tensor Bernstein basis. If all their coefficients are positive, define

    Lq=min_k [(-A)_k/Fm_k],
    Lv6=the cell's rational lower endpoint for v6,
    t=floor(1024*max(Lq,Lv6))/1024.

For any point in that cell, q(Lq)=A+Lq*Fm<=0 (all Bernstein coefficients <=0); since Fm>0 and actual q(x)>0, x>Lq. Also x>=v6>=Lv6, so t<=x. This is an analytic lower bound, not a numerical estimate.

Elevate the four c_i coefficient tensors of Y0(x) to the COMMON six-variable degree `(2,2,2,3,3,3)`. Combine these tensors POINTWISE at t to certify the upper signs of Y0(t),Y0'(t),Y0''(t), rather than summing separate extrema and losing correlations. Likewise g0 and -A share a common degree-one basis, so their pointwise sum at t certifies g(t)>0. The third derivative is exactly `-3A²<0`. These finite sign rules validate the adaptiveY0 leaf on the ENTIRE cell and all admissible x, not a sampled state.

## 9. Certificate conventions and global logical closure

Outer QO/HO use compactification `r_i=s_i/(1-s_i)`, multiply by `prod(1-s_i)^2`, and the familiar open-positive-orthant strictness rule. Excluded compactified cubes are `[5/16,37/64]^6` (QO, exactly N6) and `[7/16,5/8]^6` (HO, exactly M6). NB and MC use the affine rate boxes in their stated sorted labels; SB uses the FULL unsorted B7, allowing within-block permutations; MP uses variables `(ubar,vbar)` in that order; R3 uses `(y,tau,gamma)` with y,gamma compactified and tau affine. Split axis is zero-based path depth modulo dimension; bit0 is lower half, bit1 upper half. All sign predicates are uniform over J and the dual enclosures, with coefficient interval arithmetic or an equivalent exact parameter Bernstein method. "Unsorted" means some i<j have cell lo_i>hi_j, never just an unsorted midpoint.

If every obligation QO,HO,NB,MC,R3,SB,MP is exact-verified, the four cases exclude EVERY spectrum at EVERY `z_*<z<=z_*+epsilon`. For arbitrary z>z_*, the adopted spectral shift maps a hypothetical G to a ratio `z' in(z_*,min(z,z_*+epsilon)]`, preserving irreducibility, spectral bound zero and the repeated critical factor. Thus no such G exists at ANY z>z_*. The caller then proves the candidate PH theorem for every c,d>0, and the adopted attaining construction gives supremum=max=z_*.

This is not a claim that the PH-realizable set is downward closed; any fuller interval composition or minimum-order table must separately cite the adopted construction bands and PH8 upper result.

## 10. Actual evidence and high-consequence gate

At the fixed rational center z=z0, with point rational approximations of a_dual,b_dual, the owner kernel FLOAT searches closed:

- QO: 55,983 leaves (40,984 positive +14,999 excluded).
- HO: 15,729 leaves (15,557 positive +172 excluded).
- R3: 2,251 leaves (Abar<=0:1100, Dbar<=0:1082, f1<4:69).
- NB on the enlarged N6: 169,312 leaves (Q21687, adaptiveY0 103616, unsorted42839, Disc555, Y2v6 466, E4v6 149).
- MC: 41,207 leaves (H15832, jointEnd9992, unsorted10074, SchurBlock5309).
- SB: 82,670 leaves (Schur13768, Fnegative68902).
- MP: 41 leaves (Fnegative40, local1).

These counts are diagnostics only, NOT exact certificate receipts. Some earlier designs did not close within their finite caps: direct near-root six-dimensional covers; a redundant seven-dimensional multiplier-admission cover; small-q independent coefficient-interval and fixed-anchor variants; and an outer Q cube whose lower bound was too narrow. They were replaced by the final routed Schur block, common-basis adaptive cubic tails and enlarged N6 above. No timeout was called an exclusion.

The exact local-stage run finished 09:37:14 PDT and is pinned in Section 2. The older local radius10^-6 packet and its predecessor checker remain unchanged; the enlarged centered-polynomial checker transparently reuses pinned interval/AD declarations, so it is NOT an independent replay. All global models and finite counts above remain kernel diagnostics; they have not been serialized as exact proofs.

Before ANY full-target executable GO: freeze this definition-first manuscript and the intended input set; obtain disjoint algebra and bridge/robustness hostile reviews; obtain a hardened author checker (always-active named scientific errors, cooperative stop with INCOMPLETE receipts, source bindings, exclusive output, bounded resource/clock admission); obtain a separately authored definition-first checker WITHOUT exposing the author's verifier code; and freeze a bounded prior-art screen only under explicit parent source/public-search authorization. Parent has been asked for that gate. No public query or external transmission is inferred authorized. Afterward, both checkers must consume ONE pinned certificate/input set in the same admission window; nonzero, incomplete or failed obligations leave NOT_PROVED.

END — exact LOCAL optimum stage plus a complete written global reduction and fixed-center floating closure of all finite pieces; the GLOBAL theorem is NOT_PROVED pending the frozen high-consequence gate.
