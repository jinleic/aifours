# Lemmas used by the moqls7-maximum lane

This file is a late, explicit documentation correction following the static reviews. It did not exist in the
original review snapshot; the old references to it are not evidence that it had been written before those runs.
No frozen encoder or old evidence is changed. Definitions and Lemma 10 are from the pinned Ball–Simoens
arXiv:2607.12933v2, layout LF90–148 and LF178–192. The theorem packages retain their own explicit trust boundaries.

## C0. Classicality, straightening and rays
A QLS is classical iff, after entry phases, all entries lie in one ONB. Row/column permutations do not alter its
ray set. Each ONB row supplies seven distinct rays; if there are exactly seven in total every entry is parallel to
one row-basis vector, and conversely a classical QLS has exactly seven. Independent global unitaries are allowed
on the individual squares in a set, so the set is classical iff all its members are classical. These unitaries
straighten each classical member in place to a Latin square of standard-basis labels; no independent reindexing of
cells is required.

## C1. Orthogonality to a classical member
For a classical L, the product-vector inner product is

    <psi_p tensor |L(p)>, psi_q tensor |L(q)>> = <psi_p,psi_q> [L(p)=L(q)].

Hence a quantum square is orthogonal to L iff its seven entries on each L-symbol line form an ONB. With two
classical members, K1 is exactly the non-classical ONB-assignment problem on their 4-net. The ONB-assignment
problem is symmetric in the four classes; net isomorphism is sufficient even if not every class permutation is a
source set-isotopy. This is an existence transport, not a claim about the narrower isotopy group.

## W. Fresh three-square support bound
Independently straighten the first row of each square to e_0,...,e_6. At an off-first-row cell (i,j), column
orthogonality excludes coordinate j from every support. For any two squares, compare their product at (i,j) to
its first-row product e_k tensor e_k. Orthogonality gives

    <e_k,psi_a(i,j)> <e_k,psi_b(i,j)> = 0.

Their supports are therefore disjoint, for every pair a,b. Three nonempty, pairwise disjoint supports lie inside
six coordinates, so their weights sum to at most six. Each individual weight is at most four, and weight four
forces the other two to be singletons. Weight two is allowed. This is derived for three squares, not imported
from the old four-square theorem.

## K1 frame and F1–F4
Choose a net line ell as the basis. Each point outside ell lies on three other net lines meeting ell at three
distinct points: two coincident meetings would make two different net lines share two points. Orthogonality to
those three basis vectors excludes their coordinates, leaving four allowed coordinates.

For each ONB line, supports must satisfy:
- F1 nonempty, by unit norm;
- F2 no two orthogonal entries share exactly one support coordinate, since then their inner product is one
  nonzero product;
- F3 every coordinate is covered, since the line vectors form a unitary matrix;
- F4 unique coverage of coordinate k forces weight one at its covering vector: column k has one coefficient of
  modulus one, exhausting that row's norm.

These are only necessary conditions for general unitary realisation. A Boolean SAT pattern is not a vector
witness. The full K1 exclusions and seven-phase relation are in `K1-THEOREM.r3.md`.

## Lemma 10 in an arbitrary basis, with every partner preserved
Suppose every entry of a square has weight at most two in one fixed ONB. Pick a weight-two vector with support
{a,b}, and a unitary U on that two-dimensional coordinate plane sending it to a coordinate ray. Apply U to all
entries with exactly this support, leaving all other entries untouched. If another weight-at-most-two entry was
orthogonal to one of these, it had either the same support or disjoint support (a one-coordinate overlap cannot
cancel). Thus every previously zero inner product stays zero. Unit norms and the row/column ONBs remain intact,
and no support grows; at least one weight-two entry disappears. Repeating finitely many times yields a classical
square with support contained pointwise in the old support.

For tensor orthogonality with any other square, every required zero product still has its former zero factor.
Thus the same replacement preserves orthogonality to all partners simultaneously, not just one preselected
partner. Before this argument one may apply a global unitary on the chosen square alone to send any ONB B to the
standard basis; this preserves all its Gram inner products. Undoing that unitary preserves classicality and the
partner orthogonalities. Therefore the printed lemma is basis-free in precisely the sense used here.

## G4. Heavy minimal counterexamples; separate from K1 section 8
Minimise the number m of individually non-classical squares over all non-classical MOQLS(7) triples, if any exist.
The minimum exists because m is one of 1,2,3. Theorem K1 excludes m=1. A non-classical square light in any ONB
could be replaced by the preceding lemma, producing a triple with m-1 >= 1 non-classical squares, a contradiction.
Every non-classical square of a minimal triple is consequently heavy in every ONB.

Given K1, every K2 triple is minimal; after K2 is excluded, the same applies to K3. In each own-line frame the
weight of a point is its number of nonzero Gram overlaps with that line. Points on the line have weight one, so a
heavy witness lies off it. This justifies G4 in `GRAM-ENCODING.r1.md` independently of the more limited
standard-frame reduction in K1 section 8. The chronological prerequisites may not be reversed.
