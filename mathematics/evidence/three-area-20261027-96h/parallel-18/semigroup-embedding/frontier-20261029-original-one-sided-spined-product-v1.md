# Exact spined-product decomposition of every original source

**Status: NEW AUTHOR WRITTEN GENERAL THEOREM; UNREVIEWED / UNADOPTED.** This strengthens the fresh subdirect decomposition to a complete fibre-product description and commuting congruences. It does NOT construct the still-unpaid physical hosts of the matching one-sided quotients, and is not a general Q1 solution or novelty assertion.

## 1. Statement

Let S be an original nonempty regular weakly-E locally r-orthodox semigroup. Let χ_L,χ_R be its least local-LRB/local-RRB congruences and χ=χ_L∨χ_R its least locally-inverse congruence. Put

`A=S/χ_L`, `B=S/χ_R`, `T=S/χ`,

with natural maps A→T and B→T. Then χ_L and χ_R **commute as equivalence relations**, their intersection is equality, and

`S ≅ A ×_T B = { (a,b)∈A×B : a,b have the same T-image }`.     (1)

The isomorphism is the canonical map `s↦([s]_χL,[s]_χR)`. The matching intermediate source element for any compatible pair is explicitly `s u t`, where s represents a∈A, t represents b∈B, and u is any mutual inverse of s. No global identity, finiteness or global orthodoxy is assumed.

## 2. Pure Green-kernel lemma

Let ρ be an idempotent-pure congruence on a regular semigroup U, with ρ⊆R_U. If a ρ b and u∈V(a), then

`a u b=b`, `b u a=a`.                                    (R)

For the first equality, a R b gives b=ax with x∈U¹, so aub=auax=ax=b. For the second, `au ρ bu` and au is idempotent, so bu is idempotent by purity. The two are R-related by ρ⊆R. For R-related idempotents, `(bu)(au)=au`. Multiply on the right by a:

`b u a u a = a u a = a`.

Since uau=u, the left side is bua, proving(R). The dual lemma for ρ⊆L_U is

`a u b=a`, `b u a=b`.                                    (L)

It follows by reversing products, or by applying the left-zero idempotent pair equations to ua,ub and multiplying by a.

## 3. Applicable quotient kernels and the explicit filler

The fresh local Green-containment theorem `frontier-20261028-original-one-sided-subdirect-theorem-v1.md`, SHA `5bb5ecb15691e4c953eb6bc877af8c7a98e1444bebca9188da3bce89c42504b5`, proves χ_L⊆R_S, χ_R⊆L_S and χ_L∩χ_R=equality. The exact one-sided quotient theorem gives χ=χ_L∨χ_R and shows A has localLRB bands and B localRRB bands.

Apply the Green theorem AGAIN to A: its localLRB congruence is equality, so its leastLI congruence is its localRRB congruence, namely `χ/χ_L`, contained in L_A. Similarly `χ/χ_R⊆R_B`. Both quotient congruences are idempotent-pure: the original source has a pure least-CS map η, both χ_L and χ_R are contained in kerη, and the induced A→S/kerη and B→S/kerη maps are pure. A class of χ/χ_L or χ/χ_R containing an idempotent therefore contains only idempotents. These are the exact hypotheses for the lemma in §2.

Take arbitrary a=[s]_χL∈A and b=[t]_χR∈B with the same T-image. This means s χ t. Choose u∈V(s) in S and set v=sut. In A, the two images of s,t are related by the pure L-kernel χ/χ_L; (L) gives `[v]_χL=[s]_χL=a`. In B, the images are related by the pure R-kernel χ/χ_R; (R) gives `[v]_χR=[t]_χR=b`. Thus v maps to the prescribed compatible pair.

The canonical map to the fibre product is a homomorphism. It is injective by χ_L∩χ_R=equality, and the filler proves it is onto; hence(1). The same argument shows any χ-related s,t can be linked by a χ_L step and a χ_R step (with the appropriate s u t or t u s filler). Therefore `χ=χ_Lχ_R=χ_Rχ_L`, proving permutability. □

## 4. Exact remaining scientific obligation

The two factor classes are still original: A has localLRB idempotent bands and B localRRB bands, each has a pureCS actor and maps by the opposite Green cover onto the WEU locally-inverse T. The rectangular-fibre/covers and universal comparable proofs are separately pinned. This result describes EXACTLY how the two matching one-sided problems fit together; it does not assume their hosts exist or that an ordinary quotient multiplication action is well-defined.

For S68, χ_R=equality and the decomposition is degenerate in one factor, consistent with its genuine matching R-gap. Thus this theorem does not replace the hard one-sided case by the already solved locally-inverse T. All load-bearing source-class, local quotient/Green and purity facts are fresh same-author candidates requiring independent review; no formal proof or full originalQ1/Q2 resolution is claimed.
