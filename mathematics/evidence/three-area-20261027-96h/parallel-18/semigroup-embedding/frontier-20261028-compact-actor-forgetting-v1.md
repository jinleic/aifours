# Compact, sharp rectangular encoding from refined to coarser actors

**Status: NEW AUTHOR WRITTEN WHOLE-HOST EMBEDDING with exact finite control; UNREVIEWED / UNADOPTED.** This gives a direct, coordinate-projection case of actor transport with an explicit factor bound. The application to arbitrary original hosts is conditional on the separately reviewed finest-actor/same-band lift candidates. It does not prove canonical SEP or Q1.

## 1. Explicit general encoding

Let `D₁=M[G;I₁,Λ₁;P¹]`, `D₀=M[G;I₀,Λ₀;P⁰]`, with onto row/column maps `ρ:I₁→I₀`, `κ:Λ₁→Λ₀` and duplicate sandwich entries

`P¹_(λ,i)=P⁰_(κ(λ),ρ(i))`.

Thus `h(i,g,λ)=(ρ(i),g,κ(λ))` is an onto pure CS homomorphism. Let G act by automorphisms α on a band B. Choose sets J,K and labels `j:I₁→J`, `k:Λ₁→K` that are injective **within each fibre** of ρ and κ respectively. Give the rectangular band R=J×K multiplication `(j,k)(j',k')=(j,k')`; G acts trivially on R and by α on B.

The map

`Φ:(b,(i,g,λ)) ↦ (((j(i),k(λ)),b), (ρ(i),g,κ(λ)))`

is an injective homomorphism of the **entire** physical product `P(B,D₁)` into `P(R×B,D₀)`. Indeed, both products use the identical group weight `gP⁰_(κ(λ),ρ(i'))`; rectangular multiplication retains the left label j(i) and the right label k(λ'), matching the D₁ product. Equality of target values recovers the coarse row/column and labels, hence the original row/column, and also g and b. There is no group coinduction, nonnormal-subgroup condition, or source-specific assumption. If B is seminormal, R×B is seminormal because rectangular bands are seminormal and identities are preserved by products. □

For finite actors one can take `|J|=max_(i₀∈I₀)|ρ⁻¹(i₀)|` and `|K|=max_(λ₀∈Λ₀)|κ⁻¹(λ₀)|`. Hence the band factor grows by at most their product. The trivial infinite choice J=I₁,K=Λ₁ always works; no finite-cardinality claim is made for unbounded infinite fibres.

## 2. Finest-to-actual consequences and sharpness

For a regular source with actual q pure CS, the finest actor q̂ of `frontier-20261028-finest-pure-cs-actor-v1.md`, SHA `772cf39e2d5c6aab1c127ed73edaf3e7c2e617deda8f3113b8059df19f4c83ab`, has exactly the coordinate-projection form above. Combine §1 with the separately unreviewed SAME-band arbitrary-to-finest lift `frontier-20261028-finest-actor-same-band-lift-v1.md`, SHA `fa8bcc7beb069fbe873380429415f9c90723420a241abd078fe206973d1d8c3c`: any faithful SN host over any CS actor yields one over actual q, with at most `r_max c_max` times as many band elements in the finite case. This is a new route to the actual-actor interface, not a review or retroactive change of any historical transport verdict.

The factor bound is sharp in general. Let S be a rectangular band on r×c elements, r,c≥1. Its syntactic idempotence quotient q is the one-element semigroup, and its finest pure CS actor is S itself. A singleton band hosts S over that actor. Over the one-element actor, any faithful host must have at least rc band elements, and the rectangular band itself realizes that. Here `r_max=r`, `c_max=c`, so the factor rc cannot be improved universally.

## 3. Concrete 68-source control

For the pinned S68, the finest actor D₁₂ maps to actual D₈ by leaving rows fixed and merging two of three columns. Thus `r_max=1`, `c_max=2`; the pinned 8-band/D₁₂ host yields a 16-band/D₈ host by this construction. `frontier-20261028-refined-to-actual-compact-checker-v1.py`, SHA `d134b1b70753de8bbd8a3c93533d32f80d13aa1dcda6e0b6cc8a912d985372f9`, ran in the Python eval kernel before Wed Oct 28 22:36:57 PDT 2026. It directly checks all 4,624 source multiplication equations and all 256 same-q injectivity pairs for the displayed right-zero-2×B8 band. It does not enumerate the entire band or independently review the algebra.

The bound is not always optimal for a particular source: the separately replay-certified S68 minimum over actual q is 10, smaller than the constructed 16. All finite data, source hypotheses and the predecessor universal results remain same-author and unreviewed. No all-source embedding, independent/formal proof or novelty is claimed.
