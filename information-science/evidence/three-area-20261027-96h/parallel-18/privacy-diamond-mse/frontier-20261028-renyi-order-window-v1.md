# A joint Renyi-order/cost window for actual near-optimal translations

**AUTHOR CANDIDATE — WRITTEN with an exact-affinity/Decimal diagnostic; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 18:27:10 PDT 2026`.

## 1. Exact original model and the phase transition

For EVERY fixed finite epsilon>0, set b=e^(-epsilon), let D be the FULL CLOSED unit l1 diamond, and let F_epsilon contain ALL Borel laws satisfying the additive privacy inequality for EVERY event and EVERY h in D. Let V be the original all-law squared-Euclidean optimum and mu_* its unique law. Fix ANY Euclidean unit vector e and set

    mu_t=tau_(t e)mu_*,       delta=t^2,       0<t<1/(2sqrt(2)).

These are actual exact-epsilon private laws with `J(mu_t)=V+delta`. For an arbitrary fixed real a>0, let the Renyi order grow with the shrinking cost gap as

    alpha_a(t) = 1 + [a/epsilon] log(1/t)
               = 1 + [a/(2epsilon)] log(1/delta).                       (1)

**Candidate exact limit, in BOTH directions:**

    lim_(t->0+) D_(alpha_a(t))(mu_t||mu_*)
      = lim_(t->0+) D_(alpha_a(t))(mu_*||mu_t)
      = 0                          if 0<a<=1,
      = epsilon(1-1/a)              if a>1.                             (2)

As a increases the limit rises continuously from 0 to epsilon. The two max-divergences are exactly epsilon at every sufficiently small nonzero t. Thus fixed finite orders vanish along this near-optimal family, but orders of size `log(1/delta)/(2epsilon)` reveal a genuine crossover. This is a statement about Renyi divergence BETWEEN the actual law and the optimizer, not the Renyi privacy parameter of a different mechanism.

The limit is for one explicit feasible family; it does NOT assert the worst-case joint-order modulus has the same phase diagram. Indeed other shifted-mixture near-optimizers can make forward fixed-order alpha>1 divergences arbitrarily large. No original target/value redefinition, all-epsilon uniformity, numerical proof, novelty or parent adoption is claimed.

## 2. Sole named research import and exact translator

The input is parent-WRITTEN_SUPPORTED LAW642 `privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`: unique all-law optimum, finite V, centered compact convex core S with interior, and density `p_*=Z^(-1)b^(n_S)`, `n_S=min{k:x in S+kD}`. No TV-stability theorem, its f68 radius repair, MDA, v241/v253, PMLR, or other unreviewed scientific conclusion is a premise.

Translation preserves the event privacy inequalities, and symmetry gives `J(mu_t)=V+t^2`. The original exact epsilon is attained by a far-quadrant event; translating that event shows the same for mu_t. The normalized moment and actual Borel/full-D caller are therefore unchanged.

## 3. Exact affinity and linear-order TV

Write K_k=S+kD. Since D contains the Euclidean ball of radius 1/sqrt(2), different level boundaries are separated by at least 1/sqrt(2). For `0<t<1/(2sqrt(2))`, their t-neighborhoods and hence their translated symmetric-difference bands are pairwise disjoint. Each K_k and its translate have equal entering and leaving area

    A_k(t)=|(K_k+t e) minus K_k|=|K_k minus(K_k+t e)|.

On an entering strip the translated/original density ratio is b^(-1), and on the leaving strip it is b; all other points have ratio 1. Thus with `T(t)=TV(mu_t,mu_*)`,

    T(t)=(1-b)/Z sum_(k>=0)b^k A_k(t),
    integral p_t^alpha p_*^(1-alpha)
      =1+[b^(1-alpha)+b^alpha-(1+b)]T(t)/(1-b).                        (3)

This identity also applies in the reverse direction because its coefficient is invariant under alpha<->1-alpha. It is an actual global integral, not a local approximation.

The TV is LINEAR to first order with a positive coefficient. Indeed slicing each convex K_k by lines parallel to e gives

    |K_k triangle(K_k+t e)|
      =2 integral_(proj K_k) min(t,ell_k(y))dy,
    lim_(t->0+) |K_k triangle(K_k+t e)|/t =2 width_(e^perp)(K_k).

Minkowski addition makes the projection width `w_S+k w_D`, and the geometric weighted sum is finite. Dominated convergence yields

    T(t)/t -> C_e=[w_S+m w_D]/Z >0.                                     (4)

In particular T(t)=Theta(t), with no use of the earlier TV-stability modulus. The exact all-order affinity (3) and width calculation are rederived here; the related unreviewed previous author note is not imported as an opaque result.

## 4. Derivation of the joint-order limit

For alpha=alpha_a(t),

    b^(1-alpha)=exp(epsilon(alpha-1))=t^(-a),
    b^alpha=b t^a.

Consequently the coefficient of T in (3) is

    c_alpha=[t^(-a)+b t^a-(1+b)]/(1-b),
    c_alpha T(t) = [C_e/(1-b)] t^(1-a)[1+o(1)].                        (5)

The divergence is `log(1+c_alpha T)/(alpha-1)`, with `alpha-1=(a/epsilon)log(1/t)`.

- If 0<a<1, (5) tends to 0, so the numerator log tends to 0 while the denominator tends to infinity. The limit is 0.
- If a=1, (5) tends to the finite positive constant C_e/(1-b); the numerator stays bounded and the denominator tends to infinity. The limit is again 0.
- If a>1, (5) diverges, and its log is `(a-1)log(1/t)+O(1)`. Dividing by `(a/epsilon)log(1/t)` gives `epsilon(1-1/a)`.

The reverse affinity is identical, so the reverse limits are the same. For alpha=infinity the entering/leaving bands have positive area and the likelihood ratio attains b^(-1), giving exactly epsilon in both directions for each small t. This is compatible with, but not an interchange of, the limits alpha->infinity and t->0.

## 5. Actual bounded diagnostic, with failed first step disclosed

On a SYNTHETIC staircase S=D, b=1/2, Z=12, an exact slice calculation gives `T=(4t-t^2/2)/12` for the displayed short shifts. For `t=2^(-q)` and `a in {1/2,1,2}`, equation (1) has integer orders `alpha=1+a q`. I computed each affinity with `fractions.Fraction` and only its logarithm with Python Decimal. The first attempted cell raised `TypeError: conversion from Fraction to Decimal is not supported`; I corrected the alpha conversion to an integer and reran the failed loop. Actual corrected output:

```text
q= 8 shift=2^-q; (a,alpha,Dalpha)= [('1/2', 5, '0.009281389'), ('1', 9, '0.063535942'), ('2', 17, '0.321565394')]
q= 16 shift=2^-q; (a,alpha,Dalpha)= [('1/2', 9, '0.000323197'), ('1', 17, '0.031925982'), ('2', 33, '0.333903461')]
q= 32 shift=2^-q; (a,alpha,Dalpha)= [('1/2', 17, '0.000000636'), ('1', 33, '0.015963301'), ('2', 65, '0.340238198')]
a=2 predicted limit eps/2= 0.346573590
```

The Decimal numbers are numerical diagnostics, not enclosures or proof of (2); S=D in this sample is not claimed to be the actual original optimizer. All-variable limit proof is §4. The original typed-error output remains disclosed and no file was overwritten to disguise it.

## 6. Review and nonclaims

This author candidate depends on LAW642 and ordinary convex slicing/geometric summation. It does not repair or import the f68 TV-stability chain. The order window does not characterize a supremum over all near-optimizers, nor commute limits beyond the exact family stated. Request a disjoint review of disjoint shell bands, affinity normalization, width limit, alpha-dependent errors and both directed conventions. No parent, independent-model/human/formal/kernel or novelty acceptance is claimed; historical held outputs remain nonpremises.
