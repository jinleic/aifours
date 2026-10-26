# A matching finite-value formula in the small-optimum regime

## 0. Status, scope, and dependency boundary

Observed clock before creation: **2026-10-23T17:09:51-0700**. This is exploratory written research; the structural route and some algebra preceded this manuscript and its proposal. It is not preregistered. No scientific program, numerical minimization, sampling, proof assistant, or model CLI was used.

**CANDIDATE, conditional at this freeze on the coupled-optimizer packet below.** No earlier disk, envelope, peer, or parent verdict is inherited. The claim is an exact *implicit* finite-dimensional value and an attained admissible law for every ε≥4√2. It is not an elementary closed-form value, not a formula for all ε>0, not a new mechanism class, and not a solution of the broad book privacy-utility question. NOVELTY_UNCLEAR remains mandatory.

The full original optimization is unchanged:

```
D = {h in R² : |h1|+|h2| <= 1},   b = exp(-ε),   ε>0,
V = inf_mu ∫ |x|² dmu(x),
mu(E) <= b^(-1) mu(E+h) for every Borel E and every h in D.
```

The infimum is over all Borel probability laws, without an assumed density, symmetry, convexity, independence, attained peak, or one-core representation.

### D0: exact imported assertion

The complete author candidate packet supplies the following simultaneous assertion. An original global minimizer can be chosen with density

```
q(x) = alpha * b^(n(x)),   alpha>0,
n(x) = min{k>=0 : x in K_k},
```

where the minimum is finite everywhere, the K_k are nonempty compact closed level sets, K_0 has positive area, and:

1. Each K_k is invariant under sign changes and coordinate interchange and is an absolute-coordinate order ideal.
2. With R=√V, K_0⊂B_R.
3. For every integer k≥0,

```
K_k+D ⊂ K_(k+1) ⊂ (K_k+D) union B_R.
```

The closed-level density represents an original global minimizer, rather than a density relaxation. Pointwise full-D privacy and the all-law existence step are part of this dependency.

Recorded immutable source pins:

- `proof-coupled-level-tail-saturation-v1.md`: `ae1e05470b233d2e51a3c56f45a58ab97ecd249a5ed479dc33c6d29ae4ea3958`.
- `proof-coupled-level-tail-ADDENDUM-1-closed-levels.md`: `87320046a2396eb936138af7c3eb3122a5e3451140a70171dce73cb270fd5596`.
- `proof-coupled-level-tail-ADDENDUM-2-coordinate-Steiner.md`: `15a4d1eda329a5f8eb22207c8fce9750f906d5f3cba8d290a65bde5426c29007`.

At this freeze their actual coupled reconstruction has not been received/read by this owner. The present deduction does not promote D0. All conclusions below carry that dependency until its disposition is actually read.

## 1. Exact formula to be proved

Fix ε≥4√2 and put U=4/ε²≤1/8. Let G have probabilities P(G=k)=(1-b)b^k, k≥0. Define

```
m   = E G   = b/(1-b),
T2  = E G²  = b(1+b)/(1-b)²,
T3  = E G³  = b(1+4b+b²)/(1-b)³,
T4  = E G⁴  = b(1+11b+11b²+b³)/(1-b)⁴,
v   = T2-m² = b/(1-b)².
```

For 0≤λ≤U and 0≤t≤√(λ/2), define on 0≤y≤t

```
psi_(t,λ)(y) = min(2t-y, max(t, sqrt(max(λ-v-y²,0))-m)).
```

For an admissible profile F on [0,t], set

```
Z_t(F) = 8 ∫_0^t (F(y)-y) dy + 8tm + 2T2,

N_t(F) = (2/3)T4 + (16/3)tT3 + 4t²T2
       + 8 ∫_0^t [ T2 F(y) + m(F(y)²+y²)
                    + F(y)³/3 + y²F(y) - 4y³/3 ] dy.

H_b(t,λ) = N_t(psi_(t,λ)) - λ Z_t(psi_(t,λ)),
Phi_b(λ) = min_{0<=t<=sqrt(λ/2)} H_b(t,λ).
```

At t=0 these formulas mean Z_0=2T2 and N_0=(2/3)T4; the associated core is the single point {0}.

**Candidate theorem, conditional on D0.** Phi_b is continuous and strictly decreasing on [0,U], with Phi_b(0)>0 and Phi_b(U)≤0. It has one zero λ*. Then

```
V(ε) = λ*.
```

For any minimizer t* of H_b(t,λ*) on its displayed compact interval, t*>0. Extend the first-octant region

```
0 <= y <= t*,   y <= x <= psi_(t*,λ*)(y)
```

by sign changes and coordinate interchange to a compact core S*. Define

