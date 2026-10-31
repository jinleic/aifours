# Universal separation of first-norm and squared-cost staircase selectors

**AUTHOR CANDIDATE — WRITTEN with exact polynomial checks; NOT independently reviewed or parent-adopted.** Actual native pre-write clock: `Wed Oct 28 17:54:28 PDT 2026`.

## 1. Exact all-variable statement

For EVERY finite epsilon>0 let `b=e^(-epsilon)`, `m=b/(1-b)`, `D={h:||h||_1<=1}` and F_epsilon the ALL-Borel probability laws obeying the additive privacy inequality for EVERY Borel event and EVERY shift in the FULL CLOSED D. Write `L(mu)=E||X||_1`, `W(mu)=E||X||_1^2` and `J(mu)=E||X||_2^2`.

There are unique centered-staircase scalar offsets `gamma_1,gamma_2 in (0,1)` minimizing L and W, respectively, and

    gamma_1 < gamma_2   for EVERY finite epsilon>0.                       (1)

At the named matching-norm per-cost import, the actual centered law Q_gamma1 is a GLOBAL all-Borel L minimizer and Q_gamma2 is a GLOBAL all-Borel W minimizer. Both are fully private laws and

    W(Q_gamma2) < W(Q_gamma1),
    J(Q_gamma2) < J(Q_gamma1),
    L(Q_gamma1) < L(Q_gamma2).                                           (2)

Thus for EVERY epsilon, a genuinely globally mean-l1-optimal staircase is strictly suboptimal for the registered all-law squared-Euclidean objective, with an actual competing law, and also for all-law squared-l1. It is immaterial whether some other nonradial mean minimizer exists; no all-law uniqueness of mean minimizers is assumed. No assertion is made that Q_gamma2 is always the all-law Euclidean optimizer.

A constructive, parameter-specific positive gap and root-separation bound are given in §5. This generalizes the previous exact `epsilon=log 2` counterexample; it is NOT a refutation of the PMLR theorem, which actually states FIRST-norm optimality. No worldwide source non-equivalence, priority or novelty claim follows.

## 2. Scope and named inputs

The publisher source `kulesza-suresh-wang-pmlr258-2025.pdf`, SHA `4e67a46d80e705df6b23a92e8fb88599a8b14c874af3f7b434a0ed217ca71df3`, printed page 3 Definition 5 / Theorem 2 concerns FIRST-power E||Z||_K and a gamma-staircase. The exact source-to-squared-cost counterexample is a new argument, not a theorem attributed to that paper; its NR-K17/NR-K10 proof qualifications persist.

The one model-specific research import is the prior parent-WRITTEN_SUPPORTED alternative matching-norm per-cost theorem `institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, §I: for each nondecreasing radial cost, an actual centered staircase attains the all-Borel, all-event, full-closed-ball infimum. It applies separately to r and r^2. The result below supplies the scalar selector/equality separation independently; it does NOT import LAW642, v241, v253 or my unreviewed all-law uniqueness candidate. The named per-cost theorem is a supplied ALTERNATIVE proof, not a claimed repair of printed NR-A/NR-D.

## 3. Exact formulas and unique first-moment offset

For 0<=gamma<=1, let Q_gamma have density `Z_gamma^(-1)b^(n_gamma(x))`, where `n_gamma(x)=min{k>=0:||x||_1<=gamma+k}`. The full closed-D triangle inequality gives `|n_gamma(x+h)-n_gamma(x)|<=1` for all x,h, so every Q_gamma is a genuine original feasible law. Q_0=Q_1 a.e. as normalized laws.

Write

    D(g)=g^2+2mg+m+2m^2,
    M3(g)=g^3+3mg^2+3(m+2m^2)g+m+6m^2+6m^3,
    M4(g)=g^4+4mg^3+6(m+2m^2)g^2
           +4(m+6m^2+6m^3)g+m+14m^2+36m^3+24m^4.

Exact diamond layer integration gives

    L(Q_g)=(2/3) M3(g)/D(g),
    W(Q_g)=M4(g)/(2D(g)),
    J(Q_g)=(2/3)W(Q_g).                                                  (3)

The last equality is ONLY for these centered diamond-radial densities. Differentiation yields

    L'(g)=(2/3) Q_m(g)/D(g)^2,
    Q_m(g)=g^4+4mg^3+6m^2g^2-2m(1+3m)g+m^2.                           (4)

Let `v=m(1+m)>0`, `t=1+2m`, `x=g+m`. Direct expansion gives

    Q_m(g)=x^4-2v t x+3v^2,       t^2=4v+1.                              (5)

The unique `g0=sqrt(v)-m` lies in (0,1). At g0,

    Q_m(g0)=2v^(3/2)(2sqrt(v)-t)<0.

Also `Q_m(0)=m^2>0`, `Q_m(1)=(1+m)^2>0`. Its descending nonzero coefficient signs have exactly two changes. By Descartes and the intermediate value theorem it has exactly two simple positive roots, one in (0,g0), one in (g0,1). Because Q_0=Q_1 as laws, the latter is the unique global scalar minimum. Define it as gamma_1. In particular

    x_1=gamma_1+m > sqrt(v),     z=x_1^2/v > 1.                         (6)

The named per-cost theorem makes Q_gamma1 an actual GLOBAL L minimizer.

## 4. The squared-cost derivative is strictly negative at the mean selector

Differentiating W in (3),

    W'(g)=P_m(g)/D(g)^2,
    P_m(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
              -m(1+2m)(1+6m)g + m^2(1+2m).                            (7)

Define `R_m(g)=2g^3+6mg^2-(1+6m)g+m`. The exact all-variable identities are

    P_m(g)=(g+m) Q_m(g)+v R_m(g),
    R_m(g)=2x^3-(1+6v)x+2v t.                                            (8)

At the mean stationary root, (5) gives `2v t=(x_1^4+3v^2)/x_1`. Hence

    R_m(gamma_1)=[3(x_1^2-v)^2-x_1^2]/x_1.                            (9)

To prove its sign without numerical root comparison, substitute z from (6) into (5) and `t^2=4v+1`:

    1/v = [(z^2+3)^2-16z]/(4z),
    1/v - 3(z-1)^2/z = (z-1)^3(z+3)/(4z) > 0.

Equivalently,

    x_1^2 - 3(x_1^2-v)^2 = v^2 (z-1)^3(z+3)/4 >0,
    P_m(gamma_1) = -v^3 (z-1)^3(z+3)/(4x_1) <0.                       (10)

This is an exact STRICT identity for EVERY m>0, not an inference from selected examples or a hidden assumption about root locations.

P_m's descending coefficient signs have exactly two changes after a possible zero is omitted. Its endpoints are `P_m(0)=m^2(1+2m)>0` and `P_m(1)=(1+m)^2(1+2m)>0`. With (10), IVT gives one positive root before gamma_1 and one after; Descartes shows they are the only positive roots and both are simple. Because the endpoint Q_0/Q_1 laws coincide, the second root is the unique global scalar W minimum gamma_2 and satisfies (1).

The named per-cost theorem makes Q_gamma2 a GLOBAL W minimizer; `W'` is strictly negative throughout `(gamma_1,gamma_2)`, and `L'` is strictly positive there. This proves both strict opposite-cost inequalities in (2). The actual feasible competitor Q_gamma2 also strictly improves J by (3), so the mean-optimal law cannot attain the all-law Euclidean optimum even when the latter is nonradial or not explicitly characterized here.

## 5. Explicit positive gap and selector distance

Let `p0=-P_m(gamma_1)>0`, explicitly given by (10), and define the elementary polynomial bound

    B(m)=5+31m+44m^2+36m^3.

For every g in [0,1], the derivative in (7) satisfies `|P_m'(g)|<=B(m)` by the triangle inequality. Let

    h=min{(1-gamma_1)/2, p0/(2B(m))} >0,
    Dmax=D(1)=(1+m)(1+2m).

