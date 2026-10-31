# The finest pure actor preserves the band of any physical host

**Status: NEW AUTHOR WRITTEN GENERAL THEOREM with exact finite gauge control; UNREVIEWED / UNADOPTED.** This is an arbitrary-actor reduction, not a proof that any original source embeds. It relies on the independently unreviewed finest-pure-actor construction `frontier-20261028-finest-pure-cs-actor-v1.md`, SHA `772cf39e2d5c6aab1c127ed73edaf3e7c2e617deda8f3113b8059df19f4c83ab`, and on the displayed Rees homomorphism normal form. It does not settle SEP/R/L or the printed-product interface.

## 1. General same-band lifting lemma

Let `h:D₁→D₀` be ANY homomorphism between completely simple Rees semigroups, not necessarily onto, injective or pure. Let an arbitrary semigroup S have maps `r₁:S→D₁`, `c:S→B` such that `s↦(c(s),h(r₁(s)))` is a homomorphism into the physical product P(B,D₀), where D₀'s group acts by automorphisms α on the band B. Then there is a group action on **the same band B** and a band-coordinate map c₁ for which `s↦(c₁(s),r₁(s))` is a homomorphism into P(B,D₁). If the original map is injective, so is the lifted map.

Choose Rees coordinates `D_k=M[G_k;I_k,Λ_k;P^k]`. The standard Rees homomorphism form gives row/column maps ρ,κ, a group homomorphism `φ:G₁→G₀`, and elements `a_i,b_λ∈G₀` such that

`h(i,g,λ)=(ρ(i), a_i φ(g) b_λ, κ(λ))`,
`b_λ P⁰_(κ(λ),ρ(j)) a_j = φ(P¹_(λ,j))`.              (1)

For completeness, in normalized D₁ coordinates choose a base row i₀ and column λ₀, and put `E_i=(i,1,λ₀)`, `F_λ=(i₀,1,λ)`, `H_g=(i₀,g,λ₀)`. Homomorphisms preserve R and L, so h's rows and columns define ρ,κ. Write h(E_i)=(ρ(i),X_i,κ(λ₀)), h(F_λ)=(ρ(i₀),Y_λ,κ(λ)), and h(H_g)=(ρ(i₀),K_g,κ(λ₀)). With `p*=P⁰_(κ(λ₀),ρ(i₀))`, define `a_i=X_i p*`, `b_λ=Y_λ`, `φ(g)=K_g p*`. The identities `E_i H_g F_λ=(i,g,λ)`, `H_g H_h=H_(gh)` and `F_λ E_j=H_(P¹_(λ,j))` give (1) directly. General Rees coordinates are obtained from a normalized presentation by row/column gauge changes; the standard normal form remains (1). No normality or surjectivity of φ is assumed.

For `r₁(s)=(i_s,g_s,λ_s)` set

`c₁(s)=α_(a_(i_s)⁻¹)(c(s))`,      `β_g=α_(φ(g))`.

The latter is a genuine G₁-action on the SAME B. The D₀ group weight for s,t is, using (1),

`a_(i_s) φ(g_s) b_(λ_s) P⁰_(κ(λ_s),ρ(i_t)) = a_(i_s) φ(g_s P¹_(λ_s,i_t)) a_(i_t)⁻¹`.

Therefore

`c₁(st)=c₁(s) β_(g_s P¹_(λ_s,i_t))(c₁(t))`,

which is the full physical multiplication over D₁. If two lifted images are equal, their r₁ rows coincide and their h-images coincide. Applying the common α_(a_i) to equal c₁ values gives equal original c values; original injectivity yields equal source elements. □

## 2. Consequence for the finest pure actor

Let S be regular with actual `q:S→D` pure and CS, and let `q̂:S→D̂` be the finest pure CS quotient of the named predecessor. Suppose S has ANY faithful physical host with band B and actor D₀. Its actor map `r:S→D₀` is pure. Its image T is a regular subsemigroup of D₀ and hence CS. The predecessor gives `r=h q̂` for a homomorphism `h:D̂→T⊆D₀`. Apply §1 directly: S embeds into a physical product `P(B,D̂)` with the **same B**, allowing a possibly different D̂ group action. No rectangular factor, band enlargement, finiteness or actor-surjectivity is required.

Consequently, for any fixed class V of bands and any cardinal κ, S has a faithful physical V-band-by-any-CS host with at most κ band elements iff it has one over D̂ with at most κ band elements. The reverse direction is immediate. If a canonical V-band product over q̂ is defined with its usual universal mapping property, existence is equivalently injectivity of that canonical map; this last statement explicitly imports that canonical construction, rather than proving SEP. The same-band theorem works even when V is not a variety because B itself is unchanged.

For the 68-source, D̂ is the 12-actor and this result explains the pinned optimal band size8; its actual coarsest actor D8 has fixed-actor optimum10. No inconsistency follows: moving toward the **finest** actor preserves B, whereas previous transport toward the **coarsest** actual actor can require a rectangular band enlargement.

## 3. Exact finite gauge control and limits

`frontier-20261028-pure-actor-same-band-lift-checker-v1.py`, SHA-256 `b20ad285aa6ed99947981661d4dbf9849b3a7e98d76d4c6697cd049fe4d633dc`, ran in the Python eval kernel before Wed Oct 28 22:20:54 PDT 2026. It verifies all 64 source products for an injective nononto CS actor homomorphism `D₁` of size8 into D₀ of size54, with C₂ mapped to a nonnormal subgroup of S₃ and nontrivial occupied-row gauges; the same six-element left-zero band carries the original and lifted models. This finite control does not prove the universal algebra or independently review the pure-actor theorem.

The theorem does not pay the original same-q̂ idempotent separation, compare a printed product convention, prove any source embeds, or establish novelty. A disjoint review must verify the Rees normal-form/gauge algebra, original-host injectivity implication, and every assumption of the finest-actor predecessor. All outputs remain author-written and unadopted.
