# Uniform low-privacy asymptotics across all Euclidean/l1 squared weights

**AUTHOR CANDIDATE — WRITTEN with exact rational coefficient checks; NOT independently reviewed or parent-adopted.** Native pre-write clock `Wed Oct 28 18:50:50 PDT 2026`.

## 1. Original full-law class, with an arbitrary changing weight

Let b=e^(-epsilon) in (0,1), D the FULL CLOSED unit l1 diamond, and F_b ALL Borel laws obeying the epsilon privacy inequality for EVERY Borel event and EVERY h in D. For `theta in [0,1]` define

    c_theta(x)=(1-theta)||x||_2^2+theta||x||_1^2,
    H_theta(b)=inf_(mu in F_b) E_mu c_theta(X).

Every weight is nonnegative, including BOTH endpoints. For the earlier mixed cost `J+lambda W`, put `theta=lambda/(1+lambda)`, so `H_theta=H_lambda/(1+lambda)`; theta=1 covers the pure squared-l1 endpoint without an infinite coefficient.

Let

    A_theta=|{c_theta<=1}|,
    C_D(theta)=integral_D c_theta(x)dx=(2+theta)/3,
    C_theta=sqrt[2 C_D(theta)/A_theta].                                  (1)

**Uniform all-law value candidate:** as b->0,

    H_theta(b)=C_theta sqrt(b)+O(b^(3/4))   UNIFORMLY theta in [0,1].   (2)

In particular this remains true if theta=theta(b) changes arbitrarily as b decreases to 0; lambda(b) may tend to infinity at ANY rate. The O constant is independent of theta.

**All-near-optimal moving-shape candidate:** if ANY theta_n in [0,1], b_n->0 and actual feasible laws mu_n satisfy

    E_mu_n c_(theta_n)(X) <= C_(theta_n)sqrt(b_n)+o(sqrt(b_n)),          (3)

then their scaled laws satisfy

    TV(Law(b_n^(-1/4)X_n), Uniform(B_(theta_n))) ->0,
    B_theta={z:c_theta(z)<=C_theta}.                                     (4)

No convergence of theta_n, optimizer existence, density ansatz, central symmetry of mu_n or fixed-weight shortcut is assumed. If theta_n->theta0, the moving uniform laws themselves converge in TV to Uniform(B_theta0), including the squared-l1 endpoint theta0=1.

This is a joint source/target-interface result: theta=0 is original squared Euclidean, theta=1 is squared l1, intermediate theta are true mixed losses, and FIRST-power l1 is a different objective. It is not a claim of a finite-epsilon scalarized selector/phase threshold, an external publication's theorem, priority, novelty, or nonadditive privacy.

## 2. Named dependency and explicit coefficient

The ONLY prior research artifact used is my still-UNREVIEWED direct proof `frontier-20261028-peak-floor-low-privacy-universal-v1.md`, SHA `d44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43`, especially its pointwise peak-floor and exact capped-density bathtub identities. This note explicitly checks the uniform-in-theta steps rather than assuming its fixed-lambda O constants are uniform. The cited predecessor itself has NO LAW642, v241, MDA, PMLR, f68 or other research import; its status is not upgraded here.

In each quadrant `c_theta(r cos phi,r sin phi)=r^2[1+theta sin(2phi)]`. Hence for 0<=theta<1,

    A_theta = integral_0^pi du/[1+theta sin u]
            = 2 arccos(theta)/sqrt(1-theta^2),                          (5)

with continuous endpoint A_1=2. Direct geometry yields A_0=pi and A_1=|D|=2. Since `||x||_2^2<=c_theta(x)<=2||x||_2^2`, uniformly

    pi/2 <= A_theta <= pi,       2/3 <= C_D(theta) <=1.                 (6)

Thus all A_theta, C_theta and `y_theta=1/(A_theta C_theta)` are uniformly bounded above and away from 0. At theta=1/2, `A=4pi/(3sqrt(3))` and `C^2=5sqrt(3)/(4pi)`; at theta=1, C=1.

## 3. All-bounds-valid uniform peak-floor estimate

The cited predecessor's all-law derivation applies separately at every theta: with actual bounded pointwise density representative of essential supremum M, a near-peak point forces floor bM on one translated D, even convexity minimizes its integrated cost at the origin, and the remaining capped-density mass obeys the homogeneous-cost bathtub bound. It gives, for EVERY theta and b,

    H_theta(b) >= sqrt[2b C_D(theta)/A_theta+4b^2/A_theta^2]
                      -2b/A_theta.                                       (7)

By (6) this is `>=C_theta sqrt(b)-C0 b` with one finite C0 for all theta.

For the upper law, put s=b^(1/4), `R_theta=(2C_D(theta)/A_theta)^(1/4)` and take the actual private shell law with core `S=s R_theta {c_theta<=1}`. All these bodies lie in a common Euclidean ball of radius O(s), contain 0, and have top area `A_theta R_theta^2 s^2` and top c_theta moment `(A_theta/2)R_theta^4 s^4=C_D(theta)b`.

