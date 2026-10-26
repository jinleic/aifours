# Independent in-harness written reconstruction: ME4

Before-creation clock observed: **2026-10-23T13:07:06-07:00**. Reviewer: `MathResearch96h`, at the parent's explicit request. No execution, numerical calculation, model CLI, nested agent or author-file edit was performed. This review is ordinary in-harness written checking, not cross-vendor, human, formal or kernel acceptance.

## Snapshot and verdict

Complete manuscript read, lines1–294:

`/Users/jinleic/repos/aifours/physics/evidence/three-area-20261023-96h/proof-GS4-maximally-entangled-reference-v1.md`

SHA256 **`684ec10f7b7ab25bf0331fdbe9f660ffbfc195c37581addd36d14cf1228debb5`**, matching the parent's requested pin.

Checkpoint read, including all requested §2–§6 (and its surrounding scope):

`/Users/jinleic/repos/aifours/physics/evidence/three-area-20261023-96h/checkpoint-001-grouped-schur-v1.md`

SHA256 **`f9f4cf45de4031459862fb86ad98556fa6dca5607271ecb9d450be53380179e5`**.

The current physics selection and the exact source statements of the imported closed sectors were also read as specified below. Hashes identify bytes only.

**Verdict: 0 FATAL /0 MAJOR /0 MINOR. No substantive defect found in the complete ME4 written argument, its strict-coverage example, or the stated boundary.** This is not verification of the assay's provenance/output or a novelty verdict. The unrestricted W4, arbitrary entangled-reference theorem and all-copy NPT conclusion remain unproved.

## 1. Convention and switched complement

For one site, direct expansion gives

    (<u| tensor I)(I-F/2)(|x> tensor I)
      =<u,x>I-|x><u|/2 = Lambda(|x><u|).

Tensoring the local swaps yields the stated unnormalized-partial-trace polarization. For C=|u><v|+|x><y| the mixed term is indeed <y,Lv>, with L=Lambda_tensor(|x><u|), not <y,L-dagger v>. The ordinary positive compression of R has block matrix [[A,L],[L-dagger,D]], whose usual complement is D-L-dagger A^-1 L. It does not give the switched matrix required in the proof.

If D-L A^-1 L-dagger is PSD, the actual Cauchy–Schwarz calculation is

    |y-dagger L v|^2
      =|<A^(-1/2)L-dagger y,A^(1/2)v>|^2
      <=(v-dagger A v)(y-dagger L A^-1 L-dagger y)
      <=(v-dagger A v)(y-dagger D y).

This closes the correctly polarized quadratic. Arbitrary covectors v,y are allowed; orthogonal input rays are not added as an assumption.

The co-Choi definition Jhat(E)=sum |b><a| tensor E(|a><b|) equals the ordinary Choi matrix of E composed with transpose. Its positivity therefore means complete copositivity, which implies positivity; it is not complete positivity of E itself. The tensor-product step below uses the co-Choi matrices and never assumes that arbitrary positive maps tensorize.

## 2. Independent one-site domination

With P0=|0><0|, A0=I-P0/2 and A0^-1=I+P0, the map products are

    M0(E00)=A0,
    M0(E0b)=-|0><b|/2 for b!=0,
    M0(Ea0)=-|a><0|/2 for a!=0,
    M0(Eab)=|a><b|/2 for a,b!=0.

These give exactly the three reducing sectors in §3. On |00>, C0=S0=1/2. On (|0a>,|a0>), C0-S0=diag(0,1) and C0+S0=[[2,-1],[-1,1]], whose determinant is1 and diagonals are positive. On Q tensor Q, the difference is I-F_Q and the sum is I. Thus -C0<=S0<=C0 holds in every first-site dimension, including dimension1 when the other sectors are absent.

## 3. Raw two-site identity, independently contracted entrywise

Expanding Lambda tensor Lambda on |ab><Omega| gives

    L_ab=delta_ab I-(E_ab tensor I+I tensor E_ba)/2+|ab><Omega|/4.

For Omega=sum_a |aa>, ||Omega||^2=4, A_eta=3I+|Omega><Omega|/4 and A_eta^-1=I/3-|Omega><Omega|/48. The identity L_ab Omega=delta_ab Omega follows because the middle terms total -|ab> and the last term is +|ab>.

Let R_ab(c,d)=L_ab-dagger|cd>. Directly,

    R_ab(c,d)=delta_ab|cd>-(delta_ac|bd>+delta_bd|ca>)/2
              +delta_ac delta_bd Omega/4.

In the row(ab,cd), column(ef,gh) co-Choi entry, the I/3 part is one third of <R_ef(c,d),R_ab(g,h)>. I independently grouped its sixteen delta products as follows (P=P12, A=F13, B=F24, F=AB):

| Products in the vector inner product | Resulting operator contribution |
|---|---|
| identity times identity | P |
| identity against either negative term, and the reverse | -(AP+BP+PA+PB)/2 |
| identity against Omega term, and the reverse | (FP+PF)/4 |
| four negative-negative products | (A+B+QF+Qprime F)/4 |
| negative-Omega products in both orders | -F/2 |
| Omega-Omega product, using norm squared4 | +F/4 |

