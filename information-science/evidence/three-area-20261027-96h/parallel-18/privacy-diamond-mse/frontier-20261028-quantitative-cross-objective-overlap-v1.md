# A source-independent quantitative cross-objective overlap bound

**AUTHOR CANDIDATE — WRITTEN with exact exponent controls; NOT independently reviewed or parent-adopted.** Native pre-write clock `Wed Oct 28 19:00:57 PDT 2026`.

## 1. Exact all-law inequality

For b=e^(-epsilon), let F_b be ALL Borel laws satisfying additive epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. Set `C1=2^(1/3)` and `s=b^(1/3)`.

For any fixed finite K_J>0, the candidate states that there are b0>0 and C_K<infinity such that, for EVERY 0<b<b0, EVERY 0<=xi<=1, and EVERY TWO actual laws mu_L,mu_J in F_b satisfying

    E_muL ||X||_1 <= C1 s (1+xi),
    E_muJ ||X||_2^2 <= K_J sqrt(b),                                      (1)

one has

    1-TV(mu_L,mu_J)
      <= C_K [ b^(1/18)(xi+b^(1/3))^(2/3) + b^(1/6) ].                  (2)

No original optimizer, exact source selector, geometric-core assumption, centeredness or mutual relation of the two input laws is assumed. The bound is a quantitative version of cross-objective separation, valid for a specified first-moment relative budget xi and any squared-cost law with the stated second-moment cap.

**Sharpness of both scales.** For ANY xi(b)->0 with `xi(b)/b^(1/6)->infinity`, there are explicit full-private exact-epsilon laws satisfying (1) with fixed K_J=2 and

    1-TV(mu_L,mu_J) >= (1-o(1))/4 * b^(1/18) xi^(2/3).                (3)

When xi is a suitable constant times b^(1/3), explicit laws satisfying (1) have overlap at least a positive constant times b^(1/6). Thus neither term in (2) can be dropped in general in the exhibited respective regimes. No claim is made that C_K is sharp or that the bound identifies exact finite-b optimizers.

This theorem is source-independent: it imports NO LAW642, v241, MDA, PMLR, f68 or prior research result. It rederives the few peak-floor and mean-bathtub estimates needed below. The earlier still-unreviewed sharp-exponent candidate `frontier-20261028-near-optimal-overlap-sharp-exponent-v1.md` is not an opaque premise.

## 2. All-law mean peak, bathtub deficit and explicit relative budget

Every fully private law has a bounded all-point private density representative. Let p_L be such a representative, M its essential supremum, and choose x0 with `p_L(x0)>=(1-s)M`. Full-D privacy forces `p_L>=ell=b(1-s)M` on x0+D. Set `g=p_L-ell 1_(x0+D)`, `y=s^2 M`, and h=integral g=1-2ell. Thus `0<=g<=M`, `ell=(1-s)y s` and h>=0.

The integrated first norm on ANY translate of D is at least 4/3 by even convexity. The leading floor term and (1), with s<1/2, bound y above uniformly for all xi<=1. Then ell=O(s), so h>=1/2 for sufficiently small s. The exact capped-density bathtub minimum for g is `(2/(3sqrt(2)))h^(3/2)M^(-1/2)`. Since L/s is bounded by 2C1, this term also bounds y away from zero. Hence the scaled bathtub radius `t=sqrt[h/(2y)]` is bounded above by one universal K.

In the scaled coordinates, the EXACT mean-cost identity is

    L(mu_L)/s = (1-s)y F(x0)
                 + [2/(3sqrt(2))]h^(3/2)y^(-1/2) + Delta,              (4)

where `F(x0)=integral_(x0+D)||x||_1 dx>=4/3`, and Delta>=0 is the integral of `(||z||_1-t)` times the difference between the actual scaled g density and the cap y on tD. Because y lies in a fixed positive compact interval, `ell=O(s)` and `(1-2ell)^(3/2)>=1-3ell` give uniformly

    (1-s)y F(x0)+[2/(3sqrt(2))]h^(3/2)y^(-1/2)
      >= f(y)-C s >= C1-C s,
    f(y)=(4/3)y+[2/(3sqrt(2))]y^(-1/2),    min_(y>0)f(y)=C1.

Combining with (1) and (4) yields the quantitative, nonnegative DEFICIT bound

    0<=Delta<=C'(xi+s).                                                   (5)

No rate of weak/TV convergence, source theorem, or uniqueness of a minimizer is used.

## 3. Squared-cost privacy itself controls the other peak

Let M_J be the essential density supremum of mu_J, and take an actual point within an arbitrary factor 1-eta of it. The full-D density inequality supplies floor `b(1-eta)M_J` on some translate x0+D. Since

    integral_(x0+D)|x|_2^2 dx = 2|x0|_2^2+2/3 >=2/3,

