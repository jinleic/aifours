# Original Euclidean optimum: fractional third term from the actual rounded core

**AUTHOR CANDIDATE — WRITTEN with exact rational cap-coefficient control; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 17:36:29 PDT 2026`.

## 1. Exact conditional result

For the original all-Borel, every-event, full-CLOSED-unit-diamond additive-DP class, with squared-Euclidean value V(epsilon), put

    b=e^(-epsilon),  s=b^(1/4),  R=(4/(3pi))^(1/4),
    c0=2/sqrt(3pi)=R^2,   c1=8sqrt(2)/(3pi R),
    c2=8sqrt(2)/(5pi R^3 4^(2/3)) = 2^(2/3)3^(3/4)/(5pi^(1/4)).

As epsilon->infinity, the AUTHOR candidate is the genuine fractional-power asymptotic

    V = c0 s^2 + c1 s^3 - c2 s^(11/3) + o(s^(11/3)).                  (1)

Equivalently the third term is `-c2 exp(-11 epsilon/12)`. This improves the previous `o(s^3)` remainder and proves that its remainder is NOT O(s^4). It is not an endpoint-epsilon=infinity law, a numerical fit, a source-priority assertion, or a new proof of the original LAW642 theorem.

The proof imports the exact LAW642 core/rounded stationarity and my two explicitly UNREVIEWED predecessor candidates. It is a full conditional written derivation, not parent adoption or independent review. The first missing assurance is disjoint review of those entire predecessors and this fractional-cap calculation.

## 2. Exact inputs

1. Parent-WRITTEN_SUPPORTED original all-law LAW642, `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`. Its actual source `privacy-all-law-optimum-self-contained-v1.md`, SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, §§8.3–8.5 supplies the unique convex core, the full-diamond/rounded alternatives, active nonzero rounded facet, and the R-branch stationarity below. The associated original proof and standard-analysis imports stay at their prior same-harness written-support scope.
2. My own UNREVIEWED `frontier-20261028-euclidean-low-privacy-disk-limit-v1.md`, SHA `b277d099eb211302b73754a971f63d81dc781f160a5096ad6f30db85de85d7b3`: actual optimal scaled cores converge in area to the disk R B and are uniformly bounded; `V/s^2->R^2`.
3. My own UNREVIEWED `frontier-20261028-euclidean-second-term-and-disk-law-v1.md`, SHA `188cd3ff1648e9f46ac00fdc1d0068272715559143fe9ec5643a7af03740b4d4`: upgrades the actual convex cores to Hausdorff convergence to R B and establishes `V/s^2=R^2+c1 s+o(s)`. It also proves a genuine exact feasible disk-shell upper law. This third-term calculation depends on these actual-law results; no claim of their review/adoption is made.

No MDA cost theorem, Kulesza mean-norm result, mixed-cost threshold, held diagnostic outcome, or source-equivalence conclusion is used in (1). Standard imports: finite-dimensional convex support/Hausdorff facts, elementary polygon-strip integration, dominated estimates, and Taylor expansion of square roots.

## 3. Actual rounded-facet scale from the existing stationarity

LAW642 gives

    S_*={x: ||x||_1<=2t,
             |x|_2^2+2m||x||_infinity+T2<=V},
    m=b/(1-b), T2=m+2m^2.

The preceding actual-core Hausdorff limit is a Euclidean disk of positive radius R. Consequently the full-diamond branch cannot occur along any sequence b->0: the ratio of support at an axis and at a diagonal normal of any homothetic diamond is sqrt(2), whereas the disk ratio is 1. The LAW642 alternatives therefore put S_* eventually on its ROUNDED branch with an active nonzero facet.

For that branch, let `d=t-c` be the positive terminal facet width in the notation of source §8.4. The actual junction point is `(t+d,t-d)`, and source stationarity is

    P(d)=C0+t v,
    P(d)=(4/3)d^3+2m d^2+m^2 d,
    C0=m/3+(3/2)m^2+m^3,       v=m+m^2.                                (2)

The active facet's scaled support in each diagonal-normal direction is `sqrt(2)t/s`. Hausdorff convergence of S_*/s to R B gives

    t/s -> R/sqrt(2).                                                     (3)

Also 0<d<t, so d->0. Divide (2) by m: the two noncubic P terms tend to 0 and `C0/m+t v/m ->1/3`. Hence

    d^3/m -> 1/4,       d = 4^(-1/3)s^(4/3)(1+o(1)).                  (4)

No selected parameter, threshold root or formal-series solution is assumed.

## 4. Actual clipping depth and comparison to a clipped disk

Set `K=S_*/s`, `R_b=sqrt(V-T2)/s`, and let the diagonal facet cut the comparison disk at distance

    a_b=sqrt(2)t/s,    delta_b=R_b-a_b.

The arc/facet junction obeys

    V-T2=2t^2+2d^2+2m(t+d).                                              (5)

Rationalizing the difference and using (3)–(4) yields

    delta_b = [2d^2+2m(t+d)] /
              [s(sqrt(2t^2+2d^2+2m(t+d))+sqrt(2)t)]
            = D0 s^(2/3)(1+o(1)),    D0=4^(-2/3)/R.                   (6)

The previous second-term candidate also gives `R_b=R+O(s)`. The scaled true core is

    K={z: ||z||_1<=2t/s,  |z|_2^2+2(m/s)||z||_infinity<=R_b^2}.

Since m/s=O(s^3) and K is uniformly bounded, it is sandwiched between `B_(R_b-Cs^3) intersect {||z||_1<=2t/s}` and the analogous B_(R_b) intersection, for a fixed C. Their symmetric-difference area and |z|^2-moment are O(s^3). Thus, to order s^(5/3), K may be compared to a Euclidean disk of radius R_b cut by four equal, disjoint diagonal caps of depth delta_b. This is an error estimate for the ACTUAL core, not an assertion of exact circularity.

## 5. Quantitative circular-cap deficit

Let a disk of radius r be cut by a line at inward depth delta>0. Using normal coordinate u=r-n·z in [0,delta] and tangential coordinate y,

    r^2-|z|^2 = 2ru-u^2-y^2,    |y|<=sqrt(2ru-u^2).

The integral of the nonnegative radial deficit on one cap is

    (4/3) integral_0^delta (2ru-u^2)^(3/2)du
      = (8/15)(2r)^(3/2) delta^(5/2) [1+O(delta)].                    (7)

Four caps therefore have leading coefficient `(32/15)(2R)^(3/2)`. Their total area is O(delta^(3/2))=O(s). Let A=|K|, I=integral_K |z|^2 dz, and A0=pi R^2. The exact equality `2/3=pi R^4/2` implies the full-disk part of `I+2/3-R^2 A` is `(pi/2)(R_b^2-R^2)^2=O(s^2)`. Replacing R_b^2 by R^2 in each removed cap adds only `O(s)*O(delta^(3/2))=O(s^2)`. The O(s^3) true-core-to-clipped-disk discrepancy is still smaller. Using (6)–(7) gives

    (I+2/3)/A
      = R^2 + [32(2R)^(3/2)/(15 A0)] delta_b^(5/2)
              + o(s^(5/3)),       A=A0+O(s).                             (8)

All four caps are disjoint for sufficiently small s, because delta_b->0 and R>0.

## 6. Tail first variation and the fractional coefficient

For a uniformly bounded convex K containing 0, the diamond's four-edge geometry gives the UNIFORM first-variation estimate

    M(D+sK)=M(D)+s sum_(edges e) h_K(n_e) integral_e |y|^2 ds_y+O(s^2), (9)

where `h_K(n)=sup_(z in K)n·z`. To see the O(s^2) directly: on every edge, supporting points of K and segments from 0 fill the outward strip up to the support height except within O(s) of the vertices; the polygon support inequalities supply the reverse inclusion. All excluded vertex neighborhoods have area O(s^2), and |x|^2 is smooth and uniformly bounded there. Thus no differentiability or smoothness of K is required; convexity/0 in K are used for the filled strips.

All four active diagonal supports of this actual K equal `a_b=R_b-delta_b`, and the four edge integrals total `8sqrt(2)/3` (previous candidate §3). Therefore

    M(D+sK)=2/3+(8sqrt(2)/3)s(R_b-delta_b)+O(s^2).                    (10)

The exact shell layer ratio, with `A=|K|=A0+O(s)`, gives uniformly

    V/s^2 = [I+M(D+sK)]/A + O(s^2).                                     (11)

Substitute (8) and (10), then use R_b=R+O(s):

    V/s^2 = R^2+c1 s
      + [32(2R)^(3/2)/(15 A0)] delta_b^(5/2)
      - [8sqrt(2)/(3 A0)] s delta_b + o(s^(5/3)).                      (12)

Let `delta_b=D0 s^(2/3)(1+o(1))`. From `D0^(3/2)=1/(4 R^(3/2))`, the cap-cost coefficient in (12) is exactly 2/5 of the magnitude of the negative support term. The net is

    - (3/5)[8sqrt(2)D0/(3 A0)] s^(5/3)
    = -c2 s^(5/3).

Multiplying by s^2 gives (1). The O(s^2) terms omitted from V/s^2 are o(s^(5/3)), because 2>5/3. The coefficient is strictly negative since R>0.

## 7. Bounded exact arithmetic and review boundary

A local Python `fractions.Fraction` cell checked only the elementary cap-integration coefficients and their stationary-scale ratio:

```python
from fractions import Fraction as F
one_cap=F(4,3)*F(2,5)
four_cap=4*one_cap
ratio=(four_cap/F(8,3))*2*F(1,4)
print('one_cap_integral_coefficient=',one_cap)
print('four_caps_coefficient=',four_cap)
print('at stationary scale cap_cost_fraction_of_support_gain=',ratio)
print('net_negative_fraction_of_support_gain=',1-ratio)
```

Actual output:

```text
one_cap_integral_coefficient= 8/15
four_caps_coefficient= 32/15
at stationary scale cap_cost_fraction_of_support_gain= 2/5
net_negative_fraction_of_support_gain= 3/5
```

This machine check does NOT verify the LAW642 stationarity, rounded-branch selection, uniform convex first variation, cap asymptotic or full original theorem. Those are the written steps above and explicit imported predecessors. No independent model/CLI, external publication, formal kernel or novelty review was performed. A disjoint reviewer must inspect (2), the true-core sandwich, uniform O(s^2) first variation, all exponents and the constants before any parent adoption.
