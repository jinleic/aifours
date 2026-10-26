# Candidate: every common numerator can be forced outside the plant coefficient box

Observed before creation: **2026-10-23T14:35:56-0700**. InfoSPR7, info-2, the same universal degree-seven SPR target. **CANDIDATE**, written proof only, not separately reconstructed. No executable arithmetic or search. This is a materially different ansatz obstruction after the Routh-hull branch, not a second problem slot or a universal synthesis counterexample.

## Claim and original-target gap

There is an explicit continuum of monic degree-seven interval families with **all seven lower coefficient widths positive**, all denominators strictly Hurwitz, and an actual common monic strict-SPR numerator, such that **no numerator belonging to the plant coefficient box itself works**.

Thus choosing a Kharitonov corner, the coefficient midpoint, any convex combination of corners, or any other member of that box is not a universally valid synthesis rule. This does not exclude unrestricted real degree-seven numerators; we construct one outside the box. The universal degree-seven conjecture remains unresolved. The generic failure of simple center choices may have older examples; no novelty or earliest-degree claim is made.

## Explicit families and numerator

Fix the rational constants

`m=1/(1560*13^7)`, `rho=m/1484`.

In particular `0<rho<1/100`. For every real scale `L>=1000` and `0<=u<=1`, put

`a_{L,u}(s)=s^7+L s^6+12s^5+(99L/10)s^4+44s^3`

`              +(133L/5)s^2+48s+L(177/10+u)`.                (1)

Let `B_L` consist of the independent interval box

`a_{L,u}(s)+sum_{k=0}^6 eta_k s^k`,

where `0<=u<=1`, `|eta_k|<=rho` independently. Its seven lower coefficient intervals are exactly

`[L-rho,L+rho]`, `[12-rho,12+rho]`,

`[99L/10-rho,99L/10+rho]`, `[44-rho,44+rho]`,

`[133L/5-rho,133L/5+rho]`, `[48-rho,48+rho]`,

`[177L/10-rho,187L/10+rho]`.

The constant-coordinate representation is a Minkowski sum, so every point of these seven independent intervals is included, not merely a correlated subset. All widths are positive.

An actual common numerator will be

`b_L^outside(s)=s^7+(1/(260L))s^6+12s^5+(9/(260L))s^4`

`                   +44s^3+(11/(130L))s^2+48s+3/(65L)`.      (2)

It has exact degree seven and is not in `B_L`: its `s^6` coefficient is far below `L-rho`.

## 1. Denominator stability and unrestricted synthesis are genuine

Define

`E_0(t)=-(t-1)(t-3)(t-59/10)`

`       =-t^3+(99/10)t^2-(133/5)t+177/10`,

`O(t)=-(t-2)(t-4)(t-6)`, `D(t)=(tO(t))'`.

Then the components of (1) are `E_{a_{L,u}}=L(E_0+u)` and `O_{a_{L,u}}=O`. Since `L>0`, multiplying the even component by `L` does not change its roots or signs. The strict Hermite–Biehler argument for `d=1/10`, `0<=u<=1` in the pinned Routh candidate applies verbatim: signs at `0,2,4,6` are `+,-,+,-`, so every base denominator is strictly Hurwitz.

The only quantitative import from `routh-obstruction-candidate-v1.md`, SHA256 **`47953be4805c2838a93204d077e71d2332e3468c09dc69fb973fba6563058cac`**, is its explicitly proved all-frequency inequality at `d=1/10`:

`tO(t)^2+(1/1040)D(t)(E_0(t)+u) >= m(1+t)^7`

for all `0<=u<=1`, `t>=0`. Its separate-agent reconstruction is recorded at SHA256 `cc5afd3f33275acad5033a2449cc9e03f0a1a7372fd3e9eb5dc6aa74684d7bda`; this is written evidence, not formal or parent acceptance.

Numerator (2) is precisely

`b_L^outside(s)=sO(-s^2)+(1/(1040L))D(-s^2)`.

Consequently its base-family pairings satisfy the exact identity

`P_{a_{L,u},b_L^outside}(t)`

` =tO(t)^2+(1/(1040L))D(t)L(E_0(t)+u)`

` =tO(t)^2+(1/1040)D(t)(E_0(t)+u)`

` >=m(1+t)^7`.                                               (3)

The sum of its absolute coefficients is `105+176/(1040L)<106`. For any perturbation `v=sum eta_k s^k`, `|eta_k|<=rho`, the same seven-term estimate used in the pinned candidate gives

`|P_{v,b_L^outside}(t)|<=742rho(1+t)^7=(m/2)(1+t)^7`.

Thus (2) is strictly common on the full seven-width box, with

