# Positive routing normal form for an actual three-state downstream chain block

Actual `/bin/date` observation before this write: **Sun Oct 25 23:51:32 PDT 2026**. MathResearch96h-2, math-1. WRITTEN AUTHOR CANDIDATE. No interpreter, calculator, eval, CAS, scientific program, solver or replay was used; there are no machine checks. All prior process findings and approximate-ZERO-credit quarantines remain.

This is an exact representation change with all actual input/exit/feedback constraints, not a spectrum-only replacement. It removes a terminal two-cycle by a nonnegative triangular routing map, at the price of unequal holdings and explicit inherited routing inequalities. It does NOT assert that arbitrary PH7 has the entry/exit shape assumed below.

## 1. Actual block and scope

Consider a raw actual Metzler matrix in an R/o/S partition, where S has three states:

    G=[ A     b      0
        r^T  −w      t^T
        D     f      F ],

    t=theta e1,        gamma_S=eta e3,
    beta=(beta_R,0,0_S),    where 0_S is a three-entry zero row,

with theta,eta>0, beta_R>=0, and every actual b,r,D,f entry nonnegative. The downstream block is the GENERAL chain-Hessenberg form

    F=[ −a   b0    0
         l   −d    e
         h    f0  −g ],                            (F)

where a,d,g>0; b0,e>0; l,h,f0>=0. Thus the 2→1 and 3→1 backward entries are retained, not suppressed. Assume F is Hurwitz. In an irreducible raw PH matrix with Perron root zero this holds for any proper principal block; this is the ordinary Perron/principal-M-matrix boundary, not a new PH theorem.

The designated entry is state 1 of S and the exit is state 3. The missing direct 1→3 edge is an ASSUMPTION, appropriate to an actual three-vertex shortest downstream path. A degree-two downstream path with a positive shortcut, arbitrary entry support, or arbitrary upstream initial support on S is NOT covered automatically.

## 2. Exact triangularization and preserved signs

The principal two-state block on S2,S3 is Hurwitz Metzler, so dg>e f0. Define exact positive algebraic quantities

    Delta=sqrt((d−g)^2+4e f0),
    lambda_plus=(d+g+Delta)/2,
    lambda_minus=(d+g−Delta)/2,
    m=(g−d+Delta)/(2e)>=0.

Because (d+g)^2−Delta^2=4(dg−e f0)>0,

    lambda_plus>=lambda_minus>0.

Also

    e m^2+(d−g)m−f0=0.

Let E32 have its sole nonzero entry 1 in row 3, column 2, and put

    M=I+m E32,       M^(−1)=I−m E32.

Direct multiplication, with no dropped term, gives

    F_new=M F M^(−1)
       =[ −a      b0           0
           l   −lambda_plus    e
         h+m l     0      −lambda_minus ].          (T)

For clarity the (3,2) entry before using the quadratic is

    f0+(g−d)m−e m^2=0.

Every other off-diagonal entry in (T) is nonnegative. Thus the old terminal two-cycle is removed, while the remaining backward entries and the induced 3→1 routing h+m l survive positively.

Embed L=diag(I_R,1,M). The FULL matrix becomes

    G_new=L G L^(−1)
       =[ A       b       0
          r^T    −w       t^T
          M D     M f     F_new ].                  (G)

Indeed t^T M^(−1)=theta e1^T, so the designated entry remains nonnegative and unchanged. All MD and Mf entries are nonnegative because M>=0. Moreover

    beta_new=beta L^(−1)=beta>=0,
    gamma_new=L gamma=gamma,

since beta has no downstream component and M e3=e3. Therefore this is an actual common-matrix transformation preserving the ENTIRE characteristic polynomial and scalar transfer:

    beta_new(yI−G_new)^(−1)gamma_new
       =beta(yI−G)^(−1)gamma.

The inverse M^(−1) need not be nonnegative. Positivity was verified on the exact affected entries, boundary vectors and couplings; it was not inferred from similarity alone.

## 3. Literal PH normalization is preserved

