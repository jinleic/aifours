# Threshold-free TV stability from a strict shield-improvement argument

**AUTHOR CANDIDATE — WRITTEN, with exact rational shield control; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:34:54 PDT 2026`.

## 1. Actual target and new theorem

Fix EVERY finite epsilon>0, write b=e^(-epsilon), and let F_epsilon be ALL Borel noise laws on R^2 satisfying the epsilon privacy inequality for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. Let `J(mu)=E|X|_2^2`, V its full-law minimum, and mu_* its unique law.

**Candidate:** ANY feasible sequence `mu_n=>mu_*` weakly converges to it in total variation. In particular ANY feasible cost-near-minimizing sequence `J(mu_n)->V` converges to mu_* in TV and W2, and the uniform fixed-epsilon cost-to-TV modulus tends to zero.

Unlike the earlier original-TV candidate, this proof uses NO v241 threshold, no diamond-radius inequality and no input from any unreviewed erosion criterion. Its only research input is LAW642's actual full-law optimum/unique law/canonical compact convex core. The new step is a direct **shield improvement lemma**: a geometric shell law whose core contains a positive-area set of points with their entire D-neighborhood inside the core cannot be a squared-Euclidean minimizer. Hence the actual optimizer's core erosion has area zero, which is enough for the saturation proof; showing it is EMPTY is unnecessary.

The f68 review on the DIFFERENT frozen earlier TV candidate remains `0F/1M/1m`. That candidate's original radius gap is separately repaired in `frontier-20261028-all-law-tv-stability-v1-addendum-1-f68-radius-repair.md`, SHA `05d802dd109d144ac10655d1a1f0e42de652e4305f3b51239f6bbcc3e27f8cd4`. The proof here bypasses that caller prospectively; it does not edit old bytes, erase the historical finding, or imply independent review/parent adoption of this successor.

## 2. Sole research import and geometric definitions

Parent LAW642 `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, gives finite V, the unique ORIGINAL optimum, and its density

    p_*(x)=Z^(-1)b^(n_S(x)),       n_S=min{k>=0:x in S+kD},

where S is a compact convex body with nonempty interior. Its central symmetry is NOT required for the new erosion argument. Define the closed core erosion

    E={x:x+D subset S}.                                                   (1)

Standard ingredients explicitly used below: Radon–Nikodym/Lebesgue differentiation, elementary convex-body interior and boundary facts, Tonelli, weak compactness/Portmanteau and the weak-plus-second-moment W2 criterion. LAW642 is not re-established or formalized here.

## 3. Strict shield improvement forces |E|=0

Assume for contradiction that the compact E has positive area. On E subset S, p_* is the constant 1/Z. Since each Euclidean circle has planar area zero, the squared-radius cost `|x|^2` cannot be almost everywhere constant on a positive-area E. Choose disjoint measurable E1,E2 subset E with positive finite areas and real `r1<r2` such that

    |x|^2<=r1 on E1,        |x|^2>=r2 on E2.

Define the bounded signed function

    f=1_(E1)/|E1| - 1_(E2)/|E2|.

Then `integral f=0` but `integral |x|^2 f <= r1-r2<0`. Choose lambda>0 sufficiently small that `|lambda f|<=c`, where `c=(1-b)/[2(1+b)]`. Define

    p'(x)=p_*(x)[1+lambda f(x)].                                         (2)

