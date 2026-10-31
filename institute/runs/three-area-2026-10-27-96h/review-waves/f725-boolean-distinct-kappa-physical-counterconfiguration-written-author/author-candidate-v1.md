# F725: same-object sheared physical counterconfiguration and affine-alignment qualification

Status: nonblind written author reconstruction, for independent parent disposition. The mathematical output below is not an all-U3-capped witness. The separate local-H premise and original caller discussed in §7 are not established here. J always denotes the parity of the number of nonzero entries at w=0; the linear swap on two-bit vectors is written J2.

## 1. Exact physical object, including all sites

Work in F2, with 0=(0,0), p=(1,0), q=(0,1), r=(1,1), and c=(ell,h,j,b), j,b in F2^2. Let f_j=j0 j1, R(j,b)=j dot b, rho(b)=(-1)^(1+b0 b1). Let S={(1,f_j,j,b)}. On S put a=(-1)^R and g=rho; on its h-mates put a=0, g=-2 rho. On the two ell=0 points with (j,b)=(0,0), put a=0,g=4; on the six ell=0 points with j!=0,b=0, put a=0,g=-2; on the other 24 ell=0 points put a=g=0. At every site use the same inverse

    4u(c,w) = x(c)+3 a(c) chi1(w)+g(c) chi2(w)+y(c) chi3(w),
    chi3=chi1 chi2,

with chi1 and chi2 independently taking both signs as w runs over the four labels. In particular, the graph condition is y=-a g x. These are the displayed f/R and coefficients, not a newly selected phase.

Define the reference X_* on S by X_*=2*1_{b=j}-1, on the four mates (1,1+f_j,j,0) by +2, and on ell=0 by the six left-hand entries in this table, all other entries zero. Define P(ell,h,j,b)=(ell,h,j,b+j) and X'=X_* composed with P. The right-hand entries list ALL six ell=0 values of X' in the original physical coordinates; P=P^{-1}.

| j | h | b | X_* | X' |
|---|---:|---|---:|---:|
| p | 1 | q | +2 | -2 |
| p | 1 | r | -2 | +2 |
| q | 1 | p | -2 | +2 |
| q | 1 | r | +2 | -2 |
| r | 0 | p | +2 | -2 |
| r | 0 | q | -2 | +2 |

Thus X'(1,f_j,j,b)=2*1_{b=0}-1, the four actual D0 sites are (1,1+f_j,j,j), all with X'=+2, and no ell=0 E-row is occupied by X'. The three displayed Z2 pairs have differences p,q,r, respectively, and lie in the three distinct j=p,q,r L-cosets. Relative to the actual anchor b_j=j, the graph exception is b=0, so Delta_j=j and epsilon_j=+1. In the 1+1+1 location condition the map Delta is the identity, and Delta(a_d+a_d')=d+d' for the chosen coset labels a_d=d. This is a calculation on the actual coordinates, not a replacement of anchors by representatives.

Now define one Y' on exactly the same 64 sites:

* on S, Y'=-a g X';
* on the 12 other graph h-mates (b!=j), and on the six ell=0 E-row sites (j!=0,b=0), set Y'=+2 except Y'(0,0,p,0)=-2;
* on the six tabulated Z2 sites set Y'=+2; at (0,0,0,p) set Y'=+4;
* at the four D0, the two F sites and the other 17 Z sites set Y'=0.

The site partition is therefore 16 graph, 4 D0, 12 graph-mate D3, 6 E-row D3, 2 F, 6 Z2, 1 Z4 and 17 Z0, totalling 64. There are exactly 18 D3 sites, 23 spatial zeros of Y' (=4+2+17), and

    sum X'^2 = 16+4*4+6*4 = 56,
    sum Y'^2 = 16+18*4+6*4+16 = 128.

The Z4 point (0,0,0,p) is not in the six tabulated Z2 sites. No independent per-frequency choice of x, y, signs, or Z4 location is made.

## 2. Direct U0 transform, carried balance, and graph characters

For s in F2 and a two-bit covector alpha, write chi_alpha(b)=(-1)^alpha(b), and

    Z_{ell,j}(s,alpha)=(1/4) sum_{h,b} X'(ell,h,j,b)(-1)^(s h+alpha(b)).

