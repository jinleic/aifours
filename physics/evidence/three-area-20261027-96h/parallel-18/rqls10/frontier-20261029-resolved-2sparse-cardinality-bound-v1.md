# Sparse-support cardinality bound for any resolved quantum Latin square

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:16:18 PDT 2026**. This is an unrestricted-resolution structural bound, not a general 1RQLS10 no-go.

## Theorem

Let Q be a `t`-resolvable QLS of order n, with t>=1, and suppose that in SOME common orthonormal basis every cell vector has support size at most2. Then the number of distinct rays satisfies

`cardinality(Q) <= n + floor((n²-n)/(t+2))`.                         (1)

In particular every 1RQLS10 that is globally 2-sparse in some basis has at most **40 rays**. Therefore any 100-ray 1RQLS10, if it exists, must contain a vector with support at least3 in EVERY common orthonormal basis. This applies to ANY resolution Latin square, not only the cyclic one.

## Proof

The contexts are the n rows, n columns and n transversal bases in each of t orthogonal resolutions. Each cell belongs to exactly `t+2` contexts. Any two distinct such contexts containing the same cell intersect only at that cell: two rows or columns are disjoint; row/column and transversal intersections are singletons; two different resolutions' transversals intersect in exactly one cell by definition.

Suppose a cell x has a vector with exact support `{i,j}`. In any ONB context containing x, a 2-sparse vector that is orthogonal to x is either disjoint from `{i,j}` or has the SAME support `{i,j}`; an overlap of exactly one nonzero coordinate cannot give zero inner product. A support-one vector on i or j is not orthogonal to x. Since an ONB spans both coordinates, exactly one other vector in that context lies in this two-dimensional support plane. Its ray is the UNIQUE orthogonal complement of x in that plane.

The partner cells of x in its `t+2` contexts are pairwise distinct because those contexts meet only at x, but all carry the same partner ray. Therefore every support-two ray that occurs in Q has multiplicity at least `t+2`: apply the preceding argument to any cell carrying its orthogonal-partner ray. Let h<=n be the number of distinct support-one rays and m>=h the number of cells carrying them. At most `(n²-m)/(t+2)` distinct support-two rays remain, so

`cardinality <= h+(n²-m)/(t+2) <= h+(n²-h)/(t+2) <= n+(n²-n)/(t+2)`.

Taking the integer floor proves (1). Multiplicities are projective; phases do not affect the argument.

## Consequences and boundary

For t=1,n=10 this gives <=40 rays, strictly excluding the maximal target under the global support-two hypothesis. More locally, in any 2-sparse 1RQLS every support-two ray and its planar orthogonal partner appear in at least three distinct cells. The statement is compatible with the explicit 100-ray QLS10 in `frontier-20261029-maximal-separable-sector-qls10-no-transversal-v1.md` SHA **f689af59576f63d0dd4f0e9afc5f811e54009215b9748ff49d9471d753ee0b63**, which is not resolvable and is not globally 2-sparse in its displayed basis.

This theorem does not show that all QLS10s admit a 2-sparse basis; they need not. It leaves unrestricted 1RQLS10 open and requires independent written review.
