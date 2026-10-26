# OUTER-1 candidate: global objective calibration removes the entire multilevel head

Observed clock before creation: **2026-10-24T05:49:18-0700**.

## 0. High-risk new claim, imports, and assurance ceiling

**HIGH-RISK AUTHOR CANDIDATE.** This manuscript claims the named assertion C for EVERY finite ε>0, hence V=W1. It is NOT covered by the MathShor review of the269-line W1 calibration, which explicitly left equality unproved. No independent reconstruction or parent acceptance of the NEW argument below is claimed.

The proof is a GLOBAL signed-objective comparison for the full selected optimal head, not a fixed-profile optimum, local stationary condition, selected-family example or epsilon variant. It does not depend on the269-line one-core critical-system calculation. If this argument and that separate calibration are both accepted, their composition would evaluate the supported outer minimum through the screened one-core systems.

Imports: the original attained all-law optimizer and simultaneous closed pointwise-private D4 canonical levels from D0; the diagonal-Steiner geometry of Addendum3; and the supported finite-parameter theorem E. Their frozen snapshots and parent composition remain unchanged. The backward raising operation in closed-level Addendum1 §5 (D0-R7, unused by E itself) is NOW explicitly relevant; its exact competitor argument is supplied again in Section2 at the interface used here. No unused antecedent is silently promoted.

Binding attribution: both selector comparisons are PRIOR Amir-Rietzke2025 Theorem1(i)+Lemma1(iii) corollaries; attainment is a statement-level ElSalamouny-Gambs Theorem8 prior consequence; shell/Minkowski ancestry is PRIOR. The calibration verification below is elementary, not a claimed new general control method. Full-result priority/NOVELTY_UNCLEAR and all evidence errata/HOLD remain operative. No scientific program, arithmetic/CAS, numerical solve/integration, test, replay, CLI or nested agent was used.

## 1. Original optimizer and exact canonical order

Fix ANY b∈(0,1), ε=-log b. Let J=V(ε), and take the genuine global optimum supplied by the supported structural packet:

```
q(z)=alpha*b^n(z),   alpha>0,
K_i={n<=i},   i>=0.
```

The SAME levels are compact, measure-regular, D4-invariant and have coordinate and diagonal contractions. Their first-octant profiles F_i on[0,t_i] satisfy

```
F_i(t_i)=t_i,   t_i<=F_i(y)<=2t_i-y,
F_i nonincreasing and1-Lipschitz,
t_(i+1)>=t_i+1/2,
F_(i+1)(y)>=F_i(y)+1 on[0,t_i].
```

Every t_i>0 and t_i→infinity. The exact forward condition is

```
K_(i+1) ⊂ (K_i+D) union B_sqrt(J).
```

No one-core identity or convexity of these bodies is assumed.

Put r(z)=max(|z1|,|z2|), s(z)=|z1|+|z2|. Each canonical K is an ideal for the product order of(r,s). To see this directly, if(a,c)∈K with a≥c≥0, then K contains

```
{z:r(z)<=a, s(z)<=a+c}.
```

Below height c this follows by coordinate contractions; above c, the boundary segment from(a,c) to(c,a) gives x=a+c-y, and contractions fill beneath it. D4 covers all sectors. This argument does not assume the whole K convex.

Consequently, for a first-octant point z=(x,y), x≥y≥0,

```
z+D ⊂ H  <=>  (x+1,y)∈H
```

for every canonical level H. Indeed every z+h has r≤x+1 and s≤x+y+1, so its invariant pair is dominated by that of(x+1,y). Necessity uses h=(1,0).

## 2. Global optimality forces EXACT unit cap increments

We first prove

```
F_(i+1)(y)=F_i(y)+1,    every0<=y<=t_i, every i>=0.       (A)
```