Directly from the sites above,

    Z_{1,j}=(-1)^(s f_j) [1-2*1_{alpha=0}+(-1)^s chi_alpha(j)]/2,
    (Z_{0,0},Z_{0,p},Z_{0,q},Z_{0,r})
      =(0, (-1)^s[-chi_alpha(q)+chi_alpha(r)]/2,
           (-1)^s[chi_alpha(p)-chi_alpha(r)]/2,
           [-chi_alpha(p)+chi_alpha(q)]/2).

The (s,alpha)=(0,0) column vanishes. For the other seven columns, the complete values are as follows; for example p- means -1 at j=p, and omitted entries are zero.

| (s,alpha) | ell=0 | ell=1 |
|---|---|---|
| (1,0) | none | 0-, p-, q-, r+ |
| (0,b0) | p-, r+ | 0+, q+ |
| (1,b0) | p+, r+ | p+, r- |
| (0,b1) | q+, r- | 0+, p+ |
| (1,b1) | q-, r- | q+, r- |
| (0,b0+b1) | p+, q- | 0+, r+ |
| (1,b0+b1) | p-, q+ | p+, q+ |

Every nonzero column has four distinct nonzero positions on an affine two-flat in (ell,j) and sign product -1. A character on that flat has product +1, so each signed character sum is +2 or -2. The quotient transform multiplies this sum by 4. Hence the full 64-point unnormalized transform of X' has exactly eight zeros, 28 entries +8 and 28 entries -8. The equal signs follow also from sum_xi X'hat(xi)=64 X'(0)=0. In particular every U0 coefficient is divisible by 8 and capped at 8, and X'hat(0)=0. This is a direct table for X', not an appeal to the numerical result of the old finite run.

On a graph row, using 2*1_{b=0}-1=(-1)^(b0 b1+b0+b1), the forced graph values are

    Y'(1,f_j,j,b)=(-1)^((j+r) dot b).

Thus, in physical b coordinates, the intrinsic H-characters are (r,q,p,0), in the row order j=(0,p,q,r). Their values in b-order (0,p,q,r) are respectively

    (+,-,-,+), (+,+,-,-), (+,-,+,-), (+,+,+,+).

They are four distinct covectors; their total graph sum is 4. Here lambda_j=j, B=I and Delta_j=j, D=I. Consequently the character-linear map T+J2(B+D) is I, rank 2. A row translation b_aligned=b+j changes a row character only by the scalar (-1)^((j+r) dot j)=+1 here, so these same four characters remain distinct in this globally aligned coordinate system.

Let t be the specified transported original-DC covector, not an after-the-fact chosen zero, and set

    x_t(c)=(-1)^t(c) X'(c),   y_t(c)=(-1)^t(c) Y'(c).

The fixed a and g are NOT modulated. For all xi, xhat_t(xi)=X'hat(xi+t); hence all 64 caps and divisibilities hold and xhat_t(t)=X'hat(0)=0. This holds for every possible supplied t, so it includes the specific carried one without assigning it a numerical value.

## 3. Exact inverse, support, J, and the 52 failure

At t=0 the inverse is ternary at every one of its 256 physical entries. On S, x,a,g are signs and y=-agx. If chi1=a x, the two chi2 values both give u=x; if chi1=-a x, one chi2 value gives 0 and the other gives -x. Thus each graph site has three nonzeros. At a D0 or D3 site the numerator is a sum of two independently signed magnitude-2 terms and has two nonzeros; the same is true at each Z2 site. Each F or Z4 site has four nonzeros, and each Z0 has none. The support is exactly

    16*3 + 2*4 + 4*2 + 18*2 + 6*2 + 1*4 = 116.

For w=0, chi1=chi2=chi3=1. The graph nonzero counts by b=(0,p,q,r) are (4,2,2,4): b=0 and b=r contribute four each, while b=p and b=q each require a=-1 and contribute two. Off graph, the exact counts are F=2, D0=3, graph-mate D3=9, E-row D3=1, Z2=3, Z4=1, Z0=0. For example, among the four D0, g=+2 at j=0,p,q and -2 at j=r; among graph-mate D3 exactly the three sites with b=r give zero; and the chosen negative E-row value is the unique nonzero E-row at w=0. Therefore the total is

    12+2+3+9+1+3+1 = 31,