Suppose the original raw pair becomes Hurwitz after the physical shift T0=G−cI and has positive normalizer v=−T0^(−1)gamma>0 with beta v=1. Then

    T0_new=L T0 L^(−1),       v_new=L v>0,
    beta_new v_new=beta v=1.

Define the actual normalized pairs by diagonal scaling with v and v_new. They both have nonnegative initial/exit vectors, generator row sums equal to minus the literal exit vector, and identical transfer. No PH normalization is borrowed from a polynomial with different entries.

Equivalently the normalized change of coordinates is

    S=diag(v_new)^(−1)L diag(v),
    S>=0,       S1=1,
    T_PH,new=S T_PH S^(−1).

Its inverse may have negative entries, but the actual initial vector after this change is beta_new diag(v_new)>=0. The raw boundary calculation above proves that sign, instead of assuming all stochastic similarities preserve all initial laws.

## 4. Exact inverse routing constraints: no enlarged cone masquerading as equivalence

Removing the cycle does NOT license treating every new feedback entry as free. For each column j,

    D_new,1j=D_1j,
    D_new,2j=D_2j,
    D_new,3j=D_3j+m D_2j,

and similarly

    f_new,3=f_3+m f_2.

Thus an image must obey

    D_new,3j>=m D_new,2j for EVERY j,
    f_new,3>=m f_new,2,
    h_new>=m l.                                      (R)

These are actual entrywise routing constraints, not a selected scalar budget.

They also give a complete inverse parameterization. Choose lambda_plus>=lambda_minus>0, e>0 and

    0<=m<=(lambda_plus−lambda_minus)/e.

Set

    d=lambda_plus−e m>0,
    g=lambda_minus+e m>0,
    f0=m(lambda_plus−lambda_minus−e m)>=0,
    h=h_new−m l>=0,
    D_3j=D_new,3j−m D_new,2j>=0,
    f_3=f_new,3−m f_new,2>=0,

with the other entries unchanged. Then

    dg−e f0=lambda_plus lambda_minus>0,
    sqrt((d−g)^2+4e f0)=lambda_plus−lambda_minus,

so the m defined in §2 is exactly the chosen m, including the coincident and zero-cycle endpoints. Applying L^(−1) reconstructs the original whole matrix and its nonnegative boundary data. Full F/G stability, target characteristic and numerator identities remain required and are preserved by similarity, not asserted from (R) alone.

Consequently (T),(R) are an exact representation of this actual downstream class. Dropping (R) gives only a one-sided enlargement and cannot be used as a PH witness certificate for the original class.

## 5. Consequence for the new disjoint-cycle branch

For the equal downstream holdings of `PH7-disjoint-downstream-two-cycle-cone-v1.md`, a=d=g=b0=e=1, l=h=0, f0=sigma. Then m=sqrt(sigma), and the downstream block has holdings

    (1,1+sqrt(sigma),1−sqrt(sigma)),

with its terminal two-cycle removed and all actual cross/middle feedback routed by (R). In any actual irreducible PH7 candidate sigma<1 by proper principal stability, so all three transformed holdings are positive.

The full all-u obstruction in that manuscript's Addendum 1 already closes the original equal-holding sigma family at 8/9. This normal form therefore is NOT another attempt to rescue the closed family. Its value for further work is the exact replacement of a terminal two-cycle in the broader UNEQUAL-holding downstream class, with the common-matrix coefficient and routing constraints exposed.

The original unrestricted PH7 target still has two complete dominator strata; neither is reduced WLOG to the present entry/exit shape. Different hidden quadratics, additional off-middle cycles, shortcut entries, other path/exit arrangements and arbitrary five-state upstream blocks remain. No actual witness at 8/9 or whole-system no-go is obtained. The minimum stays in {7,8} at its named B6/upper8 imports. The triangular routing mechanism is classical matrix algebra; no novelty, priority, formal/kernel/configured-family/human/executable acceptance, new GO, clean-process claim or deadline change is made.
