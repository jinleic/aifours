# Compact whole-host transport along any pure onto CS map

**Status: NEW AUTHOR WRITTEN GENERAL THEOREM with exact nonabelian finite control; UNREVIEWED / UNADOPTED.** This extends the coordinate-projection-only `frontier-20261028-compact-actor-forgetting-v1.md`, SHA `76abc0c22c6119a908b9ac36f7b5ed00192a92a0c05f86003189416562c6c198`, to arbitrary row/column gauges and arbitrary groups. It is prospective evidence, not a retroactive disposition of any historical f95 review. It does not solve original SEP/R/L or Q1.

## 1. Exact theorem

Let `h:D₁→D₀` be an **onto idempotent-pure** homomorphism of completely simple semigroups, and let `P(B,D₁)` be any physical band-by-CS product with D₁'s group acting by automorphisms on B. Then the ENTIRE product embeds into `P(R×B,D₀)` for an explicitly constructed rectangular band R, with a D₀-group action on the same B transported through the local-group isomorphism. This holds for finite or infinite bands, actors and groups.

Choose Rees coordinates, group homomorphism φ and gauges as in the direct derivation in `frontier-20261028-finest-actor-same-band-lift-v1.md`, SHA `fa8bcc7beb069fbe873380429415f9c90723420a241abd078fe206973d1d8c3c`:

`h(i,g,λ)=(ρ(i), a_i φ(g)b_λ, κ(λ))`,
`b_λ P⁰_(κ(λ),ρ(j)) a_j=φ(P¹_(λ,j))`.                   (1)

Surjectivity of h makes ρ and κ onto. Purity makes the local group map φ injective; it is also onto: for a chosen cell idempotent e, any element of the target local group has a source lift x, and `e x e` lies in the source local group and maps to it. Thus φ is a group isomorphism, with no finiteness assumption. Define the target G₀ action on B by `γ_g=α_(φ⁻¹(g))`.

Choose sets J,K and labels `j:I₁→J`, `k:Λ₁→K` injective within each fibre of ρ,κ, and let R=J×K be rectangular. Let G₀ act trivially on R. Define

`Φ:(b,(i,g,λ)) ↦ (((j(i),k(λ)), γ_(a_i)(b)), h(i,g,λ))`.  (2)

For a second source actor `(j,h,μ)`, its target action weight is, by (1),

`a_i φ(g)b_λ P⁰_(κ(λ),ρ(j)) = a_i φ(gP¹_(λ,j)) a_j⁻¹`.

Consequently the target B product of `γ_(a_i)(b)` and the transformed second factor is

`γ_(a_i)( b · α_(gP¹_(λ,j))(b') )`,

and the rectangular label product is `(j(i),k(μ))`. This is precisely Φ of the source product. If two Φ-images agree, the coarse row plus j-label recovers i, the coarse column plus k-label recovers λ, and the target group coordinate plus injectivity of φ recovers g; applying `γ_(a_i⁻¹)` recovers b. Thus Φ is an injective homomorphism of the entire product. □

For finite actor row/column sets, take `|J|=max_(i₀)|ρ⁻¹(i₀)|`, `|K|=max_(λ₀)|κ⁻¹(λ₀)|`; the band grows by at most their product. For arbitrary infinite sets, J=I₁,K=Λ₁ is always valid. Rectangular bands and direct products preserve the seminormal and globally regular band identities, so the construction stays in either of those specific varieties whenever B does. The factor bound is universally sharp by the rectangular-band-to-one-actor example in the predecessor.

## 2. Exact nonabelian control and scope

`frontier-20261028-compact-pure-onto-gauge-checker-v1.py`, SHA-256 `70cbf4dce8f8f519d2590f92cde6cc15fb2bd6d254974efb1d5174831584c22a`, ran in the Python eval kernel before Wed Oct 28 22:50:43 PDT 2026. It uses the nonabelian group S₃, an onto pure Rees map from a 72-element actor to a 24-element actor with noncommuting row/column gauges, and its 8-element Boolean semilattice action. It checks all 5,184 actor products/purity, injectivity of the entire 576-element source host into the 768-element target host, and all 331,776 whole-host product equations. This control does not prove the general result or independently review the Rees normal form.

The theorem is only for **onto** pure actor homomorphisms. It makes no assertion about nononto maps or their nonnormal subgroup coinduction; those remain the separately reviewed scope in `frontier-20261028-pure-CS-coinduced-whole-host-v1.md`, SHA `b129099ed4ae481a0d212ec68c5271b91b700757721d8c41d712b55e9755bad2`. Nor does it establish that the canonical map is injective, resolve any original Q1/Q2, or claim novelty/formal/independent verification.
