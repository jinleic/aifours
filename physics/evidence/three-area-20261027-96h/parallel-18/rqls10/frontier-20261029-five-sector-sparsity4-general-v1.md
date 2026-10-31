# A five-dimensional sector of a maximal resolved QLS must contain a four-sparse ray

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:39:49 PDT 2026**. This strictly strengthens `frontier-20261029-sector-3sparse-maximal-qls10-no-go-v1.md` SHA **6725533d190ccaedb4a9388f9b10e7502007b3659ec9abc85cc9d66eb82ef195**: no row-basis assumption, no equal-sector assumption, and no sparsity condition on the complementary sector.

## Theorem

Let Q be a t-resolvable QLS of order N>=7, t>=1, with maximal cardinality N². Suppose there is a 5-dimensional subspace H such that every cell ray lies in H OR in H-perpendicular; sector membership may have any pattern. Then for EVERY orthonormal basis of H, at least one cell ray in H has support size at least4 in that basis. No assumption is made on the support of rays in H-perpendicular.

For the original N=10 target, this means any maximal 1RQLS10 with a 5+5 sector decomposition must have a 4- or 5-supported ray in EACH sector relative to EVERY basis of that sector. In particular there is no such maximal array globally 3-sparse in any sector-adapted basis, whether or not that basis occurs as a row. The theorem does not say every QLS10 admits such a sector decomposition.

## Proof

Suppose instead all H-rays are support≤3 in some basis of H. Put `s=t+2`. There are `sN` row, column and resolution contexts. Since every global context is an ONB and every ray lies in H or H-perpendicular, each context contributes an ONB of five H-rays. Each cell appears in exactly s contexts; any two of its contexts share only that cell, by the Latin and resolution-orthogonality conditions.

Maximality makes all N² cell rays distinct. There are at most five support-one H-rays, so at most five such cells. Each occurs in s contexts; hence at most `5s` contexts contain a support-one H-ray. At least `s(N-5)` contexts have no support-one H-ray.

The 5D support lemma proved in the predecessor says: an ONB of C5 with all supports of size2 or3 contains a same-coordinate-plane orthogonal pair of support-two rays; furthermore any 5D ONB of support≤3 has at most one support-two ray that lacks such a partner in that ONB. The lemma remains valid with arbitrary complex amplitudes, and its support-three combinatorics also have an independently checked finite control in the predecessor.

Let M be the number of support-two cells in H. A support-two ray has a UNIQUE orthogonal partner in its coordinate plane. Because all cell rays are distinct and any two contexts containing the cell share no other cell, it can have that partner in at most ONE of its s contexts. Each no-singleton H-basis contributes at least two distinct paired support-two cells. Thus

`M >= 2s(N-5)`.                                                      (1)

Every support-two cell is unpaired in at least s-1 contexts. At most one unpaired support-two cell occurs in any H-basis, so

`(s-1) M <= sN`.                                                      (2)

Combining (1)–(2) requires `2(s-1)(N-5)<=N`. But N>=7 and s>=3 give `2(s-1)(N-5)>=4(N-5)>N`, a contradiction.

## Boundary

This theorem applies to ANY sector incidence pattern and ANY fixed t mutually orthogonal resolution families. It is an obstruction only to the combination of maximality, an exact 5D orthogonal sector split and 3-sparsity inside that sector. A mixed-sector ray, an arbitrary non-sector array, or a sector whose rays require support≥4 is not excluded. The written support lemma, context counting and maximality use need independent review; no novelty or formal-verification claim is made.