For example AP has kernel delta_ef delta_ag delta_bc delta_dh, PA has kernel delta_ab delta_fg delta_ce delta_dh, QF has kernel delta_ad delta_bh delta_ce delta_fg, and Qprime F has kernel delta_ag delta_bc delta_df delta_eh. These are exactly the corresponding contractions; no transpose of X or omitted conjugation is used.

Since C=I-(A+B)/2+F/4,

    CP+PC-P=P-(AP+BP+PA+PB)/2+(FP+PF)/4.

The combined I/3 contribution is therefore

    (CP+PC-P)/3+[A+B-F+(Q+Qprime)F]/12.

The rank-one part of A_eta^-1 contributes -P12 P34/48: its entry is -delta_ab delta_cd delta_ef delta_gh/48, by L_ab Omega=delta_ab Omega. This proves ID at the raw matrix-entry level, independently of the assay and the later block matrices.

## 4. K and its complete orthogonal decomposition

Each of the four Bell-contraction ranges is permuted by A and B. Hence K and K-perp reduce C. Every P/Q term vanishes on K-perp, also after C or F, so ID reduces there to S=(A+B-F)/12. On joint swap eigenvalues (a,b), I obtain exactly:

    (++): C-S=1/6, C+S=1/3;
    (+-),(-+): C-S=2/3, C+S=5/6;
    (--): C-S=5/2, C+S=2.

For the four J embeddings, direct contraction gives diagonal Gram entries4 Tr(X-dagger Y), the J1/J2 and J3/J4 off-diagonals Tr(X-dagger)Tr(Y), and every other off-diagonal Tr(X-dagger Y). Thus for traceless X,Y the displayed G follows. Its four given h vectors are pairwise Euclidean-orthogonal with norm squared4, and multiplication by G gives eigenvalues6,2,4,4 respectively. This also independently validates the normalization J(h_i)/(2 sqrt(g_i)).

The identity components collapse to p,p,q,q, with norms squared16 and inner product4. Contracting against any traceless component gives a multiple of Tr X, hence zero. A Hilbert–Schmidt orthonormal traceless matrix basis therefore gives15 mutually orthogonal four-dimensional blocks plus the independent two-dimensional span of p,q. Since every Bell-contraction range is spanned by these J images, all of K is covered, with dimension62. The remaining194 dimensions are in K-perp. No representation-theoretic coverage assumption is needed.

## 5. Identity block and its exact forms

On p,q, A and B both exchange p and q, F is the identity, P12 maps p to4p and q to p, Q+Qprime maps p to2q and q to8q, and P12 P34 maps p to16p and q to4p. Substitution into ID gives precisely

    C=[[5/4,-1],[-1,5/4]],
    S=[[5/4,-3/4],[-1,1/4]].

I multiplied by the nonorthogonal Gram matrix [[16,4],[4,16]] rather than treating these action matrices as Euclidean Hermitian. The resulting forms are diag(0,15) and [[32,-22],[-22,17]]. Completing the square gives

    15|beta|^2,
    32|alpha-11beta/16|^2+15|beta|^2/8,

as claimed. This avoids an incorrect eigenvalue check in a nonorthogonal basis.

## 6. Traceless block action and both SOS expansions

The swaps preserve X and act by the stated permutations; there is no hidden transpose of X. Their eigenvalues on h0,h1,h2,h3 give C=diag(1/4,9/4,3/4,3/4).

As an independent intermediate check, in the orthonormal f basis I obtain

    P12=
      [[3/2, sqrt3/2, -sqrt6/2, -sqrt6/2],
       [sqrt3/2,1/2,-sqrt2/2,-sqrt2/2],
       [-sqrt6/2,-sqrt2/2,1,1],
       [-sqrt6/2,-sqrt2/2,1,1]],

    Q+Qprime=
      [[3,-sqrt3,0,0],[-sqrt3,1,0,0],
       [0,0,2,-2],[0,0,-2,2]],

    F=diag(1,1,-1,-1), A+B=diag(2,-2,0,0).

Here P12 P34 vanishes because Tr X=0. Applying ID to these matrices gives the manuscript's S entry for entry: diagonals1/12,5/12,1/12,1/12; entries01=sqrt3/6,12=13=-sqrt2/3,23=1/3, with the other entries zero.

After replacing f2,f3 by f_plus,f_minus, C-S has the three-by-three block stated in §7 and f_minus eigenvalue1. Expanding SOS-minus gives z1 coefficient1/2+4/3=11/6 and off-diagonals -sqrt3/6,2/3, exactly matching the block.

For C+S, SOS-plus gives z1 coefficient1/4+29/12=8/3; the z1/z_plus off-diagonal is-2/3; the z_plus coefficient is

    (29/12)(8/29)^2+57/58 =16/87+57/58=7/6.

The z0/z1 off-diagonal is sqrt3/6 and the f_minus coefficient1/2. Thus both full SOS forms are exact and nonnegative. The square-root entries are symbolic basis normalizations, not numerically recognized eigenvalues.

