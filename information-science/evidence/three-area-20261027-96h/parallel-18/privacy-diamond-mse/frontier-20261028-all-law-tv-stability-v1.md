# Full-law near-optimal privacy mechanisms converge in total variation

**AUTHOR CANDIDATE — WRITTEN with exact rational checks, NOT independently reviewed or parent-adopted.** Actual native pre-write clock `Wed Oct 28 18:03:36 PDT 2026`.

## 1. Exact original model and new conclusions

Fix EVERY finite epsilon>0; write `b=e^(-epsilon)` and `D={h:||h||_1<=1}`. Let F_epsilon contain ALL Borel probability laws mu satisfying

    mu(A)<=b^(-1)mu(A+h)       for EVERY Borel A and EVERY h in the FULL CLOSED D.

Set `J(mu)=integral |x|_2^2 mu(dx)` and `V=inf_(mu in F_epsilon)J(mu)`. Let mu_* denote the unique original optimizer imported below.

**A. Weak-to-TV continuity at the ACTUAL optimum.** If ANY sequence `mu_n in F_epsilon` converges weakly to mu_*, then `TV(mu_n,mu_*)->0`. No moment convergence, symmetry, parametric family, density regularity or exact-privacy-equality hypothesis is needed for this statement.

**B. All-law near-optimal stability.** If ANY feasible sequence satisfies `J(mu_n)->V`, then the ENTIRE sequence converges to mu_* in total variation AND in Euclidean Wasserstein-2 distance. This includes arbitrary nonradial, nonsymmetric and nonsmooth densities, and is not restricted to the prior finite joint-bin family. The privacy bound and epsilon are fixed across the sequence.

**C. Uniform fixed-epsilon modulus.** Define

    omega_epsilon(delta)=sup{TV(mu,mu_*): mu in F_epsilon, J(mu)<=V+delta}.

Then `omega_epsilon(delta)->0` as delta decreases to zero. Moreover for a positive, explicitly specified fixed-epsilon constant c_epsilon,

    omega_epsilon(delta)>=c_epsilon sqrt(delta)       for all sufficiently small delta>0.   (1)

Thus uniqueness/near-optimality gives a genuine uniform TV modulus, but no universal TV upper exponent greater than 1/2 can hold. This result does NOT prove a square-root UPPER rate, any explicit upper modulus, a rate uniform in epsilon, or TV convergence when epsilon itself varies.

A sharp distinction matters: weak-to-TV continuity is FALSE at a general feasible interior law, even at fixed epsilon. An explicit fully private oscillatory counterexample is in §8. The saturation geometry of the actual optimizer is essential.

## 2. Exact research imports

