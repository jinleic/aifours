# Independent review: all-law TV stability

**Reviewer:** PrivacyTVStabilityReview, same harness. **Actual `/bin/date` observation before this write:** 2026-10-28T18:11:19-0700 PDT.

## Verdict and exact scope

**Pinned candidate as written: 0 FATAL / 1 MAJOR / 1 MINOR.** The major is a missing, load-bearing import-to-conclusion step, not a counterexample: the claimed diamond radius bound is not literally stated or linked to the radius by either authorized parent input. Section 2 supplies an independent written repair from the literal all-law optimizer and diamond-shape imports. Conditional on those imports and that additional repair, my reconstruction supports the candidate's fixed-epsilon A, B, and C, including the lower-modulus constant. This review does not silently amend the frozen candidate or constitute parent adoption. No counterexample to the repaired universal theorem was found; the explicitly constructed nonoptimal counterexample is valid. The minor is the ambiguous word “interior.”

### MAJOR M1 — radius bound is not a literal authorized import

Candidate LF38 and LF48 attribute `S=gamma D, 0<gamma<1` to v241. The pinned v241 parent LF5–9 states that the core is a full diamond; LF31 gives an unnamed diamond-family parameter `q_*` in `(0,1)` but does not define it as the core's radius. LAW642 parent LF18–22 specifies `S` and `t_*>0` but does not literally supply `2t_*<1`. Thus neither pinned parent as provided makes the quoted radius bound an explicit imported statement. It cannot be justified by silently consulting the original proofs, the held threshold manuscript, or an older verdict. The gap is material because `D not subset S` is used to obtain every core plateau's strict saturation neighbor. The direct repair below establishes the needed bound using only all-law optimality and the fact that the actual core is some positive-radius diamond.

### MINOR m1 — “interior” is not defined

Candidate LF27 says “a general feasible interior law,” whereas LF155 correctly calls the example a slack law. The example has a global privacy ratio bound 2 under budget 6, but is not an interior point of the feasible laws in the usual TV or weak topology on all probability measures: adding an arbitrarily small atom converges in either topology and is infeasible by the absolute-continuity argument below. Say **strictly privacy-slack law**, or specify a suitable relative topology. This does not affect the counterexample or A–C.

## 1. Complete inputs and unverified imports

I read the manifest first, then each entire pinned body in its stated order, through the final line. Live SHA-256 values were:

1. LAW642 parent, `privacy-all-law-self-contained-parent-v1.md`, 40 LF, `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`.
2. v241 separated parent, `privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md`, 63 LF, `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`.
3. Candidate, `frontier-20261028-all-law-tv-stability-v1.md`, 173 LF, `3f6c2a61738cc92f615e375d88f6dfb10f96b553585b5c8468480a7ec9683f79`.

Manifest SHA-256 `5f88c9a7a79eeda839e49ca98c20227675984d179a404fb5fdecd9740f1d283a`. These hashes bind bytes, not mathematical validity. The following are **unverified research imports**, not proofs independently re-established here:

- LAW642: for each finite positive epsilon, existence and uniqueness as a law of the all-Borel-law optimum, its stated density `Z^-1 b^n`, core formula, `V>T2`, and `V<4m^2+4m+1/3`. I use no broader LAW642 dependency-closure assertion as a theorem.
- The literal v241 statement that the positive cubic has a unique positive root and gives the exact diamond-versus-rounded transition including equality. I use neither its norm-class gap nor NORM148, MDA, or any held threshold result. A full diamond with nonempty interior and the explicit symmetric core is `gamma D` for some `gamma>0`; the strict upper bound is proved in section 2, not imported.