## 7. Tensor bridge, arbitrary maximally entangled rays and rank scope

C0 and C are strictly positive because their swap-product eigenvalues are positive. The two signed dominations make their normalized S matrices Hermitian contractions. All eigenvalues of T0 tensor TB lie in[-1,1], so I-T0 tensor TB is PSD. Congruence produces the co-Choi matrix of Lambda1 tensor LambdaB-M0 tensor M. This map is completely copositive and hence positive.

For u=|0> tensor Omega, the reference inverse factors as A0^-1 tensor A_eta^-1. Writing x as a sum of product basis vectors gives the image of |x><x| under the preceding map as exactly D-L A_u^-1 L-dagger, with the same switched orientation independently checked in §1. This is the desired all-x inequality. Rank2 enters only in expressing C using the reference ray and a second range vector; no assumption on normality, Hermiticity or real entries is used. Rank1 is a direct specialization. Adjoint invariance gives co-range.

Every maximally entangled two-ququart vector equals a nonzero scalar times (U tensor V)Omega. A first-site unitary sends any nonzero a to a scalar multiple of |0>. Each local Lambda is covariant under unitary conjugation, and simultaneous local-unitary conjugation of C preserves each unnormalized partial-trace Hilbert–Schmidt norm. This is sufficient to transport the theorem. Independent left/right conjugation is not presumed. Scaling the reference changes A and L compatibly and leaves M unchanged.

## 8. Separation example, independently evaluated by hand

Write the example as

    C=E01 tensor |Phi4><Phi4|
      +(1/3) sum_{r,s=0}^2 E_{r+1,(s+2 mod4)} tensor |rr><ss|.

The pairs u,x and v,y are orthonormal, so rank C2, norm squared2 and the range/co-range projectors are the asserted E/F. The projection of v onto E has norm squared1/12, so E differs from F and C is nonnormal.

When beta in alpha u+beta x is nonzero, its first-site components1,2,3 contain independent |00>,|11>,|22>, giving Schmidt rank at least3 across1:23. At beta0, u remains entangled across2:3. Thus E has no fully product vector; the same argument after cyclic first-site shift applies to F. Both planes have full one-site support at all three sites, so every minimal local support projection is I4 and its output-input overlap is4, not at most2.

The partial traces are independently obtained as follows:

* Tr1 C=(|11><00|+|22><11|)/3, norm squared2/9.
* Tr2 C=E01 tensor I4/4 plus three distinct matrix units |10><20|,|21><31|,|32><02|, each with coefficient1/3. These units are Hilbert–Schmidt orthogonal to the first term and each other, giving1/4+1/3=7/12. Tr3 is identical.
* Tr12 C and Tr13 C vanish because the two surviving Tr1 units are off-diagonal in each remaining index.
* Tr23 C=E01+(E12+E23+E30)/3 has norm squared1+3/9=4/3.
* The complete trace is zero.

Consequently

    q3=2-(1/2)(2/9+7/12+7/12)+(1/4)(4/3)
      =2-25/36+1/3=59/36.

This is positive and is only a calibration/sector-separation example, not a Werner counterexample.

For crossed locally orthogonal product-code spaces, a vector's Schmidt rank across1:23 equals its number of nonzero code coefficients, since the local1 and paired23 code vectors are orthonormal. A rank-one vector on that cut must be one fully product codeword. The plane E contains |0> tensor Phi4, which is rank1 across1:23 but entangled across2:3, so E cannot be contained in any such code space. The same holds for F. This validates the extra product-code qualification rather than inferring it merely from the absence of a fully product vector in E.

## 9. Source, assay and novelty boundaries

I read the retained primary Wu–Zou arXiv:2608.02647v1 text: Theorem7.2 and the minimal local support definition; Theorem7.3/Lemma7.4; AppendixC.1; and the actual locally orthonormal-code hypotheses in TheoremC.2. They match the manuscript's listed strict-coverage exclusions. I also opened the primary [ULAM.AI July31,2026 note](https://www.ulam.ai/archive/obstructions_to_werner_distillation.pdf), Theorem1.1(2), Corollary1.2 and its code-envelope formulation. Every partition into blocks of size at most2 for three sites has a singleton, and the example's minimal support on every singleton has dimension4; therefore neither plane satisfies that envelope hypothesis.

These are statement-level comparisons, not authentication of all proofs in those sources or worldwide priority. The ME4 proof is reconstructed above without using their sector theorems as mathematical premises; they enter only the baseline comparison.

I did not run, replay or verify the admitted exact assay, its r2 negative rational vector, resource receipts or process settlement. The written r4 proof stands on the explicit identities and SOS forms reconstructed here. The assay-only r3 and failed general-r2 domination are not promoted by this review. The checkpoint's historical “undecided” language remains historical; the later proof closes only the stated r4 candidate.

No new source says that arbitrary biseparable reference rays are covered. No inference from the finite-copy theorem to asymptotic NPT bound entanglement, every Werner parameter or arbitrary channel capacity is accepted. Novelty remains unresolved even though the example lies outside the named source sectors.