Because all c_theta satisfy `c_theta<=2||x||_2^2` and are homogeneous of degree 2, uniform containment between D and `(1+C s)D` gives, for all theta at once,

    |S+D|=2+O(s),     integral_(S+D)c_theta=C_D(theta)+O(s),
    sum_(k>=2)b^k [area and cost moments of S+kD] =O(b^2).

The positive geometric-layer ratio yields `H_theta<=C_theta sqrt(b)+C1 b^(3/4)` with C1 independent of theta. Combining with (7) proves (2), including an arbitrary moving theta(b). This is not inferred from pointwise convergence followed by an unjustified exchange of limits.

## 4. Uniform all-near-optimal moving-shape stability

For a sequence satisfying (3), let s_n=b_n^(1/4). Apply the cited peak-floor decomposition to the ACTUAL density p_n at theta_n, with eta=s_n:

    M_n=esssup p_n,    y_n=s_n^2 M_n,
    ell_n=b_n(1-s_n)M_n,
    g_n=p_n-ell_n 1_(x_n+D),     h_n=1-2ell_n.

The floor cost and (6) bound y_n uniformly above; the positive residual mass/bathtub term then bounds y_n uniformly away from 0, and ell_n=O(s_n^2). Define

    f_theta(y)=y C_D(theta)+1/[2A_theta y],
    y_theta=1/sqrt(2A_theta C_D(theta)).

Its unique minimum is C_theta. On the common compact y interval, `f_theta''(y)=1/(A_theta y^3)` has a uniform positive lower bound. Since (3), the uniform lower estimate and the nonnegative bathtub deficit force `f_(theta_n)(y_n)-C_(theta_n)->0`, they imply

    y_n-y_(theta_n)->0,       Delta_n->0.                                (8)

No convergence of theta_n is needed. The even-convex floor minimum is sufficient here; unlike the fixed-weight tail-profile theorem, we do NOT need to assert a rate or even a separate limit for the chosen peak x_n.

Let `g_n^#(z)=s_n^2 g_n(s_n z)`, `T_n=h_n/[A_(theta_n)y_n]`, and `g_n^0=y_n 1_{c_(theta_n)<=T_n}`. Their masses agree. The positive bathtub deficit gives, for any d>0,

    ||g_n^#-g_n^0||_1 <= Delta_n/d+2 A_(theta_n)y_n d.

The band-area formula `|{c_theta<=t}|=A_theta t` is exact, so the constants are uniform. Take n->infinity and then d->0. Equation (8) makes `T_n-C_(theta_n)->0`; the same sublevel-area identity gives

    ||g_n^0 - y_(theta_n) 1_{c_(theta_n)<=C_(theta_n)}||_1 ->0.

The scaled floor has total mass `2ell_n=O(s_n^2)->0`. This proves the MOVING-TV conclusion (4) uniformly for arbitrary theta_n, with no fixed-parameter diagonalization or implicit optimizer uniqueness.

## 5. Endpoint and non-W2 boundary

If theta_n->theta0, (5) and continuity of c_theta/C_theta imply the moving uniform densities converge in L1 to that for theta0: pointwise convergence holds off the null cost boundary and all supports lie in a common bounded disk. Hence the scaled law has the stated fixed limit.

For theta0=1, `c_1=||x||_1^2`, A_1=2 and C_1=1, so the limiting law is uniform on the unit diamond. This includes ANY sequence of mixed weights lambda_n->infinity via theta_n=lambda_n/(1+lambda_n), regardless of its rate relative to epsilon. Theta0=0 gives the original Euclidean disk of radius `(4/(3pi))^(1/4)`.

When theta_n->theta0, the scaled expected costs tend to C_theta0 by (2)–(3), but the uniform limiting law's cost is C_theta0/2. Consequently Euclidean W2 convergence to that limit is impossible: W2 convergence would imply convergence of the continuous theta0-cost (bounded by a constant multiple of |x|^2), while `|c_theta_n-c_theta0|<=2|theta_n-theta0||x|^2` and the scaled second moments stay bounded. This is an actual TV-versus-moment distinction, not a hidden claim of an exact finite-parameter support.

## 6. Actual exact arithmetic and limits

A bounded local `fractions.Fraction` check observed

```text
theta= 0 C_D= 2/3 2*C_D= 4/3
theta= 1/2 C_D= 5/6 2*C_D= 5/3
theta= 1 C_D= 1 2*C_D= 2
theta=1/2: A=(4/3)*pi/sqrt3; C_theta^2=(5/4)*sqrt3/pi
pure squared-l1 endpoint: A=2,C_D=1,C=1
```

The endpoint/half-weight trigonometric identities and uniform layer/deficit estimates are written proofs; the printed formula labels are not extra machine certification. This candidate and its named predecessor remain UNREVIEWED. Request disjoint review especially of the uniformly bounded peak/bathtub parameters, moving sublevel-band L1 estimate and rapidly changing-weight interpretation. No source priority, novelty, formal/kernel/human/configured-family or parent acceptance is claimed. Historical held results are not premises.
