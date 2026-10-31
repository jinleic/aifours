# An exact original-source family that needs BOTH sides of SN

**Status: NEW AUTHOR WRITTEN FAMILY based on pinned finite witnesses; UNREVIEWED / UNADOPTED.** This is a sharp target-variety boundary and exact all-actor band-size result, not a counterexample to full Q1. It uses no actor-transport theorem for its lower bound or nonembedding claim.

## 1. The source68 has no LEFTSN-band host over any actor

In any LEFT-seminormal band, `abc=abcac`. If E,F satisfy `EF=F`, `FE=E` and have a common right identity B (`EB=E`, `FB=F`), the leftSN identity at `(a,b,c)=(E,F,B)` gives

`F=EFB=EFBEB=FEB=EB=E`.

Thus no distinct R-pair of a leftSN band can have a common right identity.

Now the pinned original S68 has distinct idempotents e=37,f=61 and source a=0,b=25 with `ef=f,fe=e,eb=e,fb=f,ae=af`. Under ANY CS actor map r, the R equations force r(e),r(f) to share a row, and ae=af forces their columns equal. A CS cell has a unique idempotent, so their actors are identical d. For any physical host, its band coordinates E,F therefore satisfy EF=F,FE=E; the products eb and fb have the SAME group weight w, giving a common right identity `B=α_w(c_b)`. If the band is leftSN, the preceding identity forces E=F and the physical images agree. Hence **S68 has no faithful leftSN-band-by-CS host for any actor or action**.

Dually S68^op has no faithful rightSN-band-by-CS host. In contrast the pinned eight-element band B8 is RIGHTSN: an exact eval-kernel check exhausts all512 rightSN substitutions and finds no failure, while its leftSN law fails at(1,3,6). The already pinned host `S68→P(B8,D12)` therefore witnesses the strict orientation, and the opposite host uses the leftSN band B8^op. These statements do not confuse rightSN with right-regular bands: B8 is not globally regular.

## 2. Mixed products and exact minimum band cardinality

For any integers a,b≥0 with d=a+b≥1, put

`S_(a,b)=S68^a × (S68^op)^b`.

These are regular weakly-E locally-r original sources. They have 68^d elements; each has nonorthodox and non-locally-inverse slices. The product of the pinned finite hosts embeds S_(a,b) into a physical host with

`band B8^a × (B8^op)^b` of size `8^d`,
`actor D12^a × (D12^op)^b` of size `12^d`.

For the universal lower bound, each S68 factor has eight distinct source idempotents in the upper cone F=[0,8,16,24,36,44,52,60] above source0, and the opposite has the same order. Their direct-product cone has exactly8^d distinct idempotents above a common source idempotent. Under EVERY CS actor map those idempotents all have the same actor value, because its idempotent natural order is equality. A faithful physical host must assign them8^d distinct band coefficients. Therefore

`min_(ALL CS actors and all bands) |band| = 8^d`.

This lower bound is independent of the actor, group action, source generator count and the pure-CS quotient classification. It applies even to arbitrary non-SN bands, while the displayed optimal band is SN.

If a,b≥1, the source has a slice isomorphic to S68 and another slice isomorphic to S68^op (fix idempotents in all other coordinates). A leftSN-band physical host would restrict to a forbidden host of S68; a rightSN-band host would restrict to a forbidden host of S68^op. Thus these MIXED original sources have **no host using either one-sided seminormal variety alone**, despite having an explicit fullSN host and an exact optimal band size. The original full target cannot generally be replaced by either one-sided target.

## 3. Scope and evidence

The finite B8/D12 source witness and exact cone lower bound are pinned in `frontier-20261028-quotient68-global-band-optimum-v1.md`, SHA `513a404929f7c68b86256ac6db2c7cf86ddab3f0fd29a67c402f409d11ffc592`; original source-class checking must include the full-natural-order erratum `frontier-20261028-natural-order-weu-audit-erratum-v1.md`, SHA `801f699bb640bd1e58eed095779c05b882e7d9eddd0ea1c470b522ecbc345c28`. This family is proved symbolically by product laws and the literal single-source witness; no 68^d source multiplication tables were generated or verified by enumeration.

The supplemental literal checker `frontier-20261029-source68-essential-one-sided-checker-v1.py`, SHA `27e335b23fdce6eca3eba5d9dc4d5d234a28db0458e8b1802923be6eb9208a38`, completed before Thu Oct29 01:12:25 PDT2026. It verifies B8's512 rightSN substitutions and the stated leftSN failure, all source obstruction equations, and EVERY4,624 opposite-source physical product plus injection. For the C₂ actor, the opposite host uses actor `(λ,g,i)`, transposed sandwich matrix, band B8^op, and coefficient `α_g(c_s)`; the checker verifies those exact formulas rather than treating an opposite physical product as unchanged.

The case a=b=1 has 4,624 source elements and an optimal64-element band, with the displayed144-actor giving a9,216-element whole host. That is NOT a minimum whole-host claim: its actual-actor product10×10 band yields another host of size6,400. The source cardinalities and host sizes are exact arithmetic, not executed large-source census.

All proofs and finite inputs remain same-author unreviewed; no all-source Q1/Q2 solution, independent/formal verification or novelty is claimed.
