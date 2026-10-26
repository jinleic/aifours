# ORIGINAL r1 WHOLE35star: exact12-to11 free-source cover and cycle elimination

Owner MathKacMoody-2. Verbatim returned metadata clock before creation: **Sun Oct 25 14:05:58 PDT 2026** (`/bin/date`). WRITTEN SOURCE-REDUCTION THEOREM CANDIDATE, not yet a creator-rank or original-kernel verdict. No scientific interpreter/program/CAS/enumeration/solver/replay/compile/CLI/nested agent/GO.

## 0. Same complete family and replacement representation

The unresolved family stays ENTIRE original r1 D3:P_(2,3,5)->S_(2,3,4), ALL s>=3, with every old/new ideal and actual integrability boundary retained. Its s1/2 controls are zero-kernel. Whole10/27 candidates retain their separate gates; no global F5/Serre/H13 result follows here.

This replaces the larger formal16 assay by an exact12-cover with ONE explicit free relation, yielding a stated ACTUAL11 basis. The earlier immutable `level5-r1-grade3-35star-complete-graph-assay-v1.md`, SHA256 `9983fe5f7e6e976bba29694cd200ae8ac29d783d566dcf380f8631dae9f19e6e`, remains the literal18-pair operator input. Its proposed16-cover was not a rank verdict; nothing there is overwritten or silently accepted.

All permanent process histories remain: actual future-only grade3 ACK and owner ACK-order overlay, separate parent r2 freeze-order finding, and the owner cadence-finding checkpoint. Prior exposure is not renamed preregistration. Classical finite-Levi/free-Lie/polynomial imports are unchanged; no old computation, full invariant form, new GO or acceptance is used.

## 1. Actual Laurent coordinate space and the full F0-zero part

Use the same harmonic Laurent model, normalized by Z_s=(z1*z2*z3)^s, with a=u2-u1,b=u3-u1,c=v2-v1,d=v3-v1 and each covector Yi=(p_i,q_i,r_i). The trace quotient eliminates r_i=-p_i v_i-q_i u_i. For the critical type mu=(3s-8,4), point degree is5 and every Y has degree1. The node1 lowering is

    F1=Dv-sum_i p_i partial_qi, Dv=a partial_c+b partial_d.

Write a whole lowest tensor as

    p1p2p3 F0 +sum_i q_i p_j p_k F_i
                              +sum_(i<j)q_i q_j p_k Fij.

The exact equations sum F_i=DvF0 and Fij=(DvFi+DvFj-DvFk)/2 give32 parameters: F0 has v-degree2,u-degree3 (dimension12), and two free F_i have v-degree1,u-degree4 (10 each). These are whole spaces, not a domain rank guess.

Put

    L_i=p_i c+q_i a, M_i=p_i d+q_i b,
    epsilon_ij=p_i q_j-q_i p_j,
    E_L=epsilon12*L3, E_M=epsilon12*M3,
    F_L=epsilon13*L2, F_M=epsilon13*M2.                           (2.1)

The F0-zero part is EXACTLY

    E_L P(a,b)+E_M Q(a,b)+F_L R(a,b)+F_M S(a,b),                 (2.2)

where the four coefficients are arbitrary quartics. To see completeness, epsilon12*Y3 and epsilon13*Y2 are the two independent copies of the SL2 standard module inside the Y cube; the third obeys epsilon12*Y3-epsilon13*Y2+epsilon23*Y1=0. Each expression epsilon12*(p3 H+q3 DvH), H=cP+dQ, is lowest because Dv^2H0, and similarly for epsilon13/Y2. The four vector components are independent on the open set ad-bc!=0. Thus(2.2) has20 parameters, exactly the kernel dimension32-12 from the explicit lowering recursion. No unproved spanning of a smaller subspace is used.

## 2. Stars supply ALL12 F0 parameters

