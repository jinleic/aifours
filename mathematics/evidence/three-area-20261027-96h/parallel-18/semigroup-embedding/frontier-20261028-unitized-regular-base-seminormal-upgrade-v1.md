# Unitized regular-band Rees lifts admit seminormal physical hosts

**NEW AUTHOR WRITTEN CANDIDATE with exact finite check; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 20:09:19 PDT 2026**. This is an additive target-band strengthening of `frontier-20261028-adjoined-identity-band-rees-theorem-v1.md`, SHA `72e2bf6e7679405eaad15d1f95fe59d55bd71f8ca542ff8f541e42cce5e75295`. It invokes the classical regular-band left/right decomposition at an explicit scope, and does not assert that the printed book's product convention or all-source problem has been paid.

## 1. Exact abstract band lemma

Let B be ANY globally regular band and `K={p∈B: bpb=b for all b∈B}`. Assume K≠∅. Adjoin a NEW identity1 to B. Let J,M be nonempty row/column sets, each equipped with a tag in a common set Ω. Choose any Rees sandwich H satisfying

- `H_(m,j)=1` if tag(m)=tag(j);
- `H_(m,j)∈K` if tag(m)≠tag(j).

Inside the full Rees semigroup over B^1, let T consist of all B-middle cells and only those 1-middle cells whose row and column tags agree. The closure/idempotence proof in the predecessor applies verbatim: a product with B-middle or off-diagonal H has B-middle; if both middles and the connecting H are1, the output's tags align. Thus T is a band.

**Lemma.** T satisfies the seminormal identity

`x y z w x = x y z x z w x`.                              (SN)

This lemma is about arbitrary index/tag sets and arbitrary off-diagonal K choices; no P-pattern or finiteness restriction is used.

## 2. Proof using both regular-band projections

By Kimura's classical decomposition, B embeds into a product of a left regular band L (`xyx=xy`) and a right regular band R (`xyx=yx`); see the source and exact import in `frontier-20261028-all-cs-globally-regular-band-obstruction-v1.md` §3. Adjoin new identities to L and R, and send the new identity of B^1 to their pair. This extends the embedding `B^1↪L^1×R^1`.

If k∈K and b∈B, `b k b=b`. In the L projection, left regularity makes `b k b=b k`, so k acts as a RIGHT identity on every B-image element. In the R projection, right regularity makes `b k b=k b`, so k acts as a LEFT identity on every B-image element. The formal1 has both properties.

Take arbitrary `x,y,z,w∈T`, with respective B^1 middle values a,b,c,d. Denote the connecting sandwiches in their products by H_xy, H_yz, H_zw, H_wx, H_zx and H_xz. Put

`P=a H_xy b H_yz c`,       `S=c H_zw d H_wx a`.

The two middle values in (SN) are

`L=P S`,       `R=P H_zx a H_xz S`,

because c²=c in B^1. Both Rees words have the same outer row/column, so it suffices to show L=R in B^1.

**Left projection.** If P∈B, the adjacent H_zx,H_xz are K elements or1 and act as right identities. Also `P a=P` in L^1: P begins with a, so this is `a v a=a v`; it is immediate if a=1. Thus the projections of R and PS agree. If P=1, every factor `a,H_xy,b,H_yz,c` is1 because B is an ideal in B^1. In particular x,y,z are aligned 1-middle cells, and the diagonal-H rule forces their tags to agree along x→y→z. Hence H_zx=H_xz=1, so L=R already in B^1.

**Right projection.** If S∈B, H_xz and H_zx act as left identities on S. Also `a S=S` in R^1: S ends with a, so this is `a v a=v a`; it is immediate if a=1. The projections of R and PS agree. If S=1, every factor `c,H_zw,d,H_wx,a` is1; z,w,x are aligned 1-middle cells with matching tags, so again H_zx=H_xz=1 and L=R in B^1.

Thus both projections agree, and the B^1 embedding is injective. This proves (SN). The two projections need not be preserved by any group action; they are used only on static band products.

## 3. Consequence for the predecessor's ACTUAL q host

For a nonunit P matrix satisfying the predecessor's weak-E characterization, all its off-diagonal H values lie in K and all equal-tag entries are the formal1. The predecessor's T is therefore seminormal by §2. Its target `T^G` and the rectangular factor in the pure onto-CS actor pushforward are seminormal, since identities are preserved under products and rectangular bands satisfy (SN). Hence the explicit natural-actor host and, under the named WRITTEN actor pushforward, its faithful ACTUAL-q host both have seminormal band parts.

If all P entries are the new source identity and K is empty, the predecessor's separate evaluation band is a rectangular band times B^1. B^1 is globally regular, hence seminormal, so this branch also has a seminormal band target without requiring z∈K.

Accordingly, every regular weak-E locally-r source in the FULL REES family over `(B⋊G)^1` from the predecessor has the stronger seminormal physical-band host. This is exactly that family, not an assertion about arbitrary original sources. Whether this physical product exactly matches the printed problem's product convention remains a separate D1–D4 question.

## 4. Exact checks and remaining limits

`frontier-20261028-unitized-evaluation-seminormal-checker-v1.py`, SHA `af65cd23f310fe6623282efc16b53b9f75dbb6e619a55b488959cb43ef9e9cc8`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 20:09:19 PDT 2026**, exit0. Its nonrectangular4-element regular band has a two-element K class and nontrivial C2 action; the corresponding T has72 elements. It directly checks ALL72⁴=26,873,856 seminormal substitutions and all72³ associativity substitutions. The predecessor's separate102-source checker covers the complete faithful-host and actual-q computations; this note does not re-run it.

The larger204-element predecessor T also had 2,996,352 selected substitutions with unit-middle x,z and distinct tags checked without finding a violation; that bounded result is NOT used as proof and does not cover all204⁴ substitutions. The general lemma is the §2 written argument with the named Kimura import. No equivalence of seminormal and locally regular varieties, independent/cross-vendor/formal review, all-source embedding or novelty is claimed.
