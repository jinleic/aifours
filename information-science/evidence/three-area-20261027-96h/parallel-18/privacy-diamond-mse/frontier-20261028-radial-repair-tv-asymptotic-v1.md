# A sharper actual private radial approximation to 1D-staircase products

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:12:59 PDT 2026`.

## 1. Sharp leading TV for a whole explicit family

Fix epsilon>0 and any gamma,eta in [0,1]. Let Q_gamma be the product of the two symmetric 1D epsilon-private staircases of offset gamma, and let P_eta be the ACTUAL 2D full-D-private diamond staircase of offset eta. Define

    c={2gamma-eta} in [0,1),   t=min(c,1-c),
    G(c)=1/2-(3/2)t^2+t^3.                                               (1)

The source-independent written claim is the UNIFORM asymptotic

    TV(Q_gamma,P_eta)=(epsilon/2)G(c)+O(epsilon^2),                      (2)

where the error is uniform even if gamma and eta vary with epsilon. `G` has a unique minimum 1/4 at c=1/2 modulo 1. Thus choosing any eta in [0,1] with

    eta = 2gamma-1/2  (mod 1)                                             (3)

gives an actual full-D private law with

    TV(Q_gamma,P_eta)=epsilon/8+O(epsilon^2).                             (4)

This improves the explicit Laplace upper `epsilon/6+O(epsilon^2)` in the unreviewed 7d15 candidate. The optimum of G is only within this radial staircase trial family; no claim that epsilon/8 is the true nearest-private-law coefficient is made.

If gamma->1/2, the unreviewed exact privacy-defect candidate `frontier-20261028-product-staircase-exact-delta-v1.md`, SHA-256 `1f6b748298e994bed0392b1e9cfc15d4cd80f02920942b464d7ecbc1c39265eb`, supplies the separate lower bound. Combining with the ACTUAL P_eta construction yields

    (epsilon/32)[1+o(1)] <= inf_(mu full-D epsilon-private)TV(mu,Q_gamma)
                            <=epsilon/8+O(epsilon^2).                     (5)

Only the lower side imports 1f6b; (1)–(4) require no named research theorem.

## 2. Common feasible reference and phase identity

Let Lambda_epsilon be product Laplace `(epsilon^2/4)e^(-epsilon||x||_1)`. On noncentral shells, let

    theta_i={|x_i|-gamma}, i=1,2,
    theta_R={||x||_1-eta}={theta_1+theta_2+c}.

The 1D and 2D exact normalizers give, uniformly in the offsets,

    dQ_gamma/dLambda_epsilon
       =1+epsilon[(theta_1-1/2)+(theta_2-1/2)]+O(epsilon^2),
    dP_eta/dLambda_epsilon
       =1+epsilon(theta_R-1/2)+O(epsilon^2).                             (6)

The regions where either coordinate or the radial staircase is central have Lambda_epsilon mass O(epsilon), and the relevant ratios there differ from 1 by O(epsilon), so their total L1 contribution is O(epsilon^2).

The absolute values under Lambda_epsilon are independent Exp(epsilon) variables. Their fractional phases are independently uniform on [0,1] up to O(epsilon) in bounded-test expectation: periodize the exponential density over unit intervals and bound the error by its total variation `integral|w'|=epsilon`; omitted central mass is O(epsilon). For S=theta_1+theta_2, (6) gives the leading difference

    (dQ_gamma-dP_eta)/(epsilon dLambda_epsilon)
       = floor(S+c)-c-1/2+O(epsilon).                                     (7)

S has triangular density `s` on [0,1] and `2-s` on [1,2].

## 3. Exact phase integral and optimization

For 0<=c<=1, the three values of `floor(S+c)-c-1/2` occur with probabilities

    P0=(1-c)^2/2,   P1=1-P0-c^2/2,   P2=c^2/2.

For 0<=c<=1/2, direct integration yields

    E|floor(S+c)-c-1/2|=1/2-(3/2)c^2+c^3.

For 1/2<=c<1 the expression is symmetric under c->1-c. This proves (1)–(2). The derivative on [0,1/2] is `3c(c-1)<=0`, strictly negative away from c=0, so the unique minimizer modulo 1 is c=1/2 with value 1/4. Equation (3) realizes it, proving (4). P_eta is genuinely full-D private by the unit-change-of-shell-index inequality.

## 4. Status

No numerical, formal, independent review, novelty, exact nearest-private law or parent acceptance is claimed. The uniform phase calculation and actual upper construction are written from explicit densities; the lower bound explicitly imports the unreviewed 1f6b candidate. Review should check offset modular arithmetic, central-shell errors, phase uniformity and the triangular expectation.
