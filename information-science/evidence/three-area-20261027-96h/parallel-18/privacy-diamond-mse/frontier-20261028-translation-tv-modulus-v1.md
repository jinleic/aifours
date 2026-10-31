# Exact translation asymptotic and an explicit original-law TV modulus obstruction

**AUTHOR CANDIDATE — WRITTEN with one exact rational check; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:20:29 PDT 2026`.

## 1. Original full-law problem and new result

Fix EVERY finite epsilon>0. Let b=e^(-epsilon), m=b/(1-b), D the full CLOSED unit l1 diamond, and F_epsilon the ALL-Borel probability laws satisfying the additive privacy inequality for every Borel event and every shift in D. Let V be the original squared-Euclidean cost optimum and mu_* its unique law.

At the named LAW642 input, the optimizer's canonical density is `p_*(x)=Z^(-1)b^(n_S(x))`, `n_S(x)=min{k:x in S+kD}`, where S is a centrally symmetric compact convex body with nonempty interior. For any Euclidean UNIT vector e let u be a Euclidean unit vector perpendicular to e; let `w_K(u)=max_(x in K)u·x-min_(x in K)u·x` denote width. For the actual translated optimizer `mu_t=tau_(t e)mu_*`, the candidate exact first-order formula is

    lim_(t->0+) TV(mu_t,mu_*)/t = [w_S(u)+m w_D(u)]/Z.                   (1)

For every t, mu_t is an actual full-D-private law and `J(mu_t)=V+t^2`, because mu_* is centered. Thus for the true original-law modulus

    omega_epsilon(delta)=sup{TV(mu,mu_*):mu in F_epsilon, J(mu)<=V+delta},

one has the explicit geometry-dependent bound

    liminf_(delta->0+) omega_epsilon(delta)/sqrt(delta)
       >= (1/Z) max_(||u||_2=1) [w_S(u)+m w_D(u)] >0.                  (2)

The maximum is attained. This quantitatively strengthens the previous positive-but-tiny far-tail lower constant. It is SHARP FOR THE TRANSLATED FAMILY, not proved to be the optimal constant among all near-optimal laws. No square-root UPPER bound, explicit equality for omega, epsilon-uniformity, novelty, or stronger assurance is asserted.

There is also an exact, nonasymptotic formula for every centered diamond staircase Q_gamma on sufficiently short axis translations:

    TV(tau_(t e1)Q_gamma,Q_gamma)
       =[2(gamma+m)t-t^2/2]/Z_gamma,                                    (3)
    0<t<min{2gamma,1/(2sqrt(2))},    Z_gamma=2(gamma^2+2m gamma+m+2m^2).

When the actual optimizer core is gamma D, (3) applies to that actual law. This does NOT assume the core is a diamond above the separately known transition.

## 2. Exact input, privacy and cost

The only research import needed for (1)–(2) is the parent-WRITTEN_SUPPORTED all-law LAW642 optimum/core theorem `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`. It gives the original unique law, its centered symmetric convex compact core S, full-event feasibility and finite second moment. It is not re-certified by this note.

Translations preserve the original event inequality by applying it to the translated event; they introduce no restricted-shift or moment-tuple surrogate. Since p_* is centrally symmetric, its mean exists and equals 0, so

    J(tau_(t e)mu_*)=E|X_*+t e|^2=V+t^2.                                 (4)

The original law has exact epsilon privacy: in a sufficiently far positive quadrant its canonical index rises by one when e1 is added, giving equality on an actual positive-probability rectangle. Translation preserves this exact ratio. Thus the witnesses in (2) are not just approximately private. The modulus lower bound itself needs only feasibility.

## 3. Separated level boundaries give an exact TV sum

Let `K_k=S+kD`. The layer identity is

    p_*=(1-b)/Z sum_(k>=0)b^k 1_(K_k).                                   (5)

The unit diamond contains the Euclidean ball of radius `r0=1/sqrt(2)`. Thus `K_k+r0 B_2 subset K_(k+1)`, and the distance between any two distinct nested level boundaries is at least r0. If `0<t<r0/2`, the symmetric-difference sets `K_k triangle (K_k+t e)` lie in pairwise disjoint t-neighborhoods of those boundaries. This is an actual uniform separation across all k, not a finite-tail assumption.

On each such disjoint region only one summand in (5) changes. Tonelli gives the exact identity

    TV(mu_t,mu_*)=(1-b)/(2Z) sum_(k>=0)b^k |K_k triangle(K_k+t e)|.   (6)

The countable sum is finite; its first-order bound is proved below.

## 4. Slice proof of the exact directional constant

Slice a compact convex K by lines parallel to e, with scalar transverse coordinate y on e-perpendicular. Each nonempty slice is an interval of length ell_K(y). Translating that interval by t changes length `2 min(t,ell_K(y))`. Hence

    |K triangle(K+t e)| =2 integral_(proj_(e^perp) K) min(t,ell_K(y))dy. (7)

Every transverse point in the INTERIOR of the projection has positive slice length; possible zero-length endpoint slices have one-dimensional measure zero. Dominated convergence gives

    lim_(t->0+) |K triangle(K+t e)|/t =2 w_K(u),
    |K triangle(K+t e)|/t <=2 w_K(u).                                    (8)

Minkowski addition commutes with projection, and lengths of sums of real intervals add. Therefore `w_(S+kD)(u)=w_S(u)+k w_D(u)`. The bound in (8) and the finite weighted geometric sum justify dominated convergence in (6). Using `(1-b)sum b^k=1` and `(1-b)sum k b^k=m` proves (1). S has interior, so the coefficient is strictly positive in every direction.

The map u->w_S(u)+m w_D(u) is continuous on the compact unit circle. Fix a maximizer and put t=sqrt(delta) in (4), giving (2). This is a LOWER bound for the full nonlinear optimum modulus; the proof does not claim the translated family exhausts it. It also independently rules out any uniform exponent greater than 1/2 at fixed epsilon.

## 5. Exact axis-translation formula for a diamond core

Let S=gamma D with gamma>0, so K_k=(gamma+k)D and `Z_gamma=2(gamma^2+2m gamma+m+2m^2)`. For axis translation e1, the vertical slice at y has length `2(gamma+k-|y|)` for `|y|<gamma+k`. If `t<2gamma`, the slice formula (7) evaluates exactly:

    |K_k triangle(K_k+t e1)|=4(gamma+k)t-t^2.

If also `t<1/(2sqrt(2))`, the level-boundary separation justifies (6). Summing the geometric weights gives

    TV(tau_(t e1)Q_gamma,Q_gamma)
       = [2(gamma+m)t-t^2/2]/Z_gamma,

which is (3). This holds for ANY gamma>0, not only a minimizing staircase. For a translated actual optimizer on the diamond branch, J increases exactly by t^2 as in (4). The endpoint gamma=0 produces the same normalized law as gamma=1, so it can be represented by the latter when applying (3).

## 6. Optional simplification of the best direction on the rounded branch

At the separately adopted v241/LAW642 exact regime, S is D4-symmetric and

    S={||x||_1<=2t_*, |x|^2+2m||x||_infinity+T2<=V},
    v=m(1+m),  T2=m+2m^2.

Because S and D are centrally symmetric,

    max_u[w_S(u)+m w_D(u)] =2 max_(s in S,d in D)||s+m d||_2.

A convex norm reaches its maximum over the diamond d at a vertex ±e1,±e2. Choosing the vertex with the sign and coordinate of largest |s_i| gives

    max_d ||s+m d||^2=|s|^2+2m||s||_infinity+m^2 <=V-v.

Above the v241 transition, the true core has a genuine free circular-type arc on which its quadratic inequality is equality; hence the maximum is exactly `sqrt(V-v)`, and (2)'s bound becomes `2sqrt(V-v)/Z`. On a full-diamond core S=gamma D, it is instead `2(gamma+m)/Z`. At transition equality of these expressions is not asserted here without the full source boundary check. This paragraph explicitly imports the separated v241 branch statement; the all-regime width formula (2) does not.

## 7. Actual exact arithmetic check and limits

A bounded local `fractions.Fraction` check used a SYNTHETIC b=1/2, gamma=1 staircase and t=1/10; it did not claim gamma=1 is the original optimizer:

```text
synthetic b= 1/2 gamma= 1 Z= 12 shift= 1/10 exact_TV= 79/2400 limit_coefficient= 1/3 cost_increase= 1/100
slice_identity for any a>=t/2: symmetric_difference_area=4*a*t-t^2
```

The exact first-order formula relies on the written disjoint-boundary and convex-slice proof, not the selected arithmetic. The original TV-stability candidate `frontier-20261028-all-law-tv-stability-v1.md` received f68 0F/1M/1m and has the separate additive radius repair SHA `05d802dd109d144ac10655d1a1f0e42de652e4305f3b51239f6bbcc3e27f8cd4`; this note's lower bound does NOT import that TV-stability theorem. Its optional branch paragraph uses the stated v241/LAW642 source scope only.

Request disjoint review of uniform boundary separation, countable absolute-sum exchange, convex slices and the optimization over directions. No formal/kernel/human/configured-family, priority or novelty acceptance is claimed; historical held outcomes are not accepted premises.
