# A source-independent all-law low-privacy theorem via peak floors

**AUTHOR CANDIDATE — WRITTEN with exact geometric checks and a bounded Decimal diagnostic; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:45:49 PDT 2026`.

## 1. Exact original class and what is independently proved

For EVERY finite epsilon>0 let b=e^(-epsilon), D={h:||h||_1<=1} CLOSED, and F_epsilon contain ALL Borel laws satisfying

    mu(A)<=b^(-1)mu(A+h) for EVERY Borel A and EVERY h in D.

Fix ANY finite `lambda>=0` and the genuine full-law mixed cost

    c_lambda(x)=||x||_2^2+lambda||x||_1^2,
    H_lambda(b)=inf_(mu in F_epsilon) E_mu c_lambda(X).                    (1)

Define the compact convex unit-cost body and two explicit geometric constants

    K_lambda={x:c_lambda(x)<=1},  A_lambda=|K_lambda|,
    C_D=integral_D c_lambda(x)dx = 2/3+lambda.

**Nonasymptotic all-law lower bound:** for EVERY 0<b<1 and every feasible mu,

    E_mu c_lambda(X)
      >= sqrt[2b C_D/A_lambda + 4b^2/A_lambda^2] - 2b/A_lambda.          (2)

**Exact low-privacy leading value:** as b->0, for every fixed lambda>=0,

    H_lambda(b)=C_lambda sqrt(b)+O_lambda(b^(3/4)),
    C_lambda=sqrt[2(2/3+lambda)/A_lambda].                               (3)

An explicitly constructed full-D-private shell law attains the upper side through O_lambda(b^(3/4)). For lambda=0 this is the ORIGINAL all-law Euclidean value and `C_0=2/sqrt(3pi)`. Unlike my earlier disk-limit candidate, (2)–(3) require NO LAW642, v241, MDA, PMLR, f68 or other research-theorem import.

**All-near-optimal limiting laws:** for ANY sequence b_n->0 and ANY actual feasible laws mu_n with

    E_mu_n c_lambda(X) <= C_lambda sqrt(b_n)+o(sqrt(b_n)),               (4)

the rescaled laws `Law(b_n^(-1/4) X_n)` converge in TOTAL VARIATION to the UNIFORM law on

    B_lambda={z:c_lambda(z)<=C_lambda}.                                  (5)

No optimizer existence, uniqueness, assumed density/symmetry, geometric-shell ansatz or input source theorem is needed. In particular lambda=0 yields the Euclidean disk of radius `(4/(3pi))^(1/4)` for EVERY first-order-near-optimal original law, even if the optimizer were not known. A moment-topology warning: the limiting uniform law has mean cost C_lambda/2 while the rescaled laws have mean cost ->C_lambda. Thus their TV convergence is NOT W2 convergence; a vanishing privacy tail carries the missing half of the scaled cost.

This is an AUTHOR-WRITTEN derivation, not an independent-review, formal/kernel, novelty or publication claim. Fixed lambda is essential: no asymptotic uniform in lambda->infinity is asserted.

## 2. Explicit lambda geometry

The l1 diamond has area 2, `integral_D ||x||_2^2=2/3` and `integral_D ||x||_1^2=1`, so C_D=2/3+lambda. Polar integration in the first quadrant gives

    A_lambda = 2 integral_0^(pi/2) dtheta/[1+lambda(1+sin(2theta))]
             = [2/sqrt(1+2lambda)]
                [pi/2-arctan(lambda/sqrt(1+2lambda))].                  (6)

The formula is valid at lambda=0 by direct substitution; A_0=pi. For lambda=1, `A_1=2pi/(3sqrt(3))` and `C_1=sqrt(5sqrt(3)/pi)`. The cost body is a genuine compact centrally symmetric convex set for every fixed finite lambda>=0.

## 3. Pointwise DP and the peak-floor decomposition

Let mu be ANY original feasible law. Integrating its event inequality over D and using Tonelli gives a density p and the finite cap `p<=1/(2b)` a.e. Let M=esssup p>0. Replacing p by shrinking-ball limsups gives a density representative of the SAME law satisfying p<=M at EVERY point and

    p(y)>=b p(x) whenever ||x-y||_1<=1, for ALL x,y.                     (7)

For any eta in (0,1), choose an actual x0 with `p(x0)>=(1-eta)M`. Equation (7) supplies the pointwise floor

    p(x)>=ell  on x0+D,       ell=b(1-eta)M.

Set `g=p-ell 1_(x0+D)`. Then g>=0, g<=M a.e. and its EXACT mass is `h=1-2ell>=0`. For the even convex cost c_lambda,

    integral_(x0+D)c_lambda(x)dx >= C_D.                                (8)

Indeed its integral over x0+D is an even convex function of x0. In fact the Euclidean part gives the stronger `>=C_D+2|x0|_2^2`, since the remaining squared-l1 part is even/convex and is minimized at zero.

## 4. Exact bathtub lower bound for ALL laws

Homogeneity gives `|{c_lambda<=t}|=A_lambda t` and `integral_(c_lambda<=t)c_lambda dx=A_lambda t^2/2`. Among all 0<=g<=M with integral h, the strict bathtub optimum is M on `{c_lambda<=h/(A_lambda M)}` and zero outside. The proof subtracts the common threshold times equal masses; both inside/outside differences are nonnegative. Therefore

    integral c_lambda g >= h^2/(2A_lambda M).

Adding the actual floor contribution and (8), then allowing eta->0, yields for x=bM>0

    E_mu c_lambda >= C_D x + b(1-2x)^2/(2A_lambda x).

The floor mass itself shows x<=1/2. Expanding and applying AM–GM for any x>0,

    C_D x + b(1-2x)^2/(2A_lambda x)
      = (C_D+2b/A_lambda)x + b/(2A_lambda x) - 2b/A_lambda
      >= sqrt[2b C_D/A_lambda+4b^2/A_lambda^2]-2b/A_lambda.

This proves (2) for EVERY original law. The peak is only approximated, not assumed to be attained. No interchange of infimum/limit or one-core ansatz is used.

## 5. A genuinely private matching upper law

Set `s=b^(1/4)` and `R_lambda=(2C_D/A_lambda)^(1/4)`. Take the ACTUAL geometric core `S_trial=s R_lambda K_lambda` and density proportional to `b^(min{k:x in S_trial+kD})`. For every closed-D shift its shell index changes by at most 1, hence this is a genuine all-event epsilon-private probability law.

Its top area is `A_lambda R_lambda^2 s^2` and top cost moment is `(A_lambda/2)R_lambda^4 s^4=C_D b`. Because the core is in an O_lambda(s) Euclidean ball and contains 0,

    |S_trial+D|=2+O_lambda(s),
    integral_(S_trial+D)c_lambda=C_D+O_lambda(s),

and all k>=2 weighted layer contributions are O_lambda(b^2). The positive geometric-layer normalizer cancels its common factor (1-b). Therefore the ACTUAL upper cost is

    [2 C_D b+O_lambda(bs)]/[A_lambda R_lambda^2 s^2+2b+O_lambda(bs)]
      = C_lambda s^2+O_lambda(s^3).

Combined with (2), this proves (3). Lambda=0 supplies the original `2/sqrt(3pi)` leading constant without importing the previously supported original optimal law.

## 6. Every first-order-near-minimizer has the SAME scaled TV limit

Take ANY b_n->0 and ANY actual mu_n satisfying (4); put `s_n=b_n^(1/4)`. For each n choose a point x_n within factor `(1-s_n)` of its pointwise density supremum M_n, as in §3. Define

    y_n=s_n^2 M_n,   ell_n=b_n(1-s_n)M_n,
    g_n=p_n-ell_n 1_(x_n+D),   h_n=integral g_n=1-2ell_n.

The cost upper bound and the positive floor term first bound y_n above. Then ell_n=O(s_n^2), h_n->1; the bathtub lower term bounds y_n away from 0. The scaled cost identity gives

    E c_lambda(X_n)/s_n^2
       = (1-s_n)y_n F(x_n) + h_n^2/(2A_lambda y_n) + Delta_n,          (9)

where `F(x)=integral_(x+D)c_lambda`, `F(x)>=C_D+2|x|^2`, and the exact bathtub deficit Delta_n>=0 is defined in §7. The function `y C_D+1/(2A_lambda y)` has the unique minimum C_lambda at

    y0=1/sqrt(2A_lambda C_D)=1/(A_lambda C_lambda).

Since the left side tends to C_lambda by the matching lower and upper bounds, (9) forces

    y_n->y0,        x_n->0,        Delta_n->0.                            (10)

This conclusion concerns EVERY first-order-near-optimal law; the chosen x_n need not be an attained maximum and x_n/s_n is not claimed to converge.

## 7. Quantitative bathtub-deficit-to-TV argument

Let `p_n^#(z)=s_n^2 p_n(s_n z)` and `g_n^#(z)=s_n^2 g_n(s_n z)`. Then `0<=g_n^#<=y_n`, `integral g_n^#=h_n`, and define

    T_n=h_n/(A_lambda y_n),
    g_n^0(z)=y_n 1_{c_lambda(z)<=T_n}.

