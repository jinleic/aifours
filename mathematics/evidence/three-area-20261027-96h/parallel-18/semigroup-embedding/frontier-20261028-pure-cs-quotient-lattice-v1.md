# Pure CS quotient kernels are a product of partition lattices

**Status: NEW AUTHOR WRITTEN GENERAL THEOREM; UNREVIEWED / UNADOPTED.** This builds on `frontier-20261028-finest-pure-cs-actor-v1.md`, SHA `772cf39e2d5c6aab1c127ed73edaf3e7c2e617deda8f3113b8059df19f4c83ab`. It classifies pure completely simple quotients under that theorem's hypotheses; it does not establish the original embedding or the canonical band SEP/R/L conditions.

## 1. Statement

Let S be regular, and assume its actual idempotence-context quotient `q:S→D=M[G;I,Λ;P]` is onto, pure and completely simple. Let `q̂:S→D̂=M[G;R,C;P̂]` be the finest pure CS quotient from the predecessor, with `ρ:R→I`, `κ:C→Λ` its row and column projection maps and `P̂_(C,R)=P_(κ(C),ρ(R))`.

For EACH equivalence relation `~R` on R whose classes lie within fibres of ρ, and EACH equivalence relation `~C` on C whose classes lie within fibres of κ, define

`D_(~R,~C)=M[G;R/~R,C/~C;P']`,
`P'_([C],[R])=P_(κ(C),ρ(R))`,
`q_(~R,~C)(s)=([R_s],g_s,[C_s])`.

These maps are all onto, pure, completely simple quotients of S. Conversely, **every** onto pure CS quotient of S is uniquely S-compatible-isomorphic to precisely one such quotient. Ordered by kernel inclusion, the pure-CS quotient kernels form the direct product of the partition lattices of the individual fibres `ρ⁻¹(i)` and `κ⁻¹(λ)`.

For finite S the exact number of pure CS quotient kernels is

`∏_(i∈I) Bell(|ρ⁻¹(i)|) · ∏_(λ∈Λ) Bell(|κ⁻¹(λ)|)`,

where Bell(k) counts set partitions. Empty fibres do not occur because q is onto.

## 2. Construction and purity

The matrix P' is well-defined because the relations do not mix distinct q rows or distinct q columns. The map `D̂→D_(~R,~C)` projects rows and columns and leaves g unchanged; it is an onto Rees homomorphism. It is pure: idempotence is `g=(P'_[C],[R])⁻¹`, the same condition as in the source cell. Its composition with the onto pure q̂ gives the displayed onto pure quotient. The special case of equality partitions is q̂; the coarsest allowed partitions give q.

## 3. Exhaustion of all pure CS quotients

Let `r:S→T` be any onto pure CS quotient. By the predecessor, `q=f r` for an onto pure map `f:T→D`, and `r=h q̂` for an onto pure `h:D̂→T`. Define R~R R' iff their h-images have the same Rees row, and C~C C' iff their h-images have the same Rees column. These are well-defined, and they refine the fibres of ρ,κ because f maps each T row/column to a definite D row/column. Homomorphisms between CS semigroups preserve row and column relations.

Define a coordinate map

`Ψ:T→D_(~R,~C)`,  `Ψ(t)=([row(t)], group-coordinate of f(t), [column(t)])`.

Here `[row(t)]` denotes the unique ~R-class of q̂-rows mapping to that T-row, and similarly for columns. Every cross-cell of T exists. The predecessor's pure-onto-CS lemma shows f restricts to an isomorphism from EACH T cell group onto the corresponding D cell group: injectivity follows by purity, and surjectivity by lifting a target group element x and sandwiching a lift by the chosen cell idempotent. Thus Ψ is bijective cell by cell. It is a homomorphism: rows/columns multiply in the Rees way, and the middle coordinate is the group coordinate of `f(t₁)f(t₂)`, namely `g₁P_(κ(C₁),ρ(R₂))g₂`. Hence Ψ is an isomorphism, and `Ψ r=q_(~R,~C)`.

The equivalence relations are uniquely determined by the kernel: q̂ is onto, so for any two refined rows one may choose source elements with the same refined column and group coordinate; their quotient values agree exactly when those rows are merged. The dual test recovers column merges. Therefore kernel inclusion corresponds exactly to coarsening the row and column partitions, proving the lattice claim. □

## 4. Example and limits

For the 68-source, `|R|=2`, `|C|=3`, its actual actor has 2 rows and2 columns, and one actual column has two refined columns. Thus the formula gives `Bell(1)²·Bell(1)·Bell(2)=2`, the two quotients D₈ and D₁₂ independently identified in `frontier-20261028-quotient68-pure-cs-quotients-v1.md`, SHA `8494ddd4f4091f3ef446018536c2273c77961f4e24fa1cbba310895a62135532`.

The classification concerns pure CS quotients and their kernels, not arbitrary non-pure homomorphisms, unknown original source hypotheses, or canonical band injectivity. It uses the full onto-ness and cellwise group-isomorphism proof of the named predecessor, and all results remain same-author candidates pending independent mathematical review and novelty clearance.