and J=31 mod 2=1. At t=0 the four character rows give graph sum 4, the 17 positive and one negative D3 values sum to 32, the six Z2 values sum to 12, and Z4 contributes 4. Thus

    Y'hat(0)=4+32+12+4=52.

For arbitrary supplied t, multiplying x and y together by the site character preserves the graph relation, all the local forms, ternarity, and the support count 116, while a and g remain fixed. To establish J rather than assume that the entire u is modulated, calculate the physical Fourier residues. For xi=(nu,s,beta,alpha),

    ahat(xi)=4(-1)^(nu+s f_alpha+beta(alpha)),
    sum_b rho(b)(-1)^alpha(b) = -2(-1)^(alpha0 alpha1),
    sum_j (-1)^(s f_j+beta(j)) = 4*1_{beta=0} if s=0,
                                    2(-1)^(beta0 beta1) if s=1.

The ell=1 contribution to ghat is (-1)^nu[1-2(-1)^s] times the last two sums. The ell=0 contribution is 12-16*1_{beta=0} for s=0 and zero for s=1. Consequently 3 ahat=ghat=4 mod 8 for every xi. Since xhat_t is 0 mod 8 and a ternary u(c,0) has the parity of its nonzero indicator, the actual inverse gives yhat_t(xi)=4J mod 8 for every xi. But

    yhat_t(t)=Y'hat(0)=52=4 mod 8,

so J=1 for the particular transported physical object for every specified t. At that actual frequency t the U3 cap 12 fails by the exact value 52. No conclusion about any other completion of x_t is inferred from this one failed y_t, and no all-capped witness is asserted.

## 4. The general anchor/character calculation at its precise imports

Assume the stated rank-two quadratic f, the radical K=rad(B_f) with K-to-b projection an isomorphism, the displayed physical quadratic rho, bent R and R+f, and the actual four-distinct-D0 location theorem with its same-x U0/divisibility/carried-balance hypotheses. Write the unique radical point above b as k(b), z=(i,0)+k(b), and d(b)=f(z+k(b))+f(z), a linear function of b. Then h'=h+d(b) makes the graph h'=F(i), F(i)=f(i,0). The complement to K carries a nondegenerate binary quadratic, so sum_i F(i)=1.

For R_i(b)=R((i,0)+k(b)), let v_i(alpha)=sum_b (-1)^(R_i(b)+alpha(b)). Bentness and Parseval give sum_i v_i(alpha)^2=16; the i-Walsh transforms of v_i and of (-1)^F(i) v_i both have magnitude 4, with the b-frequency shifted by d for R+f. A Boolean function on two bits is affine with Walsh values one +/-4 and three 0, or nonaffine with all four values +/-2. If any row were nonaffine, the energy 16 would force all four rows to contribute +/-2. Their signs would have product -1 because their i-transform is flat; multiplication by (-1)^F(i) reverses that product and contradicts flatness of the other transform. Thus all R_i are affine. The same energy identity shows that every alpha occurs as the row linear covector exactly once. Every permutation of four elements of F2^2 is affine, so lambda_i=T i+lambda_0 with T invertible.

Let b_i be the actual D0 anchor in row i, Delta_i its actual exception offset, and gamma_i=b_i+Delta_i the exception's physical graph coordinate. The imported location result makes Delta affine at either of its two alternatives; it is a necessary location theorem, not an independent assignment of signs. Write the weighted graph values as epsilon_i(2*1_{b=gamma_i}-1). For J2(v0,v1)=(v1,v0), multiplication by the actual -ag gives the intrinsic graph covector

    kappa_i = lambda_i+(1,1)+J2 gamma_i.                 (1)

Indeed the sign 2*1_{b=gamma}-1 is (-1)^((b0+gamma0)(b1+gamma1)+b0+gamma0+b1+gamma1), and its quadratic term cancels the b0 b1 in -g. Only the row scalar depends on epsilon_i, R_i(0), and gamma's constant terms. In particular translations within a row change its scalar but not its H-character.

Since lambda and Delta are affine,

    XOR_i kappa_i = J2 XOR_i b_i.                       (2)

