# Low-noise projector-overlap budgets from the new Pauli norm lemma

Actual clock preceding creation: **Sun Oct 25 04:38:30 PDT 2026**. Owner PhysicsDepol4. This is an immutable continuation of the SAME low-noise k2,3,4 target after completing assigned review v31-B. The primary packet under v31-E review is unchanged.

**Status: WRITTEN corollary at named imports.** No scientific arithmetic interpreter, eval, symbolic computation, enumeration, replay, solver, external-model CLI or nested agent was used. No independent written reconstruction of this corollary has been performed. There is still no unrestricted closure of any missing low-noise index and no exact physical counterexample.

## 1. Literal scope and imports

Let rho be ANY mixed or pure four-qubit state, Pi ANY complex orthogonal rank-k projector, k in{2,3,4}, and0<p<2/3. Use the actual unnormalized-identity marginal maps X_s, not an independently selected marginal tuple. Write

`u=p/[2(1-p)]`, `a3=(1-p)^3 p/2>0`,

`r=Tr(Pi rho)`, `d4=1-r`,

`d1=3k+1-Tr(Pi X1)`, `d2=3k+3-Tr(Pi X2)`,

`delta3=Tr(Pi X3)-(k+3)`.

These use the SAME actual rho, Pi and p. All three deficits are nonnegative: d4 by0<=Pi<=I, d1 by the universal X1 comparison, and d2 by the inherited frozen U2 certificates at k2,3,4.

Named imports:

- `low-noise-pair-norm-and-signed-map-v1.md`, SHA256 `5a067a6fb6c746ab0a47c20df2bc6b025986125dd18b2cda0ab045a82c896a83`, §§2–3: the NEW WRITTEN all-complex proof `Z(rho)<=4I`. Its v31-E reconstruction is a separate gate, not presumed returned or accepted here.
- `residual-low-noise-witness-profile-v1.md` §2: the exact coefficient identity for the original channel gap, reproduced in §2 below.
- The inherited frozen U2 certificate package and operative addendum at `priority-written-dispositions-v1.md` §3's trust boundary. Those certificates were not replayed.

No pure-state moment identity or pure-only second-eigenvalue assertion is needed. In particular, this corollary does NOT extend the pure lambda2(X3)<=2 statement to mixed inputs.

## 2. Exact original-channel gap

For0<p<2/3, the first k product-reference eigenvalues have sum

`(1-p/2)^4+(k-1)(1-p/2)^3(p/2)`.

Let G_k be `Tr(Pi D_p^tensor4(rho))` minus this reference sum. The nonnegative channel expansion and its coefficient ratios give EXACTLY

`G_k/a3=delta3-u^2 d1-u d2-d4/u`.                      (1)

This identity is at the original channel, not at the PPT relaxation. A strict counterexample with any actual projector therefore requires its right-hand side to be positive. Conversely, an actual projector with positive G_k witnesses a violated Ky-Fan comparison even if Pi was not independently identified as the output's leading spectral projector.

## 3. New actual-state bounds on the excess

The exact Pauli identity and new norm lemma give

`X3=2rho+Z/2<=2rho+2I`.

Taking the trace against the SAME rank-k Pi gives

`Tr(Pi X3)<=2r+2k`.

Thus

- at k2, `delta3<=2r-1=1-2d4`;
- at k3, `delta3<=2r=2-2d4`.

At k4 the sharper elementary bound for this purpose is `Tr(Pi X3)<=Tr X3=8`, giving `delta3<=1`. The new norm lemma alone would give `delta3<=3-2d4`, which is no stronger than1 for the relevant maximization; it is not substituted for the trace bound.

No off-range block is discarded. These inequalities hold for all actual rho and Pi, including Pi not containing rho's support.

## 4. Pointwise channel certificates and necessary violation budgets

Substituting §3 into(1) and using

`2+1/u=2+2(1-p)/p=2/p`,

yields the following exact pointwise upper bounds:

`k2: G_2/a3<=1-[u^2 d1+u d2+(2/p)d4]`,                 (2)

`k3: G_3/a3<=2-[u^2 d1+u d2+(2/p)d4]`,                 (3)

`k4: G_4/a3<=1-[u^2 d1+u d2+d4/u]`.                    (4)

Consequently, a STRICT physical counterexample necessarily satisfies

| index | necessary strict budget | necessary overlap |
|---|---|---|
|k2| `u^2 d1+u d2+(2/p)d4<1` | `d4<p/2`, equivalently `r>1-p/2` |
|k3| `u^2 d1+u d2+(2/p)d4<2` | `d4<p`, equivalently `r>1-p` |
|k4| `u^2 d1+u d2+d4/u<1` | `d4<u`, equivalently `r>1-u` |

These are actual SAME-projector conditions, not merely a constraint on an optimized unrelated X3 projector. They are valid for mixed states as well as pure states at the named Z1/U2 imports.

The contrapositives give exact exclusion certificates: if the corresponding budget is at least its right-hand threshold, the actual trace cannot beat the product-reference partial sum. In particular, an actual k2 witness projector with r<=1-p/2, or k3 witness projector with r<=1-p, is excluded for every input at that p. Equality in these overlap tests is also excluded because a channel counterexample must be strict.

This is a p-dependent quantitative restriction on any hypothetical violating projector, not an unrestricted state-region theorem or a replacement of the assigned target. The genuine top-k projector need not satisfy the excluded low-overlap condition.

## 5. What this does not repair

All final relaxed controls from §6 of `low-noise-pair-norm-and-signed-map-v1.md` have d4=0. At p=1/2 their new budgets are respectively17/44<1,3/4<2 and1/2<1. They therefore survive these NECESSARY budget screens, consistently with their positive relaxed channel gaps. No relaxation point has been promoted to an actual state/projector pair.

Likewise, small d4 does NOT allow replacing Pi by a projector containing psi without accounting for the changed trace. As p tends to zero these budgets force overlap toward one, but they give neither exact containment nor a uniform bound on the remaining off-range Schur correction. The old off-range method obstruction and the joint-Hessian beta-to-target transfer gap remain.

At d4=0 the required strict inequality still contains the unknown excess delta3 in(1). These budgets are not sufficient for a violation, and passing them does not provide a physical counterexample. An additional multi-vector Pauli bound or actual-state/projector compatibility estimate is still required.

## 6. Per-index settlement

- **k2: OPEN** for0<p<2/3. New WRITTEN witness budget(2) is available; `K2(X3)<=5` or a direct unrestricted channel certificate remains unproved.
- **k3: OPEN** for0<p<2/3. New WRITTEN witness budget(3) is available; `K3(X3)<=6` or a direct unrestricted channel certificate remains unproved.
- **k4: OPEN** for0<p<2/3. Trace-derived budget(4) is recorded for a uniform interface; it is not claimed as a new solution or a new Pauli-norm consequence. `K4(X3)<=7` or a direct unrestricted channel certificate remains unproved.

No full all-p composition follows. Central/high-noise imports retain their prior scope. Zhang's matched complementary clipped-tail mechanism remains explicitly attributed by the unchanged source-audit-v2 note; no novelty, formal/kernel, independent-model or worldwide-priority clearance is asserted.
