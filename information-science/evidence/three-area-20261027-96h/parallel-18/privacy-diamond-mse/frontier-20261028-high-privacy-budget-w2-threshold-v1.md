# Sharp W2 threshold for high-privacy joint-budget mechanisms

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:50:18 PDT 2026`.

## 1. Scope and named imports

Assume the unreviewed pinned high-privacy all-law rigidity candidate `frontier-20261028-sharp-high-privacy-universal-limit-v1.md`, SHA-256 `8615b71531aee0c55760796aad35dc6cb39002606b64b919017ed7a6e8b647d2`, and the source-independent but unreviewed high-privacy budget bracket `frontier-20261028-high-privacy-budget-inversion-v1.md`, SHA-256 `ba65c92c585e68fc7dbfc4047a532811710f488114de95023f3e5ef239f0b834`. No LAW642, MDA or PMLR theorem is imported.

Let j,ell->infinity, lambda=ell/sqrt(j), and let epsilon_min(j,ell) be the minimum-privacy infimum for actual full-D-private laws subject to J<=j and L<=ell. Consider arbitrary feasible law sequences with `epsilon/epsilon_min->1`, and write Z=epsilon X, Lambda=(1/4)e^(-||z||_1)dz.

The written threshold is:

* EVERY such mechanism sequence satisfies `Law(Z)->Lambda` in TV and W1, for ANY budget ratio sequence.
* EVERY such mechanism sequence also converges in W2 if `liminf lambda>=1`.
* Conversely, if `liminf lambda<1`, there exist such feasible near-minimum-privacy sequences for which W2 does NOT converge to 0. If lambda->0, the divergence can be made `W2->infinity`.

Thus `liminf ell/sqrt(j)>=1` is necessary and sufficient for UNIVERSAL W2 among near-minimum-privacy mechanisms; it is not a restriction on the existence of a good product-Laplace mechanism, which works at every ratio.

## 2. Universal convergence and sufficient W2 condition

The budget bracket gives `epsilon_min=2 max(j^(-1/2),ell^(-1))[1+o(1)]`. If ell>=sqrt(j) along a subsequence then

    E|Z|^2 <= epsilon^2 j <=4+o(1);

the original finite privacy lower bound in the rigidity import is `E|Z|^2>=4-o(1)`, so the original-J nearopt condition holds. If ell<sqrt(j), then

    E||Z||_1 <= epsilon ell <=2+o(1),

and the same import gives the lower bound `>=2-o(1)`; choosing a mixed weight large enough to suppress the finite J contribution converts this to its mean-dominant nearopt condition. The two alternatives show TV and W1 convergence along every subsequence.

If `liminf lambda>=1`, even in terms with lambda<1 we have `max(1,lambda^(-2))<=1+o(1)`, and thus

    E|Z|^2 <= epsilon^2 j =4 max(1,lambda^(-2))[1+o(1)] <=4+o(1).

The privacy lower bound forces convergence of this second moment to 4. Weak convergence to Lambda plus second-moment convergence gives W2 convergence, as claimed.

## 3. Necessity by an actual feasible rare-translation law

Suppose lambda<=c<1 along an infinite subsequence. Take any delta->0, `epsilon=2(1+delta)/ell`, and in Z coordinates use the mixture

    mu=(1-t)Lambda+t tau_(R e1)Lambda,
    K=2(c^(-2)-1)>0,   R=K/delta,   t=delta^2/K.                          (1)

For small delta, 0<t<1. In original X coordinates both components are translates of the true epsilon-private product-Laplace law, so their mixture is full-D private. Exactly

    E|Z|^2=4+tR^2=4+K,
    E||Z||_1 <=2+tR=2+delta.                                             (2)

Since `epsilon ell=2(1+delta)`, the mean budget holds. Also `epsilon^2 j=4(1+delta)^2/lambda^2>=4/c^2>4+K`, so the squared budget holds. The budget bracket makes this epsilon asymptotically minimal. Nevertheless

    W2(mu,Lambda)>=sqrt(4+K)-2>0.                                        (3)

If only a subsequence has lambda<=c, use this construction there and a budget-feasible product-Laplace law elsewhere; the complete sequence remains near-minimum-privacy but does not converge in W2.

If lambda->0, replace fixed K by `K=1/lambda->infinity` and use the same R=K/delta, t=delta^2/K. For small lambda, `4+K<4/lambda^2<=epsilon^2 j`, so both budgets hold and (3) diverges. Yet TV<=t->0 and W1<=tR=delta->0. All feasibility checks are for the ACTUAL law, not for a relaxed moment region.

## 4. Quantitative corollary, separately conditional

If additionally the unreviewed source-independent candidate `frontier-20261028-quantitative-high-privacy-rigidity-v1.md`, SHA-256 `dc2e2881f2b2f2978ab03ce505175f569272a26a8501e33a6c2feda7381b79be`, is valid, set `s=max(j^(-1/2),ell^(-1))` and `eta=|epsilon/(2s)-1|+s`. The active budget implies either the J gap or the L gap in that candidate is O(eta), giving the uniform coarse rate `TV=O(eta^(1/12))` as eta->0. This quantitative statement has the ADDITIONAL explicit unreviewed dependency dc2; the W2 threshold in §§1–3 does not.

## 5. Status

These are written deductions conditional on the pinned unreviewed imports and standard W2 moment theory, with an explicit feasible counterexample. No numerical, formal, independent-review, novelty, priority or parent-acceptance claim is made. Disjoint review should focus on the moving lambda threshold, strict budget inequalities in (2), and the divergence construction.
