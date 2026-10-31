# An infinite CS-parameter family with exact minimum band 8

**Status: NEW AUTHOR WRITTEN CONDITIONAL FAMILY based on the pinned finite source/host; UNREVIEWED / UNADOPTED.** This is a family of positive original-Q1 instances, not an all-source theorem. It uses the original physical product convention and does not assert novelty or settle printed-convention questions.

Let S₀ be the specific 68-source in `frontier-20261028-quotient68-global-band-optimum-v1.md`, SHA `513a404929f7c68b86256ac6db2c7cf86ddab3f0fd29a67c402f409d11ffc592`. For **any nonempty completely simple semigroup D**, finite or infinite, put `S=S₀×D`. Subject to the pinned S₀ finite witness, all the following hold:

1. S is regular, weakly E-unitary and locally r-orthodox; it is neither orthodox nor locally inverse.
2. S embeds in a physical seminormal-band-by-CS product using a band with exactly 8 elements.
3. No faithful physical host over any CS actor can use fewer than 8 band elements, even if the band need not be seminormal.
4. S admits no faithful physical host over any CS actor using a **globally regular** band.

Proof. Fix any idempotent d∈D. The map `x↦(x,d)` embeds S₀ in S, so S inherits its explicit nonorthodox pair and non-locally-inverse local-corner witness. A completely simple semigroup is regular and each of its local monoids is a group; the finite direct product of regular locally-r semigroups remains regular and locally-r. Weak E-unitarity is inherited by products: a natural-order witness to an idempotent below an element projects to such a witness in each factor, and every completely simple semigroup has equality as its natural order on idempotents below arbitrary elements. Thus both factors force idempotence of the corresponding element.

The pinned finite host embeds `S₀→P(B₈,D₁₂)`, with B₈ seminormal. The regrouping isomorphism

`P(B₈,D₁₂)×D ≅ P(B₈,D₁₂×D)`

uses the direct-product CS Rees matrix and lets the second actor's local group act trivially on B₈. Hence S embeds in the right side and has a faithful 8-band host.

The eight distinct idempotents `F=[0,8,16,24,36,44,52,60]` of S₀ have 0 as a common lower bound. Their products with d are eight distinct idempotents of S, all above `(0,d)`. Under any CS actor homomorphism, idempotent natural order is equality, so these eight values share one actor. A faithful physical host must assign them eight distinct band coefficients. This proves the universal band lower bound 8 and, with the displayed host, its sharpness for every D.

Finally, the explicit source relations `(ef=f, fe=e, ae=af, e=stv, f=sv=utv)` from `frontier-20261028-quotient68-all-cs-direct-obstruction-v1.md`, SHA `9092df28a55693c396ee5797b2687eb457265b139087d1119d69eb0f36e35043`, remain true after pairing every participating element with d. The source idempotents remain distinct. Its transport-free arbitrary-CS proof applies to S and excludes every globally regular-band host, without regard to the size or structure of D. □

The family is genuinely infinite by taking, for example, D to range over groups of different finite orders, and also includes infinite D. The actor-refined 8-band host, finite source data and all-actor proof are the named same-author inputs; no independent verification of them is implied. No claim is made about the minimum **whole** host cardinality for these products, their actual syntactic actors, or every weakly-E locally-r source.