```
n_*(x) = min{k>=0 : x in S*+kD},
p_*(x) = b^(n_*(x)) / Z_(t*)(psi_(t*,λ*)).
```

This is a genuinely admissible original law attaining λ*. The formula uses one compact scalar minimization and one unique scalar zero, with explicit one-dimensional integrals; no unknown function or unrestricted-law optimization remains inside it.

## 2. Why an original optimal law has one core here

The product Laplace density (ε²/4)exp(-ε|x|_1) satisfies full-D privacy and has squared-Euclidean cost U=4/ε². Therefore V≤U≤1/8. An attained cost zero would force a point mass at the origin, which violates privacy at any nonzero shift in D; thus V>0.

Take the global minimizer from D0 and any c∈K_0. For x∈B_R,

```
|x-c|_1 <= sqrt(2)(|x|+|c|) <= 2sqrt(2)R <= 1.
```

Hence B_R⊂K_0+D. The two D0 inclusions give K_1=K_0+D. Because every later K_k contains B_R, the same inclusions inductively give

```
K_k = S+kD for every k>=0,   S=K_0⊂B_R.
```

This is a consequence for an original minimizer, not an inserted one-core ansatz. S is compact, D4-invariant, coordinate-downward, and of positive area.

## 3. Filling an irregular core without changing any integer tail

We next eliminate irregular prefix geometry within the *derived* one-core class. Convexity is not assumed.

Let r be the maximum coordinate of S in the positive quadrant. By symmetry both axis intercepts are r, and r≤R. Define its closed upper profile

```
F(y) = max{x>=0 : (x,y) in S},   0<=y<=r.
```

It exists, is nonincreasing and upper semicontinuous, and F(0)=r. Put

```
h = max_{0<=y<=r} (F(y)+y),
t = h/2,
M(y) = max_{0<=s<=y} (F(s)+s).
```

Then r≤h≤√2R≤1/2, so 0<t≤1/4 and t≤r. A maximizer (u,s) with u+s=h has, after interchange if necessary, s≤t≤u. Thus M(t)=h, and M(y)=h for y≥t.

For y2≥y1, monotonicity of F gives M(y2)≤M(y1)+(y2-y1): a maximizing s≤y1 contributes at most M(y1), and a maximizing s≥y1 contributes at most F(y1)+y1+(y2-y1). M is also nondecreasing. Consequently

```
Fhat(y) = M(y)-y,   0<=y<=t,
```

is continuous, nonincreasing and 1-Lipschitz, with

```
Fhat(t)=t,   t<=Fhat(y)<=2t-y,   Fhat(0)=r.
```

Let Shat be its D4 first-octant extension. It is compact and coordinate-downward. It contains S: every first-octant point of S has y≤t, and F(y)≤M(y)-y.

Moreover Shat⊂conv(S). Indeed, at a boundary point (M(y)-y,y), choose s≤y attaining M(y)=F(s)+s. Since M(y)-y≥y, one has s≤y≤F(s). The boundary point lies on the segment joining (F(s),s) and its interchange (s,F(s)), both in S. Interior coordinate contractions stay in conv(S), since that convex hull is unconditional; reflections and interchange do also. Therefore

```
S ⊂ Shat ⊂ conv(S) ⊂ B_R.
```

### Exact integer dilations, including boundaries

For every integer k≥1, the first-octant boundary of S+kD is exactly

```
x_max(y) = k+Fhat(y),       0<=y<=t,
x_max(y) = k+2t-y,         t<=y<=t+k/2.
```

To check this without a generic-position assumption, the full nonnegative-quadrant upper profile is the maximum of

```
F(z)+k-|y-z|,   0<=z<=r,   |y-z|<=k.
```

For the first octant, y≤(h+k)/2=t+k/2≤k, and r≤R<1≤k; hence every z∈[0,r] is eligible. Terms z≥y cannot beat k+F(y) when that case exists. Terms z≤y give k-y+M(min(y,r)). This is k+Fhat(y) below t and k+h-y above t. The endpoint x_max=y occurs at t+k/2; larger y is excluded by the l1-support bound h+k. Compactness makes these maxima and all boundary inclusions exact. Sign changes and interchange cover all sectors.

Applying the same argument to Shat gives the identical profile, since Fhat(y)+y=M(y) below t and the maximum thereafter is h. Hence

```
Shat+kD = S+kD for every integer k>=1.
```

The raw densities b^(n_S) and b^(n_Shat) therefore differ only on Shat\S, where their values are b and 1. Their difference is nonnegative, supported in B_R, and equals 1-b on that set. If it had positive integral, normalization would strictly lower the cost V: its added mass has cost strictly less than V almost everywhere, because the circle |x|²=V has area zero. This contradicts global optimality. Thus S and Shat agree almost everywhere, and the law with core Shat is also globally optimal.

