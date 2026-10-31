# An exact fibre-saturation test for minimum-band hosts

**Status: NEW AUTHOR WRITTEN FINITE CRITERION; UNREVIEWED / UNADOPTED.** This is a constructive special case of the much larger finite band-optimization formula. It does not prove all finite sources embed and does not assume the printed product convention is settled.

## 1. Fixed-actor criterion

Let S be a finite semigroup, `r:S→D=M[G;I,Λ;P]` an onto idempotent-pure CS map, and d an idempotent of D. The fibre `F=r⁻¹(d)` is a band of size m. For any isomorphism-closed class V of bands, the following are equivalent:

1. S embeds in a physical V-band-by-D product with band cardinality exactly m.
2. `F∈V`, and there exist a group action `α:G→Aut(F)` and a map `b:S→F` such that:
   * `b(e)=e` for every e∈F;
   * `b(st)=b(s) α_(g_s P_(λ_s,i_t))(b(t))` for all s,t∈S;
   * if r(s)=r(t) and s≠t, then b(s)≠b(t).

Proof. In any faithful host the source F embeds into the band coordinate: all elements in F have actor d, and d's self-weight is 1. Hence every host band has at least m elements. If its size is m, the coefficient map `F→B` is a bijective band homomorphism. Conjugating the actor action and all coefficients by its inverse gives exactly condition2. Conversely condition2 gives the displayed physical source homomorphism, with injectivity for equal actors and automatic distinction for unequal actors. □

Because S and D are finite, so are F and G. One can enumerate Aut(F), every homomorphism G→Aut(F), and the finitely many assignments b:S→F satisfying the stated constraints. This decides attainability of the *fibre lower bound* and can provide a literal table or an exact finite search certificate. It may still be computationally expensive; arc consistency alone is generally not complete.

## 2. All-actor consequence and exact example

If S is regular and its actual idempotence-context quotient is CS, the unreviewed finest-actor theorem and SAME-band lifting `frontier-20261028-finest-actor-same-band-lift-v1.md`, SHA `fa8bcc7beb069fbe873380429415f9c90723420a241abd078fe206973d1d8c3c`, identify the minimum band size over all CS actors with the minimum over the finest pure actor q̂. Thus an affirmative fibre-saturation test for an idempotent q̂-fibre F proves the **global all-actor minimum m**. This implication uses the general lift theorem; the fixed-actor criterion in §1 does not.

For the pinned S68, q̂ has a fibre F of size8. The literal proof in `frontier-20261028-quotient68-unique-8band-host-v1.md`, SHA `212ff5c3e718db2fcec32fdf12e271d3a631960b09863a632a57ca781373baa1`, enumerates Aut(F), excludes one C₂ action and forces all coefficients uniquely for the other; direct product/injectivity checks give a solution. Hence the fibre lower bound8 is attained, and this particular q̂-host is unique up to the fibre relabelling. The q-actor fibre of size9, by contrast, has no saturated solution; separate arc traces and a ten-band host prove fixed-q minimum10.

Neither example gives a universal theorem that the largest fibre bound is always attained. A non-saturated fixed actor may still have a larger finite host. All source and trace evidence, the same-band lift, and the ordinary Rees interpretation remain subject to independent review; no novelty or formal proof is claimed.
