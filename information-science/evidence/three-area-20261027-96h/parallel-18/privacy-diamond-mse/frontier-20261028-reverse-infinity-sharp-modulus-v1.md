# Reverse max-divergence modulus has exact limiting value epsilon

**AUTHOR CANDIDATE — WRITTEN with an exact rational constant check; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:25:04 PDT 2026`.

## 1. Exact original-law statement

Fix EVERY finite epsilon>0, set b=e^(-epsilon), let D be the FULL CLOSED unit l1 diamond, and let F_epsilon contain ALL Borel laws satisfying the epsilon privacy inequality for EVERY Borel event and EVERY shift in D. Let V be the original all-law squared-Euclidean optimum and mu_* its unique law.

Define the REVERSE max-divergence cost-slack modulus

    R_infinity^-(delta)=sup{D_infinity(mu_*||mu):mu in F_epsilon,J(mu)<=V+delta}.

**Candidate sharp result**, conditional on the named corrected all-law TV-stability input:

    lim_(delta->0+) R_infinity^-(delta) = epsilon.                         (1)

This is an exact NONZERO limiting modulus even though TV, W2 and every fixed finite REVERSE Renyi divergence go to zero. It sharpens the earlier lower bound `liminf>=epsilon`. The forward infinity modulus is instead infinite for every positive slack, at the separately written construction; the two directions are not interchangeable.

The key direct bound is stronger than (1). There is an explicit positive geometric constant kappa_epsilon such that EVERY fully private mu with `T=TV(mu,mu_*)<kappa_epsilon/(2Z)` obeys

    D_infinity(mu_*||mu)
       <= epsilon - log(1-2 Z T/kappa_epsilon).                          (2)

This pointwise statement needs only the named LAW642 optimizer/core geometry and elementary analysis; it does NOT require mu to be near-optimal in cost or import the TV-stability theorem. The latter is needed solely to replace T by an all-law cost-slack modulus tending to zero.

## 2. Exact inputs and review qualifications

LAW642 parent `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, supplies the original unique centered optimizer with density

    p_*=Z^(-1)b^(n_S),   n_S(x)=min{k>=0:x in S+kD},

where S is a compact centrally symmetric convex body containing 0 in its interior, and V is finite.

For the final uniform cost-slack LIMIT ONLY, I import my UNREVIEWED `frontier-20261028-all-law-tv-stability-v1.md`, SHA `3f6c2a61738cc92f615e375d88f6dfb10f96b553585b5c8468480a7ec9683f79`, TOGETHER WITH its f68 review, SHA `901186e44e95fce0456f19ca06a411e5eb1b0f6b83cd7cc01b661d474f830b19`, and the additive radius/slack repair `frontier-20261028-all-law-tv-stability-v1-addendum-1-f68-radius-repair.md`, SHA `05d802dd109d144ac10655d1a1f0e42de652e4305f3b51239f6bbcc3e27f8cd4`. F68 found 0F/1M/1m at the ORIGINAL pinned scope; the corrected composite has NOT thereby been reviewed or parent-adopted. Its named v241/Law imports remain. Equation (2) and the translation lower witness are independent of that TV-stability claim.

## 3. A uniform positive portion of the actual core

Choose rho>0 with `rho B_2 subset S`, and let `M=max_(y in S)||y||_1`. Define

    theta=min{1/2, 1/[2(M+sqrt(2)rho)]},
    kappa=pi theta^2 rho^2 >0.                                           (3)

For EVERY y in S, convexity puts the Euclidean disk

    B_2((1-theta)y,theta rho) subset S.

Every point z of that disk obeys

    ||z-y||_1 <= theta(M+sqrt(2)rho) <= 1/2 <1.

Hence

    |S intersect (y+D)| >= kappa       for EVERY y in S.                  (4)

The constant is explicit once any genuine interior radius rho is specified. No symmetry, selected y, or uniform numerical threshold is used in this geometric step.

## 4. TV closeness forces a global one-budget lower density bound

Let mu be ANY law in F_epsilon, with T=TV(mu,mu_*). A finite bounded all-point private density representative p is obtained as a shrinking-ball limsup, as in the f68-reviewed source; it represents the same law. On all points of S, the canonical p_* equals `a=1/Z`.

For every y in S and all z in `S intersect(y+D)`, pointwise privacy gives `p(y)>=b p(z)`. Integrating and using (4),

    p(y) >= b[a - (1/kappa) integral_S |p-p_*|]
         >= b[a-2T/kappa].                                               (5)

Assume `2ZT<kappa`, so the bracket is positive. For ANY x in R^2, let k=n_S(x). Compactness/closedness give some y in S with `x-y in kD`; splitting that vector into k closed-D steps and iterating privacy gives

    p(x)>=b^k p(y)>=b^(k+1)[a-2T/kappa].                                (6)

The k=0 case uses x=y in S. Since `p_*(x)=a b^k`, (6) implies pointwise

    p_*(x)/p(x) <= b^(-1)/(1-2ZT/kappa).

Taking essential supremum and logs proves (2). It holds even on shell boundaries for these canonical/ball representatives; only the a.e. law ratio is required. The direct bound is not a hidden consequence of near-optimality or of a hypothetical continuity of max divergence.

## 5. Matching lower witness and sharp limit

For any Euclidean unit e, let mu_t be the translate of mu_* by t e. Translation preserves full-D privacy and, since mu_* is centrally symmetric with finite second moment,

    J(mu_t)=V+t^2.                                                       (7)

For all sufficiently small positive t, the two convex core boundaries are crossed on positive-area entering and leaving strips; distinct staircase-level boundaries are separated by at least 1/sqrt(2), so those strips cross no other level. On one strip `p_*/p_t=1/b`, and on the other the reciprocal is 1/b. The original privacy inequality for te in D gives the matching upper ratio 1/b. Therefore

    D_infinity(mu_*||mu_t)=epsilon                                       (8)

(and the forward max divergence also equals epsilon). This is an actual exact-epsilon law and holds for EVERY small t>0, not just in a limiting sense.

The corrected named TV-stability candidate says `omega_epsilon(delta)=sup_{J<=V+delta}TV(mu,mu_*) ->0`. For sufficiently small delta, plug T<=omega_epsilon(delta) into (2):

    R_infinity^-(delta)
      <= epsilon - log(1-2Z omega_epsilon(delta)/kappa) -> epsilon.

Conversely the translated law with t=sqrt(delta) has cost exactly V+delta and reverse max divergence epsilon by (8). Thus the liminf is at least epsilon and (1) follows. The theorem does NOT assert that R_infinity^-(delta)=epsilon for finite positive delta, or give an explicit upper rate for omega.

## 6. Exact constant diagnostic and limits

For a SYNTHETIC staircase core S=D, b=1/2, Z=12, take rho^2=1/2 and M=1. Then theta=1/4, kappa=pi/32. At T=1/1000, a local Fraction check printed

```text
synthetic S=D,b=1/2,Z=12: kappa/pi= 1/32 2*Z*T/kappa times pi= 96/125
using pi>3 makes denominator positive: True
```

This only checks the elementary constants in (2), not that S=D is the actual optimal core or that the uniform TV modulus is correct. Pi>3 follows from an inscribed regular hexagon.

Request disjoint review of (4)–(6), pointwise representative/essential-sup handling and the uniform corrected-TV dependency. No full-source equivalence, new Euclidean optimum, novelty, formal/kernel/human/configured-family or automatic parent acceptance is claimed; historical held material remains a nonpremise.
