# Original sources are rectangular-band coextensions of locally inverse sources

**Status: NEW AUTHOR WRITTEN STRUCTURAL CONSEQUENCE; UNREVIEWED / UNADOPTED.** This uses the fresh universal comparable-reflection and local Green-containment proofs. It is not a proof that every such coextension embeds in the printed/physical target, and no novelty is asserted.

Let S be a regular weakly-E locally r-orthodox original source. Let χ_L,χ_R be its least local LRB/RRB congruences and χ=χ_L∨χ_R its least locally-inverse congruence. Then:

1. `S/χ` is regular, weakly-E and locally inverse; the congruence χ is **over rectangular bands**: every χ-class containing an idempotent is a rectangular band.
2. χ_L is over **right-zero bands**, and χ_R is over **left-zero bands**.
3. If S's local idempotent bands are RRB, χ_R is equality and χ=χ_L, so S is a right-zero-band coextension of a weakly-E locally-inverse quotient. Dually, local LRB sources are left-zero-band coextensions.

Proof. The fresh source-class bridge gives a pure least-CS congruence ν, and all three kernels are contained in ν. Thus a χ-class containing an idempotent consists entirely of source idempotents, because every member has the same idempotent ν-image. It is a subsemigroup, since its quotient class is idempotent, and hence a band. For x,y in such a class, xyx is an idempotent in the same χ-class and `xyx≤x`. The fresh theorem `frontier-20261028-original-universal-comparable-separation-v1.md`, SHA `91cfce68da383e3d47f66f4b37a2cedc509172007dc1dd4ba6b8503bd5763bce`, §1 proves χ never collapses distinct comparable idempotents, so xyx=x. This is the rectangular-band law, proving1 (the quotient source properties were proved in the least-LI packet).

The same saturation makes each idempotent χ_L-class a band, while the Green theorem `χ_L⊆R` makes every two members R-related idempotents. Thus `xy=y` for every x,y in that class, a right-zero band. The χ_R argument is dual. If the relevant local one-sided identity already holds, its generating congruence is equality, and3 follows. □

The χ_L/χ_R subdirect decomposition and identity-context proof are in `frontier-20261028-original-one-sided-subdirect-theorem-v1.md`, SHA `5bb5ecb15691e4c953eb6bc877af8c7a98e1444bebca9188da3bce89c42504b5`; the least-LI quotient/purity proof is `frontier-20261028-localinverse-residual-kernel-v1.md`, SHA `1a98319b9cea8e65116cebc6c2876c6b5966ceb2c560b85518ef2228a116ca90`. These are the exact named proof dependencies and require independent review. The published locally-inverse embedding theorem is not needed for the **rectangular-fibre structural assertion**: it uses only §1 of the comparable packet, not its physical-host subsections.

For S68, χ has a60-element locally-inverse quotient and equals χ_L, with nontrivial right-zero idempotent fibres; χ_R is equality. Its separate all-actor obstruction rules out any globally regular-band host, while its eight-element SN-band/refined-actor host is faithful. Therefore 'right-zero-band coextension' does NOT mean a right-zero or even globally regular band suffices as the host's band factor. That inference would contradict the explicit source. The remaining original task is a genuinely twisted seminormal-band realization of the one-sided coextensions, not a mere concatenation of rectangular fibre labels.

All claims remain same-author written support pending independent source, proof and finite-witness review; no formal verification or full Q1 result is claimed.
