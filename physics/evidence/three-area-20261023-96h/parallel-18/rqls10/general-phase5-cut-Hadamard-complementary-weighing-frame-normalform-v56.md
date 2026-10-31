# RQLS10 v56 — General phase5 cut-Hadamards become complementary tenth-root weighing frames in C5

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 13:35:39 PDT 2026**. AUTHOR-WRITTEN CANDIDATE; exact written character/count/Gram arguments only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion for this proof. All historical process/math findings and ZERO-credit quarantines persist.

## 1. Exact scope and named imports

Let H be ANY BH(10,5), not assumed Gaussian, a pair product or from a preclassified list. Write zeta=exp(2pi*i/5), dephase one exponent row to0, and put D_H=span_F5{1,h_i-h_0:0<=i<10}. Assume the indicator T of some FIVE physical coordinates belongs to D_H. Its complement is the other five coordinates.

The normal-form necessity below uses only elementary phase5 orthogonality/selforthogonality, re-proved in section2. For the converse identification T inD_H, import the exact full-rank lemma of v42: ANY ten-vector phase5 ONB has context affine rank4, so dim D_H=5 and D_H=D_H^perp. The construction of a Hadamard from the stated frame data itself does NOT need that lemma. The mixed TypeI/TypeII quantum-transversal application separately imports ENTIREv55, including its named full-rank/selfdual/weighted-moment hypotheses.

The published one-class BH(10,5) report newly frozen in source-BH10-5-oneclass-reported-import-v1.json is NOT an input to ANY theorem/proof here. No Gaussian/WLOG/classification step occurs. This is a representation of a genuine residual, not an original10-dimensional no-go.

## 2. Every five-block row difference has one of exactly two count profiles

For distinct rows, v=h_i-h_j has EACH F5 value exactlyTWICE: the vanishing integer polynomial of degree<=4 is a multiple of1+x+x^2+x^3+x^4, and its coefficient sum is10. Thus sum v_t=sum v_t^2=0 inF5. Polarizing these identities after dephasing gives h_i dot h_j=0, and each h_i is orthogonal to1; also1 dot1=10=0. Hence D_H is selforthogonal, without using its rank.

Because T is inD_H, every difference satisfies

    sum_{t inT} v_t=0 inF5.

In that five-coordinate block let n_a count the value a. Then each n_a is0,1or2 and sum n_a=5. The number k of doubled values equals the number k of missing values, so k=0,1or2.

If k=0, each value occursONCE. If k=1, replacing one value b ofF5 by a different doubled value a changes the sum0 to a-b!=0, impossible.

If k=2, call the doubled values a,b, the singleton c, and the missing values d,e. They are the five distinct F5 values. The zero block sum and the sum of allF5 give

    2a+2b+c=0,
    a+b+c+d+e=0,
    a+b=d+e,
    c=-2(a+b).

Subtract c from all values. The doubled pair and the missing pair each sum0. They partition F5^*, so for some u!=0 the doubled pair is{+u,-u} and the missing pair{+2u,-2u}. Therefore the profile is exactly

    center c ONCE; c+u and c-u eachTWICE;
    c+2u and c-2u eachZERO times.                 (QP)

The complementary five-block counts are2-n_a. They are either again allONCE, or the same center with u replaced by2u.

This proves the COMPLETE two-profile assertion; no list or search was evaluated.

## 3. Exact inner products, complementary Grams and the weighing matrix

Normalize the left and right restricted row vectors by1/sqrt5, forming two10-by-5 matrices L and R whose entries are fifth roots divided bysqrt5. Set G_L=L L*, G_R=R R*.

For the allONCE profile, the restricted inner product is0. For(QP), its unnormalized value is

    zeta^c (1+2 zeta^u+2 zeta^(-u))
      =zeta^c sum_{j inF5} zeta^(u j^2).

Write G(u)=sum_j zeta^(u j^2). Its conjugate equals G(-u)=G(u), since -1=2^2 inF5. Moreover

    |G(u)|^2=sum_{x,y} zeta^(u(x^2-y^2))
             =sum_{a,b} zeta^(u a b)=5,

where (a,b)=(x-y,x+y) is bijective and all a!=0 inner character sums vanish. Thus G(u) is REAL with absolute value sqrt5, and every NONZERO normalized inner product is

    +/- zeta^c /sqrt5.

