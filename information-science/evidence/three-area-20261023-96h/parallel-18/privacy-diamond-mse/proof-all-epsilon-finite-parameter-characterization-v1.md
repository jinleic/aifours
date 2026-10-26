# All finite epsilon: finite-parameter variational characterization with attainment

Observed clock before creation: **2026-10-23T18:33:44-0700**.

## 0. High-risk candidate and exact boundary

**HIGH-RISK AUTHOR CANDIDATE.** This is conditional on the complete coupled-optimizer packet D0 and its diagonal-Steiner Addendum3. No actual coupled reconstruction or parent disposition has yet been received/read by this owner. No earlier verdict is inherited. The new selector regularity argument below also has no independent check yet.

This is exploratory written reasoning, not preregistered. No scientific program, numerical optimization, sampling, CAS, proof assistant, model CLI or new agent was used.

The claim is an exact finite-parameter variational characterization of the ORIGINAL all-Borel V for every finite ε>0, together with a genuinely attaining original law. There is no remaining optimization over an unknown measure or unknown curve inside the formula. There remain an explicit compact finite-parameter minimum, a unique scalar zero, and ordinary integrals of finite-dimensional pointwise minimum values. No elementary closed form, numerical evaluation, uniqueness of all optimal laws, novelty certificate, or broad book-problem solution is claimed.

Whether this degree of exact characterization closes the owner's full target is a separate disposition; it is not inferred by this author. The current target is not silently narrowed or declared complete.

### Imports and unchanged model

```
D = {h in R²: |h1|+|h2| <=1},   b=exp(-ε),   ε>0,
V = inf_mu ∫ |x|² dmu(x),
mu(E) <= b^(-1)mu(E+h) for EVERY Borel E and EVERY h in D.
```

The original class has no assumed density, symmetry, convexity, independent coordinates, attained peak or shell ansatz.

D0 supplies some original global minimizer with geometric-valued density alpha*b^n and simultaneous compact, measure-regular closed level sets K_k, D4 symmetry, coordinate contractions, central top level K_0⊂B_(sqrt V), and

```
K_k+D ⊂ K_(k+1) ⊂ (K_k+D) union B_(sqrt V).
```

Its immutable three-body pins are listed in `proof-small-optimum-matching-value-v1.md`, SHA `45bd223bd6118ab8c651de90d35af69bacc3edc6e2f7125683926aedeceb1221`. Only its stated D0 is imported, not its separate new small-regime theorem.

`proof-coupled-level-tail-ADDENDUM-3-diagonal-Steiner.md`, SHA `6da3be079457f4558a32d422c04185e01e0f996fccfe6719152da2c53f55ad36`, additionally derives diagonal contractions of the SAME original optimal levels. Each level has a first-octant profile F on[0,t] with

```
F(t)=t,   t<=F(y)<=2t-y,
F nonincreasing and1-Lipschitz.
```

This permits nonconcave profiles and nonconvex planar levels. It gives exact full-D coupling

```
t_next >= t+1/2,
F_next(y) >= F(y)+1 on0<=y<=t,
```

and the exact parallel profile s+F(y) below t and s+2t-y above t, for EVERY real s≥0. These are the load-bearing geometry imports, not a norm substitution or sampled-shift approximation.

## 1. Explicit finite parameters and scalar moment constants

Define

```
U = 4/ε²,
L = ceil(sqrt(2U)) >=1,
B = sqrt(pi)*U*b^(-(L+1)/2).
```

Let G have P(G=k)=(1-b)b^k and put

```
m  = E G  = b/(1-b),
T2 = E G² = b(1+b)/(1-b)²,
T3 = E G³ = b(1+4b+b²)/(1-b)³,
T4 = E G⁴ = b(1+11b+11b²+b³)/(1-b)⁴.
```

The finite support-parameter domain is

```
T = { (t_0,...,t_L): 0<=t_0,
      t_(i+1)>=t_i+1/2 for0<=i<L,  t_L<=B }.
```

It is a compact polytope and is nonempty by the original-optimizer inclusion proved in Section6. Define fixed positive weights and coefficients

```
a_i = (1-b)b^i,  c_i=d_i=0,       0<=i<L,
a_L = b^L,      c_L=m, d_L=T2.
```

For t∈T, 0≤y≤t_L, let I(y)={i:y≤t_i}; it is a nonempty terminal interval of indices. For i∈I(y), define

```
ell_i(y) = max_{0<=p<=i} [t_p+i-p-max(y-t_p,0)],
u_i(y)   = 2t_i-y.
```

Define the finite pointwise polytope P_t(y) by