We have proved that an original optimum may be taken from the complete derived profile class

```
F:[0,t]->R continuous, nonincreasing, 1-Lipschitz,
F(t)=t,   t<=F(y)<=2t-y,
0<t<=sqrt(V/2).
```

The last bound follows from (t,t)∈Shat⊂B_R. This class is not assumed convex as a family of planar bodies, and its members need not be convex bodies.

## 4. Exact mass and moment of the entire derived class

Take any such profile with 0<t≤1/2. Its axis intercept is at most 2t≤1. Its integer dilations have the two-part first-octant profile in Section3; the same maximum argument applies because t+k/2≤k and all original vertical coordinates are at most1≤k.

Direct first-octant integration gives, for every integer k≥0,

```
Area(S+kD) = 8 ∫_0^t (F(y)-y)dy + 8tk + 2k².
```

For the moment, the part below y=t is

```
∫_0^t [(k+F(y))³/3 + y²(k+F(y)) - 4y³/3]dy.
```

The remaining first-octant triangular part is exactly

```
∫_t^(t+k/2) [(k+2t-y)³/3 + y²(k+2t-y) - 4y³/3]dy
= k⁴/12 + tk³/3 + t²k²/2.
```

For example, with w=k+2t its integrand is w³/3-w²y+2wy²-8y³/3, whose primitive is w³y/3-w²y²/2+2wy³/3-2y⁴/3. Evaluation at t and w/2 gives the displayed expression. Multiplying by8 and expanding the first part yields

```
Moment(S+kD) = (2/3)k⁴ + (16/3)tk³ + 4t²k²
            + 8 ∫_0^t [k²F + k(F²+y²) + F³/3+y²F-4y³/3]dy.
```

These identities also hold for k=0, with the triangular part empty.

For a nonempty compact core,

```
b^(n_S(x)) = (1-b) sum_{k>=0} b^k 1_(S+kD)(x).
```

Tonelli and the polynomial identities therefore give exactly the Z_t and N_t of Section1. All geometric tails are included. The formulas for T2,T3,T4 follow by successive application of b(d/db) to 1/(1-b), then multiplication by1-b.

At t=0 the core {0} gives the point-core values in Section1. It is still an absolutely continuous noise law after normalization; no point mass is added.

## 5. Eliminating every profile, not selecting a new family by ansatz

Fix t and λ. In N_t(F)-λZ_t(F), the part depending on F at y is

```
F³/3 + mF² + (T2+y²-λ)F.
```

Its derivative is

```
(F+m)² + v+y²-λ,
```

and its second derivative is 2(F+m)>0 for F≥0. Its unique minimizer on the pointwise interval [t,2t-y] is precisely psi_(t,λ)(y).

This pointwise minimizer belongs to the full profile class. It is continuous and nonincreasing. Where the lower-clipped root exceeds t, its square-root denominator is greater than t+m≥y, so the absolute value of its derivative y/sqrt(λ-v-y²) is at most1. Elsewhere the lower-clipped function is constant. It is therefore 1-Lipschitz. Taking its minimum with the 1-Lipschitz function 2t-y preserves that property. At y=t the two bounds coincide, giving the required endpoint.

Thus pointwise minimization has not left a missing functional feasibility condition: for every admissible F,

```
N_t(F)-λZ_t(F) >= H_b(t,λ),
```

with equality at psi_(t,λ). No convexity, differentiability, or Euler-Lagrange stationarity ansatz is being imposed on the competitor F.

For t≤√(λ/2), the resulting core also lies in B_(sqrt λ). On a boundary portion with psi=t this follows from 2t²≤λ. If psi>t, let w=sqrt(λ-v-y²)-m; then psi≤w and

```
w²+y² = λ-T2-2mw < λ.
```

Inner coordinate contractions reduce Euclidean cost. This is a consistency property of the derived minimizer, not an assumption used to exclude other profiles.

## 6. Scalar zero: continuity, strictness, and endpoint control

The function H_b is continuous on the compact domain

```
0<=λ<=U,   0<=t<=sqrt(λ/2).
```

For t>0 this follows by rescaling y=tu in the explicit integrals: the clipped profile is continuous in (t,λ,u). At t=0 the integration interval and all t-polynomial corrections vanish, so the displayed point-core values are the same limit. Rescaling t=s sqrt(λ/2), 0≤s≤1, also makes the minimizing interval fixed; elementary compact minimum continuity gives continuity of Phi_b.