The two g densities have exactly the same mass. Homogeneity and (9) give the NONNEGATIVE exact deficit

    Delta_n=integral [c_lambda(z)-T_n][g_n^#(z)-g_n^0(z)] dz.             (11)

The two factors have the SAME sign inside/outside the sublevel set. For any fixed d>0, its contribution outside `|c_lambda-T_n|<d` is at least d times the L1 error there. The band itself has area at most `2 A_lambda d`, and the density difference is bounded by y_n. Hence

    ||g_n^#-g_n^0||_1 <= Delta_n/d + 2 A_lambda y_n d.                   (12)

By (10), take n->infinity and then d->0 to get L1 convergence. Also `T_n->1/(A_lambda y0)=C_lambda`, so `g_n^0` converges in L1 to `f_lambda=y0 1_{c_lambda<=C_lambda}`, the uniform density on B_lambda.

Finally the scaled floor component has total mass `2ell_n->0`; it does not affect TV. Thus `p_n^#->f_lambda` in L1, proving (5). This is a direct ALL-law stability proof of the low-privacy scaling limit, not a reconstruction of a specific assumed optimizer core.

## 8. The lost half-moment and the W2 warning

For the limit uniform density, homogeneity gives

    E_(f_lambda) c_lambda = C_lambda/2,

whereas (4) plus (2) gives `E c_lambda(b_n^(-1/4)X_n)->C_lambda`. Thus the rescaled laws converge in TV but not in W2: W2 convergence would force convergence of every continuous function bounded by a constant times `1+|z|^2`, including c_lambda. The nonzero missing half comes from rare privacy-enforced mass outside the shrinking core. No individual tail-location or finite-epsilon support claim is inferred.

## 9. Actual checks and assurance

Exact local Fraction arithmetic printed

```text
unit diamond exact: area= 2 integral_l1_squared= 1 integral_euclidean_squared= 2/3
lambda=1 target diamond integral= 5/3 lambda=0 leading coefficient squared=4/(3*pi)
```

A bounded 70-digit Decimal diagnostic for b=10^-8, lambda=0, using the exact disk-shell upper formula observed:

```text
lower/s²= 0.651406357004   trial/s²= 0.666504816229
predicted_limit= 0.651470015871   lower<=trial: True
lambda=1: A1= 1.209199576156   predicted_coefficient= 1.660314571733
```

These samples and Decimal numbers are diagnostics, not interval certificates or a replacement for §§3–7. The analytical proof imports only standard RN/differentiation, Tonelli, convexity, geometric layer cake and basic Euclidean change of variables; no LAW642, MDA, threshold, source-proof or previously held result is used. Request disjoint review of the all-shift peak representative, exact floor/cap optimization, uniform upper-layer errors, equality-deficit argument and all-near-optimal scaling before adoption. No formal/kernel/human/configured-family, source priority or novelty claim is made.
