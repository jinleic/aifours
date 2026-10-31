# The one-sided quotient maps are opposite Green covers

**Status: NEW AUTHOR WRITTEN GENERAL LEMMA and exact finite diagnostic; UNREVIEWED / UNADOPTED.** This identifies a precise representation interface for the remaining one-sided original problem. It does not make multiplication descend to an ordinary action of the locally-inverse quotient, or construct its general physical host.

## 1. A pure R-kernel quotient is an L-cover

Let `π:S→T` be an onto homomorphism of regular semigroups, idempotent-pure, and with `kerπ⊆R_S`. Then for every idempotent e∈S, the restriction

`π|L_e : L_e→L_(π(e))`

is bijective. Here this property is called an **L-cover**, with the displayed definition fixing the terminology. The dual assertion holds for an onto pure map with kernel contained in L: it is an R-cover.

Injectivity: if a,b∈L_e and π(a)=π(b), then kerπ⊆R makes a H b. Choose a'∈V(a). We have `aa' kerπ ba'`; the first member is idempotent, so purity makes ba' idempotent as well. Since a L b, RIGHT multiplication by a' gives `aa' L ba'`; the kernel R-containment makes them H-related, hence equal. Also b L a gives b=za for some z∈S¹, so `ba'a=zaa'a=za=b`. Multiplying `ba'=aa'` on the right by a now gives b=a.

Surjectivity: let t∈L_(π(e)). Choose an inverse v of t, and put `t'=π(e)v`. Since tπ(e)=t and π(e),vt are L-related idempotents, `π(e)vt=π(e)`; hence `t't=π(e)` and t' is a mutual inverse of t. Choose lifts s,s'∈S with π(s)=t, π(s')=t'. Then `p=s's` is idempotent by purity and has the same π-image as e. The R-kernel hypothesis gives p R e; for those idempotents `pe=e`. Set a=se. We have `π(a)=tπ(e)=t`, a∈Se, and `s'a=s'se=pe=e`, so a L e. This proves onto-ness and the lemma. □

## 2. Original one-sided quotient application

For an original regular weakly-E locally-r S, the fresh kernel theorem `frontier-20261028-original-one-sided-subdirect-theorem-v1.md`, SHA `5bb5ecb15691e4c953eb6bc877af8c7a98e1444bebca9188da3bce89c42504b5`, gives `χ_L⊆R`, `χ_R⊆L`. Both congruences lie inside the pure least-CS kernel, so their quotient maps are idempotent-pure. Therefore

`S→S/χ_L` is an L-cover, and `S→S/χ_R` an R-cover.

If the original S has RRB local idempotent bands, χ_R is equality and its least locally-inverse quotient is χ_L; hence it is an L-cover onto a weakly-E locally-inverse source with right-zero idempotent fibres. The dual local-LRB case is an R-cover with left-zero idempotent fibres. This complements the rectangular-coextension theorem, rather than asserting a direct semidirect-product realization.

## 3. An explicit obstruction to a naive ordinary quotient action

The pinned S68 has χ_L-quotient60, and its distinct same-χ_L pair37,61 has left multiplication tables differing at source indices24,…,31 and52,…,59. Thus choosing a representative of a quotient element does **not** define a well-defined left action of that quotient on all of S68 by ordinary source multiplication. The right tables differ as well. In particular the L-cover property alone does not justify importing a global étale-action representation that assumes quotient classes have identical translations.

`frontier-20261028-quotient68-green-cover-checker-v1.py`, SHA `49fc66b509716d242d378821f51fca2d7d34672825ca1efc7afef645110bf677`, ran in the Python eval kernel before Wed Oct 28 23:45:08 PDT 2026. It reconstructs χ_L and the60-element quotient, checks purity and R-containment, and directly verifies all34 idempotent L-class restrictions are bijective; the source has13 distinct L-classes and the quotient11. It also checks the exact16 translation disagreements of the named same-quotient pair. Its data source is `frontier-20261028-quotient68-faithful-host-data-v1.json`, SHA `64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf`. This is a finite failure of one proposed ordinary action, not an obstruction to the actual SN host (which is explicitly faithful). The exact unresolved task is to construct the correct partial/contextual representation of these Green covers, or another valid band cocycle, not to ignore the representative dependence. All statements remain same-author unreviewed; no formal proof, novelty or full Q1 result is claimed.