Since the nonzero squares are{1,4} and the nonsquares{2,3}, G(u)+G(2u)=2+2 sum_{a!=0} zeta^(u a)=0. Replacing u by2u therefore negates the Gauss sum. The two physical blocks give opposite nonzero inner products, as also follows directly from H H*=10I:

    G_L+G_R=2 I_10.                              (C)

Column orthogonality gives L*L=R*R=2 I_5. Hence both ten-vector collections are unit-norm tight frames with frame constant2, and G_L^2=2G_L. Define

    W=sqrt5 (G_L-I_10).

Then W is Hermitian, has zero diagonal, its NONZERO entries are tenth roots +/-zeta^c, and

    W^2=5 (G_L^2-2G_L+I_10)=5 I_10.             (W)

Thus W is a complex WEIGHING matrix of order10 and weight5, NOT a BH(10,10) matrix: it has zeros. Its complementary frame has weighing matrix -W. The diagonal of(W) says that each row has exactlyFIVE nonzero entries, since each nonzero entry has modulus1. Each vector consequently has FOUR orthogonal neighbors and FIVE mutually-unbiased-overlap neighbors among the other nine vectors. The ten rays in either restricted frame are distinct because all off-diagonal overlap moduli are0 or1/sqrt5, never1.

No step proves that the nonzero support graph of W must be bipartite/K5,5, or that the orthogonality graph is twoK5s. Those would be additional assertions, not a WLOG use of the Gaussian example.

## 4. Exact converse, including its actual phase-factorization requirement

Conversely suppose W is Hermitian, diagonal0, its nonzero entries are tenth roots, and W^2=5I. Require ACTUAL10-by-5 matrices L,R with entries fifth roots divided bysqrt5 and

    L L*=I+W/sqrt5,
    R R*=I-W/sqrt5.                              (F)

Then H=sqrt5 [L R] has fifth-root entries and H H*=10I, so it is a BH(10,5). Equations(F), including the specified fifth-root FACTORIZATIONS, are indispensable; a combinatorial support graph or an arbitrary spectral square root is not enough.

For each off-diagonal entry, the five-term sum of left root ratios is0 or +/-sqrt5*zeta^c. In the zero case its five counts are all1. In the nonzero case choose u with the matching sign of its quadratic Gauss sum; (QP) represents exactly that value. Two integer coefficient vectors representing the same fifth-root sum differ by a constant vector, and their coefficient sums are both5. That constant is therefore0. Hence the actual counts equal(QP), and their F5 first moment is0. Thus T is orthogonal to every exponent-row difference and to1: T inD_H^perp. By the separately named full-rank lemma fromv42, D_H is selfdual, so T is actually inD_H.

This proves a NECESSARY AND SUFFICIENT frame-factorization representation of phase5 Hadamards with an indicator5cut, at the explicitly named full-rank import for the reverse code-membership statement. It constructs ONE Hadamard only, not a resolved100rayQLS.

## 5. Genuine mixed-type application and exact original gap

Apply ENTIREv55 to ANY TypeI phase5 H and ANY TypeII tenth-root K whose entrywise row-product array admits evenONE quantum transversal. Its actual TypeII five-coordinate cut MUST be an indicator inD_H. Therefore H necessarily has the above complementary phase5 frames and tenth-root weighing W, ON THAT ACTUAL K CUT, up to the harmless root gauges/permutations already stated inv55.

This replaces the generic aligned mixed-type residual by an explicit C5 frame/complex-weighing representation rather than silently assuming Gaussian rows. It does NOT solve the simultaneous existence of a suitable K, its product-frame transversals, their full ten-class resolution, or global100-ray distinctness. Those are separate constraints. It also does NOT prove the absence or existence of any non-Gaussian phase5 Hadamard; no published classifier is operative here.

The physical five-coordinate cut in this representation is an algebraic indicator for a phase-code moment. It is NOT a rank5 common reducing sector of the original100ray projector commutant. Every flat cell may have nonzero components on BOTH coordinate blocks. Do not identify it with the independently accepted necessary intrinsic-sector10/4+6/5+5 alternatives, or weaken the independently unrestrictedv50 rank4 scope.

Originalmaximal1-RQLS10 remains UNKNOWN. All three unrestricted intrinsic branches areOPEN. No actual original100-ray array/resolution, unrestrictedno-go, finite witness/checker, formal/kernel/configured-family/vendor/human/priority/current-openness/novelty promotion is supplied. SameHOLD/noGO/18/exclusive-root/cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark.
