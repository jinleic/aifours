# Joint Euclidean-square and first-norm budgets: sharp low-privacy inversion

**AUTHOR CANDIDATE — WRITTEN with explicitly nonrigorous numerical illustrations; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:27:49 PDT 2026`.

## 1. Setup, pinned import and claim

Condition on the unreviewed source-independent limiting moment-region candidate `frontier-20261028-full-critical-moment-region-v1.md`, SHA-256 `c8ce61fb2d40463f5fdf488cb2ed5aebe40bf59c8bd97dc18b7674caf94bf463`, including its actual private shell boundary constructions and all-law lower support inequalities. The present result does not make that candidate independently accepted.

Let J=E|X|_2^2, L=E||X||_1 for original all-event/full-closed-D-private noise laws, and let

    b_max(j,ell)=sup{ b=e^(-epsilon): a b-private law has J<=j, L<=ell }.

Equivalently `epsilon_min=-log b_max`, even if the supremum is not attained. Suppose `j->0`, `ell->0` and

    ell/sqrt(j) -> lambda in (0,infinity).                               (1)

For theta>=0 use the import's T_theta, with

    u_theta=T_theta-theta T'_theta,    v_theta=T'_theta,
    lambda_0=8/(3pi),    u_0=2/sqrt(3pi).                                (2)

The WRITTEN conclusion is

    b_max(j,ell)=z_*(lambda) j^2[1+o(1)],
    epsilon_min=2log(1/j)-log z_*(lambda)+o(1),                          (3)

where

    z_*(lambda)=3pi/4                                      if lambda>=lambda_0,
    z_*(lambda)=u_theta^(-2)                               if 0<lambda<lambda_0,
                 theta is the UNIQUE positive solution v_theta/sqrt(u_theta)=lambda. (4)

Both budgets bind to leading order in the second case; only the J budget binds strictly for lambda>lambda_0. At equality lambda=lambda_0 both are leading-order tight, yet the unconstrained J optimum already supplies the boundary. The limit is for fixed positive lambda, not an automatically uniform joint statement if lambda itself tends to 0 or infinity.

## 2. Why the crossing in (4) exists and is unique

The import establishes differentiability, strict concavity, T_theta'>0, and `T_theta~theta^(2/3)`, `T'_theta~(2/3)theta^(-1/3)` as theta->infinity. Consequently v_theta strictly decreases from v0 to 0. Also u_theta strictly increases: for theta2>theta1>=0, strict concavity gives

    u_2-u_1 = (T_2-T_1)-(theta2-theta1)v_2+theta1(v_1-v_2) >0.

Therefore `v_theta/sqrt(u_theta)` is continuous and strictly decreases from `v0/sqrt(u0)=8/(3pi)` to zero, proving the asserted unique crossing.

For a boundary law at theta and a proposed asymptotic scale `b=z j^2`, put s=b^(1/4). Its actual shell construction has `J~u_theta s^2` and `L~v_theta s`. The two budgets therefore require

    z <= u_theta^(-2),       z <= (lambda/v_theta)^4.                     (5)

The first right side decreases and the second increases with theta. Their maximum possible minimum occurs either at theta=0 when lambda>=lambda_0 or at the unique positive crossing. This yields (4).

## 3. All-law upper bound and actual-law lower bound

The original J peak-floor bound alone gives `b_max=O(j^2)` as j->0. The actual theta=0 shell, or any fixed positive theta shell, shows `b_max>=c_lambda j^2` for every fixed lambda>0, after choosing z strictly below the right side of (5). Thus arbitrary near-supremizing b values admit a convergent positive-ratio subsequence `b/j^2->z`.

On that subsequence, every feasible law has bounded scaled J and L, so pass to a further subsequence with finite limits u,v. The import's moment-region result says v>0 and every such point is dominated by some actual efficient frontier point `(u_theta,v_theta)` with theta>=0. The budget inequalities imply (5), so z is at most the maximum in (4). This establishes the upper limit even if no finite-b optimum exists.

Conversely, fix any z strictly less than z_*(lambda) and choose the corresponding frontier theta from (4). The actual full-D shell laws realize its u_theta,v_theta. At b=zj^2 both scaled budgets have positive slack; because ell/sqrt(j)->lambda, the actual laws satisfy both for all small j. Hence b_max>=zj^2, and letting z approach z_* proves (3). No unverified interchange of an optimizer and a limit is used.

## 4. Limiting cases and worked illustrative ratios

For lambda>=8/(3pi), (3) becomes the original squared-error budget inversion

    epsilon_min=2log(1/j)+log[4/(3pi)]+o(1).                             (6)

As a SEPARATE iterated limit lambda->0 AFTER deriving the fixed-lambda coefficient, the large-theta expansions give

    z_*(lambda) ~ (27/4)lambda^2,
    -log z_*(lambda) = log[4/(27lambda^2)]+o(1).                          (7)

Equation (7) is not a proof for arbitrary joint lambda(j)->0; in that regime the scaling may cross over to a different mean-dominated window.

A Python `math` Simpson/bisection diagnostic, not interval-certified, reported

```text
lambda=0.5  theta≈2.3440364222  u≈0.8526803456  v≈0.4617034617  z*≈1.3753951700
lambda=0.25 theta≈9.1100416873  u≈1.5768816516  v≈0.3139348711  z*≈0.4021627115
lambda_0=8/(3pi)≈0.84882636; z*(lambda>=lambda_0)=3pi/4≈2.35619449
```

The first two values used Simpson grid 256 during bisection and grid 512 for the reported moments; they are approximate diagnostics only. The exact result is the implicit expression (4), conditional on c8ce. No source equivalence, novelty, formal/independent review, joint-vanishing-ratio result, or parent acceptance is claimed.