Suppose the inequality were strict somewhere. By continuity and t_i>0 it is strict on an interior height interval. Choose there a target point(x,y) strictly between the right cap F_i(y)+1 of K_i+D and the cap F_(i+1)(y), with a positive margin from both. The exact cap/line geometry of Addendum3 makes this point outside K_i+D and inside K_(i+1). The forward condition puts it in the cost ball.

Now z=(x-1,y) remains in the first octant, since x>F_i(y)+1≥t_i+1≥y+1. It is outside K_i, but z+D⊂K_(i+1) by the canonical-order criterion above. Its cost is STRICTLY below J: subtracting one from the positive x coordinate lowers squared cost, and the target cost was at most J. These strict margins persist on an open positive-area set U of such z.

On U the old index is i+1: it is outside K_i and in K_(i+1). Raise q there to alpha*b^i. Every neighbor in z+D has old height at least alpha*b^(i+1), so all directed privacy inequalities involving a raised endpoint hold; at an unchanged endpoint the opposing value only increased, and pairs with both endpoints raised have ratio1. Thus this is a genuine all-shift-private unnormalized competitor. The added mass/moment are finite, and its actual normalized cost change is

```
∫_U (|z|²-J)(alpha*b^i-q(z)) dz
--------------------------------------------------- < 0.
          1+∫_U(alpha*b^i-q(z))dz
```

This contradicts ORIGINAL global optimality. Hence(A) holds in the interior and then at all endpoints by continuity. This is precisely the backward-raising operation with a verified positive-area cost improvement, not an assumption that necessary obstacles define the optimum.

As a consequence t_(i+1)≤t_i+1, by evaluating(A) at t_i and using monotonicity of F_(i+1). In particular this is compatible with, but does not alone settle, the known maximal-decay obstruction.

## 3. A single global offset function represents ALL remaining head freedom

For y≥0 choose any i with y≤t_i and define

```
f(y)=F_i(y)-i.
```

Equation(A) makes this independent of the chosen active i. On any bounded y interval choose one large i covering it; therefore f is globally continuous, nonincreasing and1-Lipschitz. It satisfies f(t_0)=t_0 and

```
f(t_i)=t_i-i.
```

For x≥y≥0 the exact closed-level index is

```
n(x,y)=max(0,ceil(x-f(y))).                              (B)
```

Indeed membership in K_i means both y≤t_i and x≤f(y)+i. Since x≥y, the latter ceiling is at least ceil(y-f(y)), which already ensures the former. Thus the formula retains every birth index and endpoint; no inactive constraint is discarded.

For y≥t_0 put

```
g(y)=y-f(y).
```

Then

```
g(t_0)=0,
1<=g'(y)<=2 almost everywhere,
y-t_0<=g(y)<=2(y-t_0).
```

The derivative bounds are the actual nonincreasing1-Lipschitz properties of f, so g is absolutely continuous and strictly increasing. In particular y≥g(y)/2. No finite-head shape has been set to a chosen curve; arbitrary head freedom is now the allowed trajectory g.

Keeping f below t_0 and replacing it above t_0 by2t_0-y produces exactly the one-core law generated by S=K_0. It has g_fast(y)=2(y-t_0). The remaining question is a GLOBAL objective comparison between these two trajectories.

## 4. A universal feasible cost ceiling, not an extra epsilon bound

Write

```
m=b/(1-b),  v=m+m²,  T2=m+2m²,
lambdaP=T4/(3T2)=4m²+4m+1/3.
```

The point-core density b^ceil(|z|_1), with its null origin convention, is genuinely full-D-private and has finite raw mass2T2 and moment(2/3)T4. Thus

```
0<=J<=lambdaP.
```

This is only an available feasible-law ceiling needed in the calibration below, not a new envelope result. No W1 formula, scalar stationary optimum or numerical parameter is used to obtain it.

## 5. Signed row cost and the fast-tail potential

Fix ANY0≤lambda≤lambdaP for this section. For g≥0,y≥0 define the signed first-octant row cost

```
R_lambda(g,y)=∫_0^infinity [(y+z)²+y²-lambda] b^ceil(z+g) dz.
```

