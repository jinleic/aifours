# Independent reconstruction: physical U0 example and same-x signed U3 frontier

**PROSPECTIVE GENERAL PROOF AUTHOR; NONBLIND; UNADOPTED.** This is a written reconstruction from the complete assigned packet, not a scientific execution or an independent-model-family, human, formal, or parent check. It identifies a concrete error in the source's purported exact seven-column table: **all six ell=1 entries in its three s=1, nonzero-alpha rows have the opposite sign.** The corrected table below still has the required four-point supports and negative products, so this error alone does not disprove the U0-capped construction. The 24-sign U3 system is not solved. No global Boolean conclusion, feasibility or infeasibility of that system, automatic clearance of any old gate, source identity, or novelty is claimed.

## 1. Scope and actual imports

Work on the common 64-block physical space c=(ell,h,j,b), with ell,h in F2 and j,b in F2^2. Let e toggle h, q(b)=1+b0 b1, rho(b)=(-1)^q(b), S={(1,f(j,b),j,b)}, and a=1_S(-1)^r. The input hypotheses are that f is quadratic with polar rank 2, and the **same** f+q, r, and r+f are bent. On S take g=rho(b), on its e-mates g=-2 rho(b), on the two F blocks g=4, on the other six b=0 E-row blocks g=-2, and on the remaining 24 Z blocks g=0. All arithmetic in coordinates is over F2; signs and sums are integer-valued.

The same physical inverse is

    u(c,w) = [x(c)+3a(c) chi1(w)+g(c) chi2(w)+y(c) chi3(w)]/4,
    chi3=chi1 chi2,                         x=U0, y=U3.

On S it imposes y=-agx and x=+/-1. The local block forms supplied by the packet are F:(x,y)=(0,0); D0:(+/-2,0); D3:(0,+/-2); Z2:(+/-2,+/-2); Z4:(0,+/-4); Z0:(0,0), with the appropriate physical a,g. At the named local H_local=0 import the counts are 4 D0, 18 D3, 6 Z2, 1 Z4, 17 Z0, with energies 56 and 128. H_local here is not the plane H below. The packet does not separately define H_local by a displayed formula; the named import is therefore not independently identified with any unstated invariant here.

The carried covector t is the actual specified image of original DC under the common gauge. It is fixed before choosing x, not selected as a convenient zero. The Walsh transform is what(xi)=sum_c w(c)(-1)^xi(c). This work does not restore the original selected nonzero T, original gauge, rank/atom constraints, or source equivalence.

Write K=rad(B_f), H={(0,d_f(k),k):k in K}, d_f(k)=f(z+k)+f(z), L=H direct-sum <e>, and lambda|H=0, lambda(e)=1. Choose a physical complement M of L, with M0={m in M:ell(m)=0}, M1={m in M:ell(m)=1}; extend covectors from L by zero on M. The rank and bentness imply K->F2^2_b is an isomorphism: in a basis whose first symplectic pair supports B_f and whose other two vectors span K, pf(B_f+B_q)=B_q|K because B_q has rank two. Nondegeneracy of B_f+B_q forces B_q|K nondegenerate. Each ell=0 H-cell therefore has exactly one b=0 point and three Z points.

For X(c)=(-1)^t(c)x(c), define Z_m(eta)=1/4 sum_(v in L) X(m+v)(-1)^eta(v). The adopted packet S3 imports the seven-profile theorem at its actual physical/zero-flat and collateral-atom boundaries: with the physical and divisibility premises, the 64 U0 caps <=8 and the specific balance xhat(t)=0 are equivalent to a zero eta=0 column and, for each nonzero eta in L*, either one entry +/-2 or four entries +/-1 on an affine two-flat of M with product -1, with all entries integral. All seven are evaluated on the **same x**. The identity

    xhat(t+eta+mu)=4 sum_(m in M) Z_m(eta)(-1)^mu(m),   mu in M*,

also shows directly that these profiles suffice for balance, all caps and divisibility by 8. S2 adopts the actual four-distinct-D0 location theorem only; S1's stronger assertions and example were unadopted. S4 reports a separate parent finite quotient run and a different U0 illustration, not a finite check of the present y or of this proof. No outgoing source links or sibling bodies are used.

## 2. Complete location argument and the signs needed for a U0 iff