Then `P_m(g)<=-p0/2` on `[gamma_1,gamma_1+h]`, and `D(g)<=Dmax` there. Integrating the exact derivative and using (3), the FULL original Euclidean optimum V obeys

    J(Q_gamma1)-V >= J(Q_gamma1)-J(Q_(gamma_1+h))
                    >= p0 h/[3 Dmax^2] >0.                              (11)

Likewise `W(Q_gamma1)-Wmin>=p0 h/[2Dmax^2]>0`. This is a positive fixed-epsilon bound expressed entirely by the uniquely specified quartic root and elementary m; it is not claimed uniform over epsilon. By the mean value theorem between the ordered roots,

    gamma_2-gamma_1 >= p0/B(m) >0.                                      (12)

No assumption of uniqueness of any nonradial global minimizer is needed for (11)–(12).

## 6. Actual exact algebra and sample diagnostics

A bounded local Python Eval cell used exact integer-polynomial dictionaries for the three identities in (8)/(5) and `fractions.Fraction` for the factorization. Actual output:

```text
P=(g+m)Q+vR: True
Q=x^4−2v(1+2m)x+3v²: True
R=2x³−(1+6v)x+2v(1+2m): True
(z−1)^3(z+3) coefficients ascending: [Fraction(-3, 1), Fraction(8, 1), Fraction(-6, 1), Fraction(0, 1), Fraction(1, 1)]
equals z^4−6z²+8z−3: True
```

The first cell successfully checked the three bivariate identities but the subsequent factor step hit `TypeError: 'tuple' object is not callable` because an unrelated persistent-kernel name shadowed a helper. I retried ONLY that failed factor step using explicit coefficient lists, producing the final two lines above. Nothing about the successful first checks was rerun or silently treated as a failed output.

As a separate bounded check, exact Fraction bisection isolated the two scalar minima at five rational m values; all produced `mean_upper<square_lower=True`:

```text
m= 1/10000 mean_upper<square_lower= True gap_bracket_lower= 308088983/6710886400
m= 1/10 mean_upper<square_lower= True gap_bracket_lower= 2173723299/33554432000
m= 1 mean_upper<square_lower= True gap_bracket_lower= 70227011/3355443200
m= 10 mean_upper<square_lower= True gap_bracket_lower= 90389497/33554432000
m= 1000 mean_upper<square_lower= True gap_bracket_lower= 46589/1677721600
```

These finite samples do NOT prove the universal statement; (5)–(10) provide the all-variable written proof. The earlier selected epsilon=log 2 candidate `frontier-20261028-pmlr-mean-selector-counterexample-v1.md`, SHA `f95169d5deb53d3b0c6ea4dbbbfb58e872b387297740ff5e81ac222e868a2167`, independently supplies explicit rational comparator/gap bounds and remains UNREVIEWED.

## 7. Assurance and nonclaims

This is an unreviewed written successor at the explicitly named alternative per-cost input, with exact algebra checks. It does not repair an as-printed PMLR/MDA proof or claim the sources stated squared-Euclidean optimality. It does not prove the complete original Euclidean optimum, original law uniqueness, worldwide novelty, or SOURCE-MATCH-U1 beyond the specific source-selector non-transfer. Request disjoint review of the scalar moment/derivative formulas, quartic root selection, (8)–(10), full-event caller and gap bounds before any parent adoption. No human, independent model family, formal/kernel or full-proof executable acceptance is asserted.