A map from F2^2 to F2^2 is affine exactly when the XOR of its four values is 0. If b_i=B i+b_* and Delta_i=D i+Delta_*, then (1) is affine with linear part T+J2(B+D). A rank-0 map has one character four times, rank 1 has two characters twice each, and rank 2 has all four once. Therefore even multiplicity is equivalent to rank at most 1 in the affine-anchor case; it does not follow merely from location, U0 caps, or J=1. The explicit x_t,y_t in §§1–3 realize rank 2 under the displayed f/R and physical inverse, but violate U3 and hence do not disprove any additional restriction deduced using all U3 caps.

For completeness, the even-multiplicity partial-Parseval obstruction used by the source can be reconstructed at its stated larger-class assumptions. Given four graph character rows, 12 signed magnitude-2 mates at nonzero b, odd sum F, y energy 128, and all full coefficients 4 mod 8, suppose all caps are <=12. With n negative mate signs, the graph contribution to A1 is 0 mod 8 and the mate contribution is 4(n+s) mod 8. Full Parseval makes exactly eight of the 64 coefficients magnitude 4. Let E count triples at s=n with |A1|=8 and O count triples at s=n+1 with |A1|=4. Counting these full coefficients gives E+O<=8; the ell=1 energy 64 gives 4E+O+9(16-O)=128, or O=2+E/2. If C is the sum of the 12 products of graph and mate signs, the fixed-s Parseval identity gives E=16+(-1)^n C>=4. Thus E=4 and every mate sign is -(-1)^n times its graph sign. Their product yields product sigma_i=(-1)^n. In the opposite slice, put v_i=sigma_i(-1)^((n+1)F(i)); product v_i=-1, and the row transform at alpha is v_i[12*1_{alpha=kappa_i}-2]. If all four kappa coincide, choosing that alpha gives magnitude 20. If two distinct kappa occur twice, choose an occurring alpha and a beta which makes its two active signed v_i agree; the other two cancel by the negative total product, again giving magnitude 20. This contradicts the assumed cap. It is conditional on all its hypotheses; the present four-distinct-character object does not satisfy the even-multiplicity hypothesis.

## 5. MATH MAJOR: broad affine-alignment overstatement, with exact repair

Equation (2) correctly shows that nonaffine anchors have nonzero XOR of the kappa values and hence cannot have every character multiplicity even. The particular map b'=b+b_i with h' fixed is nonaffine when i->b_i is nonaffine, so the source's warning against simply using THAT map to transport the physical Fourier spectrum is correct.

However, the broader statement that alignment itself is not affine is false if arbitrary full-space affine coordinate shears are allowed. Because F is a nondegenerate binary quadratic, {1,i0,i1,F(i)} is a basis for the functions on the four i values. Therefore EVERY anchor array has a unique representation

    b_i=B i+c+v F(i),           v=XOR_i b_i.