letting eta->0 gives `M_J<=3J(mu_J)/(2b)<= (3K_J/2)b^(-1/2)`. Therefore

    mu_J(B_2(r)) <= (3pi K_J/2)b^(-1/2)r^2                             (6)

for every Euclidean ball centered at 0 and every r>0. This is derived directly from privacy and the specified second-moment budget, not an assumed Euclidean optimizer density.

## 4. Optimize the overlap split

The floor of mu_L has total mass 2ell=O(s). The bathtub comparison density is supported on tD with t<=K. For `r>=2Ks`, its nonnegative deficit outside B_2(r/s) is at least `(r/s-t)` times the scaled g mass there. Hence

    mu_L(B_2(r)^c) <= O(s)+2s Delta/r.                                  (7)

For densities p_L,p_J, overlap `1-TV=integral min(p_L,p_J)`. Splitting at B_2(r) and using (6)–(7),

    1-TV <= O(b^(-1/2)r^2+s+s Delta/r).

Choose `r=max{b^(5/18)Delta^(1/3), 2Ks}` (if Delta=0 the first term is 0). Then

    1-TV <= O[b^(1/18)Delta^(2/3)+b^(1/6)+b^(1/3)].

Substitution of (5) and b^(1/3)<=b^(1/6) proves the all-law bound (2). This proof permits arbitrary moving density peaks and arbitrary xi; its constants do not depend on a hidden convergence rate.

## 5. Matched construction in the intermediate-budget regime

Suppose xi=xi(b)->0 with `xi/b^(1/6)->infinity`. Let L0 be the explicit first-norm shell law with core `2^(1/3)s D`, whose mean cost is `C1 s+O(s^2)`. Let E0 be the explicit Euclidean disk-shell law with core radius `(4/(3pi))^(1/4)b^(1/4)`, whose J-cost is `[2/sqrt(3pi)]sqrt(b)+O(b^(3/4))`; for b small it satisfies (1) with K_J=2. These shell laws are pointwise full-D private by the index triangle inequality; their formulas are elementary geometric sums, not an external theorem.

Define a THIRD actual diamond-shell law Q_q with

    q=b^(5/18)xi^(1/3),
    w=(1/4)b^(1/18)xi^(2/3),
    mu_L=(1-w)L0+w Q_q,       mu_J=E0.                                   (8)

The regime assumption gives `q^3/b=b^(-1/6)xi->infinity`, hence Q_q's top-core probability tends to 1 and `L(Q_q)=O(q)` (indeed <=2q eventually). Since `w q=(1/4)s xi`, the mixture cost satisfies `L(mu_L)<=C1 s(1+xi)` for small b: its extra cost is at most `(1/2)s xi`, while L0's O(s^2) remainder is o(s xi). Both input laws obey every full-D event inequality, and all three compact-core shell components share an exact far-quadrant e1-shift ratio b, so the mixture and E0 have EXACT epsilon privacy.

The component core qD lies inside E0's disk core because `q/b^(1/4)=b^(1/36)xi^(1/3)->0`. Its exact shell normalizer satisfies `Z_q~2q^2`, while E0's normalizer satisfies `Z_E~A0 sqrt(b)`, where `A0=2sqrt(pi/3)<4`. On qD,

    (w p_Qq)/p_E = w Z_E/Z_q -> A0/8 <1.

As p_muL>=w p_Qq, the overlap on that core is at least `w Q_q(qD)=(1-o(1))w`, proving (3). The asymptotic condition on xi ensures the first term in (2) dominates b^(1/6), so the b- and xi-powers are jointly attained up to constants.

## 6. The small-budget b^(1/6) term also occurs

For xi a sufficiently large fixed multiple of s=b^(1/3), choose mu_L=L0 and mu_J=E0. The first trial has cost `C1 s+O(s^2)`, so it meets (1). Its diamond core has radius `C1 s` and lies strictly inside E0's disk core for small b. Its core density is of order b^(-2/3), larger than E0's order b^(-1/2); hence the overlap on that core is exactly the E0 mass there,

    |C1 s D|/Z_E ~ [2 C1^2/A0] b^(1/6).

This proves an Omega(b^(1/6)) overlap for that budget scale; the displayed coefficient is strictly positive.

## 7. Actual exact exponent check and review boundary

A bounded Fraction-only cell observed

```text
b=2^-72: xi= 1/64 component_radius= 1/4194304 weight= 1/1024
weight*radius/(s*xi)= 1/4 main_term_over_b^(1/6)= 16
component_core_radius_over_Euclidean_scale= 1/16
```

These are selected exact scaling diagnostics, not verification of the full all-law inequality. The proof uses only standard RN/differentiation, Tonelli, convexity, radial layer integrals and the geometric shell event inequality. Request disjoint review of the peak-floor deficit bound (5), sequence-dependent radius, normalization/core density comparison and budget constants. No formal/kernel/human/configured-family, source priority, novelty or parent acceptance is claimed. Historical held outcomes are nonpremises.