Assume precisely one actual D0 block in each of the four ell=1 L-cosets. Name them D_i, put G_i=D_i+e, and write epsilon_i=X(D_i)/2. The graph H-plane G_i+H contains four +/-1 values. Its zero-column equation forces their sum to -2 epsilon_i, hence the unique exceptional offset delta_i in H satisfies

    X(G_i+h)=epsilon_i(2 1_(h=delta_i)-1).                         (2.1)

The four ell=1 lambda entries are

    Z_(m_i)(lambda)=+epsilon_i (-1)^lambda(D_i).                   (2.2)

This is a **plus**, not a minus: the graph sum is -2 epsilon_i and its lambda phase is opposite that of D_i. These four entries consume the column's full squared norm 4. Consequently every ell=0 lambda entry vanishes. Together with the zero column this makes the X sum on each ell=0 H-cell separately zero. Since the sole b=0 point there has x=0, a cell contains either no selected Z2 or exactly two with opposite weighted signs. Six Z2s give three occupied cells, with coset multiplicities either 1+1+1 or 2+1.

For nonzero alpha in H*, let bar(alpha) vanish on e and M and eta_s=bar(alpha)+s lambda. Expanding (2.1),

    Z_(m_i)(eta_s) = epsilon_i (-1)^eta_s(G_i)
                      [(-1)^alpha(delta_i)+(-1)^s]/2.             (2.3)

Each graph coset contributes one unit of squared norm across the two extensions. For a Z2 pair z,z+d with d!=0 and xi=X(z)/2, the eta_s contribution is xi(-1)^eta_s(z) if alpha(d)=1 and zero otherwise. If two active cells share a coset, their two extension contributions are C1+C2 and, up to a common sign, C1-C2; their total squared norm is still 2(C1^2+C2^2). The two columns have total squared norm 8, of which the graph contributes 4. Thus exactly two of the three directions are active for each nonzero alpha. As every nonzero direction is killed by exactly one nonzero alpha, the three directions are exactly the three nonzero H-elements. Their XOR is zero. Via H->b this proves the physical nonzero-b census (2,2,2) and XOR(Z2)=0.

Let X_D=sum_i D_i, where sum means XOR. It lies in L because the four M1 representatives XOR to zero. To find lambda(X_D), choose u,v representing the two-dimensional quotient by K with B_f(u,v)=1, and write the four z-coordinates of D_i as su+tv+k_st. The h-coordinates are 1+f(su+tv+k_st). Since d_f is linear on K,

    lambda(X_D)=sum_(s,t) f(su+tv)+d_f(sum_(s,t) k_st)=1.

Here the last d_f term cancels the radical lift's h-coordinate, and the four f values have XOR B_f(u,v)=1. The four lambda entries form the plane M1; their product is -1. Equation (2.2) gives product_i epsilon_i=+1.

