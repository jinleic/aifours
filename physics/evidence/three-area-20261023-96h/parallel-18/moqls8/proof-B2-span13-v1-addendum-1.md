# B2 span13 v1 — explicit one-channel row classes, additive clarification1

Apply after immutable `proof-B2-span13-v1.md`. This makes its §4 ONE-CHANNEL invocation explicit; no assertion or bound changes and the full conditional assembly remains untouched.

At the final one-channel case, put beta={b,b-perp}. Let:

- k be the number of rows containing mixed vectors in span(b,c). Such a row has exactly two mixed cells forming an ONB of that two-space, and one B-pure b-perp cell.
- m_beta be the number of NONMIXED rows whose two B-vectors form beta.
- m_alpha be the number of NONMIXED rows of any other B-ray-pair alpha. At least one alpha exists from the two different actual B-axis bases.

These are disjoint row sets and

    8=k+m_beta+sum_alpha m_alpha.

For EACH other square separately, the pure-B class spans have lower dimensions m_beta+k and m_alpha. Their mutual orthogonality and the total8force equality. Each alpha's two ray-occurrence matchings are therefore ONBs of an m_alpha-space. With FOUR other squares and TWO distinct row/column-forced zero positions in each transition row, the supports are nonempty and disjoint on m_alpha-2 places, so

    4<=m_alpha-2, hence m_alpha>=6.

Mixed-cell vectors of each other square lie in its k-space W_s obtained by removing the pure-b m_beta-space from the beta class span. Decompose the mixed two-regular board by its orthonormal ray-pairs in span(b,c). The same dimension saturation makes the two occurrence matchings of every nonempty mixed class bases of an ell-space. The identical FOUR-support/TWO-zero argument gives ell>=6. Hence k>=6.

The contradiction that fires is therefore

    8>=k+m_alpha>=6+6=12,

using one actual non-beta PURE-B row class and the disjoint set of MIXED rows. It is not a sum of overlapping mass counts, not a joint-cell assertion and not a claim that projected B-parts were orthogonal. This is exactly §3 of the pinned low-span rigidity candidate, specialized to n8,t5.
