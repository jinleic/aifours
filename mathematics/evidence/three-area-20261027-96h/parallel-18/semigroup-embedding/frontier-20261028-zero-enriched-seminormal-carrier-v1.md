# The successful six-band carrier is a zero-enriched symmetric band

**Status: NEW AUTHOR WRITTEN STRUCTURAL IDENTIFICATION with exact finite table check; UNREVIEWED / UNADOPTED.** This gives a documented replacement for the B_I-power-only strategy falsified by S68. It does not claim B_I with zero is a universal carrier for all original sources.

## 1. Exact identification and action

The six-element SN band C used in the pinned faithful C⁵ host of S68 is isomorphic to the earlier five-band B5 with an absorbing zero adjoined. In the B5 labels from `frontier-20261028-ambiguous-source-local-band-host-v1.md`, the isomorphism from labels `(0,1,2,3,4,new-zero)` to C labels is

`(5,2,0,3,1,4)`.

An exact Python eval-kernel check compared all36 products and verified that the extended B5 involution `(1 3)(2 4)` fixing the new zero corresponds to C's involution `(0 1)(2 3)` fixing4,5. Thus C is not an unrelated exotic band: it is precisely **B_(2) with zero**, after the explicit relabelling. This reinterprets, without modifying, the pinned six-band witness.

For arbitrary I, adjoin a new absorbing zero to the symmetric B_I and write B_I⁰. Every permutation action on B_I extends by fixing zero. The seminormal identity is content-regular: both sides contain exactly the same variables. If a variable is assigned zero, both sides evaluate to zero; otherwise B_I's identity applies. Hence B_I⁰ is seminormal, and any group still acts faithfully through its regular action on I. Its old local corners are their former regular corners with an absorbing zero adjoined; the new zero corner is trivial, so it is locally regular directly as well.

The quasiidentity Q from `frontier-20261028-symmetric-carrier-universal-obstruction-v1.md`, SHA `356d0cadbee7b1f54b530543945a5f67ccb09c063b08d6dcd89c699d09831acd`, fails in B_I⁰ for |I|≥2: choose two distinct v_i,v_j as E,F, choose any u_k as B, and choose A to be the new zero. Then EF=F,FE=E,EB=E,FB=F and AE=AF=0 while E≠F. The enriched carrier therefore escapes the exact obstruction that all ordinary B_I powers satisfy.

## 2. Same identities, different quasivariety

For any I, B_I contains a two-element semilattice `{u_i,v_i}`. Therefore every semigroup identity valid in B_I has the same variable content on both sides: otherwise specialize to that semilattice, assigning0 to a variable missing on the other side and1 elsewhere. As a result, adjoining zero preserves EVERY identity of B_I, not just the SN identity. Conversely B_I is a subband of B_I⁰. Thus

`var(B_I⁰)=var(B_I)`.

There is also an explicit HSP construction: on `B_I×SL₂`, collapse the ideal `B_I×{0}` to one zero and retain `B_I×{1}` as B_I. This is a homomorphism onto B_I⁰. Because SL₂ is a subband of B_I, the source band is a subband of B_I². Hence B_I⁰ is a homomorphic image of a subband of B_I². For an arbitrary group action, the action on B_I×SL₂ with trivial second coordinate preserves that ideal and descends to B_I⁰; no claim is made that the chosen SL₂ subband of B_I is invariant under all permutations.

Despite the SAME variety of identities, B_I⁰ is not in the subband/product closure `SP({B_J}∪rectangular bands)` for |I|≥2, because Q holds throughout that closure and fails in B_I⁰. Thus homomorphic images of the model bands matter, and an SP-only finite model search can miss hosts even when it searches powers of an identity-generating carrier. No assertion here proves that the B_I variety equals all seminormal bands.

## 3. Consequence for the genuine one-sided frontier

The successful six-band host and the optimal eight-band source-fibre host of S68 now have a concrete carrier interpretation: the former is a power of B_(2)⁰, and the latter embeds as a band in that power by restriction to a pure idempotent actor fibre. Thus the eight-band lies in HSP(B5), while Q proves it cannot lie in SP(B5 plus rectangular bands). This explains the earlier model-family failure without changing any source or host result.

The needed future question is not 'can arbitrary group actions on B_I powers rescue Q?'—the direct obstruction proves no. It is whether appropriately zero-enriched/quotient carriers or a broader contextual construction can represent every matching right-zero or left-zero coextension. That universal embedding is **not proved**. The identification and direct action/product check are same-author exact evidence only; all source, universal quotient and host claims remain pending independent review, with no novelty or formal-proof assertion.
