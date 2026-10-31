# Sharp global high-privacy TV repair of the product staircase

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:17:12 PDT 2026`.

## 1. Exact finite lower bound and globally sharp asymptotic

Fix epsilon>0, b=e^(-epsilon), m=b/(1-b), and ANY gamma in [0,1]. Let nu_gamma be the actual 1D epsilon-private symmetric staircase proportional to `b^(max(0,ceil(|x|-gamma)))`; put Q_gamma=nu_gamma tensor nu_gamma. Q_gamma is an auxiliary product and is NOT generally private for the full 2D diamond.

Define

    a_out=[min(gamma,1/2)+m/2]/[2(gamma+m)].                            (1)

For EVERY original all-event/full-closed-D epsilon-private 2D law mu, the source-independent written finite-epsilon bound is

    TV(mu,Q_gamma) >= [4b(1-b)/(1+b)] a_out^2.                           (2)

Its high-privacy expansion is `epsilon/8+O(epsilon^2)`, UNIFORMLY for gamma in [0,1]. An ACTUAL full-D-private radial staircase achieves the same leading value, so

    inf_(mu full-D epsilon-private) TV(mu,Q_gamma)
       =epsilon/8+O(epsilon^2),                                           (3)

again UNIFORMLY for arbitrary gamma(epsilon) in [0,1]. This is a GLOBAL infimum over all private Borel laws, not only radial or staircase laws. The result improves the epsilon/32 single-shift lower in unreviewed 1f6b; it is a statement about approximation of a NONPRIVATE comparator, not an exact optimizer for original J or L.

For epsilon=ln 2 and gamma=`3^(1/3)-1`, (2) yields

    TV(mu,Q_gamma) >= (gamma+1/2)^2/[6(gamma+1)^2]
                   >2209/31104 >1/15.                                   (4)

The interpretation of this gamma as the exact 1D J-optimal offset is conditional on unreviewed cde9; the geometric bound is independent of that theorem.

## 2. Four outward half-shifts and a finite all-law lower bound

The 1D normalizer is `2(gamma+m)`. For positive shift 1/2 define the HIGH region

    H_+ = union_(n>=0) ( max(0,gamma+n-1/2), gamma+n )

with empty intervals omitted; let H_-=-H_+. On H_+, `p(x+1/2)=b p(x)`, and H_+ lies strictly on the positive axis. Its exact probability is a_out in (1): the first interval has length min(gamma,1/2), all n>=1 intervals have length 1/2 and heights proportional to b^n. By symmetry nu(H_-)=a_out, `nu(H_+ +1/2)=nu(H_- -1/2)=b a_out`, and the two latter shifted sets lie strictly on opposite axes.

For each sign pair sigma=(sigma1,sigma2) in {+,-}^2 set

    A_sigma=H_sigma1 x H_sigma2,
    B_sigma=A_sigma+(sigma1/2,sigma2/2).

All four A_sigma are pairwise disjoint (quadrants), as are all four B_sigma. Every displacement is in D. Thus ANY actual full-D-private mu obeys, after summing the four distinct privacy inequalities,

    mu(B)>=b mu(A),   A=union A_sigma, B=union B_sigma.                   (5)

The auxiliary product has `Q(A)=4a_out^2`, `Q(B)=4b^2 a_out^2`. Comparing the two event probabilities to mu with the total-variation definition gives

    4b(1-b)a_out^2 <=(1+b)TV(mu,Q),

which is exactly (2). This sums FOUR valid privacy inequalities; it does not incorrectly replace the four different shifts by a single common shift.

For gamma in [0,1], `a_out=1/4+O(epsilon)` uniformly as m~1/epsilon and `4b(1-b)/(1+b)=2epsilon+O(epsilon^2)`. Equation (2) therefore gives the lower side of (3).

## 3. Matching actual private construction

Choose eta in [0,1] satisfying `eta=2gamma-1/2 mod 1`, and use the ACTUAL full-D-private diamond staircase P_eta. Under the product-Laplace reference, the fractional phases theta_i={|x_i|-gamma} are independent uniforms to O(epsilon); the staircase/reference ratios have first-order perturbations `theta_1+theta_2-1` for Q_gamma and `{theta_1+theta_2+1/2}-1/2` for P_eta. Thus their leading difference is `floor(theta_1+theta_2+1/2)-1`, whose absolute value is 1 on two triangles of total area 1/4 and 0 elsewhere. Uniform central-region and phase-periodization errors are O(epsilon^2) in L1. Consequently `TV(Q_gamma,P_eta)=epsilon/8+O(epsilon^2)`, proving the upper side of (3).

For the concrete (4), cde9 gives gamma=`3^(1/3)-1` for the 1D J optimum, so 11/25<gamma<1/2 by exact cubes. Here b=1/2,m=1 and `a_out=(gamma+1/2)/[2(gamma+1)]`. The latter is increasing in gamma, hence `a_out>47/144` and the lower in (2) is greater than `(2/3)(47/144)^2=2209/31104>1/15`. Only the assertion that this gamma is 1D-optimal imports cde9, SHA-256 `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`; the bound for the stated actual product is otherwise source-independent.

## 4. Status and suggested review

The whole proof is WRITTEN from original event privacy, exact 1D shell probabilities and an explicit true-private radial upper law. No parent/source optimality theorem, numeric computation, formal or independent review, novelty, exact finite-epsilon nearest-private optimizer, or parent adoption is claimed. The 1D-optimum interpretation in (4) has its explicit unreviewed input. High-priority review should scrutinize disjointness of the four A/B sets, summing different shift inequalities, the TV factor, uniform gamma endpoints and the first-order phase upper.
