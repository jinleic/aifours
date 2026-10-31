# Nested physical hosts flatten to ONE host with the SAME band

**Status: NEW AUTHOR WRITTEN tool theorem with explicit formula and a complete finite replay; UNREVIEWED / UNADOPTED. Associativity of such products is plausibly classical in e-variety language; NO novelty is claimed.** It supplies a safe way to iterate extensions without enlarging the band variety. It does not solve originalQ1/Q2.

## 1. Statement at its exact (gauge-free) scope

Let B be a band acted on by a group K, `D₁=M[K;I₁,Λ₁;P₁]`, and let a group H act on I₁, Λ₁, K and B such that:

- `h·P₁(λ,i)=P₁(hλ,hi)` (H permutes rows/columns and acts on K by automorphisms);
- `h∘α_k∘h⁻¹=α_(h(k))` on B, so `α_(k,h)=α_k∘h` is an action of `G=K⋊H`.

Then `θ_h(b,(i,g,λ))=(h(b),(hi,h(g),hλ))` acts by automorphisms on the physical host `P(B,D₁)`. For any `D₂=M[H;I₂,Λ₂;P₂]`, the nested product `P(P(B,D₁),D₂)` is ISOMORPHIC to the single physical host `P(B,D)`, with

`D=M[G; I₁×I₂, Λ₁×Λ₂; Q]`, `Q((λ,u),(i,j))=(P₁(λ,P₂(u,j)i), P₂(u,j))`,

via the bijection

`((b,(i,g,λ)),(j,h,u)) ↦ (b, ((i,j),(g,h),(h⁻¹λ,u))).`

The transformed column `h⁻¹λ` is the essential bookkeeping step.

## 2. Written proof

Write x and y with inner coordinates `(i,g,λ),(i',g',λ')` and outer coordinates `(j,h,u),(j',h',u')`, and put `w=hP₂(u,j')`. The nested product is

`((b·α_(gP₁(λ,wi'))(w(c)), (i,gP₁(λ,wi')w(g'),wλ')), (j,wh',u')).`

On the target side, with `γ=(g,h)` and `p=P₂(u,j')`, equivariance of P₁ gives `γQ=(g·h(P₁(h⁻¹λ,pi')),hp)=(gP₁(λ,wi'),w)`. Therefore the target band coefficient is `b·α_(gP₁(λ,wi'))(w(c))`, the group coordinate is `(gP₁(λ,wi')w(g'),wh')`, the row is `(i,j)`, and the column is `((wh')⁻¹wλ',u')=(h'⁻¹λ',u')`. These are exactly the flattened nested coordinates. The map is bijective because `(h,λ)` and `(h,h⁻¹λ)` determine each other. □

Corollary. If a semigroup T embeds H-equivariantly, by this gauge-free coordinate action, into `P(B,D₁)` with B∈V, then every subsemigroup of `P(T,D₂)` embeds into a physical V-band-by-CS host with the SAME band B. In particular RIGHTSN, LEFTSN and SN hosts are closed under such iterated extensions. Gauged H-actions on D₁ (with row/column gauge cocycles) are NOT covered by this statement and would need a separate normalization argument.

## 3. Exact finite replay

`frontier-20261029-iterated-Pastijn-flattening-checker-v1.py`, SHA `5885de9a5786dec155962e9f8319aa927d3a27b472bb3bd460b247f890330028`, completed in the Python eval kernel before ThuOct29 03:59:28 PDT2026. It uses the seven-element NON-GLOBALREG RIGHTSN band B_{0,1,2}, K=C₃ acting by rotation of each three-element layer, H=C₂ acting by inversion/reflection, nonabelian G=S₃, a nontrivial C₃-valued sandwich `P₁=[[0,1],[2,0]]` with nontrivial H-row/column permutations, and the twisted D₂ sandwich. It verifies the band, compatibility and semidirect action laws, that θ is an automorphism of the inner host, that the map is a bijection on all672 elements, and ALL451584 nested products match the single-host formula. The final actor has96 elements, four rows, four columns and group S₃.

This is an auxiliary construction lemma, not a source-class theorem, an independent review or a formal proof.
