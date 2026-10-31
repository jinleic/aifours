# N=2 scalar minimum: corrected normal cones and a necessary nonsmooth condition

**Disposition: partial same-harness written support; the original f280 package is not accepted as a complete repair.** Native clock before composition: 2026-10-29T20:56:51-0700 PDT. The original 59-LF manuscript has **0F/2M/1m**. Parent read it, the complete 172-LF review and both 16/44-LF adopted imports; all frozen bindings match. Parent separately read the later owner addendum (SHA 5042e2f1...fd4b). That addendum was not an input to the completed reviewer attempt and does not retroactively change its verdict.

## Adopted necessary conditions

Retain the full actual-cutoff-two hypothesis 1/2<V≤2 and the f273 conditional attained reduction V=min_K ρ, K={a≥0,c≥a+1/2}. Write h(x;λ) for the corrected-profile signed value and λ*=ρ(x*). Strict decrease in λ and the unique zero give

ρ(x)≥λ* if and only if h(x;λ*)≥0.

Thus a constrained local minimum of ρ is a constrained local minimum of h(·;λ*) at value zero. No exact implicit Clarke identity is needed. With a specified compatible local Lipschitz extension (or a precise relative convention), constrained Fermat gives the necessary condition **0∈∂_C h(·;λ*)+N_K**. It is not a sufficient condition or an equivalence to ordinary directional nonnegativity.

At a smooth point the full geometric conditions are:

| Geometry | Necessary gradient conditions |
|---|---|
| a>0, c>a+1/2 | h_a=h_c=0 |
| a>0, c=a+1/2 | h_a+h_c=0, h_c≥0 |
| a=0, c=1/2 | h_a+h_c≥0, h_c≥0 |
| a=0, c>1/2 | h_c=0, h_a≥0 |

At a kink use **one and the same** g∈∂_C h in the corresponding row. At the vertex, the feasible tangent cone is cone{(0,1),(1,1)}. Its polar is cone{(−1,0),(1,−1)}, so −g in that cone requires g_c≥0 and g_a+g_c≥0. Parent independently reconstructed this polar and both feasible-ray tests. There is no sign reversal of h_c at the vertex.

Under the imported unique fixed-profile rule, h_λ=−Z evaluated at that minimizing profile is single-valued and negative, with Z≥2bT₂>0. Local Lipschitzness on K and regular smooth-stratum differentiation are supported at that imported scope, not a proof of Clarke regularity through every frontier. On each actual block interval [L,U], Leibniz uses its own limits, their speeds and any explicit parameter derivative of the integrand. The core interval ends at a, not universally c. Endpoint speeds are 1 and 2; diagonal ties require directional max/min rules rather than evaluating a strict indicator at equality. Tail constant and moving-join contributions must remain included. Zero a-dependence holds only for an entirely slack tail, not merely at some heights.

## Not adopted

**M1:** reject the original vertex cone, h_c≤0 and claimed sign reversal. The owner's later addendum correctly repairs this geometry and the core integration range (m1); this parent check is prospective.

**M2:** no exact partial-Clarke implicit identity, integral-selection equality or ordinary-one-sided-directional equivalence is established. Merely saying “inclusions only” does not settle the direction, hypotheses, moving-boundary terms or deterministic terms of an interchange formula. The late addendum's selection-set formulation is therefore **not adopted as an exact representation or automatic repair**. The necessary condition above uses the actual correctly defined subdifferential; an outer selection-set bound, if used, needs its containment direction and hypotheses explicitly proved.

The review's generic controls distinguish the issues: a constrained function increasing along the feasible vertical ray can minimize at the vertex, contradicting the old h_c≤0 rule; a minimum of smooth branches can be Clarke-stationary while decreasing in ordinary directions. These are written calculus checks, not selected privacy instances.

No scalar-pair uniqueness, sufficiency, vertex exclusion or global value formula follows. Item-(c) work must keep all diagonal, edge, vertex and kink branches unless separately excluded with valid arguments, and may not use the rejected exact identities.

## Evidence boundary

Source and returned review are preserved in the [f280 wave directory](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f280-privacy-n2-normal-cone-envelope/); the companion receipt pins the complete reads and the later addendum separately. Reviewer and parent used written reconstruction and metadata only here. Same-harness conditional imports remain explicit; no human, independent-family, formal/kernel or novelty verification.
