# Exact finite-epsilon staircase/Laplace TV, KL and Rényi formulas

**AUTHOR CANDIDATE — WRITTEN with explicitly nonrigorous Decimal diagnostics; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:02:37 PDT 2026`.

## 1. Law definitions and exact Rényi affinity

Fix any epsilon>0 and gamma in [0,1]. Let P_gamma be the actual full-D-private centered diamond staircase with `p(x)=b^n/Z`, `n=max(0,ceil(||x||_1-gamma))`, `b=e^(-epsilon)`, and let Q be the actual product-Laplace law with `q=(epsilon^2/4)e^(-epsilon||x||_1)`. Put

    m=b/(1-b), v=m(1+m),
    D=gamma^2+2m gamma+m+2m^2, Z=2D, A=2/(epsilon^2 D).

For EVERY real s define the finite positive affinity

    I_s=integral p^s q^(1-s) dx.                                         (1)

The source-independent exact formula is

    I_s = A^s epsilon^2 { integral_0^gamma r e^[-(1-s)epsilon r]dr
           + integral_(gamma-1)^gamma (v+m u)e^[-(1-s)epsilon u]du }.    (2)

Both one-dimensional integrals are elementary, with the usual continuous interpretation at s=1. Formula (2) has no infinite sum. In particular `I_0=I_1=1`, and for EVERY alpha>0, alpha!=1,

    D_alpha(P_gamma||Q)=log(I_alpha)/(alpha-1),
    D_alpha(Q||P_gamma)=log(I_(1-alpha))/(alpha-1).                      (3)

The ratio p/q is bounded above and below by positive finite constants, so (1) is finite even for negative s. Alpha=1 is obtained continuously or by the separate exact KL formulas below. This is a finite-epsilon result for actual trial laws; no source-optimality claim is made.

## 2. Derivation of (2)

Under Q the diamond radius r has density `epsilon^2 r e^(-epsilon r)`. On the central part 0<=r<=gamma, n=0. On shell n>=1 write r=n+u, u in [gamma-1,gamma]. Then the exponent in `q (p/q)^s` is

    -(1-s)epsilon r-s epsilon n = -epsilon n-(1-s)epsilon u.

Sum `sum_(n>=1)b^n=m` and `sum_(n>=1)n b^n=v`, and use the exact density ratio `p/q=A e^(epsilon(r-n))`. This yields (2), including gamma=0 and gamma=1 up to null shell boundaries. Its finite integrals can be evaluated by exponentials and rational operations; numerical implementations near s=1 must avoid cancellation.

## 3. Both KL directions in closed form

Define the exact staircase first-norm moment

    M3=gamma^3+3m gamma^2+3(m+2m^2)gamma+m+6m^2+6m^3,
    L_gamma=(2/3)M3/D.

Differentiating the normalization Z at fixed gamma gives `E_P n=v(2gamma+1+4m)/D`. Under Q, `P_Q(r>t)=e^(-epsilon t)(1+epsilon t)` and the tail-sum formula gives

    E_Q n=e^(-epsilon gamma)[1+epsilon gamma+epsilon m]/(1-b).

Consequently

    D_KL(P_gamma||Q)=log A+epsilon[L_gamma-v(2gamma+1+4m)/D],            (4)
    D_KL(Q||P_gamma)=-log A-2
       +epsilon e^(-epsilon gamma)[1+epsilon gamma+epsilon m]/(1-b).      (5)

Although the individual terms in (4)–(5) can be numerically cancellation-prone, the exact expressions are nonnegative KL divergences.

## 4. Exact total-variation integral

Let `u0=-log(A)/epsilon`. The ratio in §2 has strict essential extrema on either side of 1 (it is not constant and integrates to 1), so `gamma-1<u0<gamma`. The positive density difference is exactly the region `r-n>u0`. Put `r0=max(0,u0)`. Splitting the central part and summing the geometric shells gives

    TV(P_gamma,Q)=epsilon^2 {
       integral_(r0)^gamma r[A-e^(-epsilon r)]dr
       + integral_(u0)^gamma (v+m u)[A-e^(-epsilon u)]du }.              (6)

The central integral is interpreted as zero when gamma=0; u0<gamma ensures no other empty-interval case. Both displayed integrands are nonnegative over their ranges. They are elementary exponential integrals. This exact formula neither claims any law is globally optimal nor replaces the original full-D problem with a radial model.

## 5. Bounded diagnostic and scope

A Python Decimal cell at precision 60, epsilon=0.5 and gamma=0.7, evaluated (2). It returned I_0=I_1=1 to the displayed 60 digits, I_2≈1.02074081704780484 and I_-1≈1.02103901800569616, giving D2(P||Q)≈0.02052865489768367 and D2(Q||P)≈0.02082075393293912. These are non-interval point diagnostics for a selected actual trial, not proof or optimizer verification.

Equations (1)–(6) are WRITTEN using only the defined actual laws and geometric sums. No named research theorem or prior candidate is imported, and no source equivalence, formal/independent review, novelty, exact original optimizer or parent adoption is claimed. Suggested review: shell indices at gamma endpoints, affinity exponents for reverse order, threshold u0, and central-piece handling.
