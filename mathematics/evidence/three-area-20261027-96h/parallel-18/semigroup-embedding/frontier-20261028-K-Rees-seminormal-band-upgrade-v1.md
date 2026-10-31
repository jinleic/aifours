# K-sandwich Rees bands over regular bands are seminormal

**NEW AUTHOR WRITTEN TARGET-SCOPE UPGRADE with exact finite check; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 20:11:50 PDT 2026**. This strengthens the band target for the globally-regular-base portion of `frontier-20261028-regular-band-base-rees-theorem-v1.md`, SHA `5c883d3fb81b68af93a9848b3fc0c58acb19766c169375787c18bff0cea4e8aa`. It does NOT extend the conclusion to locally-regular-but-globally-nonregular base B or equate physical and printed products.

## Exact lemma

Let B be a globally regular band, `K(B)={p: bpb=b for every b∈B}`, and H any full Rees sandwich matrix over K(B). Then the full Rees band `T=M[B;J,M;H]` is seminormal:

`x y z w x = x y z x z w x`.

T is a band because every H value p satisfies b p b=b. By the named Kimura decomposition, B embeds into a product of a left regular band L and a right regular band R. For p∈K and b∈B, the identity bpb=b gives `b p=b` in L (using xyx=xy), and `p b=b` in R (using xyx=yx).

For x,y,z,w∈T, the two Rees words have the same outer row and column. Their middle values are the corresponding base middle values with H entries interspersed. In the L projection, scanning from the FIRST base middle b∈B removes every later H, since each acts as a right identity on the current B element. In the R projection, scanning from the LAST base middle b∈B removes every earlier H, since each acts as a left identity. Thus both projections reduce the two middles to the respective projections of the ordinary B words `a b c d a` and `a b c a c d a`. Every regular band is seminormal (equivalently, both left and right regular projections satisfy the identity), so these agree. The embedding of B in L×R is injective; hence the T middles agree. No commutativity, K singleton, row normalization or finite size is assumed.

## Consequence for the Rees source family

In the predecessor's theorem, if its base B is globally regular and all P components lie in K(B), its group-indexed evaluation T has all H∈K. Thus T and T^G are seminormal by the lemma. Its physical host over the natural CS actor, and under the named pure onto-actor pushforward its host over ACTUAL q_τ, have seminormal band parts; the rectangular factor in the pushforward preserves the identity. Source regularity/WEU/local-r and the canonical-q dependency remain exactly as in the predecessor.

This is not a seminormal claim for the stronger predecessor `frontier-20261028-local-band-base-rees-theorem-v1.md`, SHA `65c9a9cdaa2dcbbb72824e592f8a969fe8f648cc059b533c2d611e86fea49b22`, when its base B is only locally regular. No equivalence between local regularity and seminormality is asserted.

## Exact finite check

`frontier-20261028-regular-base-Rees-seminormal-checker-v1.py`, SHA `b6ee1b1b58b1751d5af569b420b3e329d0e5231755cae3a532445a7d71205da2`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 20:11:50 PDT 2026**, exit0. Its base is a nonrectangular4-element regular band with two K elements; the group-indexed Rees band T has64 elements. It checks the band laws and EVERY 64⁴=16,777,216 seminormal substitution.

This finite check is same-author. The general proof relies on the named classical Kimura decomposition and elementary band identities; it is not inferred from the sample. No independent review, formal proof, novelty, full-original result, or printed-product equivalence is claimed.
