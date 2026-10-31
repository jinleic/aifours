# Sharp erosion criterion for weak-to-TV continuity at a private staircase law

**AUTHOR CANDIDATE — WRITTEN, with exact rational counterexample arithmetic; NOT independently reviewed or parent-adopted.** Native pre-write clock `Wed Oct 28 18:10:22 PDT 2026`.

## 1. A complete if-and-only-if theorem

Fix ANY finite epsilon>0, b=e^(-epsilon), and let `D={h:||h||_1<=1}` be the FULL CLOSED sensitivity diamond. Let F_epsilon be ALL Borel laws obeying `mu(A)<=b^(-1)mu(A+h)` for EVERY Borel A and EVERY h in D.

Let S be ANY compact convex body in R^2 with nonempty interior. No central symmetry, optimality, radius, Euclidean ball assumption or origin condition is imposed. Define

    n_S(x)=min{k>=0:x in S+kD},
    q_S(x)=Z^(-1)b^(n_S(x)),   Z=integral b^(n_S(x)) dx,
    E=S minus-D := {x:x+D subset S}.                                     (1)

Here `minus-D` denotes geometric erosion, NOT set difference. The density q_S is an actual fully private probability law; E is a compact convex set, possibly empty or lower-dimensional.

**Sharp criterion:** the following are equivalent:

1. E has planar Lebesgue measure 0.
2. For EVERY sequence `mu_n in F_epsilon` with `mu_n => Q_S:=q_S dx` weakly, `TV(mu_n,Q_S)->0`.

If E has positive area, there is instead an explicit sequence of ACTUAL exact-epsilon laws which converges weakly to Q_S but stays a positive TV distance away. Thus merely having a compact convex staircase core or pure DP does not guarantee weak-to-TV continuity; the geometric erosion is the precise boundary. Equality cases with nonempty but null erosion are included in the positive statement.

This structural theorem is independent of LAW642, v241, PMLR, MDA and my earlier optimizer-stability candidate. As a separate consequence, the ORIGINAL optimal-law stability candidate applies because its named symmetric optimum core satisfies D not subset S, forcing E empty. This note does not claim any original optimizer/value theorem or global novelty.

## 2. The staircase is an actual full-event law

Because S is bounded and nonempty, all sufficiently large kD translates cover the plane and n_S is finite everywhere. If h belongs to D, membership gives `n_S(x+h)<=n_S(x)+1`; using −h gives the reverse. Hence

    q_S(x)<=b^(-1)q_S(x+h)         for EVERY x and EVERY h in CLOSED D.

The density is integrable: if `S subset aD` then `n_S(x)>=||x||_1-a`, giving an exponential tail, and S has positive area. Normalization gives a probability law, and integrating the pointwise inequality gives every Borel event. The tail is positive at every x.

The privacy parameter is exactly epsilon. Let c=max_S(s1+s2) and choose B larger than both coordinate maxima of S. If x1,x2>B, every s in S is coordinatewise below x, so

    n_S(x)=ceil(x1+x2-c).

Thus in a far-quadrant open rectangle E0, translation by h=(1,0) raises n_S by 1 at every point and `Q_S(E0)=b^(-1)Q_S(E0+h)`. This establishes exact budget attainment, although the iff proof needs only feasibility.

## 3. Null erosion implies weak-to-TV continuity

Suppose |E|=0 and `mu_n => Q_S` weakly with all mu_n in F_epsilon. As in the original-law proof, integrating privacy over D gives all densities the common cap `C=1/(2b)`. Shrinking-ball limsups supply finite measurable representatives p_n of the SAME laws, bounded by C everywhere and satisfying

    p_n(y)>=b p_n(x) whenever ||x-y||_1<=1                               (2)

for ALL point pairs; no uncountable exceptional-set intersection is used.

Write

    U_0=int S,
    U_k=int(S+kD) minus (S+(k-1)D),    k>=1.

The convex-body boundaries have area 0, and the U_k cover the plane up to those boundaries. The target q_S is `b^k/Z` on U_k.

For any x in U_0 minus E, `x+D` is not contained in S; because S is closed, some h in int D has y=x+h outside S. Then `y in int(S+D) minus S=U_1` and its l1 distance from x is <1. For any x in U_k, k>=1, write `x=z+h` with `z in int S` and `h in int(kD)`. Set `y=z+(k-1)h/k`. Then y is in int(S+(k-1)D), at l1 distance <1 from x. If k>=2 and y were in S+(k-2)D, x would lie in int(S+(k-1)D), contradicting x in U_k. Thus y in U_(k-1); for k=1, y in U_0.

For every such x choose small Euclidean balls U around x and B around y contained in the two respective plateaux and with every pair in U×B at distance <1. Ball boundaries have Q_S-measure zero, so weak convergence gives their two mass limits. The pointwise inequality (2) is saturated by q_S on the two adjacent plateaux. If k>=1,

    integral_(U×B)[p_n(x)-b p_n(y)]
       = |B| mu_n(U)-b |U| mu_n(B) ->0,

