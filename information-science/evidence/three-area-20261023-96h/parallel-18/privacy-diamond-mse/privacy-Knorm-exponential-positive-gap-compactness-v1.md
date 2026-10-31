# Registered full-diamond MSE: the ENTIRE exponential K-norm class has an attained minimum and a positive value gap

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 07:15:34 PDT 2026**. **NEW AUTHOR-WRITTEN SOURCE-FAMILY COMPARISON CANDIDATE**, not reviewed or parent-adopted. Exact WRITTEN symbolic geometry/integration only; no scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent, machine check or new GO.

## 0. Precise new delta and source-class boundary

The earlier159LF source comparison `privacy-AS21-JY24-norm-orders-and-continuous-nonattainment-v1.md`, SHA256 `dc2527d01b33be504a052746669716f75f519035691cd53df9627c97b370e42e`, deliberately proved ONLY nonattainment in the continuous-density class and did NOT infer a positive infimum gap for exponential K-norm mechanisms. That logical restraint remains correct for THAT proof. This NEW body supplies the additional compactness/attainment argument needed to obtain a strict exponential-family gap.

The family is the SAME centered K-norm EXPONENTIAL class actually specified in [Awan–Slavković, JASA2021](https://doi.org/10.1080/01621459.2020.1773831) / [arXivv4](https://arxiv.org/html/1801.09236v4), and [Joseph–Yu, COLT2024/PMLR247](https://proceedings.mlr.press/v247/joseph24a.html). It is not a new primary problem, an auxiliary graph family or a staircase family silently renamed K-norm. The positive PRIOR geometry/norm-selection/containment/volume/conditional-variance/sampling results remain credited. Their intrinsic-order optimum is NOT asserted to optimize unconditional MSE within this family.

**New WRITTEN result at the exact imports below:** for every finite epsilon>0, the infimum of registered squared-Euclidean MSE over ALL centered exponential norm densities that satisfy EVERY shift in FULL CLOSED D is ATTAINED within that exponential class and is STRICTLY larger than V(epsilon). A geometric constant kappa independent of epsilon describes this class minimum as kappa/epsilon². The optimal shape, kappa and the positive gap are NOT evaluated or numerically enclosed here.

This is an assurance/source-comparison consequence IMPORTING the registered all-law optimum/uniqueness. It is not an independent proof of V, new mechanism/value discovery, evaluated improvement, worldwide priority/non-equivalence/novelty or public refutation. Smooth-private infimum equality from the earlier packet remains compatible and is explicitly distinguished in §8.

## 1. Named inputs and exact theorem

Let D={z∈R²:|z1|+|z2|<=1}, finite epsilon>0. Let E_epsilon be the class of centered densities

    p_(a,H)(z)=Z_(a,H)^(-1)exp(-a||z||_H),

where a>0 is finite and H is ANY compact convex centrally symmetric genuine norm unit ball in R² with nonempty interior, and the resulting LAW is epsilon-private for EVERY Borel event and EVERY shift h∈FULL CLOSED D. Norms/shapes/rates are unrestricted within this definition; no lp or polygon ansatz is imposed.

**LAW642 (NAMED adopted research import):** `privacy-all-law-optimum-self-contained-v1.md`,642LF, SHA256 `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, at `RUN/privacy-all-law-self-contained-parent-v1.md`, SHA256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`.

Exactly used: the original ALL-Borel full-D squared-Euclidean problem has finite positive value V(epsilon), UNIQUE optimal LAW mu_epsilon, and a canonical a.e. density `Z^-1 b^n_S`, b=exp(-epsilon)∈(0,1), where S is nonempty compact and `n_S(z)=min{k>=0 integer:z∈S+kD}`. ALL-law uniqueness matters; selected symmetric uniqueness is insufficient. No scalar/root/Galois/table output or source K25/MDA/EG theorem is a premise.

**Ordinary classical imports:** norm continuity/triangle inequality; event measure order for AC laws; positive Tonelli/layer cake; elementary homothety and exact integration by parts; compact-body extreme values; **Blaschke selection theorem** in R² (every sequence of nonempty compact convex sets lying in one fixed compact ball has a Hausdorff-convergent subsequence); preservation of containment/convexity/central symmetry under Hausdorff limits. This is a named classical convex-geometry theorem, not a hidden research result or formal/kernel claim. The model-specific radius bound, shape-cost continuity and strict gap are proved below.

**Theorem — WRITTEN at precisely these imports.** There exists a finite positive geometric constant kappa, independent of epsilon, and a genuine norm ball L_* containing D such that

    min_(p∈E_epsilon) J(p)=kappa/epsilon²,
    kappa/epsilon²>V(epsilon) for EVERY finite epsilon>0.  (GAP)

The minimum is over the ENTIRE stated exponential norm class. No minimizing shape uniqueness, intrinsic-order characterization, explicit kappa, numerical gap/rate or arbitrary nonadditive-channel conclusion is claimed.

## 2. Full-D privacy calibration is an exact norm-body containment condition

The density exp(-a||z||_H) is positive continuous. If its LAW is full-D epsilon-private, then for EACH fixed h the event inequality yields

    p(z)<=exp(epsilon)p(z+h) a.e.z.

Both sides are continuous, so a strict failure at any point would persist on a positive-volume open neighborhood, contradicting the a.e. inequality. The density inequality therefore holds EVERYWHERE for this fixed h. At z=0 it gives

    exp(a||h||_H)=p(0)/p(h)<=exp(epsilon),
    a||h||_H<=epsilon for EVERY h∈D.                      (NECESS)

Conversely this inequality and the norm triangle inequality give

    p(z)/p(z+h)<=exp(a||h||_H)<=exp(epsilon)

for EVERY z and EVERY h∈D, hence actual full-Borel privacy. This proves necessity AND sufficiency, including all slanted boundary shifts.

Define L=(epsilon/a)H. Then `||z||_L=(a/epsilon)||z||_H`, so the SAME density is proportional to exp(-epsilon||z||_L), and NECESS is exactly D⊂L. Thus

    E_epsilon = {p_L(z)=Z_L^(-1)exp(-epsilon||z||_L):
                  L genuine compact convex symmetric norm ball,
                  D⊂L}.                                (ALL_SHAPES)

This absorbs every positive rate/calibration without discarding an admissible norm. D⊂L also supplies the UNIFORM Euclidean inradius rho=1/sqrt(2), since rho B2⊂D.

## 3. Exact Euclidean MSE as a geometric shape functional

For L from ALL_SHAPES write

    V_L=area(L)>0,
    A_L=integral_L |z|2² dz,
    m(L)=A_L/V_L.

Homothety gives `area(tL)=t²V_L` and `integral_(tL)|z|2²dz=t^4A_L`. The positive exponential layer identity

    exp(-epsilon r)=epsilon integral_(r to infinity)
                                      exp(-epsilon t)dt

and Tonelli give EXACTLY

    Z_L=epsilon V_L integral_0^infinity t²exp(-epsilon t)dt
        =2V_L/epsilon²,
    N_L=epsilon A_L integral_0^infinity t^4exp(-epsilon t)dt
        =24A_L/epsilon^4.

The factorial integrals follow by repeated integration by parts; all expressions are exact symbols, not a scientific program or floating calculation. Consequently

    J(p_L)=N_L/Z_L=12 m(L)/epsilon².                      (SHAPE_COST)

The family is nonempty: L=D gives the product-Laplace density proportional to exp(-epsilon|z|1), with cost4/epsilon². This follows also by adding its two scalar Laplace second moments2/epsilon². Hence the class infimum is finite and no worse than that benchmark.

## 4. Every possibly improving shape has a UNIFORM circumradius bound

Let R_L=max_(z∈L)|z|2; compactness attains it at v∈L. Since D⊂L, R_L>0. Put e=v/R_L and `L_plus=L∩{z:e·z>=0}`. Central symmetry and the zero area of its cutting line give

    area(L_plus)=V_L/2.

By convexity,

    T=(v+L_plus)/2⊂L,
    area(T)=V_L/8.

Every point z∈T has e·z>=R_L/2, hence |z|2²>=R_L²/4. Therefore

    m(L)=A_L/V_L
       >=[area(T)/V_L](R_L²/4)=R_L²/32.                 (RADIUS)

Combining with SHAPE_COST gives

    J(p_L)>=3R_L²/(8epsilon²).

Thus every shape with cost<=the product-Laplace benchmark4/epsilon² satisfies

    R_L²<=32/3.                                        (UNIFORM_R)

This is an ACTUAL bound over the ENTIRE norm-shape class, not an assumed bounded parameter range or a numerical shape scout. All potential improvements lie in one fixed Euclidean ball and contain the same fixed inball rho B2.

## 5. Hausdorff continuity of the actual MSE — proved by inclusions

Suppose L_n→L in Hausdorff distance, with every L_n containing D and lying inside the fixed radius ball. The Hausdorff limit is compact convex symmetric and contains D, so L is still a genuine norm ball, not a collapsed/singular shape.

Write eta_n=d_H(L_n,L)→0 and c_n=1+eta_n/rho. The definition of Hausdorff distance and rho B2⊂L,L_n give

    L_n⊂L+eta_n B2⊂L+(eta_n/rho)L=c_n L,
    L⊂L_n+eta_n B2⊂c_n L_n.

The Minkowski identity uses convexity and0∈L. Equivalently

    c_n^(-1)L⊂L_n⊂c_n L.

Area and nonnegative quadratic integration therefore satisfy the exact squeezes

    c_n^(-2)V_L<=V_(L_n)<=c_n²V_L,
    c_n^(-4)A_L<=A_(L_n)<=c_n^4A_L.

Thus V_(L_n)→V_L>0, A_(L_n)→A_L, and SHAPE_COST gives `J(p_(L_n))->J(p_L)`. This directly proves continuity of the ACTUAL objective on the required shape class; no weak convergence of unbounded moments, density derivative or unidentified uniform-integrability theorem is assumed.

## 6. The exponential-family infimum is ACTUALLY attained

Let S be the subset of ALL_SHAPES with J(p_L)<=4/epsilon². It is nonempty because D belongs. UNIFORM_R places every element in one fixed compact ball. Blaschke gives a Hausdorff-convergent subsequence from any sequence in S. Its limit contains D and preserves symmetry/convexity; §5's objective continuity makes it remain in S.

Take a minimizing sequence for the entire exponential class. Any term whose cost exceeds4/epsilon² can be replaced by the benchmark L=D without increasing the cost. Thus there is a minimizing sequence INSIDE S. Select a Hausdorff-convergent subsequence and apply the actual continuity proof to obtain a genuine L_*∈S attaining the ENTIRE class infimum.

Since the admissible shape set D⊂L does not depend on epsilon, SHAPE_COST makes the minimization a purely geometric problem:

    kappa=12 min_(L⊃D, L norm ball)m(L),
    min_(p∈E_epsilon)J(p)=kappa/epsilon².

The minimizing shape(s) may be chosen independently of epsilon. Their identity and uniqueness are NOT determined here. kappa is finite by the benchmark and positive because every admissible law has positive MSE; in particular the attained norm-exponential law is nondegenerate.

The compactness proof is the essential step missing from a mere nonmembership argument. Without it, nonattainment of V alone would NOT imply a strict infimum gap.

## 7. LAW642 diagonal jumps now force a STRICT value gap

Repeat the needed law argument IN BODY rather than importing the unreviewed159LF successor. For LAW642's compact S choose B above0 and both coordinate maxima, and put `c=max_(s∈S)(s1+s2)`. For x,y>B,

    dist_1((x,y),S)=x+y-c,
    n_S(x,y)=ceil(x+y-c),
    f_epsilon(x,y)=Z^(-1)b^ceil(x+y-c).

Take a far integer jump line x+y=c+ell inside that quadrant and a small open square crossing it but no other integer line. Its two open halves have distinct constant densities `Z^-1 b^ell` and `Z^-1 b^(ell+1)` a.e. A continuous density representing the same law would have to equal each constant EVERYWHERE on its respective open half, since an open deviation has positive volume. Continuity at a point of the separating line then forces equality of those distinct constants, contradiction.

Hence mu_epsilon has NO continuous density version. The actual exponential-class minimizer p_(L_*) is positive continuous and full-D epsilon-private. If its cost were V(epsilon), LAW642 ALL-law uniqueness would force its law to equal mu_epsilon, impossible. The original all-law lower bound already gives cost>=V, so

    J(p_(L_*))=kappa/epsilon²>V(epsilon).

This proves GAP for every finite epsilon>0. The positive separation is

    delta(epsilon)=kappa/epsilon²-V(epsilon)>0,

but neither kappa nor delta is evaluated, enclosed or assigned a uniform rate. No minimizing shape is guessed and no scalar numerical/root/Galois output is consumed.

## 8. Compatibility and exact source consequence

The earlier159LF smooth-class result remains compatible: independent Gaussian POSTPROCESSING of the original optimum preserves exact epsilon privacy and yields positive smooth densities of costV+2sigma², so their infimum is V without attainment. That class is NOT the norm-EXPONENTIAL shape class. Here its competitor shapes were proved cost-sublevel compact with an objective-continuous admissible limit; the smooth family instead can approach a discontinuous density and is not closed under that limit. The two infimum claims must not be conflated.

Likewise finite JOINT bin/geometric-tail families and matching-norm staircases are different actual source classes with their own recovery/attainment/gates. No generic claim that “all finite or continuous families have a gap” is made.

AS21's containment/volume/conditional-direction orders do not purport to solve this unconditional norm-EXPONENTIAL MSE shape problem, and JY24's samplers/Gaussian-ellipse MSE results retain their exact classes. This new conditional comparison proves an unrestricted-value gap for the ENTIRE exponential norm family, not a refutation of either source or a claim that their preferred intrinsic norm is the MSE minimizer. All generic geometry/sampling/optimization ancestry remains positive PRIOR.

The theorem IMPORTS LAW642 and therefore is NOT an independent lower bound or discovery of the original optimum. It is a newly proved source-family assurance consequence at that exact named input. Worldwide novelty/priority and all-creative-corollary equivalence remain UNCLEAR; no publication significance claim follows.

A fresh COMPLETE source/mathematics/dependency/application gate is REQUIRED for this new body. The159LF packet's non-gap nonclaim remains historically unchanged; only THIS later compactness proof supplies the stronger statement prospectively. No branch review or same-topic source verdict automatically accepts it.

## 9. Execution and original round

The complete calibration/moment/radius/Hausdorff/gap lead was saved BEFORE this body in checkpoint096. Exact WRITTEN symbols/fractions/integer products only; no scientific execution, machine check or algorithm. No prior source/packet/ACK/parent/other-owner byte was edited.

All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, strict auxiliary214STOP/UNADMITTED and all parent/reviewer/source/import/N4UNKNOWN/exit/old-arithmetic qualifications remain. No clean cognition/runtime/history or continuous-work census, stronger human/family/cross-vendor/formal/kernel/executable/novelty/publication assurance, new model/slot/owner or new GO.

Same eighteen owners; science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; active substantive actual-clock checkpoints at most30minutes. This is not early final-park or round closeout; the authorized registered source/priority residual continues.
