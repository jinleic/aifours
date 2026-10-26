# NormalizedN4 preparation addendum1 — PPT headroom and mutation controls

Observed immediately before creation: **2026-10-23T15:20:15-07:00**. PhysicsPPT44. Written preparation only. Nothing here authorizes execution, validates unrun code, or promotes a numerical witness. The script/input/request pins remain those in `admission-request-normalized-bose-N4-v1.json`, SHA `198327a9eed06cee76574ad22e2a18f1cfce40a9d3a984af485229eb6f213ab4`.

## 1. What the PPT-specific headroom assessment can and cannot establish

The exact target is the PPT local-filter image `rho_x=R_x/49` at x=(1,1,1,1). It is outside the slot's proved SN2 mixed-kernel region. The physical witness is an unrestricted real symmetric16by16 Y (real restriction justified only by conjugation averaging for this real input), not Park's two-parameter covariant family. The normalization correction was explicitly derived from canonical lifting trace at most two; it does not inherit the bare-lift's all-level PSD-only proof.

The exact N4 non-PSD control proves that the **particular finite cone** is not PSD-only. It does not prove that it contains an indecomposable ququart witness, can detect a PPT state, or detects the chosen target. The control is reduction-type, and this limitation remains an explicit open GO gate.

There is nevertheless a meaningful PPT-specific theoretical check: the **trace-corrected hierarchy as a family** is not incapable of PPT detection in all dimensions. The following compactness/duality argument shows why; it does not replace the still-unknown N4/ququart headroom with a claim that it is passed.

## 2. Why the corrected family is not another all-level dead end

Use unnormalized auxiliary Omega_k and write C_N for contraction on Alice's auxiliary and Bob1's auxiliary. For physical trace-one rho define the finite outer set

`K_N={C_N(sigma_N): sigma_N>=0, Bose-supported on the N complete Bob copies,`
`                       Tr(sigma_N)<=k, Tr(C_N(sigma_N))=1}`.

For k=2 the dual sufficient certificate is exactly the new cone

`Q_N(Y)+mu(I-2Q_N(I))>=0`, `mu>=0`.

The canonical Schmidt construction in the frozen proposal proves `SN<=k subset K_N` for every finite N. In general k, a normalized rank-at-most-k vector with Schmidt coefficients s_i admits a product lift of trace `(sum_i s_i)^2<=k`; normalize the Bob factor to norm one and extend it identically N times. Mixtures preserve the trace bound and Bose support.

Each K_N is compact: positive sigma_N with trace bounded by k form a compact finite-dimensional set, Bose support and trace equalities are closed, and contraction is continuous. Partial trace gives `K_(N+1) subset K_N`.

Suppose a fixed rho belongs to every K_N. Choose associated sigma_N. Their Alice-plus-first-Bob marginals have uniformly bounded trace and hence a convergent subsequence. By a diagonal subsequence over each fixed number M of Bob copies, obtain Bose extensions for the same limiting marginal at every M. Its trace is nonzero because contraction has trace one. The standard infinite-extendibility/de Finetti characterization of separability (the import used in Chen–Collins–Fawzi Section2.2) therefore makes this limiting marginal separable across the augmented Alice:Bob cut. Contracting its auxiliary factors maps every augmented product vector to a physical vector of Schmidt rank at most k. Its contraction is still rho by continuity. Hence `SN(rho)<=k`.

Thus

`intersection_(finite N) K_N = {physical states with SN<=k}`.       (1)

The trace bound matters. Without it, the single-flag erasure construction from the bare-lift obstruction can be multiplied by N to recover rho, and its trace grows with N. It cannot be used to defeat the compactness argument with a uniformly trace-at-most-k sequence.

For an explicit dual connection, minimize `Tr[Q_N(W)sigma]` over the displayed Bose-positive constraints `Tr[Q_N(I)sigma]=1`, `Tr(sigma)<=k`. Its dual has scalars lambda and mu>=0 with