`P_{p,b_L^outside}(t)>=(m/2)(1+t)^7>0` for every `p in B_L`.    (4)

Every denominator of the full box is also strictly Hurwitz: along `a_{L,u}+lambda v`, the strict pairings (4) prevent any imaginary-axis zero; fixed monic degree and bounded coefficients prevent a root escape to infinity. Starting from the already Hurwitz base member, root continuity gives the result. This is a denominator-stability proof, not an inference from cancellation in a transfer function.

## 2. An exact two-frequency obstruction for every numerator inside the box

Suppose a numerator `b` belongs to `B_L`. Write it as

`b=a_{L,theta}+v`, `0<=theta<=1`, `|[s^k]v|<=rho`, `0<=k<=6`.

A common numerator for `B_L` would in particular have to work with the two exact denominators `a_{L,0}` and `a_{L,1}`, which belong to the box.

Use the two exact squared-frequency values

`t_1=101/100`, `t_2=11/10`.

Let `alpha_i=-E_0(t_i)`. Direct rational substitution into the factored polynomial gives

`alpha_1=97311/1000000`, so `9/100<alpha_1<1/10`,

`alpha_2=114/125`, so `alpha_2>9/10` and `1-alpha_2=11/125>2/25`. (5)

Both `t_i` lie in `[0,2]`. On that interval `|O(t_i)|<=48`, and hence

`t_i O(t_i)^2<=4608`.

For `i=1,2` and `j=0,1`, the even part of `a_{L,j}` is `L(j-alpha_i)`, with absolute value at most `L`; its imaginary part has magnitude at most `2*48=96`. Thus

`|a_{L,j}(i sqrt(t_i))|<=L+96<=2L`.

Also each of the seven monomials in `v(i sqrt(t_i))` has absolute magnitude at most `8rho`, since `t_i<=2` and `k<=6`. Therefore

`|v(i sqrt(t_i))|<=56rho`,

`|P_{a_{L,j},v}(t_i)|<=112Lrho`.                              (6)

Put

`e_L=4608/L^2+112rho/L`.

For every `L>=1000`, using `rho<1/100`,

`e_L<4608/1000000+112/100000=716/125000<1/100`.                (7)

These are uniform symbolic bounds over the full parameter range and every perturbation coefficient.

### First frequency forces theta<1/4

The exact unperturbed pairing against the lower-constant denominator is

`P_{a_{L,0},a_{L,theta}}(t_1)`

` =-L^2 alpha_1(theta-alpha_1)+t_1 O(t_1)^2`.

If the perturbed numerator had a strictly positive pairing with `a_{L,0}`, (6)–(7) would necessarily give

`theta<alpha_1+e_L/alpha_1`

`      <1/10+(1/100)/(9/100)=19/90<1/4`.                     (8)

### Second frequency forces theta>3/4

The exact unperturbed pairing against the upper-constant denominator is

`P_{a_{L,1},a_{L,theta}}(t_2)`

` =L^2(1-alpha_2)(theta-alpha_2)+t_2 O(t_2)^2`.

Strict positivity after the perturbation would necessarily give

`theta>alpha_2-e_L/(1-alpha_2)`

`      >9/10-(1/100)/(2/25)=31/40>3/4`.                      (9)

The necessary conditions (8) and (9) are incompatible. Thus **every** numerator in the complete independent coefficient box `B_L` fails at least one of these two denominators and two exact frequencies.

This is not a frequency-grid heuristic: it is an exact finite obstruction to the explicitly quantified numerator ansatz `b in B_L`, with the remaining real numerator quantifier deliberately left untouched. Equations (2)–(4) demonstrate why it cannot be promoted to a counterexample against that unrestricted quantifier.

## Scope, prior art and review boundaries

- The plant box equals the convex hull of its coefficient vertices; hence the exclusion includes every Kharitonov corner, midpoint, arbitrary positive convex average, and any other polynomial staying inside that box.
- It excludes **only** that ansatz. It does not impose a restriction on admissible numerators in the actual book problem; the constructed numerator (2) lies outside.
- The positive result is a scaled use of the prior pinned residue inequality plus explicit full-width perturbation, not an independent new method to be counted separately.
- No priority claim is made. Prior work already constructs numerators outside plant families; the novelty of this exact all-parameter exclusion has not been cleared. The fixed-parity base family is classically synthesizable, as already acknowledged in the initial selection.
- Candidate-specific identities and inequalities above are written algebra. The quantitative imported bound is tied to its exact source hash. Independent reconstruction and parent review of this new numerator-ansatz exclusion have not occurred. No formal/kernel, human, external-model or executable verification is claimed.