and the integrand is nonnegative. For k=0 the saturated difference is `p_n(y)-b p_n(x)` and the same conclusion holds with a factor 1/b in the next inequality. A shared y and triangle inequality give, with `bar p_n=mu_n(U)/|U|`,

    integral_U |p_n-bar p_n|
       <= (2/|B|) integral_(U×B)|p_n(x)-b p_n(y)| ->0

for k>=1, with the indicated 1/b modification for k=0. Since `bar p_n->q_S|U`, p_n converges to q_S in L1 on U.

For each bounded plateau U_k, finite ball subcovers of compact subsets plus the uniform cap control all but arbitrarily small area. The excluded E is null. Thus L1 convergence holds on every fixed plateau. Large-k tails are controlled using weak convergence on the compact convex S+ND, whose boundary is Q_S-null, followed by N->infinity. Therefore `||p_n-q_S||_1->0`, which proves (2).

## 4. Positive erosion gives an explicit exact-private counterexample

If |E|>0 then E, being convex, has nonempty interior. Choose x0 in int E and a small ball U such that `U+D subset int S`. Choose a nonzero nonnegative even-about-x0 compactly supported bump psi in U, with `0<=psi<=1`. Choose

    a=(1-b)/[2(1+b)] in (0,1),
    p_n(x)=q_S(x)[1+a psi(x) sin(2pi n(x1-x0_1))].                    (3)

The perturbation is supported inside S, where q_S=1/Z. Oddness of the sine about x0 and evenness of psi give `integral p_n=1` for every integer n; p_n is strictly positive.

For any x,y with l1 distance<=1, if both lie in S, their values are between `(1-a)/Z` and `(1+a)/Z`, and

    (1+a)/(1-a)=(3+b)/(1+3b) < 1/b.

If a pair crosses outside S, neither point can be in supp(psi), because supp(psi)+D lies inside int S. Their densities are then the unperturbed q_S values and satisfy the full privacy inequality. Pairs outside S are also unchanged. Therefore (3) is pointwise full-CLOSED-D private, hence obeys every Borel event.

The unperturbed far-quadrant event from §2 lies outside the compact bump, so EVERY p_n has exact privacy parameter epsilon. Riemann–Lebesgue gives `p_n dx => Q_S` weakly. Periodic absolute-sine averaging instead gives

    TV(p_n dx,Q_S) = [a/(2Z)] integral psi(x)|sin(2pi n(x1-x0_1))|dx
                    -> [a/(pi Z)] integral psi(x)dx >0.

Thus the implication in criterion 2 fails whenever |E|>0. This establishes the converse and completes the iff, including geometric boundary cases.

## 5. Fully explicit one-parameter control

Take S=2D, b=1/2 (`epsilon=log 2`) and

    psi(x)=(1-2||x||_1)_+,     a=1/6,
    p_n(x)=q_(2D)(x)[1+(1/6)psi(x)sin(2pi n x1)].

The bump support lies in (1/2)D and its D-neighborhood is in (3/2)D, strictly inside S. Here S minus-D=D has positive area. Direct layer and radial integration give

    Z=22,     integral psi=1/6,     (1+a)/(1-a)=7/5<2,
    p_n dx => Q_(2D) weakly,       TV(p_n dx,Q_(2D))->1/(792pi)>0.

Each p_n is an actual FULL-event/FULL-CLOSED-D exact-log2 private law. This is a rigorous counterexample to ANY attempted claim that weak convergence within F_epsilon automatically implies TV convergence at all staircase cores; it is not a counterexample to the original optimizer theorem.

A bounded exact `fractions.Fraction` cell checked the constants:

```text
S=2D b=1/2 normalizer= 22 bump_integral= 1/6 ratio_bound= 7/5
TV_limit_coefficient_of_1_over_pi= 1/792
```

The TV limit uses the written periodic-averaging/Riemann–Lebesgue argument, not those rational calculations alone.

## 6. Connection to the actual original optimum

For any centrally symmetric convex S, if E is nonempty choose x in E. Then both `x+D` and `-x+D` are in S, and convexity implies D subset S by averaging equal d-points. Thus D not subset S implies E is empty.

My still-UNREVIEWED `frontier-20261028-all-law-tv-stability-v1.md`, SHA `3f6c2a61738cc92f615e375d88f6dfb10f96b553585b5c8468480a7ec9683f79`, shows from the named LAW642 and separately adopted v241 threshold theorem that the ACTUAL original unique optimal core is centrally symmetric and does not contain D at ANY finite epsilon. If that exact named argument survives review, the criterion above gives weak-to-TV continuity at the original optimizer, and cost-near-optimal compactness gives its all-law TV stability. The present general iff itself does not rely on LAW642, v241 or that unreviewed candidate.

## 7. Assurance

This is an AUTHOR-WRITTEN structural theorem and exact counterexample, not independent-model/human/formal/kernel review, priority, or proof of the original full Euclidean optimum. Ordinary imports: Radon–Nikodym/Lebesgue differentiation, basic convex interiors and null boundaries, Portmanteau, Riemann–Lebesgue and periodic averaging. Request disjoint review of the NULL versus POSITIVE erosion boundary, adjacent-plateau coverage, local-to-global L1 argument and all-crossing privacy check before adoption. Historical held results are not used as premises.