`Q_N(W)-lambda Q_N(I)+mu I>=0`,

and value `lambda-k mu`. Slater feasibility is available: mix a canonical augmented product lift of trace1 with a small positive-definite Bose-supported state normalized to contraction trace1. The latter can be chosen as the Bose identity scaled to contraction trace1 and has trace k; a sufficiently small mixture has trace strictly below k while being positive definite on Bose support. Hence the standard finite-dimensional SDP strong-duality argument applies to this support-function problem.

Setting `Y=W-(lambda-k mu)I` turns the dual constraint into

`Q_N(Y)+mu[I-kQ_N(I)]>=0`.

A strict separation of a physical state from compact K_N therefore supplies a negative witness in the trace-corrected cone. This is a theoretical separation argument, **not a computed witness or an asserted finite level for the P44 target**.

In particular, the already-known PPT SN3 state in4by5 from Krebs–Gachechiladze must be separated by some finite level of the analogous rectangular corrected hierarchy. Consequently the corrected family is not universally restricted to decomposable witnesses in all physical dimensions. This observation leaves completely open whether **N4 in4by4** has enough PPT headroom. It is a reason that the proposed bounded screen is not refuted by the all-level bare-lift lemma, not a proof that the screen will succeed.

Classical imports here are compactness in finite-dimensional matrix spaces, infinite-extendibility implies separability, strict convex separation, and SDP support-function duality with the displayed Slater point. These imports and the proposed finite-level check require independent review; no kernel or human acceptance is claimed.

## 3. Exact wrong-normalization controls

Let `Omega_2=|00>+|11>` in the first two physical levels of the4by4 space, and set

`Ymut=(15/14)I-(4/7)P(Omega_2)`.

Its trace is16 and its expectation on normalized rank-two Omega_2 is exactly

`15/14-(4/7)*2=-1/14`.

It therefore **cannot** be a valid two-block-positive witness. A correct implementation must reject it.

Let Q denote the unnormalized-singlet N4 lift. The bosonic contraction for the physical2-level projector has norm squared at most

`(2*2+N-1)/N=7/4`.

This follows from `L L^*=(4+n_selected)/4` and `n_selected<=3` on the three-spectator output. Hence

`Q(P(Omega_2)) <= (7/4)I`.

The incorrectly weakened trace-factor-one condition at mu=1 would give

`Q(Ymut)+I-Q(I)`
` =(1/14)Q(I)+I-(4/7)Q(P(Omega_2)) >=0`.

It would falsely certify the rank-two-negative Ymut. The correct factor-two condition fails, as it must by the canonical rank-two lift in the soundness proof.

Likewise, incorrectly normalizing the auxiliary singlet projector by1/2 while retaining the trace-factor2 convention, at mu=1/2, produces exactly half of the preceding wrong-factor-one positive operator:

`(1/2)Q(Ymut)+(1/2)[I-Q(I)]>=0`.

The same Ymut still has physical expectation-1/14. Thus these are fixed **negative implementation controls** for both normalization mistakes; they are not fabricated search outputs. The prepared script evaluates the wrong and correct cones, checks the required sign split, and compares all entries with its separately encoded raw tensor checker only after an exact GO.

## 4. Preparation and admission state

Both new scientific modules are complete sources, not stubs. Neither was imported, compiled, smoke-run, optimized or scientifically evaluated while preparing. Metadata inspection found an existing read-only environment with the required versions; no installation or old runtime occurred.

The concrete future screen remains exactly one target with fixed controls, two solver calls (separable control then target), one thread, cooperative internal bounds, no retries or adaptive level/input queue. The admission request correctly remains **HOLD/noGO**. A parent mathematical read/reconstruction, assessment of the finite N4 PPT-specific uncertainty above, fresh aggregate resources, and a separately pinned named GO are still required. If that cost/benefit gate is not met, no assay is run.
