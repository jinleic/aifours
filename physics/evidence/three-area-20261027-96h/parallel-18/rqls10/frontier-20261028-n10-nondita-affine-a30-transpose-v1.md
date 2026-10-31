# The transposed A.30 family also has no Fourier transversal

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:26:50 PDT 2026**. Conditional on `frontier-20261028-n10-nondita-affine-a30-allphase-no-transversal-v1.md` SHA **586014909b52ba5854a41979be9ac900295da4914a2fbdae70af1ad31dc2cf03**, the transpose of its literal K(a,b) also has NO cyclic-Fourier-product transversal for EVERY unit a,b and every source-row order, including repeated rays.

Indeed the all-source-orders no-transversal property is invariant under transpose, as shown in `frontier-20261028-transpose-duality-full-dita-8-10-v1.md` SHA **292be10e699510426a60db376d168b47e9fe063f962cc837bde6993267758dc1**: a transversal of R K^T with chosen-column permutation P transposes to a transversal for `P^T K R^T`, contradicting the original all-row-order theorem.

For generic unit a,b, K and K^T are monomially inequivalent: the exact ratio census in the underlying packet records **zero** row pairs with 5+5 ratio multiplicities for K, but **two** such row pairs for K^T, namely the original column pairs (6,7) and (8,9). Row-pair ratio multiplicity counts are invariant under row/column permutations and gauges. The same census shows that generically both K and K^T lie outside the 2×5 and 5×2 Diţă classes. Special parameter coincidences are not covered by the inequivalence claim, although the no-transversal claim covers them.

This is a written corollary of unreviewed computer-assisted premises, not a general even-order or unrestricted QLS10 no-go; it requires independent review together with those premises.