```
ell_i(y) <= s_i <= u_i(y),       i in I(y),
s_(i+1) >= s_i+1,               i,i+1 in I(y).
```

Its objective is the explicit strictly convex polynomial

```
Q_(t,λ,y)(s) = sum_(i in I(y)) a_i
                [s_i³/3+c_i*s_i²+(d_i+y²-λ)*s_i].
```

Write its unique minimizer as s*(t,λ,y), and its minimum value as q_b(t,λ,y). This is a problem with at most L+1 scalar variables, piecewise affine bounds and a cubic objective, not an optimization over a function.

## 2. Explicit value formula

For0≤λ≤U define

```
C_b(t,λ)
 = a_L[(2/3)T4+(16/3)t_L*T3+4t_L²*T2
             -λ(8t_L*m+2T2)]
   +8 sum_(i=0)^L a_i[-t_i⁴/3+λ*t_i²/2]
   +(8/3)a_L*m*t_L³,

J_b(t,λ) = C_b(t,λ) +8∫_0^(t_L) q_b(t,λ,y)dy,
Phi_b(λ) = min_(t in T) J_b(t,λ).
```

**Candidate theorem, at the imported boundary.** Phi_b is continuous and strictly decreasing on[0,U], Phi_b(0)>0 and Phi_b(U)≤0. It has exactly one zero λ*, and

```
V(ε) = λ* for EVERY finite ε>0.
```

Choose any t* minimizing J_b(t,λ*) on T and set

```
F_i(y) = s_i*(t*,λ*,y),   0<=y<=t_i*.
```

These are actual continuous nonincreasing1-Lipschitz profiles; that assertion is proved below and is essential. Form K_i by D4 extension of

```
0<=y<=t_i*,   y<=x<=F_i(y),
```

and extend K_(L+j)=K_L+jD. If t_0*=0 its first set is the point{0}, which creates no atom. Then

```
n(x)=min{k>=0:x in K_k},
p_*(x)=b^(n(x))/∫b^(n(z))dz
```

is an original full-D-private law attaining λ*.

## 3. Why the endpoint envelope is mandatory and the pointwise polytope is nonempty

For any genuinely feasible profile tuple and p≤i, coupling at y≤t_p gives F_i(y)≥F_p(y)+i-p≥t_p+i-p. For y≥t_p, apply the1-Lipschitz inequality from its endpoint:

```
F_i(y) >= F_i(t_p)-(y-t_p)
       >= 2t_p+i-p-y.
```

Thus EVERY feasible tuple satisfies F_i(y)≥ell_i(y); these additional lower bounds do not narrow the original profile problem.

Each ell_i is nonincreasing1-Lipschitz and ell_i(y)≥t_i≥y on its domain. The diagonal increment condition implies ell_i(y)≤u_i(y): for each p≤i, 2(t_i-t_p)≥i-p, and the two cases y≤t_p and y≥t_p give precisely this inequality. At the endpoint,

```
ell_i(t_i)=u_i(t_i)=t_i.
```

On common active domains,

```
ell_(i+1)(y) >= ell_i(y)+1,
u_(i+1)(y) >= u_i(y)+1.
```

The first follows by retaining every term p≤i in the next maximum; the second is2(t_(i+1)-t_i)≥1. Therefore both the ell-vector and u-vector satisfy the order constraints. P_t(y) is nonempty and compact. All variables are nonnegative; its cubic objective is strictly convex, so its minimizer is unique.

Componentwise minimum and maximum preserve the order constraints. Equivalently, subtract i from coordinate s_i, after which the vectors are nondecreasing. This lattice fact is used in the next section.

## 4. Main new step: the pointwise selector really is a feasible curve tuple

Dropping curve regularity naively was invalid, as the lambda0 two-level control in checkpoint011 shows. The endpoint envelopes above repair that exact defect. Here is a full comparison proof rather than an assumption of automatic smoothness.

### 4.1 Monotonicity within a fixed active-index interval

Let y1<y2 have the same active indices, and let p=s*(y1), q=s*(y2). Every lower and upper bound is nonincreasing in y. Thus p∨q is feasible for the old problem and p∧q for the new problem. Optimality in the two problems gives a nonnegative sum of their objective increments. Only indices with q_i>p_i contribute to that sum, which is exactly

```
-(y2²-y1²) sum_(q_i>p_i) a_i(q_i-p_i).
```

It is strictly negative if any such coordinate exists, a contradiction. Hence q_i≤p_i for every active index.

### 4.2 The1-Lipschitz lower comparison

