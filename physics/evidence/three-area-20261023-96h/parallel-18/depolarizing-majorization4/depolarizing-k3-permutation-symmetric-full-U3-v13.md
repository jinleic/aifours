# Actual k3 continuation v13 — the ENTIRE permutation-symmetric sector: full U3 majorization and original all-p k3

## 0. Status, exact chronology and limits

**NEW COMPLETE AUTHOR-WRITTEN CANDIDATE, NOT ACCEPTED.** One actual-state subtheorem: full U3 spectral majorization for EVERY permutation-symmetric four-qubit state (arbitrary complex Dicke coefficients, pure or mixed), hence the ORIGINAL k3 comparison at every physical p and every complex rank-three projector on that sector, its local-unitary images and their specified affine hull. The unrestricted original k3 task remains OPEN outside the separately stated families/regions. No formal/kernel/configured-family/human/executable/novelty acceptance and no park/closeout.

Actual `/bin/date` immediately before this body: **Sun Oct25 21:27:05 PDT2026**.

**Chronology, bounded and qualified.** The core argument of Sections2–4 was first worked out privately AFTER the actual21:02:55 observation and BEFORE my WORKER RECEIPT of the v110 dispatch message, which arrived while a metadata date command was running (that command returned21:05:29). Whether that private reasoning preceded the parent's21:04:02 intake/manifest creation is NOT established; checkpoint059's phrase "derived BEFORE dispatch" is therefore qualified to "before worker receipt of the dispatch message" (additive qualification recorded in checkpoint061;059's bytes are not edited). After receipt, no primary reasoning/source work continued; checkpoint059 (SHA256 `e3b0361b23999e9e989ef2a145c2c13c2dce713561efbd492795ec828d6e214f`) only SAVED the already-derived lead before the v110 ACK. The v110-B review (402LF, SHA256 `896fda88652cb1332620382dc6221fda976a425fff09bfb00f7edcfc7434d9d6`) was ACTUALLY RETURNED before the separate primary ACK observed21:23:45. THIS body is a fresh post-ACK written reconstruction of that exposed lead, NOT a preregistration, a post-ACK first discovery or a backdated proof.

Permanent findings remain: BOTH numbered-cadence lapses, historical PRIVATE WRITTEN approximate-scoping disclosure SHA256 `5b49e61483a80113eefc4a18047c7876676916fe631caaa923a46c7f783b4329` with ZERO proof/verification credit and global clean-exact-history implication withdrawn, v104 primary-pause PROCESS MAJOR SHA256 `44fb09bb6d4fb5be9c19631313e552ae4a3f155b59f15d7a52c11fa2fff3087e`, v106 inventory correction, v11 generator wording and v12 optional-row orientation qualifiers, and every parent/peer history. Correct mathematics cures none of them; no global thought/runtime/cadence-clean census is asserted.

Strict exact WRITTEN/static-source/metadata only: no scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent or GO. Same18 owners, own root, HOLD, October27 cutoff11:05:38/deadline12:35:38, 30-minute substantive cadence. Zhang's matched complementary-clipping attribution (`source-audit-v2-zhang-prior-claim.md`, SHA256 `2de2a70b2f965064bc75b1024dd005233dc94aea048e17227e4e279888bd07d5`) and unclear priority remain; no novelty claim.

## 1. Exact theorem

Let Sym denote the five-dimensional permutation-symmetric subspace of (C^2)^(tensor4), spanned by the Dicke states D0..D4. With ORIGINAL unnormalized X_j(rho)=sum_(|I|=j) rho_I tensor I_(I-complement):

**Theorem S.** For EVERY density rho supported on Sym (arbitrary complex coefficients, pure or mixed),

    lambda(X3(rho)) is majorized by (4,1,1,1,1,0,...,0)
                  =lambda(X3(|0000><0000|)).                (S)

In particular K3(X3(rho))<=6 for EVERY complex rank-three projector. Consequently, for every physical p in[0,4/3] and every complex rank-three Pi,

    Tr Pi D_p^(tensor4)(rho) <= K3(D_p^(tensor4)(|0000><0000|)),

and the same holds for all images (U1 tensor U2 tensor U3 tensor U4)rho(...)^dagger under ARBITRARY single-qubit unitaries and for the specified convex hull of all these inputs, by ORIGINAL fixed-Pi affine traces.

No restriction on C, R, eta_SP, TC epsilon, phases or rank is imposed. This is NOT a claim that a general state can be symmetrized without changing the output spectrum; symmetrization is not used as a reduction.

## 2. Pure symmetric states: an actual site-Fourier splitting of Z

Let psi in Sym be a unit vector, rho=|psi><psi|. For a qubit, sum over the four Paulis sigma A sigma = 2Tr(A)I, so Tr_i(rho) tensor I_i=(rho+sum_a S_(i,a)rho S_(i,a))/2 and

    X3=2rho+Z/2,   Z=sum_(i,a) |S_(i,a)psi><S_(i,a)psi|.      (2.1)

Fix REAL orthonormal vectors u_0=(1,1,1,1)/2 and u_1,u_2,u_3 orthogonal to u_0 (so each has coordinate sum0). These are fixed numbers, independent of psi; no vector is ever normalized. Define

    chi_(a,r)=sum_i u_(r,i) S_(i,a) psi,  a in{x,y,z}, r=0..3.

Since (u_(r,i)) is a real orthogonal4-by-4 matrix, sum_r u_(r,i)u_(r,j)=delta_ij and

    Z=sum_(a,r) |chi_(a,r)><chi_(a,r)|.                       (2.2)

This is an exact identity on the SAME twelve actual vectors, not a covariance transport or an assumed spectrum.

**The actual Gram.** Permutation symmetry of psi gives, for every site i,

    <S_(i,a)S_(i,b)>=delta_ab+i epsilon_abc r_c =: Gon_ab,

the full complex on-site matrix with the COMMON Bloch vector r (imaginary commutator terms retained). For i!=j put T_ab=<S_(i,a)S_(j,b)>. It is REAL because the commuting product of Hermitian operators on distinct sites is Hermitian; it is independent of the ordered pair (i,j) by permutation symmetry; and it is SYMMETRIC because swapping the two sites gives T_ab=<S_(j,a)S_(i,b)>=<S_(i,b)S_(j,a)>=T_ba. Since sum_i u_(r,i)=2delta_(r0),

    <chi_(a,r),chi_(b,s)>
      =delta_rs Gon_ab+T_ab(4delta_(r0)delta_(s0)-delta_rs).

Hence, for r,s in{1,2,3},

    <chi_(a,r),chi_(b,s)>=delta_rs (Gon-T)_ab,
    <chi_(a,0),chi_(b,s)>=0,
    <psi,chi_(b,s)>=r_b sum_i u_(s,i)=0.                    (2.3)

Also chi_(a,0)=J_a psi with J_a=sum_i S_(i,a)/2.

**Trace identities.** On Sym every swap acts trivially, and SWAP_(ij)=(I+sum_a S_(i,a)S_(j,a))/2. Therefore 1=<SWAP_(ij)>=(1+Tr T)/2, i.e. Tr T=1. Also Tr Gon=3. Hence

    Tr(Gon-T)=2,   sum_a ||J_a psi||^2=Tr(Gon+3T)=6.        (2.4)

The second is the familiar <J^2>=j(j+1)=6 for spin j=2, obtained here directly.

## 3. The block decomposition of the ACTUAL X3

Put H0'=span(psi,J_x psi,J_y psi,J_z psi) and H_r=span(chi_(x,r),chi_(y,r),chi_(z,r)) for r=1,2,3. By(2.3) these four subspaces are mutually orthogonal. By(2.1),(2.2),

    X3=[2|psi><psi|+(1/2)sum_a|J_a psi><J_a psi|]  on H0',
       directsum (1/2)sum_a|chi_(a,r)><chi_(a,r)|  on each H_r,
       directsum 0 on the orthogonal complement.             (3.1)

Each block is positive. By(2.4):

    Tr(H0' block)=2+6/2=5,   Tr(H_r block)=2/2=1 (r=1,2,3),

total8=Tr X3, as required. Every eigenvalue of an H_r block therefore lies in[0,1]. Every eigenvalue of X3 is at most4, because each rho_(bar i) tensor I_i has operator norm at most1.

No eigenvalue of Gon-T or of the H0' block had to be computed; only traces, positivity and the universal norm bound are used. All complex same-site XY commutators are inside Gon; nothing is replaced by a real covariance.

## 4. All Ky Fan prefixes: proof of(S) for pure states

Let k>=1 and consider any k eigenvalues of X3; suppose j of them come from the H0' block.

- j>=2: those j sum to at most the whole positive block trace5; the other k-j are each<=1. Total<=5+(k-2)=k+3.
- j=1: total<=4+(k-1)=k+3.
- j=0: total<=k.

Hence K_k(X3)<=min(k+3,8) for all k, using positivity for the cap8. The reference X3(|0000><0000|) has eigenvalues4 on |0000>, 1 on each single excitation and0 elsewhere, whose prefix sums are exactly min(k+3,8). Traces agree. This proves(S) for every pure symmetric state, with NO case distinction on C, R, eta_SP or epsilon.

Edge controls (exact): for psi=|0000>, H0'=span(|0000>,|W4>) with block 4|0000><0000|+|W4><W4| and each H_r one-dimensional with eigenvalue1, reproducing the reference exactly; zero vectors chi_(z,r)=0 cause no normalization issue.

## 5. Mixed states, local-unitary images, original channel at ALL physical p

A density supported on Sym has a spectral decomposition into pure states of Sym. For each fixed projector the map rho->Tr Pi X3(rho) is affine; K_k is the supremum of such traces, hence convex. Therefore(S) extends to every mixed rho supported on Sym.

For p in[0,1), put t=1-p and z=p/[2(1-p)]>=0. The ORIGINAL identity is

    D_p^(tensor4)(rho)=t^4[rho+zX3+z^2X2+z^3X1+z^4I].

For every rank-three Pi the universal coefficient bounds are Tr Pi rho<=1, Tr Pi X1<=10 (Ky Fan convexity in the four local marginals, pure-marginal top three4,3,3) and Tr Pi X2<=12 (from the positive full-spin-flip identity 3I-X2+3rho=(1/2)sum_(weight(P)=2)P tilde(rho)P, Pauli multipliers(27,-9,-1,3,3) after the factor1/16). With K3(X3)<=6,

    Tr Pi D_p^(tensor4)(rho)<=t^4[1+6z+12z^2+10z^3+3z^4]=t^4(1+z)^3(1+3z),

which is exactly the product-reference top-three sum, attained by the common projector onto |0000>,|1000>,|0100>. p1 gives I16/16. For1<p<=4/3 set q=2-p: full spin flip maps D_q output to D_p output antiunitarily, preserving both entire spectra.

Both the channel and X3 are covariant under arbitrary local unitaries U1 tensor...tensor U4, so spectra and the reference are unchanged for LU images. Averaging the ORIGINAL fixed-Pi/p affine traces gives the specified convex hull. No nonlinear moment of a mixed state is used to infer a decomposition.

The paper does NOT claim original all-index majorization on Sym: the needed X2 prefixes for general k are separate (and the universal X2 statements of the original problem are not re-derived here).

## 6. Exact scope controls — a genuinely new positive-defect middle-C branch

Inside Sym the theorem covers simultaneously: product states; GHZ (C=1); the vacuum-plus-W4 family of v12 (C=0, epsilon=3s^3); and, e.g., the family

    psi_theta=cos(theta)D0+sin(theta)D2, c=cos^2(theta).

For psi_theta (direct written computation): sigma_y^(tensor4)|0000>=|1111> and each weight-two basis state maps to its complement with coefficient+1, so Theta D2=D2 and

    C=(1-c)^2,  r_z=c, r_x=r_y=0,  R=4c^2,
    eta_SP=c^2-(2c^2-1+(1-c)^2)=2c(1-c),
    E2=<L^2>=c^2<(sum Z_i)^2>=16c^3,
    epsilon=E2-6R+8-4C=16c^3-28c^2+8c+4=4(1-c)^2(4c+1).

The last factorization is the exact identity (c-1)^2(4c+1)=4c^3-7c^2+2c+1. For0<c<1 both eta_SP and epsilon are STRICTLY positive, C ranges over the middle interval, and R=4c^2>0. Members with C<8/9 lie outside the v11 high-C region, outside the R=0 critical locus and outside the v10 equality locus; they are not literal members of the v12 paired-parity or W-class families (no claim about LU-inequivalence is needed or made). These are exact symbolic controls of scope, NOT approximate scouts, executed checks or channel counterexamples.

## 7. Inputs, nonclaims and the remaining original gap

The proof uses only: the single-qubit Pauli twirl identity, the SWAP/Pauli identity, permutation symmetry, a fixed real orthogonal site transform, Gram-matrix positivity/trace, X3<=4I, Ky Fan convexity/positivity, and the universal coefficient bounds/channel expansion recalled in Section5 (all re-derived in earlier packets and recalled here in writing). No TC/POL/CLIP inequality, global half-trace, uncentered-Z majorization conjecture, DDVV/Lu-Wenzel theorem, classification, program or historical unadmitted arithmetic is a premise.

The block mechanism relies on BOTH the site-independence of Gon/T and the swap invariance giving Tr T=1. For a state invariant only under a smaller 2-transitive site group (e.g. A4) the same orthogonal splitting holds but Tr T may be <1 and the H_r traces exceed1; no extension is claimed.

**Original residual:** arbitrary actual four-qubit states outside the union of separately stated families/regions (v10 eta_SP=0 locus, v11 R=0 critical locus and C>=8/9 region, v12 paired-parity and general W classes with their hulls, and this symmetric sector with its LU hull), with arbitrary complex off-face projectors and NO positive cutoff. The global full-B clipping balance Tr(X3-3rho-I)_+<=Tr(X3-3rho)_- remains UNPROVED in general; scalar moment data alone do not decide it. No all-state k3 certificate, original counterexample or all-index unrestricted composition is delivered. Each listed candidate still needs its own entire gate; branch packets do not accept their union.

This complete packet is a parkable subresult, not a park of the active original assignment.