Also unformalized standard imports used are Tonelli and geometric-series differentiation; Radon–Nikodym, differentiation of measures, and finite Radon-measure order; elementary convex-body facts (including interiors of Minkowski sums and null boundaries); tightness, Prokhorov, Portmanteau, lower semicontinuity of a nonnegative l.s.c. cost; the weak-plus-second-moment criterion for W2; the Riemann–Lebesgue lemma and periodic averaging. No external model, original author source, held payload, software solver, or numerical selected-parameter probe was used. This is a written same-harness review, not formal, human, independent-model, novelty, or publication assurance.

## 2. Independent repair: the actual core does not contain D

Set `b=exp(-epsilon)`, `m=b/(1-b)`, `D={r=|x|_1<=1}`, `T2=m+2m^2`. The LAW642 formula makes `S` a compact centrally symmetric convex body with `0` in its interior, since `t_*>0` and `V>T2`.

**Diamond side, including equality.** By v241 the actual core is `gamma D` for some `gamma>0`. For every `a>=0`, define `q_a(x)=b^{min{j>=0: x in (a+j)D}}` and normalize it to a law. It is feasible: if `h in D` and `x in (a+j)D`, then `x+h in (a+j+1)D`; applying this also to `-h` gives the two pointwise inequalities. It has finite second moment. On writing `r=|x|_1`, its cost is

```
J(a) = (1/3) [sum_{j>=0} b^j (a+j)^4] /
                 [sum_{j>=0} b^j (a+j)^2].
```

To see the factors, `q_a=(1-b) sum_j b^j 1_{r<=a+j}` a.e., a diamond of radius R has area `2R^2` and squared-Euclidean integral `2R^4/3`. Let `N` be geometric with `P(N=j)=(1-b)b^j`. Its first four moments are

```
M1=m, M2=m+2m^2,
M3=m+6m^2+6m^3, M4=m+14m^2+36m^3+24m^4.
```

Differentiating the convergent sums, `2 M3 M2-M4 M1=m^2(1+2m)`, hence

```
J'(0) = 2/[3(1+2m)] > 0.
```

For powers 1 through 4, shifting `j` shows the sums at `a=1` are `1/b` times those at `a=0`; thus `J'(1)=J'(0)>0` and `J(1-eta)<J(1)` for sufficiently small `eta>0`. A core of radius 1 cannot be optimal.

For `a>1`, put `v=a-1>0`. Exactly a.e.,

```
q_v = b q_a + (1-b) 1_{vD}.
```

The normalized `q_v` law is a nontrivial mixture of the normalized `q_a` law and the uniform law on `vD`. Its latter component has cost `v^2/3`, strictly less than the `q_a` law's cost: the latter has positive mass outside `vD`, and, conditional on l1-radius r, its angular mean squared-Euclidean radius is `2r^2/3`. Consequently `J(v)<J(a)`. Thus no `a>=1` can be the all-law optimum; global optimality forces `0<gamma<1`. This resolves M1 mathematically without adding a research premise, but the repair is additive to the candidate.

**Rounded side.** For the v241 cubic `f(s)=2s^3-9s^2-108s-81`, `f(1)=-196`, `f(s)->+infinity`, and its positive root is unique; hence the root exceeds 1. Above threshold, `s>1`, and `m(1+m)=1/(4s)<1/4` implies `m<1/4`. At `e1=(1,0)`, the core's second inequality would require `1+3m+2m^2<=V`. But its difference from the imported strict upper bound for V is

```
(1+3m+2m^2) - (4m^2+4m+1/3)
 = 2/3-m-2m^2 > 7/24 > 0.
```

Thus `e1` is not in the rounded core. On both regimes, and at the transition through the diamond side, `D` is not a subset of `S`.

## 3. Every law: an all-shifts pointwise representative

Fix any feasible probability `nu`. For every Borel A of finite Lebesgue area, integrating the event inequality over the closed diamond of area 2 and using Tonelli gives

```
2 nu(A) <= b^-1 int_D nu(A+h) dh <= b^-1 |A|.
```

The last inequality follows by integrating `1_A(z-h)` in h, bounded by `|A|`, and then integrating z against nu. Hence `nu` has a density and `nu(A)<=C|A|` for `C=(2b)^-1`; in particular every ball has this bound. Define for every x

