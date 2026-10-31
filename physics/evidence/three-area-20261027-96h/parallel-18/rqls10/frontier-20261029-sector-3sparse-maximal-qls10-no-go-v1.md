# A maximal 1RQLS10 cannot be three-sparse inside two five-dimensional sectors

**WRITTEN + FINITE-CONTROL AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:38:36 PDT 2026**. This is a new original-order obstruction beyond the additive/XOR sector pattern. It is NOT a general QLS10 no-go.

## Theorem

Suppose Q is a 1-resolvable QLS10 with **100 distinct rays**. Then the following two properties cannot both hold:

1. There is an orthogonal decomposition `C10=H0 direct_sum H1`, `dim H0=dim H1=5`, such that EVERY cell ray lies entirely in one of the two sectors. Sector choices may have an arbitrary incidence pattern; no additive or tensor-product pattern is assumed.
2. In the common orthonormal basis formed by SOME ROW of Q, EVERY cell vector has support size at most3.

Because each ray in the chosen row lies in a sector, this row basis consists of five vectors from H0 and five from H1. The statement is invariant under global unitary, cell phases, and row/column permutations. It does not rule out sector-decomposable solutions that require support≥4 in every row basis, nor globally 3-sparse arrays in some unrelated basis that is not a row basis.

## 1. A 5D support lemma

Let B be any ONB of C5 whose vectors, in a fixed coordinate basis, all have support size 2 or3. Then B contains an orthogonal pair supported on the SAME two coordinate directions.

First suppose every vector has support exactly3. Two different supports cannot intersect in exactly one coordinate: their inner product would consist of a single nonzero term. Their complements are 2-subsets of {1,...,5} that are pairwise intersecting. Any pairwise-intersecting family of edges is either a star or contained in the three edges of a triangle. A star would omit a common coordinate in all five vectors, impossible for an ONB. In the triangle case, the two coordinates outside the triangle occur in every support. Each triangle coordinate appears only in vectors whose complement is the opposite triangle edge. A coordinate cannot occur in just one unitary column: row normalization would make that single entry modulus1, contradicting that column's support3. Thus each opposite edge has multiplicity at least2, requiring at least6 vectors, contradiction.

Now suppose B contains a support-two ray x on coordinates {i,j}. Let u be its unique orthogonal ray in that plane. Any other basis vector intersecting {i,j} must have both coordinates nonzero; its projection to this plane is a nonzero multiple of u. If one such vector has no outside coordinate, it is the required support-two partner. Otherwise each has one extra coordinate k. Two such vectors with DIFFERENT extra coordinates have nonzero inner product from their u-components, impossible. All share one k, and Parseval plus orthogonality forces exactly two of them; together with x they form an ONB on the coordinate triple {i,j,k}. The remaining two basis vectors lie in the two complementary coordinates, and since support-one is excluded, they form the required same-plane support-two pair.

The same argument shows that in any 5D ONB with support≤3, at most ONE support-two ray can lack its same-plane support-two partner: its two support-three companions isolate a coordinate triple, leaving only a two-dimensional complement whose support-two rays are paired.

## 2. Context counting contradiction

Choose the row in hypothesis 2 as the coordinate basis. Consider one 5D sector. Exactly five first-row cells are its five singleton coordinate rays. Maximality makes every other cell nonparallel to those five, hence forbids any further support-one ray. Every global row, column or resolution transversal is an ONB of C10 and contains exactly five rays in this sector, forming a 5D ONB.

There are 30 contexts. The distinguished row contains all five singleton rays. Of the other29 contexts, exactly ten contain a singleton from this sector: its five first-row cells each occur in one distinct column and one distinct transversal, and no two first-row cells can lie in the same column or transversal. Thus **19** sector bases contain no support-one ray. By the lemma, each of these19 bases contains at least two cells forming a same-plane support-two pair.

Let M be the number of support-two CELLS in this sector. A cell x can have a same-plane partner in at most ONE of its three contexts: the partner ray is unique, and 100-ray maximality makes it the same cell each time, but any two of x's row, column and transversal meet only at x. The 19 no-singleton contexts therefore require at least `2*19=38` distinct support-two cells, so `M>=38`.

Every support-two cell belongs to three contexts and, by the same uniqueness argument, is UNPAIRED in at least two of them. By the lemma's final paragraph, each sector basis contains at most one unpaired support-two cell. No support-two cell belongs to the distinguished row, so there are at most29 possible unpaired incidences. Hence `2M<=29`, contradicting `M>=38`.

This contradiction applies to either sector alone. It uses the actual 30 basis contexts, their Latin incidences and pairwise nonparallel rays; it does not rely on a numerical search or a classical colorization.

## Evidence and boundary

The 5D all-support-three combinatorial step is also checked independently as a finite control by `frontier-20261029-support3-five-control-v1.py` SHA **37fb07df6c619c60b920bb75f402e43cf895e2a0a732cec28f3b858bbc90feaf**, result SHA **6c37464e9cee95a16129aeee344ce8105cdeb0a84f9fe7288e4120ac9f8f65a6**: among2002 multisets of five 3-subsets, 330 have no singleton intersection and NONE has all coordinate degrees at least2. The written star/triangle proof above establishes the lemma without this finite control.

The support lemma, sector context counts and uniqueness/pairwise-context-intersection argument require independent full review. A 100-ray 1RQLS10 with no 5+5 sector decomposition, or with some cell of support at least4 relative to every row basis, remains outside this result.
