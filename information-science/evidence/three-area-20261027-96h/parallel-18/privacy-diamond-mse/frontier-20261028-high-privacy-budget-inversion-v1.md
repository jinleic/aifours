# Elementary finite and sharp high-privacy budget inversion

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:41:51 PDT 2026`.

## 1. Explicit finite-b bracket

For j,ell>0, let epsilon_min(j,ell) be the infimum epsilon>0 over all original all-event/full closed l1-diamond-private Borel noise laws with `J=E|X|^2<=j`, `L=E||X||_1<=ell`. The source-independent written assertion is the FINITE-budget bracket

    max{ log[(j+1+sqrt(4j+1))/j], log[1+2/ell] }
       <= epsilon_min(j,ell)
       <= max{ 2/sqrt(j), 2/ell }.                                       (1)

The upper side is achieved as a budget-feasible value by the actual product-Laplace law, not a relaxed construction. For the individual problems, use only the corresponding lower and upper entries.

If j->infinity and ell->infinity in ANY relative proportions, put `s=max(j^(-1/2),ell^(-1))`. Then

    epsilon_min(j,ell) = 2s+O(s^2),                                      (2)

with the one-sided bounds `2s-O(s^2)<=epsilon_min<=2s` and a universal error constant. In particular `epsilon_min^J(j)=2/sqrt(j)+O(1/j)` as j->infinity and `epsilon_min^L(ell)=2/ell+O(1/ell^2)` as ell->infinity. This is an arbitrarily varying JOINT budget ratio, not only a fixed-ray limit.

## 2. Proof from actual half-line privacy

For b=e^(-epsilon) and every coordinate, repeated privacy on the two half-lines gives `P(|X_i|>=n)>=b^n` for integers n>=1. Integrating over unit intervals gives the finite-epsilon bounds

    J>=2b(1+b)/(1-b)^2,       L>=2b/(1-b).                              (3)

The mean constraint ell>=2b/(1-b) gives `b<=ell/(ell+2)`. The squared constraint j>=2b(1+b)/(1-b)^2 is equivalent, by solving the quadratic and rationalizing, to

    b <= j/[j+1+sqrt(4j+1)].                                             (4)

Taking -log of these two necessary conditions gives the lower half of (1). The product-Laplace density `(epsilon^2/4)e^(-epsilon||x||_1)` has `J=4/epsilon^2` and `L=2/epsilon`, so epsilon equal to the upper half of (1) meets BOTH budgets and is fully private by the reverse triangle inequality.

For x=1/sqrt(j)->0, the J log bound is `2x+O(x^2)`; for y=1/ell->0, the L log bound is `2y+O(y^2)`. Their maximum is `2max(x,y)+O(max(x,y)^2)`, and the product-Laplace upper is exactly `2max(x,y)`, proving (2). This proof invokes no external research theorem, optimizer family or previous candidate.

## 3. Conditional limit-law consequence

The separately pinned, unreviewed candidate `frontier-20261028-sharp-high-privacy-universal-limit-v1.md`, SHA-256 `8615b71531aee0c55760796aad35dc6cb39002606b64b919017ed7a6e8b647d2`, would additionally imply that if a feasible mechanism uses `epsilon/epsilon_min(j,ell)->1` in the regime j,ell->infinity, then `Law(epsilon X)` converges to the product-Laplace law in TV and W1. To see this, along any subsequence either `ell>=sqrt(j)` or `ell<sqrt(j)`: in the former the J budget is asymptotically tight at the lower value 4/epsilon^2, and in the latter the L budget is asymptotically tight at 2/epsilon. In the latter case choose `alpha=kappa epsilon=(1+epsilon^2 j)/epsilon`, so alpha->infinity and the scaled J contribution divided by alpha vanishes; the import's mixed-nearoptimality condition then follows from mean nearoptimality. This paragraph is CONDITIONAL on the unreviewed rigidity proof and is not needed for (1)–(2).

## 4. Scope

The finite and high-privacy inversion in (1)–(4) is a written source-independent result, not an exact finite-budget optimum, novelty claim, formal proof, independent review or parent adoption. No numerical checks or external source imports were used. Disjoint review should check the quadratic root, simultaneous lower-bound maximization and the uniform big-O in (2).