Values at individual jump points do not affect the integral. For g in an open phase, write

```
j=ceil g,   gamma=j-g in(0,1),
P(G=k)=(1-b)b^k.
```

The row has the exact positive layer representation with lengths gamma+G. Hence

```
R_lambda(g,y)=b^j E[ ((y+gamma+G)³-y³)/3
                      +(y²-lambda)(gamma+G) ],
partial_g R_lambda
=-b^j[(y+gamma+m)²+y²+v-lambda].                        (C)
```

R is continuous across integer phases: the geometric reindexing identity E h(G+1)=E h(G)/b applies to each length polynomial h with h(0)=0. It is piecewise smooth; no delta term is created when differentiating a phase integral whose endpoint values agree.

Define the fast-tail potential

```
Hfast_lambda(g,y)=∫_0^infinity R_lambda(g+2u,y+u)du.
```

All integrals and derivatives used below converge. For example

```
|R_lambda(g,y)|
 <= b^g[(2y²+lambda)/epsilon+2y/epsilon²+2/epsilon³],
```

because b^ceil(z+g)≤b^(z+g). The derivative in(C) has a similar geometric-polynomial bound. Dominated differentiation on phase interiors, with cancellation of moving endpoint terms, is therefore legitimate. The potential is continuous, piecewise C1 and locally Lipschitz; its derivative bounds extend finitely to phase boundaries.

The fast-flow identity

```
Hfast(g+2h,y+h)=Hfast(g,y)-∫_0^h R(g+2u,y+u)du
```

gives

```
partial_y Hfast+2 partial_g Hfast+R=0.                  (D)
```

We next prove the load-bearing sign partial_g Hfast<0 on the ENTIRE relevant state region g>0,y≥g/2, not just on the reference trajectory.

## 6. Exact derivative and strictly positive polynomial certificate

For g>0 in a phase, j=ceil g≥1, gamma=j-g∈[0,1], and put t=y+gamma/2. The state restriction gives t≥j/2≥1/2. Define

```
A(t)=2t²+2mt+T2-lambda,
Cdiag(t)=2t²+2(1+2m)t+4m²+4m+2/3,
K(t,gamma)=m(Cdiag(t)-lambda)
           +A(t)gamma+(m/2)gamma²+gamma³/6.
```

Then the exact derivative is

```
partial_g Hfast_lambda(g,y)=-(b^j/2)K(t,gamma).         (E)
```

Here is the full summation check. The initial partial phase contributes

```
-(b^j/2)[A(t)gamma+(m/2)gamma²+gamma³/6].
```

At state j and height t, the subsequent complete phase ell≥1 contributes

```
-(b^(j+ell)/2)[A(t+ell/2)+m/2+1/6].
```

Using EXACTLY

```
sum_(ell>=1)b^ell=m,
sum_(ell>=1)ell*b^ell=v,
sum_(ell>=1)ell²*b^ell=m+3m²+2m³,
```

that complete tail is-(b^j/2)m(Cdiag(t)-lambda), proving(E). There is no missing factor1-b: it is already present in the row's geometric expectation before the phase sum.

Now K increases with t and decreases with lambda. Since t≥1/2 and lambda≤lambdaP,

```
K(t,gamma)
 >= K(1/2,gamma;lambdaP)
  =2m²(1-gamma)
    +m(11/6-2gamma+gamma²/2)+(gamma+gamma³)/6
 >=m/3>0,    0<=gamma<=1.                              (F)
```

The last inequality uses that11/6-2gamma+gamma²/2 decreases on[0,1] and equals1/3 at1. Also

```
partial_t K=m[4t+2(1+2m)]+gamma(4t+2m)>0,
partial_lambda K=-(m+gamma)<0.
```

Thus(E)-(F) prove partial_g Hfast<0 everywhere needed. The initial state g=0 needs only continuity of the value, not a derivative sign. Integer crossings along g(y) are isolated since g'≥1; the phasewise identities suffice for integration.

