# Sharp high-privacy value and universal product-Laplace law

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:39:40 PDT 2026`.

## 1. Main claims and exact class

For every epsilon>0 let b=e^(-epsilon) and let F_epsilon be the original ALL-Borel, ALL-event, FULL closed l1-unit-diamond private noise laws on R^2. Put `J=E|X|_2^2`, `L=E||X||_1`. The source-independent written finite-epsilon bounds are

    J >= 2b(1+b)/(1-b)^2,          L >= 2b/(1-b).                       (1)

The actual product-Laplace density `(epsilon^2/4)exp(-epsilon||x||_1)` is fully private and has `J=4/epsilon^2`, `L=2/epsilon`. Consequently

    inf_(F_epsilon) J = (4/epsilon^2)[1+O(epsilon)],                    (2)
    inf_(F_epsilon) L = (2/epsilon)[1+O(epsilon)].                       (3)

More strongly, for ANY weight kappa=kappa(epsilon)>=0, possibly oscillating or unbounded,

    inf_(F_epsilon)(J+kappa L)
       = [4/epsilon^2+2kappa/epsilon][1+O(epsilon)],                     (4)

with a UNIVERSAL relative O(epsilon), not one depending on kappa.

If ANY actual feasible sequence satisfies the first-order-near-optimal condition

    J+kappa L <= [4/epsilon^2+2kappa/epsilon][1+o(1)],                    (5)

then its scaled law converges to the unique product-Laplace law in BOTH total variation and W1:

    Law(epsilon X) -> Lambda(dz)=(1/4)e^(-||z||_1)dz.                    (6)

If `kappa epsilon` remains bounded, this convergence also holds in W2. If `kappa epsilon->infinity`, W2 need not converge and may diverge, despite (5), TV and W1; an actual private example is given in §6. Taking kappa=0 gives universal original-J near-optimal TV AND W2 convergence. No LAW642, MDA, PMLR, v241 or prior research theorem is imported.

## 2. Finite privacy: two one-dimensional tail inequalities

Each coordinate marginal inherits epsilon privacy for the shifts +1 and -1 because the corresponding coordinate unit vectors are in D. For i=1,2 and every integer n>=1, repeated privacy on the positive and negative half-lines gives

    P(X_i>=n) >= b^n P(X_i>=0),
    P(X_i<=-n)>= b^n P(X_i<=0).

The two outer events are disjoint, while the two inner events have combined probability at least 1. Thus `P(|X_i|>=n)>=b^n`. Integrating tail probabilities on each interval [n-1,n] yields

    E|X_i| >= sum_(n>=1) b^n =b/(1-b),
    E X_i^2 >= sum_(n>=1)(2n-1)b^n =b(1+b)/(1-b)^2.

Summing the two coordinates proves (1) without a density, symmetry, independence or optimizer assumption. The Laplace density in §1 is an actual private law by the reverse triangle inequality, and its stated moments are exact. Since

    epsilon b/(1-b)=1+O(epsilon),
    epsilon^2 b(1+b)/(1-b)^2=2+O(epsilon),

(1) and the Laplace law prove (2)–(4), with the same relative error bound uniformly for all nonnegative weights.

## 3. Any high-privacy weak limit is log-Lipschitz

Let Z=epsilon X and denote its law by mu_epsilon. For ANY fixed h in R^2, express the original displacement h/epsilon as `n=ceil(||h||_1/epsilon)` equal D-steps. Repeated privacy gives

    mu_epsilon(A) <= exp(epsilon n) mu_epsilon(A+h)
                  <= exp(||h||_1+epsilon) mu_epsilon(A+h).                (7)

This holds for every Borel A.

Under (5) put alpha=kappa epsilon. If alpha remains bounded along a subsequence, (1) bounds E|Z|^2 uniformly; if alpha->infinity along a subsequence, (1)–(5) give E||Z||_1->2. Thus each case is tight. Weakly pass to a subsequence. Applying (7) to nonnegative bounded continuous test functions and taking the limit gives, for EVERY h,

    mu(A)<=exp(||h||_1)mu(A+h).                                          (8)

The inequality for sets follows from the test-function measure order. Integrating (8) over h in D proves `mu(A)<=e |A|/2`, so mu has a bounded density. Its ball-average limsup representative satisfies the ratio (8) at EVERY point. It is strictly positive because it is nonzero somewhere and the two directions of (8) propagate positivity, and therefore its log is globally 1-Lipschitz for the l1 distance. In particular the density p is locally Lipschitz and, almost everywhere,

    |partial_i p|<=p   for i=1,2.                                         (9)

This conclusion comes from the ORIGINAL full shift family, not from assuming regularity of the initial laws.

## 4. Rigidity of equality and all-nearopt weak limits

For any probability density satisfying (9), with finite relevant moments, integration by parts with compact cutoffs gives for each coordinate

    1=-integral z_i partial_i p <= integral |z_i|p,
    2 integral |z_i|p =-integral z_i|z_i| partial_i p
                        <=integral z_i^2 p.                               (10)

The cutoffs are removed using the stated finite first or second moments. If `integral ||z||_1 p=2`, equality in the first inequalities forces `partial_i p=-sign(z_i)p` almost everywhere for both coordinates. The ONLY normalized solution is `p=(1/4)e^(-||z||_1)`. If `integral |z|^2p=4`, both inequalities in (10) are equalities, reducing to the same solution.

Now return to (5). If alpha is bounded, write `U=E|Z|^2`, `V=E||Z||_1`. The marginal bounds give `U>=4-o(1)` and `V>=2-o(1)`; the total upper bound `U+alpha V<=(4+2alpha)[1+o(1)]` implies U->4. Every weak limit has squared moment <=4 by lower semicontinuity, while (10) forces >=4; it is Lambda. If alpha->infinity, (5) and U>=0 give V<=2+o(1), while the marginal lower bound gives V>=2-o(1); every weak limit has first moment <=2 and hence is Lambda by (10).

An arbitrary alpha sequence has either a bounded or an alpha->infinity subsubsequence, so EVERY weak subsequential limit is Lambda. This proves weak convergence of the full sequence. In the bounded-alpha case U->4, so weak convergence plus second-moment convergence implies W2. In the alpha->infinity case V->2, so weak convergence plus first-moment convergence implies W1. A subsequence argument gives W1 for arbitrary nonnegative alpha.

## 5. Upgrading weak convergence to total variation

Original finite-epsilon privacy implies each mu_epsilon has a density f_epsilon. The same all-point ball-average representative argument, applied to (7), gives

    ||f_epsilon(.-h)-f_epsilon||_1 <= exp(||h||_1+epsilon)-1.            (11)

Let rho_delta be a compact smooth probability kernel supported in delta D. Then

    ||f_epsilon-f_epsilon*rho_delta||_1 <= exp(delta+epsilon)-1.          (12)

For fixed delta, weak convergence plus tightness implies `f_epsilon*rho_delta -> Lambda*rho_delta` in L1: convergence is uniform on compact sets by equicontinuity of the fixed kernel, and tightness controls the tails. First take epsilon->0, then delta->0 in (12) and use L1 continuity of mollification of Lambda. This proves total variation in (6), including when the original scaled densities have small discontinuities.

## 6. Actual W2 failure when the mean weight dominates

Take alpha=kappa epsilon->infinity. In Z coordinates, mix `(1-t)Lambda+t tau_(R e1)Lambda` with `R=alpha^(1/2)` and `t=alpha^(-3/4)`. In original X coordinates this is a mixture of two translates of the actual epsilon-private product-Laplace law, hence fully private. Exactly

    E|Z|^2 =4+tR^2=4+alpha^(1/4),
    |E||Z||_1-2| <=tR=alpha^(-1/4).

The mixed objective differs from `4+2alpha` by at most `alpha^(1/4)+alpha^(3/4)=o(alpha)`, so (5) holds. The second moment diverges and W2(Law(Z),Lambda)->infinity by the reverse triangle inequality in L2. In contrast TV<=t->0 and W1<=tR->0. This demonstrates the sharp difference between universal TV/W1 and W2 when alpha is unbounded.

## 7. Status and recommended review

No numerical, formal, independent-model, human or parent verification of these claims was performed. The proof uses standard measure order, Lebesgue differentiation, weak compactness, integration by parts and mollification; it does not import a named research theorem or earlier candidate. Disjoint review should scrutinize the half-line tail inequalities, limiting measure-order passage, equality rigidity, uniform-in-kappa case split, and the TV/W2 conclusions. There is no novelty, priority, exact finite-epsilon optimum, or parent-adoption claim.