Retain the partial graph labels of the assay:

    S1=p1*alpha21*alpha31, S2=p2*alpha12*alpha32,
    S3=p3*alpha13*alpha23,
    U123=p1*alpha21*alpha32,
    U132=p1*alpha23*alpha31,
    U213=p2*alpha12*alpha31,
    U231=p2*alpha13*alpha32,
    U312=p3*alpha13*alpha21,
    U321=p3*alpha12*alpha23.

All carry the common Z_s and a homogeneous cubic h(a,b). The p1p2p3 coefficients of S1,S2,S3 are respectively

    cd, c(c-d), d(d-c).

They are an independent basis of quadratic forms in c,d. Consequently the12-dimensional star tensor space maps ISOMORPHICALLY to every possible F0. In particular no star combination is lost in the actual harmonic/trace quotient, and any relation after the correction below lies entirely in the corrected-chain part.

## 3. Correct the six chains and prove their whole20-dimensional image

Define V_ijk=U_ijk+S_j, where j is the MIDDLE vertex of the chain k->j->i. Direct substitution alpha12=L1,alpha13=M1,alpha21=-L2,alpha23=M2-L2,alpha31=-M3,alpha32=L3-M3 gives

    V123=a(E_M-E_L), V213=a E_M,
    V312=b F_L, V132=b(F_L-F_M),
    V321=(a-b)(F_L-E_L), V231=(a-b)(F_M-E_M).                    (3.1)

For example U123+S2=(p2L1-p1L2)*alpha32=-epsilon12*a*alpha32. Thus every V has F00; all corrected chains transform by complete-copy permutations just like their original regular chain orbit.

For EACH channel X=L or M, the six generators in(3.1) give the same map

    (x,y,z) -> (a*x-(a-b)z, b*y+(a-b)z),                        (3.2)

from three cubics to two quartics. It is SURJECTIVE: for target quartics(e,f), choose

    z=e(0,b)/b+f(a,0)/a,
    x=[e+(a-b)z]/a, y=[f-(a-b)z]/b.

Each division is exact by the displayed boundary values; the result is a polynomial cubic. This is not a rational-point restriction or an unavailable coefficient computation.

The whole kernel is also explicit. From a*x=(a-b)z, coprimality gives z=a*w; the second equation forces w=b*v. Hence

    (x,y,z)=(b(a-b)v,-a(a-b)v,ab*v), v arbitrary linear.         (3.3)

Thus each12-dimensional channel has a two-dimensional kernel and a ten-dimensional image. Both channels together give the ENTIRE20-dimensional F0-zero part(2.2), with exactly FOUR tensor relations. The star12 plus corrected-chain24 therefore SURJECTS onto the whole32-dimensional actual tensor space, with no unexamined image rank or mixed relation.

## 4. Every cycle is eliminated by actual polynomial identities

Let T1=p1*alpha23*alpha32 and analogously T2,T3. Direct expansion gives

    T1+S2+S3=(a-b)(F_M-E_L).                                   (4.1)

Apply the polynomial right inverse(3.2) separately to its L/M channels. In the cubic monomial basis A=a3,B=a2b,C=ab2,D=b3, the COMPLETE four identities are

    T1*A=U123*(A-B)+U231*A-S2*B,

    T1*B=U213*(-B+C)+U123*(B-C)
               +U312*(A-B)-U132*(A-B)
               +S1*(A-2B+C)-S2*C-S3*A,

    T1*C=U213*(-C+D)+U123*(C-D)
               +U312*(B-C)-U132*(B-C)
               +S1*(B-2C+D)-S2*D-S3*B,

    T1*D=U321*D-U132*(C-D)-S3*C.                               (4.2)

The other cycle roots follow by complete-copy covariance. The S23 symmetry interchanges the first/fourth and second/third identities, as required. These are actual polynomial identities after the trace quotient, not deletion of four physical source directions. They specify every cycle output of the18-pair table using stars/chains only.