For 1+1+1, let a_d in M0 be the coset of the cell with direction d. For any nonzero alpha the two active Z cells lie in distinct M cosets, contributing two unit entries in each eta_s column. The remaining norm requires exactly two graph entries for each s. Equation (2.3), for all three alpha, implies by Fourier inversion that the four delta_i are the four H-elements once each. The map delta:M1->H is therefore an affine bijection; call its linear part A:M0->H. For distinct d,d', choose alpha active on both. The two graph offsets with alpha(delta)=s differ by d+d', while the support-flat condition says their M representatives differ by a_d+a_d'. Hence

    A(a_d+a_d')=d+d' for every distinct nonzero d,d'.              (2.4)

For 2+1, suppose d1,d2 occur in the two cells over a, and d3=d1+d2 over b!=a. The unique alpha0 active on d1,d2 kills d3. At one extension their contributions add to a singleton +/-2 and exhaust the norm; at the other they cancel and all four graph entries occur. Thus all delta_i lie on one alpha0 level, a line parallel to d3. For either other nonzero alpha, the active cells are over a and b. Two graph entries per extension force the two line elements to occur twice each; the flat equation puts equal-delta graph representatives at difference a+b. Thus delta is affine onto that line, with kernel <a+b>. This proves both alternatives, not merely one chosen example.

The actual physical graph-negative XOR also follows. On each graph plane, X has a singleton exception; multiplying by the character t|H either complements the set or symmetric-differences a two-point half-plane. The XOR of that half-plane is the unique nonzero element k_t in ker(t|H), or zero when t|H=0. Therefore the XOR of negative physical x points on G_i+H is G_i+delta_i+k_t. Both alternatives make sum_i delta_i=0, so XOR(P)=X_D. The three Z2-pair differences XOR to zero, so XOR(W)=X_D for the ten D0/Z2 points. This does not by itself replace the other physical divisibility congruences.

The following signs complete an exact same-x U0 criterion, not a U3 criterion. Choose a physical point z_d in each Z2 pair and xi_d=X(z_d)/2. For alpha active on two directions d,d' in **different** M0 cosets, let i,i' be the two graph indices with alpha(delta)=s. The four-entry support and odd-product conditions are

    m_i+m_i'=a_d+a_d',                                             (2.5)
    epsilon_i epsilon_i' xi_d xi_d'
      (-1)^eta_s(G_i+G_i'+z_d+z_d') = -1.                         (2.6)

The two extra (-1)^s factors from the graph entries cancel. Switching the chosen member of a Z2 pair flips xi_d and its character together. In 1+1+1 impose (2.4) and all six actual equations (2.6). In 2+1 impose the affine rank-one description just proved, (2.6) for both extensions of each alpha!=alpha0, and, for representatives z1,z2 of the two cells over a,

    alpha0(delta_i)=1+bar(alpha0)(X_D)  for every i,                (2.7)
    xi1 xi2 (-1)^[bar(alpha0)(z1+z2)+bar(alpha0)(X_D)]=+1.        (2.8)

Indeed the four-graph column has product (-1)^[bar(alpha0)(X_D)+s], hence (2.7); the other extension is s=bar(alpha0)(X_D), and lambda(z1+z2)=1 gives the addition condition (2.8). Conversely, the listed graph and pair forms make the zero column vanish; product epsilon_i=+1 and lambda(X_D)=1 give the lambda column; the equations above give precisely the six remaining singleton or odd-product flat columns. The quotient identity then proves all U0 divisibilities, all 64 caps and the specified balance. Necessity uses the stated S3 profile import. The signs, support locations and all columns remain tied to one actual x; no independent-spectrum construction is used.

## 3. Explicit x, corrected seven columns, and physical C

Put 0=(0,0), p=(1,0), q=(0,1), r=(1,1); vector r is not the phase. Take

    f(j,b)=j0 j1,             phase r(j,b)=j0 b0+j1 b1.

The polar rank is 2. The Walsh transform of f+q factors into two nondegenerate binary quadratic sums of magnitude 2. For both phase and phase+f, summing over b selects j equal to the b-frequency and leaves magnitude 4. Thus all three required functions are bent. Here H is the b-plane, lambda=h, and use M={(ell,0,j,0)}. Put f_j=j0j1, G_j=(1,f_j,j,0), D_j=(1,1+f_j,j,0).

Define x_* on the graph by x_*(1,f_j,j,b)=2 1_(b=j)-1, and x_*(D_j)=+2. Its only other nonzero entries are

    (ell,j,h,b; x_*) = (0,p,1,q;+2), (0,p,1,r;-2),
                       (0,q,1,p;-2), (0,q,1,r;+2),
                       (0,r,0,p;+2), (0,r,0,q;-2).

For **each given t**, define x_t(c)=(-1)^t(c)x_*(c). Thus X=x_* in the profile definition, while a and g remain fixed. The zero column vanishes: each graph sum -2 cancels its D0 +2 and every Z pair sums to zero. The complete nonzero columns are as follows; j+ means +1 at that M representative, and unlisted entries vanish.

| eta | ell=0 entries | ell=1 entries |
|---|---|---|
| lambda | none | 0-, p-, q-, r+ |
| b0 | p+, r- | 0+, q+ |
| b0+lambda | p-, r- | p-, r+ |
| b1 | q-, r+ | 0+, p+ |
| b1+lambda | q+, r+ | q-, r+ |
| b0+b1 | p-, q+ | 0+, r+ |
| b0+b1+lambda | p+, q- | p-, q- |

These are literal evaluations of one x_t. To reproduce them without relying on a table, for alpha!=0 and s in F2 the graph entry is

    [(-1)^(s f_j)/2] [(-1)^alpha(j)+(-1)^s],                     (3.1)

and the ell=0 entry is one half of the signed character sum of the listed pair at its fixed h. For alpha=0,s=1 the graph entry is -(-1)^f_j. As a direct discrepancy, at j=p, eta=b0+lambda the four graph values contribute -2 and D_p contributes -2, giving Z=-1, while S1's table prints +1. At j=r the value is +1, while S1 prints -1. The same simultaneous reversal occurs for both ell=1 entries in each of the other two nonzero-alpha, s=1 rows. This is an exact-value defect in the unadopted source, not a reason to alter its bytes or infer a global failure.

Every corrected row has four +/-1 entries, XOR-zero support and product -1. Fourier transformation on its affine support gives magnitude 2 at every M frequency. Hence xhat_t has exactly eight zeros t+L-perp and the other 56 values are +/-8; in particular all caps and xhat_t(t)=0 hold for the actual specified t. Directly, x has 16 graph units, four D0s and six Z2s, so sum x^2=16+16+24=56.

The packet's physical C congruences can also be checked without selecting t. Write t=nu ell+s h+beta(j)+alpha(b), and S_s(gamma)=sum_j (-1)^[s f_j+gamma(j)]; then S_0(gamma)=4 1_(gamma=0), S_1(gamma)=2(-1)^(gamma0 gamma1). For P={graph points:x_t=-1},

    |P|=8+(-1)^nu S_s(beta)                 if alpha=0,
    |P|=8-(-1)^nu S_s(beta+alpha)           if alpha!=0.

Thus |P| is even and |P|/2=s modulo 2. Among the four D0s, the number with negative x has parity s. Among the three Z2 pairs, one member is negative exactly when alpha kills its direction; for alpha=0 all three contribute one and for alpha!=0 exactly one does. Hence the number N of negative points among the ten D0/Z2 sites has parity s+1, and |P|/2+|N| is odd. XOR of the four D0 sites is e, and the three Z2 differences p,q,r XOR to zero, so XOR(W)=e. On the graph planes the physical negative XOR is sum_j G_j+sum_j j=e, with the four identical t|H half-plane XOR corrections cancelling, hence XOR(P)=e as well. These are the actual C cardinality/XOR conditions from S3, not separately chosen spectral columns.

## 4. Reference common y, local fibre signs, and J for every t

On the same x_* put y_*=-agx_* on S; put y_*=0 at F and D0; put y_*=+2 at all 18 D3s and six listed Z2s; put y_*=+4 at c_*=(0,0,0,p); put y_*=0 at the other Z sites. For every given t let y_t=(-1)^t y_*. This does not change a or g and preserves y_t=-agx_t on the graph. The inverse is ternary for every block, not just a spectrum assigned after the fact.

For explicit single-entry phases, write epsilon(c)=(-1)^t(c), use w with chi3=chi1 chi2, and denote the de-twisted x_*/2 sign at a listed Z2 site by zeta. The actual inverse values are:

* On S put A=a chi1, G=g chi2. If G=A then u=A; if G=-A then u=(x_t+A)/2. Exactly three of the four entries are nonzero, all with their displayed signs.
* F: u=chi2 at all four w. D0 at D_j has u=epsilon(D_j) precisely where chi2=epsilon(D_j), and zero otherwise, because g(D_j)=+2.
* A graph D3 mate (1,1+f_j,j,b), b=p,q,r, has g/2=-rho(b). If its de-twisted y/2 sign is d, then it is nonzero exactly when chi1=-rho(b) epsilon(c) d, with value -rho(b) chi2. An E-row D3 has g/2=-1; with sign e it is nonzero exactly when chi1=-epsilon(c)e, with value -chi2.
* A Z2 with de-twisted y/2 sign z has u=epsilon(c) zeta exactly when chi3=zeta z, and zero otherwise. A Z4 with de-twisted y/4 sign k has u=epsilon(c) k chi3 at all four w. Z0 has u=0.

These formulas cover arbitrary allowed signs below, not merely the all-positive reference. Consequently the actual support is 16*3+2*4+4*2+18*2+6*2+1*4=116; x-energy is 56 and y-energy is 16+18*4+6*4+16=128. Exactly 4 D0, 2 F and 17 Z0 blocks have y=0, i.e. 23 spatial y zeros. They realize the displayed local types and counts of the named import; the separate undefined-in-packet H_local identification remains at the import boundary stated in section 1.

At t=0 and w=(0,0), the graph has 7 zeros, distributed by b as 3,2,2,0 for 0,p,q,r, so it has 9 nonzeros. The off-graph numbers of nonzeros are 2 F, 4 D0, 8 graph D3 mates (those with b=p or q), 3 Z2 and 1 Z4, totaling 18. Thus the physical w=0 slice has 27 nonzeros and J=1.

This parity persists for every fixed t, not by changing the gauge or choosing t. The explicit a spectrum is

    ahat(nu,s,beta,alpha)=4(-1)^[nu+s f_alpha+beta(alpha)].

For g, set R(alpha)=sum_b rho(b)(-1)^alpha(b)= -2(-1)^(alpha0 alpha1). Its graph and mate contribution is

    (-1)^nu [1-2(-1)^s] S_s(beta) R(alpha),

and its ell=0 contribution is 2 1_(s=0)[4-2 sum_(j!=0)(-1)^beta(j)]. For s=0 the graph term is divisible by 8 and the other term is -4 or 12; for s=1 the ell=0 term vanishes and the graph term is +/-12. Hence ghat(xi)=4 mod 8 for every xi, as is ahat(xi). Since every xhat_t is divisible by 8, the **actual** four-fibre inverse gives, for every xi,

    4J = xhat_t(xi)+3 ahat(xi)+ghat(xi)+yhat_t(xi)
       = yhat_t(xi)  (mod 8).                                    (4.1)

Here the first equality modulo 8 follows because sign-weighted sums of ternary u(c,0) have the same parity as their number of nonzeros. At t=0 the count gives yhat_*(xi)=4 mod 8 for all xi. Character modulation translates the y spectrum: yhat_t(xi)=yhat_*(xi+t), and the same fixed-a/g inverse gives J=1 for every specified t. This is not an amplitude cap.

Indeed the graph y_* sum is -8, the 18 D3s contribute 36, the six Z2s contribute 12 and the Z4 contributes 4. Thus yhat_t(t)=yhat_*(0)=44>12. This particular common y is not U3-capped; it is not a Boolean witness.

## 5. Exact 24-sign same-x U3 system, all phases and quantifiers

Fix the preceding actual x_t, f, phase, g and t. Every local completion y with the given local counts is specified by de-twisting y_tilde(c)=(-1)^t(c)y(c), keeping the forced graph and making one joint choice:

* d_(j,b)=+/-1 at the 12 graph D3 mates (1,1+f_j,j,b), j in {0,p,q,r}, b in {p,q,r}, with y_tilde=2d_(j,b);
* e_(j,h)=+/-1 at the six E-row D3s (0,h,j,0), j in {p,q,r}, h in F2, with y_tilde=2e_(j,h);
* z_(d,b)=+/-1 at the six listed Z2 sites, with y_tilde=2z_(d,b);
* one actual Z4 site (0,h_*,j_*,b_*) among the 24 ell=0 Z sites excluding those six, and one k=+/-1, with y_tilde=4k. The other 17 Z sites, F and D0 have y=0.

There are exactly 18 possible Z4 sites and two signs. No other x/y placement is allowed in this fixed-x family. Changing any one of the 24 d/e/z signs toggles exactly one w=0 nonzero at that physical block: the two possibilities on a D3 interchange zero/nonzero, as do the two on a Z2. A Z4 is always nonzero at w=0, regardless of site or sign. Relative to the all-positive reference, which has J=1 for every t, the exact J condition is therefore

    number of negative signs among the 12 d, 6 e, 6 z is even.      (5.1)

Equivalently, each single sign flip changes every y Walsh coefficient by 4 modulo 8; changing Z4 sign changes it by 0 modulo 8, and relocating Z4 changes it by 4+4=0 modulo 8. Equation (4.1) yields the same parity conclusion. There is no independent parity variable for the Z4.

For the forced graph, direct substitution yields y_tilde(1,f_j,j,b)=sigma_j (-1)^kappa_j(b), where

    sigma_0=+1, sigma_p=sigma_q=sigma_r=-1,
    kappa_0=kappa_r=b0+b1,  kappa_p=kappa_q=0.

Set B_p={q,r}, B_q={p,r}, B_r={p,q}, h_p=h_q=1 and h_r=0. For s in F2 and alpha,beta in (F2^2)* define the **same physical** partial transforms

    A1(s,alpha,beta) = sum_j (-1)^beta(j) [
          4 sigma_j (-1)^(s f_j) 1_(alpha=kappa_j)
        + 2 (-1)^[s(1+f_j)] sum_(b=p,q,r) d_(j,b)(-1)^alpha(b) ],

    A0(s,alpha,beta) = 2 sum_(j=p,q,r) (-1)^beta(j)
                                sum_(h in F2) e_(j,h)(-1)^(s h)
        + 2 sum_(d=p,q,r) (-1)^[beta(d)+s h_d]
                                sum_(b in B_d) z_(d,b)(-1)^alpha(b)
        + 4k (-1)^[beta(j_*)+s h_*+alpha(b_*)].                  (5.2)

Every one of these expressions uses the same 24 signs and the same actual Z4 site. For the ell-frequency nu, all 64 physical coefficients are exactly

    yhat(t+nu ell*+s h*+beta+alpha)=A0(s,alpha,beta)+(-1)^nu A1(s,alpha,beta).  (5.3)

For real A0,A1, max(|A0+A1|,|A0-A1|)=|A0|+|A1|. Therefore **all 64** caps |yhat|<=12 are equivalent to the 32 inequalities

    |A0(s,alpha,beta)|+|A1(s,alpha,beta)|<=12
       for every s in F2 and every alpha,beta in (F2^2)*.          (5.4)

Together with (5.1), this is exactly the J-and-U3-cap problem for this fixed physical x, the given t, the specified local counts and one common inverse. Neither equation permits independently chosen spectra, and the equivalence does not prove that a satisfying assignment exists or does not exist.

For uniform necessary restrictions, let n_j be the number of negative d_(j,b), and n=sum_j n_j. The graph contribution to A1 is -8 at both (s,alpha,beta)=(0,0,0) and (1,0,0). From (5.4), |A1|<=12. At the first index,

    A1=-8+2(12-2n)=16-4n,                          so 1<=n<=7.

At the second,

    A1=-8-2 sum_(j,b)(-1)^f_j d_(j,b)
       =-20+4(n_0+n_p+n_q-n_r),
    so 2<=n_0+n_p+n_q-n_r<=8.                                    (5.5)

These are necessary for every site and every choice of remaining signs; they exclude the all-positive graph-D3 signs and also the all-negative graph-D3 signs, but do not settle (5.1),(5.4).

## 6. Unpaid frontier and assurance

The exact first unpaid step for this one explicit physical x is a single shared assignment of 24 signs and one of 18 Z4 sites with sign, satisfying (5.1) and all 32 inequalities (5.4), or a proof that no such assignment exists. No search, enumeration, solver, program, test, build, linter or formatter was run by this author. Even a resolution for this x does not quantify over all actual f/phase/x choices, other four-distinct-D0 instances, or other D0 allocations. Beyond any such common capped x/y, the 140 zero positions of the **same u** require a v with odd negative parity and all 256 odd-half caps <=14, then the exact original gauge, selected T, rank/eight-zero, atom and pairwise-inverse caller must be restored. These requirements are not supplied here. The parent must read and adjudicate this body independently; the S1 table correction is not an automatic parent disposition.

Chronology and exposure: before direct PREBODY ACK I read the full manifest, freeze receipt, final binding, prepared metadata, actual dispatch receipt and all 21 listed controls through their endings, using controls for permission/status only. I independently checked the three supplied manifest/freeze/final-binding SHA-256 pins; the prepared binding's other hashes are parent metadata, not my fresh source-hash observations. After that ACK I read the sole ordered packet part in serial RAW windows of at most 20 LF from 1 through its ending at 358 before deriving. The complete S1-S4 bodies were visible, so this is nonblind. A native clock observation during work was 2026-10-30T16:44:38-0700 PDT; it is not a scientific verification or a creation timestamp. All held episodes and ALL their method, selection, proof, planning, confidence, reporting and downstream consumers remain NONINPUT; no old code, sibling proof or outgoing source link was read. The literal document was created once as a new exclusive-write artifact; no candidate/source was copied then edited. **CHILD SCIENTIFIC EXECUTION NOT RUN.** No external model, human, formal/kernel verification, parent adoption, novelty or original-target closure is claimed.