Put delta=y2-y1. Shift the old problem by writing z_i=s_i-delta. Its optimizer is p-delta, its bounds are[ell_i(y1)-delta,u_i(y2)], and its order constraints are unchanged. The new lower bounds are at least the shifted old lower bounds; its upper bounds are identical.

For a fixed coordinate, let A_i(z) be the old objective after this shift and let B_i(z) be the new objective. Their derivatives satisfy

```
B_i'(z)-A_i'(z) = 2a_i*delta*(y1-z-c_i) <=0.
```

The sign is justified on the entire comparison range: since the index is active at y2,

```
z >= ell_i(y1)-delta >= t_i-delta >= y1,
```

and c_i≥0. Taking the componentwise minimum of p-delta and q is feasible for the shifted old problem, and their maximum is feasible for the new one. If some q_i<p_i-delta, summing the two optimality increments integrates B_i'-A_i' over a positive interval and is strictly negative. Even when c_i=0 and the lower endpoint is y1, the derivative is strictly negative at every larger z in that interval. Contradiction. Consequently

```
p_i-delta <= q_i <= p_i.
```

The selector is nonincreasing1-Lipschitz on every interval of fixed active indices.

### 4.3 No jump when an active level disappears

Within such an interval the feasible polytopes vary continuously in Hausdorff distance. One explicit approximation is to clip a feasible vector between the new ell and u vectors: both bounding vectors satisfy the order constraints, so componentwise clipping remains feasible, and moves each coordinate by at most the maximum bound change. Strict convexity and compactness then give continuity of the unique optimizer.

At y=t_j, coordinate j is fixed to t_j by its equal lower/upper bounds. Removing it leaves exactly the later-coordinate polytope used immediately to the right: ell_(j+1)(t_j)≥t_j+1 already encodes its last coupling constraint. All later couplings remain the same. Its objective is constant at that boundary, so the unique optimizer in the remaining coordinates agrees from the two sides. This argument also covers t_0=0.

Thus the one-sided selectors join continuously at every active-index boundary. There are only finitely many such boundaries. The interval comparisons glue to global nonincreasing1-Lipschitz profiles F_i on[0,t_i], with F_i(t_i)=t_i. The pointwise bounds and gaps are retained. The full-D geometry import therefore makes the resulting entire tuple genuinely feasible.

### 4.4 Exact profile minimization, not a relaxation

Every originally feasible profile tuple belongs to P_t(y) at each y by Section3, so its signed integral is at least the integral of the pointwise minima. Conversely the pointwise selector is a feasible curve tuple by Sections4.1-4.3, and attains those minima everywhere. Therefore J_b(t,λ) is EXACTLY the minimum of N-λZ over the full derived profile class at that fixed t. No hidden functional infimum remains.

## 5. Checking the signed objective and all geometric tails

For a first-octant level (t_i,F_i),

```
Area(K_i)=8∫_0^(t_i)(F_i-y)dy,
Moment(K_i)=8∫_0^(t_i)(F_i³/3+y²F_i-4y³/3)dy.
```

The raw geometric density has layer identity

```
b^n=(1-b)sum_(k>=0)b^k*1_(K_k).
```

Levels0 through L-1 therefore have weights a_i=(1-b)b^i. The entire remaining tail is b^L times the one-core raw density generated by K_L. Addendum3's exact parallel polynomials give its full Z_t(F), N_t(F), namely

```
Z_t(F)=8∫_0^t(F-y)dy+8tm+2T2,

N_t(F)=(2/3)T4+(16/3)tT3+4t²T2
       +8∫_0^t[T2F+m(F²+y²)+F³/3+y²F-4y³/3]dy.
```

These hold at arbitrary t here. Subtract λZ and collect the terms containing F_i. They are exactly Q_(t,λ,y). The remaining integrals use

```
∫_0^t[-4y³/3+λy]dy=-t⁴/3+λt²/2,
∫_0^t m*y²dy=m*t³/3,
```

and give exactly C_b(t,λ). Thus no shell, mass factor, or first-octant factor8 has been suppressed.

## 6. Why a true original optimum is in this bounded finite-parameter class

The product Laplace law gives V≤U. For the D0 minimizer q≤alpha, tail integration of P(|X|²≤s)≤pi*alpha*s gives V≥1/(2pi*alpha). At x∈K_k, pointwise full-D privacy gives

```
V >= alpha*b^(k+1)∫_D|x+h|²dh
  = alpha*b^(k+1)(2|x|²+2/3).
```

Consequently

```
|x|² <= pi*U²*b^(-(k+1)).
```

For k≤L this is at most B², so every diagonal intercept of the original optimal head is at most B. Its parameter vector belongs to T by exact coupling.

