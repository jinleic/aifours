# An exact normalized radial repair and high-privacy cubic bracket

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction series checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:44:07 PDT 2026`.

## 1. Exact finite bound and high-privacy refinement

Let Q be the product of two symmetric 1D half-offset epsilon-private staircases, `b=e^(-epsilon)`, and let `T_*(b)` be its nearest total-variation distance to ALL original full-D pure-epsilon-private 2D Borel laws. Put

    r=sqrt[(1+b^2)/2],
    eta=[r-b]/(1-b),
    U(b)=(1-b)/[2(1+r)^2].                                               (1)

For EVERY b in (0,1), eta is in (1/2,1), the actual 2D radial staircase P_eta is full-D private, and the source-independent written bracket is

    b(1-b)/(1+b)^3 <= T_*(b) <= TV(Q,P_eta)=U(b).                       (2)

At b=1/2 it reads `2/27<=T_*<=4/(4+sqrt(10))^2`. The right side is an exact comparison to a particular actual mechanism, not a claim of finite-b nearest-law optimality.

At high privacy epsilon->0 the exact bounds give

    epsilon/8-epsilon^3/24+O(epsilon^5) <= T_*
      <= epsilon/8-13epsilon^3/384+O(epsilon^4).                         (3)

In particular the epsilon^2 coefficient of the GLOBAL infimum is zero. If the epsilon^3 coefficient limit exists, it lies in `[-1/24,-13/384]`; existence is not asserted. This refines the source-independent written epsilon/8 first-order result without importing it.

## 2. Exact lower by four different privacy shifts

Write m=b/(1-b). For the 1D half-offset staircase, the positive pre-jump half-interval union H+ has mass `a=1/[2(1+b)]`; H-=-H+ has the same mass. Its outward half-shifts map these sets to disjoint positive or negative sets with probability b a. For each sign pair sigma form `A_sigma=H_sigma1 x H_sigma2` and its outward shift `B_sigma=A_sigma+(sigma1/2,sigma2/2)`. The A_sigma are mutually disjoint, as are the B_sigma. Any full-D private mu satisfies `mu(union B_sigma)>=b mu(union A_sigma)`, while Q gives probabilities 4a^2 and 4b^2a^2. Comparing both events by TV yields the lower in (2).

## 3. Exact normalized radial upper

Let Z1=1+2m be the 1D normalizer and `Z_eta=2(eta^2+2m eta+m+2m^2)` the radial staircase normalizer. The chosen eta solves `Z_eta=Z1^2`, equivalently

    eta=-m+sqrt(m^2+m+1/2).                                              (4)

It lies in (1/2,1). For product indices n1,n2 and radial index n_R, the density ratio is `q/p_eta=b^(n1+n2-n_R)`. The exponent belongs to {-1,0,1}, and Q exceeds P_eta EXACTLY on k=-1. Write `|x_i|=n_i+u_i`; for n_i=0 use u_i in [0,1/2], otherwise u_i in [-1/2,1/2]. The k=-1 region is `u1+u2>eta`. Since eta>1/2, it is a triangle of side `1-eta` and area `(1-eta)^2/2` for EVERY index pair, including both central indices. Summing quadrants and geometric weights gives

    Q(k=-1)=2(1-eta)^2/(1+b)^2,
    TV(Q,P_eta)=(1-b)Q(k=-1).                                             (5)

From (4), `1-eta=(1+b)/[2(1+r)]`, so (5) simplifies to U(b). P_eta is actually full-D private by the unit-change-of-shell-index argument.

## 4. Exact series checks and limitations

The Python eval kernel used `fractions.Fraction` truncated power-series arithmetic with b=e^(-epsilon). It checked

    U=epsilon/8+0*epsilon^2-13epsilon^3/384+epsilon^4/128+...,
    b(1-b)/(1+b)^3=epsilon/8+0*epsilon^2-epsilon^3/24+0*epsilon^4+....

A separate 70-digit Decimal evaluation supplied point diagnostics only. All geometric and global-infimum deductions are WRITTEN, not formally/independently reviewed, novelty-cleared or parent-adopted. Suggested review: equality of normalizers, all central triangle areas, exact TV sign set and expansion direction.
