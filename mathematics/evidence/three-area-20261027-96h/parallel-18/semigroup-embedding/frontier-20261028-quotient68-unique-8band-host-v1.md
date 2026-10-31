# Uniqueness of the 68-source's optimal eight-band realization

**Status: NEW AUTHOR WRITTEN + literal exact finite replay; UNREVIEWED / UNADOPTED.** This strengthens the finite host record `frontier-20261028-quotient68-global-band-optimum-v1.md`, SHA `513a404929f7c68b86256ac6db2c7cf86ddab3f0fd29a67c402f409d11ffc592`. It is a fixed-source result, not a universal uniqueness claim.

## 1. Saturation principle

Let `r:S→D` be pure and onto CS, and let the fibre F over an idempotent actor d have m elements. F is a band. In every faithful physical host over r, F's band coefficients are pairwise distinct; hence |B|≥m. If |B|=m, F exhausts B and its coefficient map is a band isomorphism, because d's physical self-weight is the identity. Thus, after the unique relabelling that identifies each coefficient with its source element in F, the band table is fixed. Possible actor-group actions are exactly homomorphisms `G→Aut(F)`, and all remaining source coefficients are solutions of the finite multiplication constraints.

## 2. Exact uniqueness for the refined 12-actor

For S68 and its finest/refined actor `r₁₂`, the fibre

`F=[0,8,16,24,36,44,52,60]`

has eight idempotents; every faithful eight-band host over r₁₂ is thus, after fibre relabelling, a solution over exactly the 8×8 fibre table. Enumerating all 8! permutations of F shows exactly two band automorphisms, both involutions:

`id=(0,1,2,3,4,5,6,7)`,
`τ=(0,1,5,6,7,2,3,4)`.

Since the actor group is C₂, these are the only two actions. The pinned exact trace file `frontier-20261028-quotient68-8band-unique-arc-traces-v1.json`, SHA-256 `83596ecfe35abb5a71367aa4dad655e4cfcb1c5b57279bf97a7f677906beb7bd`, supplies sound domain-pruning steps for the source multiplication equations with the eight fibre values fixed. The identity action reaches an empty domain after 97 reductions. For τ, 132 reductions force **every one of the 68 source coefficient domains to a singleton**. Every genuine solution must survive each reduction; therefore there is at most one. The resulting assignment is exactly the previously pinned 8-band host, and the verifier checks all 4,624 equations and injectivity. Therefore the faithful minimum-band host over the fixed refined actor is unique up to the canonical fibre-based band relabelling.

`frontier-20261028-quotient68-8band-unique-replay-v1.py`, SHA-256 `29873dc94772bed32ee322f449bfd979d7e976ccd03787fa121275654257cdf1`, executed in the Python eval kernel before Wed Oct 28 22:27:16 PDT 2026. It independently recomputes all 8! automorphisms, replays each stated domain reduction using the literal source table, verifies the empty/singleton conclusions and checks the unique solution's products and injectivity. It does not import Z3. It shares the author's source and traces, so independent source/certificate review is still required.

## 3. Arbitrary actor qualification

The separate actor-image classification `frontier-20261028-quotient68-actor-image-classification-v1.md`, SHA `ab1ac0cf15127a7fd5bb0b5545eff543cec8c6c55dc3e0a213c079791a777749`, says that the actor image of any faithful host is D₈ or D₁₂. The fixed D₈ actor requires at least ten band elements; hence any eight-band host's **actor image** must be D₁₂. Conditional on the independently unreviewed same-band Rees restriction/gauge, such a host restricts to D₁₂ on the same B and is therefore equivalent, after actor isomorphism and fibre relabelling, to the unique realization above. This does NOT classify arbitrary unused elements of a larger ambient actor or its action outside the source actor image.

No all-source Q1 or whole-host uniqueness is asserted. The finite identities, source q/refined actor, congruence traces and gauge remain pending independent review; no formal proof or novelty is claimed.