Let λ2>λ1 and choose a minimizer t1 for Phi_b(λ1). Its clipped profile is a permissible competitor at the same t1 for λ2, whose t-domain is larger. Because every core has Z_t(F)≥2T2>0,

```
Phi_b(λ2)
<= H_b(t1,λ2)
<= H_b(t1,λ1) - (λ2-λ1)Z_(t1)(psi_(t1,λ1))
<= Phi_b(λ1) - 2T2(λ2-λ1).
```

Therefore Phi_b is strictly decreasing. At zero its domain is just t=0, so Phi_b(0)=(2/3)T4>0.

At λ=U, use the original global minimizer placed in the derived class by Sections2-3. Its parameter t0 satisfies t0≤√(V/2)≤√(U/2). Therefore

```
Phi_b(U) <= H_b(t0,U)
         <= N_(t0)(F0)-U Z_(t0)(F0)
          = (V-U) Z_(t0)(F0) <= 0.
```

There is exactly one zero λ*∈(0,U]. Every minimum defining Phi_b is attained by compactness.

At t=0,

```
N_0/Z_0 = T4/(3T2) >= 1/3 > U,
```

because k⁴≥k² at every nonnegative integer. Hence H_b(0,λ*)>0. A minimizing t* at the zero cannot be0.

## 7. Matching the unrestricted lower value with an actual admissible law

The level index of every nonempty core satisfies, for every x and every h∈D,

```
n_S(x+h) <= n_S(x)+1,
n_S(x)   <= n_S(x+h)+1.
```

Indeed, S+kD+h⊂S+(k+1)D, and -h∈D. This holds at all corners and boundaries, not just almost everywhere. Its normalized density therefore satisfies the original privacy inequality for every Borel event by integration. The Z and N above are its exact finite normalization and cost numerator.

For t* and psi_(t*,λ*), H_b(t*,λ*)=Phi_b(λ*)=0, so the admissible law p_* has cost λ*. Thus V≤λ*.

Conversely, applying the profile minimization to the true optimal profile at λ=V gives Phi_b(V)≤0. Strict monotonicity and the unique zero imply V≥λ*. Therefore V=λ*, and p_* attains it.

This is an all-law lower conclusion: arbitrary feasible laws are bounded below by the original global minimum, whose value has just been matched. They were not individually assumed to have the symmetry, density, or one-core form of the derived optimal representative. Infinite-cost feasible laws satisfy the lower inequality trivially.

## 8. Claim delta, sources, and the exact remaining full target

Relative to D0's finite arbitrary head and eventual forced tails, the new candidate deduction is:

1. In the small-optimum regime, all head levels collapse to one core for an original optimum.
2. All irregular one-core profiles can be filled to the full stated nonincreasing 1-Lipschitz class without changing any integer tail.
3. That entire derived functional class is eliminated by the clipped profile, leaving an exact scalar minimum/unique-zero formula and an attaining original law.

These are dependencies of one matching-value result, not separately counted independent discoveries. This is not another ε-threshold comparison or a parameter sample.

The mechanism class is PRIOR: Soria-Comas and Domingo-Ferrer's2013 Theorem13 already supplies suitable downward-core Minkowski-shell mechanisms. Its Section6 explicitly says determining *all* optimal multivariate noises is out of scope (authenticated `source-soria-comas-2013-UOC.txt`, LF780-784); its Definition5 is concentration-order minimality, not a proof of this squared-loss optimum or class-completeness import. The known mechanism is not claimed invented here.

The2018 ElSalamouny-Gambs generic arbitrary-domain framework includes our model exactly with X=D/2 and ell constant off zero. Its circularization hypotheses do not apply to this embedding. The operative source clarification is `source-location-interface-ADDENDUM-1-exact-embedding.json`, SHA `87e7bd40bce5633631dfd06ba8987501ce47202da3b38fa87f6d913578257266`. Existence/regulation/symmetrization tools are prior ingredients; no source proof or worldwide novelty is certified.

For **0<ε<4√2**, this manuscript gives no exact V and does not assert that one-core representation fails or succeeds. The first unresolved step is to replace the small-cost head collapse by a complete treatment of the genuinely coupled finite head, or produce another matched all-law lower/upper certificate. The coarse regime boundary is not claimed sharp. The full finite-ε primary remains open outside the stated range even if this candidate and D0 pass written reconstruction.

Requested reconstruction is written-only: D0's simultaneous representative properties; the arbitrary nonconvex core fill and every boundary in the integer-dilation identity; all moment coefficients/factors8; clipped-profile global admissibility; moving-domain scalar continuity/strictness; point-core exclusion; and the unrestricted-to-derived-class logic. Any scientific execution would require a separate authorization. No verification beyond the author derivation is claimed here.
