# Item (a): complete normal-cone/kink envelope conditions for the N=2 two-scalar minimum

Owner: InfoResearch96h-2 / info-1. Native clock observed before drafting: `Thu Oct 29 20:20:00 PDT 2026`.

**AUTHOR-WRITTEN, UNREVIEWED; repairs the f273 M1 at all-variable scope.** Standing hypothesis of the f273-adopted reduction: the actual cutoff is two, `1/2<V<=2` (now certified nonempty by the frozen f278 candidate), and `V=min rho(a,c)` over `K={a>=0, c>=a+1/2}`, with rho(a,c) the unique zero in λ of the corrected-profile value h(a,c;λ). No ε is selected; no numeric instance is used.

## 1. Objects and regularity

Fix λ>0. With the adopted two-line rule, the per-height minimized integrands are minima of finitely many candidates, each a C^∞ function of (a,c) on its stratum: the slack value (projections Π_0, Π_1 of the block roots R_0, R_1 onto their moving boxes) and the active value (S*=projection of the pooled root R_1 onto the moving diagonal interval), plus the corner and free-tail one-variable clips for heights in (a,a+1/2] and (a+1/2,c]. Integrating over y with moving limits, h(a,c;λ) is:

* **locally Lipschitz** on K (candidates and their (a,c)-gradients are uniformly bounded on compacts; only finitely many strata);
* **C^1 on each open stratum**, the strata being separated by the coincidence surfaces (slack-vs-active equality; box-boundary coincidences R_0=a, R_0=2a−y, R_1=c, R_1=2c−y; interval-endpoint coincidences a=c−1, 2a−y=2c−y−1);
* **strictly decreasing in λ** with `∂_λ h=−Z_min<0`, where `Z_min>=2bT2>0` is continuous and single-valued in (a,c,λ).

**Stratum gradients (Danskin+Leibniz master form).** On a stratum, for a block value `V(a)=8∫ min_{z∈[ℓ(a),u(a)]} ψ(z,y)dy` with moving box endpoints of speeds ℓ', u' and moving integral limits,

    ∂_a V = 8[ψ(z*(ŷ),ŷ)]_ŷ=limits + 8∫_0^{c} ψ_z(z*(y),y)·(1_{z*=ℓ}ℓ' + 1_{z*=u}u')dy,   (M)

where z*(y) is the (unique, by strict convexity) pointwise minimizer and the bracketed boundary term carries the y-limit speeds (1 at y=a and y=a+1/2 for the corner subinterval; 1 at y=c). Instantiated: ∂_aΦ_0^min uses speeds (1 at the lower box z=a, 2 at the upper z=2a−y); ∂_cTail^min uses the constant part's derivative (16/3)T3+8cT2−λ8m, speed 1 at z=c and 2 at z=2c−y, and the y=c boundary term; ∂_aTail^min is ZERO on slack strata (no a-dependence) and on active strata uses the diagonal-interval speeds (∂_aℓ=1_{a>c−1}, ∂_a u=2·1_{2a−y<2c−y−1}) together with the moving corner-subinterval limits (speeds 1 at y=a and 1 at y=a+1/2) and the corner-floor speed 2 on {2a+1−y>c}. Every coefficient is explicit; no unstated stationarity is used anywhere below.

**Clarke subdifferential.** h is an integral of pointwise minima of finitely many C^1 candidates with C^1 moving switching surfaces; by the standard interchange for Lipschitz integrands, ∂_C h_{(a,c)}(a,c;λ) is the set of integrals of measurable selections from the pointwise convex hulls `co{∇σ(y), ∇α(y)}` on the coincidence set {σ=α} and the single relevant gradient elsewhere; at heights where candidates additionally coincide with box faces, the hull is over the coinciding candidates only. In particular ∂_C h is a nonempty compact convex set equal to {∇h} at smooth points.

## 2. The five geometries: complete first-order conditions

