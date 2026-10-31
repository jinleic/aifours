# Every finite pure-CS quotient has a completely simple section

**Status: NEW AUTHOR WRITTEN STRUCTURAL THEOREM; UNREVIEWED / UNADOPTED.** Likely classical; no novelty is asserted. A section of an actor quotient does NOT make the source a physical product or solve its band cocycle. This statement explicitly separates those obligations.

## 1. Exact theorem

Let S be any nonempty FINITE semigroup, and let `r:S→D` be an onto idempotent-pure homomorphism to a completely simple D. Then there exists a completely simple subsemigroup `T⊆S`, contained in the minimum ideal of S, such that `r|T:T→D` is an isomorphism. In particular r is a split epimorphism and the induced `σr:S→T`, with σ=(r|T)⁻¹, is a semigroup retraction.

The finite source need not be assumed regular, although the original source class is regular. We make no infinite-source claim without a completely simple minimum ideal.

## 2. Proof

The minimum nonempty ideal I of a finite semigroup is completely simple (the singleton zero case is included as the one-element group/CS semigroup). This is the named standard finite minimal-ideal/Rees–Suschkewitsch fact. The image r(I) is a nonempty ideal of D because r is onto: for d=r(s), `d r(i)=r(si)` and `r(i)d=r(is)` lie in r(I). Simplicity gives r(I)=D. The restriction `h:I→D` is onto and pure.

For ANY onto pure homomorphism between CS semigroups, the induced map from each local group is an isomorphism. Injectivity: equal images of x,y in one group make `h(xy⁻¹)` idempotent; purity makes xy⁻¹ the group identity. Surjectivity: for a chosen cell idempotent e and any z in the target local group, lift z to x∈I; then exe lies in eIe and maps to z. This proof works for infinite groups as well.

In Rees coordinates h induces onto row and column maps. Select one source row above each target row and one source column above each target column. Let T be the subsemigroup of I consisting of ALL group elements in those selected cross-cells. It is a full Rees submatrix semigroup, hence CS. Its row/column maps to D are bijective and each H-cell group map is bijective by the previous paragraph. Therefore `h|T` is a bijective homomorphism, and its inverse is a section σ:D→S. This proves the theorem. □

More generally the same proof works for any (possibly infinite) S having a completely simple ideal I whose r-image is D, with row/column choices allowed. The finite theorem is unconditional at the displayed pure-CS quotient assumptions.

## 3. Scope of the splitting

No section element is asserted to be an identity for the rest of S. Indeed T lies in the minimum ideal, so every product with one factor in T remains in that ideal; outside elements generally cannot be written as `e·σ(d)` or `σ(d)·e`. Thus the section does NOT prove factorizability, a global action by source multiplication, or a band-by-CS product realization.

For the pinned S68, the refined pure D12 actor has a literal section at band coefficient0: source indices0,…,7 and32,…,35 represent its12 actors, and the pinned host/actor tables check their multiplication. The actual D8 quotient also has a section on source indices0,…,7. Nevertheless S68 has no trivial-action physical host over ANY actor, by the exact band-hom collapse certificate in `frontier-20261029-trivial-action-cryptogroup-boundary-v1.md`, SHA `97ccbee3420d379131a6236fa9744342eef03766ac84cb1646af8101008d8fc6`. Thus splitting is not a substitute for the nontrivial matching one-sided cocycle.

The theorem adds a useful finite reduction, not an acceptance of any source packet, host or originalQ1/Q2 solution. Independent review of the finite minimal-ideal fact, pure local-group maps, Rees cross-cell restriction and section/ideal limitations is required. No formal verification or novelty is claimed.
