# Original planar DP optimum: low-privacy disk limit and explicit leading gap

**AUTHOR CANDIDATE — WRITTEN with exact rational elementary checks; NOT yet independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 17:30:24 PDT 2026`.

## 1. Exact all-law target and results

For every finite epsilon>0, put `b=e^(-epsilon)` and `D={h:|h1|+|h2|<=1}`. Let F_epsilon be ALL Borel noise laws mu satisfying `mu(A)<=b^(-1)mu(A+h)` for EVERY Borel A and EVERY shift in the full CLOSED D. Let

    V(epsilon)=inf_(mu in F_epsilon) E_mu |X|_2^2.

This is the actual registered all-law squared-Euclidean optimum, not the sensitivity-norm cost and not a radial ansatz. The limit below takes epsilon->infinity but asserts every law/inequality only for finite epsilon.

**Claim A (actual optimal value):** as b decreases to 0,

    V(epsilon) = [2/sqrt(3pi)] sqrt(b) + O(b^(3/4)).                     (1)

Equivalently `V=(2/sqrt(3pi))e^(-epsilon/2)+O(e^(-3epsilon/4))`. This resolves the open 1/2-versus-2/3 leading-coefficient interval in my prior asymptotic candidate, conditionally on the named original-optimum theorem, without using any threshold computation.

**Claim B (actual optimal law):** let mu_* be the original unique optimum and S_* its canonical core. Put `R0=(4/(3pi))^(1/4)`. Then the rescaled core converges to the Euclidean disk in symmetric-difference AREA,

    | b^(-1/4) S_*  triangle  B_2(0,R0) | = O(b^(1/8)),                (2)

and the rescaled entire optimal noise law converges to the uniform probability distribution on that disk in TOTAL VARIATION at the same rate:

    TV(Law(b^(-1/4) X_*), Uniform(B_2(0,R0))) = O(b^(1/8)).             (3)

This is not just a statement about one chosen trial core: it applies to the actual unique all-law optimizer imported below. The rate is an explicit upper rate from a coarse deficit argument, not asserted sharp.

**Claim C (radial cost separation):** for the infimum V_rad over feasible centered l1-diamond-radial laws,

    V_rad = (2/3)sqrt(b) + O(b^(3/4)),
    V_rad-V = [2/3-2/sqrt(3pi)]sqrt(b) + O(b^(3/4)),                   (4)
    V/V_rad -> sqrt(3/pi) < 1.                                           (5)

The comparison is to the centered DIAMOND-radial class only, not the union of every norm/translation. Equation (4) is an asymptotic FIXED-parameter gap, not a uniform positive additive gap over unscaled epsilon. `pi>3` follows, for example, from the perimeter of an inscribed regular hexagon.

## 2. Named inputs and exact normalizers

The essential research import is the previously parent-WRITTEN_SUPPORTED LAW642 theorem, `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA-256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, lines 14–22. At each epsilon it provides the UNIQUE actual F_epsilon optimizer with density

    p_*(x)=Z^(-1)b^(n_*(x)),
    n_*(x)=min{k>=0:x in S_*+kD},
    S_*={x: ||x||_1<=2t_*, |x|_2^2+2m||x||_infinity+T2<=V},
    m=b/(1-b),  T2=m+2m^2,  V>T2,  t_*>0.

In particular S_* is compact, contains 0 in its interior, has positive area, and satisfies `S_* subset B_2(0,sqrt(V))`. We import existence, canonical shape and uniqueness at their named written-support level; their proof and old held outcomes are NOT reverified or relabelled here.