Let (a*,c*) minimize rho over K and let λ*=rho(a*,c*)=V, so h(a*,c*;λ*)=0. Because ∂_λ h<0 is continuous and single-valued, Clarke's implicit-function chain rule gives `∂_C rho(a*,c*) = −∂_C h_{(a,c)}(a*,c*;λ*)/(∂_λ h)`; since the normal cone N_K is a cone and ∂_λh<0, the minimum condition `0∈∂_C rho + N_K` is EQUIVALENT to

    0 ∈ ∂_C h_{(a,c)}(a*,c*;λ*) + N_K(a*,c*).                          (F)

Evaluating N_K in each geometry gives the promised boundary formulas:

**(G1) Interior smooth point** (a*>0, c*>a*+1/2, stratum-smooth): ∇_{(a,c)}h=0. This is the only place where unrestricted stationarity is valid.

**(G2) Corner edge** (a*>0, c*=a*+1/2, smooth strata): N_K={t(1,−1):t>=0}, hence

    h_a = −t,  h_c = t,  i.e.  h_a + h_c = 0  with  h_c >= 0.            (G2)

Tangential stationarity along the edge plus a nonnegative inward-normal derivative. Equivalently, in edge parametrization s=a, d/ds h(s,s+1/2;λ*)=0 and ∂_c h>=0.

**(G3) Vertex** (a*=0, c*=1/2): both constraints active; N_K={ (−x−z, x): x,z>=0 }, hence

    h_c <= 0   and   h_a + h_c >= 0.                                     (G3)

Note the SIGN REVERSAL relative to (G2): at the vertex the feasible directions are {u>=0, w>=u}; the two active constraints contribute both generators. A condition copied from (G2) would be wrong here.

**(G4) a=0 edge** (a*=0, c*>1/2): N_K={t(−1,0):t>=0}, hence

    h_c = 0   with   h_a >= 0.                                           (G4)

**(G5) Interior or boundary KINK** (any feasible point where the stratum is not smooth): the condition is the SUBDIFFERENTIAL system: there exists a measurable selection g(y) from the pointwise hulls of §1 such that −∫g(y)dy ∈ N_K; equivalently all one-sided directional derivatives of h along feasible directions are >=0. NO single branch's gradient may be set to zero: at a slack/active kink each branch gradient separately defines only a one-sided derivative.

At a corner-edge kink, (G2) is replaced by: ∃g∈∂_C h with g_a+g_c=0 and g_c>=0; analogously at (G3)/(G4) vertices/edges. These mixed statements are the complete repair of the non-adopted P3: the two-equation system is valid ONLY on (G1), and on the boundary/kink loci exactly the displayed sign systems hold.

## 3. Sufficiency status and what remains open

These are necessary conditions. Convexity of rho in (a,c) is NOT established (the two blocks' regime boundaries differ; the pooled identity does not globalize), so no sufficiency and no uniqueness follows — item (c) remains open. Second-order/structure analysis of the corner-edge condition (G2) — e.g., whether h_c>0 forces the minimizer off the corner, or whether the vertex condition (G3) can hold at all — is open. All statements are at the standing hypothesis; nothing here selects ε or computes instances.

## 4. Premises, noninputs, controls

Premises: the f273-adopted items 1–5 (two-line rule, one-way active-interval implication, strict fixed-parameter uniqueness, attained implicit reduction rho). Standard imports: Danskin's theorem, Clarke subdifferential/implicit-function chain rule for Lipschitz maps with a strictly single-valued partial, Lebesgue dominated convergence. No diagnostics were run for this packet (no script, no grid); the failed/superseded script artifacts of checkpoint 018 remain as there disclosed. Same continuing author; no held/withdrawn/ZERO body, MDA26 source text, f161/f162 or protected v214 material used; the monotonicity observation stays unreviewed and separate, not folded here; no ln64 or parameter variant is introduced.