The following is a globally invertible affine change of the full physical coordinate space, leaving ell,h',i unchanged:

    b'' = b+B i+c+v(h'+1).                              (3)

At the actual D0 anchor, h'=F(i)+1 and b=b_i, so b''=0 in every row. At the graph, h'=F(i), so b''=b+b_i+v: this is still a translation on each graph row and preserves its intrinsic kappa, up to a row scalar. The inverse of (3) has the same shear formula. It permutes the full Walsh frequencies and can introduce only signs; consequently magnitudes and the residue class 4 mod 8 are preserved. In original (h,b) coordinates compose with the invertible linear h'=h+d(b) change.

If b_i is nonaffine then v!=0 and XOR_i kappa_i=J2 v!=0, so even multiplicity still fails: the affine shear does NOT make the partial-Parseval lemma applicable. Nor does it supply any U3 witness or global obstruction. This shear sends the physical h-toggle e to e plus the H-vector v; it is not an e-preserving coordinate change, so an argument that requires the original physical mate relation must explicitly carry that change rather than pretending the labels are unchanged. Thus the specific fixed-h map restriction and the nonautomatic even-kappa conclusion survive; only the blanket impossibility of affine alignment is refuted. Parent has classified this as ONE f718 author MATH MAJOR, not a falsification of the conditional even-kappa lemma and not an automatic hold of unrelated statements.

## 6. Remaining scope and historical checks

This construction verifies exactly the displayed physical f/R, same inverse, graph and all physical coordinates, four D0 anchors, actual six Z2 sites, all 64 U0 caps/divisibilities and specified t-zero, four intrinsic distinct characters, the complete site/energy/support/w=0 counts, J=1, and yhat_t(t)=52. It neither finds an all-U3-capped y for this or any x, nor excludes all such y, other anchor allocations, V, or the original Boolean target. The stronger possible implication from simultaneous J=1 AND all U3 caps to additional anchor/character restrictions remains a separate global condition.

The packet's S6 corrects f689's three profile-row signs and w=0 graph census as one explicit-example MATH MAJOR; the original body is unchanged. The actual S7 f710 v1 run failed, exit 1; S8 reports one separately corrected v2 PASS only for its fixed physical x, 64 transports and 1,800 sampled sign/site cases. These receipts do not test the present shear, exhaust 2^24 signs, produce a U3 witness, or establish V. They are not substituted for the above direct calculation.

## 7. Source coverage, process and limitations

Before the packet I read the complete manifest, freeze receipt, final binding, parent-live-metadata supply, actual dispatch receipt, and all 21 listed controls through their endings, and sent a direct PREBODY ACK to Main with that count. One initial attempt to read the dispatch used a mistyped workstation path and returned not found; the actual receipt was then read through its ending before the ACK. The 21 controls were used for status and permissions only. Held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers are NONINPUT.

After that ACK I read the sole packet in ascending serial raw windows of at most 20 LF through its final LF 621, before comparison or derivation. It contained complete bodies S1 LF1–197, S2 LF1–3, S3 LF1–206, S4 LF1–30, S5 LF1–37, S6 LF1–17, S7 LF1–42 and S8 LF1–55. S1 and S3 were unadopted author candidates; S4/S5 supply their stated conditional adopted imports; S6 is an additive correction; S7/S8 are historical run receipts only. Parent-reported whole-source SHA256 pins, respectively:

    S1 74a5f0cbec49ecabc63e33bdfdc20937092eb5faaef2616c5874533c0eb5adc3
    S2 96195b75b83e0f2d91f71849238f58808fb31c8803ed1439c67cb5e91587371f
    S3 a3e060e7564d91f0539c7bb9eb7b8603210617680c1e0ec8fb6bc26862210dca
    S4 fa3b4e334713a4981b267e12be567d2f328ca00203fb525a45100bd1deae2d4a
    S5 44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a
    S6 ba7cc22c99c615a0674d04ea827d90527494cfb0956452d8ad9588a885fd71f0
    S7 c863d8aed5ad610cc4854391f7efe5eb544fab36cd924e0a8a7ced43ff772e30
    S8 20b2bebb3cd3a0e93772a1160ff87a8b0dcfe3c658d575b7b366630f0a74cb0a

Direct metadata hashes observed after packet read: manifest ae74c6b03fd7efec922c22ccf26a80352190a183d6fd1d2a9138b0d28a2cd897; freeze c4d6574bd231d7310bcdc2d5d4512568e9b4ffe237e41686f8fde5c3da895fb2; final binding 331f517cea617d51d42760741573598f74826e40dd5fa81ebf8c68d2580e6fa4; supplied metadata f8e401aa8d79f088b54563ec5cda0f6f4d8a6731958e6dffb7e7f5a7cc0c72ef; actual dispatch e8039ce2fba15fe931f6d284ec7add99a59f067b5e83472761b7e77b05f2b985; sole packet ab1dde98809fd53370935e3e2188de5e83e3432d9ed50624aff68d83b8e3cde9. The eight original source bodies were not opened outside their frozen packet renderings; their pins above are parent-supplied, not separate child rehashes.

S5 lists a separate imported local-H=0 premise, but its definition is not displayed in the packet, and S3/S7/S8 expressly leave the separate local-H definition unverified or untested. Accordingly I do not claim an independent check of that premise, of original-source equivalence, or of the original caller. This limitation does not change the directly calculated conditional physical assertions in §§1–3.

No child scientific executable, CAS, solver, test, build, linter, formatter, old code, outgoing source, sibling artifact or finite search was used. Hashing the assigned metadata and packet was a metadata operation. Native clock observed during the work was 2026-10-30T17:02:36-0700 PDT, not a creation-time assertion. This is one complete exclusive-write output, subject to independent parent review and disposition.