```
p(x) = limsup_{j->infinity} nu(B_2(x,1/j)) / |B_2(0,1/j)|.
```

It is Borel, lies in `[0,C]` at every x, and by differentiation is a density of the same law a.e. For any x,y with `|x-y|_1<=1`, each pair of translated balls satisfies `nu(B(y,1/j))>=b nu(B(x,1/j))`; taking limsups yields `p(y)>=b p(x)` for **all** such x,y simultaneously. This is not an intersection of uncountably many a.e. assertions.

## 4. Adjacent saturation for every point; local oscillation

Write `T_k=S+kD`, `U_0=int S`, and `U_k=int T_k \ T_{k-1}` for k>=1. They are open bounded plateaux with optimizer value `b^k/Z`. The nested compact bodies cover the plane and `T_{k-1} subset int T_k`; their boundaries are planar-null.

For `x in U_0`, if `x+D subset S`, central symmetry also gives `-x+D subset S`; convexity and averaging `x+d` with `-x+d` for each `d in D` would give `D subset S`, a contradiction. Closedness then gives `h in int D` with `x+h` outside S; because `x in int S`, the point is in `U_1`.

For `x in U_k`, k>=1, the convex interior-of-sum identity gives `x=z+h` with `z in int S` and `h in int(kD)`. Set `y=z+(k-1)h/k`; for k=1 this is in `U_0`, while for k>=2 it is in `int T_{k-1}`. If it were in `T_{k-2}`, then adding `h/k in int D` would put x inside `T_{k-1}`, contrary to x outside the closed inner body. Thus `y in U_{k-1}` and `|x-y|_1<1`.

This also supplies a strict adjacent-level neighbor for the canonical pointwise density at the otherwise omitted boundary points: if `x in boundary T_j`, then `x notin T_{j-1}` for j>=1, so `n_S(x)=j`, while `x in int T_{j+1}`. Points y outside `T_j` but in `int T_{j+1}` approach x arbitrarily closely; choose one with distance <1, so `y in U_{j+1}` and `p_*(y)=b p_*(x)`. An open same-level ball around a boundary x is neither claimed nor needed, since the boundaries are null.

For each **open-plateau** x choose balls `U` around x and `B` around its adjacent y small enough that every pair in U x B has l1-distance <1. If k>=1 define `E_n(x,y)=p_n(x)-b p_n(y)>=0`. Weak convergence to `mu_*` and null ball boundaries give

```
int_{U x B} E_n = |B| mu_n(U) - b|U| mu_n(B) -> 0.
int_U |p_n - mean_U(p_n)| <= (2/|B|) int_{U x B} E_n -> 0.
```

The second line follows by integrating the triangle inequality through a common y and averaging over x'. For k=0 use `E_n=p_n(y)-b p_n(x)>=0`; the same estimate acquires `1/b`. In both cases the local mean tends to the optimizer's constant, so the local L1 error tends to zero.

## 5. Compact/area/tail exhaustion; closure, uniqueness and W2

For a fixed k, choose a compact subset of `U_k` with arbitrarily small leftover area and finitely cover it with the balls above. The uncovered error is at most `2C` times that area. Therefore each fixed plateau has vanishing L1 error. For fixed N the finitely many plateaux through N cover `T_N` except null boundaries. Since `mu_*(boundary T_N)=0`, weak convergence gives `mu_n(T_N^c)->mu_*(T_N^c)`, and the L1 tail limsup is at most `2 mu_*(T_N^c)`, tending to zero as N grows. Thus weak convergence to the **actual** optimizer entails TV convergence; no moment convergence is needed for this part.

For near-optimal laws, bounded second moments give tightness. Any weak subsequential limit obeys, for each fixed h and all nonnegative compactly supported continuous f,

