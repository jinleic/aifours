# Independent written reconstruction: tail-envelope characterization

Before-creation clock observed: **2026-10-23T13:18:08-07:00**. Reviewer: PhysicsResearch96h. No author edits, scientific program, solver, model CLI or formal proof was performed.

## Snapshot and verdict

Reviewed all 145 lines of `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-tail-envelope-characterization-v1.md`, SHA-256 **`ddad3ac40668af6363a9e69fa489bfc67406c17f96abe7e9db79569338859ce5`**.

**0 FATAL / 0 MAJOR / 0 MINOR. No substantive defect found under the fixed p,q,g_min and complete bounded-real-model boundaries.** Both curve-evaluation identities and both directions of the complete-invariant criterion reconstruct. The result does not claim to recover the factual distributions themselves or to be a finite-sample sufficient-statistic theorem.

## 1. Feasible switch domain and the two tail functions (lines 7–17)

For r in I, the two switch masses are r and t=r-h, so `r+t=2r-h<=1`. Thus every feasible r lies at or below `(1+h)/2`. The earlier tail-extremum construction gives W nonnegative, concave, nondecreasing and 2-Lipschitz. For reflected factual outcomes, the upper-tail integral is `x-ell_s(x)`, so its combined W is exactly Wbar and it has the same properties. These statements remain true with atoms or zero strata.

## 2. Least nondecreasing 1-Lipschitz majorant (lines 19–54)

For each fixed r, `W(r)-(r-m)_+` is nondecreasing and 1-Lipschitz in m. Taking an attained maximum preserves both properties. On I, the choice r=m gives E_W(m)>=W(m).

If g is any nondecreasing 1-Lipschitz majorant on I, then for r<=m, monotonicity gives g(m)>=g(r); for r>=m, the Lipschitz condition gives g(m)>=g(r)-(r-m). Therefore in both cases `g(m)>=W(r)-(r-m)_+`. Maximizing proves g>=E_W. This establishes the exact least-majorant order, not just one admissible majorant.

Joint concavity of `W(r)-(r-m)_+`, together with the convex feasible interval I, proves concavity of E: mix the two maximizing r values when mixing the two m values. This is a valid partial-maximization argument for a jointly concave function; it does not rely on the generally false claim that an arbitrary maximum of concave functions is concave.

Let r0 maximize W-r and K be that maximum. If m<=r0, the r>=m branch attains m+K at r0, while every r<=m contributes at most r+K<=m+K. If r0<=m<=u, concavity makes W-r nonincreasing to the right of m; both branches maximize at m and yield W(m). If m>=u, monotonicity yields W(u). These are exactly the three cases in (4). If r0 ranges over a flat interval of maximizers, W(r)=r+K there, so no choice ambiguity remains.

Outside I the envelope need not be nonnegative; the manuscript does not claim otherwise. This is consistent with positive lower bounds, because the lower curve is -E at a tent argument that may be outside I.

## 3. Evaluation of L and U (lines 56–101)

The two lower hinge locations are `a=h+eta` and `b=1-eta`, with sum 1+h. The larger is at least `(1+h)/2`, hence at least every feasible r. Its hinge vanishes exactly, including equality at an endpoint. The remaining hinge is at `m_L=min(a,b)`, so

`F_eta(r)=(r-m_L)_+-W(r)`.

Minimizing over I therefore gives `L=-E_W(m_L)`, with the displayed sign and without a residual constant.

For outcome reflection, the normalized budget changes from eta to 1-eta (because gamma changes sign and g_min changes to -1-g_min). Applying the same lower formula to Wbar and negating gives

`U=E_Wbar(min(h+1-eta,eta))`.

It also agrees with the direct G_eta expansion from the base theorem. Since the larger hinge is at or beyond u and r_minus/r_plus lie in I, the former median/clamp selector is exactly `clamp_I(max(r0,min_hinge))`; no optimizer convention changed.

## 4. Recovery/injectivity from the full curves (lines 103–130)

Fixing p,q fixes h and I; fixing g_min also fixes the complete compatible gamma interval of length one. For any m in I choose eta=m-h. This is the feasible defier mass t, so it lies in [0,1]. Feasibility gives `2m-h<=1`, hence

`m_L(eta)=min(m,1-m+h)=m`.

Thus the **entire** lower curve genuinely exposes every envelope ordinate on I:

`E_W(m)=-L(g_min+m-h)`.

For the upper curve choose eta=m, which also lies in [0,1]. The same inequality gives

`m_U(eta)=min(h+1-m,m)=m`,

and hence `E_Wbar(m)=U(g_min+m)` for every m in I. These choices remain available at endpoints and for singleton I, so no unexplored part of either envelope restriction is hidden from the curves.

For sufficiency, E_W restricted to I supplies `K=E_W(l)-l`. The exact global formula then extends it to `m+K` for m<l and the constant E_W(u) for m>u. The same is true for Wbar. Therefore equal restrictions determine equal E values even when a tent argument lies outside I, and hence equal complete L/U curves. Necessity follows from the two recovery formulas just reconstructed.

This proves equality of the two envelope restrictions **if and only if** equality of the entire identified-interval curves for common p,q,g_min. It does not claim that one envelope alone determines both endpoints, that one gamma suffices, or that the original laws are injectively recoverable.

## 5. Threshold relation and limits (lines 132–145)

Since `B_*=1+max(W-r)=1+K`, the main sign threshold is `g_min+1+E_W(l)-l`, exactly as displayed. A nonlinear trimmed-tail summary need not be a finite list of ordinary moments, so this does not contradict a moment-summary barrier. That separate barrier proof was not needed for the envelope result.

Correctness here is population partial identification under the fixed model. It is not a clinical claim, finite-sample inference, universal statistical sufficiency, novelty certification or a repair of the separate Kuroki access gate. Parent and formal/human gates remain distinct.