- LAW642 original all-law unique optimizer/core theorem, parent `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, lines 14–22. It gives finite positive V, unique mu_*, canonical density

      p_*(x)=Z^(-1)b^(n_S(x)),   n_S=min{k>=0:x in S+kD},
      S={||x||_1<=2t, |x|_2^2+2m||x||_infinity+T2<=V},
      m=b/(1-b), T2=m+2m^2, V<lambdaP=4m^2+4m+1/3.

  S is a compact centrally symmetric convex body with nonempty interior containing 0.
- Separately adopted v241 threshold/diamond-versus-rounded theorem, `institute/runs/three-area-2026-10-23-96h/privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md`, SHA `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`, lines 5–11,29–35. Its positive threshold s_t is the unique positive root of `2s^3-9s^2-108s-81=0`; the core is gamma D with `0<gamma<1` on and below that threshold. This is the SEPARATED adopted result, not an original held threshold manuscript.

These are named same-harness WRITTEN_SUPPORTED inputs, not formal/human/configured-family proofs. Standard imports include Radon–Nikodym, Lebesgue differentiation, Portmanteau/Prokhorov, elementary convex-set interior/boundary facts, and the standard weak-plus-second-moment criterion for W2. No MDA, PMLR, v253, new external source or earlier unreviewed candidate is required for A–C.

## 3. The actual core cannot contain the full sensitivity diamond

The only special geometric condition needed below is

    D is NOT a subset of S.                                               (2)

On the adopted diamond side, `S=gamma D` with 0<gamma<1, so (2) is immediate. On the rounded side, put `s=sinh^2(epsilon/2)`. The threshold cubic is -196 at s=1 and has a unique positive root; hence `s>s_t>1`. The identity `m(1+m)=1/(4s)` implies `m<1/4`, since m>=1/4 would give `m(1+m)>=5/16>1/4`.

The core inequality at the axis point e1=(1,0) would require

    1+2m+T2 = 1+3m+2m^2 <= V < 4m^2+4m+1/3.

But for m<1/4,

    1+3m+2m^2-(4m^2+4m+1/3)
      = 2/3-m-2m^2 > 2/3-1/4-1/8 = 7/24 >0.

Thus e1 is not in S, proving (2) on the rounded side as well, including the exact boundary handled on the diamond side. No decimal threshold or selected source probe is needed.

## 4. Pointwise private representatives and saturation plateaux

For every feasible law nu and Borel A of finite Lebesgue area, integrate the event inequality over D and use Tonelli:

    2 nu(A) <= b^(-1) integral_D nu(A+h) dh <= b^(-1)|A|.

Thus nu has a density bounded by `C=1/(2b)` a.e. Define the finite representative

    p_n(x)=limsup_(j->infinity) mu_n(B_2(x,1/j))/|B_2(0,1/j)|.

Lebesgue differentiation makes this a density of the SAME law, and the bound above gives `0<=p_n(x)<=C` for EVERY x. Applying the original privacy inequality to each pair of translated shrinking balls gives simultaneously for ALL x,y with `||x-y||_1<=1`,

    p_n(y)>=b p_n(x).                                                     (3)

No uncountable union of density exceptional sets is taken.

Put

    U_0=int S,
    U_k=int(S+kD) minus (S+(k-1)D),      k>=1.                           (4)

They are bounded open plateaux for each fixed k. All boundaries of the full-dimensional convex bodies S+kD have planar measure 0, so their union covers the plane up to a null set. On U_k, `p_*=b^k/Z` exactly. The point of the next lemma is that each plateau point has a positive-volume, STRICTLY-within-D neighbor on an adjacent plateau where the optimizer saturates (3).

## 5. Every plateau point has a strict adjacent-level neighbor

**Core k=0.** Take x in int S. If `x+D subset S`, central symmetry gives `-x+D subset S`; convexity of S then gives `D subset S` by averaging `(x+d)` and `(-x+d)` for every d in D, contradicting (2). Since S is closed, `x+int D` is not contained in S either. Choose h in int D with `y=x+h` outside S. Because x is in int S and h in int D, y lies in `int(S+D)`. Thus y lies in U_1, and `||x-y||_1<1`.

**Shell k>=1.** Take x in U_k. The interior formula for sums of convex bodies gives `x=z+h` with `z in int S`, `h in int(kD)`. Set `y=z+(k-1)h/k`. Then `y in int(S+(k-1)D)` and `||x-y||_1=||h||_1/k<1`. If k>=2 and y belonged to S+(k-2)D, adding h/k in int D would place x in `int(S+(k-1)D)`, contradicting x outside the closed inner body. Thus `y in U_(k-1)`; for k=1 the same definition gives y in U_0.

In either case x and y lie in open plateaux and their l1 distance is strictly less than 1. Small Euclidean balls U around x and B around y can therefore be chosen inside those plateaux so EVERY pair of points in U×B is at l1 distance strictly less than 1.

## 6. Saturation upgrades weak convergence to local L1 convergence

Assume `mu_n => mu_*` weakly. Let p_n be the pointwise representatives above. Boundaries of Euclidean balls have mu_*-measure 0 because mu_* has a density, so `mu_n(U)->mu_*(U)` and `mu_n(B)->mu_*(B)` for every ball used in §5.

For k>=1, U lies in U_k and B in U_(k-1). By (3), for EVERY x in U,y in B,

    p_n(x)-b p_n(y)>=0.

Its integral over U×B is

    |B| mu_n(U) - b |U| mu_n(B) -> 0,

because `p_*|U=b p_*|B`. Hence the L1 integral of that nonnegative difference tends to 0. For x,x' in U, triangle inequality through a common y in B gives

    |p_n(x)-p_n(x')|
       <= |p_n(x)-b p_n(y)| + |p_n(x')-b p_n(y)|.

Integrating and using the mean `bar p_n=mu_n(U)/|U|` gives

    integral_U |p_n-bar p_n| <= (2/|B|) integral_(U×B)|p_n(x)-b p_n(y)| ->0.

Since `bar p_n->p_*|U`, this proves `integral_U|p_n-p_*|->0`.

For k=0 the saturated comparison is instead `p_n(y)-b p_n(x)>=0` with y in U_1; the same calculation has the harmless factor 1/b. Thus EVERY point of every U_k has a ball on which the L1 distance tends to zero.

Each bounded U_k admits finite subcovers of compact subsets with arbitrarily small remaining area. The uniform bound C for p_n and p_* controls the uncovered part, so `integral_(U_k)|p_n-p_*|->0` for each fixed k. For a large N, the compact convex S+ND has a mu_*-null boundary; weak convergence gives convergence of its total mass, and its complement has arbitrarily small mu_* mass as N increases. Hence the total L1 tails are uniformly small eventually. Combining finitely many U_k, the null shell boundaries and the tails yields

    integral_R2 |p_n-p_*| dx ->0,

which proves A. This uses the actual all-shift saturation graph, not an invalid assertion that bounded densities plus weak convergence automatically imply L1 convergence.

## 7. Near-optimal laws, W2, and a lower bound on the modulus

Let `mu_n in F_epsilon` satisfy `J(mu_n)->V`. The second moments are bounded, so the sequence is tight. A weak subsequential limit remains in F_epsilon: for EACH fixed h, pass the event-order inequality through nonnegative compactly supported continuous test functions and use Radon measure order; the SAME weakly convergent subsequence works for all h. Lower semicontinuity gives its J<=V, so LAW642's unique all-law optimizer forces the limit mu_*. Every subsequence has the same limit, hence the whole sequence converges weakly to mu_*; A gives TV convergence. Weak convergence plus convergence of second moments `J(mu_n)->J(mu_*)` gives W2 convergence by the standard Wasserstein criterion. This proves B.

If `omega_epsilon(delta)` failed to tend to 0, a sequence delta_n↓0 and feasible mu_n with cost<=V+delta_n but TV bounded below would contradict B. This proves the uniform fixed-epsilon upper-modulus existence without giving an explicit rate.

For the complementary lower bound, independently construct `mu_t=Law(X_*+tU)`, where U has independent triangular coordinates with density `(1-|u|)_+` on [-1,1]. Convolution preserves EVERY event/full-D inequality and `E U=0`, `E|U|^2=1/3`, so

    J(mu_t)=V+t^2/3.                                                      (5)

Let c=max_(x in S)(x1+x2), choose B above all core coordinates and choose an integer k with c+k>2B+8. For x in the far positive quadrant, `n_S(x)=ceil(x1+x2-c)`. On a unit-length diagonal strip of thickness t immediately above the level `x1+x2=c+k`, with 0<t<1/4, the smoothed density exceeds p_* by at least

    Z^(-1)b^k(1-b) Pr(U1+U2>1) = Z^(-1)b^k(1-b)/24.

The last probability is the exact triangle integral in §9. The strip has planar area t. Thus

    TV(mu_t,mu_*) >= b^k(1-b)t/(48Z).                                  (6)

Set t=sqrt(3delta) for 0<delta<1/48. Equation (5) and (6) give (1) with `c_epsilon=sqrt(3)b^k(1-b)/(48Z)>0`. In particular any proposed universal fixed-epsilon upper bound `TV<=C(J-V)^a` with a>1/2 fails along this ACTUAL feasible family. This lower obstruction does not prove a matching square-root upper bound.

## 8. Why the private saturation hypothesis cannot be removed

Let `a=log 2`, epsilon=log 6, and let `p0(x)=(a^2/4)exp(-a||x||_1)`. For positive integers n define the FULL-SUPPORT density

    p_n(x)=p0(x)[1+(1/2)sin(2pi n x1)].

Its integral is 1 because p0 is even in x1 and the sine term is odd; it is positive everywhere. For any h in D, the Laplace factor changes by at most 2 and the oscillatory factor's ratio is at most `(3/2)/(1/2)=3`. Thus `p_n(x)<=6p_n(x+h)` for all x,h, giving actual epsilon=log 6 feasibility for every event. The privacy bound is at most log6; exact budget attainment is NOT asserted.

The Riemann–Lebesgue lemma gives weak convergence `p_n dx => p0 dx`. Periodic averaging gives `integral p0 |sin(2pi n x1)| dx -> 2/pi`, so

    TV(p_n dx,p0 dx) -> 1/(2pi) >0.

Therefore general weak convergence within one fixed F_epsilon does NOT imply TV convergence. The target p0 is a feasible slack law, not claimed to be an optimizer, and this example is not a counterexample to A–C.

## 9. Actual exact arithmetic and review boundaries

A bounded local Python `fractions.Fraction` check produced

```text
negative-control DP density ratio bound= 6
rounded-core axis margin >= 7/24
core no-containing-diamond via axis bound at m=1/4: True
```

The triangular constant in §7 is the elementary exact integral

    Pr(U1+U2>1)=integral_0^1 integral_(1-u)^1 (1-u)(1-v)dv du=1/24.

It was independently Fraction-checked in `frontier-20261028-smooth-exact-privacy-stability-v1.md`, SHA `40651c034f1800091c1daeb17ea9490fcf9e745fe4c74494381869b5e3626eec`, but the displayed integral is enough for this written proof; that unreviewed file is not a mathematical premise.

This is a full original-law, fixed-epsilon stability candidate conditional on the named LAW642/v241 results. Request a disjoint review of core noncontainment, plateau-neighbor existence, pointwise representative, every local-to-global L1 step and the weak-closure/W2 caller. No upper TV exponent, epsilon-uniform modulus, formal/kernel/human/configured-family, independent-model or novelty acceptance is claimed. Historical quarantined outcomes are not accepted premises.