It is positive. Its mass is exactly 1 because p_* is constant on E and integral f=0. Its squared cost is FINITE and strictly smaller:

    J(p')-V=(lambda/Z) integral_E |x|^2 f <0.                             (3)

It remains to verify actual full-D privacy, not just a directional variation. If two points x,y at l1 distance<=1 BOTH lie in S, their unperturbed densities are 1/Z and their factors lie in [1-c,1+c]; their ratio is at most

    (1+c)/(1-c)=(3+b)/(1+3b)<1/b.

If exactly one point is outside S, neither point lies in E: for a point in E its entire D-neighborhood is in S. Both densities are then unperturbed, so the original pointwise staircase privacy applies. Outside/outside pairs are also unchanged. Thus p' is pointwise private for EVERY h in closed D, and its law obeys EVERY Borel-event inequality. Equation (3) contradicts the actual all-law optimality of p_*.

Therefore

    |E|=0.                                                                (4)

This conclusion is stronger in its logical economy than the earlier radius proof: it uses neither a transition regime nor uniqueness. It does NOT assert E is empty, and it does not rely on a prior weak-to-TV theorem.

## 4. Null erosion yields weak-to-TV at the ACTUAL optimizer

Let mu_n in F_epsilon converge weakly to mu_*. Integrating privacy over D gives all laws a common density bound `C=1/(2b)`. Shrinking-ball limsups supply finite density representatives p_n of the SAME laws satisfying `p_n(y)>=b p_n(x)` for EVERY pair with `||x-y||_1<=1`.

Let U0=int S and `Uk=int(S+kD) minus (S+(k-1)D)` for k>=1. Convex boundaries are null; the U_k cover the plane modulo null boundaries, and p_*=b^k/Z on U_k.

For x in U0 minus E, x+D is not contained in S; closedness lets us pick h in int D with y=x+h outside S, hence y in U1 and distance<1. For x in U_k,k>=1, write x=z+h with z in int S and h in int(kD), and put y=z+(k-1)h/k. Then y is in U_(k-1) and `||x-y||_1<1`: otherwise y would belong to S+(k-2)D and adding h/k in int D would put x in the forbidden inner body. This also covers k=1 with y=z in U0.

Choose balls U around x and B around y within these plateaux, so every cross-pair has distance<1. For k>=1, the nonnegative pointwise slack has

    integral_(U×B)[p_n(x')-b p_n(y')]
      = |B|mu_n(U)-b|U|mu_n(B) ->0,

because the target plateaux saturate the inequality and ball boundaries have mu_*-measure zero. A shared y and the triangle inequality yield

    integral_U |p_n-mean_U(p_n)|
       <= 2/|B| integral_(U×B)|p_n(x')-b p_n(y')| ->0.

The means converge to the target plateau constant; the k=0 comparison reverses direction and adds only a factor 1/b. Thus p_n->p_* in L1 on a ball around EVERY plateau point except E and null boundaries. Because |E|=0 by (4), finite-ball covers of compact subsets and the common L-infinity cap give L1 convergence on each fixed bounded plateau. Weak convergence of the mass of S+ND (its convex boundary is null), followed by N->infinity, controls the global tails. Therefore `||p_n-p_*||_1->0`, proving the weak-to-TV statement.

The proof requires merely |E|=0, not D not subset S. In particular possible lower-dimensional erosion cannot invalidate the result.

## 5. Near-optimal laws and uniform cost modulus

If J(mu_n)->V, their second moments are bounded, hence they are tight. Any weak subsequential limit remains fully private by passing compactly supported nonnegative continuous test-function order for each h through the SAME subsequence, and has J<=V by lower semicontinuity. LAW642 uniqueness identifies it with mu_*. Thus the whole sequence converges weakly, and §4 gives TV convergence. Weak convergence plus the exact second-moment convergence gives W2 convergence.

Consequently `omega_epsilon(delta)=sup{TV(mu,mu_*):mu in F_epsilon,J(mu)<=V+delta}` tends to zero as delta decreases to 0: otherwise choose a contrary sequence. No explicit upper rate, epsilon-uniformity or upper power exponent is established.

## 6. Actual rational shield-improvement control

As a bounded exact example, let b=1/2, S=2D (so E=D and Z=22). Take

    E1=[-1/4,1/4]^2,
    E2=[1/2,3/4] x [-1/8,1/8],     lambda=1/96.

Both disjoint sets lie inside E. Their areas are 1/4 and 1/16; their average squared radii are 1/24 and 77/192. Equation (2) has factor 25/24 on E1 and 5/6 on E2, so its worst core ratio is 5/4<2. Its EXACT squared-cost decrease is 23/135168. Local Python `fractions.Fraction` output was

```text
S=2D shield sets: areas= 1/4 1/16 squared-cost means= 1/24 77/192
lambda= 1/96 max_relative_perturbation= 1/6 exact_cost_decrease= 23/135168
worst_core_ratio= 5/4 less_than_DP_budget= True
```

This synthetic core is not claimed to be the original optimizer. Its purpose is to check the algebra of the all-pairs-private strict-improvement mechanism; the general proof is §3.

## 7. Assurance boundary

This is an AUTHOR-WRITTEN, threshold-free successor conditional solely on LAW642 and the named ordinary facts. It has not been independently reviewed or parent-adopted; it does not retroactively change f68's finding or v241, nor does it grant its unreviewed KL/Lp/Renyi successors automatic acceptance. Request disjoint review of the two-set strict improvement, full-shift boundary cases, null-erosion plateau coverage, weak closure and compact exhaustion. No formal/kernel/human/configured-family, priority or novelty claim is made; historical held outputs are nonpremises.
