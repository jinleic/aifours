# Exact privacy under smooth near-optimality: nonattainment and sharp TV exponent obstruction

**AUTHOR CANDIDATE — WRITTEN, PARTLY CHECKED BY EXACT RATIONAL ARITHMETIC; NOT YET INDEPENDENTLY REVIEWED.** Native pre-write clock: `Wed Oct 28 17:02:29 PDT 2026`.

## 1. Target, exact import and what is new

For every finite epsilon > 0, let `b=exp(-epsilon)` and `D={h in R^2: |h1|+|h2|<=1}`. Let F_epsilon contain EVERY Borel probability law mu with

    mu(A) <= b^(-1) mu(A+h)

for EVERY Borel A and EVERY h in the FULL CLOSED D. Put `J(mu)=integral (x1^2+x2^2) mu(dx)` and `V=inf_{mu in F_epsilon} J(mu)`.

The one research import is the already parent-WRITTEN_SUPPORTED LAW642 theorem at its exact all-law/closed-shift scope, parent disposition `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA-256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, especially lines 14–22. It states: V is finite and is attained by exactly ONE probability law mu_*, with density

    p_*(x)=Z^(-1) b^(n(x)),
    n(x)=min {k nonnegative integer: x in S+kD},

where S is a compact convex set with nonempty interior containing 0 and Z is the normalizing integral. The rest of the present construction is proved here; no selector formula, numeric threshold, external-paper theorem, or held outcome is imported. An exact proof of this theorem is NOT reproduced or formally verified here.

The previous parent S20 note `privacy-v214-S20-discontinuity-lemma-scoped-parent-v1.md` (lines 5–7, 18–26) proves that any feasible continuous-density law has cost strictly greater than V but expressly does NOT decide a positive infimum gap. The new result pays that missing infimum question, while retaining the unique all-law optimizer import. It gives C-infinity, strictly positive, **exact-epsilon** laws with an explicit cost increment, total-variation rates BOTH ways, and an attained privacy-loss event. It also rules out every universal near-optimum total-variation stability exponent greater than 1/2 even within that smooth exact-privacy subclass.

This is not a claim that the local PMLR source established these statements, an independent proof of LAW642, a novelty/priority claim, or an all-law TV stability theorem.

## 2. The construction and precise statements

Let phi be any probability density with all these properties:

1. support contained in `[-1,1]^2`;
2. `phi` is symmetric under u -> -u, so its mean is 0;
3. `kappa=integral |u|_2^2 phi(u)du` is strictly positive;
4. `alpha=integral_{u1+u2>1} phi(u)du` is strictly positive.

A concrete C-infinity choice is

    rho(s)=C exp(-1/(1-s^2)) for |s|<1, and rho(s)=0 otherwise,
    phi(u1,u2)=rho(u1)rho(u2),

where C is the reciprocal of the positive integral of the displayed one-dimensional bump. Its support, symmetry, strict positivity on (-1,1)^2 and C-infinity property are standard elementary consequences of the flat bump. Thus kappa>0 and alpha>0. The constants need no decimal evaluation.

For `t>0`, let U have density phi, independently of X distributed as mu_*, and define

    mu_t = Law(X+tU),       q_t(x)=integral p_*(x-tu) phi(u)du.

Then, at the named LAW642 import and standard facts described below, for EVERY finite epsilon>0:

**A.** Every mu_t lies in the original F_epsilon. If phi is the C-infinity bump, q_t is C-infinity and strictly positive everywhere. Each mu_t has privacy parameter EXACTLY epsilon: an actual unit-diamond shift h and an actual positive-probability Borel event E give equality `mu_t(E)=exp(epsilon) mu_t(E+h)`.

**B.** For every t>0, `J(mu_t)=V+kappa*t^2`. Consequently the infimum of J over all C-infinity strictly positive density laws having exact privacy epsilon is V, but no law in that class attains V. The same conclusion holds for all continuous-density laws with privacy at most epsilon. All assertions are for each fixed finite epsilon, not a uniform-in-epsilon estimate.

**C.** There are finite positive constants `c_epsilon, C_epsilon` (dependent also on phi), and `t0>0`, such that for every `0<t<t0`,

    c_epsilon*t <= TV(mu_t,mu_*) <= C_epsilon*t,
    W_2(mu_t,mu_*) <= sqrt(kappa)*t.

Thus `TV(mu_t,mu_*) = Theta(sqrt(J(mu_t)-V))` along this explicit smooth exact-privacy family. In particular, for ANY exponent a>1/2, no finite constant C and positive cost-gap neighbourhood can make

    TV(mu,mu_*) <= C (J(mu)-V)^a

hold for all exact-epsilon C-infinity positive-density feasible laws in that neighbourhood. This is a LOWER obstruction to possible global stability exponents. It does NOT establish any upper TV modulus over all feasible near-optimal laws, a uniform lower cost gap, or a universal W2 rate.

## 3. Privacy, regularity and exact quadratic cost

Convolution preserves the entire EVENT formulation, not just a pointwise inequality. For every Borel A and every h in D, Tonelli and feasibility of the SAME mu_* give

    mu_t(A) = integral mu_*(A-tu) phi(u)du
            <= b^(-1) integral mu_*(A+h-tu) phi(u)du
            = b^(-1) mu_t(A+h).

This works simultaneously for every closed-boundary shift, and does not rely on any common uncountable exceptional set of density versions.

The canonical p_* is positive at every point because 0 belongs to S and the dilates kD exhaust R^2; it is bounded by Z^(-1). A nonnegative normalized kernel therefore yields q_t(x)>0 for every x. For the flat C-infinity bump, convolution with its scaled compactly supported derivatives makes q_t C-infinity: differentiating acts on the bump, and bounded p_* plus L1 translation continuity of each derivative supplies continuity. The exact same argument with one weak L1 derivative yields C^1 for the separate triangular kernel below.

Independence, finite J(mu_*), bounded U and E[U]=0 give the EXACT identity

    J(mu_t)=E|X+tU|^2=V + 2t E[X] dot E[U] + t^2 E|U|^2
           = V+kappa*t^2.                                              (1)

No symmetry or mean-zero property of mu_* is needed for the cross term. The coupling (X,X+tU) immediately yields

    W_2(mu_t,mu_*)^2 <= kappa*t^2.                                     (2)

These are squared EUCLIDEAN costs and the standard Euclidean W2 distance. The PMLR theoretical objective is E||X||_1, while its angular map also preserves same-norm squared-l1 radius. Equation (1) is neither of those radial-cost statements; it does not import a first-moment minimizer or a squared-l1 staircase selector.

## 4. One actual closed-shift event spends the entire privacy budget

Since S is compact, choose B>0 strictly exceeding BOTH coordinate suprema of S, with an additional positive margin, and write

    c = max_{s in S} (s1+s2).

If x1,x2>B, every s in S lies coordinatewise below x. Thus

    dist_1(x,S) = x1+x2-c,
    n(x) = ceil(x1+x2-c).                                               (3)

Here the distance is positive and the minimum in S is attained. The first equality uses the SAME maximizer of the linear functional; the second follows from the full CLOSED dilation `S+kD`, including integer boundaries. It holds for all points in that far quadrant, not merely almost everywhere.

Take the actual full-boundary shift `h=(1,0) in D`. For every x1,x2>B+t and every u in the kernel support, both x-tu and x+h-tu lie in the far quadrant. Equation (3) and `ceil(r+1)=ceil(r)+1` give

    p_*(x+h-tu)=b p_*(x-tu),    hence q_t(x+h)=b q_t(x).                (4)

Choose ANY nonempty open bounded rectangle E in `{x1>B+t,x2>B+t}`. It is a Borel event with mu_t(E)>0 and E+h stays in that region. Integrating (4) proves

    mu_t(E)=b^(-1) mu_t(E+h).

The all-shift upper inequality of section 3 supplies epsilon privacy; this ONE actual event and shift rule out every smaller privacy parameter. Thus the budget is attained, not merely approached via a limit or inferred from numerical ratios. The result applies to every t>0 and to both kernels in this note.

## 5. Nonattainment and equality of smooth/continuous infima

For each t>0, the C-infinity mu_t belongs to the exact-epsilon subclass and, by (1), has cost V+kappa*t^2. The original lower bound gives the reverse infimum inequality. Therefore its smooth exact-privacy infimum equals V, and the same is true for the larger continuous-density, privacy-at-most-epsilon subclass.

To see nonattainment without importing S20, choose any integer k so large that `c+k>2B+8`; such a k exists. On the open far-quadrant sets just below and just above the diagonal `x1+x2=c+k`, (3) gives the distinct constants `Z^(-1)b^k` and `Z^(-1)b^(k+1)`. Both open sets accumulate at a point of the same boundary segment. Any continuous density agreeing with p_* almost everywhere would equal the corresponding constant on each open set and hence at the common boundary point, impossible because 0<b<1. This uses equality of laws/densities only up to null sets; no pointwise-version uniqueness is assumed.

By LAW642 there is exactly one original optimal LAW, mu_*. Thus no original feasible law admitting a continuous density can attain V. This completes the continuous nonattainment proof and, unlike S20 alone, also proves the exact zero INFIMUM gap with explicit approximants. The continuity proof's far-quadrant argument uses no transition threshold and no previously held diagnostic.

## 6. Quantitative upper TV rate for every t

All level sets `K_k=S+kD` are compact convex bodies. Since the closed levels are nested, the actual canonical density has the exact pointwise level representation

    p_* = (1-b)/Z * sum_{k>=0} b^k 1_{K_k}.                            (5)

For a finite-perimeter set K and any vector y, the standard BV translation inequality is

    integral |1_K(x-y)-1_K(x)| dx <= |y|_2 P(K).                        (6)

For planar convex bodies, Cauchy's perimeter formula gives Minkowski additivity, so

    P(K_k)=P(S)+k P(D)=P(S)+4 sqrt(2) k.                                (7)

Both (6) and (7) are NAMED standard geometric-analysis imports; they are not machine-certified in this note. Tonelli, (5)–(7) and `E|U|<=sqrt(kappa)` give

    TV(mu_t,mu_*)
      <= t sqrt(kappa)/(2Z) * [ P(S) + 4 sqrt(2) b/(1-b) ].             (8)

The right side is finite for each fixed epsilon because P(S)<infinity and 0<b<1. It remains valid for all t>0. This is an explicit upper bound for THIS construction; it is not a uniform bound for arbitrary near-optimizers.

## 7. Strict matching-order lower TV rate and exponent barrier

Choose the integer k from section 5. For `0<t<1/4`, use the positive-area strip

    |x1-(c+k)/2| < 1/2,
    0 < u := x1+x2-c-k < t.

Because `c+k>2B+8` and each coordinate of U has magnitude at most 1, every x-tu on this strip is in the far quadrant. Also `-2t < u-t(U1+U2) < 3t`, so the only possible shell indices of x-tu are k and k+1. The boundary equality has kernel probability zero because phi is a density. On the strip p_*(x)=Z^(-1)b^(k+1), and direct integration yields

    q_t(x)-p_*(x)
      = Z^(-1) b^k (1-b) Pr[U1+U2 > u/t]
      >= Z^(-1) b^k (1-b) alpha > 0.                                  (9)

The coordinate change `(x1,u) -> (x1,x2)` has absolute Jacobian 1; the strip has area t. Hence

    TV(mu_t,mu_*) >= [b^k(1-b)alpha/(2Z)] t.                             (10)

Combining (1), (8), (10) proves the two-sided Theta statement. The fixed k is chosen existentially from the ACTUAL imported core's compactness; the theorem is for every epsilon and does not assume k is uniform or numerically known.

For any a>1/2, (1) and (10) give

    TV(mu_t,mu_*) / (J(mu_t)-V)^a
       >= [b^k(1-b)alpha/(2Z kappa^a)] t^(1-2a) -> infinity.

Therefore any asserted all-near-optimizer bound with exponent >1/2 fails already on this C-infinity, strictly positive, exact-privacy family. No converse bound with exponent 1/2 is asserted.

## 8. Fully rational kernel and actual bounded exact checker

A separate concrete kernel has closed rational constants:

    phi_tri(u1,u2)=(1-|u1|)_+ (1-|u2|)_+.

It has total mass 1, mean zero, support `[-1,1]^2`, and `kappa=1/3`, `alpha=1/24`. Its first weak derivatives are L1, hence mu_t has a C^1 density. Equations (1), (4), (8), (10) still apply. In particular its exact cost gap is `t^2/3` and

    TV(mu_t,mu_*) >= b^k(1-b)t/(48 Z)       for 0<t<1/4.

The exact 1/24 follows by integrating `(1-u)(1-v)` over `0<u<1, 1-u<v<1`: all other sign quadrants have u+v<=1. These are explicit all-variable kernel constants, not a selected optimizer.

I executed the following bounded in-kernel Python checker using only `fractions.Fraction` and integer/rational polynomial integration; no floats, optimizer, solver, or external model were used. An initial attempted `import sympy` failed with `ModuleNotFoundError`; no installation was attempted, and the independent fractions calculation below succeeded.

```python
from fractions import Fraction as F