Because the original optimal levels are nonempty coordinate ideals, K_0 contains0 and K_L⊃LD. Our choice of L gives LD⊃B_(sqrt U)⊃B_(sqrt V). The D0 sandwich therefore forces

```
K_(L+j)=K_L+jD for every j>=0.
```

The selected original optimum has exactly the class represented above.

Conversely EVERY parameter vector in T and every feasible profile tuple generates original full-D-private levels. Their finite head lies in a box of halfwidth2B and their tails grow only polynomially in size, so normalization and second moment are finite. Their union covers the plane because K_k⊃kD. Thus the class is not a density relaxation: all of its members are original feasible laws, and it includes an original global optimum.

## 7. Continuity, unique scalar zero, and attainment

### 7.1 Continuity and finite outer minimization

The functions ell and u are continuous in(t,y). For almost every fixed y under a convergent parameter sequence, the active indices stabilize. On that finite-dimensional polytope, the clipping argument of Section4.3 gives continuous feasible correspondence, and strict convexity gives a continuous minimum value. All profiles are bounded by2B and all y by B; hence the integrands are uniformly bounded on the compact parameter/λ domain. Active-index boundaries form a finite measure-zero set. Dominated convergence therefore proves joint continuity of J_b(t,λ).

The compact T thus attains each outer minimum, and Phi_b is continuous in λ. This does not claim the optimizing support parameters are unique.

### 7.2 A strictly positive mass lower bound

Every generated sequence has K_L⊃LD. With its RAW normalizer Z,

```
Z >= (1-b)b^L Area(LD) = 2(1-b)b^L L² =: Z_min >0.
```

Its RAW moment also satisfies

```
N >= (1-b)b^L Moment(LD) = (2/3)(1-b)b^L L⁴ >0.
```

The latter proves Phi_b(0)>0 directly.

### 7.3 Strict monotonicity and the upper endpoint

For λ2>λ1, take a minimizing parameter vector and feasible selector at λ1. The same original law is a permissible competitor at λ2, since the entire class is independent of λ. Exact profile minimization gives

```
Phi_b(λ2) <= Phi_b(λ1)-Z_min*(λ2-λ1).
```

Thus Phi_b is strictly decreasing. At λ=U, the true original optimum from Section6 is a competitor and has signed numerator(V-U)Z≤0. Therefore Phi_b(U)≤0. Continuity gives one and only one zero λ*∈(0,U].

### 7.4 Actual law and matching ALL-law lower conclusion

An outer minimizer at λ* exists, and its pointwise selector is a feasible curve tuple by Section4. Its normalized law p_* has signed numerator zero, hence cost λ*. Full privacy holds pointwise: from K_k+D⊂K_(k+1), both n(x+h)≤n(x)+1 and n(x)≤n(x+h)+1 hold for every h∈D. Integration gives every Borel-event inequality. There is no exceptional-direction or boundary omission.

Thus V≤λ*. Conversely, applying exact profile minimization to the true original optimum at λ=V gives Phi_b(V)≤0. The unique zero and strict monotonicity imply V≥λ*. Hence V=λ* and p_* attains it.

This bounds EVERY original feasible law below by λ*, including nonsymmetric or infinite-cost laws. Only an optimal representative was derived to have the special geometry; arbitrary competing laws were not assumed to do so.

## 8. What is and is not determined

The formula uses a compact(L+1)-parameter minimum, ordinary one-dimensional integrals of unique finite-dimensional convex minima, and one unique scalar zero. There is no unknown curve whose regularity is deferred to a future optimizer: it is produced by the explicit pointwise selector and proved feasible above. No numerical integration or optimizer has been executed.

The finite parameter minimum has NOT been evaluated into elementary expressions or particular numerical noise laws. If an elementary closed form or an executed numerical instance is required, that is a further named requirement, not claimed satisfied here. No scientific execution permission exists for this lane.

The general geometric-valued/shell mechanisms and standard symmetrization/convexity tools are PRIOR. The SCDF2013 construction is not used as a global class-completeness theorem; the2018 generic location framework overlaps our model exactly but does not supply this optimization through its circularization hypotheses. All previously retained source and provenance boundaries remain, and NOVELTY_UNCLEAR is mandatory.

The highest-risk new reconstruction obligations are: mandatory endpoint envelopes; min/max feasibility with offset order constraints; derivative comparison after the y-shift; continuity through disappearing active levels; every tail coefficient/weight; bounded original-optimizer inclusion; and the exact all-law lower/attaining-law logic. Actual D0/Addendum3 reconstruction and an independent read of this full body are still required. This manuscript does not promote itself or close the slot by declaration.