## 7. GLOBAL comparison of every admissible remaining head trajectory

Use lambda=J. Along the arbitrary trajectory g(y) of Section3, the chain rule and(D) give almost everywhere

```
R_J(g(y),y)+d/dy Hfast_J(g(y),y)
 =(g'(y)-2) partial_g Hfast_J(g(y),y) >=0.              (G)
```

Both factors on the right are nonpositive. This comparison holds along the WHOLE unknown trajectory because y≥g/2, not merely at the fast reference or an infinitesimal perturbation. On each bounded interval there are finitely many integer phase crossings; continuity and local Lipschitz regularity of the potential make their boundary terms telescope. There is no assumption of a smooth original density or trajectory.

The terminal value vanishes. Indeed the bound above gives

```
|Hfast_J(g,y)|<=C_(b,J)*b^g(1+y²),
```

and g(y)≥y-t_0. Integrating(G) from t_0 to infinity therefore yields

```
∫_(t_0)^infinity R_J(g(y),y)dy
 >= Hfast_J(0,t_0)
  =∫_(t_0)^infinity R_J(2(y-t_0),y)dy.                (H)
```

The difference is exactly the integral of the nonnegative right side in(G). It is STRICT if g'<2 on a positive-measure set, because(E)-(F) are strictly signed for every positive state.

This is a complete tail objective inequality for every allowed head, not a local maximum-decay argument. The earlier feasible square+tail control does not contradict it: maximal decay alone did not constrain cost, whereas(H) uses the actual signed objective and the valid cost ceiling.

## 8. Actual one-core competitor, normalization, and assertion C

In the first octant, the raw original density is given by(B). For y≤t_0 it agrees EXACTLY with the raw one-core density generated by S=K_0, because every active profile there is F_0(y)+i. For y>t_0, the original row is b^ceil(z+g(y)); the S-generated one-core row is b^ceil(z+2(y-t_0)). D4 supplies the other sectors; their interfaces have zero area.

The one-core law is genuinely original-feasible: its closed levels S+iD obey all full-shift inclusions, cover the plane, and have positive finite normalizer and finite moment. It has no independently assigned plateau masses. Since the original density is alpha times its raw geometric density,

```
N_original-J Z_original=0.
```

Multiplying(H) by8 and adding the unchanged pre-top rows gives

```
N_onecore-J Z_onecore <=0.
```

After its ACTUAL normalization, this feasible law has cost≤J. But J is the original all-law minimum, so the inequality must be equality. Strictness in Section7 forces g'=2 almost everywhere above t_0. Absolute continuity and g(t_0)=0 then give

```
g(y)=2(y-t_0),   f(y)=2t_0-y,   every y>=t_0.
```

Using f(t_i)=t_i-i proves t_i=t_0+i/2, and every profile is now

```
F_i(y)=i+F_0(y),         0<=y<=t_0,
F_i(y)=i+2t_0-y,         t_0<=y<=t_0+i/2.
```

Thus K_i=K_0+iD EXACTLY for the selected canonical global optimum. This establishes the literal OUTER-1 assertion C. Its parameter vector belongs to the supported finite class, and exact inner minimization/uniqueness identifies its profiles with the supported minimizing selectors; no tight-support-only shortcut is used.

Consequently V=W1. This last identification uses only the definition of the entire canonical one-core minimum: the original problem contains that class, and the original global optimum just proved belongs to it. It does NOT depend on the269-line W1 stationary-system proof. If the independently reviewed W1 calibration is composed after acceptance of this NEW argument, its unique arc/facet core and screened scalar equations determine the original V and a genuinely attaining law.

No uniqueness of all noncanonical original optimizers, elementary inverse, numerical root, formal/kernel, human/vendor, novelty or broad-book conclusion is inferred. The general symmetrization, comparison and verification tools remain prior. The NEW head-removal argument must receive its own actual hostile reconstruction before any parent promotion; prior W1 or E verdicts do not accept it by implication.