def integral_unit(coefficients):
    return sum((F(coef, degree + 1) for degree, coef in enumerate(coefficients)), F(0))

one_dim_norm = 2 * integral_unit([1, -1])
one_dim_var = 2 * integral_unit([0, 0, 1, -1])
alpha = integral_unit([0, 0, F(1, 2), F(-1, 2)])
b, t, k = F(1, 2), F(1, 4), 5
Z = 2 * (1 + b) / (1 - b) ** 2
base = b ** (k + 1) / Z
rise = (1 - b) * b ** k * alpha / Z
q = base + rise
print('normalization_1d:', one_dim_norm)
print('variance_1d:', one_dim_var, '; variance_2d:', 2 * one_dim_var)
print('mass_U1_plus_U2_gt_1:', alpha)
print('triangular_kernel_exact_cost_increment_t=1/4:', t*t*(2*one_dim_var))
print('synthetic_D_core_b=1/2_Z:', Z)
print('point=(3,13/4): base=',base, 'q_minus_base=',rise, 'q=',q, 'q_shifted=',b*q)
print('synthetic_lower_TV_coefficient:', (1-b)*b**k*alpha/(2*Z))
```

Actual output:

```text
normalization_1d: 1
variance_1d: 1/6 ; variance_2d: 1/3
mass_U1_plus_U2_gt_1: 1/24
triangular_kernel_exact_cost_increment_t=1/4: 1/48
synthetic_D_core_b=1/2_Z: 12
point=(3,13/4): base= 1/768 q_minus_base= 1/18432 q= 25/18432 q_shifted= 25/36864
synthetic_lower_TV_coefficient: 1/36864
```

This checker verifies only the displayed rational integrals/arithmetic and the quoted formula values. The synthetic example has core S=D and b=1/2; there `Z=(1-b) sum_{j>=0} b^j area((j+1)D)=2(1+b)/(1-b)^2=12`, and (3)–(4) apply. It is an admissible staircase LAW, **not a claim that S=D is the registered optimum**. The checker computes the tail value from the proven formula; it does not independently integrate the whole convolution, verify LAW642, prove the general assertions, or certify a novelty claim. The endpoint t=1/4 is used only for this point check; the strip lower-bound theorem itself states t<1/4.

## 9. Scope, standard imports and review frontier

Named nonresearch imports: Tonelli/Fubini, standard dominated differentiation for compact smooth kernels, elementary second moments/coupling, the BV translation estimate for indicators and the planar convex perimeter/Minkowski formula. LAW642 is the named research import and only delivers same-harness written support. The unique law/value, original full Borel events and CLOSED shifts were not narrowed. The source-optimality ceiling remains unpaid: a PMLR first-norm theorem is not promoted to a squared-l1 or squared-Euclidean theorem, and no literature firstness is inferred.

All historical quarantine findings remain historical/unvalidated and are not relied upon as proof premises. This fresh candidate does not overwrite earlier bytes or repair/relabel any prior finding. It requests an actual disjoint complete review before adoption; no formal/kernel/human/configured-family/executable full-proof or novelty certification is asserted. The exact kernel arithmetic is the ONLY machine-checked part.