For the radial comparison ONLY, I also use the parent-supported matching-norm per-cost staircase attainment for W_l1², `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, and the actual angular-infimum relation `V_rad=(2/3)W`, `dispositions/info-1-angular-cost-and-radial-infimum-parent-v1.md`, SHA `5e8fd8ec0cbd42af73a891acff0d8c0073d38e5e3795f558d401f6e5350374b4`. These are separate mathematical inputs, not a claim that PMLR printed a mismatched squared-Euclidean optimum. Claims A–B do NOT use MDA, v253, the threshold, or my previous unreviewed asymptotic candidate.

Elementary geometric constants, independently derived in §3 and rational-checked in §8, are

    |D|=2,       integral_D |x|_2^2 dx=2/3.                              (6)

## 3. Uniform layer estimates for ANY small core

For a compact S containing 0, define `n_S(x)=min{k>=0:x in S+kD}` and let Q_S be the normalized density b^(n_S). Every Q_S is a genuine all-event, full-CLOSED-D feasible law: `n_S(x+h)<=n_S(x)+1` for h in D, and the reverse follows from −h in D; integrate the pointwise ratio for every Borel event. This is a valid ORIGINAL input law, not a test relaxation.

Suppose `S subset B_2(0,r)` with `r<=1`. Then, for every integer k>=1,

    kD subset S+kD subset (k+sqrt(2)r)D.                                 (7)

The left inclusion uses 0 in S; the right uses `||x||_1<=sqrt(2)||x||_2`. It does not require convexity of S. Since `|aD|=2a^2` and `integral_(aD)|x|_2^2 dx=(2/3)a^4`, (7) gives uniformly

    |S+D|=2+O(r),        integral_(S+D)|x|_2^2 dx=2/3+O(r),
    sum_(k>=2) b^k |S+kD|=O(b^2),
    sum_(k>=2) b^k integral_(S+kD)|x|_2^2 dx=O(b^2),                    (8)

for b<=1/2, with constants independent of S. The geometric-polynomial sums converge.

Writing `A=|S|`, `I=integral_S |x|_2^2 dx`, the exact layer identity

    b^(n_S(x))=(1-b)sum_(k>=0)b^k 1_(S+kD)(x)

and Tonelli yield the ACTUAL cost

    J(Q_S)=[ I + (2/3)b + O(br+b^2) ] /
           [ A + 2b + O(br+b^2) ].                                       (9)

The common positive factor (1-b) cancels; no infinite signed sum or assumed support profile is used.

## 4. Explicit admissible upper law and optimizer size

Take the REAL Euclidean disk

    S_trial=B_2(0, R0 b^(1/4)),  R0=(4/(3pi))^(1/4).

It contains 0 and Q_(S_trial) is the fully feasible exact shell law just defined. Its area and second moment are

    A_trial=2 sqrt(pi/3) sqrt(b),       I_trial=(2/3)b.

Equation (9) therefore gives

    V <= J(Q_trial) = [2/sqrt(3pi)]sqrt(b) + O(b^(3/4)).                 (10)

This is an actual upper law, NOT a statement that the trial disk is the exact finite-epsilon optimizer.

For the true optimizer, write S=S_*, A=|S| and I=integral_S |x|^2. LAW642's explicit core condition and (10) yield

    S subset B_2(0,r),   r=sqrt(V)=O(b^(1/4)),   A<=pi V=O(sqrt(b)).     (11)

Conversely, (7) and (6) imply that the k=1 term of the NONNEGATIVE numerator in (9) is at least `(2/3)b`. Since V<=C sqrt(b) and the denominator is `A+O(b)`, we get `A>=c sqrt(b)` for all sufficiently small b. Thus

    0<c <= x:=A/sqrt(b) <= C < infinity,    I=O(b).                     (12)

No lower area, nondegeneracy or unknown profile was assumed.

## 5. Sharp lower constant and actual value

Among planar sets of fixed area A, the centered Euclidean disk uniquely minimizes the integral of |x|_2^2; its value is

    I >= A^2/(2pi).                                                       (13)

The elementary proof subtracts rho^2 times equal areas inside and outside the disk of radius `rho=sqrt(A/pi)`; the integrand is nonnegative on both differences.

Define the actual nonnegative deficit `Delta=(I-A^2/(2pi))/b`. The uniform bounds (8), (11) and (12) turn (9) into

    V/sqrt(b) = f(x)+Delta/x+O(b^(1/4)),
    f(x)=x/(2pi)+2/(3x),       x=A/sqrt(b).                              (14)

The constants in O are uniform for x in the compact positive interval of (12). The unique minimizer of f on x>0 is

    x0=2 sqrt(pi/3),     f(x0)=2/sqrt(3pi),
    f(x)-f(x0)=(x-x0)^2/(2pi x).                                        (15)

The upper law (10), Delta>=0 and (14)–(15) force

    V/sqrt(b)=2/sqrt(3pi)+O(b^(1/4)),
    x=x0+O(b^(1/8)),       Delta=O(b^(1/4)).                            (16)

This proves (1). The square in (15) is an identity, not a numerical fit; all possible actual core areas are covered.

## 6. The actual optimal core and probability law become a disk

Let B_rho be the centered disk with `|B_rho|=A`; put `E=|S triangle B_rho|`. By the equal-area identity,

    I-A^2/(2pi) = integral_(S minus B_rho)(|x|^2-rho^2) dx
                 +integral_(B_rho minus S)(rho^2-|x|^2) dx.              (17)

For any h>0, the planar area of the entire band `{||x|^2-rho^2|<h}` is at most `2pi h`, including h>=rho^2. Take `h=E/(4pi)`: at least E/2 of the symmetric difference lies outside that band. Equation (17) yields the quantitative stability bound

    I-A^2/(2pi) >= E^2/(8pi).                                            (18)

From (16), the deficit is `b Delta=O(b^(5/4))`; hence `E=O(b^(5/8))`. Rescaling by b^(-1/4) divides planar area by sqrt(b), so the rescaled core differs from the matching-area disk by O(b^(1/8)). Moreover x=x0+O(b^(1/8)) makes that disk's rescaled radius `sqrt(x/pi)=R0+O(b^(1/8))`. The area of the difference between the two disks is O(b^(1/8)). This proves (2).

For the actual canonical law, p_* equals 1/Z on S and at most b/Z on its complement. From the exact layer normalizer, `Z=(1-b)[A+2b+O(br+b^2)]`, so `Z-A=O(b)` and, using A=Theta(sqrt(b)), the probability outside S is O(sqrt(b)). Conditional on S the law is UNIFORM on S. After rescaling, the total-variation distance between uniforms on the rescaled core and the fixed disk is O(their symmetric-difference area), since their areas stay bounded away from 0 and infinity. Adding the O(sqrt(b)) tail mass proves (3). No almost-sure coupling or pointwise boundary convergence is claimed.

## 7. Centered diamond-radial optimum and the leading gap

Let W be the ALL-law squared-l1 optimum. MDA per-cost attainment reduces W to the minimum over centered D staircases with offset gamma in [0,1]; the actual angular relation gives `V_rad=(2/3)W`. For `m=b/(1-b)`, the scalar cost is

    W(Q_gamma)=N/(2D0),
    D0=gamma^2+2m gamma+m+2m^2,
    N=gamma^4+4m gamma^3+6(m+2m^2)gamma^2
      +4(m+6m^2+6m^3)gamma+m+14m^2+36m^3+24m^4.

The trial gamma=m^(1/4) gives `W<=C sqrt(m)`. For all gamma in [0,1] and small m,

    W(Q_gamma) >= (gamma^4+m)/[2(gamma^2+4m)].                         (19)

If gamma minimizes W, (19) and the trial upper bound force `gamma^2=Theta(sqrt(m))`: the m numerator gives the lower bound, and the gamma^4 numerator the upper bound. In that uniform regime,

    W(Q_gamma)= (1/2)(gamma^2+m/gamma^2)+O(m^(3/4))
               >= sqrt(m)+O_lower(-m^(3/4)),

by AM–GM. The trial gamma=m^(1/4) gives the matching upper bound. Thus

    W=sqrt(m)+O(m^(3/4))=sqrt(b)+O(b^(3/4)),
    V_rad=(2/3)sqrt(b)+O(b^(3/4)).

Combining with (1) proves (4)–(5). The angular identity is used for the infima, not incorrectly for arbitrary nonradial laws. No threshold, original rounded-core root evaluation, or unreviewed earlier asymptotic is needed.

## 8. Actual bounded exact arithmetic

A local Eval cell used `fractions.Fraction` only. The identity `integral_D x1^2 dx=4 integral_0^1 x^2(1-x)dx=1/3`, together with coordinate symmetry, gives the exact diamond moment 2/3. I also checked (15) for four rational controls with pi formally assigned 3 and x0=2; this is diagnostic algebra, not a proof that the actual pi equals 3.

```python
from fractions import Fraction as F
area=4*(F(1)-F(1,2))
Ix=4*(F(1,3)-F(1,4))
M=2*Ix
print('D_area=',area,'x_squared_integral=',Ix,'Euclidean_squared_moment_integral=',M)
for t in (F(1),F(2),F(3),F(5,2)):
 pi=F(3); t0=F(2)
 f=lambda z:z/(2*pi)+F(2,3)/z
 assert f(t)-f(t0)==(t-t0)**2/(2*pi*t)
print('variational square identity exact rational controls: 4/4')
print('leading optimum constant satisfies c^2 = 4/(3*pi); radial c_rad^2 = 4/9')
```

Observed:

```text
D_area= 2 x_squared_integral= 1/3 Euclidean_squared_moment_integral= 2/3
variational square identity exact rational controls: 4/4
leading optimum constant satisfies c^2 = 4/(3*pi); radial c_rad^2 = 4/9
```

The last line is a human-readable algebra label, not an additional automatic proof. No numerical solver, floating-point fit, independent-model CLI, or selected diagnostic from a held source was used. The geometric layer/compactness and total-variation conclusions are the written proof above, not machine-certified by these checks.

## 9. Exact ceiling and review request

Claims A–B depend on the named LAW642 all-law/canonical-core theorem; Claim C additionally imports the matching-norm per-cost theorem and parent angular infimum relation. They do NOT reprove those source theorems or establish that any named external publication independently obtained this asymptotic, optimal law, or source-match. No worldwide novelty, human/formal/kernel/configured-family review or parent adoption is claimed. Historical quarantines are not accepted premises. A disjoint review should inspect the uniform layer error, area lower bound, quantitative deficit, total-variation tail normalization and radial scalar minimizer bounds before any adoption.