```
int f(x) dmu(x) <= b^-1 int f(x-h) dmu(x).
```

The sign corresponds to `mu(A)<=b^-1 mu(A+h)`. Both test functions are continuous and compactly supported, so passing to the limit uses the same weak subsequence for **every** h, not a subsequence depending on h. Finite Radon-measure order then gives every Borel event inequality for that h; because h was arbitrary, the limit is fully private. Lower semicontinuity gives cost at most V, hence the LAW642 unique law is the limit. Tightness and uniqueness imply whole-sequence weak convergence; the preceding argument gives TV. Since costs converge to the optimizer's second moment, the standard criterion gives W2 convergence as well. A sequence contradicting `omega_epsilon(delta)->0` would have `delta->0` and violate this near-optimal conclusion.

## 6. Convolution lower modulus: independently checked geometry and constants

Let U have independent coordinates with density `(1-|u|)_+` on `[-1,1]`. Each has mean 0 and second moment `1/6`, so independent addition to `X_*` preserves every full-D event inequality and gives `J(mu_t)=V+t^2/3`. Set `c=max_{z in S}(z1+z2)` and take `B>max_{z in S,i}|z_i|`, B positive. Choose an integer k>=1 with `c+k>2B+8`. For `0<t<1/4`, use the strip

```
B+2 < x1 < B+3,   0 < x1+x2-c-k < t.
```

It has area t. Both coordinates of x and of `x-tU` exceed B. In that quadrant the exact distance from x to S in l1 is `x1+x2-c`, achieved at a maximizer of `z1+z2`; therefore `n_S(x)=ceil(x1+x2-c)` here. On the strip it is k+1. Writing `r=x1+x2-c-k`, the perturbed level is `k+r-t(U1+U2)`, which lies strictly between k-1 and k+1, and is below k whenever `U1+U2>1`. Thus the smoothed density never falls below the original on the strip and rises by at least `Z^-1 b^k(1-b)` on that event.

The claimed probability is exactly

```
P(U1+U2>1) = int_0^1 int_{1-u}^1 (1-u)(1-v) dv du = 1/24.
```

Consequently the stated, conservative bound `TV(mu_t,mu_*)>=b^k(1-b)t/(48Z)` is valid using `TV=(1/2)||p_t-p_*||_1`. With `t=sqrt(3 delta)` and `0<delta<1/48`, this yields the candidate's positive `c_epsilon=sqrt(3)b^k(1-b)/(48Z)`. This is a **lower** obstruction to an exponent >1/2 at each fixed epsilon. It proves neither a square-root upper bound nor any epsilon-uniform modulus.

## 7. Oscillatory negative control

For `a=log 2`, `epsilon=log 6`, `p0=(a^2/4)e^{-a|x|_1}`, and `p_n=p0(1+sin(2pi n x1)/2)`, the perturbation is positive and integrates to one by oddness. For any `h in D`, the Laplace ratio is at most 2 and the multiplier ratio at most 3, so all p_n obey the full event inequality with factor 6; p0 itself has ratio at most 2 and hence strict privacy slack. Riemann–Lebesgue gives weak convergence to p0, while periodic averaging gives

```
TV(p_n dx,p0 dx) -> (1/2)(1/2)(2/pi) = 1/(2pi).
```

The limit is genuinely nonoptimal under LAW642: on the nonempty open core the optimizer density is constant, while p0 is not constant on any nonempty open set; both are continuous there and so cannot agree a.e. This is a counterexample only to weak-to-TV continuity at arbitrary feasible laws, not to the optimizer-specific theorem.

## 8. Result boundary

The independently supplied radius repair, local-to-global argument, and lower construction are written mathematical evidence conditional on the two specifically listed unverified research imports. They do not certify the old proof bodies, cure any historical hold, establish a rate above, prove epsilon-uniformity, or make a formal or priority/novelty claim. Parent assessment remains separate; the original pinned candidate's M1 and m1 are not silently edited away.
