# A two-cell parity obstruction in powers-of-two Fourier products

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:05:49 PDT 2026**. This explains part of the all-local-order non-Butson tensor obstruction; it is not a general even-order result.

## General lemma

Let n=2^a, a>=1, let F be conjugation-stable with `Phi_n` irreducible over F, and let K be a complex Hadamard over F. If two Fourier-product cells lie in opposite-parity physical rows, use DISTINCT columns c,d, and are orthogonal, then the multiset

`{conjugate(K_(t,c))*K_(t,d): t=0,...,n-1}`

has EVEN multiplicity at every value. Indeed their row difference Delta is odd, so zeta_n^Delta is primitive. Its Gram polynomial in F[x] has degree<n and is divisible by `Phi_n(x)=1+x^(n/2)`. The coefficient at each u and u+n/2 must agree. This is true for every source-row ordering.

Consequently, if every distinct K-column ratio multiset has at least one value of ODD multiplicity, then NO orthogonal opposite-parity-row pair with distinct columns exists. Every n-cell ONB clique that meets BOTH row parities must then be one complete column: compare every clique cell with one cell from the opposite parity. This is stronger than the mere no-transversal conclusion but uses the named ratio condition.

## Exact source instance

For the explicit non-Butson/non-Diţă K8 in `frontier-20261028-t8b-generic-and-explicit-no-transversal-v1.md` SHA **bb279c42f4e76a77e9cbcbf980501af140969492d14e174fd0a98f2ea9d69ef9**, all entries lie in Q(zeta6), over which Phi8 is irreducible. Exact `frontier-20261028-t8b-column-ratio-parity-v1.py` SHA **9b9f8e0494a5864340cebf1a20e7c2525d2baf70799745a531bc5063d404b027**, result SHA **8c8e0b1d82fdfeb787ae675b8afe216e45494b8d779ff400abc14fda6d9f2561**, obtains the SAME per-pair patterns in both Q(zeta8) tensor Q(zeta6) and Q(zeta24): among28 column pairs, the sorted multiplicities are

```text
12 × (1,1,1,1,1,1,1,1)
12 × (1,1,1,1,2,2)
 4 × (1,1,3,3).
```

Every pair has an odd multiplicity. Hence for this K and ANY source-row permutation, an opposite-parity orthogonal pair must share a column, and any mixed-parity local8 ONB is a whole column. One separate exact clique-shape scan, `frontier-20261028-t8b-all-row-orders-tensor-parity-v4.cpp` SHA **bc34113b1a2b2607034f8bbb2d95b219dbcc01c4e0a561e9b29eb018e5fb44c2**, recorded 40320 row, 40320 column and 3456 four-row-by-two-column cliques, no other shapes, in 5040 normalized orders; its stdout and scope are recorded in `frontier-20261028-t8b-all-row-orders-clique-shape-observation-v1.json`. The lemma implies these rectangles use just one row parity. The independent all-order scans in `frontier-20261028-t8b-odd-tensor-all-local-orders-v1.md` SHA **6ee697a61fe0425924d59f872b14c75d6ce4118dd8e37964765052b49f7cf412** are still needed for the within-parity mod4 congruence; the independently written Bron–Kerbosch replay checked the congruence but did not separately classify shapes.


The named field irreducibility, actual source ratio transcript and all-order tensor caller require independent review. No claim is made that all Hadamards satisfy the ratio condition, that the tensor theorem holds without its within-parity input, or that arbitrary even Fourier products have no transversal.