## 5. The WHOLE free source has twelve cover vectors and ONE relation

The star tensor12 is two regular copy-permutation representations; the corrected-chain tensor24 is four regular representations. Their free-Lie images therefore have dimensions4 and8, respectively, before actual relations. Let b(u tensor v tensor w)=[u,[v,w]], Pi the actual harmonic projection, and suppress common Z_s in the notation.

Use the four star cover vectors

    F_A=bPi(S1*A), G_A=bPiP12(S1*A),
    F_B=bPi(S1*B), G_B=bPiP12(S1*B).

For corrected chains put f_h=bPi(V123*h),g_h=bPiP12(V123*h), h=A,B,C,D. These are the whole12 cover, not selected actual columns.

Independently, finite Weyl/Witt extraction at stable defect(5,2) gives tensor coefficient32 and Adams3 coefficient-1, so the actual free multiplicity is(32-(-1))/3=11. The Laurent normalization makes that whole count independent of s>=3. At s3/4 the actual FINITE polynomial subspace remains the smaller5/10 space; it is not identified with the Laurent11.

The FOUR tensor relations from(3.3) lie entirely in corrected chains. One is

    (V213-V123)*(B-C)-V312*(A-B)+V321*B=0.                      (5.1)

Apply b. Complete-copy bracket permutations give

    bV213*h=g_(S12h), bV312*h=-g_(R2h),
    bV321*h=(f-g)_(S13h).

Since S12(B-C)=-(B-C), R2(A-B)=B-2C+D and S13B=-B+2C-D, equation(5.1) becomes the explicit nonzero formal free relation

    -2f_B+3f_C-f_D+g_B-3g_C+2g_D=0.                            (5.2)

The12-cover surjects onto the actual11, so its free kernel is one-dimensional. The vector(5.2) is nonzero in the formal regular-orbit basis and therefore spans that ENTIRE kernel. There is no hidden second relation or omitted image-rank assumption.

Consequently an ACTUAL COMPLETE Laurent free-lowest basis is

    F_A,G_A,F_B,G_B,
    f_A,f_B,f_C,
    g_A,g_B,g_C,g_D.                                            (5.3)

Whenever f_D appears, replace it by-2f_B+3f_C+g_B-3g_C+2g_D. This is an exact actual source basis, not the earlier formal16 treated as physical.

## 6. Exact remaining original-creator computation

Use the original local coefficient-1 and kappa=1-s, Q_ad=pi_s[(1/s)rho_x+rho_y]. On this WHOLE critical type

    L3=(s+10-8/s)I-((s-1)/s)F_y.

Every entry is now uniquely specified by the assay's COMPLETE18 ordered-pair rows, the four-term bracket identity

    F_y bP=b(K12+K13+K32)P+bP12(K23-K32)P,
    F_y bP12P=bP12(K21+K23+K31)P+b(K13-K31)P,

all cycle substitutions(4.2), V=U+S_middle, and the ONE relation(5.2). No arbitrary new testing map or unavailable actual-ideal convention remains in that11x11 computation.

The scientific residual is still the ENTIRE original35star family for ALL s>=3: prove this whole creator invertible, give another valid whole-map detector, or exhibit an actual original nonzero quotient-kernel element. No matrix entry, determinant or kernel verdict is fabricated here. The current source/frame theorem is genuine uniform progress but not the missing injectivity proof.

All actual [U,R] source and R target closures remain. If invertibility is obtained on the Laurent whole space, the explicit polynomial-subspace inclusion handles the actual s3/s4 walls; L3I3 subset I3 then descends it to the actual quotient, and the common triple-kernel identity returns to ORIGINAL D3. These are the precise conditions, not permission to skip the boundary/ideal argument.

All process overlays, actual exposure, HOLD/v9/v10/v11 and unchanged original cutoff/deadline remain. No stronger acceptance, old19/H13/globalSerre promotion, scientific execution or round closeout is implied.
